# 三角恒等式的证明与练习

## 学习目标

不是孤立背诵公式，而是建立以下证明链：

\[
\text{平方关系}
\rightarrow\text{和差角}
\rightarrow\text{倍角}
\rightarrow\text{半角与降幂}
\rightarrow\text{积化和差}.
\]

弧度、单位圆和基础特殊角此前已经学习，本课不重复展开，只在需要时抽查。

## 1. 平方关系的两个派生式

从

\[
\sin^2x+\cos^2x=1
\]

两边除以 \(\cos^2x\)，在 \(\cos x\ne0\) 时得到：

\[
\boxed{1+\tan^2x=\sec^2x}.
\]

两边除以 \(\sin^2x\)，在 \(\sin x\ne0\) 时得到：

\[
\boxed{1+\cot^2x=\csc^2x}.
\]

## 2. 余弦差角公式的证明

取单位向量：

\[
\mathbf u=(\cos a,\sin a),\qquad
\mathbf v=(\cos b,\sin b).
\]

按坐标计算点积：

\[
\mathbf u\cdot\mathbf v
=\cos a\cos b+\sin a\sin b.
\]

两向量长度均为 \(1\)，夹角为 \(|a-b|\)。按长度和夹角计算：

\[
\mathbf u\cdot\mathbf v
=\cos(a-b).
\]

两种算法计算的是同一个点积，因此：

\[
\boxed{\cos(a-b)=\cos a\cos b+\sin a\sin b}.
\]

![余弦差角公式的单位向量证明](../assets/trigonometry-cosine-difference.svg)

## 3. 余弦差角公式的三角形证明

如果点积还不直观，可以在单位圆中直接使用三角形证明。令

\[
A=(\cos a,\sin a),\qquad B=(\cos b,\sin b),
\]

圆心为 \(O\)。此时 \(OA=OB=1\)，圆心角
\(\angle AOB=|a-b|\)。

![余弦差角公式的三角形证明](../assets/trigonometry-cosine-difference-triangle.svg)

在三角形 \(OAB\) 中用余弦定理计算边 \(AB\)：

\[
AB^2=1^2+1^2-2\cos(a-b)=2-2\cos(a-b).
\]

再用坐标距离公式计算同一条边：

\[
\begin{aligned}
AB^2
&=(\cos a-\cos b)^2+(\sin a-\sin b)^2\\
&=2-2(\cos a\cos b+\sin a\sin b).
\end{aligned}
\]

两式相等，消去相同项后得到：

\[
\boxed{\cos(a-b)=\cos a\cos b+\sin a\sin b}.
\]

当前检查只聚焦第一步：解释为什么
\(\angle AOB=|a-b|\)，并用余弦定理写出 \(AB^2\)。
不要在这一步通过前跳到数值例题。

## 4. 余弦差角公式的另一种三角形证明：投影法

为了让图中的长度都为正，先画 \(0<b<a<90^\circ\) 的情形。取单位线段
\(OP=1\)，它与水平线的夹角是 \(a\)；再作一条与水平线夹角为
\(b\) 的射线 \(OH\)。从 \(P\) 向 \(OH\) 作垂线，垂足为 \(H\)。

![余弦差角公式的直角三角形投影证明](../assets/trigonometry-cosine-difference-projection.svg)

### 第一次算 \(OH\)：直接看大直角三角形

因为

\[
\angle POH=a-b,
\]

所以在直角三角形 \(OPH\) 中：

\[
OH=OP\cos(a-b)=\cos(a-b).
\]

### 第二次算 \(OH\)：先把 \(OP\) 拆成横边和竖边

从 \(P\) 向水平线作垂线，垂足为 \(Q\)。在单位直角三角形
\(OPQ\) 中：

\[
OQ=\cos a,\qquad QP=\sin a.
\]

从 \(Q\) 向 \(OH\) 作垂线，垂足为 \(R\)。在直角三角形
\(OQR\) 中：

\[
OR=OQ\cos b=\cos a\cos b,
\]

