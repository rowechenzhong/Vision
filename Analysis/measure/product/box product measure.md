Given two measure spaces $(S, \FFF,\mu)$,  and $(T, \GGG, \lambda)$, we will construct a product measure space $(S\times T, \FFF\otimes \GGG, \mu \otimes \lambda)$. The ==**product space**== has set $\Omega = S\times T$ . The ==**product $\sigma$-field**== is $\FFF\otimes \GGG = \sigma(S_0)$.
$$ S_0 = \{A\times B: A\in \FFF, B \in \GGG\}$$
Observe that $S_0$ is a [[semi-algebra]]. This should be reminiscent of the [[box product]] from topology; compare the following results to analogous topological results.

> [!example] Cross-sections are measurable
> Suppose $E$ is a measurable set in $S\times T$. Then for any fixed $x$, $E_x = \{y\in T: (x,y)\in E\}$ is measurable in $T$.
> ^cross-sections-measurable

>[!proof]-
> Consider all sets $E\in \FFF\otimes \GGG$ such that $E_x$ is measurable! Observe that this is a $\sigma$-algebra containing $S_0$. Thus it contains the whole thing!

By the [[Standard Measure Construction]], we need only exhibit a pre-measure on the [[semi-algebra]] $S_0$ given in the product space construction, and one is naturally handed to us.

>[!theorem] Boxes work
>The function $(\mu\otimes \lambda): S_0\to [0,\infty]$ given by
>$$ (\mu\otimes \lambda)(A\times B) = \mu(A)\times \lambda(B)$$
>is a pre-measure.

>[!proof] Boring, todo.

> [!theorem] Products are associative
> One can write $\mu_1\otimes \mu_2\otimes\cdots \mu_n$ and everything works correctly.

>[!proof]- Boring, todo.