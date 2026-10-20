"""File 文件类
================================================================
设计理念
----------------------------------------------------------------
目的：对电脑中的"单个文件"建模。一个文件天然具有：
      状态（路径、大小、修改时间……）+ 行为（读、写、删……），
      适合用 OOP 封装——创建 File 对象即拿到该文件的"句柄"，
      之后对文件的所有操作都通过对象方法完成，外部代码
      不需要直接操作 os/open 等底层细节。

属性（成员变量）：
    path     文件完整路径（字符串）
    name     文件名（由 path 派生）
    dir      所在目录（由 path 派生）
    ext      扩展名（由 path 派生，如 '.txt'）

方法（成员函数）：
    exists()      文件是否存在
    getSize()     文件大小（字节）
    getTime()     最后修改时间（'年-月-日 时:分:秒'）
    read()        读取全部文本内容
    write(text)   写入文本（覆盖）
    append(text)  追加文本
    delete()      删除文件
    rename(new)   重命名（同步更新 path/name/ext 等属性）
    __repr__()    打印文件摘要：name, size, time

封装要点：rename/delete 等方法在改变文件状态后同步更新
内部属性，保证对象状态始终与磁盘上的真实文件一致——
这正是"数据与行为绑定"的 OOP 思想。
================================================================
"""

import os
import time


class File:
    def __init__(self, path):
        self.path = os.path.abspath(path)  # 统一存绝对路径
        self._updateInfo()

    def _updateInfo(self):
        """由 path 派生 name / dir / ext（内部方法，属性变化后调用）"""
        self.dir = os.path.dirname(self.path)
        self.name = os.path.basename(self.path)
        self.ext = os.path.splitext(self.path)[1]

    def exists(self):
        return os.path.isfile(self.path)

    def getSize(self):
        """文件大小（字节）"""
        if not self.exists():
            raise Exception('file not found: %s' % (self.path))
        return os.path.getsize(self.path)

    def getTime(self):
        """最后修改时间，格式：'2026-10-20 15:30:00'"""
        if not self.exists():
            raise Exception('file not found: %s' % (self.path))
        stamp = os.path.getmtime(self.path)
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))

    def read(self):
        """读取全部文本"""
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, text):
        """写入文本（覆盖原内容），创建后不存在的文件"""
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(text)

    def append(self, text):
        """在末尾追加文本"""
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(text)

    def delete(self):
        """删除文件"""
        if not self.exists():
            raise Exception('file not found: %s' % (self.path))
        os.remove(self.path)

    def rename(self, new_name):
        """重命名文件，并同步更新内部属性"""
        if not self.exists():
            raise Exception('file not found: %s' % (self.path))
        new_path = os.path.join(self.dir, new_name)
        os.rename(self.path, new_path)
        self.path = new_path
        self._updateInfo()

    def __repr__(self):
        if not self.exists():
            return 'File(%s) [not found]' % (self.name)
        return 'File(%s, %d bytes, %s)' % (self.name, self.getSize(), self.getTime())


# ---------------- 演示：对作业文件夹中的文件建模 ----------------
f = File(r'作业\hello_world.py')
print(f)                     # 文件摘要
print('name:', f.name)
print('dir :', f.dir)
print('ext :', f.ext)
print('size:', f.getSize(), 'bytes')
print('time:', f.getTime())
print('content:')
print(f.read())

# 写入 / 追加 / 重命名 / 删除 演示（用临时文件）
tmp = File('_file_test.txt')
tmp.write('Hello, File class!\n')
tmp.append('written by append()\n')
print('tmp size:', tmp.getSize(), 'bytes')
print(tmp.read())
tmp.rename('_file_test_renamed.txt')
print('renamed to:', tmp.name)
tmp.delete()
print('exists after delete:', tmp.exists())
