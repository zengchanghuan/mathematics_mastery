---
title: Calculus Progress - 微积分学习进度
document_type: execution-progress
status: active
updated: "2026-08-14"
current_phase: "Week 2 - 极限与连续"
---

# Calculus Progress — 微积分学习进度

> 当前学习执行状态的唯一入口。训练后更新；不要因为计划日期或单次做对/做错就大幅改变 Mastery。

## 文件分工

- [learning_plan.md](learning_plan.md)：长期路线、阶段边界和验收标准。
- [calculus_tutor.md](calculus_tutor.md)：AI Tutor 的教学与出题规则。
- [calculus/01_limits/README.md](calculus/01_limits/README.md)：当前章节的例题、错因和学习证据。
- 本文件：当前焦点、掌握判断、薄弱点和下一轮训练队列。

## Current Focus

**极限与连续主线：渐近线间隔复测 + Week 2 未覆盖内容。**

当前先巩固空点、竖直/水平/斜渐近线和多项式除法中的负号稳定性，再补齐连续与介值定理、夹逼定理、基本三角极限及 ε-δ 直觉。

计算型定积分专项仍保留为长期重点，但它属于 Week 4 的积分核心和 Phase 5 的一元微积分补全，不作为现在的起点。进入前必须先通过极限、导数、基本积分与微积分基本定理的前置门。

```mermaid
flowchart LR
    A[当前 Week 2 极限与连续] --> B[Week 3 导数]
    B --> C[Week 4 积分与基本定理]
    C --> D[第一阶段复盘]
    D --> E[Phase 5 计算型积分专项]
```

## Current Stage

`Limits & Continuity — Developing with Asymptote Retest`

训练流程：**主动回忆 → 识别对象 → 说明依据 → 完成计算 → 检查符号与条件 → 独立变式 → 间隔复测**。

## Mastery Dashboard

| Knowledge Point | Status | Priority |
|---|---|---|
| 代数变形 | 🟡 Developing | Very High |
| 函数基础 | 🟡 Developing | Medium |
| 三角函数基本关系 | 🟡 Developing | High |
| 指数与对数互逆 | 🟡 Developing | High |
| 函数值、极限值与左右极限 | 🟡 Developing | High |
| 直接代入与基本极限运算 | 🟡 Developing | Medium |
| 因式分解/有理化处理 `0/0` | 🟡 Developing | High |
| 空点与竖直渐近线 | 🟡 Developing | High |
| 水平渐近线与无穷远极限 | 🟡 Developing | High |
| 斜渐近线与多项式除法 | 🟡 Developing | Very High |
| 连续与间断分类 | 🟡 Developing | High |
| 介值定理 | ⬜ Not Assessed | Next |
| 夹逼定理与基本三角极限 | ⬜ Not Assessed | Next |
| ε-δ 定义直觉 | ⬜ Not Assessed | Later |
| 导数基本公式 | ⬜ Not Assessed | Week 3 |
| Chain Rule | ⬜ Not Assessed | Week 3 |
| 基本不定积分公式 | ⬜ Not Assessed | Week 4 |
| 换元积分 | ⬜ Not Assessed | Week 4 / Phase 5 |
| 分部积分 | ⬜ Not Assessed | Phase 5 |
| sin/cos 幂次积分 | ⬜ Not Assessed | Phase 5 |
| tan/sec 型积分 | ⬜ Not Assessed | Phase 5 |
| Newton–Leibniz | ⬜ Not Assessed | Week 4 |
| 定积分换元与上下限 | ⬜ Not Assessed | Week 4 / Phase 5 |
| 奇偶性与对称积分 | ⬜ Not Assessed | Phase 5 |
| 区间变换 | ⬜ Not Assessed | Phase 5 |
| 反常积分定义与计算 | ⬜ Not Assessed | Phase 5 |
| 部分分式 | ⬜ Not Assessed | Medium |
| 三角换元 | ⬜ Not Assessed | Later |
| 数列与级数 | ⬜ Not Started | Later |
| Taylor Series | ⬜ Not Started | Later |

> `Not Assessed` 不等于 `Weak`。没有实际答题证据时，不提前给未来主题贴上薄弱标签。

