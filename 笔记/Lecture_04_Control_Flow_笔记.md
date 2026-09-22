# Lecture 04 · Control Flow 控制流

> Advanced Programming — 条件语句、循环语句

**控制流**：指程序中语句、指令或函数调用被执行/求值的顺序。默认 Python 从上到下顺序执行，控制流语句可以改变这个顺序——做决策、重复动作或跳转。

**大纲**：① 条件语句（Conditional statements）② 循环语句（Loop statements）

## 一、条件语句（Conditional Statements）

让程序做决策——只在满足特定条件时才执行某段代码。

### 1. `if` 语句

仅当条件为 `True` 时执行代码块。

```python
age = 18
if age >= 18:
    print("你已成年")
```

### 2. `if / else` 语句

条件为 `False` 时提供另一个分支。

```python
age = 16
if age >= 18:
    print("你已成年")
else:
    print("你还未成年")
```

### 3. `if / elif / else` 语句

链式判断多个条件，从上到下检查，**第一个为 True 的分支会执行，其余跳过**。

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)   # B
```

### 4. `match / case` 语句（Python 3.10+）

多个 `elif` 分支的更优雅替代——结构化模式匹配（structural pattern matching）。

```python
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other")   # _ 是通配符，匹配任何未命中的情况
```

## 二、循环语句（Loop Statements）

重复执行一段代码多次。Python 有两种主要循环：`for` 和 `while`。

### 1. `for` 循环

遍历一个序列（list、tuple、string、range、dict 等）的每个元素。

```python
for i in range(5):
    print(i)            # 0 1 2 3 4

for ch in "hello":
    print(ch)           # h e l l o
```

**`enumerate()` —— 同时取索引和值**

```python
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

**`range()` 的几种形式**

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8  （步长为 2）
range(10, 0, -2)  # 10, 8, 6, 4, 2  （步长为负，倒序）
```

**`zip()` —— 同时遍历多个序列**

```python
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Alice is 25
# Bob is 30
```

### 2. `while` 循环

只要条件保持 `True` 就重复执行。

```python
count = 0
while count < 3:
    print(count)
    count += 1
# 0 1 2
```

### 3. 循环控制关键字

| 关键字 | 作用 |
| --- | --- |
| `break` | 立即退出循环 |
| `continue` | 跳过本次循环剩余部分，进入下一次迭代 |
| `pass` | 什么都不做（占位符，保持语法完整） |

```python
# break：找到 3 就退出
for i in range(10):
    if i == 3:
        break
    print(i)        # 0 1 2

# continue：跳过偶数
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)        # 1 3

# pass：占位，不执行任何操作
for i in range(3):
    pass            # 什么都不做
```

## 三、`for` vs `while` —— 何时用哪个

| 用 `for` | 用 `while` |
| --- | --- |
| 已知要遍历的序列 | 循环直到某个条件改变 |
| 迭代数据集合 | 等待用户输入 / 事件 |
| 固定重复次数 | 迭代次数未知 |
