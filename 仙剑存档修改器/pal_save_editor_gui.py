# -*- coding: utf-8 -*-
"""仙剑98柔情版 存档修改器（GUI）
================================================================
依据《Pal存档属性分析与修改方案.md》的偏移表实现：
  属性区  0x200+0x044 起（字段步进0x0C，角色步进2）
  披挂区  0x200+0x080 起（6栏，栏步进0x0C）
  仙术区  0x37C 起（第2页+0x17C，每12字节一轮=6人x2字节，每角色32位）
  物品区  0x6C0-0xCBF（256槽，每项6字节：代码+数量+保留）；0xCC0起为状态表勿动
  金钱    0x28 起（32位小端）
功能：选择存档 -> 自动解析角色/装备/仙术/背包/金钱 -> 可视化修改 -> 备份保存
================================================================
"""
import os
import shutil
import struct
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

PAGE2 = 0x200
CHARS = ['李逍遥', '赵灵儿', '林月如', '巫后', '阿奴']
ATTRS = [('修行', 0x044), ('最大体力', 0x050), ('最大真气', 0x05C),
         ('体力', 0x068), ('真气', 0x074), ('武术', 0x0C8),
         ('灵力', 0x0D4), ('防御', 0x0E0), ('身法', 0x0EC), ('吉运', 0x0F8)]
EQUIP_SLOTS = [('头部', 0), ('披风', 1), ('衣甲', 2), ('武器', 3), ('靴子', 4), ('饰品', 5)]
ITEM_BASE = 0x6C0
ITEM_MAX = 256        # 物品区共256槽(0x6C0-0xCBF，0.RPG空背包边界+三档结构实证)；0xCC0起为场景物件/事件状态表，勿动
ITEM_ZERO_END = 10
MONEY_OFF = 0x28      # 金钱：第1页 0x28-0x2B，32位小端（palhero/CSDN 交叉确认）
SPELL_BASE = 0x17C    # 仙术区：绝对 0x37C(第2页+0x17C) 起，每12字节一轮(6人x2字节)
SPELL_MAX = 32        # 每角色法术位上限 32

