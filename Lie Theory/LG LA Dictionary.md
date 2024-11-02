> [!theorem] Morphisms
> Let $\phi:G\to K$ induce $\phi_* : \Lie G \to \Lie K$. Then $H = \ker \phi$ is a **closed** Lie subgroup (which is obviously normal) with lie algebra $\hh = \ker \phi_*$.
> 
> This induces map $\overline{\phi}:G/H\to K$ which is an **immersion**. The image $\im \overline{\phi}$ is an immersed submanifold of $K$ Lie-isomorphic to $G / H$ with algebra $\im \phi_*\cong \fg / \hh$.

This is immediate by [[Vect(X)#^action-ker-im|this theorem]]. Note that if $V$ is a finite-dimensional representation of $G$ and $v\in V$, then $G_v$ is a closed Lie subgroup with Lie algebra $\fg_v = \{z\in \fg: zv = 0\}$.

# Fundamental Theorems of Lie Theory

>[!theorem] First Fundamental Theorem - Connected subgroups $\iff$ Lie subalgebras
>There is a bijection between connected Lie subgroups $H\subset G$ and Lie subalgebras $\hh\subset \fg$.

>[!theorem] Second Fundamental Theorem - Maps
>If $G,K$ are Lie groups with $G$ simply connected, then the map $\Hom(G,K)\to \Hom(\Lie G, \Lie K)$ via $\phi\to \phi_*$ is a bijection.

>[!theorem] Third Fundamental Theorem - Existence
>Any finite-dimensional Lie algebra admits a Lie group.

For $\KK\in \{\RR, \CC\}$, $G\mapsto \Lie G$ is an equivalence between the category of simply-connected $\KK$-Lie groups and finite-dimensional $\KK$-Lie algebras. [[LG + Homotopy|Any connected Lie group has the form $G / \Gamma$ where $G$ is simply connected and $\Gamma\subset G$ is a discrete central subgroup.]]



# Some details

>[!theorem]
>The ==**center**== $Z$ of a connected Lie group $Z$ is a closed (normal, commutative) Lie subgroup of $G$ with Lie algebra $\mathfrak z$. $G / Z(G)$ is called the ==**adjoint group**== of $G$, and is naturally isomorphic to the image of the adjoint representation $\Ad:G \to \GL(\fg)$.