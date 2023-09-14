$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$> [!problem] Products of Manifolds
> Suppose $X$ is an $m$-dimensional manifold, and $Y$ is an $n$-dimensional manifold. Show that:
> - $X\times Y$ is an $m + n$-dimensional manifold.
> - If $X$ and $Y$ are ($C^k$/real analytic/complex analytic) then $X\times Y$ is as well.

>[!solution]- $X\times Y$ is a manifold
>$X\times Y$ is:
>- Hausdorff, obviously.
>- Has countable basis, obviously.
>- For any $(x,y)\in X\times Y$, pick the desired atlases $(U, \phi)$ and $(V, \psi)$, then $(U\times V, \phi \times \psi)$ is an atals from $U\times V$ to $\RR^m\times \RR^n \cong \RR^{m + n}$.

>[!solution] Regularity
>A multivariable function satisfies any of the above regularity conditions iff it does componentwise.

>[!problem] Implicit Function
> Let $f_1,\dots, f_m$ be functions $\RR^n\to \RR$ which are ($C_k$/RA). Let $X\subset \RR_n$ be the set of points $P$ such that $f_i(P)= 0$ for all $i$ and $df_i(P)$ are linearly independent. Use the implicit function theorem to show that $X$ is a topological manifold of dimension $n-m$ and equip it with a natural ($C_k$/RA) structure. Prove the analogous statement for holomorphic functions $\CC_n\to \CC$.
> 
> It is useful to recall the [[implicit function theorem]].

>[!todo]
>DO this!!!


