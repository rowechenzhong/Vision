> [!theorem] Doob Upcrossing
> Let $X$ be a [[Discrete-time Martingale|supermartingale]]. Let $U_n[a,b]$ be the number of [[upcrossings]] by $X$ including time $n$. Then,
> $$(b-a)\EE(U_n[a,b]) \leq \EE[(X_n - a)^-].$$

The most common application is to take the supremum of both sides to bound $U[a,b]$:
$$(b-a)\EE[U[a,b]] \leq \sup_n \EE[(X_n - a)^-]$$

> [!idea] Why is this obvious?
> Recall that supermartingales die downwards. If $U_n[a,b] = m$, you upcrossed $m$ times; in expectation over all of $\Omega$, you accumulated $(b-a)U_n[a,b] \geq 0$ of movement. However, this number is supposed to be negative. Thus one expects that there is a strong bound to this, which can be computed by carefully considering the steps you take after upcrossing for the last time.

