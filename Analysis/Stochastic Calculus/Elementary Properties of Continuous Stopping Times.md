>[!theorem] Important Properties of C STs.
>Suppose $S, T$ are stopping times.
>
>1. If $S\leq T$, then $\FFF_S\subset \FFF_T$.
>2. $S\land T$ and $S\lor T$ are both stopping times. $\FFF_{S\land T} = \FFF_S\cap \FFF_T$.

>[!example] A difference between continuous and discrete processes
>Suppose $(X_n)_{n\geq 0}$ is adapted to $(\FFF_n)_{n\geq 0}$, where $n\in \ZZ_{\geq 0}$. If $T$ is a stopping time, then $X_T\in \FFF_T$. This is clear; for any Borel set $A$,$$
>\{X_T\in A\}\cap \{T\leq n\} = \bigcup_{k = 0}^n \left(\{X_k\in A\}\cap \{T = k\}\right)\in \FFF_n
>$$

>[!idea] Intuition
>In continuous time, such an argument does not hold, because we cannot take a naive union over uncountable times. This is why we add regularity conditions such as those found in [[Continuous Random Process Definitions]].