# 物品名称表（234 项，0x3D-0x126；依 WORD.DAT 内置名称表，与对照表互校）
ITEM_NAMES = {
    0x3D: '观音符', 0x3E: '圣灵符', 0x3F: '金刚符', 0x40: '净衣符', 0x41: '灵心符', 0x42: '天师符',
    0x43: '风灵符', 0x44: '雷灵符', 0x45: '水灵符', 0x46: '火灵符', 0x47: '土灵符', 0x48: '舍利子',
    0x49: '玉菩提', 0x4A: '银杏子', 0x4B: '糯米', 0x4C: '糯米糕', 0x4D: '盐巴', 0x4E: '茶叶蛋',
    0x4F: '鸡蛋', 0x50: '糖葫芦', 0x51: '蜡烛', 0x52: '符纸', 0x53: '檀香', 0x54: '大蒜',
    0x55: '黑狗血', 0x56: '酒', 0x57: '雄黄', 0x58: '雄黄酒', 0x59: '九节菖蒲', 0x5A: '驱魔香',
    0x5B: '十里香', 0x5C: '水果', 0x5D: '烧肉', 0x5E: '腌肉', 0x5F: '还魂香', 0x60: '赎魂灯',
    0x61: '孟婆汤', 0x62: '天香续命露', 0x63: '止血草', 0x64: '行军丹', 0x65: '金创药', 0x66: '蟠果',
    0x67: '紫菁玉蓉膏', 0x68: '鼠儿果', 0x69: '还神丹', 0x6A: '龙涎草', 0x6B: '灵山仙芝', 0x6C: '雪莲子',
    0x6D: '天仙玉露', 0x6E: '神仙茶', 0x6F: '灵葫仙丹', 0x70: '试炼果', 0x71: '女娲石', 0x72: '八仙石',
    0x73: '蜂巢', 0x74: '尸腐肉', 0x75: '毒蛇卵', 0x76: '毒蝎卵', 0x77: '毒蟾卵', 0x78: '蜘蛛卵',
    0x79: '蜈蚣卵', 0x7A: '鹤顶红', 0x7B: '孔雀胆', 0x7C: '血海棠', 0x7D: '断肠草', 0x7E: '醍醐香',
    0x7F: '忘魂花', 0x80: '紫罂粟', 0x81: '鬼枯', 0x82: '腹蛇涎', 0x83: '蜂王蜜', 0x84: '雪蛤蟆',
    0x85: '赤蝎粉', 0x86: '化尸水', 0x87: '迷魂香', 0x88: '九阴散', 0x89: '无影毒', 0x8A: '三尸蛊',
    0x8B: '金蚕蛊', 0x8C: '幻蛊', 0x8D: '隐蛊', 0x8E: '冰蚕蛊', 0x8F: '火蚕蛊', 0x90: '食妖虫',
    0x91: '灵蛊', 0x92: '爆烈蛊', 0x93: '碧血蚕', 0x94: '蛊', 0x95: '赤血蚕', 0x96: '金蚕王',
    0x97: '引路蜂', 0x98: '傀儡虫', 0x99: '梅花镖', 0x9A: '袖里剑', 0x9B: '透骨钉', 0x9C: '雷火珠',
    0x9D: '毒龙砂', 0x9E: '吸星锁', 0x9F: '缠魂丝', 0xA0: '捆仙绳', 0xA1: '无影神针', 0xA2: '血玲珑',
    0xA3: '长鞭', 0xA4: '九截鞭', 0xA5: '金蛇鞭', 0xA6: '木剑', 0xA7: '短刀', 0xA8: '铁剑',
    0xA9: '大刀', 0xAA: '仙女剑', 0xAB: '长剑', 0xAC: '红缨刀', 0xAD: '越女剑', 0xAE: '戒刀',
    0xAF: '玄铁剑', 0xB0: '芙蓉刀', 0xB1: '柳月刀', 0xB2: '青锋剑', 0xB3: '苗刀', 0xB4: '凤鸣刀',
    0xB5: '双龙剑', 0xB6: '玉女剑', 0xB7: '金童剑', 0xB8: '龙泉剑', 0xB9: '鬼牙刀', 0xBA: '七星剑',
    0xBB: '玄冥宝刀', 0xBC: '巫月神刀', 0xBD: '磐龙剑', 0xBE: '太极剑', 0xBF: '无尘剑', 0xC0: '青蛇杖',
    0xC1: '鬼头杖', 0xC2: '冥蛇杖', 0xC3: '天蛇杖', 0xC4: '头巾', 0xC5: '青丝巾', 0xC6: '发饰',
    0xC7: '银钗', 0xC8: '翠玉金钗', 0xC9: '皮帽', 0xCA: '珍珠冠', 0xCB: '天师帽', 0xCC: '紫金冠',
    0xCD: '天蚕丝带', 0xCE: '凤凰羽毛', 0xCF: '冲天冠', 0xD0: '布袍', 0xD1: '藤甲', 0xD2: '丝衣',
    0xD3: '铁锁衣', 0xD4: '夜行衣', 0xD5: '青铜甲', 0xD6: '罗汉袍', 0xD7: '铁鳞甲', 0xD8: '天师道袍',
    0xD9: '精铁战甲', 0xDA: '金缕衣', 0xDB: '鬼针胄', 0xDC: '天蚕宝衣', 0xDD: '青龙宝甲', 0xDE: '白虎之铠',
    0xDF: '玄武战袍', 0xE0: '朱雀战衣', 0xE1: '披风', 0xE2: '护肩', 0xE3: '武士披风', 0xE4: '护心镜',
    0xE5: '霓虹羽衣', 0xE6: '菩提袈裟', 0xE7: '虎纹披风', 0xE8: '凤纹披风', 0xE9: '龙纹披风', 0xEA: '圣灵披风',
    0xEB: '草鞋', 0xEC: '木鞋', 0xED: '布靴', 0xEE: '绣花鞋', 0xEF: '铁履', 0xF0: '武僧靴',
    0xF1: '鹿皮靴', 0xF2: '疾风靴', 0xF3: '莲花靴', 0xF4: '虎皮靴', 0xF5: '龙鳞靴', 0xF6: '步云靴',
    0xF7: '魅影神靴', 0xF8: '香袋', 0xF9: '护腕', 0xFA: '铁护腕', 0xFB: '竹笛', 0xFC: '珍珠',
    0xFD: '玉镯', 0xFE: '念珠', 0xFF: '银针', 0x100: '铜镜', 0x101: '八卦镜', 0x102: '乾坤镜',
    0x103: '豹牙手环', 0x104: '圣灵珠', 0x105: '金罡珠', 0x106: '五毒珠', 0x107: '风灵珠', 0x108: '雷灵珠',
    0x109: '水灵珠', 0x10A: '火灵珠', 0x10B: '土灵珠', 0x10C: '炼蛊皿', 0x10D: '寿葫芦', 0x10E: '紫金葫芦',
    0x10F: '布包', 0x110: '桂花酒', 0x111: '紫金丹', 0x112: '玉佛珠', 0x113: '金凤凰蛋壳', 0x114: '火眼麒麟角',
    0x115: '青龙碧血玉', 0x116: '毒龙胆', 0x117: '破天锤', 0x118: '包袱', 0x119: '银杏果', 0x11A: '鲤鱼',
    0x11B: '鹿茸', 0x11C: '钓竿', 0x11D: '捕兽夹', 0x11E: '六神丹', 0x11F: '情书', 0x120: '玉佩',
    0x121: '石钥匙', 0x122: '天书', 0x123: '香蕉', 0x124: '凤纹手绢', 0x125: '手卷', 0x126: '芦苇漂',
}

