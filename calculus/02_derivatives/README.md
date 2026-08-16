---
title: Week 3 导数与微分
document_type: learning-notes
status: active
updated: "2026-08-16"
---

# 导数：从平均变化率到瞬时变化率

> 开始日期：2026-08-15
>
> 进入证据：Week 2 极限与连续章节检查 \(3.5/4=87.5\%\)。

## 1. 导数的严格定义

如果极限存在，函数 \(f\) 在 \(x=a\) 处的导数定义为：

\[
\boxed{
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}
}
\]

其中：

- \(a\) 是固定的目标输入。
- \(h\) 是从 \(a\) 到附近输入 \(a+h\) 的横向变化。
- \(f(a+h)-f(a)\) 是对应的纵向变化。
- 差商 \(\frac{f(a+h)-f(a)}{h}\) 是两点之间的割线斜率，也是平均变化率。
- 当 \(h\to0\) 时，附近点靠近目标点；割线斜率的极限就是切线斜率和瞬时变化率。

等价形式为：

\[
f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}
\]

## 2. 几何直观：割线逼近切线

![点 Q 靠近点 P 时割线逼近切线](assets/secant-to-tangent.svg)

## 3. 完整例题：由定义求 \(f(x)=x^2\) 在 \(x=1\) 处的导数

\[
\begin{aligned}
f'(1)
&=\lim_{h\to0}\frac{f(1+h)-f(1)}{h}\\
&=\lim_{h\to0}\frac{(1+h)^2-1}{h}\\
&=\lim_{h\to0}\frac{1+2h+h^2-1}{h}\\
&=\lim_{h\to0}\frac{2h+h^2}{h}\\
&=\lim_{h\to0}(2+h)\\
&=2
\end{aligned}
\]

因此：

