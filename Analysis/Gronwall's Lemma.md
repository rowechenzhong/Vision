>[!claim] Gronwall
>Let $g$ be a non-negative **bounded** measurable function on $[0,T]$. Suppose that there exist two constants $a,b\geq 0$ such that for every $t\in [0,T]$,$$
g(t)\leq a + b\int_0^t g(s)ds.
$$Then, for every $t\in [0,T]$, $g(t) \leq a\exp(bt)$.

>[!proof]- Iterate
> This is clear, because one can simply iterate:
> $$
> g(t)\leq a + a(bt) + a\frac{(bt)^2}{2} + \dots + a\frac{(bt)^n}{n!} + b^{n+1}\underbrace{\int_0^t ds_1 \int_0^{s_1} ds_2 \dots \int_0^{s_n}ds_{n+1} ds_{n+1} g(s_{n+1})}_\star
> $$
> where if $0\leq g\leq K$ the error term is $\star \leq K \frac{(bt)^{n+1}}{(n+1)}!\to 0$. We win.

There are other versions of this lemma where $a,b$ don't have to be constant.

> [!claim] Gronwall Differential Form
> Let $I = [0,\infty)$ or $[0,a)$ or $[0,a]$. Let $g, b$ be real-valued continuous functions on $I$. Suppose $g$ is differentiable in the interior of $I$, and$$g'(t)\leq b(t)g(t)$$on $I$. Then, for all $t\in I$,$$g(t)\leq g(0)\exp\left(\int_0^t b(s)ds\right).$$