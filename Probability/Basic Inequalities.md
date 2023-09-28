>[!theorem] Markov's Inequality
>If $X\geq 0$ is a random variable,
>$$ \PP(X\geq t) = \EE\left[\id_{X\geq t}\right] \leq \EE\left[\frac{X}{t}\right] = \frac{\EE[X]}{t}$$

>[!prob] Chebyshev's Inequality
> If $X\in L^2$ is a random variable, show that
> $$\PP\left(\abs{X - \EE[X]}\geq t\right) \leq \frac{\Var(X)}{t^2}$$
