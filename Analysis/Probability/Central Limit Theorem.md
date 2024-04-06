---
aliases:
  - CLT
---
Let $X_N$ be a sequence of IID random variables with mean $0$ and variance $1$. Let $S_n = X_1 + \dots + X_n$. Then,
$$
	\frac{S_n}{\sqrt{n}} \to N(0,1)
$$
[[Weak Convergence|in distribution]]. In other words, for all $x\in \RR$, as $n\to \infty$,
$$
		\PP\left(\frac{S_n}{\sqrt{n}}\leq x\right) \to \int_{-\infty}^x \frac{1}{\sqrt{2\pi}} e^{\frac{-y^2}{2}}dy
$$