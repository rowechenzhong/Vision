You should've expected this when you were learning algebraic topology LOL

# Reducing to Path-connected components

Recall the following definitions:
- Path-connected components (on manifolds, this is the same as a connected component).
- Quotient topologies

Let $G^\circ$ be the path-connected component containing $1$.

>[!claim] We only care about pc components.
>1. $G^\circ \trianglelefteq G$
>2. $\pi_0(G) = G/ G^\circ$ with the quotient topology is a discrete and countable group.

This is clear; for the second part, all cosets are open, thus the quotient is discrete; the quotient is countable just because manifolds have countable base.

# Reducing to Simply Connected Components

Recall the following from [[Homotopy Theory]]:
- [[covering spaces]] 
- [[homotopy]]

>[!idea]
>The idea of Homotopy theory was that if you are as nice as possible locally, we can talk about global structure. This is really good for Lie algebra. For instance, regularity and being a manifold are local properties, thus a covering is automatically a regular map. One can push the local coordinates through the map, and then the mapping is literally the identity in local coordinates.

Recall the basic properties of Lifting:
- [[lifting property]]
- [[lifting criterion]]
- [[unique lifting]]

You should expect that:

>[!claim]
>Suppose $X,Y$ are manifolds and $\tilde{X}$ is a covering space of $X$. If $\tilde{f}:Y\to \tilde{X}$ lifts $\tilde{f}:Y\to X$, then $\tilde{f}$ is regular iff $f$ is.

This is pretty obvious, because $f$ and $\tilde{f}$ are identical on local coordinates.
- [[constructing the galois correspondence]]

>[!definition] Universal Covering Group
> Let $\tilde{G}$ be the universal covering of $G$. Then $\tilde{G}$ is a manifold, and a group via $(x\cdot y)(t) = x(t)y(t)$.

>[!proof]- This is obviously a group, do everything pointwise.
> Recall that elements of $\tilde{G}$ are paths $x:[0,1]\to G$. The multiplication on the RHS is the group operation on $G$. Alright, then the constant path at $1$ is the identity of $\tilde{G}$, the inverse of any path can be done pointwise $(x^{-1})(t) = x(t)^{-1}$, and this guy is obviously associative.

>[!idea]
>Observe that $(x\cdot y)$ is homotopic to $y(t)$ concatenated with $x(t)y(1)$. 

>[!claim]
>- $\tilde{G}$ is a simply connected Lie group.
>- The covering $p:\tilde{G} \to G$ is a homomorphism of Lie groups.

>[!proof]- $\tilde{G}$ is a Lie group
>$\tilde{G}$ is already simply connected, a manifold, and a group. We need to show that the group operation $\tilde{m}:\tilde{G}\times \tilde{G}\to \tilde{G}$ is regular. Well, $\tilde{m}$ is a lift of the regular mapping $\tilde{G}\times \tilde{G} \to G\times G\to G$ given by
>$$
>	(x,y)\to (x(1), y(1))\to x(1)y(1)
>$$
>Thus, it is regular itself.

>[!proof]- Homomorphism
>$p$ is already a regular map. It is a homomorphism because for any $x,t\in \tilde{G}$, $x(t)y(t)$ is mapped to $x(1)y(1)$, as desired.

>[!claim]
>$Ker(p)$ is a central subgroup of $\tilde{G}$ naturally isomorphic to $\pi_1(G) = \pi_1(G, 1)$. 

>[!proof]-
>$Ker(p)$ consists of all paths in $G$ such that $x(1) = 1$, i.e., all loops. The path $x(t)y(t)$ is homotopic to $x(0)y(t)$ concatenated with $x(t)y(1)$, so this is naturally isomorphic to $\pi_1(G)$. Why are all loops central? Suppose $x\in Ker(p)$; then for any $y$, I want to show $x(t)y(t)$ is homotopic to $y(t)x(t)$. But both are homotopic to $x(t)$ concatenated with $y(t)$, in that order.

Thus, $\tilde{G}$ is a central extension of $G$ by $\pi_1(G)$ (this is what it means to be a central extension). This also shows that $\pi_1$ of any pc topological group is abelian.

The remainder of this course will focus on simply-connected lie groups.