为了完全用三角形说明第二段，再过 \(R\) 作 \(RS\parallel QP\)，
交 \(PH\) 于 \(S\)。因为 \(QR\parallel PS\)、\(QP\parallel RS\)，
四边形 \(QPSR\) 是平行四边形，所以

\[
RS=QP=\sin a.
\]

在直角三角形 \(RSH\) 中，\(\angle SRH=90^\circ-b\)，于是

\[
RH=RS\cos(90^\circ-b)=\sin a\sin b.
\]

而图上 \(OH=OR+RH\)，因此：

\[
\boxed{\cos(a-b)=\cos a\cos b+\sin a\sin b}.
\]

这条证明只用了平行四边形和直角三角形中的“邻边 \(=\) 斜边乘余弦”。
图中先选锐角，
是为了避免有向线段的符号干扰；推广到其他象限时，使用带正负号的投影，
公式保持不变。

### 完整数值例子

取 \(a=60^\circ,b=30^\circ\)：

\[
\begin{aligned}
\cos(60^\circ-30^\circ)
&=\cos30^\circ=\frac{\sqrt3}{2},\\
\cos60^\circ\cos30^\circ+\sin60^\circ\sin30^\circ
&=\frac12\cdot\frac{\sqrt3}{2}
 +\frac{\sqrt3}{2}\cdot\frac12
=\frac{\sqrt3}{2}.
\end{aligned}
\]

当前只检查第二次计算中的第一小步：长度为
\(\cos a\) 的水平边，与 \(b\) 方向夹角是 \(b\)，它在 \(b\) 方向上的投影是多少？

## 5. 余弦和角公式

### 几何直观：把 \(b\) 翻到横轴下方

角 \(b\) 关于横轴反射以后变成 \(-b\)。反射前后：

\[
\cos(-b)=\cos b,\qquad \sin(-b)=-\sin b.
\]

也就是横坐标不变，纵坐标变号。此时角 \(a\) 与角 \(-b\) 之间的夹角
正好是 \(a+b\)。

![余弦和角公式的反射推导](../assets/trigonometry-cosine-sum-reflection.svg)

### 严格推导

将差角公式中的第二个角换成 \(-b\)：

\[
\begin{aligned}
\cos(a+b)
&=\cos[a-(-b)]\\
&=\cos a\cos(-b)+\sin a\sin(-b)\\
&=\cos a\cos b-\sin a\sin b.
\end{aligned}
\]

\[
\boxed{\cos(a+b)=\cos a\cos b-\sin a\sin b}.
\]

减号不是硬记出来的，而是来自
\(\sin(-b)=-\sin b\)。

### 完整例题：计算 \(\cos75^\circ\)

\[
\begin{aligned}
\cos75^\circ
&=\cos(45^\circ+30^\circ)\\
&=\cos45^\circ\cos30^\circ
 -\sin45^\circ\sin30^\circ\\
&=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}
 -\frac{\sqrt2}{2}\cdot\frac12\\
&=\boxed{\frac{\sqrt6-\sqrt2}{4}}.
\end{aligned}
\]

记忆结构：余弦和差角公式中间的符号与括号里的符号相反。

当前带提示练习：

\[
\cos105^\circ=\cos(60^\circ+45^\circ).
\]

第一步只需要按和角公式展开，不急着化简。

## 6. 已完成例题

\[
\begin{aligned}
\cos15^\circ
&=\cos(45^\circ-30^\circ)\\
&=\cos45^\circ\cos30^\circ
  +\sin45^\circ\sin30^\circ\\
&=\frac{\sqrt6+\sqrt2}{4}.
\end{aligned}
\]

## 7. 后续独立练习

使用和角公式计算：

\[
\boxed{\cos75^\circ=\cos(45^\circ+30^\circ)}.
\]

状态：已作为余弦和角公式的完整例题讲解；后续安排独立变式复测。

## 8. 后续课程

- 正弦和差角公式及证明；
- 正弦、余弦倍角公式；
- 半角与降幂公式；
- 积化和差与和差化积；
- 返回三角极限与等价无穷小。
