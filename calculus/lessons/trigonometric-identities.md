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

首次作答写成
\(\cos60\cos45+\sin60\sin45\)。角度符号为提高输入速度可以省略；
经一次“和角公式中间为减号”的提示后，已正确订正为
\(\cos60\cos45-\sin60\sin45\)。下一步只代入四个特殊角函数值，
暂不化简。学习者已独立正确给出
\(\cos60=1/2\)、\(\cos45=\sqrt2/2\)、
\(\sin60=\sqrt3/2\)、\(\sin45=\sqrt2/2\)；当前等待完成乘法与合并。

最终正确得到：

\[
\cos105^\circ=\frac{\sqrt2-\sqrt6}{4}.
\]

结果为负，与 \(105^\circ\) 位于第二象限的余弦符号一致。当前独立变式是
使用 \(\cos(60^\circ-45^\circ)\) 计算 \(\cos15^\circ\)。

学习者给出正确最终结果 \((\sqrt2+\sqrt6)/4\)，但没有按题意写计算过程；
由于该结果此前出现过，当前只补查差角公式的展开行，再判断是否完成独立变式。

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

## 9. 正弦和差角公式

### 9.1 严格表述与条件

对于任意实数角 \(a,b\)，只要二者使用相同的角度单位，就有：

\[
\boxed{\sin(a+b)=\sin a\cos b+\cos a\sin b},
\]

\[
\boxed{\sin(a-b)=\sin a\cos b-\cos a\sin b}.
\]

这里没有分母，所以不存在“分母不能为零”一类的额外限制；公式对所有实数角成立。
正弦公式的中间符号与括号里的符号相同：和角用加号，差角用减号。

### 9.2 几何直观：正弦是高度

单位圆上角 \(\theta\) 对应点的纵坐标是 \(\sin\theta\)。在下面的单位直角三角形中，
竖边 \(PQ=\sin\theta\)，斜边 \(OP=1\)。从顶点 \(P\) 看，夹角是
\(90^\circ-\theta\)，竖边又是这个角的邻边，所以：

\[
\cos(90^\circ-\theta)=\frac{PQ}{OP}=\sin\theta.
\]

![正弦和角公式的余函数推导](../assets/trigonometry-sine-sum-complement.svg)

直观上，求 \(\sin(a+b)\) 就是在求转到角 \(a+b\) 后的最终高度；
余函数关系把“高度问题”转换成了已经掌握的余弦差角问题。

### 9.3 和角公式的逐步推导

第一步使用余函数关系：

\[
\sin(a+b)=\cos[90^\circ-(a+b)].
\]

第二步整理括号：

\[
90^\circ-(a+b)=(90^\circ-a)-b.
\]

第三步对 \((90^\circ-a)-b\) 使用余弦差角公式：

\[
\begin{aligned}
\sin(a+b)
&=\cos[(90^\circ-a)-b]\\
&=\cos(90^\circ-a)\cos b
  +\sin(90^\circ-a)\sin b\\
&=\sin a\cos b+\cos a\sin b.
\end{aligned}
\]

最后一步使用了
\(\cos(90^\circ-a)=\sin a\) 和
\(\sin(90^\circ-a)=\cos a\)。

### 9.4 差角公式的来源

把和角公式中的 \(b\) 换成 \(-b\)：

\[
\begin{aligned}
\sin(a-b)
&=\sin[a+(-b)]\\
&=\sin a\cos(-b)+\cos a\sin(-b)\\
&=\sin a\cos b-\cos a\sin b.
\end{aligned}
\]

依据是 \(\cos(-b)=\cos b\)（偶函数）和
\(\sin(-b)=-\sin b\)（奇函数）。

### 9.5 完整例题：计算 \(\sin75^\circ\)

\[
\begin{aligned}
\sin75^\circ
&=\sin(45^\circ+30^\circ)\\
&=\sin45^\circ\cos30^\circ
  +\cos45^\circ\sin30^\circ\\
&=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}
  +\frac{\sqrt2}{2}\cdot\frac12\\
&=\boxed{\frac{\sqrt6+\sqrt2}{4}}.
\end{aligned}
\]

几何检查：\(75^\circ\) 位于第一象限，所以结果应为正；而且正弦不超过 \(1\)，
上面的结果也符合这个范围。

### 9.6 当前带提示练习

\[
\sin15^\circ=\sin(45^\circ-30^\circ).
\]

第一步只按正弦差角公式展开，不代入数值。

