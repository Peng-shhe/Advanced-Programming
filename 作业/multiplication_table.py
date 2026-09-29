# 9x9 乘法口诀表
# 要求：
# 1. 使用转义字符 \t 对齐每一列，使用 \n 换行
# 2. 使用条件语句 if，当乘积大于 20 时，在数字后面加上 * 标记
# 3. 内层循环控制每行打印的列数（第 i 行打印 i 列）

for i in range(1, 10):           # 外层循环：控制行数，i 从 1 到 9
    line = ""                     # 每一行的内容
    for j in range(1, i + 1):    # 内层循环：控制列数，第 i 行打印 i 列
        product = i * j           # 计算乘积
        if product > 20:          # 条件判断：乘积大于 20 时加 * 标记
            line += f"{j}x{i}={product}*\t"
        else:
            line += f"{j}x{i}={product}\t"
    line += "\n"                  # 每行末尾用 \n 换行
    print(line, end="")           # 打印这一行（不再额外换行）
