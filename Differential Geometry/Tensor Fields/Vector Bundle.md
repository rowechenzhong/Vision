We will define a ==**$k$-vector bundle**== of ==**rank**== $n$ on $X$. 
- First, let's talk about the fibration structure: This is a manifold $E$ with a surjective regular map $p:E\to X$.
- Each fiber $p^{-1}(x)$ is a $k$-vector space of dimension $n$.
- Let's force all the vector spaces to talk to each other: Every $x\in X$ has a neighborhood $U$ admitting a diffeomorphism $h:U\times k^n\to p^{-1}(U)$ such that:
	1. First off, for all $u$, $h(u, \bullet)$ maps into $p^{-1}(u)$.
	2. For all $u$, $h(u,\bullet)$ is a linear map. (So for specific $u$, $g_U$ assigns coordinates to the vector space at $u$).

>[!idea]
>This is exactly the definition of a [[Fiber Bundle]] except that the $h$ map needs to be linear.

>[!idea]
> Even if $X$ is a complex manifold and $k = \CC$, $E$ need not be a complex manifold. If all $h$ can be chosen to be holomorphic then it is though. So we're going to always assume those $h$ are chosen to be holomorphic.

>[!example] Trivial Vector Bundle
>A vector bundle is ==**trivial**== if it is $X\times k^n$.

This holds if it admits a [[frame]].

See [[clutching functions]].

One can direct sum vector bundles; this is called the ==**Whitney sum**==.