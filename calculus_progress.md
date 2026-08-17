---
title: Calculus Progress - 微积分学习进度
document_type: execution-progress
status: active
updated: "2026-08-17"
current_phase: "Week 3 - 导数核心；短暂回补第一章目录缺口"
---

# Calculus Progress — 微积分学习进度

> 本文件保存详细阶段仪表板；跨设备恢复的唯一精确停点在 [calculus/PROGRESS.md](calculus/PROGRESS.md)。不要因为计划日期或单次做对/做错就大幅改变 Mastery。

## 文件分工

- [learning_plan.md](learning_plan.md)：长期路线、阶段边界和验收标准。
- [calculus_tutor.md](calculus_tutor.md)：AI Tutor 的教学与出题规则。
- [calculus/01_limits/README.md](calculus/01_limits/README.md)：极限、连续、错因和待回补内容。
- [calculus/02_derivatives/README.md](calculus/02_derivatives/README.md)：当前导数章节的定义、推导、例题和学习证据。
- [calculus/PROGRESS.md](calculus/PROGRESS.md)：当前精确停点和下一道题。
- 本文件：详细阶段、掌握判断、薄弱点和长期训练队列。

## Current Focus

**导数主线：完成教材目录缺口的最小回补后，从商法则继续。**

Week 2 章节检查为 \(3.5/4=87.5\%\)，已经达到进入导数的门槛。当前已学习导数定义、切线、幂函数、线性运算和乘积法则。学习者确认幂函数、线性运算和乘积法则较熟悉；按照掌握优先原则跳过当堂重复练习，但保留跨日抽查。

对照学习者提供的教材目录，先补数列极限、无穷小比较和闭区间连续函数性质。学习到 \(1-\cos x\sim x^2/2\) 时发现三角恒等式的证明链条尚未建立，因此在当前位置插入[三角学桥接复习](calculus/00_preparation/trigonometry_bridge_review.md)。弧度、单位圆和基础特殊角不重复，直接补和差角、倍角、半角、降幂与积化和差的证明和应用；完成后返回无穷小比较，再回到商法则。

计算型定积分专项仍保留为长期重点，但它属于 Week 4 的积分核心和 Phase 5 的一元微积分补全，不作为现在的起点。进入前必须先通过极限、导数、基本积分与微积分基本定理的前置门。

```mermaid
flowchart LR
    A[闭区间连续函数性质补全] --> B[商与链式法则]
    B --> C[特殊函数求导与微分]
    C --> D[微分中值定理与导数应用]
    D --> E[基础不定积分]
    E --> F[定积分与基本定理]
    F --> G[Phase 5 计算型积分专项]
```

## Current Stage

`Derivative Core — Product Rule Passed; Chapter 1 Gap Repair In Progress`

训练流程：**主动回忆 → 识别对象 → 说明依据 → 完成计算 → 检查符号与条件 → 独立变式 → 间隔复测**。

## Mastery Dashboard

| Knowledge Point | Status | Priority |
|---|---|---|
| 代数变形 | 🟡 Developing | Very High |
| 函数基础 | 🟡 Developing | Medium |
| 三角函数基本关系 | 🟡 Developing | High |
| 三角恒等式的证明与应用 | 🟡 Developing | Immediate Bridge |
| 指数与对数互逆 | 🟡 Developing | High |
| 函数值、极限值与左右极限 | 🟡 Developing | High |
| 直接代入与基本极限运算 | 🟡 Developing | Medium |
| 因式分解/有理化处理 `0/0` | 🟡 Developing | High |
| 空点与竖直渐近线 | 🟡 Developing | High |
| 水平渐近线与无穷远极限 | 🟡 Developing | High |
| 斜渐近线与多项式除法 | 🟡 Developing | Very High |
| 连续与间断分类 | 🟡 Developing | High |
| 介值定理 | 🟡 Developing | Review |
| 零点定理正式条件 | 🟡 Developing | Retest |
| 闭区间连续函数性质 | 🟡 Developing | Retest |
| 一致连续性 | 🟡 Developing | Retest |
| 数列极限与收敛性质 | 🟡 Developing | Gap Repair |
| 无穷小比较与等价无穷小 | 🟡 Developing | Gap Repair |
| 夹逼定理与两个重要极限 | 🟡 Developing | Review |
| ε-δ 定义直觉 | 🟡 Developing | Review |
| 导数定义与切线 | 🟡 Developing | High |
| 幂函数求导 | 🟡 Developing（自述熟悉） | Retest |
| 线性运算求导 | 🟡 Developing（自述熟悉） | Retest |
| 乘积法则 | 🟡 Developing（自述熟悉） | Retest |
| 商法则、反函数求导 | ⬜ Not Assessed | Next |
| Chain Rule | ⬜ Not Assessed | Week 3 |
| 三角、指数、对数函数导数 | ⬜ Not Assessed | Week 3 |
| 微分中值定理链条 | ⬜ Not Assessed | Week 3 |
| 洛必达法则与有限阶 Taylor 公式 | ⬜ Not Assessed | Week 3 |
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

1. 导数函数和指定点的斜率曾发生混淆；需要继续执行“先求公式，再代入横坐标”。
2. 点斜式切线方程已经完成基础订正，但还缺跨日无提示复测。
3. \(\varepsilon\) 与 \(\delta\) 的角色曾受题目顺序影响，需要间隔复测输入距离与输出误差。
4. 介值定理的根区间曾把开区间写成闭区间；本次零点定理存在性题已经正确写成 \(c\in(1,2)\)，仍需间隔复测确认稳定。
5. 渐近线、多项式除法和负号运算已能完成当前题目，但长期稳定性仍待 2026-08-19 复测。

## Next Training Queue

- [x] 严格定义和直观讲解有界性、最大值最小值定理。
- [x] 零点定理已完成存在性题和条件辨认变式。
- [ ] 2026-08-19：无提示复测闭区间连续函数性质与零点定理全部条件。
- [x] 从严格定义、几何直观和线性函数证明学习一致连续性。
- [ ] 2026-08-19：无提示复测线性函数一致连续证明和负斜率的绝对值。
- [ ] 短单元补数列极限、无穷小比较和连续函数运算。
- [ ] 按定义、几何、证明、例题、练习完成三角学桥接复习。
- [ ] 返回导数主线：商法则 → 反函数求导 → 链式法则。
- [ ] 完成三角、指数、对数函数求导与基础隐函数求导。
- [ ] 按费马 → 罗尔 → 拉格朗日 → 柯西的顺序学习微分中值定理。
- [ ] 2026-08-19：间隔复测渐近线、负号、\(\varepsilon\)/\(\delta\)、切线斜率和自述熟悉的三类求导法则。

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
