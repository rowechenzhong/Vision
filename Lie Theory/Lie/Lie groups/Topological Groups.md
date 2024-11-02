>[!definition] Topological Groups
>A topological group is a group $G$ which is also a topological space, so that the multiplication map $m : G\times G\to G$ and the inversion map $\iota: G\to G$ are continuous.

>[!idea]
>So for example, left and right translation are homeomorphisms; the neighborhoods of a point $g$ are precisely the neighborhoods of $1$ shifted by $g$.

>[!example]
>For example, the group $(\RR, +)$ of real numbers with the operation of addition and the usual topology of $\RR$ is a topological group, since the functions $(x,y)\to x + y$ and $x\to -x$ are continuous. Also a subgroup of a topological group is itself a topological group, so another example is rational numbers with addition, $(\QQ, +)$. This last example is not a very good model for continuity, however, and shows that general topological groups are not very well behaved.

Thus, we will focus on a special class of topological groups called **Lie groups**, which are also [[topological manifolds]].

>[!problem]
>Let $H\trianglelefteq G$ be a [[discrete topology|discrete]] normal subgroup of a [[connected]] topological group. Then, $H$ is [[central]].

>[!solution]-
>Fix any $h\in H$. Consider the function $f(g) = ghg^{-1}$; this is a continuous function $G\to G$, which we know maps into $H$ only. In particular, for all $h'\in H$, for sufficiently small neighborhoods $h'\in U$, $U\cap H = \{h'\}$; thus the pre-image of each $h'$ must be a disjoint open cover of $G$. $G$ is connected, thus exactly one of these must be $G$ and the rest must be $\emptyset$; we know that $1\in f^{-1}(h)$, so we are done.