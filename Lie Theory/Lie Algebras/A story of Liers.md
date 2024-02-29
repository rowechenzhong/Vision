This is a [[story]].

# Prelude: Differential Geometry

General topological spaces can sometimes be pathological, e.g. too large (long line, not second-countable), not respect limits (non-Hausdorff). So we will now restrict attention to some of the nicest spaces possible, [[topological manifolds]], which are locally homeomorphic to $\RR^n$. The basic trick here is that whenever you want to make a query to an open set on a manifold, you instead look at a local chart that maps it to $\RR^n$.

Now, sometimes this still isn't nice enough for us. We primarily care about analytic functions from $\RR^n$ (or $\CC^n$). The problem is that, if the underlying charts on your manifold don't possess the degree of smoothness you require, you're waffling about nothing. So we restrict our attention to analytic manifolds, which have the property that their atlas is smoothly stitched together. This smooth stitching is known as a structure; manifolds can have non-diffeomorphic structures, so this is additional data.

The next main idea to get a hold of is that of [[tangent spaces]], which are infinitesimal displacements about any point on your manifold. The nontrivial idea is that infinitesimal displacements are equivalent to derivations at your point. Thus we consider the space of linear functionals on germs.

The final idea is that of submersions, immersions, and submanifolds. A submersion is a map which is locally surjective. A immersion is a map which is locally injective, but possibly not globally so. An immersed submanifold is an immersion which is locally and globally injective, but possibly not compatible with the induced topology. An embedded is a map which is locally and globally injective, and homeomorphic to the subspace topology of its image; such manifolds are automatically locally closed, but might not be so globally. A closed embedded submanifold is an embedded submanifold which is also closed in its ambient space.

# Chapter 1: Lie Groups

A lie group $G$ is a manifold endowed with a regular group action $m: G\times G \to G$, and a diffeomorphic inversion. Any lie group is an extension of a discrete countable group by a connected Lie group, by considering the path-connected component of the identity. **Lie groups will always be considered connected from now on.** Any connected lie group can also be extended to a simply-connected lie group via $\pi_1(G)$; this is its covering space; but this simplification will not be needed for a while. (As a side effect, $\pi_1(G)$ is always abelian).

The main thesis going forward is that $\fg = T_1 G$ encodes tremendous amounts of information about $G$. An open neighborhood of $1$ obviously generates $G$, so this should be clear.

### A side-quest on quotients and actions on manifolds

If $H\subset G$ is any subgroup, then as a topological space, the cosets $G / H$ may not form a manifold. The desired condition is that $H\subset G$ is a closed Lie subgroup, i.e. an embedded submanifold (these are equivalent for difficult reasons). Then as a topological space, $G / H$ is a $n-k$ dimensional manifold, and $G\to G / H$ is a locally trivial fibration with fiber $H$, such that as vector spaces $T_1(G / H) = T_1G /T_1 H$. This is called a **homogenous $G$-space**.

Then, if $H\trianglelefteq G$, then $G / H$ is a lie group as desired. Thus the natural analogue of a normal subgroup is a closed normal Lie subgroup.

If $H\subset G$ is a subgroup which is merely an immersed submanifold (with manifold structure from the source), we call $H$ a Lie subgroup. The main isomorphism theorems can then be written. If $f:G\to H$, then $\ker f$ is a closed normal Lie subgroup. Then, $\im f$ is an immersed submanifold which is also a Lie subgroup in $H$. As expected, $G / \ker f \cong \im f$ as Lie groups.

Generically, $G$ might act on some manifold $X$ with some regular action $G\times X\to X$. Then, by standard results of group theory, for any $x\in X$, $G_x$ is a normal subgroup. It also happens to be a closed Lie subalgebra. Meanwhile, any orbit $Gx\subset X$ is an immersed submanifold. The quotient space $G / G_x$ is naturally isomorphic to $Gx$.

###  Vector Space Representations
A representation of a Lie group $G$ on a complex vector space $V$ is a lie group homomorphism $G\to \GL_n(\CC) = \GL_V(\CC)$. We will always be considering $\CC$-vector spaces, so things like the second half of Schur work.

