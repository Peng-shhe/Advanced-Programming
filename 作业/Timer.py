"""Timer 计时器类
================================================================
设计理念
----------------------------------------------------------------
目的：对一段代码的运行时长进行计时。
用法：在代码段之前调用 start()，之后调用 end()，
      Timer 自动记录两个时刻并计算出中间经过的时长。

属性（成员变量）：
    _start   计时开始的时刻（秒），未开始时为 None
    _end     计时结束的时刻（秒），未结束时为 None
    running  计时器当前是否正在计时（防止重复 start/end）

方法（成员函数）：
    start()      记录开始时刻；若正在计时则报错
    end()        记录结束时刻；若未开始/已结束则报错
    elapsed()    返回计时时长（秒），内部按需换算
    __repr__()   打印计时结果，如 elapsed: 0.512 s

计时基准使用 time.perf_counter()——Python 中精度最高的
单调时钟，不受系统时间调整影响，专用于测量时间间隔。
================================================================
"""

import time


class Timer:
    def __init__(self):
        self._start = None   # 开始时刻（秒）
        self._end = None     # 结束时刻（秒）
        self.running = False  # 是否正在计时

    def start(self):
        """开始计时（在代码段之前调用）"""
        if self.running:
            raise Exception('timer is already running')
        self.running = True
        self._start = time.perf_counter()

    def end(self):
        """结束计时（在代码段之后调用）"""
        if not self.running:
            raise Exception('timer is not running')
        self._end = time.perf_counter()
        self.running = False

    def elapsed(self):
        """返回计时时长（秒）"""
        if self._start is None:
            raise Exception('timer has not been started')
        # 已结束则返回起止差值；仍在计时则返回当前经过的时间
        end = self._end if self._end is not None else time.perf_counter()
        return end - self._start

    def __repr__(self):
        return 'elapsed: %.3f s' % (self.elapsed())


# ---------------- 演示：测量一段代码的运行时长 ----------------
t = Timer()
t.start()                      # 代码段开始

total = 0                      # 被计时的代码段
for i in range(10 ** 7):
    total += i
print('total =', total)

t.end()                        # 代码段结束
print(t)                       # 输出计时时长
