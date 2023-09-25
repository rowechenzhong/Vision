Let $F:X\to Y$ be a regular map. Now that we have [[differential|differentials]] which are linear maps $dF_P: T_PX\to T_{F(P)} Y$, we can talk about basic properties of linear maps.
- If $dF$ is surjective for all $P\in X$, then we call $F$ a ==**submersion**==. Intuitively, $F$ locally fills $Y$.
- If $dF$ is injective for all $P\in X$, then we call $F$ an ==**immersion**==. Intuitively, $F$ does not have a local kernel; it is locally homeomorphic to its image.

>[!problem]  Implicit Function Theorem
> In full generality-- if $F$ is a submersion then for any $Q\in Y$, $F^{-1}(Q)$ is a manifold of dimension $\dim X - \dim Y$.

>[!solution]
>This is a local question. For any $P\in F^{-1}(Q)$, we wish to exhibit a local homeomorphism to $\RR^{n-m}$. Looking at local charts $\phi: U\to \RR^n$. and $\psi: V\to \RR^m$ with $P\in U$ and $Q\in V$, we observe that $\psi \circ F\circ \phi^{-1}$ is also a submersion.
>
 Thus, we must show $\phi\circ F^{-1} Q$ is locally homeomorphic to $\RR^{n-m}$ inside $\RR^n$. This is just the [[Basic Manifold Exercises#^1292a3|Implicit Function Theorem]].
 
- An immersion $f:X\to Y$ is an ==**embedding**== if $F:X\to F(X)$ is also a homeomorphism, in which case $X\equiv F(X)\subset Y$ is said to be an ==**embedded submanifold**==.
- An embedding $F:X\to Y$ of manifolds is ==**closed**== if $F(X)\subset Y$ is a closed subset; in this case $F(X)$ is called a ==**closed, embedded, submanifold**==.

>[!example]
>The distinction between and immersion and an embedding is that embeddings cannot intersect themselves; they must remain globally separated. Immersions, on the other hand, are totally fine; you can immerse a Klein bottle in $\RR^3$, but there's no way embed it.


>[!example] Non-example
>An irrational winding

