> [!theorem]
> Suppose $f:[a,b]\to \RR$ is continuous. Let
> $$
> 	F_a(t) = \int_a^t f(x)\der x
> $$
> Then, $F_a$ is differentiable on $[a,b]$, with $F'_a = f$.

>[!proof]- Not deep
>Well, fix some $t\in [a,b)$. For any $\eps$, there is a $\delta$ such that $\abs{f(x) - f(t)} \leq \eps$ for all $\abs{x - t}\leq \delta$. Thus, for $0 < h \leq \delta$,
> $$
> \begin{align*}
> 	\abs{\frac{F_a(t + h) - F_a(t)}{h} - f(t)} &= \abs{\frac1h\int^{h} \left(f(t + h) - f(t)\right)\der h}\\
> 	&\leq \frac1h\int_a^{a + h} \abs{f(t+h) - f(t)}\\
> 	&\leq \eps
> \end{align*}
> $$
> This demonstrates right differentiability. Left differentiability is similar on $(a,b]$. This concludes.

> [!theorem]
> Suppose $F:[a,b]\to \RR$ is differentiable with continuous derivative $f$. Then,
> $$
> 	\int_a^b f(x)\der x = F(b) - F(a)
> $$

> [!proof]- Also not deep
> Observe $(F - F_a)' = 0$ on $(a,b)$. By the [[mean value theorem]], $F - F_a$ is constant.

>[!idea] Equivalent Phrasing
>If I give you a continuous $f:[a,b]\to \RR$, then you can find me some $F(x)$ such that $F' = f$. The claim is that this must be $F_a$ up to a constant.