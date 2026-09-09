# Lecture 02. Fundamentals in Computer Science 计算机科学基础笔记

> 课程：Advanced Programming（高级编程）
> 主题：计算机的组成——硬件（Hardware）与软件（Software）

---

## 一、总览（The Big Picture）

- 计算机种类繁多、形态各异：从洗衣机里的微小芯片，到占满整个房间的巨型机器。
- 计算机由两大部分组成：
  - **硬件（Hardware）**：摸得着的物理部件（the physical parts you can touch）。
  - **软件（Software）**：看不见的指令，告诉硬件该做什么（the invisible instructions）。

---

## 二、硬件 Hardware —— 计算机的"身体"

计算机硬件系统的基本组成：

| 部件 | 角色 |
| --- | --- |
| **CPU**（中央处理器） | 计算机的"大脑" |
| **Memory**（内存：RAM、ROM、cache 缓存） | 数据暂存 |
| **Storage**（存储器：硬盘 HDD、固态硬盘 SSD） | 长期保存数据 |
| **Motherboard**（主板） | 连接所有部件 |
| **Input/Output devices**（输入/输出设备） | 键盘、显示器等 |
| **Bus systems**（总线系统） | 各部件之间数据传输的通道 |
| **Power supply & cooling**（电源与散热系统） | 供电与降温 |

### 1. CPU（Central Processing Unit，中央处理器）

- 计算机的"**大脑**"，执行程序指令，完成所有基本的**算术、逻辑、控制和输入/输出（I/O）**操作。
- 主要厂商：**Intel、AMD**。

**关键指标（Key specifications）：**

| 指标 | 说明 |
| --- | --- |
| Clock speed（主频） | 单位 GHz，越高越快 |
| Cores（核心数） | 独立处理单元数量 |
| Threads（线程数） | 可并行执行的任务线程 |
| Cache memory（缓存） | L1 ~ L3，CPU 内部高速缓存 |
| TDP（热设计功耗） | 单位瓦特（W），反映功耗与散热需求 |

**实例对比（课件数据）：**

| 指标 | Intel Core i9-14900K（台式机） | Intel Core i5-8250U（笔记本） |
| --- | --- | --- |
| 主频 | 基准 3.2 GHz（P 核）/ 2.4 GHz（E 核），最大睿频 6.0 GHz | 基准 1.60 GHz，最大睿频 3.40 GHz |
| 核心 | 24 核（8 个性能核 P-cores + 16 个能效核 E-cores） | 4 核 |
| 线程 | 32 线程 | 8 线程 |
| 缓存 | L3：36 MB；L2 共 32 MB | L3：6 MB（Intel Smart Cache） |
| TDP | 基准 125 W，最大睿频 253 W | 基准 15 W，最大约 10~25 W |

> 注：现代 Intel 酷睿采用 **P-core（性能核）+ E-core（能效核）** 的混合架构。

### 2. RAM（Random Access Memory，随机存取存储器/内存）

- 计算机的**短期、临时存储器**。
- 属于**易失性存储器（volatile memory）**：关机或重启后，RAM 中的所有数据**立即丢失**。

**关键指标：**

| 指标 | 说明 |
| --- | --- |
| Capacity（容量） | 8 GB、16 GB、32 GB、64 GB+ |
| Speed（速度） | 单位 MHz 或 MT/s；DDR4：2133~3200 MHz；DDR5：4800~8000+ MHz |
| Latency（延迟） | 越低越好 |

### 3. Storage（外存储器）

| 类型 | 原理 | 特点 |
| --- | --- | --- |
| **HDD**（Hard Disk Drive，机械硬盘） | **机械结构**：内部有旋转的磁碟（类似 CD/唱片）和来回移动的读写磁头，本质上是一台精密的唱片机 | 容量大、便宜；速度慢、怕震动 |
| **SSD**（Solid State Drive，固态硬盘） | **电子结构**：无运动部件，使用 **NAND 闪存芯片**（类似一个巨大的高速 U 盘），通过电路瞬间访问数据 | 速度快、抗震；价格相对高 |

---

## 三、软件 Software —— 看不见的指令

软件分为两个主要层次：

1. **系统软件（System software）**：管理计算机本身，如操作系统（OS）、驱动程序等。
2. **应用软件（Application software）**：完成用户具体任务，如浏览器、Word、游戏。

### 1. 操作系统（Operating System, OS）

- 计算机上**最重要的软件**，充当"桥梁/中间人"：
  - 连接**用户**与**硬件**（CPU、RAM、存储器、键盘、鼠标、屏幕）；
  - 连接**应用程序**（浏览器、Word、游戏）与机器的物理部件。

### 2. Microsoft Windows 简史

- 微软公司开发和销售的图形操作系统家族，自 **1985 年**首次发布以来，成为全球使用最广泛的 PC 操作系统。

| 版本 | 年份 | 备注 |
| --- | --- | --- |
| Windows 1.0 | 1985 | 首个版本 |
| Windows 3.0 | 1990 | |
| Windows 95 | 1995 | "The Revolution"（革命性版本） |
| Windows XP | 2001 | 经典版本 |
| Windows Vista | 2007 | |
| Windows 7 | 2009 | 口碑极佳 |
| Windows 8 / 8.1 | 2012–2013 | |
| Windows 10 | 2015 | |
| Windows 11 | 2021 – 至今 | 最新 |

### 3. 课件推荐的应用软件

- 操作系统：Windows 10 LTSC 2021 / Windows 7

| 软件 | 用途 |
| --- | --- |
| WinRAR | 文件压缩与归档 |
| Supermium | 网页浏览器 |
| Office 2016 / Office 2010 | 办公套件 |
| HoneyView | 图片查看器 |
| K-Lite | 带解码器包的视频播放器 |
| Winamp | 音频/媒体播放器 |
| Notepad++ | 文本/代码编辑器 |
| WinHex | 十六进制编辑器 |

---

## 四、计算机如何协同工作（Putting Them All Together）

各层次关系（自底向上）：

```
输入/输出设备（键盘、显示器等）
        ↑↓
操作系统（OS）
        ↑↓
应用程序（App） + 数据（Data）
        ↑↓
CPU  ←→  RAM（内存）  ←→  Storage（硬盘/SSD）
```

- 数据和程序平时存放在 **Storage（硬盘/SSD）**中；
- 运行时被加载到 **RAM（内存）**；
- **CPU** 从内存中取指令、执行运算；
- **OS** 负责调度管理这一切；
- 用户通过**输入/输出设备**与计算机交互。

**补充：键盘（Keyboard）**
- 标准键盘约有 **104 ~ 108 个按键**。

---

## 要点速记

- 计算机 = 硬件（可触摸的物理部件）+ 软件（看不见的指令）。
- 硬件七大部分：CPU、内存（RAM/ROM/Cache）、存储器（HDD/SSD）、主板、I/O 设备、总线、电源散热。
- CPU 指标：主频（GHz）、核心数、线程数、缓存（L1~L3）、TDP（W）；厂商 Intel、AMD。
- RAM 是**易失性**临时存储，断电数据即失；DDR4/DDR5 看 MHz。
- HDD 靠旋转磁碟（机械、慢），SSD 靠 NAND 闪存芯片（电子、快）。
- 软件分系统软件与应用软件；**OS 是用户/应用与硬件之间的桥梁**。
- Windows 1.0（1985）→ 95（革命）→ XP（2001）→ 7（2009）→ 10（2015）→ 11（2021）。
- 工作流程：硬盘中的程序/数据 → 调入内存 → CPU 取指执行 → OS 调度 → I/O 交互。
