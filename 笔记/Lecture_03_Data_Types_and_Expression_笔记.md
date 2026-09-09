# Lecture 03 · Data Types & Expression 数据类型与表达式

> Advanced Programming — 标识符、变量与赋值、内置数据类型
> 大纲：① 标识符/变量/赋值 ② 内置数据类型 ③ 运算符与表达式 ④ 基本输入/输出（③④ 下一讲展开）

## 一、标识符（Identifier）

给变量、函数、类、模块等对象起的名字。

**命名规则**
- ✅ 字母（A-Z, a-z）、数字（0-9）、下划线 `_`；数字不能开头
- ❌ 空格及 `@ # $ % !` 等特殊符号；不能是关键字（`if`、`else`、`for`、`while`、`def`、`class` 等）

```python
# ✅ 合法
my_var = 10;  _name = "private";  variable1 = 5
user_name = "John";  _private = True;  MyClass = "x"

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
| snake_case | `user_name` | 变量、函数、模块 |
| PascalCase | `MyClass` | 类名 |
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
