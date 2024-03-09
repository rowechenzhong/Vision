Let $L$ be a [[simple ideal|simple]] lie algebras over algebraically closed $F$. Let $H$ be its maximal [[Toral Subalgebra]]. Let $\Phi\subset H^*$ be the set of roots of $L$ relative to $H$. The symmetric bilinear form dual to the Killing form makes $E$ a Euclidean space, at which point $\Phi$ is a root system in $E$. Let $L', H', \Phi', E'$ be analogous.

First, you should expect that

>[!claim]
>$\bigcup_{\alpha \in \Delta} L_\alpha \cup L_{-\alpha}$ generates $L$.

This is clear, because $[L_\alpha L_\beta] = L_{\alpha + \beta}$ (this is surjective). This is why we have exactly the freedom to choose $\pi_\alpha$ with $\alpha \in \Delta$ in the below.

Also, you should expect that

>[!claim]
>If $L$ is a simple Lie algebra, with $H, \Phi$ as above, then $\Phi$ is an irreducible root system.

The contrapositive is pretty clear. Thus,

>[!claim]
>Let $L$ be a semisimple Lie algebra with maximal toral subalgebra $H$ and root system $\Phi$. If $L = L_1 \oplus \dots \oplus L_t$ is the [[Semisimple Simple Decomposition]], then each $H_i = H\cap L_i$ is a maximal toral subalgebra of $L_i$.
>
>Then, the corresponding irreducible root systems $\Phi_i$ are canonical irreducible components of $\Phi$ such that $\Phi = \Phi_1\oplus \dots \oplus \Phi_n$.

Thus we are reduced to the simple case.

> [!theorem] Isomorphism Theorem
> Suppose there is an isomorphism $\alpha \mapsto \alpha'$ from $\Phi$ to $\Phi'$ inducing $\pi: H\to H'$. Fix some basis $\Delta \subset \Phi$, with induced basis $\Delta'\subset \Phi'$. For each $\alpha \in \Delta$, choose an arbitrary Lie algebra isomorphism $\pi_\alpha: L_\alpha \to L'_\alpha$.
> 
> Then, there exists a unique isomorphism $\pi: L\to L'$ extending $\pi, \pi_\alpha$.

Recall that each $L_\alpha$ was one-dimensional, so $\pi_\alpha$ amounts to picking an arbitrary nonzero $x_\alpha \in L_\alpha$ and $x'_\alpha \in L'_\alpha$.

# Proof

The uniqueness of $\pi$ is immediate: we have mapped $x_\alpha \to x'_\alpha$ for each $\alpha\in \Delta$, which immediately induces unique $y_\alpha$ such that $[x_\alpha y_\alpha] = h_\alpha$ and $y'_\alpha$; this generates everything.

Actually, I'm going to skip this proof, TODO; the proof in Humphrey's is specific to simple Lie algebras and does some scuffed diagonal thing.