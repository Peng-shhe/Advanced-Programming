# Lecture 01. Introduction 课程导论笔记

> 课程：Advanced Programming（高级编程）
> 教师：张子邦（Zibang Zhang / Charles Cheung），暨南大学光电工程系副教授
> 办公室：蒙民伟理工楼 411；实验室：蒙民伟理工楼 309

---

## 一、课程概况（About This Course）

### 1. 学习内容（What to Learn?）

| 模块 | 内容 |
| --- | --- |
| Programming with Python | Python 编程实践 |
| Basic Algorithms | 基础算法 |
| Fundamentals in Computer Science | 计算机科学基础 |
| English for Computer Science | 计算机专业英语 |

课程大纲分三部分：
- **Part 1**：Python 基础（Basics in Python）
- **Part 2**：常用第三方库（Frequently Used 3rd-party Libraries）
- **Part 3**：综合案例（Cases）

### 2. 为什么学（Why Learn It?）

- **计算机科学基础**：构建计算的理论根基。
- **Python 编程**：能快速把想法变成可运行的代码，加速学习与原型开发。
- **基础算法**：训练逻辑思维与问题求解能力——把复杂任务拆解为清晰的、逐步的指令。
- **专业英语**：提升撰写代码注释、技术文档和专业邮件的能力。

### 3. 如何学（How to Learn It?）

- **多动手实践**：把 Python 知识用于实际。
- **项目驱动学习（Project-based learning）**：最好的学习方式。
- **把 AI 当作编程伙伴，而非拐杖**：
  - ✅ 正确做法：先自己写代码，再让 AI "Review my code and suggest 3 improvements"（审查代码并提 3 条改进建议）。
  - ❌ 错误做法：让 AI 写好一切，自己只复制粘贴。

### 4. 考核方式（Assignments & Final Exam）

- **平时作业**：
  1. 整理、编写每节课的笔记；
  2. 完成所有布置的习题。
- **期末考试**：课程设计项目（course design project），**分组进行**。每组提交一份课程设计作品 + 一份课程设计报告，细节后续公布。
- **在线平台**：
  - http://172.18.58.166:11001/
  - https://im.jnu-diclc.com/

---

## 二、Python 简介

### 1. 名称由来与历史（History）

- Python 本义：巨蛇、大蟒（英 [ˈpaɪθən]，美 [ˈpaɪθɑn]）。
- 由荷兰人 **Guido van Rossum（吉多·范罗苏姆）** 于 **1989 年**开发。
- 命名来自英国喜剧系列《**Monty Python's Flying Circus**》（巨蟒剧团之飞翔的马戏团），与蛇无关。

关键版本节点：

| 时间 | 版本 |
| --- | --- |
| 1991 年 2 月 | Python 0.9.0（首个版本） |
| 1994 年 1 月 | Python 1.0 正式发布，社区开始快速增长 |
| 2000 年 10 月 | Python 2.0 |
| 2008 年 12 月 | Python 3.0 |
| 2026/8/29（课件日期） | 最新版 Python 3.14.7 |

- 官网：https://www.python.org/

### 2. Python 的优点（Advantages）

1. **对初学者极其友好（Beginner Friendliness）**
   - 语法几乎像 plain English（自然英语）；
   - 用**缩进（indentation）**代替花括号和分号。
2. **开发速度极快（Development Speed）**
   - 动态类型、"batteries-included"（自带电池/开箱即用）的标准库、语法简洁；
   - 写出同样可运行程序的时间约为 Java 或 C++ 的 **1/5**。
3. **"瑞士军刀"式的生态系统（Ecosystem）**
   - 数据科学与 AI、Web 后端、自动化与脚本、科学计算等领域全覆盖。
4. **庞大的社区支持（Community Support）**。
5. **优秀的企业支持（Corporate Backing）**。

### 3. Python 的缺点（Disadvantages）

1. **执行速度慢（最大短板）**：明显慢于 C、C++、Java。
2. **全局解释器锁（GIL, Global Interpreter Lock）**：
   - 一种互斥锁（mutex）机制，同一进程内**同一时刻只允许一个线程执行 Python 字节码**，限制多线程并行。
3. **内存消耗高（High Memory Consumption）**。
4. **移动端开发能力弱（Mobile Development is Weak）**。
5. **运行时错误（Runtime Errors）**：
   - 动态类型导致很多错误在代码**实际运行时**才被解释器发现。
6. **版本与依赖管理问题（"Dependency Hell" 依赖地狱）**：
   - 同一包在 Python 3.8 可用、在 3.11 可能出错；两个包可能依赖同一库的冲突版本。

---

## 三、开发环境（IDE Deployment）

- **IDE**：Integrated Development Environment，集成开发环境。

### 1. 内置 IDE：IDLE

启动方式：
- **开始菜单**：点击 Windows 开始按钮 → 输入 `IDLE` 或 `Python` → 点击 "IDLE (Python GUI)"；
- **命令提示符（Command Prompt）**：输入 `idle`。

### 2. 推荐环境：Miniconda + Visual Studio Code (VSCode)

- **Miniconda = Python + 少量必需依赖**（轻量级的 Python 发行版）：
  - 下载：https://repo.anaconda.com/miniconda/
- **VSCode**：微软开发的免费、轻量、开源代码编辑器，2015 年首次发布：
  - 下载：https://code.visualstudio.com/

课件还演示了在 Windows 7 上安装 Miniconda 和 VSCode 的步骤。

---

## 要点速记

- Python 1989 年由 Guido van Rossum 创建，名字来自喜剧《Monty Python》；Python 3.0 于 2008 年发布。
- 优点：语法简单、开发快、生态强、社区大；缺点：速度慢、GIL、占内存、移动端弱、运行时才报错、依赖地狱。
- GIL：同一时刻只有一个线程执行 Python 字节码。
- 学习方法：项目驱动 + 自己先写代码再让 AI 提改进意见。
- 考核：平时笔记与习题 + 期末分组课程设计（作品 + 报告）。
- 推荐环境：Miniconda + VSCode（内置 IDE 为 IDLE）。
