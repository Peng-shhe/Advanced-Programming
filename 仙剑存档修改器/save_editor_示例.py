# -*- coding: utf-8 -*-
"""仙剑98柔情版 存档角色属性修改器
================================================================
存档格式（逆向验证）：角色属性区位于文件第2页（基址 0x200），
每个字段按 6 个角色槽排列，每槽 2 字节（16 位小端整数）。
角色槽顺序固定：0李逍遥 1赵灵儿 2林月如 3巫后 4阿奴 5保留槽

用法：
  显示  python pal_save_editor.py show  <存档路径>
  修改  python pal_save_editor.py set   <存档路径> <角色名> <字段> <数值> [字段 数值 ...]
        例：python pal_save_editor.py set 1.RPG 李逍遥 体力 999 武术 999

修改前自动在同目录生成 .bak 备份。
================================================================
"""
import struct
import shutil
import sys
import os

PAGE2 = 0x200                      # 角色属性区基址（第2页）
CHARS = ['李逍遥', '赵灵儿', '林月如', '巫后', '阿奴', '保留槽']
# 字段名 -> 相对第2页的偏移（每个角色 +2 字节）
FIELDS = {
    '修行':   0x044,
    '最大体力': 0x050,
    '最大真气': 0x05C,
    '体力':   0x068,
    '真气':   0x074,
    '武术':   0x0C8,
    '灵力':   0x0D4,
    '防御':   0x0E0,
    '身法':   0x0EC,
    '吉运':   0x0F8,
}
MAX16 = 65535


def offset(char, field):
    """计算某角色某字段的文件内绝对偏移"""
    return PAGE2 + FIELDS[field] + 2 * CHARS.index(char)


def show(path):
    with open(path, 'rb') as f:
        buf = f.read()
    save_cnt = struct.unpack_from('<H', buf, 0)[0]
    print('%s  （存盘次数 %d，大小 %d 字节）' % (path, save_cnt, len(buf)))
    head = '  %-6s' % '角色'
    for fn in FIELDS:
        head += '%6s' % fn
    print(head)
    for ch in CHARS:
        row = '  %-6s' % ch
        for fn in FIELDS:
            row += '%6d' % struct.unpack_from('<H', buf, offset(ch, fn))[0]
        print(row)


def load(path):
    with open(path, 'rb') as f:
        return bytearray(f.read())


def save(path, buf):
    with open(path, 'wb') as f:
        f.write(buf)


def backup(path):
    bak = path + '.bak'
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
        print('已备份 ->', bak)


def modify(path, args):
    """args = [角色, 字段1, 值1, 字段2, 值2, ...]"""
    char, rest = args[0], args[1:]
    if char not in CHARS or char == '保留槽':
        print('错误：未知角色 [%s]，可选：%s' % (char, ' '.join(CHARS[:5])))
        return
    if len(rest) % 2 != 0:
        print('错误：字段与数值必须成对出现')
        return
    buf = load(path)
    for i in range(0, len(rest), 2):
        field, value = rest[i], rest[i + 1]
        if field not in FIELDS:
            print('错误：未知字段 [%s]，可选：%s' % (field, ' '.join(FIELDS)))
            return
        if not value.isdigit() or not 0 < int(value) <= MAX16:
            print('错误：数值须为 1~%d 的整数' % MAX16)
            return
        off = offset(char, field)
        old = struct.unpack_from('<H', buf, off)[0]
        struct.pack_into('<H', buf, off, int(value))
        print('%-4s %-5s: %d -> %d  (偏移 0x%X)' % (char, field, old, int(value), off))
    backup(path)
    save(path, buf)
    print('修改完成。')


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ('show', 'set'):
        print(__doc__)
        return
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == 'show':
        show(path)
    else:
        # set <存档> <角色> <字段> <值> [...]  ->  argv[3:] 为奇数个
        if len(sys.argv) < 6 or (len(sys.argv) - 3) % 2 != 1:
            print('用法: set <存档> <角色> <字段> <数值> [字段 数值 ...]')
            return
        modify(path, sys.argv[3:])


if __name__ == '__main__':
    main()
