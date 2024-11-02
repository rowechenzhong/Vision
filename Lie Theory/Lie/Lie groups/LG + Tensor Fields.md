If a Lie group $G$ [[LG + Actions|acts on]] a manifold $X$, then it also acts on the tangent bundle $TX$! Indeed, for all $g\in G$, $p\in X$, $v\in T_pX$, send

$$
g((p, v)) = (gp, d_pg(v))
$$

where $d_pg$ is the [[Differential]] of $g$ at $p$ as usual. This extends to [[Tensor Fields]] as you would expect.

In particular $G$ acts on tensor fields _on itself_ via left and right translations; these actions are denoted $L_g$ and $R_g$ as usual. We say that a tensor field on $G$ is ==**left invariant**== if $L_gT = T$ for all $g\in G$, and ==**right invariant**== if $R_gT = T$ for all $g\in g$.

> [!idea]
> Actions by things in $g$ will slide the contents of our tensor bundle around; a left-invariant vector field (if one exists) is obtained by taking a vector and "spreading it around" $G$. This is completely trivial, actually, let's make this a theorem.

> [!theorem] Spread a vector like peanut butter
> For any $\tau\in \fg^k\otimes \fg^{*\otimes m}$, there exists a unique left-invariant tensor field $L_\tau$ whose value at $1$ is $\tau$. Thus, the space of such tensor fields is naturally isomorphic to $\fg^k\otimes \fg^{*\otimes m}$. Ditto for right actions.
>
> In particular, all Lie groups are [[frame|parallelizable]].

^b9afb7

This is blithingly obvious. After you have see the [[Various Adjoint maps]]:

> [!problem]
>$L_\tau$ is also right invariant iff $R_\tau$ is also left invariant iff $\tau$ is invariant under the [[Various Adjoint maps|adjoint representation]] $Ad_g$.

> [!solution]-
> Consider $L_\tau$. A right action by $g$ slides $(1,\tau)$ to $(g, (d_1R_g)\tau$. This is in $L_\tau$ iff
>
> $$
> 	(d_1R_g)\tau = (d_1L_g)\tau
> $$
>
> i.e. $\tau$ is invariant under the adjoint representation.