On (smooth/RA) manifolds $X$, a ==**derivation at**== $P$ is a functional on [[Germ|germs]] $D: O_P\to \RR$. This must satisfy the ==**Leibniz rule**==
$$
	D(fg) = D(f)g(P) + f(P)D(g)
$$
In particular, $D(1) = 0$.

We call the space of all such derivations $T_P X$, the ==**tangent space**==. This is a real vector space.

Ditto for CA manifolds.

>[!claim] Basis
>Let $x_1,\cdots, x_n$ be local coordinates at $P$. Then $T_PX$ has basis
>$$
>	D_i(f) = \frac{\pa f}{\pa x_i}(0)
>$$

>[!proof] Boring, Todo

Every tangent vector $v\in T_PX$ defines a derivation $\pa_v: O(U)\to \RR,\CC$ for each neighborhood $U$ of $P$.

>[!todo]
>Understand this slightly more thoroughly.