We have the usual notions of homomorphisms of representations via intertwining operators $A:V\to W$, subrepresentations, direct sums, duals, irreducible (nonzero, and only subrepresentations are $0$ and $V$), indecomposible (nonzero, and cannot be written as a direct sum of two nonzero representations).

Schur's lemma applies: if $V$ and $W$ are irreducible representations and $A:V\to W$ is some intertwiner, then either $A$ is $0$ or an isomorphism. Furthermore, if $A:V\to V$, then $A$ must be a scalar.

The quintessential representation of a Lie group is $g_*:\fg\to \fg$ via the **adjoint representation**; this is the differential of the conjugation action $G\curvearrowright G$.

In the case of unitary representations, where $\rho:G\to U(V)\subset \GL_n(\CC)$, any unitary representation is a direct sum of irreducible representations.

As an example of an explicitly non-unitary representation, the usual representation of invertible upper-triangular matrices is reducible but not decomposible, and thus admits no unitary representations.

Of course, if $G$ is finite, then by the averaging trick we find that any representation is unitary and all finite dimensional representations of $G$ are completely reducible.

### Canonical Vector Field

Given $T_1G = \fg$, we can act on this tangent space by $g\in G$ to obtain a canonical identification of $T_1G$ with $T_gG$. This is self-consistent, and any choice of $v\in \fg$ yields a canonical left-invariant vector field $L_v$ inside the vector bundle $TG$.




# Chapter 2: Lie Algebras

>[!todo] PBW

### Side quest: theorems of Engel and Lie

We now meet some new characters in our story. Given any $\fg$, I can write a descending and ascending *central series*, which are different ways to reduce Lie groups. If the series $\fg^{k+1} = [\fg^k, \fg^k]$ vanishes, $\fg$ is called *solvable*; the canonical example is the set of upper-triangular (with the diagonal!) matrices:
$$\begin{pmatrix}
* & * & *\\
 & * & *\\
 &  & *\\
\end{pmatrix}.$$If the series $\fg_{k+1} = [\fg, \fg_k]$ vanishes, $\fg$ is called *nilpotent*; this is a stronger condition. The canonical example is the set of *strictly* upper-triangular matrices.
$$\begin{pmatrix}
 & * & *\\
 &  & *\\
 &  & \\
\end{pmatrix}$$

>[!todo] Theorems of Engel and Lie

### We are given the main quest

The radical of $\fg$, $\Rad(\fg)$, is the sum of all solvable ideals of $\fg$. This is the *largest* solvable ideal. $\fg$ is *semisimple* if $\Rad(\fg) = 0$.

Then, $\fg / \Rad(\fg) = \fg_{ss}$, the *semi-simplification* of $\fg$. Thus any $\fg$ is a semidirect product of a semi-simple part and its radical. We have the short exact sequence
$$0\to \Rad(\fg)\to \fg\to \fg_{ss}\to 0$$A crucial property of $\CC$ is that this sequence splits! This is the *Levi Decomposition*.

We can decompose semisimple lie algebras into a direct sum of *simple* lie algebras $\fg$, whose only ideals are $0$ and $\fg$; this is iff. The canonical example of simple Lie algebra is $\sl_n(\CC)$. $\so_n(\CC)$ is semisimple in all dimensions except $n = 4$.

A *reductive* Lie algebra is a direct sum of a semisimple part and the center of the lie algebra. The canonical example is $\gl_n(\CC) = \sl_n(\CC)\oplus \CC$.

### A weapon bestowed
The *killing form* is the canonical form you can create from our product, $\tr_\fg(\ad x \ad y)$. This is a symmetric associative form. The *Cartan Criteria* tells us that $\fg$ is solvable iff $[\fg,\fg]\subset \ker K$, and that $\fg$ is semisimple iff $K$ is nondegenerate.

More generally, we can give any representation $\rho: g\to \End V$. In this case, we have a natural form $B_V(x,y) = \Tr_V(\rho(x)\rho(y))$. There exists $V$ such that $B_V$ is nondegenerate, iff $\fg$ is reductive!

### A Schur upgrade
Every finite-dimensional representation of $\fg$ is completely reducible iff $\fg$ is semisimple; $V = \oplus_i V_i$, where each $V_i$ is irreducible.

