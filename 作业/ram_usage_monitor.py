# 内存使用率实时监控程序
# 要求：
# 1. 使用 psutil 库获取系统内存使用率
# 2. 使用 time.sleep() 每 0.5 秒刷新一次
# 3. 打印后不换行（使用 print 的 end 参数）
# 4. 输出格式为进度条样式，例如：RAM usage: |=====    | 50%
# 5. 进度条总长度为 10 个字符，= 表示已用，空格表示剩余
#    = 的个数是百分比四舍五入取整的个数（如 32% 打印 3 个 =，89% 打印 9 个 =）
# 6. 使用 \r（回车符）回到行首实现原地刷新

import psutil
import time

while True:
    # 获取系统内存信息，percent 为内存使用率（百分比）
    mem = psutil.virtual_memory()
    percent = mem.percent

    # 计算进度条：已用部分用 =，剩余部分用空格
    # 将百分比 0~100 映射到 0~10 的进度条长度（如 32%→3个=，89%→9个=）
    used = round(percent / 10)
    bar = "=" * used + " " * (10 - used)

    # \r 回到行首原地刷新；end="" 不换行
    print(f"RAM usage: |{bar}| {percent:.0f}%", end="\r")

    time.sleep(0.5)                    # 每 0.5 秒刷新一次
