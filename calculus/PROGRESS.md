---
updated: "2026-08-17"
status: active
current_track: "三角恒等式桥接复习"
---

# 当前学习位置

> 这是换电脑或新会话后的第一读取入口。详细长期仪表板保留在 [../calculus_progress.md](../calculus_progress.md)。

## 精确停点

当前课程：[三角恒等式的证明与练习](lessons/trigonometric-identities.md)。

已经讲解：

- 从 \(\sin^2x+\cos^2x=1\) 推出
  \(1+\tan^2x=\sec^2x\) 和
  \(1+\cot^2x=\csc^2x\)；
- 用两根单位向量的点积证明
  \(\cos(a-b)=\cos a\cos b+\sin a\sin b\)；
- 由奇偶性推出
  \(\cos(a+b)=\cos a\cos b-\sin a\sin b\)；
- 完整例题
  \(\cos15^\circ=(\sqrt6+\sqrt2)/4\)。

当前等待学习者完成：

\[
\boxed{\cos75^\circ=\cos(45^\circ+30^\circ)}
\]

下一位 Tutor 不要跳过这道题，也不要先公布答案。收到答案后先核对符号，再继续正弦和差角公式。

## 为什么暂时离开极限主线

学习

\[
1-\cos x\sim\frac{x^2}{2}
\]

时，恒等式

\[
1-\cos x=2\sin^2\frac{x}{2}
\]

显得突兀。学习者确认弧度、单位圆和基础特殊角已经学过，需要补的是其余三角恒等式的证明、例题和练习。

## 当前短期顺序

1. 完成余弦和差角练习；
2. 证明并练习正弦和差角公式；
3. 推出倍角公式；
4. 推出半角与降幂公式；
5. 补积化和差与和差化积的来源；
6. 返回 \(1-\cos x\sim x^2/2\) 和等价无穷小；
7. 补连续函数运算后返回导数商法则。

## 当前掌握概况

- `Developing`：数列极限定义、\(\varepsilon\)-\(N\) 角色、基本性质、夹逼与单调有界准则。
- `Developing`：无穷小阶数、同阶与等价无穷小；当前因三角公式缺口暂停。
- `Developing`：闭区间连续函数性质、零点定理、一致连续性；等待间隔复测。
- `Developing`：导数定义、切线、幂函数、线性运算和乘积法则。
- `Not Assessed`：商法则、反函数求导、链式法则及后续微分中值定理。

## 跨设备继续方式

在另一台 Mac 拉取后，从仓库根目录执行：

```bash
git pull --ff-only
```

然后让 Tutor 依次读取：

1. `calculus/AGENTS.md`
2. `calculus/PROGRESS.md`
3. `calculus/lessons/trigonometric-identities.md`
4. `calculus/mistakes/active-review.md`