Please observe that for simply connected complex Lie groups, the representations of $\fg$ are the same as those of $G$.

If $\fg$ is semisimple, then $Aut(\fg)\subset \GL(\fg)$. Then, $G = Aut(\fg)^0 = G_{ad} = G / Z(G)$ may not be simply connected, but $\Lie G_{ad} \cong \fg$ still. $G_{ad}$ is the image of $G$ in the adjoint representation.

# Main Quest of 18.745
A *Cartan subalgebra* $\hh\subset \fg$ is a maximal commutative subalgebra consisting of semisimple elements.  they're also maximal just among commutative subalgebras, but this is not sufficient. All Cartan subalgebras are conjugate under the action of $G$.

For example, if $\fg = \sl_n$, then an example of $\hh$ is the set of (zero-trace) diagonal matrices.

It is well-known that $\hh$ can be simultaneously diagonalized. Then, we can split $\fg$ into root spaces by their eigenvalues under $\hh$; the eigenvalues are in $\hh^*$. We obtain root spaces $\fg_\alpha$ for $\alpha \in R$, along with $\hh = \fg_0$. Here are some properties of any maximal toral subalgebra $\hh$.
- $[\fg_\alpha, \fg_\beta] \subset \fg_{\alpha + \beta}$.
- If $B$ is a nondegenerate invariant bilinear form (e.g. Killing), then $\fg_\alpha \perp \fg_\beta$ unless $\alpha + \beta = 0$. There exists a $\fg_\alpha \times \fg_{-\alpha}\to \CC$
-  if $\alpha \in R$, then $-\alpha \in \fg$.
If $\hh$ is actually maximal, then
-  $\dim \fg_\alpha = 1$.
-  $\abs{R} = \dim \fg - rank \fg$.
-  $R$ span $\hh^*_\RR$, which is just a real subspace of $\hh$. In other words, the span of $R$ can be complexified to $\hh$.
-  $K^{-1}\big\vert_R$ is nondegenerate on $\hh^*_\RR$.

# Timeskip: into the land of verma modules XD

There is this thing called a **Verma module**. It is $\{v_\lambda | hv_\lambda  = \lambda(h) v_\lambda: h\in \hh, e_i v_\lambda =0 \}$.

Any **heighest weight module** with weight $\lambda$ is some quotient of $M_\lambda$.

Any finite dimensional irreducible representation of $\fg$ is a heighest weight representation, because you can take the weight decomposition and find a highest weight $\lambda$ (such that $\lambda + \alpha_i$ is not a weight for any $i$).

Note that for any $\lambda \in \hh^*$ (not necessarily integral), there is a smallest quotient $M_\lambda / J_\lambda = L_\lambda$, which is irreducible but in general $\infty$-dimensional and complicated.

There is a theorem: $L_\lambda$ is finite-dimensional iff $\lambda$ is a dominant integral weight ($\lambda \in P_+$). There's a correspondence. The explicit presentation is just $M_\lambda / \braket{f_i^{n_i+1} v_\lambda}$. 

### Weyl Character Formula

There is like a thing, $V = \bigoplus_\mu V[\mu]$, where $\dim V[\mu] < \infty$ (these are weight spaces I guess). You can compute what the sizes of all of these things are. We actually look at the **character** of each of these weights, $\chi_V = \sum_\mu \dim  V[\mu] e^\mu$ lmao what is this guy. What is $\CC[P]$. If $V$ is finite dimensional then $\CC[P]$ is now a ring (yay?)

Then uh $\tr_V( e^{h\in \hh}) = \sum_\mu \dim V[\mu] e^{\mu(h)}$.

The WCF tells you something. Lol. $\rho$ is the $\delta$-weight guy. There is a sign character $\det: W\to \pm 1$. This sends every simple reflection to $-1$; the element $s_{i_1}\dots s_{i_m}$ gets sent to $(-1)^m$. On one hand $\rho$ is the sum of the fundamental weights; on the other hand it is the $\frac12$ such of the $R_+$ guys.

Theorem. $\chi_{L_\lambda} = \dots$.