---
aliases:
  - Markov's Inequality
---
>[!problem] Markov's Inequality
>Let $f$ be a non-negative measurable function and $\lambda \geq 0$; clearly $\lambda\id_{\{f\geq \lambda\}} \leq f$, thus
>$$
>	\lambda \mu(f\geq \lambda)\leq \mu(f)
>$$

>[!problem] Chebyshev's Inequality
> If $X\in L^2$ is a random variable, show that
> $$\PP\left(\abs{X - \EE[X]}\geq t\right) \leq \frac{\Var(X)}{t^2}$$

> [!problem] Tail inequality
> Suppose $X\in L^p$. Show that $\PP(\abs{X} \geq \lambda) = O(\lambda^{-p})$.

> [!solution]-
> Indeed, $\PP\left(\abs{X}^p\geq \lambda^p\right)\leq \frac{\EE[\abs{X}^p]}{\lambda^p} = O(\lambda^{-p})$.

Also see:
- [[Jensen's Inequality]]
- [[Holder's Inequality]] and [[Minkowski's Inequality]]