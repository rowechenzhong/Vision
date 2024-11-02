>[!theorem] Intrinsic Definition ($k$-slicing theorem)
>Let $Y$ be an $n$-dimensional manifold, and let $k$ be an integer such that $0\leq k\leq n$. A $k$-dimensional [[Embedding|embedded submanifold]] of $Y$ is a subset $X\subset Y$ such that for every point $p \in X$ there exists an [[atlas|chart]] $(U, \phi)$ such that $\phi(X\cap U)$ is the intersection of a $k$-dimensional [[plane]] with $\phi(U)$.
>
>In this case, $X$ is a manifold under the subspace topology from $Y$, and the pairs $(X\cap U, \phi_{X\cap U})$ form an atlas for the structure on $X$.

%% >[!claim] A lemma
>Suppose $X\subset Y$ is endowed with the subspace topology, and $f:X\to Z$ is a continuous map under said subspace topology. Then, $X$ is [[locally closed]].

This is actually really stupid. $f:X\to Z$ is a continuous map, thus the pre-image of $Z$, $X$ itself, must be an open set. Loading. %%

>[!claim]
> Suppose $F:X\to Y$ embeds $X$ into $Y$. Then, $X$ is open in its closure. This is called being [[locally closed]].

>[!proof]- Some cap
>For each point $x\in F(X)$, there is a neighborhood $U$ in $Y$ such that $U\cap F(X) = U\cap C$ for some closed set $C$ in $Y$.
>
>Proof: take a chart of $x$ (in $Y$!!) called $(V, \phi)$. We now consider $V\cap F(X)$; this is an open set in the $F(X)$-topology, thus it is homeomorphically mapped to an open neighborhood of $x$ in the $X$ topology. I can thus find a chart of $x$ in the $X$ topology, say $(U', \psi)$, which lies completely inside $F^{-1}(V)$. We now further assert that the closure of $U'$ (in the $X$ topology) lies completely inside $F^{-1}(V)$; this is trivial because $U'$ is homeomorphic to $\RR^n$.
> 
>Now, pushing $U'$ forward again through $F$, we find that there must exist an open set $U\in Y$ such that $U\cap F(X) = F(U')$. Pick this $U$. $\conj{F(U')} = F(\conj{U'})$ is a closed set, and clearly $U\cap \conj{F(U')} = F(U')$, because $F(U')\subset U$, $F(U')\subset \conj{F(U')}$, and $U\cap \conj{F(U')}\subset U\cap V\cap \conj{F(U')}$.

>[!todo]
>Make sure this is not cap

>[!proof]- This is what you expect.
>Suppose we start from the first definition. By identifying $X$ with $F(X)$, we find (by definition of manifold) that for every point $p\in X$, there exists a chart $(V,\psi)$; a subset $V\subset X$ which is open in $X$ homeomorphic to an open set $W\subset \RR^k$ under $\psi:V\to W$.
>
>What it means for $V$ to be open in $X$ is that $V = U'\cap X$ for some open $U'\subset Y$. Now, pick a chart $(U,\phi)$ inside $U'$ which maps to $W'\subset \RR^n$ (wlog $U = U'$). By taking $\phi\circ \psi^{-1}$ we have a regular function $\RR^k\to \RR^n$ which maps homeomorphically into its image. At $\psi(p)$, this function has some derivative which spans a subspace; use any $n-k$ linearly independent vectors which are not in this subspace to fill out the basis, such that we have a function $f:\RR^n\to \RR^n$ such that
>$$
>	f(q) = (\psi^{-1}(q)_1,\dots, \psi^{-1}(q)_k, 0, \dots, 0)
>$$
>for all $q\in \phi(V)$.
>
>For some sufficiently small open neighborhood of $\psi^{-1}(p)$, this function is invertible by construction. Then, $f\circ \phi$ is the desired chart.