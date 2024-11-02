>[!definition] Representation
>If $X$ is a finite-dimensional vector space over $\RR$ or $\CC$, and the action is linear, then the action is called a ==**representation**==.
>
>(If $G$ is complex, then the vector space should be complex, but if $G$ is real the vector space can be $\RR$ or $\CC$).

>[!example] Classical
>$\GL_n(\RR)$ and all of its subgroups act on $\RR^n$ by linear transformations; $\GL_n(\CC)$ and any of its Lie subgroups act on $\CC^n$.
We now import [[Representation Theory]].

# Pending Proof

>[!theorem] Pending proof
>The stabilizer $G_x\subset G$ is a *closed* Lie subgroup, and the natural map $G/G_x\to X$ (sending left cosets to their actions on $x$) is an injective immersion whose image is $Gx$.

>[!theorem] Corrolaries
>The orbit $Gx\subset X$ is an immersed submanifold, and we have a natural isomorphism $T_x\cong T_1G/ T_1 G_x$.
>
>If $Gx$ is an embedded submanifold, then the map $G/G_x\to Gx$ is a diffeomorphism.

(By the first isomorphism theorem I think)

>[!example] Homogenous Space
>If $G$ acts on $X$ transitively, then $X\cong G / G_x$ for all $x$ -- thus $X$ is a homogenous space.
>
>Then, the map $p:G\to X$ via $p(g) = gx$ is a locally trivial fibration with fiber $G_x$.