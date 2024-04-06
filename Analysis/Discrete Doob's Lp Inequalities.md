---
aliases:
  - Lp Inequalities
---
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