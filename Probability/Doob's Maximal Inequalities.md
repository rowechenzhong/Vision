---
aliases:
  - Doob's Lp Inequality
---
Sometimes, we like to create a new random process $X^*_n = \sup_{k\leq n} \abs{X_k}$. This guy is just an increasing envelope bounding $X$, and it can be bounded.

>[!theorem] Maximal And Lp inequalities
>Let $X$ be a martingale or non-negative submartingale. Then, for all $\lambda \geq 0$,
> $$\lambda\PP(X^*_n\geq \lambda)\leq \EE\left(\abs{X_n} \id_{X^*_n\geq \lambda}\right)$$
> 
> Also, for all conjugate $1 < p,q < \infty$,
> $$\norm{X^*_n}_p\leq q\norm{X_n}_p$$

The martingale case immediately reduces to the non-negative submartingale case.

This is just [[Basic Inequalities|Markov's Inequality]] in the Martingale case.

>[!proof] Todo