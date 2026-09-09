# Lecture 03. Data Types & Expression 数据类型与表达式笔记

> 课程：Advanced Programming（高级编程）
> 主题：标识符、变量与赋值；Python 内置数据类型

**本讲大纲（Outline）：**
1. Identifier, Variable, Assignment（标识符、变量、赋值）
2. Built-in Data Types（内置数据类型）
3. Operator & Expression（运算符与表达式）
4. Basic Input / Output（基本输入/输出）

> 注：课件实际内容覆盖到第 1、2 部分（至 NoneType），运算符/表达式与输入输出部分预计在下一讲展开。

---

## 一、标识符（Identifier）

### 1. 什么是标识符

- 标识符就是给**变量、函数、类、模块或其他对象**起的名字（a name given to entities）。

### 2. 命名规则（Rules）

**✅ 允许的字符（与 C 语言相同）：**
- 字母（A–Z，a–z）
- 数字（0–9）——但**不能以数字开头**
- 下划线（`_`）

**❌ 不允许：**
- 空格或特殊字符，如 `@`、`#`、`$`、`%`、`!`
- 不能是 Python **关键字/保留字**（如 `if`、`else`、`for`、`while`、`def`、`class` 等）

### 3. 合法与非法示例

```python
# ✅ 合法
my_var = 10
_name = "private"
variable1 = 5
user_name = "John"
_private = True
myFunction = "hello"
MyClass = "example"

# ❌ 非法
1variable = 10    # 不能以数字开头
my-var = 20       # 不允许连字符 -
my var = 30       # 不允许空格
class = "test"    # 'class' 是保留关键字
@name = "John"    # 不允许 @ 符号
```

### 4. 命名规范（Naming Conventions，最佳实践）

Python 不强制，但强烈推荐：

| 规范 | 示例 | 适用场景 |
| --- | --- | --- |
| **snake_case**（蛇形命名） | `user_name`、`total_count` | 变量、函数、模块 |
| **PascalCase**（帕斯卡命名） | `MyClass`、`UserProfile` | 类名 |
| **UPPER_CASE**（全大写） | `PI`、`MAX_LIMIT` | 常量 |
| **_single_leading**（单前导下划线） | `_internal` | 约定俗成的"私有" |
| **__double_leading**（双前导下划线） | `__private` | 类中的名称修饰（name mangling） |

### 5. 重要注意事项

- **大小写敏感（Case-sensitive）**：`myvar`、`MyVar`、`MYVAR` 是三个不同的变量。
- **支持 Unicode**：Python 标识符中可以使用 Unicode 字符（如中文变量名），但不常用。
- **Dunder（double underscores，双下划线）**：像 `__init__` 这样的方法在 Python 中有特殊含义。

---

## 二、变量（Variable）

- **变量是内存中存储值的命名容器**（a named container that stores a value in memory）。

**Python 变量的关键特性：**

1. **无需声明（No Declaration Required）**
   - 与很多语言不同，不需要事先声明变量类型，Python 会自动判断。
2. **动态类型（Dynamically Typed）**
   - 变量的类型可以随时改变。
   - 例：`x = 1`（int）之后可以 `x = "hello"`（str）。
3. **大小写敏感（Case-Sensitive）**
   - `myvar`、`MyVar`、`MYVAR` 互不相同。

### 赋值（Assignment）

- 使用 `=` 进行赋值：把等号右侧的值绑定到左侧的名字上。
- Python 中"变量"本质上是对象的**引用（名字标签）**，这也是动态类型的基础。

---

## 三、内置数据类型（Built-in Data Types）

Python 基础内置类型包括：

| 类型 | 英文 | 说明 | 示例 |
| --- | --- | --- | --- |
| 布尔型 | **Boolean** | 只有两个值：`True` / `False` | `is_student = True` |
| 整型 | **Integer** | 整数 | `age = 25` |
| 浮点型 | **Float** | 小数/实数 | `height = 168.6` |
| 复数型 | **Complex** | 复数，虚部用 `j` 表示 | `coeft = 12.3 + 4.56j` |
| 字符串型 | **String** | 文本，用引号包裹 | `name = "Zibang Zhang"` |
| 空型 | **NoneType** | 只有一个值 `None`，表示"空/无" | `supervisor = None` |

### 1. Boolean（布尔型）

```python
is_student = True
is_married = False
```

### 2. Integer（整型）

```python
age = 25
year = 2000
month = 12
day = 25
```

### 3. Float（浮点型）

```python
height = 168.6
weight = 55.0
PI = 3.14159
LIGHT_SPEED = 2.99792458e8        # 光速，科学计数法
dist_sun_earth = 1.49597870700e11 # 日地距离
```

> **课堂练习（Exercise）**：利用光速 `LIGHT_SPEED` 和日地距离 `dist_sun_earth`，计算光从太阳传播到地球需要多长时间。
>
> 参考思路：
> ```python
> time = dist_sun_earth / LIGHT_SPEED   # 单位：秒
> print(time)                           # 约 499 秒 ≈ 8.3 分钟
> ```

### 4. Complex（复数型）

```python
coeft = 12.3 + 4.56j   # 虚部单位用 j（不是数学中的 i）
```

### 5. String（字符串型）

```python
nationality = "China"
name = "Zibang Zhang"
major = "光电信息科学与工程"   # 支持 Unicode/中文
```

### 6. NoneType（空型）

```python
supervisor = None   # None 表示"没有值/空"，类似其他语言的 null
```

---

## 要点速记

- **标识符**：由字母、数字、下划线组成，不能数字开头，不能用关键字；大小写敏感。
- 命名规范：变量/函数/模块用 `snake_case`，类用 `PascalCase`，常量用 `UPPER_CASE`，`_x` 表约定私有，`__x` 触发类中的名称修饰。
- **变量三特性**：无需声明、动态类型、大小写敏感。
- Python 六大基础内置类型：**bool、int、float、complex、str、NoneType**。
- 布尔值是 `True`/`False`（首字母大写）；复数虚部用 `j`；空值是 `None`。
- 浮点数可用科学计数法：`2.99792458e8`。
- 练习：光从太阳到地球约需 `1.49597870700e11 / 2.99792458e8 ≈ 499 秒`（约 8.3 分钟）。
