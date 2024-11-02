Let $(S, \FFF)$ and $(T, \GGG)$ be two measurable spaces. Usually, $(S, \FFF) = (T,\GGG) = (E,\EEE)$.

>[!definition] Transition Kernel
> A ==**Transition Kernel**== is a function $\kappa: (S\times \GGG)\to [0,1]$ such that:
> - For any fixed $B\in \GGG$, $\kappa(\bullet, B)$ is $\FFF$-measurable.
> - For any fixed $s\in S$, $\kappa(s, \bullet)$ is a probability measure on $(T, \GGG)$.

We are going to push the linear algebra now. Let $B(S), B(T)$ be the vector space of bounded measurable real functions with [[infinity norm]]. Then $f\mapsto Qf$ via$$Qf(x) = \int Q(x,dy) f(y)$$is an [[operators|operator]] $B(T)\to B(S)$. In fact, it is a contraction! Indeed, the map is obviously linear, $\id_A\to Q(x,\id_A)$ is a measurable function $S\to [0,1]$ by definition (whose norm is at most $1$, hence less than the norm of $\id_A$) and the generic case follows immediately.