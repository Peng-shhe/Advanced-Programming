# Lecture 06 · Object-Oriented Programming 面向对象编程

> Advanced Programming — 张子邦（暨南大学光电工程系）
> OOP 概念、面向过程对比、类与对象、self、特殊方法（魔术方法）、仙剑奇侠传实战案例

## 一、什么是面向对象（OOP）

**Object-Oriented Programming（面向对象程序设计）**：一种围绕**对象**组织代码的编程方式——对象是自包含的"数据（属性 attributes）+ 行为（方法 methods）"共同体，而不是围绕独立的函数和全局数据。核心思想：**用程序模拟它所处理的现实世界事物**。

**"面向"（oriented）** = 朝向、以……为方向：
- 面向过程：以"**步骤/过程**"为中心组织程序
- 面向对象：以"**对象**"为基本单位思考和构建系统

**对象 = 状态（数据、变量）+ 行为（方法、函数）**，两者不可分割地绑定在一起：

| 对象 | 状态 | 行为 |
| --- | --- | --- |
| 手机 | 电量、型号、使用时长 | 打电话、发消息、拍照 |
| 银行账户 | 余额 | 存款、取款、查余额 |
| 猫 | 名字、年龄、饥饿程度 | 叫、吃、睡 |

## 二、面向过程 vs 面向对象

| | 面向过程 | 面向对象 |
| --- | --- | --- |
| 基本单位 | 函数/步骤 | 对象 |
| 数据与行为 | 分离 | 绑定在一起 |
| 思考方式 | 先做什么，再做什么 | 有哪些事物，它们如何协作 |
| 例子 | `deposit(account, 100)` | `account.deposit(100)` |

> 关键区别：面向过程是"**动作作用于数据**"，面向对象是"**对象自己完成动作**"。

**OOP 世界观**（理解面向对象最深刻的地方）：世界由具有自主行为的事物组成，复杂系统通过事物协作运转。以下单为例：
- 面向过程：一个大函数依次调用 检查库存 → 扣减库存 → 生成订单 → 扣款 → 发通知
- 面向对象：用户、购物车、商品、库存、订单、支付服务、通知服务各管各的事——购物车"结算"、库存"扣减"、订单"生成"、支付"扣款"、通知"发消息"，**下单就是对象互相发消息、协作的结果**

面向对象不是在"写流程"，而是在"**搭建一个由对象组成的小社会**"——每个对象有自己的职责，通过接口（公有函数）沟通。

## 三、为什么需要 OOP

1960–70 年代软件规模快速增长，面向过程在大规模下崩溃：

**问题 A：数据与行为分散**——数据全局，任何函数都能修改：

```python
balance = 1000.0
def deposit(amt: float) -> None:
    global balance
    balance += amt
def withdraw(amt: float) -> None:
    global balance
    balance -= amt
def transfer(amt: float, target_account) -> None:
    global balance
    balance -= amt
```

任何函数都能改 `balance`，没人知道谁改了什么——**Bug 无法追踪**。

**问题 B：代码重复**——50 个"账户类"事物复制粘贴 50 遍，改一条规则要改 50 处。

**问题 C：难以建模复杂系统**——银行、仿真、GUI 中的事物天然有状态和行为，面向过程把每个"事物"拆成散落的变量和函数，丢失自然结构。

**OOP 的回答**：状态和行为打包进对象，隐藏内部细节，通过接口协作：

| 问题 | OOP 解决方案 |
| --- | --- |
| 数据/行为分散 | **封装（Encapsulation）**——数据存在对象内部 |
| 代码重复 | **继承与组合（Inheritance & Composition）**——复用已有代码 |
| 复杂度建模难 | **对象映射现实实体** |

## 四、OOP 的六大实际好处

1. **可维护性（Maintainability）**：修改局部化——改 `Account.withdraw()` 规则只需改一处
2. **可复用性（Reusability）**：设计良好的类（Logger、Connection、Button）写一次到处用
3. **可扩展性（Scalability）**：大系统由小而独立的对象组成，团队可并行开发
4. **可拓展性（Extensibility）**：多态让你**不改现有代码**就增加新行为（新增 `SavingsAccount` 不用动 `Account`）
5. **安全性（Safety）**：封装阻止外部代码把对象置于非法状态（setter 禁止时无法 `balance = -999`）
6. **建模能力（Modeling Power）**：用领域概念（账户、订单、用户）写代码，**代码读起来像问题本身**