## Current Weaknesses with Evidence

1. 多项式除法中，减去整行时容易漏掉变号。
2. 负系数相除或抄写完整“小尾巴”时可能丢失负号。
3. 渐近线方法已能完成，但还缺跨日、无提示复测证明长期稳定。
4. 连续条件中，仍需稳定区分“左右极限不等”和“极限值不等于函数值”。
5. 指数/对数互逆、特殊角、定义域和值域等预备知识尚未完成滚动复测。

## Next Training Queue

- [ ] 负系数多项式除法：1 道无提示题，并做乘回验算。
- [ ] 渐近线混合分类：1 道含空点与至少两类渐近线的题。
- [ ] 连续与间断迁移：2—3 道，要求逐项检查三个条件。
- [ ] 因式分解或共轭有理化极限：2 道无提示复习题。
- [ ] 三角最小前置复测：特殊角、弧度制、单位圆、基本恒等式。
- [ ] 基本三角极限与夹逼定理：先讲直觉和完整例题，再做变式。
- [ ] ε-δ：先说明它解决什么问题，再决定是否进入基础证明。
- [ ] Week 2 章节检查：基础题达到 80%，并能口头解释极限与连续的区别。

## Future Integration Target Problem Families

> 以下内容保留为 Phase 5 计算型积分专项的设计草案，当前不按此队列出题。

### A. 三角函数定积分

重点识别 $\int\sin^m x\cos^n x\,dx$：

- sin 奇数 → 留一个 sin → $u=\cos x$
- cos 奇数 → 留一个 cos → $u=\sin x$
- 两者均偶数 → 降幂

同时训练 $\sec^n x$ 与 tan/sec 混合结构。

### B. 对数 + 分部积分

典型结构：

$$\int\frac{\ln(1+x)}{x^2}\,dx,\qquad \int\frac{\ln x}{(1+x)^2}\,dx$$

目标：看到 logarithm 时主动检查分部积分。

### C. 反常积分

典型结构：

$$\int_1^\infty f(x)\,dx$$

首先转成：

$$\lim_{R\to\infty}\int_1^R f(x)\,dx$$

### D. 定积分对称与区间变换

重点区间：$[-a,a]$ 与 $[0,\pi/2]$。
看到 $[0,\pi/2]$ 上同时含 sin/cos 时，主动检查 $x\mapsto\pi/2-x$。

## Future Integration Weakness Hypotheses

以下只是未来专项启动时需要验证的假设，不代表当前测评结论：

1. 三角积分中对奇偶次策略还没有形成条件反射。
2. 换元时对“内层函数 + 导数因子”的识别需要强化。
3. 分部积分中 $u,dv$ 的选择需要专项练习。
4. 定积分换元后的上下限处理需要自动化。
5. 遇到 $\infty$ 时要稳定地先转成极限。
6. 需要加强“先识别结构，再计算”的习惯。

## Future Integration Training Queue

- [ ] 三角恒等式快速识别（5—10 题）。
- [ ] 基础换元积分（10 题）。
- [ ] 定积分换元（5—8 题）。
- [ ] 分部积分（8—10 题）。
- [ ] $\sin^m x\cos^n x$ 专项（10 题）。
- [ ] `tan/sec` 专项（5—8 题）。
- [ ] 定积分奇偶性与区间变换（8 题）。
- [ ] 反常积分基础（8—10 题）。
- [ ] 混合计算型定积分（10 题）。

## Session Log Template

### YYYY-MM-DD — Session N

**Topic:**

**Problems:**
- Correct:
- Partial:
- Incorrect:

**Error Types:**
- Pattern Recognition:
- Method Selection:
- Algebra:
- Calculus:
- Boundary:
- Limit:
- Sign:
- Transcription:
- Arithmetic:

**What became clearer:**
-

**Still weak:**
-

**Mastery changes:**
-

**Next session:**
-

## Update Rule

- 每次训练结束后，只更新有证据支持的项目。
- 一次正确只说明“本轮会做”，不能直接升为 Mastered。
- 一次粗心或转录错误不直接降为 Weak，但必须记录并设计针对性复测。
- “暂时通过”需要达到章节标准；Mastered 还需要间隔复测和迁移题证据。
