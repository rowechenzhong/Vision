---

aliases:
  - Lp Inequalities
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Also see [[Discrete Doob's Maximal Inequalities|Doob]]. Let $X^*_n = \sup_{k\leq n} \abs{X_k}$, and set $X^* = \sup_{n\geq 0}\abs{X_n}$. 

>[!theorem] $L^p$ Inequalities
> For all conjugate $1 < p,q < \infty$,$$\norm{X^*_n}_p\leq q\norm{X_n}_p.$$which immediately yields$$\norm{X^*}_p\leq q\sup_{n\geq 0} \norm{X_n}_p$$

> [!proof]- Fubini Doob and more Fubini (Easy)
> In the $L^p$ case, we consider $X^*_n\land k$ for convergence purposes.
> $$
> \begin{align*}
> 	\EE[\left(X_n^*\land k\right)^p] &= \int_0^k p\lambda^{p-1}\PP\left(X^*_n\geq \lambda\right)d\lambda \tag{Fubini}\\
> 	&\leq \int_0^k p\lambda^{p-2}\EE[X_n\id_{X^*_n\geq \lambda}] d\lambda \tag{Doob}\\
> 	&\leq \EE\left[X_n \int_0^k p\lambda^{p-2}\id_{X^*_n\geq \lambda}d\lambda \right] \tag{Fubini}\\
> 	&= \frac{p}{p-1}\EE[X_n(X^*_n\land k)^{p-1}]  \tag{Fubini}\\
> 	&\leq q\norm{X_n}_p \norm{X^*_n\land k}^{p-1}_p
> \end{align*}
> $$
> Then we monotone-convergence to win.