A ==**lie algebra**== over a field $k$ is a vector space $\fg$ over $k$ equipped with a ==**lie bracket**== $[\bullet, \bullet] : \fg \times \fg \to \fg$ which is

-   Bilinear
-   Skew-symmetric
-   Satisfies the ==**Jacobi Identity**==
    $$[[x,y],z] + [[y,z],x] + [[z,x],y] = 0$$

>[!example] Linear Lie Algebras
>Any subspace of $\gl_n(\KK)$ closed under the commutator is called a ==**Linear Lie Algebra**==.

>[!example] Canonical Construction
>Given an algebra $A$, the commutator $[x,y] = xy - yx$ yields a Lie algebra. The associative algebra $A$ is then called the ==**enveloping algebra**== of the resulting Lie algebra.
>
>It will later turn out that all Lie algebras can be embedded in such an algebra in this manner!

The most legendary example: [[Tangent spaces of Lie groups are Lie Algebras]].

Sometimes, we like to think of $[x,\bullet] = \Ad_x$ as a map in its own right. In this case, it is a derivation, and $x\to \Ad_x$ is the ==**adjoint representation**== of $\fg$.

Another example: [[Derivations are Lie Algebras]]. Thus, [[Vect(X)]].

>[!problem] Random problem
>Let $L$ over an algebraically closed field and let $x\in L$. Show that the subspace of $L$ spanned by eigenvectors of $\ad x$ is a subalgebra.

> [!solution]-
> Indeed, if $[x,y] = \alpha y$ and $[x,z] = \beta z$, then $[x,[y,z]] = [[x,y],z] + [y, [x,z]] = (\alpha+\beta)[y,z]$.

# Intro Subsequence
- [[Lie algebra Cat words]]
- [[Derivations are Lie Algebras]]
- [[Useful Ideals]]
- [[Automorphisms]]
- [[Linear Algebra and Lie Algebra]]

Basic concepts:
- [[Solvability and Nilpotency]]
- [[Lie's Theorem]]
- [[Jordan Canonical Form]]
- [[Engel's Theorem]]
- [[Cartan's Criterion]]

Massive amounts of theory:
- [[Semisimple Lie Algebras]]
- [[Lie Algebras and Bilinear Forms]]
- [[Killing Form]]