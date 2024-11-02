> [!idea] Assume everything is Lipschitz from now on
> Assume that $\sigma, b$ are continuous and $K$-Lipschitz in $x$.

> [!theorem] Lipschitz Existence and Uniqueness for SDEs
> Pathwise uniqueness holds for $E(\sigma, b)$. For every choice of filtered probability space and BM $B$, there exists a unique strong solution of $E_x(\sigma, b)$.

In particular, weak existence obviously holds, and weak uniqueness will follow from the proceeding theorems (or Yamada-Watanabe).

> [!proof]- (Ideas) The proofs are pretty entertaining, I guess.
> The solution is constructed using Picard' approximation method, lol. Let $X^0_t = x$, and define
> $$
> X^n_t = x + \int_0^t \sigma(s, X^{n-1}_s)dB_s + \int_0^t b(s, X^{n-1}_s)ds.
> $$
> 
> You use [[Gronwall's Lemma]] at some point.

In fact, you can take the entire solution, taking as input $x$ and a a BM $B$, and package it up in one massive function $F$.

> [!theorem]
> For each $x\in \RR$, there exists a mapping $F_x: C(\RR_+, \RR^m)\to C(\RR_+, \RR^d)$ which is:
> - Measurable, when $C(\RR_+, \RR^m)$ is equipped with the Borel $\sigma$-field (the usual $\sigma$-field) completed by the $W$-negligible sets and $C(\RR_+, \RR^d)$ is equipped with the Borel $\sigma$-field.
> - For every $x,\in \RR, t\geq 0$, the mapping $w\mapsto F_x(w)_t$ from $C(\RR_+,\RR^m)\to \RR^d$ is $W(dw)$-AS a measurable function of $w(r): 0\leq r\leq t$.
> - For every $w\in C(\RR_+, \RR^m)$, the mapping $x\mapsto F_x(w)$ is actually continuous. Here, $C(\RR_+, \RR^d)$ is given the topology of uniform convergence on the compacts, say, defined by the distance $\sum \alpha_k \left( \sup_{s\leq k}\abs{f(s) - g(s)} \land 1\right)$.
> - For every $x\in \RR^d$, for every choice of filtered space, for every choice of $B$ with $B_0 = 0$, the process $X_t = F_x(B)_t$ is the unique solution of $E_x(\sigma, b)$.
> - We can do even better: for any $\FFF_0$-measurable RV $U$, $F_U(B)_t$ is the unique solution with $X_0 = U$.

Not proved, too many details.