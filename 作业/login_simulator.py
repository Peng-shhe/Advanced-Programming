# 模拟登录程序
# 要求：
# 1. 用户最多有 3 次输入密码的机会（while 循环）
# 2. 正确密码为 "Py\\123"（实际字符串为 Py\123）
# 3. 每次输入后判断：正确则登录成功并退出；错误且有剩余次数则提示重试；3 次全错则锁定
# 4. 使用转义字符 \t 和 \n 美化输出

correct_password = "Py\\123"   # 正确密码，实际字符串为 Py\123
max_attempts = 3               # 最多尝试次数
attempts = 0                   # 已尝试次数

while attempts < max_attempts:
    password = input("请输入密码：")

    if password == correct_password:
        # 密码正确：登录成功并退出循环
        print("登录成功!\n欢迎使用系统。")
        break

    # 密码错误：增加已尝试次数
    attempts += 1
    remaining = max_attempts - attempts

    if remaining > 0:
        # 还有剩余次数：提示重试
        print(f"密码错误，还剩{remaining}次机会\t请重试!")
    else:
        # 3 次都错误：账号锁定
        print("账号已锁定!\n请联系管理员。")
