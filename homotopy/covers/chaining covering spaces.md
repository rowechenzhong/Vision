$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$

> [!example] Chaining Covering Spaces
 Given maps $p:X\to Y$ and $q:Y\to Z$, suppose both $q$ and $p\circ q$ are covering maps. If $Z$ is ==*locally connected*==, then $p$ is a covering map. 

This is another basic [[point-set results on covering spaces|point-set result]], but it is especially nice because it only references the arrows.

> [!proof]- 
 This is one of those proofs where your hand is forced at every turn. Pick a $y \in Y$, and let $z = q(y)$, such that $y\in q^{-1}(z)$. We can use all the conditions now; pick a connected neighborhood $U$ of $z$ which is evenly covered by $q$ and $q\circ p$. We know that $$ q^{-1}(U) = \bigsqcup_{\alpha\in A} V_\alpha $$ and $$ (p\circ q)^{-1}(U) = \bigsqcup_{\beta\in B} W_\beta $$ where each $V_\alpha$ and $W_\beta$ are homeomorphic to $U$. In particular, they are all connected. Now, suppose $y\in V$. We want to show that $V$ is evenly covered, and we're going to use that the image of a connected open set is connected. Pick some $W_\beta$. 
>  
>  
>  
>  -  Suppose $p(W_\beta)$, which is connected, does *not* intersect $V$. Then we don't care about it. 
>  
>  -  Suppose $p(W_\beta)$ *does* intersect $V$. By set theory, I know that $p(W_\beta)\in \bigsqcup_{\alpha\in A} V_\alpha$. But $p(W_\beta)$ is supposed to be connected, and each $V_\alpha$ is disjoint, thus $p(W_\beta)\subset V$. Then, I can go from $W$ to $U$ via $q\circ p$, then to $V$ via $q^{-1}$ (which is a homeomorphism from $U$ to $V$)! Thus $W$ is homeomorphic to $V$. 
>  
>  By set theory, I know that $p^{-1}(V)$ is contained in $\bigsqcup W_\beta$. Thus $V$ is evenly covered.s