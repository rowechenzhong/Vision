---

aliases:
  - Kolmogorov's Continuity Theorem
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Kolmogorov's Criterion is fundamental. Let $X:[0,\infty)\times \Omega\to S$ be a stochastic process on some complete metric space.

> [!theorem] Kolmogorov's Continuity Theorem
> Suppose there exist positive constants $\alpha, \beta, K$ such that for all $0\leq s,t$, $$\EE[d(X_t, X_s)^\alpha] \leq K\abs{t - s}^{1 + \beta}.$$ There, there exists a continuous modification $\tilde{X}$ of $X$ which is [[Types of Continuity|locally $\gamma$-Holder-continuous]] for every $\gamma < \beta/\alpha$.


>[!idea] Kolmogorov's Criterion, informal
>Let $I$ be dense in $[0,1]$, e.g. $\QQ$. Specify a random process $\xi: I\to \RR$. If $\xi$ is [[Types of Continuity|Holder-continuous]], then there is some continuous modification $X:[0,1]\to \RR$ which is Holder-continuous.

>[!idea] Continuous modifications are unique.
>See [[RPCT intuition]].

>[!idea]
>$(\star)$ is $\beta$-$L^p$-Holder continuity on $I \to L^p(\Omega)$, which is a rather odd condition. It is weakest (and thus (1) is strongest) when $\beta = \frac1p + \eps$. (2) has natural strength conditions: it is strongest at $\beta - \frac1p - \eps$, so if the $\beta$ specified first is large, (2) allows a tighter condition on $X$.

# Proof Ideas

This theorem is proved by absolutely obliterating everything with dyadic numbers. It's quite an involved and tedious proof, with no real ideas.

# Deprecated

(2) is pointwise across $\omega\in \Omega$; all paths are $\alpha$-Holder continuous. This isn't that deep though, because $X_t$ was only specified up to stochastic equivalence.

> [!theorem]- Rewritten Kolmogorov's Criterion
> Let $p \in (1,\infty)$ and $\beta \in (\frac1p, 1]$. Let $I\subset [0,1]$ be dense, and let $(\xi_t)_{t\in I}$ be random such that $\exists C  < \infty$
> $$\norm{\xi_s - \xi_t}_p \leq C\abs{s - t}^\beta \tag{$\star$}$$
> Then, there exists a **continuous** random process $(X_t)_{t\in [0,1]}$ such that:
> 1. ($X_t = \xi_t$ almost surely) for all $t\in I$.
> 2. For all $\alpha \in [0, \beta - \frac1p)$, there exists $K_\alpha \in L^p$ such that $\abs{X_s - X_t} \leq K_\alpha\abs{s - t}^\alpha$ for all $s, t \in [0,1]$.

> [!theorem]- Kolmogorov's Criterion Rewritten with alternative exponents
> Let $p > 1$ and $\beta > 0$. Let $I\subset [0,1]$ be dense, and let $(\xi_t)_{t\in I}$ be random such that $\exists C  < \infty$
> $$\EE[\abs{\xi_s - \xi_t}^p] \leq C\abs{s - t}^{1 + \beta} \tag{$\star$}$$
> Then, there exists a **continuous** random process $(X_t)_{t\in [0,1]}$ such that:
> 1. ($X_t = \xi_t$ almost surely) for all $t\in I$.
> 2. For all $0\leq \alpha < \beta/p$, there exists $K_\alpha \in L^p$ such that $\abs{X_s - X_t} \leq K_\alpha\abs{s - t}^\alpha$ for all $s, t \in [0,1]$.