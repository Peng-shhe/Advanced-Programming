#import datetime

#def check_workday():
    # 获取当前日期
 #   today = datetime.date.today()
    # 获取星期几（0代表周一，1代表周二... 5代表周六，6代表周日）
 #   weekday = today.weekday()
 #   print()
 #   if weekday < 5:  # 周一到周五（0-4）是工作日
 #       print("我不想上班")
 #   else:  # 周六（5）和周日（6）是周末
 #       print("今天不用上班")

#if __name__ == "__main__":
#    check_workday()
import datetime

def check_workday():
    today = datetime.date.today()
    # weekday() 返回 0-6（0是周一，6是周日）
    weekday = today.weekday()
    
    match weekday:
        case 0 :  # 匹配周一到周五
            print("周一我不想上班")
        case 1 :  # 匹配周一到周五
            print("周二我不想上班")
        case 2 :  # 匹配周一到周五
            print("周三我不想上班")
        case 3 :  # 匹配周一到周五
            print("周四我不想上班")
        case 4:  # 匹配周一到周五
            print("周五我不想上班")
        case 5 | 6:  # 匹配周六和周日
            print("今天不用上班")
        case _:  # 默认情况（兜底，防止意外情况）
            print("日期判断出错")

if __name__ == "__main__":
    check_workday()