## 五、类与对象（Class vs Object）

进行 OOP 的主要工具：**类（class）**。类是创建对象的**蓝图（blueprint）**，定义：
- **属性（Attributes）**——对象持有的数据（状态）
- **方法（Methods）**——对象能执行的操作（行为）

**类 : 对象 = 数据类型（type）: 变量（variable）**

```python
guangzhou_temperature = Temperature()   # 一个类可以实例化出任意多个对象
tokyo_temperature     = Temperature()
cpu_temperature       = Temperature()
```

## 六、self 是什么

`self` 是**当前实例的引用**——对象通过它访问自己的属性和方法：

```python
class Dog:
    def __init__(self, name):
        self.name = name          # 存储到当前这个实例上
    def bark(self):
        print("%s says woof!" % (self.name))

d = Dog("Rex")
d.bark()                          # 输出：Rex says woof!
```

## 七、特殊方法（魔术方法 / dunder 方法）

双下划线包围的预定义方法（`__method__`），让自定义类与 Python 内置特性集成。

**① 对象生命周期（Object Lifecycle）**

| 方法 | 调用时机 |
| --- | --- |
| `__new__(cls, ...)` | `__init__` 之前，**创建**实例 |
| `__init__(self, ...)` | 创建后，**初始化**实例 |
| `__del__(self)` | 对象即将被**销毁**时 |

```python
class Example:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super().__new__(cls)
    def __init__(self, value):
        print("Initializing instance")
        self.value = value
    def __del__(self):
        print("Destroying instance")
```

**② 字符串表示（String Representation）**

| 方法 | 用途 | 触发方式 |
| --- | --- | --- |
| `__str__` | 人类可读字符串 | `print()`、`str()` |
| `__repr__` | 无歧义字符串（调试用） | `repr()`、交互式环境 |

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return "Point(%0.2f, %0.2f)" % (self.x, self.y)
    def __repr__(self):
        return "Point(x=%0.2f, y=%0.2f)" % (self.x, self.y)

p = Point(1, 2)
print(p)        # Point(1.00, 2.00)   ← 注意 %0.2f 保留两位小数
print(repr(p))  # Point(x=1.00, y=2.00)
```

**③ 算术运算符重载（Arithmetic Operators）**——让对象支持 `+` `-` `*` `/` 等运算：

| 方法 | 对应运算 | 方法 | 对应运算 |
| --- | --- | --- | --- |
| `__add__` | `v1 + v2` | `__truediv__` | `v / 3` |
| `__sub__` | `v1 - v2` | `__neg__` | `-v` |
| `__mul__` | `v * 3` | `__abs__` | `abs(v)` |
| `__rmul__` | `3 * v`（反向乘法） | | |

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):      return Vector(self.x + other.x, self.y + other.y)  # v1 + v2
    def __sub__(self, other):      return Vector(self.x - other.x, self.y - other.y)  # v1 - v2
    def __mul__(self, scalar):     return Vector(self.x * scalar, self.y * scalar)    # v * 3
    def __rmul__(self, scalar):    return self * scalar                               # 3 * v
    def __truediv__(self, scalar): return Vector(self.x / scalar, self.y / scalar)    # v / 3
    def __neg__(self):             return Vector(-self.x, -self.y)                    # -v
    def __abs__(self):             return (self.x**2 + self.y**2) ** 0.5              # abs(v)
```

> `__rmul__` 用于处理 `3 * v` 这种"数字在左、对象在右"的情况——Python 先尝试 `int.__mul__(3, v)` 失败后，再调用 `v.__rmul__(3)`。

## 八、课堂建模示例

三个类的骨架（属性 + 方法签名），用于课堂练习：

**1. BankAccount（银行账户）**

```python
class BankAccount:
    def __init__(self):
        self.id = None             # 账号
        self._balance = None       # 余额
    def deposit(self, amount):     # 存款
        pass
    def withdraw(self, amount):    # 取款
        pass
    def getBalance(self):          # 查余额
        pass
```

**2. Circle（圆）**——周长 `C = 2πr`，面积 `S = πr²`；**半径应为正数**