\[
\boxed{f'(1)=2}
\]

点 \(P(1,1)\) 处的切线斜率为 \(2\)，切线方程为：

\[
y-1=2(x-1)
\]

即：

\[
\boxed{y=2x-1}
\]

## 当前掌握状态

- [ ] 能用自己的话解释割线斜率与切线斜率的关系。
- [ ] 能识别差商中的横向变化与纵向变化。
- [ ] 能从导数定义独立计算一个二次函数在指定点的导数。
- [ ] 能从点和导数写出切线方程。

## 4. 幂函数求导公式

> 掌握状态：学习者确认已非常熟悉，跳过当堂重复练习；保留跨日抽查，不把自述熟练直接等同于长期 Mastered。

先从导数定义推导 \(f(x)=x^3\)：

\[
\begin{aligned}
f'(x)
&=\lim_{h\to0}\frac{(x+h)^3-x^3}{h}\\
&=\lim_{h\to0}
\frac{x^3+3x^2h+3xh^2+h^3-x^3}{h}\\
&=\lim_{h\to0}
\left(3x^2+3xh+h^2\right)\\
&=3x^2
\end{aligned}
\]

因此：

\[
\boxed{(x^3)'=3x^2}
\]

![三次函数的导函数给出每一点的切线斜率](assets/power-rule-x-cubed.svg)

对于一般正整数 \(n\)，二项式展开的开头为：

\[
(x+h)^n=x^n+nx^{n-1}h+\text{含 }h^2\text{ 及更高次幂的项}
\]

代入导数定义，减去 \(x^n\) 并除以 \(h\) 后：

\[
\frac{(x+h)^n-x^n}{h}
=nx^{n-1}+\text{仍然含 }h\text{ 的项}
\]

当 \(h\to0\) 时，仍然含 \(h\) 的项全部趋近 \(0\)，因此得到幂函数求导公式：

\[
\boxed{(x^n)'=nx^{n-1}}
\]

使用规则：

1. 原指数 \(n\) 移到前面成为系数。
2. 原指数减去 \(1\)。

例如：

\[
(x^5)'=5x^4
\]

## 5. 导数的线性运算法则

> 掌握状态：学习者确认已非常熟练，跳过当堂重复练习；保留跨日抽查。

设函数 \(u(x)\)、\(v(x)\) 在当前点可导，\(c\) 是常数，则：

\[
\boxed{(u+v)'=u'+v'}
\]

\[
\boxed{(u-v)'=u'-v'}
\]

\[
\boxed{(cu)'=cu'}
\]

### 5.1 从导数定义推导加法法则

令 \(F(x)=u(x)+v(x)\)，根据导数定义：

\[
\begin{aligned}
F'(x)
&=\lim_{h\to0}\frac{F(x+h)-F(x)}{h}\\
&=\lim_{h\to0}\frac{u(x+h)+v(x+h)-u(x)-v(x)}{h}\\
&=\lim_{h\to0}
\left[
\frac{u(x+h)-u(x)}{h}
+\frac{v(x+h)-v(x)}{h}
\right]\\
&=u'(x)+v'(x)
\end{aligned}
\]

减法法则同理，只需把中间的加号换成减号。

### 5.2 从导数定义推导常数倍法则

令 \(G(x)=cu(x)\)：

\[
\begin{aligned}
G'(x)
&=\lim_{h\to0}\frac{cu(x+h)-cu(x)}{h}\\
&=c\lim_{h\to0}\frac{u(x+h)-u(x)}{h}\\
&=cu'(x)
\end{aligned}
\]

### 5.3 几何直观

函数相加时，在同一个横坐标 \(x_0\) 处，两个函数的纵向变化相加，所以它们的切线斜率也相加：

\[
m_{u+v}=m_u+m_v
\]

![函数相加时切线斜率也相加](assets/derivative-linearity.svg)

### 5.4 完整例题

求：

\[
y=3x^4-2x^2+7
\]

逐项求导：

\[
\begin{aligned}
y'
&=(3x^4)'-(2x^2)'+(7)'\\
&=3(x^4)'-2(x^2)'+0\\
&=3\cdot4x^3-2\cdot2x\\
&=\boxed{12x^3-4x}
\end{aligned}
\]

其中常数 \(7\) 不随 \(x\) 改变，因此变化率为 \(0\)：

\[
\boxed{(7)'=0}
\]

## 6. 乘积求导法则

> 掌握状态：学习者确认已比较熟练，跳过当堂重复练习；保留跨日抽查。

设 \(u(x)\)、\(v(x)\) 都可导，则：

\[
\boxed{(uv)'=u'v+uv'}
\]

注意：不能写成 \(u'v'\)。

### 6.1 几何直观：长方形面积变化

把 \(u\) 和 \(v\) 看成长方形的两条边，面积为 \(uv\)。当两条边分别增加
\(\Delta u\) 和 \(\Delta v\) 时，新增面积为：

\[
\Delta(uv)=v\Delta u+u\Delta v+\Delta u\Delta v
\]

![用长方形面积变化理解乘积法则](assets/product-rule-area.svg)

最后一块 \(\Delta u\Delta v\) 同时含有两个很小的变化量。除以输入变化量并令其趋近于 \(0\) 时，这一项的贡献趋近于 \(0\)，留下另外两项。

### 6.2 从导数定义严格推导

令 \(F(x)=u(x)v(x)\)：

\[
F'(x)=\lim_{h\to0}\frac{u(x+h)v(x+h)-u(x)v(x)}{h}
\]

在分子中加上再减去 \(u(x+h)v(x)\)：

\[
\begin{aligned}
F'(x)
&=\lim_{h\to0}
\frac{u(x+h)v(x+h)-u(x+h)v(x)}{h}\\
&\quad+\lim_{h\to0}
\frac{u(x+h)v(x)-u(x)v(x)}{h}\\
&=\lim_{h\to0}
u(x+h)\frac{v(x+h)-v(x)}{h}\\
&\quad+\lim_{h\to0}
v(x)\frac{u(x+h)-u(x)}{h}\\
&=u(x)v'(x)+v(x)u'(x)
\end{aligned}
\]

所以：

\[
\boxed{(uv)'=u'v+uv'}
\]

### 6.3 完整例题

求：

\[
y=x^2(x+3)
\]

令：

\[
u=x^2,\qquad v=x+3
\]

那么：

\[
u'=2x,\qquad v'=1
\]

使用乘积法则：

\[
\begin{aligned}
y'
&=u'v+uv'\\
&=2x(x+3)+x^2\cdot1\\
&=2x^2+6x+x^2\\
&=\boxed{3x^2+6x}
\end{aligned}
\]

## 当前执行位置

- [x] 导数定义与基础差商计算已经学习。
- [x] 幂函数、线性运算和乘积法则已由学习者确认熟悉。
- [ ] 点斜式切线方程仍需跨日抽查，重点区分导数函数与指定点的斜率。
- [ ] 第一章闭区间连续函数性质补全后，继续商法则、反函数求导和链式法则。
