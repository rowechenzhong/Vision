>[!definition] Lie Group
>A ==**Lie group**== is [[Topological Groups|topological group]] whose topology is a [[topological manifolds|manifold]] such that the group operation is [[Regular Maps|regular]]; regularity classes are inherited from the manifold.

>[!idea] Correct Sys1
>The left translation and right translation maps $L_g, R_g:G\to G$ via $L_g(x) = gx$ and $R_g(x) = xg$ are diffeomorphisms. This is actually sufficient! Because then the mapping is $L_g(R_h(1)) = gh$, and this guy will be regular.


>[!problem]
>Show that the inversion map $\iota$ is a diffeomorphism and $\der \iota_1 = -1$

>[!idea]
>For deep reasons (Hilbert's 5th problem) any Lie group is actually an RA Lie group. So we'll stop caring about regularity class now LMAO

# Cat words

>[!definition] Arrows
>A ==**homomorphism of Lie groups**== $f:G\to H$ is a group homomorphism which is also a [[Regular Maps|regular map]]. An isomorphism is a group isomorphism such that both $f$ and $f^{-1}$ are regular.