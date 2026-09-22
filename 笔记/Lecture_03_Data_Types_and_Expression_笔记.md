# Lecture 03 · Data Types & Expression 数据类型与表达式

> Advanced Programming — 标识符、变量与赋值、内置数据类型、运算符与表达式、基本输入/输出

**大纲**：① 标识符/变量/赋值 ② 内置数据类型 ③ 运算符与表达式 ④ 基本输入/输出

## 一、标识符（Identifier）

给变量、函数、类、模块等对象起的名字。

**命名规则**
- ✅ 字母（A-Z, a-z）、数字（0-9）、下划线 `_`；数字不能开头
- ❌ 空格及 `@ # $ % !` 等特殊符号；不能是关键字（`if`、`else`、`for`、`while`、`def`、`class` 等）

```python
# ✅ 合法
my_var = 10
_name = "private"
variable1 = 5
user_name = "John"
_private = True
MyClass = "example"

# ❌ 非法
1variable = 10   # 不能数字开头
my-var = 20      # 不能用连字符
my var = 30      # 不能有空格
class = "test"   # class 是关键字
@name = "John"   # @ 不允许
```

**命名规范（约定俗成，不强制）**

| 规范 | 示例 | 用于 |
| --- | --- | --- |
| camelCase | `getText`、`setValue` | 函数 |
| snake_case | `user_name`、`total_count` | 变量、模块、文件 |
| PascalCase | `MyClass`、`UserProfile` | 类名 |
| UPPER_CASE | `PI`、`MAX_LIMIT` | 常量 |
| `_x` 单前导下划线 | `_internal` | 约定"私有" |
| `__x` 双前导下划线 | `__private` | 类中名称修饰（name mangling） |

**注意**：大小写敏感（`myvar`/`MyVar`/`MYVAR` 是三个变量）；支持 Unicode（如中文变量名，少用）；`__init__` 等双下划线（dunder）方法有特殊含义。

## 二、变量与赋值（Variable & Assignment）

- 变量是内存中存值的命名容器；用 `=` 赋值，本质是把名字**绑定（引用）**到对象上
- **无需声明**：类型由 Python 自动推断
- **动态类型**：类型可随时改变，如 `x = 1` 之后可 `x = "hello"`
- **大小写敏感**

## 三、内置数据类型

| 类型 | 取值 | 示例 |
| --- | --- | --- |
| Boolean 布尔 | `True` / `False` | `is_student = True` |
| Integer 整型 | 整数 | `age = 25` |
| Float 浮点型 | 小数，支持科学计数法 | `height = 168.6`、`2.99792458e8` |
| Complex 复数型 | 虚部用 **`j`**（非 i） | `c = 12.3 + 4.56j` |
| String 字符串 | 引号包裹的文本，支持中文 | `name = "张子邦"` |
| NoneType 空型 | 仅一个值 `None`（类似其他语言的 null） | `supervisor = None` |

```python
is_student = True
age = 25
PI = 3.14159
LIGHT_SPEED = 2.99792458e8          # 光速
dist_sun_earth = 1.49597870700e11   # 日地距离
# print(dist_sun_earth / LIGHT_SPEED)  → ≈ 499 秒 ≈ 8.3 分钟
c = 12.3 + 4.56j
major = "光电信息科学与工程"
supervisor = None
```

> **练习**：光从太阳到地球需多久？→ `1.49597870700e11 / 2.99792458e8 ≈ 499 秒 ≈ 8.3 分钟`

## 四、字符串格式化（String Formatting）

`%` 格式化（printf 风格）是最古老的字符串格式化方式，用 `%` 运算符把值替换进字符串。

**常用格式说明符**

| 说明符 | 含义 |
| --- | --- |
| `%s` | 字符串 |
| `%d` | 整数 |
| `%f` | 浮点数 |
| `%x` | 十六进制（小写） |
| `%o` | 八进制 |
| `%%` | 字面量 `%` |

```python
name = "Alice"
print("Hello, %s!" % name)                    # Hello, Alice!

name = "Bob"
age = 25
print("%s is %d years old." % (name, age))    # Bob is 25 years old.

pi = 3.14159265
print("Pi is approximately %.2f" % pi)        # Pi is approximately 3.14
print("Pi is approximately %10.3f" % pi)      # Pi is approximately      3.142
print("%5d" % 42)      # "   42"  （右对齐）
print("%-5d|" % 42)    # "42   |" （左对齐）
print("%05d" % 42)     # "00042"  （零填充）
```

> 格式 `%10.3f`：总宽 10 位，小数点后 3 位；`%-5d` 负号表示左对齐；`%05d` 表示零填充。

