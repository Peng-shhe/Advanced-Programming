# Lecture 06 · Object-Oriented Programming 面向对象编程

> Advanced Programming — OOP 概念、面向过程 vs 面向对象、为什么需要 OOP、类与对象、三个建模示例

## 一、什么是面向对象（OOP）

**Object-Oriented Programming（面向对象程序设计）**：一种以**对象**为中心组织代码的编程方式——对象是自包含的"数据（属性 attributes）+ 行为（方法 methods）"共同体，而不是围绕独立的函数和全局数据来组织代码。核心思想：**用程序模拟它所处理的现实世界事物**。

**"对象" = 状态（数据、变量）+ 行为（方法、函数）**，两者不可分割地绑定在一起。现实世界到处是对象：

| 对象 | 状态 | 行为 |
| --- | --- | --- |
| 手机 | 电量、型号、使用时长 | 打电话、发消息、拍照 |
| 银行账户 | 余额 | 存款、取款、查余额 |
| 猫 | 名字、年龄、饥饿程度 | 叫、吃、睡 |

**"面向"（oriented）**= 朝向、以……为方向：
- 面向过程：以"**步骤/过程**"为中心组织程序
- 面向对象：以"**对象**"为基本单位思考和构建系统

## 二、面向过程 vs 面向对象

| | 面向过程 | 面向对象 |
| --- | --- | --- |
| 基本单位 | 函数/步骤 | 对象 |
| 数据与行为 | 分离 | 绑定在一起 |
| 思考方式 | 先做什么，再做什么 | 有哪些事物，它们如何协作 |
| 例子 | `deposit(account, 100)` | `account.deposit(100)` |

> 面向过程是"**动作作用于数据**"，面向对象是"**对象自己完成动作**"——这是思维上的根本转变。

**OOP 世界观**：世界由一个个具有自主行为的事物组成，复杂系统通过事物之间的协作来运转。以下单为例：
- 面向过程：一个大函数依次调用 检查库存 → 扣减库存 → 生成订单 → 扣款 → 发通知
- 面向对象：用户、购物车、商品、库存、订单、支付服务、通知服务各自管好自己的事，**下单就是这些对象互相发消息、协作的结果**

面向对象不是在"写流程"，而是在"**搭建一个由对象组成的小社会**"——每个对象有自己的职责，彼此通过接口（公有的函数）沟通。这更接近现实世界的运作方式，也更容易应对复杂度和变化。

## 三、为什么需要 OOP（历史视角）

1960–70 年代软件规模快速增长，**面向过程在大规模下开始崩溃**：

**问题 A：数据与行为分散**——数据是全局的，任何函数都能修改它：

```python
balance = 1000.0
def deposit(amt: float) -> None:
    global balance
    balance += amt
def withdraw(amt: float) -> None:
    global balance
    balance -= amt
```

程序一大，任何函数都能改 `balance`，没人知道谁改了什么、何时改的、为什么改——**Bug 无法追踪**。

**问题 B：代码重复**——50 个"账户类"事物就要复制粘贴 50 遍逻辑，改一条规则要找齐 50 处。

**问题 C：难以建模复杂系统**——银行、仿真、GUI 里的事物天然有状态和行为，面向过程把每个"事物"拆成散落的变量和函数，丢失自然结构。

**OOP 的回答**：把状态和行为打包进对象，隐藏内部细节，让对象通过接口协作——三大问题一一对应：

| 问题 | OOP 解决方案 |
| --- | --- |
| 数据/行为分散 | **封装（Encapsulation）**——数据存在对象内部 |
| 代码重复 | **继承与组合（Inheritance & Composition）**——复用已有代码 |
| 复杂度建模难 | **对象映射现实实体** |

## 四、OOP 的六大实际好处

1. **可维护性（Maintainability）**：修改是局部的——改 `Account.withdraw()` 规则只需改一处
2. **可复用性（Reusability）**：设计良好的类（Logger、Connection、Button）写一次到处用
3. **可扩展性（Scalability）**：大系统由许多小而独立的对象组成，团队可并行开发不同对象
4. **可拓展性（Extensibility）**：多态让你**不修改现有代码**就能增加新行为（如新增 `SavingsAccount` 不用动 `Account` 及其调用者）
5. **安全性（Safety）**：封装阻止外部代码把对象置于非法状态（如 setter 禁止时无法直接 `balance = -999`）
6. **建模能力（Modeling Power）**：用领域概念（账户、订单、用户）思考和写代码，**代码读起来像问题本身**

## 五、类与对象（Class vs Object）

进行 OOP 的主要工具：**类（class）**。

**类 : 对象 = 数据类型（type）: 变量（variable）**

类是创建对象的**蓝图（blueprint）**，它定义：
- **属性（Attributes）**——对象持有的数据（状态）
- **方法（Methods）**——对象能执行的操作（行为）

```python
class BankAccount:                 # 银行账户
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

## 六、课堂建模示例

三个类的骨架（属性 + 方法签名），用于课堂练习：

**1. Circle（圆）**——数学关系：周长 `C = 2πr`，面积 `S = πr²`；**半径应为正数**

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

**2. Temperature（温度）**——三种温标换算：
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

**3. BankAccount（银行账户）**——见第五节代码：`id` 账号、`_balance` 余额，支持存款、取款、查余额。
