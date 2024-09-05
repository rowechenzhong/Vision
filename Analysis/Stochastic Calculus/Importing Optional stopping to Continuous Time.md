See the discrete [[Optional Stopping Theorem]].


>[!theorem] Bounded Optional Stopping Theorem
> Let $X$ be a cadlag adapted integrable [[Discrete-Time Random Process|process]].
> 
> The following are equivalent:
> 1. $X$ is a martingale.
> 2. For all bounded [[Stopping Time|stopping times]] $T$, and all stopping times $S$,
>    $$\EE[X_T | \FFF_S] = X_{S\land T}.$$
> 3. For all stopping times $T$, $X^T$ is a martingale.
> 4. For all bounded stopping times $T$, $X_T$ is integrable and
>    $$\EE[X_T] = \EE[X_0].$$

> [!theorem] Optional Stopping Theorem
> Suppose $X$ is a UI martingale with right-continuous sample paths. Then it admits an AS and $L^1$ limit, and thus $X_\infty$ is defined everywhere. For **any** stopping times $S,T$, we have $\EE(X_T) = \EE(X_0)$ and
> $$\EE(X_T | \FFF_S) = X_{S\land T}$$