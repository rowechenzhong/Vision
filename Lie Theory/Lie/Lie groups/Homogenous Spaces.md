Suppose $G$ is a Lie group of dimension $n$, and $H\subset G$ is a closed Lie subgroup of dimension $k$. Then, the ==**homogenous space**== $G/H$ has a natural structure of an $n-k$ dimensional manifold, and the map $p:G\to G/H$ is a [[Fiber Bundle|fiber bundle]] with fiber $H$.

>[!proof]- Verification
>To verify this, well, pick any $\conj{g}\in G/H$, and I'll give you a chart. Let $g\in p^{-1}(\conj{g})$ be a representative (to prove something about a quotient, you always have to work in the ambient space). Then, $gH\subset G$ is an embedded submanifold (left translations are diffeomorphisms).
> 
> Pick a small [[transversal submanifold]] $U$ through $g$ (e.g., $U$ fits in a chart at $g$ where [[k-slicing theorem|k-slicing]] applies). Then, we claim that $UH$ is open. Indeed, for any $uh\in UH$, WLOG $h = 1$. Then one can find an open ball around $u$
> 
> If we pick $U$ to be a small open disk inside a chart at $g$, it is clear that $UH$ is an open set, thus $\conj{U}$ is open in the quotient topology. It is also clear that $p:U\to \conj{U}$ is a homeomorphism, which defines a local chart near $\conj{g}\in G/H$; such charts are easily checked to be regular.
> 
> The multiplication map $U\times H\to UH$ is a diffeomorphism, thus $p$ is a locally trivial fibration.

>[!idea]
>$G/H$ is not a group, generically; it is simply the set of left-cosets which has a natural manifold structure.

>[!theorem]
>We have a natural isomorphism $T_1(G/H)\cong T_1G / T_1H$.
> 
>If $H$ is also connected, then $p_0: \pi_0(G)\to \pi_0(G / H)$ is a bijection; this is basically clear.
>
>If $G$ is also connected, then we have a nontrivial exact sequence $\pi_1(H)\to \pi_1(G)\to \pi_1(G / H)\to 1$.
>
> If $H\trianglelefteq G$, then $G/H$ is a Lie group. 

>[!idea] Waffles
>There is a ==**long exact sequence of homotopy groups of a fibration**==



>[!proof]-
>$G/H$ is a group just because this is how groups work. Its operations are diffeomorphisms because we can compose through the fibration.
>
>$T_gG\to T_{\conj{g}} G/H$ is a surjective linear map with kernel $T_g gH$ (because $T_{\conj g} G/H$ in the above proof is isomorphic to $T_gU$). Thus, for $g = 1$ we get $T_1(G/H)\cong T_1G / T_1H$.