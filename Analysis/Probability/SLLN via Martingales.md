The results on this page are strictly stronger than the results in [[SLLN via Birkhoff and von Neumann]] and [[Strong LLN elementary proof]]. Let's commit arson :D

Consider the partial sums $S_n = X_1 + \dots + X_n$ where $X_i$ are independent.

# Basic SLLN

> [!theorem]
> Suppose $X_n$ are IID integrable, and let $\mu = \EE(X_1)$. Then, $\frac{S_n}{n}\to \mu$ as $n\to \infty$, AS + $L^1$.

The basic idea is that $\EE[X_1 | S_n] = \frac{S_n}{n}$, which allows us to apply [[Backwards MCT]].

Build the natural backwards filtration and write the tail sigma-algebra:
$$\hat{\FFF}_n = \sigma(S_m : m\geq n),\qquad \mathfrak{T}_n = \sigma(X_{n+1},\dots), \qquad \mathfrak{T} = \bigcap_n \mathfrak{T}_n$$
Observe that $\hat{\FFF}_n = \sigma(S_n, \mathfrak{T}_n)$. Because $X_1\pperp \mathfrak{T}_n$ and by symmetry,
$$\EE[X_1 | \hat\FFF_n] = \EE[X_1 | S_n] = \frac{S_n}{n}$$
almost surely, thus by BMCT $\frac{S_n}{n}\to \EE[X_1 | \hat\FFF_\infty]$ in AS+$L^1$.

>[!claim] The core reason SLLN works
>$\lim_{n\to \infty} \frac{S_n}{n}$ is $\mathfrak{T}_m$-measurable for all $m$ (modulo a measure-$0$ set).

>[!proof]
> Fix $m$ and $x\in \RR$. The set $\{\lim_{n\to \infty} \frac{S_n}{n} = x\}$ is $\mathfrak{T}_m$-measurable, because it is equal to $\{\lim_{n\to \infty} \frac{S_n - S_m}{n}\}$ for all $\abs{S_m} < \infty$ (an almost-sure event), and this guy is clearly $\mathfrak{T}_m$-measurable.

Thus $\EE[X_1 | \hat{\FFF}_\infty]$ is $\mathfrak{T}$-measurable. By [[Kolmogorov's Zero-One Law|K$01$]], this means it is constant almost surely. Taking expectations, it is $\EE[X_1]$ almost surely.