Let $m$ be a probability measure on $\RR$ with $\int \abs{x}m(dx) < \infty$ and $\int xm(dx) = \nu$. Let $(E,\mathcal{E}, \mu)$ be the canonical model for a sequence of independent random variables with law $m$. Then,
$$\mu\left(\left\{x:\frac{x_1+\dots+x_n}{n}\to \nu\right\}\right) = 1$$
This is obviously equivalent to SLLN.

> [!proof] Birkhoff kills
> Recall that the shift map $\theta$ is measure-preserving and ergodic. The coordinate function $f = X_1$ is integrable, and $S_n(f) = X_1 + \dots + X_n$ exactly. Thus, by [[Birkhoff's Almost Everywhere Ergodic Theorem|Birkhoff]], $\frac{X_1+\dots X_n}{n}\to \bar{f}$ almost surely for some invariant function $\bar{f}$. $\theta$ is ergodic, thus $\bar{f}$ is constant almost everywhere.
> 
> By [[von Neumann's Lp Ergodic Theorem|von Neumann]], this also converges in $L^1$, which justifies the second equality below:
> $$
> c = \mu(\bar{f}) = \mu\left(\lim_n \frac{S_n}{n}\right) = \lim_n \mu\left(\frac{S_n}{n}\right) = \nu
> $$
>