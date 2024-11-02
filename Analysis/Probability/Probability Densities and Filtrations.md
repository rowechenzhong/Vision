---
aliases:
  - Filtrations and PDFs
---
Let $(\FFF_n)_{n\geq 0}$ be a [[filtration]] on $\FFF$. Assume $\FFF = \FFF_\infty$ for simplicity. Let $(X_n)_{n\geq 0}$ be an adapted random process with $X_n\geq 0$ and $\EE[X_n] = 1$ for all $n$.

Then, for each $n$, one defines a probability measure on $\FFF_n$:
$$\tilde{\PP}_n(A) = \EE[X_n \id_A]$$
Of course, these equations determine $[X_n]$ uniquely.

>[!problem] Connecting this to things you've seen before
>The measures are consistent ($\left.\tilde{\PP}_{n + 1}\right|_{\FFF_n} = \tilde{\PP}_n$ for all $n$) iff $X$ is a martingale.
>
>Moreover, one can write a measure $\tilde{\PP}$ on $\FFF$ which has a density with respect to $\PP$, which is also compatible with $\tilde{\PP}_n$, iff $X$ is a UI martingale.

A tricky, quite instructive detail:

>[!problem]
>There exists a measure $\tilde{\PP}$ on $\FFF$ (with or without a density measure) compatible with $\tilde{\PP}_n$ iff $\EE[X_T] = 1$ for all finite stopping times $T$.

> [!solution]- $\implies$
> For any finite stopping time $T$,
> $$\EE[X_T] = \sum_{n\geq 1} \EE[X_n\id_{T = n}] = \sum_{n\geq 1} \tilde{\PP}_n(T = n) = 1$$
> by [[Convergence properties of Lebesgue Integral|Monotone Convergence]].



> [!solution]- $\Longleftarrow$
> Bounded stopping times are finite, so $(X_n)_{n\geq 0}$ is a martingale, and $\tilde{\PP}_n$ are consistent; thus we can define a consistent set function $\tilde{\PP}$ on $\bigcup_n \FFF_n$ which restricts to $\tilde{\PP}_n$ on $\FFF_n$ (this is obvious, no measure theory). We aim to show that $\tilde{\PP}$ is countably additive. Indeed, suppose I am given a sequence of disjoint subsets $A_n$ such that $\bigsqcup A_n \in \bigcup_m \FFF_m$ The stupid thing is that this means it lies in some $\FFF_m$. In this case, add $\FFF_m^c$ to the collection of subsets; we now wish to show that
> $$
> 	\sum_n \tilde{\PP}(A_n) = 1
> $$
> for all partitions $(A_n: n\geq 0)$ of $\Omega$. WLOG $A_n\in \FFF_n$ for all $n$, by adding $0$'s to the sequence if necessary. Any such partition is then a finite stopping time!$$T = \sum_n n\id_{A_n} \implies 1 = \EE[X_T] = \sum_{n\geq 1} \EE[X_n\id_{A_n}] = \sum_{n\geq 1} \tilde{\PP}_n(A_n)$$Where the last equality is by definition. Now, $\bigcup_n \FFF_n$ is an algebra generating $\FFF_\infty = \FFF$, so the Caratheodory extension Theorem says $\tilde{\PP}$ admits an extension to a measure on $\FFF$.