学习者已正确写出：

\[
\sin(45^\circ-30^\circ)
=\sin45^\circ\cos30^\circ-\cos45^\circ\sin30^\circ.
\]

当前下一步只代入四个特殊角函数值，暂不化简。

学习者随后直接给出正确结果：

\[
\sin15^\circ=\frac{\sqrt6-\sqrt2}{4}.
\]

由于前一步已经正确展示差角公式，接受跳过机械代入行。当前独立变式：

\[
\sin(x+60^\circ),
\]

要求展开并代入 \(60^\circ\) 的特殊角值，不提供分步提示。

学习者已正确完成公式展开：

\[
\sin(x+60^\circ)=\sin x\cos60^\circ+\cos x\sin60^\circ.
\]

当前只等待把 \(\cos60^\circ\) 与 \(\sin60^\circ\) 换成具体数值。

首次代入写成
\(\tfrac12\sin x+\tfrac{2}{\sqrt3}\cos x\)。其中
\(\cos60^\circ=1/2\) 正确，但 \(\sin60^\circ\) 被误取成倒数；当前只用
“正弦值必须在 \([-1,1]\) 内”作最小提示，等待自行订正第二个系数。

学习者随后正确订正 \(\sin60^\circ=\sqrt3/2\)，所以：

\[
\sin(x+60^\circ)=\frac12\sin x+\frac{\sqrt3}{2}\cos x.
\]

正弦和差角公式的带提示练习与独立变式当堂完成，状态保持 `Developing`，
等待间隔复测。

## 10. 倍角公式

### 10.1 严格表述与条件

倍角 \(2a\) 就是同一个角相加：\(2a=a+a\)。对于任意实数角 \(a\)，有：

\[
\boxed{\sin2a=2\sin a\cos a},
\]

\[
\boxed{\cos2a=\cos^2a-\sin^2a}.
\]

利用 \(\sin^2a+\cos^2a=1\)，余弦倍角公式还有两个等价形式：

\[
\boxed{\cos2a=2\cos^2a-1=1-2\sin^2a}.
\]

这些式子没有分母，对所有实数角都成立。

### 10.2 几何直观

从横轴先转过角 \(a\)，再沿同一方向转过一个角 \(a\)，最终方向就是
\(a+a=2a\)。单位圆上最终点的横坐标是 \(\cos2a\)，纵坐标是
\(\sin2a\)。

![正弦与余弦倍角公式](../assets/trigonometry-double-angle.svg)

因此倍角公式不是凭空出现的新公式，而是把和角公式里的两个角取成相同的角。

### 10.3 正弦倍角公式的推导

在正弦和角公式中令 \(b=a\)：

\[
\begin{aligned}
\sin2a
&=\sin(a+a)\\
&=\sin a\cos a+\cos a\sin a\\
&=2\sin a\cos a.
\end{aligned}
\]

最后一步的依据是两个加数完全相同。

### 10.4 余弦倍角公式的推导与三种形式

在余弦和角公式中令 \(b=a\)：

\[
\begin{aligned}
\cos2a
&=\cos(a+a)\\
&=\cos a\cos a-\sin a\sin a\\
&=\cos^2a-\sin^2a.
\end{aligned}
\]

若要只保留余弦，用 \(\sin^2a=1-\cos^2a\)：

\[
\cos2a=\cos^2a-(1-\cos^2a)=2\cos^2a-1.
\]

若要只保留正弦，用 \(\cos^2a=1-\sin^2a\)：

\[
\cos2a=(1-\sin^2a)-\sin^2a=1-2\sin^2a.
\]

三种形式数值相同；根据题目给的是 \(\sin a\)、\(\cos a\)，还是两者都有，
选择最方便的一种。

### 10.5 完整例题

已知 \(a\) 在第一象限，\(\sin a=3/5\)、\(\cos a=4/5\)，求
\(\sin2a\) 与 \(\cos2a\)。

\[
\sin2a=2\sin a\cos a
=2\cdot\frac35\cdot\frac45
=\boxed{\frac{24}{25}}.
\]

\[
\cos2a=\cos^2a-\sin^2a
=\left(\frac45\right)^2-\left(\frac35\right)^2
=\boxed{\frac7{25}}.
\]

检验：

\[
\left(\frac{24}{25}\right)^2+\left(\frac7{25}\right)^2=1,
\]

符合单位圆上的平方关系。

### 10.6 当前带提示练习

