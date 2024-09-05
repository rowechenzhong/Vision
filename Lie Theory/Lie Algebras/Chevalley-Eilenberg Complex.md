We will study the cohomology of compact connected Lie groups

>[!idea]- How did we get here?
>Basically, the Cartan Decomposition implies that any real semisimple Lie group is diffeomorphic to the product of its maximal compact subgroup and a big Euclidean space. Weak Levi Decomposition. $\RR^n$ is contractible.

Okay, recall that the [[de Rham cohomology]] exists. $b_0(M) = 1$. We know that Lie derivatives annihilate cohomology, so for any Lie group action $G\curvearrowright M$, $G$ preserves $H^\bullet(M,\CC)$.

> [!idea]- Wait, explain why?
> Actually, this is just a general thing. The space of diffeomorphisms of $M$, $D(M)$, has a Lie algebra called the smooth vector fields $\Vect(M)$. In this context, the Lie derivative is literally a Lie algebra action of $\Vect(M)$ on the full de Rham complex. All of these vector fields annihilate $H^\bullet$! So if you exponentiate, the connected component of $D(M)$ preserves $H^\bullet$. And of course, a Lie group action is just a homomorphism $G\to D(M)$; but $G$ is connected, so $G\to D(M)^\circ$, and we're good!

Now, we use the ubiquitous averaging trick again. Given any Lie group action $G\curvearrowright M$, we can consider the averaging operation $P:\Omega^\bullet(M)\to \Omega^\bullet(M)$. This commutes with $d$ (because all Lie derivatives commute with $d$), and is idempotent (just write out the integral). Thus, it is a projection into a $G$-invariant subspace: $$\Omega^\bullet(M) = \underbrace{\Omega^\bullet(M)^G}_{\im P} \oplus \underbrace{\Omega^\bullet(M)_0}_{\ker P}.$$
Deep fact:

>[!theorem] $\Omega^\bullet(M)_0$ is exact

>[!proof]
> Indeed, pick a closed $i$-form $\omega$. The cohomology class $[\omega] = [g\omega]$ for all $g\in G$, because Lie groups preserve cohomology! So$$[\omega] = \int_G [g\omega]dg = \left[\int_G g\omega dg\right] = 0\qquad \text{!!}$$Hence $\omega = d\eta$ is exact in $\Omega^\bullet(M)$. In fact, $\omega = (1-P)\omega = d(1-P)\eta$, so $\omega$ is exact in $\Omega^\bullet(M)_0$ as desired.

This is really good: the cohomology groups of $\Omega^\bullet(M)$ are exactly those of $\Omega^\bullet(M)^G$. Completely beautiful!

>[!idea] What happened?
>$M$ has some symmetry group $G$, hence the cohomology class of any form has a symmetric representative. Like, suppose $M$ is a torus and $G$ is a rotation about the symmetry axis. Then any $1$-form can be split into a symmetric and asymmetric component by this averaging-projection procedure. Meanwhile, the cohomology classes either lie completely in some coset under the group structure (a loop around the axis) or lie orthogonal to the group structure (a loop around the donut, contained in a single slice passing through the axis).

# Chevalley-Eilenberg Complex

In the case where $M = G$, recall that $\Omega^m(G)^G = \wedge^m \fg^*$!! This is really strong: it signifies that $\Omega^\bullet(G)^G$, the ==**Chevalley-Eilenberg complex**== of $G$, can be described purely algebraically. Indeed, by elementary differential geometry, we can compute that for left-invariant vector fields $v_0,\dots, v_m$,$$d\omega(v_0,\dots, v_m) = \sum_{i < j} (-1)^{i+j} \omega\left([v_i,v_j], v_0,\dots, \hat{v_i}, \dots, \hat{v_j},\dots, v_m\right).$$Reminder; left-invariant vector fields can be identified with $\fg$. This is super strong! This purely algebraic complex can be defined for $\fg$ over any field, taking the above as the definition of the differential. It is denoted $CE^\bullet(\fg)$, and its cohomology is called the ==**Lie algebra cohomology**==.

Comments:
- $CE^\bullet(\fg)$ has the wedge product multiplication as usual, hence $H^\bullet(\fg)$ is a graded algebra.
- If $G$ is a compact connected Lie group, and $\fg = \Lie(G)_\CC$ is the complexification of its lie algebra, then $H^\bullet(\fg)\cong H^\bullet(G,\CC)$ as graded algebras. This does not hold if compactness is dropped.
- The **Kunneth Theorem** in this context is quite simple. For compact connected Lie groups $G,K$, $\Omega^i(G)\otimes \Omega^j(K)\to \Omega^{i+j}(G\times K)$ via the usual tensor product yields an isomorphism of cohomology rings $H^\bullet(G,\CC)\otimes H^\bullet(K,\CC)\to H^\bullet(G\times K)$. The tensor product of algebras on the LHS is in the graded sense.