---
aliases:
  - Kolmogorov's Continuity Theorem
---
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