已知 \(a\) 在第一象限，\(\sin a=5/13\)、\(\cos a=12/13\)。第一步只求
\(\sin2a\)，暂不求 \(\cos2a\)。

学习者已独立正确计算：

\[
\sin2a=2\cdot\frac5{13}\cdot\frac{12}{13}=\frac{120}{169}.
\]

当前下一步求同题的 \(\cos2a\)，由学习者自行选择三种等价形式中最方便的一种。

学习者正确选择并计算：

\[
\cos2a=\left(\frac{12}{13}\right)^2-\left(\frac5{13}\right)^2
=\frac{119}{169}.
\]

带提示练习完成。当前独立变式：已知 \(a\) 在第二象限且
\(\sin a=3/5\)，只求 \(\sin2a\)；不提示 \(\cos a\) 的符号。
学习者已正确判断第二象限中 \(\cos a<0\)，当前等待利用平方关系求出具体值。
随后由 \(\sin^2a+\cos^2a=1\) 正确得到 \(\cos a=-4/5\)。当前等待代入
\(\sin2a=2\sin a\cos a\) 完成独立变式。首次计算得到 \(-6/25\)：
符号与分母正确，但分子漏算了因子；当前只提示重新计算
\(2\times3\times(-4)\)。

学习者随后正确订正分子为 \(-24\)，并准确说明错因是把公式前面的 \(2\)
误当成分母约掉，因此：

\[
\sin2a=-\frac{24}{25}.
\]

倍角公式的带提示练习与独立变式当堂完成；公式运用正确，保留轻量算术复测。

## 11. 为什么 \(1-\cos x=2\sin^2(x/2)\)

### 11.1 严格表述与条件

对任意实数角 \(x\)，都有：

\[
\boxed{1-\cos x=2\sin^2\frac{x}{2}}.
\]

其中 \(\sin^2(x/2)\) 表示 \([\sin(x/2)]^2\)，不是 \(\sin(x^2/2)\)。
公式没有分母，所以对所有实数 \(x\) 成立。

### 11.2 几何直观：整角对应一条弦，弦的一半对应半角

单位圆中取 \(OA=OP=1\)，圆心角 \(\angle AOP=x\)。连接弦 \(AP\)，
从圆心向弦作中线 \(OM\)。等腰三角形 \(OAP\) 被分成两个全等直角三角形，
因此每一半的圆心角是 \(x/2\)。

![一减余弦与半角平方](../assets/trigonometry-one-minus-cos-half-angle.svg)

在其中一个直角三角形中，半条弦 \(AM=\sin(x/2)\)，所以整条弦
\(AP=2\sin(x/2)\)。另一方面，余弦定理给出
\(AP^2=2(1-\cos x)\)。两种方法算同一条弦，便得到目标公式。

这条几何证明只用于建立直观，不要求学习者完整复述。

### 11.3 从倍角公式的一行推导

最短的代数来源是刚学过的余弦倍角公式：

\[
\cos2a=1-2\sin^2a.
\]

令 \(a=x/2\)，于是 \(2a=x\)：

\[
\cos x=1-2\sin^2\frac{x}{2}.
\]

把 \(\cos x\) 移到右边、平方项移到左边：

\[
\boxed{1-\cos x=2\sin^2\frac{x}{2}}.
\]

所以这不是一条突然出现的新公式，而是余弦倍角公式把角 \(a\) 改名为
\(x/2\) 后的直接改写。

### 11.4 完整例题：取 \(x=60^\circ\)

左边：

\[
1-\cos60^\circ=1-\frac12=\frac12.
\]

右边：

\[
2\sin^230^\circ=2\left(\frac12\right)^2=\frac12.
\]

左右相等，验证了公式。

### 11.5 当前带提示练习

取 \(x=90^\circ\)，分别计算
\(1-\cos90^\circ\) 与 \(2\sin^245^\circ\)，检查两边是否相等。

学习者正确得到左右两边均为 \(1\)。当前无提示变式：取
\(x=120^\circ\)，分别计算恒等式左右两边并判断是否相等。首次回答两边均为
\(1/2\)：相等关系判断正确，但将第二象限中的 \(\cos120^\circ\) 误作正值；
当前只订正左边。学习者能调用“奇变偶不变，符号看象限”，但写成
\(\cos(90^\circ+30^\circ)=\sin30^\circ\)，漏掉第二象限负号；正确结构应为
\(-\sin30^\circ\)。

经提示后，学习者正确计算左边：

