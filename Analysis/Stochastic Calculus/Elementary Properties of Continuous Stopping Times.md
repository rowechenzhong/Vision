>[!theorem] Important Properties of CTSTs.
>Suppose $S, T$ are [[Continuous Time Stopping Times|stopping times]].
>1. If $S\leq T$, then $\FFF_S\subset \FFF_T$.
>2. $S\land T$ and $S\lor T$ are both stopping times. $\FFF_{S\land T} = \FFF_S\cap \FFF_T$, and this sigma-algebra contains $\{S\leq T\}$.

>[!example] A difference between continuous and discrete processes
>Suppose $(X_n)_{n\geq 0}$ is adapted to $(\FFF_n)_{n\geq 0}$, where $n\in \ZZ_{\geq 0}$. If $T$ is a stopping time, then $X_T\in \FFF_T$. This is clear; for any Borel set $A$,$$
>\{X_T\in A\}\cap \{T\leq n\} = \bigcup_{k = 0}^n \left(\{X_k\in A\}\cap \{T = k\}\right)\in \FFF_n
>$$

>[!idea] Intuition
>In continuous time, such an argument does not hold, because we cannot take a naive union over uncountable times. This is why we add regularity conditions such as those found in [[Continuous Random Process Definitions]].

> [!theorem] Really Really stupid Properties of CSTs
> 1. $\FFF_T\subset \FFF_{t+}$. If $(\FFF_t)$ is right-continuous, then $\FFF_{T+} = \FFF_T$.
> 2. If $T = t$ is constant, $\FFF_T = \FFF_t$ and $\FFF_{T+} = \FFF_{t+}$.
> 3. If $T$ is a stopping time, then $T$ is $\FFF_T$-measurable.

>[!theorem] Slightly Stupid Properties of CSTs
>1. Let $T$ be a ST. Let $A\in \FFF_\infty$. Let$$T^A(\omega) = \begin{cases}
>    T(\omega)& \omega \in A\\
>    +\infty & \Omega \notin A
>    \end{cases}$$Then $A\in \FFF_T$ iff $T^A$ is a stopping time.
> 2. Let $T$ be a ST. A function $Y: \{T\leq \infty\}\to (E,\GGG)$ is $\FFF_T$-measurable (on the restricted measurable space) iff, for every $t\geq 0$, the restriction of $Y$ to $\{T\leq t\}$ is $\FFF_t$-measurable (on the restricted measurable space).
>

> [!theorem] Arithmetic Properties of CTSTs
> 
> 1. If $(S_n)$ is a monotonically increasing sequence of STs, then $S = \lim \uparrow S_n$ is also a stopping time.
> 2. If $(S_n)$ is a monotonically decreasing sequence of STs, let $S  =\lim\downarrow S_n$.
> 	1. $S$ is a stopping time of the filtration $\FFF_{t+}$, and $$\FFF_{S+} = \bigcap_n \FFF_{S_n+}.$$
> 	2. If $S_n$ is stationary, i.e. $\forall \omega \exists N(\omega)\forall n\geq N(\omega)$, $S_n(\omega) = S(\omega)$, then $S$ is actually a stopping time for $\FFF$, and $$\FFF_S = \bigcap_n \FFF_{S_n}.$$

> [!idea] Intuition
> 1. This is clear, because $\{S\leq t\} = \bigcap_i \{S_i\leq t\}$.
> 2. Unfortunately, $S > t$ does not play under limits.
> 	1. However, it is contained in $\FFF_s$ for all $s > t$.
> 	2. If you're eventually stationary, everything is easy.