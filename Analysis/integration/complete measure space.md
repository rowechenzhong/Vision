> [!definition] Completion
> A ==**null set**== of a measure space $(\Omega, \AAA, \mu)$ is a measurable set $A$ such that $\mu(A) = 0$. A measure space is ==**complete**== if every subset of a null set is measurable.

> [!problem]
> If $\mu$ is obtained as the restriction of an outer measure $\mu^*$ to the Caratheodory measurable sets, then $\mu$ is complete.
> ^caratheodory-complete

> [!solution]-
> This is completely trivial because all sets $A$ with zero outer measure are measurable. For any $E\subset \Omega$, $\mu^*(E\cap A)\leq \mu^*(A) = 0$, so
> $$
> \mu^*(E\cap A) + \mu^*(E\setminus A) = \mu^*(E\setminus A)\leq \mu^*(E).
> $$
> Thus $A$ is measurable.