# 仙术名称表（103 项，0x127-0x18D；依 WORD.DAT 内置名称表，重名按游戏内置命名加"1"）
SPELLS = {
    0x127: '梦蛇', 0x128: '气疗术', 0x129: '观音咒', 0x12A: '凝神归元', 0x12B: '元灵归心术', 0x12C: '五气朝元',
    0x12D: '还魂咒', 0x12E: '赎魂', 0x12F: '回梦', 0x130: '夺魂', 0x131: '鬼降', 0x132: '净衣咒',
    0x133: '冰心诀', 0x134: '灵血咒', 0x135: '金刚咒', 0x136: '真元护体', 0x137: '天罡战气', 0x138: '风咒',
    0x139: '旋风咒', 0x13A: '风卷残云', 0x13B: '风神', 0x13C: '雷咒', 0x13D: '五雷咒', 0x13E: '天雷破',
    0x13F: '狂雷', 0x140: '雷神', 0x141: '冰咒', 0x142: '玄冰咒', 0x143: '风雪冰天', 0x144: '风雪冰天1',
    0x145: '雪妖', 0x146: '火术', 0x147: '炎咒', 0x148: '三昧真火', 0x149: '炎杀咒', 0x14A: '炼狱真火',
    0x14B: '火龙', 0x14C: '土咒', 0x14D: '飞岩术', 0x14E: '地裂天崩', 0x14F: '泰山压顶', 0x150: '山神',
    0x151: '气剑指', 0x152: '弦月斩', 0x153: '弦月斩1', 0x154: '一阳指', 0x155: '七诀剑气', 0x156: '斩龙诀',
    0x157: '暗器', 0x158: '铜钱镖', 0x159: '御剑术', 0x15A: '万剑诀', 0x15B: '心剑合一', 0x15C: '天剑',
    0x15D: '天师符法', 0x15E: '斩魔刀', 0x15F: '武神', 0x160: '三尸咒', 0x161: '御蜂术', 0x162: '万蚁蚀象',
    0x163: '天女散花', 0x164: '剑气', 0x165: '炼狱爪', 0x166: '血魔神功', 0x167: '狂风术', 0x168: '鞭击',
    0x169: '御剑伏魔', 0x16A: '御剑伏魔1', 0x16B: '剑神', 0x16C: '风灵符法', 0x16D: '雷灵符法', 0x16E: '水灵符法',
    0x16F: '火灵符法', 0x170: '土灵符法', 0x171: '气吞天下', 0x172: '酒神', 0x173: '瘴气', 0x174: '万蛊蚀天',
    0x175: '毒吞天下', 0x176: '爆炸蛊', 0x177: '镇天鼎', 0x178: '咒蛇', 0x179: '飞龙探云手', 0x17A: '火龙掌',
    0x17B: '灭绝一击', 0x17C: '横扫千军', 0x17D: '爆炸', 0x17E: '魔掌天下', 0x17F: '佛法无边', 0x180: '灵葫咒',
    0x181: '气魔焰', 0x182: '合体气功', 0x183: '气功', 0x184: '剑气斩', 0x185: '火神', 0x186: '醉仙望月步',
    0x187: '投掷', 0x188: '金蝉脱壳', 0x189: '仙风云体术', 0x18A: '乾坤一掷', 0x18B: '大咒蛇', 0x18C: '腥风血雨',
    0x18D: '群魔乱舞',
}
# 装备部位 -> 物品代码区间（依游戏自带攻略《物品修改》分类表划分，用于筛选装备下拉框选项）
# 物品类(消耗品)3D-A2 / 武器A3-C3 / 头部C4-CF / 衣甲D0-E0 / 披风E1-EA / 靴子EB-F7 / 饰品F8-10E
SLOT_RANGE = {0: (0xC4, 0xCF), 1: (0xE1, 0xEA), 2: (0xD0, 0xE0),
              3: (0xA3, 0xC3), 4: (0xEB, 0xF7), 5: (0xF8, 0x10E)}
