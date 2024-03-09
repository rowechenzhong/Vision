$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
> [!theorem]
> Suppose $f:[a,b]\to \RR$ is continuous. Let
> $$
> 	F_a(t) = \int_a^t f(x)\der x
> $$
> Then, $F_a$ is differentiable on $[a,b]$, with $F'_a = f$.

>[!proof]- Not deep
>Well, fix some $t\in [a,b)$. For any $\eps$, there is a $\delta$ such that $\abs{f(x) - f(t)} \leq \eps$ for all $\abs{x - t}\leq \delta$. Thus, for $0 < h \leq \delta$,
> $$
> \begin{align*}
> 	\abs{\frac{F_a(t + h) - F_a(t)}{h} - f(t)} &= \abs{\frac1h\int^{h} \left(f(t + h) - f(t)\right)\der h}\\
> 	&\leq \frac1h\int_a^{a + h} \abs{f(t+h) - f(t)}\\
> 	&\leq \eps
> \end{align*}
> $$
> This demonstrates right differentiability. Left differentiability is similar on $(a,b]$. This concludes.

> [!theorem]
> Suppose $F:[a,b]\to \RR$ is differentiable with continuous derivative $f$. Then,
> $$
> 	\int_a^b f(x)\der x = F(b) - F(a)
> $$

> [!proof]- Also not deep
> Observe $(F - F_a)' = 0$ on $(a,b)$. By the [[mean value theorem]], $F - F_a$ is constant.

>[!idea] Equivalent Phrasing
>If I give you a continuous $f:[a,b]\to \RR$, then you can find me some $F(x)$ such that $F' = f$. The claim is that this must be $F_a$ up to a constant.