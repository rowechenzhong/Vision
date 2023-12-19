We prove these results in the case of vector spaces $V, W$; the manifold case follows.

>[!theorem] Inverse function theorem.
> Let $V\cong W \cong \RR^n$. Let $U$ be a neighborhood of $x\in V$, and let $f:U\to W$ be a smooth map. Suppose $d_xf: \RR^n\to \RR^n$ is invertible for some $x\in U$. Then, there exists a neighborhood $x\in U'\subset U$ such that $f\big\vert_{U'} \to f(U')$ is a diffeomorphism (smooth and **invertible**). In this case,
> $$d_{f(x)}(f^{-1}) = (d_xf)^{-1}.$$
> 

WLOG $x = 0$, $f(0)= 0$, and $D_0(f) = 1$ by linear transformation. Set $g(x) = f(x) - x$, such that we wish to find
$$
	y - g(x) = x
$$

What the fuck is the contraction mapping theorem. I really don't give a fuck.



>[!problem] Implicit Function
> Let $f_1,\dots, f_m$ be functions $\RR^n\to \RR$ which are ($C_k$/RA). Let $X\subset \RR_n$ be the set of points $P$ such that $f_i(P)= 0$ for all $i$. Suppose $df_i(P)$ are linearly independent for all such $P$. Use the [[implicit function theorem]] to show that $X$ is a topological manifold of dimension $n-m$ and equip it with a natural ($C_k$/RA) structure. Prove the analogous statement for holomorphic functions $\CC_n\to \CC$.

>[!proof]
>You can use the implicit functions to get homeomorphisms to $\RR^n$ on patches; these match up because everything is the desired regularity class and inverses and compositions are closed.

^1292a3

>[!todo]
>DO this!!! (better)
