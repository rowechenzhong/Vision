
> [!problem] Products of Manifolds
> Suppose $X$ is an $m$-dimensional manifold, and $Y$ is an $n$-dimensional manifold. Show that:
> - $X\times Y$ is an $m + n$-dimensional manifold.
> - If $X$ and $Y$ are ($C^k$/real analytic/complex analytic) then $X\times Y$ is as well.

>[!solution]- $X\times Y$ is a manifold
>$X\times Y$ is:
>- Hausdorff, obviously.
>- Has countable basis, obviously.
>- For any $(x,y)\in X\times Y$, pick the desired atlases $(U, \phi)$ and $(V, \psi)$, then $(U\times V, \phi \times \psi)$ is an atals from $U\times V$ to $\RR^m\times \RR^n \cong \RR^{m + n}$.

>[!solution] Regularity
>A multivariable function satisfies any of the above regularity conditions iff it does componentwise.


>[!problem] Continuous functions yield manifolds
>Given a continuous function $f: \RR^m\to \RR^n$, the graph of all points $(x, f(x))\subset \RR^{m + n}$ with the induced topology is a smooth $m$-manifold.

>[!proof]
>The conjectured atlas is simply $f$. We need to show this is a homeomorphism. This is actually just true in general; for any continuous $f:X\to Y$, it is true that $\{(x, f(x))\}\subset X\times Y$ is homeomorphic to $X$.
>
>

>[!problem] Implicit Function
> Let $f_1,\dots, f_m$ be functions $\RR^n\to \RR$ which are ($C_k$/RA). Let $X\subset \RR_n$ be the set of points $P$ such that $f_i(P)= 0$ for all $i$. Suppose $df_i(P)$ are linearly independent for all such $P$. Use the [[implicit function theorem]] to show that $X$ is a topological manifold of dimension $n-m$ and equip it with a natural ($C_k$/RA) structure. Prove the analogous statement for holomorphic functions $\CC_n\to \CC$.

>[!proof]
>You can use the implicit functions to get homeomorphisms to $\RR^n$ on patches; these match up because everything is the desired regularity class and inverses and compositions are closed.

^1292a3

>[!todo]
>DO this!!! (better)




