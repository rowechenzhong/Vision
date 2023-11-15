>[!claim] Tangent Line Trick
>Let $c:I\to \RR$ be convex $m$ be in the interior of $I$. Then there exists a $a,b\in \RR$ such that $c(x)\geq ax + b$ on $I$, with equality at $x = m$.

>[!proof]- Stupid
> Note that for all $x < m$ and $y > m$,
> $$
> 	\frac{c(m) - c(x)}{m - x}\leq \frac{c(y) - c(m)}{y - m}
> $$
> Thus I can stuff an $a$ between the supremum of the LHS and the infimum of the RHS; $c(x)\geq a(x-m) + c(m)$.

> [!theorem] Jensen's Inequality
> If $I$ is an interval, $X:\Omega\to I$ is an integrable RV, and $c:I\to \RR$ is convex, then $\EE[c(x)] \geq c(\EE[x])$ (and $\EE[c(x)]$ is defined)

> [!proof]- Bruh
> If $X$ is constant a.e. then we're done. Otherwise, $X$ differs from $\ess \inf X$ on set of positive measure, ditto for $\ess \sup$, thus $\EE[X]$ lies strictly inside $I$, and I can find $c(X)\geq aX + b$. Thus $\EE(c(X)^{-})\leq \abs{a}\EE[\abs{X}] + \abs{b}\leq \infty$ and $\EE[c(X)]$ is well-defined. We have
> $$
> 	\EE[c(X)]\geq a\EE[X] + b = c(\EE[x])
> $$