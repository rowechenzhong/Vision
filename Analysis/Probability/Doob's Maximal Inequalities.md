---
aliases:
  - Doob's Lp Inequality
---
Sometimes, we like to create a new random process $X^*_n = \sup_{k\leq n} \abs{X_k}$. This guy is just an increasing envelope bounding $X$, and it can be bounded.

This is a generalization of [[Basic Inequalities|Markov's Inequality]] to the Martingale case.

>[!theorem] Maximal And Lp inequalities
>Let $X$ be a martingale or non-negative submartingale. Then, for all $\lambda \geq 0$,
> $$\lambda\PP(X^*_n\geq \lambda)\leq \EE\left(\abs{X_n} \id_{X^*_n\geq \lambda}\right).$$
> 
> Also, for all conjugate $1 < p,q < \infty$,
> $$\norm{X^*_n}_p\leq q\norm{X_n}_p.$$

> [!idea] 676 Version
> Here is a version of the maximal inequality that was shown in 676.
> 
> If $X$ is a submartingale (not necessarily non-negative), then $\lambda \PP(X^*_n \geq \lambda)\leq \EE[\abs{X_0} + 2\abs{X_n}]$. This is kind of cool though, because the RHS is a function of solely $X_n$ and $X_0$.


Let $X^* = \sup_{n\geq 0}\abs{X_n}$. We can bound this too...

> [!theorem] Full supremum bounds
> Under the same conditions, for all $\lambda \geq 0$,
> $$\lambda \PP(X^* \geq \lambda) \leq \sup_{n\geq 0} \EE[\abs{X_n}]$$
> and for all conjugate $1 < p,q < \infty$,
> $$\norm{X^*}_p\leq q\sup_{n\geq 0} \norm{X_n}_p$$

# Proofs

The martingale case immediately reduces to the non-negative submartingale case, so we will consider only that.

> [!proof]- Maximal
> Well, we care about the event $X^*_n\geq \lambda$, so let's make it a stopping time.
> $$T = \inf\{k\geq 0: X_k\geq \lambda\} \land n\leq n$$
> By optional stopping,
> $$\begin{align*}\EE[X_n]&\geq \EE[X_T]\\
> &= \EE[X_T \id_{X^*_n\geq \lambda}] + \EE[X_T \id_{X^*_n < \lambda}]\\
> &\geq \lambda\PP(X^*_n\geq \lambda) + \EE[X_n \id_{X^*_n < \lambda}]\end{align*}$$
> where in the first case $T$ resolves to a value causing $X_T\geq \lambda$, and in the second case $X_T$ resolves to at least $X_n$.
 
> [!proof]- Lp
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

The full bounds follow quickl