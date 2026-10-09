# aria2c 下载工具调用程序
# 功能：询问用户下载网址，调用 aria2c.exe 进行下载（整合在 download() 函数中）
# 依赖：aria2c.exe（aria2 1.33.1）

import subprocess
import os

ARIA2C = r"e:\Advanced programming\aria2c.exe"   # aria2c.exe 路径


def download(split=8, max_tries=10):
    """询问下载网址和保存目录，调用 aria2c.exe 完成下载

    参数：
        split     每个文件的分块数（默认 8）
        max_tries 下载失败时的自动重试次数（默认 10）
    返回：
        True 下载成功，False 下载失败或网址为空
    """
    # 1. 询问下载网址
    url = input("请输入下载网址：").strip()
    if not url:                       # 输入为空直接退出
        print("网址不能为空!")
        return False

    # 2. 询问保存目录（直接回车保存到当前目录）
    save_dir = input("请输入保存目录（直接回车保存到当前目录）：").strip() or "."

    # 3. 询问分块数与重试次数（直接回车保持默认设置）
    ans = input(f"请输入分块数（直接回车默认 {split}）：").strip()
    if ans.isdigit() and int(ans) > 0:    # 输入合法正整数才更新，否则保持默认
        split = int(ans)

    ans = input(f"请输入重试次数（直接回车默认 {max_tries}）：").strip()
    if ans.isdigit() and int(ans) > 0:
        max_tries = int(ans)

    # 4. 组装命令并调用 aria2c.exe
    #    -d 指定保存目录
    #    -s N  每个文件分 N 块下载（分块数）
    #    -x N  每个服务器最多 N 个连接（与分块数保持一致）
    #    -m N  下载失败时自动重试 N 次（重试次数）
    cmd = [ARIA2C, "-d", save_dir,
           "-s", str(split), "-x", str(split),
           "-m", str(max_tries), url]
    print(f"开始下载：{url}")
    print(f"保存到：{os.path.abspath(save_dir)}（分块数：{split}，重试次数：{max_tries}）\n")

    # subprocess.run 调用外部程序，返回码为 0 表示下载成功
    result = subprocess.run(cmd)

    # 5. 输出结果
    if result.returncode == 0:
        print("\n下载完成!")
        return True
    else:
        print("\n下载失败，请检查网址是否有效。")
        return False


if __name__ == "__main__":
    download()
