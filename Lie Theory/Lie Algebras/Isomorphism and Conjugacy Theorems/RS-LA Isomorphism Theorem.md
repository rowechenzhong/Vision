$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
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