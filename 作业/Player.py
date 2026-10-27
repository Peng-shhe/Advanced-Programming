# -*- coding: utf-8 -*-
"""Player（仙剑角色）类：属性建模 + 从 .RPG 存档读取 + JSON 风格文本导出

Lecture 07 Files 作业：
  1) loadFromSavedFile(filepath, char_index=0)  —— 从仙剑存档按偏移读取角色属性
  2) export2Dict(filepath)                      —— 以 JSON 风格文本写出属性

存档结构参考项目文档《Pal存档属性分析与修改方案.md》，偏移均经三档存档实测验证。
"""
import struct

# —— 常量：角色序号 → 名字（存档不存名字，由游戏资源提供，按序号定位）——
CHAR_NAMES = ['李逍遥', '赵灵儿', '林月如', '巫后', '阿奴']

# —— 存档第 2 页基址 & 属性字段偏移（16 位小端，角色步进 2 字节）——
PAGE2      = 0x200
FIELD_OFFS = {
    'level':   0x044,   # 修行（等级）
    'hp_max':  0x050,   # 最大体力
    'mp_max':  0x05C,   # 最大真气
    'hp':      0x068,   # 体力
    'mp':      0x074,   # 真气
    'offense': 0x0C8,   # 武术
    'spirit':  0x0D4,   # 灵力
    'defense': 0x0E0,   # 防御
    'speed':   0x0EC,   # 身法
    'luck':    0x0F8,   # 吉运
}

# —— 属性名 → 导出 JSON key 的映射（按作业截图格式）——
JSON_KEYS = {
    'level':   'level',
    'hp':      'HP',
    'hp_max':  'HP_max',
    'mp':      'MP',
    'mp_max':  'MP_max',
    'offense': 'offense',
    'spirit':  'spirit',
    'defense': 'defense',
    'speed':   'speed',
    'luck':    'luck',
}


class Player:
    def __init__(self, name='', char_index=-1):
        self.name       = name
        self.char_index = char_index
        # —— 角色属性（默认值与课件 Role 类保持一致）——
        self.level    = 1
        self.hp_max   = 150
        self.hp       = 150
        self.mp_max   = 100
        self.mp       = 100
        self.offense  = 35
        self.spirit   = 20
        self.defense  = 40
        self.speed    = 30
        self.luck     = 30
        # —— 战斗状态 ——
        self.is_alive     = True
        self.is_defending = False

    # —— 战斗方法（与课件 Role 类保持一致）——
    def attack(self, target):
        pass

    def cast(self, target, skill):
        pass

    def defend(self):
        pass

    def levelUp(self):
        self.level += 1
        pass

    def endturn(self):
        pass

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def restoreMP(self, amount):
        self.mp += amount
        if self.mp > self.mp_max:
            self.mp = self.mp_max

    # ================================================================
    # 作业题 1：从仙剑 .RPG 存档文件中读取角色属性
    # ================================================================
    def loadFromSavedFile(self, filepath, char_index=None):
        """从仙剑 98 存档文件中按偏移读取指定角色的属性值。

        偏移公式：绝对偏移 = PAGE2(0x200) + 字段基址 + 2 × 角色序号
        所有数值为 16 位小端整数。

        :param filepath:   .RPG 存档文件路径
        :param char_index: 角色序号 0–4（0=李逍遥 … 4=阿奴）；若不传则用 self.char_index，
                           两者都未设时默认 0（李逍遥）
        :raises IndexError:          char_index 超出 0–4 范围
        :raises FileNotFoundError:   filepath 不存在
        """
        if char_index is None:
            char_index = self.char_index
        if char_index < 0 or char_index >= len(CHAR_NAMES):
            raise IndexError(f'char_index 须在 0–{len(CHAR_NAMES)-1} 范围内')
        self.char_index = char_index
        self.name       = CHAR_NAMES[char_index]

        with open(filepath, 'rb') as f:
            buf = f.read()

        for attr, base in FIELD_OFFS.items():
            off = PAGE2 + base + 2 * char_index
            val = struct.unpack_from('<H', buf, off)[0]
            setattr(self, attr, val)

        # 数据一致性兜底
        self.is_alive = self.hp > 0
        self.is_defending = False

    # ================================================================
    # 作业题 2：以 JSON 风格文本格式写出角色属性
    # ================================================================
    def export2Dict(self, filepath):
        """将角色属性以 JSON 风格文本写入 filepath，格式示例：

            {
              "name": "李逍遥",
              "HP": 100,
              "HP_max": 150,
              ...
              "luck": 20
            }

        注意：文件内是纯文本字典风格，不是严格的 JSON 文件。
        """
        lines = ['{']
        lines.append(f'  "name": "{self.name}",')
        attrs = list(FIELD_OFFS.keys())          # 保持存档字段顺序
        for i, attr in enumerate(attrs):
            key  = JSON_KEYS.get(attr, attr)
            val  = getattr(self, attr)
            tail = ',' if i < len(attrs) - 1 else ''
            lines.append(f'  "{key}": {val}{tail}')
        lines.append('}')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))


# —— 命令行快速验证（python Player.py）——
if __name__ == '__main__':
    import os, glob
    saves = glob.glob(r'..\Pal\Pal\pal\*.RPG') + glob.glob(r'..\Pal\Pal\pal\*.rpg')
    if not saves:
        print('未找到 .RPG 存档，请先放置 Pal\\Pal\\pal\\*.RPG')
    else:
        save = saves[0]
        print(f'读取存档：{save}\n')
        for idx in range(len(CHAR_NAMES)):
            p = Player()
            try:
                p.loadFromSavedFile(save, idx)
            except IndexError:
                break
            out = f'char_{idx}_{CHAR_NAMES[idx]}.txt'
            p.export2Dict(out)
            print(f'[{CHAR_NAMES[idx]}] Lv{p.level} HP {p.hp}/{p.hp_max} '
                  f'MP {p.mp}/{p.mp_max} 五维 '
                  f'武{p.offense} 灵{p.spirit} 防{p.defense} 速{p.speed} 运{p.luck}'
                  f'  → {out}')
