>[!definition] Embedded Submanifold.
> An immersion $f:X\to Y$ is an ==**embedding**== if $F:X\to F(X)$ is also a homeomorphism, in which case $X\equiv F(X)\subset Y$ is said to be an ==**embedded submanifold**==.

This is stronger than being an [[Immersed Submanifold]].

>[!example]
>The distinction between and immersion and an embedding is that embeddings cannot intersect themselves; they must remain globally separated. Immersions, on the other hand, are totally fine; you can immerse a Klein bottle in $\RR^3$, but there's no way embed it.

>[!example] Non-example
>An interesting counterexample is the immersion of $\RR$ in $S_1^2$ via $x\to (e^{ix},e^{ix\sqrt{2}})$. This is an [[Immersed Submanifold]], but its not an embedding because it is not a homeomorphism.

# Intrinsic Definition

>[!idea]
>You actually just want to identify $X$ with $F(X)$ in this case, it makes the thinking easier.

For this point of view, see the [[k-slicing theorem]].

# Variants

>[!definition]
> An embedding $F:X\to Y$ of manifolds is ==**closed**== if $F(X)\subset Y$ is a closed subset; in this case $F(X)$ is called a ==**closed, embedded, submanifold**==.