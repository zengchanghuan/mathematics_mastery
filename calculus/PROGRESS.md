---
updated: "2026-08-17"
status: active
current_track: "三角恒等式桥接复习"
---

# 当前学习位置

> 这是换电脑或新会话后的第一读取入口。详细长期仪表板保留在 [../calculus_progress.md](../calculus_progress.md)。

## 精确停点

当前课程：[三角恒等式的证明与练习](lessons/trigonometric-identities.md)。

已经讲解但尚未通过理解检查：

- 从 \(\sin^2x+\cos^2x=1\) 推出
  \(1+\tan^2x=\sec^2x\) 和
  \(1+\cot^2x=\csc^2x\)；
- 用两根单位向量的点积证明
  \(\cos(a-b)=\cos a\cos b+\sin a\sin b\)，但学习者反馈尚未理解；
- 已补充单位圆三角形 \(OAB\) 的余弦定理证明图和替代证明路径；
- 余弦和角公式与 \(\cos15^\circ\) 例题已经展示，但暂不作为过关证据。

当前等待学习者回答：

\[
\boxed{\angle AOB\text{ 为什么等于 }|a-b|\text{，余弦定理给出的 }AB^2\text{ 是什么？}}
\]

下一位 Tutor 先用[三角形证明图](assets/trigonometry-cosine-difference-triangle.svg)辅助讲解，不要跳回 \(\cos75^\circ\)。收到回答后先核对夹角与余弦定理，再检查坐标距离展开；两条路径都说清楚后，才继续余弦和角练习。

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

1. 借助图形理解余弦差角公式的三角形证明，并说清同一条边 \(AB\) 的两种算法；
2. 完成余弦和差角练习；
3. 证明并练习正弦和差角公式；
4. 推出倍角公式；
5. 推出半角与降幂公式；
6. 补积化和差与和差化积的来源；
7. 返回 \(1-\cos x\sim x^2/2\) 和等价无穷小；
8. 补连续函数运算后返回导数商法则。

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
