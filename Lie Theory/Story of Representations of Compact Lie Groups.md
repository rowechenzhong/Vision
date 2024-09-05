Let us remind ourselves of the finite group story.

We are investigating group algebra homomorphisms $\rho:\CC[G]\to \End V$ for finite-dimensional $V$. In the Lie group case, the algebra on the LHS is $L^2(G,\CC)$ with the algebra operation $\ast$ via$$(f\ast h)(x) = \int_G f(g^{-1}x)h(g)dg.$$The embedding is $g\mapsto \delta(xg^{-1})$, where the RHS is a distribution to be precise, but we won't be here. The ==**left regular representation**== has the interpretation of left-shifting now; $\psi\mapsto \psi\circ L_{g^{-1}}$. Yes, in addition to being the left-multiplication map under this algebra, this is the representation you remember, $\rho(g): h\mapsto gh$. Yes, we can flip signs or transpose and get other conventions, just work with me here. This regular representation is extremely important in both the finite and Lie case.

>[!idea] Even in the finite case, we should regard $\CC[G]\equiv L^2(G)$.

Then, we obtain a unitary structure. The key idea here is that under the $\braket{\bullet,\bullet}$ endowed by $\CC[G]$ or $L^2(G)$, any Hermitian form $[\bullet,\bullet]$ can be upgraded to an averaged Hermitian form $\{\bullet,\bullet\}$ which is $G$-invariant, by embedding $\eta: V\curvearrowright L^2(G,V)\equiv L^2(G)\otimes V$ via $\eta(v)(x) = \rho(x)(v)$ and then considering the tensor product $\braket{\bullet,\bullet}\otimes [\bullet,\bullet]$

We obtain that sub-representations admit orthogonal complements, and thus all finite-dimensional representations are completely reducible.

>[!idea] This $\eta$ map is a morally correct way to think about any finite-dimensional representation.
>There are several moving pieces here. $L^2(G)\otimes V$ is the natural ==**induction**== extending $V$ as a $\CC$-module to $L^2(G)$.

Okay, now what. In both the finite group story and the Lie group story, we now define ==**characters**== $\chi_V\in L^2(G)$ via $\chi_V(g) = \Tr(\rho(g))$. This is immediately sensible for finite-dimensional representations. Drawing analogy from Fourier analysis, the finite case, or formally evaluating the integral over $L^2(G)$, we obtain $\chi_{L^2(G)} = \delta(x)$.

The ==**matrix coefficients**== are defined by considering the doubly $G$-invariant map $G\to V^*\otimes V$ given by $\rho$, and flip this to an isometric $\xi_V\in\Hom_G(V\otimes V^*, L^2(G))$ which extends to an isometric doubly $G$-invariant map $\bigoplus_{V\in \Irrep(G)} V\otimes V^*\hookrightarrow L^2(G)$.

The characters are thus also orthonormal inside the conjugation-invariant functions $L^2(G)^G$ (as $\chi_V = \xi_V(\id_V)$ and $\id_V$ is permeable), also known as the ==**class functions**==. In the finite case, we immediately get that **the number of irreps is $\leq$ the number of conjugacy classes $<\infty$**.

>[!idea] Deep thing
>In the infinite-dimensional case, there are a continuum of conjugacy classes, but a countable number of *rational* conjugacy classes. Look at the $U(1)$ case; any fixed $q\in \ZZ$ yields a conjugacy class $\{\frac{p}{q}: (p,q) = 1\}$, and the only representations are $z\mapsto z^q$. Conjugacy classes do not naturally biject to irreps, but the cardinality arguments should carry over.
>
>More specifically, the space $L^2(G)$ is ==**separable**==; $G$ can be given a finite atlas, on which each chart is a Borel measurable compact subset of $\RR^{\dim G}$. Thus, it admits a countable orthonormal basis. This is why things like $\sum_{V\in \Irrep(G)}$ are valid.

The really good thing about characters is that they're additive under $\bigoplus$; the matrix coefficients don't have the correct type and the best you can do is a big tensor product. Thus, we already know by complete reducibility that $\chi_W = \sum_{V\in \Irrep(G)} \braket{\chi_W | \chi_V}\chi_V$; you don't need Peter-Weyl to see this. If only we could apply this to the regular representation, we would obtain Peter-Weyl, because then $L^2(G) = \bigoplus_{V\in \Irrep(G)} V^{\dim V}$ as desired.