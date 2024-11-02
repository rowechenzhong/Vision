---
aliases:
  - Peter-Weyl
  - Peter Weyl Theorem
---
See also [[Story of Representations of Compact Lie Groups]]
# Unitary Representations

Let $V$ be a finite-dimensional representation of a compact Lie group $G$.

>[!theorem] Unitary Structure
> $V$ admits a $G$-invariant Hermitian inner product $\braket{\bullet, \bullet}$, and in particular is completely reducible.

We copy the finite-group proof. Fix any Hermitian form $[\bullet,\bullet]$ and average via $\braket{v,w}\equiv \int_G [gv, gw]dg$; then $\braket{\bullet,\bullet}$ is the desired inner product. For any sub-representation $W\subset V$, $V = W \oplus W^\perp$.

From now on, finite-dimensional representations of compact Lie groups are assumed unitary under $\braket{\bullet,\bullet}$.

# Matrix Coefficients

Now, let's upgrade the character theory of finite groups.

>[!definition] Matrix Coefficients
>For any irreducible $V$, pick an orthonormal basis $v_1,\dots, v_n$. The corresponding ==**matrix coefficients**== of $V$ are the $n^2$ smooth functions
>$$
>	\psi_{V,ij} = \braket{\rho_V(g)v_i, v_j}.
>$$

> [!theorem] Orthogonality
> For any irreducible $V,W$ and $i,j,k,\ell$,
> $$\int_G \psi_{V,ij}(g) \overline{\psi_{W,k\ell}(g)}dg = \frac{\delta_{ik}\delta_{j\ell} \delta_{VW}}{\dim V}$$where $\delta_{VW}$ is $1$ if $V$ is isomorphic to $W$ and $0$ otherwise.

This is all slightly stupid though. We should imagine $\rho_V:G\to \End V$ as a collection of $n^2$ smooth functions; we simply claim that these smooth functions are orthonormal in $L^2(G)$, both within $V$ and between $V,W$. Picking a basis is unnatural, but each collection of $n^2$ smooth functions is totally reasonable.

>[!idea] Waffles
>I like to think that the collection of possible representations is discrete, thus selecting individual irreps is graceful.

>[!proof]- Easy
> Okay, well the point now is that $P = \int_G \rho_{V\otimes W^*}\in \End (V\otimes W^*)$ has a $G$-invariant image. If $V\not\cong W$, $(V\otimes W^*)^G = 0$, thus $P = 0$. Otherwise, $(V\otimes V^*)^G = \CC \id$, that is, the span of $\sum_i v_i \otimes v^*_i$. There's probably a better way to do this next step, but as brute force, observe that $g\mapsto g^{-1}$ is a measure-preserving transformation on $G$, thus $P = \int_G \rho^{-1}_{V\otimes W^*} = \overline{\int_G \rho^\top_{V\otimes W^*}}$ is Hermitian. Thus, $P$ is a multiple of the orthogonal projector onto $\id\in V\otimes V^*$. Clearly $P(\id) = \id$, thus we conclude.

# Peter-Weyl Theorem

The really deep thing:

>[!theorem] Peter-Weyl Theorem
>$\psi_{V,ij}$ form an orthonormal basis of $L^2(G)$.

Here is a re-formulation.

>[!idea]- Observe that $L^2(G)$ is a $G$-representation under the right-translation action $\psi\to \psi\circ R_g$. This is the ==**right regular representation**==
>This is true, because $g(h(\psi))(x) = ((\psi\circ R_h)\circ R_g)x = \psi(ghx)$. The important thing to remember is that $g\mapsto R_g$ is a homomorphism while $g\mapsto L_g$ is an anti-homomorphism.

> [!idea]- Observe that $\Hom_G(V, L^2(G)) \cong V^*$ as $G$-modules.
> The LHS is the space of $\psi$ such that$$
> \begin{array}{rll}
> 	V & \stackrel{\psi}{\to} & L^2(G)\\
> 	\rho\downarrow & & \downarrow\rho\\
> 	V & \stackrel{\psi}{\to} & L^2(G)\\
> \end{array}
> $$where $L^2(G)$ is given the right-regular representation (say). Any (linear map) $\psi\in \Hom(V,L^2(G))$ is also a map $G\to V^*$ via $(\psi(h))(v) \equiv \psi(v)(h)$ for all $h\in G$, $v\in V$; in our situation this means $\rho^*(g)\psi(h) = \psi(hg)$. But then $\psi(g) = \rho^*(g)\psi(1)$, which is just $V^*$.
> 
> This also works if $L^2(G)$ is given the left-regular representation.

> [!idea]- Alternative path, identical formulation
> The matrix coefficients above are considered as a mapping $\psi_V:V\otimes V^*\to L^2(G)$. This is simply not deep, $\xi = \bigoplus \psi_V$ is injective because it is in fact an isometry.
> 
> This is an embedding of $G\times G$ modules, because everything is naturally acted on; observe that the action of $(h,k)\in G\times G$ is $\braket{\rho(g)\rho(k)v_i, \rho(k)v_j}$ as expected from its action on $V^*\otimes V$.

Thus, we have an embedding of $G\times G$-modules$$
	\xi: \bigoplus_{V\in \Irrep(G)} V\otimes V^* \cong \bigoplus_{V\in \Irrep(G)} V\otimes \Hom_G(V, L^2(G))\hookrightarrow L^2(G)
$$where the final inclusion is by contraction ("plugging into $\Hom_G(V,L^2(G))$"), and we let the imagine of $\xi$ be the ==**algebraic part of $L^2(G)$**==, $L^2_{\text{alg}}(G)$. This characterizes $L^2_{\text{alg}}(G)$ as exactly the subspace of $\psi\in L^2(G)$ which generate a finite-dimensional representation under left translations by $G$ (or right-translations).

>[!theorem] Peter-Weyl II
>The space $L^2_{\text{alg}}$ is dense in $L^2(G)$.

We write that $\xi: \widehat\bigoplus_{V\in \Irrep(G)} V\otimes V^* = L^2(G)$ where $\widehat\bigoplus$ is the Hilbert space completion of the direct sum.

> [!idea] Deep idea: This is an instance of the [[Dual Centralizer Lemma|Double Centralizer]] phenomena!
> We're considering $A$ to be the algebra of "span of left-translation actions $\bigoplus_{g\in G} L_g \CC$." $A$ sort of looks like $L^2(G)$ in its own right, with actions given by $\psi(x)\mapsto \int f(g^{-1})\psi(gx)dg$ for $f\in L^2(G)$ (note that this Hilbert space does not contain $\psi(x)\mapsto \psi(gx)$ at all; I'm essentially waffling here; but one imagines that this is the correct completion). $B$, the centralizer of $A$, looks like right-translations, isomorphic to $L^2(G)$ under $\psi(x)\mapsto \int f(g)\psi(xg^{-1})dg$. (It is obvious that these lie in the centralizer, and you can convince yourself that these span (a dense subset of) the centralizer).

>[!claim] $\chi_V(g)$ form an orthonormal basis of $L^2(G)^G$, the space of conjugation-invariant functions in $L^2(G)$.

This notation is kind of bad...? Like of course $L^2(G)$ is also a representation under $\psi(x)\mapsto \psi\circ L_g\circ R_g$, but this isn't the same representation we were using before. Shrug!

The proof is to pick a convergent sequence in $L^2_{\text{alg}}$ and then average each element $\int_G \psi_n(gxg^{-1})dg$.