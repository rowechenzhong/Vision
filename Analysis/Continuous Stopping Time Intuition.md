First and foremost, a ST should extend the properties of a normal time (element of $[0,\infty]$).
1. Information-theoretically:
	1. $\FFF_T$ detects all information known at time $T$.
	2. $\FFF_{T+}$ detects all information known given $T$ already happened. (Most statements about $T$ yield identical statements about $\FFF_{T+}$, because $\FFF_{t+}$ is a filtration itself).
	3. $S\leq T$ implies $\FFF_S\subset \FFF_T$.
2. The martingale property should hold. This is true for UI martingales: $\EE(X_T) = \EE(X_0)$ and$$\EE(X_T | \FFF_S) = X_{S\land T}.$$
3. One can index an adapted process with a time to obtain an $\FFF_t$ RV. One can index a progressive process with a ST to obtain an $\FFF_T$ RV.

Secondly, one should be able to perform common arithmetic operations on the STs. The most important thing is that $S\land T$ and $S\lor T$ are stopping times, and $\FFF_{S\land T} = \FFF_S\cap \FFF_T$.