\[
1-\cos120^\circ=1-\left(-\frac12\right)=\frac32.
\]

当前只等待计算右边 \(2\sin^260^\circ\)。

学习者随后正确得到右边也是 \(3/2\)，恒等式验证完成。由于左边曾在第二象限
余弦符号上出错，本项保持 `Developing` 并安排跨日复测，不继续阻塞主线。

## 12. 半角公式与降幂公式

### 12.1 严格表述与条件

对于任意实数角 \(x\)，半角的平方公式为：

\[
\boxed{\sin^2\frac{x}{2}=\frac{1-\cos x}{2}},
\qquad
\boxed{\cos^2\frac{x}{2}=\frac{1+\cos x}{2}}.
\]

如果要求的是 \(\sin(x/2)\) 或 \(\cos(x/2)\) 本身，需要开平方：

\[
\boxed{\sin\frac{x}{2}=\pm\sqrt{\frac{1-\cos x}{2}}},
\]

\[
\boxed{\cos\frac{x}{2}=\pm\sqrt{\frac{1+\cos x}{2}}}.
\]

这里的正负号不能随意选，必须由半角 \(x/2\) 所在象限决定，而不是由 \(x\)
所在象限决定。平方形式对所有实数 \(x\) 成立；开平方形式也成立，但必须选对符号。

把半角公式中的 \(x\) 换成 \(2x\)，得到降幂公式：

\[
\boxed{\sin^2x=\frac{1-\cos2x}{2}},
\qquad
\boxed{\cos^2x=\frac{1+\cos2x}{2}}.
\]

“降幂”是把二次方的 \(\sin^2x\)、\(\cos^2x\) 变成一次的余弦；代价是角变成
\(2x\)。

### 12.2 公式地图

```mermaid
flowchart TD
    A["cos 2θ = 1 − 2sin²θ"] --> B["sin²θ = (1 − cos 2θ) / 2"]
    C["cos 2θ = 2cos²θ − 1"] --> D["cos²θ = (1 + cos 2θ) / 2"]
    B --> E["令 θ=x/2：sin²(x/2) = (1 − cos x) / 2"]
    D --> F["令 θ=x/2：cos²(x/2) = (1 + cos x) / 2"]
```

上半部分是“降幂”：从倍角公式中直接把平方项单独留下；下半部分令
\(\theta=x/2\)，便是“半角”。两套名称描述的是同一次代数变形。

### 12.3 逐步推导

从：

\[
\cos x=1-2\sin^2\frac{x}{2}
\]

移项并除以 \(2\)：

\[
\sin^2\frac{x}{2}=\frac{1-\cos x}{2}.
\]

再从余弦倍角的另一种形式：

\[
\cos x=2\cos^2\frac{x}{2}-1
\]

移项并除以 \(2\)：

\[
\cos^2\frac{x}{2}=\frac{1+\cos x}{2}.
\]

若从平方得到函数本身，必须使用
\(u^2=A\Rightarrow u=\pm\sqrt A\)，因此半角公式前面会出现 \(\pm\)。

### 12.4 几何直观

上一节的弦图中，圆心角是 \(x\)，中线把等腰三角形分成两个角为 \(x/2\)
的直角三角形。因此“整角余弦”与“半角正弦的平方”自然同时出现：

![一减余弦与半角平方](../assets/trigonometry-one-minus-cos-half-angle.svg)

平方会丢失方向信息：正数和负数平方后相同。这就是从平方公式开根号时，必须回到
单位圆看 \(x/2\) 象限的原因。

### 12.5 完整例题：用半角公式计算 \(\sin60^\circ\)

把 \(60^\circ\) 看成 \(120^\circ/2\)。因为半角 \(60^\circ\) 在第一象限，
正弦取正号：

\[
\begin{aligned}
\sin60^\circ
&=+\sqrt{\frac{1-\cos120^\circ}{2}}\\
&=\sqrt{\frac{1-(-1/2)}{2}}\\
&=\sqrt{\frac34}\\
&=\boxed{\frac{\sqrt3}{2}}.
\end{aligned}
\]

注意：决定正号的是 \(60^\circ\) 所在的第一象限，而不是整角
\(120^\circ\) 所在的第二象限。

### 12.6 当前带提示练习

已知 \(x=300^\circ\)，使用半角公式求 \(\cos(x/2)=\cos150^\circ\)。
第一步只判断 \(x/2=150^\circ\) 所在象限以及最终应取正号还是负号，暂不计算根式。