```python
class Circle():
    def __init__(self):
        self.radius = None         # 半径
        self.x = None              # 圆心坐标
        self.y = None
    def setRadius(self, radius):   # 设置半径（需校验为正）
        pass
    def getArea(self):             # 面积 πr²
        pass
    def getPerimeter(self):        # 周长 2πr
        pass
```

**3. Temperature（温度）**——三种温标换算：
- 摄氏 → 开尔文：`K = °C + 273.15`
- 摄氏 → 华氏：`°F = °C × 1.8 + 32`
- 华氏 → 开尔文：`K = (°F − 32) ÷ 1.8 + 273.15`
- **开尔文不能为负**（绝对零度限制）

```python
class Temperature:
    def __init__(self):
        self.value = None
    def setCelsius(self):          # 用摄氏度设置
        pass
    def getCelsius(self):          # 以摄氏度读取
        pass
    def setFahrenheit(self):       # 用华氏度设置
        pass
    def getFahrenheit(self):       # 以华氏度读取
        pass
    def setKelvin(self):           # 用开尔文设置（不能为负）
        pass
    def getKelvin(self):           # 以开尔文读取
        pass
```

## 九、综合案例：仙剑奇侠传（The Legend of Sword and Fairy）

用 OOP 对回合制 RPG 进行建模，将游戏实体抽象为三个类：**Role（角色）、Skill（法术技能）、Item（物品）**。

### 1. Role 人物角色类

按"身份 / 能力 / 资源 / 状态"四组组织属性，方法按职责分组：

```
Role
├── 属性
│   ├── 身份：name, level
│   ├── 能力：maxHp, maxMp, attack, defense, speed, luck, spirit
│   ├── 资源：hp, mp
│   └── 状态：skills, isAlive, isDefending
│
└── 方法
    ├── 派生：critRate, dodgeRate          # 由属性计算得出（暴击率、闪避率）
    ├── 打印：__str__, printStatus         # 状态展示
    ├── 资源：takeDamage, heal, restoreMp  # 承伤、回血、回蓝
    ├── 战斗：defend, attackTarget, useSkill
    ├── 结算：endTurn                      # 回合结束处理
    └── 成长：levelUp                      # 升级
```

| 属性 | 含义 |
| --- | --- |
| `name`, `level` | 姓名、等级（身份） |
| `maxHp`, `maxMp` | 生命/法力上限 |
| `attack`, `defense` | 攻击、防御 |
| `speed`, `luck`, `spirit` | 速度、幸运、灵力 |
| `hp`, `mp` | 当前生命、法力（资源） |
| `skills` | 掌握的技能列表 |
| `isAlive`, `isDefending` | 是否存活、是否处于防御状态 |

| 方法分组 | 方法 | 职责 |
| --- | --- | --- |
| 派生属性 | `critRate`、`dodgeRate` | 由 luck/speed 等计算暴击率、闪避率 |
| 信息展示 | `__str__`、`printStatus` | 打印角色状态 |
| 资源变化 | `takeDamage`、`heal`、`restoreMp` | 受伤、治疗、恢复法力 |
| 战斗行动 | `defend`、`attackTarget`、`useSkill` | 防御、普攻目标、施放技能 |
| 回合结算 | `endTurn` | 每回合结束的状态更新 |
| 角色成长 | `levelUp` | 升级提升属性 |

### 2. Skill 法术技能类

```
Skill
├── 属性
│   ├── name        技能名
│   ├── mpCost      消耗法力
│   ├── power       威力系数
│   ├── skillType   类型（damage / heal / defend）
│   └── description 描述
│
└── 方法
    └── __init__    构造
```

`skillType` 用字符串区分技能用途：`damage`（伤害型）、`heal`（治疗型）、`defend`（辅助/防御型）。

### 3. Item 物品类

> 注：课件第 35 页 Item 类内容尚未完成（页面展示的仍是 Skill 的结构树），按课堂进度应为独立的物品类，用于封装药品/道具的名称、效果与使用逻辑，待课件更新后补充。

**建模思路小结**：Role 持有 `skills`（Skill 对象列表）体现了**对象之间可以组合协作**——角色施放技能（`useSkill`）时扣减自身 `mp`、调用 Skill 的 `power` 和 `skillType` 计算效果，这正是前面"对象组成的小社会"思想在游戏中的具体应用。
