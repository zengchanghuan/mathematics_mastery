# Mathematics Mastery

> A systematic journey from calculus to the mathematical foundations of artificial intelligence.
>
> 从微积分、线性代数、概率统计出发，建立面向计算机科学与人工智能的数学知识体系。

## 项目定位

这不是一个只收集公式和答案的笔记仓库，而是一套长期迭代的数学学习系统。它用于记录概念理解、严格定义、推导过程、习题证据、错误修正和代码实验，最终沉淀成一套可以复习、检验、讲授和复用的个人数学教材。

第一阶段从 **2026-08-05** 开始，用 90 天建立微积分、线性代数、概率统计的核心框架，并通过数值计算和小型项目把抽象概念落到可观察的结果上。

这 90 天是基础框架，不等于完整覆盖《斯图尔特微积分》第 9 版。第一阶段之后继续补全一元微积分，并正式进入多元微积分。

详细安排见 [learning_plan.md](learning_plan.md)。

## 学习目标

- 建立从函数、极限到微积分的连续知识链。
- 从一元函数的变化率与累积量，逐步扩展到多元函数、梯度、重积分和向量场。
- 理解向量、矩阵、线性变换、特征值与 SVD 的几何意义。
- 掌握条件概率、随机变量、常见分布、统计推断与线性回归的基础。
- 能用 Python/NumPy 对公式、算法和直觉进行数值验证与可视化。
- 形成稳定的学习闭环：理解 → 推导 → 练习 → 纠错 → 讲解 → 复习。
- 为机器学习、深度学习、计算机视觉和信号处理建立数学基础。

## 什么算“掌握”

一个主题只有在留下可验证证据后，才从“看过”变成“掌握”：

1. 能不用教材，用自己的话解释直觉和适用范围。
2. 能写出严格定义，并说明符号和前提条件。
3. 能完成典型推导，知道每一步使用了什么结论。
4. 能独立解决基础题、变式题和一道综合题。
5. 能识别自己的常见错误，并解释错误产生的原因。
6. 能用图像、数值实验或代码验证结论。
7. 间隔一段时间后，仍能通过复习测试。

“Mastery” 是持续逼近的过程，不是一次学习后的标签。

## 学习路线

| 阶段 | 主题 | 核心问题 | 实践输出 |
| --- | --- | --- | --- |
| Phase 1 | 一元微积分核心 | 变化率与累积量如何被严格描述？ | 极限可视化、黎曼和与数值积分 |
| Phase 2 | 线性代数 | 如何用向量空间和线性变换描述数据？ | 最小二乘、特征向量、SVD 图像压缩 |
| Phase 3 | 概率统计 | 如何描述不确定性并从样本作出判断？ | 蒙特卡洛、大数定律与中心极限定理模拟 |
| Phase 4 | AI 数学 | 上述工具如何共同支撑模型训练？ | 从零实现线性回归与梯度下降 |
| Phase 5 | 一元微积分补全 | 级数、参数曲线和微分方程如何扩展微积分工具？ | Taylor 逼近、极坐标曲线与微分方程实验 |
| Phase 6 | 多元微积分 | 多个变量共同变化时，如何描述局部变化与整体累积？ | 梯度场、重积分、曲线积分与曲面积分可视化 |
| Phase 7 | 优化与机器学习数学 | 如何在高维空间中分析并训练模型？ | Jacobian、Hessian、约束优化与数值优化实验 |

## 仓库结构

以下目录会随着学习进度逐步创建，避免在尚未学习时预先堆积空文件：

```text
mathematics_mastery/
├── README.md
├── learning_plan.md
├── calculus/
│   ├── 00_preparation/
│   ├── 01_limits/
│   ├── 02_derivatives/
│   ├── 03_integrals/
│   ├── 04_multivariable/
│   └── exercises/
├── linear_algebra/
│   ├── 01_vectors/
│   ├── 02_matrices/
│   ├── 03_vector_spaces/
│   ├── 04_linear_transforms/
│   ├── 05_eigenvalues/
│   └── 06_svd/
├── probability_statistics/
│   ├── probability/
│   ├── random_variables/
│   ├── distributions/
│   ├── statistical_inference/
│   └── regression/
├── exercises/
│   ├── solved/
│   └── mistakes/
├── ai_prompts/
├── projects/
│   ├── numerical_calculus/
│   ├── monte_carlo/
│   ├── svd_image_compression/
│   └── linear_regression/
└── resources.md
```

## 章节模板

每个主题尽量采用同一结构，让笔记既能学习，也能用于复习和自测：

```markdown
# Topic / 主题

## 1. Intuition / 直觉
## 2. Formal Definition / 严格定义
## 3. Geometric Meaning / 几何意义
## 4. Important Theorems / 重要定理
## 5. Derivations / 推导
## 6. Examples / 例题
## 7. Exercises / 练习
## 8. Mistakes / 错误与修正
## 9. Code Experiment / 代码实验
## 10. AI Discussion / AI 讨论与核验
## 11. Review Questions / 复习问题
```

AI 讨论只作为启发、追问和反馈来源。关键定义、定理条件、推导和答案需要回到教材或可信资料核验。

## 学习与记录流程

```text
课前回忆 → 概念学习 → 手写推导 → 独立做题
    ↑                              ↓
间隔复习 ← 更新主题笔记 ← 错因分析 ← 答案核验
                         ↓
                    代码实验
```

每天默认投入 90 分钟：

- 15 分钟：主动回忆与复习旧知识。
- 35 分钟：学习一个小而完整的新主题。
- 30 分钟：独立做题或完成推导。
- 10 分钟：记录错误、更新笔记和安排下次复习。

## Git 记录约定

提交应对应一个清晰、可检查的学习增量，而不是一次性填满所有目录。

```text
feat(calculus): add limit intuition notes
feat(linear-algebra): explain vector spaces
fix(probability): correct bayes theorem explanation
experiment: visualize riemann sums
review: complete day 30 checkpoint
```

## 当前里程碑

- [ ] Day 30：完成微积分核心概念检查。
- [ ] Day 60：完成线性代数核心概念检查。
- [ ] Day 84：完成概率统计核心概念检查。
- [ ] Day 90：完成线性回归综合项目与第一阶段复盘。
- [ ] Phase 5：完成一元微积分补全检查。
- [ ] Phase 6：完成多元微积分综合检查和可视化项目。

## 长期方向

第一阶段完成后按以下顺序推进：

1. 补全一元微积分中的积分技巧、参数方程、极坐标、数列与级数和基础微分方程。
2. 进入多元微积分，学习空间几何、偏导数、梯度、重积分、向量场以及 Green、Stokes 和散度定理。
3. 在多元微积分与线性代数基础上继续学习优化、数值分析和机器学习数学。
4. 根据长期目标补充离散数学等计算机科学基础，并持续把仓库沉淀为 AI Tutor 可以检索和用于追问的高质量知识基础。
