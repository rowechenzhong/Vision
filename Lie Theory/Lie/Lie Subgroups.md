>[!definition] Lie Subgroup
>A ==**Lie Subgroup**== is a subgroup of a Lie group $G$ which is also an [[Immersed Submanifold]].

>[!definition] Closed Lie Subgroup
>A ==**closed Lie Subgroup**== is a subgroup of a Lie group $G$ which is also an [[Embedding|embedded submanifold]].

>[!example]
>So, irrational torus winding is a lie subgroup, but it's not closed.

>[!claim] Why is this called Closed?
>Closed Lie Subgroups are also closed in $G$ (so they are closed embedded submanifolds).

>[!proof]- Verification
>Um, because you're embedded, you're already open in your closure.
>
>However, note that the closure of $H\leq G$ is also a subgroup in itself;
> - The multiplication and inversion functions (in $G$, which $H$ inherits!) are continuous. So yeah.
>This is weird, because any coset of $H$ in $\conj{H}$ is guaranteed to also be open (because translation is a diffeomorphism). Thus $H = \conj{H}$.

>[!idea]
>In fact, it is also true that any closed subgroup of a real Lie group is closed. We will prove this. Er. Eventually. (Maybe)
>
>(This is why we're defining closed Lie subgroups with the stronger definition lol)

This lets us do obvious things that we couldn't before:

>[!example] Local generation
>If $U$ is a neighborhood of $1$ in a connected Lie group $G$, then $U$ generates $G$. This is clear, because the subgroup $H$ generated by $U$ is open. It is also an embedded submanifold, because for all $h\in H$, one can shift any chart $(U, \phi)$ at $1$ to $(hU, \phi\circ h^{-1})$. Thus it is both open and closed, and $H = G$.

>[!example] Homomorphisms are tight
>If $f:G\to K$ is a homomorphism of Lie groups, $K$ is connected, and $df_1:T_1G\to T_1K$ is surjective, then $f$ is surjective. This is true, because by implicit function theorem the image $f(G)$ contains some neighborhood of $1$ in $K$.
>^homomorphisms-tight