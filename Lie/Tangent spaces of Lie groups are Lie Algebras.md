Actually, we have already done significant amounts of the work.

Watch:

>[!theorem] Jacobi Identity holds for any Lie group
>$\fg$ under the [[Commutator|commutator]] is a Lie algebra.

Indeed, this follows from [[Adjoint Problems#^Lie-functor|the fact that Lie brackets preserve the Adjoint]]. For all $g\in G$, the map $\Ad(g):G\to G$ is a morphism whose differential preserves the commutator:
$$
\Ad_G(g)([x,y]) = [\Ad_G(g)(x), \Ad_G(g)(y)]
$$
Then, we can let $g$ vary along $g(t) = \exp(tz)$ and differentiate with respect to $t$ at $t = 0$.This yields:
$$
	\Ad_\fg(z)([x,y]) = [\Ad_\fg(z)(x), y] + [x, \Ad_\fg(z)(y)]
$$
But wait just a moment-- $\Ad_\fg$ is just the commutator! This says
$$
	[z, [x,y]] = [[z,x], y] + [x, [z,y]]
$$
which is precisely Jacobi.

>[!idea]
>You can write this very succinctly by excluding the $z$;
>$$
>	\Ad_\fg [x,y] = [\Ad_\fg x, \Ad_\fg y]
>$$
