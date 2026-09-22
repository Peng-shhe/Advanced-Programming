# 定义学生成绩
students = [
    ("Alice", 92.50, "A"),
    ("Bob", 78.00, "B"),
    ("Charlie", 85.75, "A"),
    ("David", 60.50, "D"),
    ("Eve", 99.25, "A"),
]

# 计算总人数和平均分
total_students = len(students)
total_score = sum(student[1] for student in students)
average_score = total_score / total_students

# 使用 % 格式化输出报告

# 1. 打印标题行（两侧各10个 =）
print("%s Score Report %s" % ("=" * 10, "=" * 10))

# 2. 打印总人数行
print("Total students: %d" % total_students)

# 3. 打印空行
print()

# 4. 打印表头
# Name 左对齐占12位，Score 右对齐占8位，Grade 右对齐占6位
print("%-12s%8s%6s" % ("Name", "Score", "Grade"))

# 5. 循环打印每位学生的成绩
for name, score, grade in students:
    # 姓名左对齐占12位，成绩保留2位小数且右对齐占8位，等级右对齐占6位
    print("%-12s%8.2f%6s" % (name, score, grade))

# 6. 打印空行
print()

# 7. 打印平均分
print("Average: %.2f" % average_score)