$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
In general, $\exp(x+y)\neq \exp(x)\exp(y)$ (this isn't even true for matrices). The map
$$
	\mu(x,y) = \log\left(\exp(x)\exp(y)\right)
$$
expresses the product in $G$ in the coordinate chart induced by $\log$. $\mu(x,0) = \mu(0,x) = x$, thus $\mu$ can be (Maclaurin) expanded on some neighborhood $U\times U\to \fg$ to
$$
	\mu(x,y) = x + y + \frac12\mu_2(x,y) + \dots
$$
where $\mu_2$ is a skew-symmetric bilinear form. The map $\mu_2$ is called the ==**commutator**==, and we denote $[x,y] = \mu_2(x,y)$. Flipping it back around, we have the (tautological) identity

>[!theorem] Baker-Campbell-Hausdorff Formula
>$$
>	\exp(x)\exp(y) = \exp(x + y + \frac12[x,y] + \cdots)
>$$

>[!example] $\GL$
>In the case of $G = \GL_n(\KK)$, we can explicitly write
>$$
>\begin{align*}
>	\exp(x)\exp(y)
>	&= \left(1 + x + \frac{x^2}{2} + \cdots \right)\left(1 + y + \frac{y^2}{2} + \cdots \right)\\
>	&= 1 + x + y + \frac{(x+y)^2}{2} + \frac{xy - yx}{2} + \cdots\\
>	&= \exp\left(x + y + \frac{xy - yx}{2} + \cdots \right)
>\end{align*}
>$$
>thus $[x,y] = xy - yx$ and the commutator coincides with the usual definition.

[[Adjoint Coincidence|This is true in more generality]].

A slightly more natural stepping stone is here:
- [[How to invert the commutator]]