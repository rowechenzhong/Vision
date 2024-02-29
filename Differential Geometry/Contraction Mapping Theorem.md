We work in a [[banach]] space.
> [!theorem] Contraction Mapping Theorem
> If $g: B(0,r)\to B(0,r)$ is a $q$-[[contraction mapping]] such that $g(0) = 0$, then $f = I + g$ is injective on $B(0, r)$. Furthermore, $B(0, (1-q)r)\subset f(B(0,r))\subset B(0, (1+q)r)$.

This is basically a small extension of the [[Banach Fixed-point Theorem]].

>[!proof]- Easy, try it!
If $a + g(a) = b + g(b)$, then $\norm{a-b} = \norm{g(b) - g(a)}$ contradiction. If $\norm{x} < r$, then $\norm{x + g(x)} < (1 + q)r$. If $\norm{y} < (1-q)r$, then $y - g$ is still $q$-contraction mapping from $B(0,r)$ to $B(0,r)$. Thus by Banach's FPT, there is a solution to $x = y - g(x)$ as desired.