## 五、数据类型转换（Data Type Conversion）

类型转换（type casting）指把值从一种类型变成另一种。

**隐式转换（Implicit，自动）**：Python 自动把"较小"类型转成"较大"类型，不丢失信息。

```python
num_int = 10
num_float = 2.5
result = num_int + num_float
print(result)        # 12.5
print(type(result))  # <class 'float'>
```

**显式转换（Explicit，手动）**：用内置函数主动转换。

| 函数 | 转为 |
| --- | --- |
| `int()` | 整数 |
| `float()` | 浮点数 |
| `str()` | 字符串 |
| `bool()` | 布尔值 |
| `list()` | 列表 |
| `tuple()` | 元组 |
| `set()` | 集合 |
| `dict()` | 字典 |

```python
x = "123"
x_int   = int(x)     # 123
x_float = float(x)   # 123.0
x_str   = str(123)   # "123"
x_bool  = bool(x)    # True
x_list  = list(x)    # ['1', '2', '3']
```

> 仅在安全且不丢失信息时（主要是数值类型之间）Python 才自动转换；需要精确控制时用显式转换函数。

## 六、运算符（Operators）

运算符是对值和变量（操作数）执行操作的特殊符号或关键字。

**1. 算术运算符（Arithmetic）**

| 运算符 | 说明 | 示例 |
| --- | --- | --- |
| `+` | 加 | `3 + 2 → 5` |
| `-` | 减 | `3 - 2 → 1` |
| `*` | 乘 | `3 * 2 → 6` |
| `/` | 除（结果为 float） | `7 / 2 → 3.5` |
| `//` | 整除（向下取整） | `7 // 2 → 3` |
| `%` | 取余 | `7 % 2 → 1` |
| `**` | 幂 | `3 ** 2 → 9` |

**2. 关系运算符（Relational）**

| 运算符 | 说明 |
| --- | --- |
| `==` | 等于 |
| `!=` | 不等于 |
| `>` `>=` | 大于 / 大于等于 |
| `<` `<=` | 小于 / 小于等于 |

**3. 逻辑运算符（Logical）**

| 运算符 | 说明 |
| --- | --- |
| `and` | 与（两边都 True 才 True） |
| `or` | 或（一边 True 即 True） |
| `not` | 非（取反） |

**4. 赋值运算符（Assignment）**

`=`、`+=`、`-=`、`*=`、`/=`、`//=`、`%=`、`**=`

**5. 位运算符（Bitwise）**

`&`（与）、`|`（或）、`^`（异或）、`~`（取反）、`<<`（左移）、`>>`（右移）

**6. 成员运算符（Membership）** & **身份运算符（Identity）**

- 成员运算符：检测值是否在序列中
- 身份运算符：检测两个变量是否引用**内存中同一个对象**（不仅仅是值相等）

```python
# 成员运算符
print("a" in "apple")        # True
print("z" not in "apple")    # True
print(2 in {1, 2, 3})        # True

# 身份运算符
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)    # True  （值相等）
print(a is b)    # False （不同对象）
print(a is c)    # True  （同一对象）
```

## 七、基本输入/输出（Basic Input / Output）

Python 用内置函数 `input()` 读取用户输入、`print()` 显示输出。

```python
name = input("请输入你的名字：")   # input() 返回字符串
print("你好，" + name)
```

## 八、转义字符（Escape Characters）

转义字符是反斜杠 `\` 加一个特殊字符，用于在字符串中表示换行、制表符、引号等难以直接输入的字符。

| 转义 | 名称 | 含义 |
| --- | --- | --- |
| `\n` | 换行 | 移到下一行 |
| `\t` | 制表符 | 水平制表 |
| `\\` | 反斜杠 | 字面量 `\` |
| `\'` | 单引号 | 字面量 `'` |
| `\"` | 双引号 | 字面量 `"` |
| `\r` | 回车 | 光标移到行首 |
| `\b` | 退格 | 光标后退一格 |
| `\f` | 换页 | 分页符 |
| `\v` | 垂直制表 | 垂直制表符 |
| `\a` | 响铃 | 尝试蜂鸣 |
| `\0` | 空字符 | Null character |
| `\ooo` | 八进制 | 八进制值 ooo 对应的字符 |
| `\xhh` | 十六进制 | 十六进制值 hh 对应的字符 |
| `\N{name}` | Unicode 名称 | 按 Unicode 名称取字符 |
| `\uxxxx` | Unicode 16 位 | 16 位十六进制值对应的字符 |
| `\Uxxxxxxxx` | Unicode 32 位 | 32 位十六进制值对应的字符 |