# 饰品位特例：玉佛珠为剧情必备饰品（灵儿装备后方可进入将军墓），其余 10F 起为剧情杂物不可装备
SLOT_EXTRA = {5: (0x112,)}


def item_name(code):
    return ITEM_NAMES.get(code, '物品0x%X' % code)


class PalSave:
    """存档数据层：负责读写 .RPG 二进制"""

    def __init__(self, path):
        self.path = path
        with open(path, 'rb') as f:
            self.buf = bytearray(f.read())

    def _w(self, off):
        return struct.unpack_from('<H', self.buf, off)[0]

    def _p(self, off, val):
        struct.pack_into('<H', self.buf, off, val)

    def _d(self, off):
        return struct.unpack_from('<I', self.buf, off)[0]

    def _p32(self, off, val):
        struct.pack_into('<I', self.buf, off, val)

    # ---- 金钱 ----
    def money(self):
        return self._d(MONEY_OFF)

    def set_money(self, val):
        self._p32(MONEY_OFF, val)

    # ---- 属性 ----
    def attr(self, ci, field_off):
        return self._w(PAGE2 + field_off + 2 * ci)

    def set_attr(self, ci, field_off, val):
        self._p(PAGE2 + field_off + 2 * ci, val)

    # ---- 装备 ----
    def equip(self, ci, slot):
        return self._w(PAGE2 + 0x80 + slot * 0x0C + 2 * ci)

    def set_equip(self, ci, slot, code):
        self._p(PAGE2 + 0x80 + slot * 0x0C + 2 * ci, code)

    # ---- 仙术 ----
    # 结构：每12字节一轮(6人x2字节，第6人为盖罗娇)，每角色32位，区域0x37C-0x4FF
    # 位 i 偏移 = 0x37C + i*12 + ci*2 （palhero fpe1.htm 原文 + 三档实测验证）
    def spell(self, ci, i):
        return self._w(PAGE2 + SPELL_BASE + i * 12 + ci * 2)

    def set_spell(self, ci, i, code):
        self._p(PAGE2 + SPELL_BASE + i * 12 + ci * 2, code)

    # ---- 物品 ----
    def items(self):
        """返回 [(槽位, 代码, 数量), ...]，连续 ITEM_ZERO_END 个空槽终止（允许中间零散空槽）"""
        out = []
        zeros = 0
        for i in range(ITEM_MAX):
            off = ITEM_BASE + i * 6
            code = self._w(off)
            if code == 0:
                zeros += 1
                if zeros >= ITEM_ZERO_END:
                    break
                continue
            zeros = 0
            out.append((i, code, self._w(off + 2)))
        return out

    def set_item(self, index, code, count):
        off = ITEM_BASE + index * 6
        self._p(off, code)
        self._p(off + 2, count)
        self._p(off + 4, 0)

    def write_items(self, counts):
        """全量重写物品区：counts 为 {代码: 数量}，数量>0 的项按代码升序从槽 0
        写起（符合游戏按代码排序的习惯），其后所有槽位清零；物品区共 256 槽
        （0x6C0-0xCBF），清零不得越过 0xCC0——之后是场景物件/事件状态表"""
        max_slots = min(ITEM_MAX, (len(self.buf) - ITEM_BASE) // 6)
        entries = sorted((c, n) for c, n in counts.items() if 0 < n <= 99)[:max_slots]
        for i, (code, cnt) in enumerate(entries):
            self.set_item(i, code, cnt)
        tail = ITEM_BASE + len(entries) * 6
        end = ITEM_BASE + max_slots * 6
        if end > tail:
            self.buf[tail:end] = bytes(end - tail)

    def save(self, path=None):
        path = path or self.path
        bak = path + '.bak'
        if not os.path.exists(bak):
            shutil.copy2(self.path, bak)
        with open(path, 'wb') as f:
            f.write(self.buf)


class EditorGUI:
    def __init__(self, root):
        self.root = root
        self.save = None
        self.attr_entries = []   # [角色][字段] -> Entry
        self.equip_combos = []   # [角色][栏位] -> Combobox
        self.spell_combos = []   # [角色][法术槽] -> Combobox
        root.title('仙剑98 存档修改器')
        root.geometry('780x720')
        self._build_menu()
        self.nb = ttk.Notebook(root)
        self.nb.pack(fill='both', expand=True, padx=6, pady=6)
        self.status = tk.StringVar(value='请通过菜单 文件->打开存档 选择 .RPG 存档')
        ttk.Label(root, textvariable=self.status, anchor='w').pack(fill='x', side='bottom')

    def _build_menu(self):
        m = tk.Menu(self.root)
        fm = tk.Menu(m, tearoff=0)
        fm.add_command(label='打开存档...', command=self.open_file)
        fm.add_command(label='保存', command=self.save_file, state='disabled')
        fm.add_command(label='另存为...', command=self.save_as, state='disabled')
        fm.add_separator()
        fm.add_command(label='退出', command=self.root.destroy)
        m.add_cascade(label='文件', menu=fm)
        self.file_menu = fm
        self.root.config(menu=m)

    # ---------------- 文件操作 ----------------
    def open_file(self):
        path = filedialog.askopenfilename(
            title='选择存档', initialdir=os.path.dirname(os.path.abspath(__file__)),
            filetypes=[('仙剑存档', '*.RPG *.rpg'), ('所有文件', '*.*')])
        if not path:
            return
        try:
            self.save = PalSave(path)
        except Exception as e:
            messagebox.showerror('错误', '读取存档失败：%s' % e)
            return
        self.file_menu.entryconfig('保存', state='normal')
        self.file_menu.entryconfig('另存为...', state='normal')
        self.build_tabs()
        self.status.set('已打开：%s（修改后请点击 文件->保存）' % path)

    def save_file(self):
        self.apply_all()
        self.save.save()
        messagebox.showinfo('完成', '已保存（原文件已备份为 .bak）')

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension='.RPG')
        if path:
            self.apply_all()
            self.save.save(path)
            messagebox.showinfo('完成', '已另存到：%s' % path)

    # ---------------- 界面构建 ----------------
    def build_tabs(self):
        for tab in self.nb.tabs():
            self.nb.forget(tab)
        self.attr_entries, self.equip_combos, self.spell_combos = [], [], []
        # 每个角色一页：属性 + 装备
        for ci, name in enumerate(CHARS):
            if self.save.attr(ci, 0x050) == 0:   # 最大体力=0 视为空槽
                continue
            frame = ttk.Frame(self.nb)
            self.nb.add(frame, text=name)
            self._build_char_tab(frame, ci)
        # 物品页
        self.item_frame = ttk.Frame(self.nb)
        self.nb.add(self.item_frame, text='背包物品')
        self._build_item_tab(self.item_frame)

    def _build_char_tab(self, frame, ci):
        # 属性区
        af = ttk.LabelFrame(frame, text='属性（直接输入数字）')
        af.pack(fill='x', padx=8, pady=6)
        entries = []
        for r, (label, foff) in enumerate(ATTRS):
            ttk.Label(af, text=label).grid(row=r // 2, column=(r % 2) * 2, sticky='e', padx=4, pady=3)
            e = ttk.Entry(af, width=8)
            e.insert(0, str(self.save.attr(ci, foff)))
            e.grid(row=r // 2, column=(r % 2) * 2 + 1, padx=4, pady=3)
            entries.append(e)
        self.attr_entries.append((ci, entries))
        # 装备区
        ef = ttk.LabelFrame(frame, text='披挂（选项来自背包物品，选"卸下"则为空）')
        ef.pack(fill='both', expand=True, padx=8, pady=6)
        bag_codes = [code for _, code, _ in self.save.items()]
        combos = []
        for r, (sname, slot) in enumerate(EQUIP_SLOTS):
            ttk.Label(ef, text=sname).grid(row=r, column=0, sticky='e', padx=4, pady=3)
            cur = self.save.equip(ci, slot)
            lo, hi = SLOT_RANGE[slot]
            extra = SLOT_EXTRA.get(slot, ())
            opts = {'卸下 (0)': 0}
            for code in bag_codes:
                if lo <= code <= hi or code in extra or code == cur:
                    opts['%s (0x%X)' % (item_name(code), code)] = code
            if cur and all(v != cur for v in opts.values()):
                opts['当前: %s (0x%X)' % (item_name(cur), cur)] = cur
            cb = ttk.Combobox(ef, values=list(opts.keys()), state='readonly', width=26)
            cur_text = next((k for k, v in opts.items() if v == cur), '卸下 (0)')
            cb.set(cur_text)
            cb.grid(row=r, column=1, sticky='w', padx=4, pady=3)
            combos.append((cb, opts))
        self.equip_combos.append((ci, combos))
        # 仙术区（每角色32个法术位，4列x8行；位偏移 0x37C + i*12 + ci*2，写入只动目标2字节）
        sf = ttk.LabelFrame(frame, text='仙术（每角色 %d 个法术位，选"无"则清空该槽）' % SPELL_MAX)
        sf.pack(fill='both', expand=True, padx=8, pady=6)
        spell_opts = {'无 (0)': 0}
        for code in sorted(SPELLS):
            spell_opts['%s (0x%X)' % (SPELLS[code], code)] = code
        combos = []
        for slot in range(SPELL_MAX):
            cur = self.save.spell(ci, slot)
            opts = dict(spell_opts)
            if cur and cur not in SPELLS:
                opts['未知 (0x%X)' % cur] = cur
            cur_text = next((k for k, v in opts.items() if v == cur), '无 (0)')
            cb = ttk.Combobox(sf, values=list(opts.keys()), state='readonly', width=14)
            cb.set(cur_text)
            cb.grid(row=slot // 4, column=slot % 4, padx=4, pady=3)
            combos.append((cb, opts))
        self.spell_combos.append((ci, combos))

    def _build_item_tab(self, frame):
        cols = ('代码', '名称', '数量')
        self.tree = ttk.Treeview(frame, columns=cols, show='headings', height=18)
        for c, w in zip(cols, (80, 200, 80)):
            self.tree.heading(c, text=c)
            self.tree.column(c, width=w, anchor='center')
        self.tree.pack(fill='both', expand=True, padx=8, pady=6)
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
        # 全物品数量表：{代码: 数量}，背包中没有的物品数量为 0；含名称表之外的未知代码
        self.item_counts = {code: cnt for _, code, cnt in self.save.items()}
        self.reload_items()
        bf = ttk.Frame(frame)
        bf.pack(fill='x', padx=8, pady=4)
        ttk.Label(bf, text='数量(0=移除):').pack(side='left')
        self.cnt_entry = ttk.Entry(bf, width=8)
        self.cnt_entry.pack(side='left', padx=4)
        ttk.Button(bf, text='设置选中物品数量', command=self.apply_item_count).pack(side='left', padx=4)
        ttk.Label(bf, text='  金钱:').pack(side='left')
        self.money_entry = ttk.Entry(bf, width=10)
        self.money_entry.insert(0, str(self.save.money()))
        self.money_entry.pack(side='left', padx=4)
        ttk.Label(bf, text='(保存时生效)').pack(side='left')

    def reload_items(self):
        self.tree.delete(*self.tree.get_children())
        codes = sorted(ITEM_NAMES)
        codes += sorted(c for c in self.item_counts if c not in ITEM_NAMES)
        for code in codes:
            self.tree.insert('', 'end', iid=str(code),
                             values=('0x%X' % code, item_name(code),
                                     self.item_counts.get(code, 0)))

    # ---------------- 数据应用 ----------------
    def on_item_select(self, _event):
        sel = self.tree.selection()
        if sel:
            self.cnt_entry.delete(0, 'end')
            self.cnt_entry.insert(0, str(self.item_counts.get(int(sel[0]), 0)))

    def apply_item_count(self):
        sel = self.tree.selection()
        if not sel:
            return
        try:
            cnt = int(self.cnt_entry.get())
            assert 0 <= cnt <= 99
        except (ValueError, AssertionError):
            messagebox.showerror('错误', '数量须为 0~99 的整数')
            return
        code = int(sel[0])
        self.item_counts[code] = cnt
        self.apply_all()          # 界面上未应用的属性/装备/仙术/金钱先写回数据层，防止重建页签丢失
        self.save.write_items(self.item_counts)
        cur = self.nb.index(self.nb.select()) if self.nb.tabs() else 0
        self.build_tabs()         # 重建页签：装备下拉框重新扫描背包，新添加的装备立即可选
        if self.nb.tabs():
            self.nb.select(min(cur, len(self.nb.tabs()) - 1))
            self.tree.selection_set(str(code))   # 恢复物品表格选中行（数量输入框随之回显）
        self.status.set('%s 数量已设为 %d（未保存）' % (item_name(code), cnt))

    def apply_all(self):
        """把界面上的属性/装备/仙术/金钱修改写回数据层"""
        for ci, entries in self.attr_entries:
            for e, (_, foff) in zip(entries, ATTRS):
                try:
                    v = int(e.get())
                    if 0 <= v <= 65535:
                        self.save.set_attr(ci, foff, v)
                except ValueError:
                    pass
        for ci, combos in self.equip_combos:
            for slot, (cb, opts) in enumerate(combos):
                self.save.set_equip(ci, slot, opts.get(cb.get(), 0))
        for ci, combos in self.spell_combos:
            for slot, (cb, opts) in enumerate(combos):
                self.save.set_spell(ci, slot, opts.get(cb.get(), 0))
        try:
            v = int(self.money_entry.get())
            if 0 <= v <= 0xFFFFFFFF:
                self.save.set_money(v)
        except ValueError:
            pass


def main():
    root = tk.Tk()
    EditorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
