If $G$ is a real Lie group of dimension $n$, then any nonzero $\xi\in \bigwedge^n \fg^*$ can be painted over the whole group to form a non-vanishing top differential form $\omega_\xi$ on $G$ which defines an orientation plus a left-invariant positive measure $\mu_\omega$ on $G$. $\bigwedge^n \fg^*\cong \RR$ thus this is unique up to scaling by a positive number. This measure, up to scaling, is called the ==**left-invariant Haar measure**== which will be denoted by $\mu_L$. The ==**right-invariant Haar measure**== is the same idea.

If $\mu = \mu_L = \mu_R$, then $G$ is called ==**unimodular**==, and $\mu$ is called a ==**bi-invariant Haar measure**==. When does this happen? It's pretty clear that $\mu_L = \mu_R$ iff the left-invariant $\omega_\xi$ is also right-invariant up to sign. This is true iff $\xi$ is invariant up to sign under the action of $G$, i.e. $\abs{\bigwedge^n \fg^*}$ is a trivial representation of $G$.

>[!idea]
>To be clear, given a $1$-dimensional real representation $V$ of $G$, $\abs{V}$ is $\rho_\abs{V}(g) = \abs{\rho_V(g)}$, not deep.

Notably, if there is only one $1$-dimensional representation of $G$, then $G$ is unimodular.

Importantly: a compact Lie group is unimodular! The representation of $G$ on $\abs{\bigwedge^n \fg^*}$ is supposed to be a continuous homomorphism $G\to \RR^+$. $G$ is compact, thus $\rho(G)$ is a compact subgroup of $\RR^+$... but the only such subgroup is trivial, thus we conclude.

In fact, compact Lie groups have finite volume, thus we standardize normalization so $\mu$ is a probability measure.