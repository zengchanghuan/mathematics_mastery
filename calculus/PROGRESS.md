---
updated: "2026-08-18"
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
  \(\cos(a-b)=\cos a\cos b+\sin a\sin b\)，但学习者反馈尚未理解；
- 已补充单位圆三角形 \(OAB\) 的余弦定理证明图和替代证明路径；
- 学习者希望再换一种三角形证明，已补充只依赖直角三角形的投影证明；
- 学习者因完整证明连续受阻而着急；已确认不再把完整复述证明作为前进门槛，
  证明保持 Developing 并留待间隔复习；
- 已用“把 \(b\) 反射为 \(-b\)”的图解释余弦和角公式中减号的来源，
  并完整示范 \(\cos75^\circ\)。

当前等待学习者回答：

\[
\boxed{\cos105^\circ=\cos(60^\circ+45^\circ)\text{，先按和角公式展开。}}
\]

下一位 Tutor 不要再用完整证明卡住主线。先核对
\(\cos105^\circ\) 的展开式；第一次出错只提示“余弦和角公式中间是减号”。
展开正确后再让学习者代入特殊角数值，并安排一道独立变式。

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

1. 完成余弦和差角公式的带提示练习与独立变式；完整证明留作间隔复习；
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
