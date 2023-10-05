We will define a ==**$k$-vector bundle**== of ==**rank**== $n$ on $X$. 
- First, let's talk about the fibration structure: This is a manifold $E$ with a surjective regular map $p:E\to X$.
- Each fiber $p^{-1}(x)$ is a $k$-vector space of dimension $n$.
- Let's force all the vector spaces to talk to each other: Every $x\in X$ has a neighborhood $U$ admitting a diffeomorphism $h:U\times k^n\to p^{-1}(U)$ such that:
	1. First off, for all $u$, $h(u, \bullet)$ maps into $p^{-1}(u)$.
	2. For all $u$, $h(u,\bullet)$ is a linear map. (So for specific $u$, $g_U$ assigns coordinates to the vector space at $u$).

>[!idea]
>This is exactly the definition of a [[Fiber Bundle]] except that the $h$ map needs to be linear.

>[!idea]
> Even if $X$ is a complex manifold an $k = \CC$, $E$ need not be a complex manifold (I don't get this lol); if all $h$ can be chosen to be holomorphic then it is though. So we're going to always assume those $h$ are chosen to be holomorphic.

>[!example] Trivial Vector Bundle
>A vector bundle is ==**trivial**== if it is $X\times k^n$.

This holds if it admits a [[frame]].
# Intrinsic

Thus, if $p:E\to X$ is a vector bundle, then $X$ has an open cover $\{U_\alpha\}$; each one trivializes as above via a diffeomorphism $$g_\alpha: p^{-1}(U_\alpha)\to U_\alpha \times k^n$$
These are basically just coordinate charts, so they have transition maps. These are called ==**clutching functions**== in the literature:
$$
	h_{\alpha\beta}: U_\alpha\cap U_\beta\to \GL_n(k)
$$
(which is holomorphic if $E$ is a holomorphic bundle). These satisfy some obvious consistency conditions:
1. $h_{\alpha\beta}(x) = h_{\beta\alpha}(x)^{-1}$.
2. $h_{\alpha\beta}(x)\circ h_{\beta\gamma}(x) = h_{\alpha\gamma}(x)$.

Thus, we have the following constructive definition:

>[!definition] Constructive Vector Bundle.
>Start from a disjoint union $\bigsqcup_\alpha U_\alpha \times k^n$, and identify points according to
>$$
>	h_{\alpha\beta}:(x,v)\in U_\beta \times K^n \sim (x, h_{\alpha\beta}(x)v)\in U_\alpha \times K^n
>$$

Of course, this non-constructive definition is morally wrong, and works for non-linear fiber bundles too.