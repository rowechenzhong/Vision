The results on this page are strictly stronger than the results in [[SLLN via Birkhoff and von Neumann]] and [[Strong LLN elementary proof]]. Let's commit arson :D

Consider the partial sums $S_n = X_1 + \dots + X_n$ where $X_i$ are independent.

# Basic SLLN

> [!theorem]
> Suppose $X_n$ are IID integrable, and let $\mu = \EE(X_1)$. Then, $\frac{S_n}{n}\to \mu$ as $n\to \infty$, AS + $L^1$.

Build the natural backwards filtration and write the tail sigma-algebra:
$$\hat{\FFF}_n = \sigma(S_m : m\geq n),\qquad \mathfrak{T}_n = \sigma(X_{n+1},\dots), \qquad \mathfrak{T} = \bigcap_n \mathfrak{T}_n$$
Observe that $\hat{\FFF}_n = \sigma(S_n, \mathfrak{T}_n)$.