---
aliases:
  - collision times
  - collision time
---
>[!claim] Oracle
>Here's a silly construction. Suppose $T$ is an ST, and $S$ is an $\FFF_T$-measurable RV such that $S\geq T$. In other words, $S$ always happens after $T$, but you know when $S$ happens the moment $T$ happens. Then of course $S$ is also an ST.

>[!claim] Dyadic Approximation
>Here's a collection of dyadic stopping times which decrease to $T$.
>$$T_n = \sum_{k = 0}^\infty \frac{k+1}{2^n} \id_{k + 1 = \ceil{T 2^n}} + \infty \id_{T=\infty}$$

> [!theorem] Collision Times
> Let $(X_t)_{t\geq 0}$ be an [[Adapted Continuous-Time Processes|adapted]] process on metric space $(E,d)$.
> 1. If the sample paths are right-continuous, then for all open $U\subset E$,$$T_U = \inf\{t\geq 0: X_t\in U\}$$is a stopping time of $\FFF_{t+}$.
> 2. If the sample paths are continuous, then for all closed $C\subset E$,$$T_C = \inf\{t\geq 0: X_t\in C\}$$is a stopping time.

> [!proof]- Boring
> 1. This part works if you're left-continuous too. Observe that $T_U < t$ iff $\exists s < t(X_s\in U)$. I can't write something like $\bigcup_{s < t} (X_s\in U)$; the best I can do is $\bigcup_{s\in \QQ, s < t}(X_s\in U)$. And this just works; you need both some form of sequential continuity on $t$, and the fact that $U$ is open. (On the other hand, nobody cares about a metric, I think you can get away with any Hausdorff space).
> 2.  First off, observe that for all $\omega$, $X_{T_C}\in C$. This is because by definition, either $X_{T_C}\in C$, or there exists a descending sequence $t_i\downarrow T_C$ such that $X_{t_i}\in T_C$. But then by right continuity, $X_{t_i}$ must be a converging sequence, and closed subspaces are sequentially closed. So $\{T_C\leq t\}$ is the same as $\{\exists s\leq t: X_s\in C\}$.
>    
>    This is like, obviously $\FFF_T$-measurable, it's just really hard to show why! What the hell XD. Apparently the only way you can actually do this is with the distance function!   $$\{\exists s\leq t:X_s\in C\} = \left\{\inf_{s\in [0,t]\cap \QQ} d(X_s, C) = 0\right\}.$$The LHS implies the RHS because any descending sequence to $s$ would satisfy the RHS. The RHS implies the LHS because by sequential compactness of $[0,t]$, there is a converging subsequence $t_i\to t'$ along which $d(X_{t_i},C)\to 0$; by continuity $d(X_{t'}, C) = 0$ and $t'\in [0,t]$.