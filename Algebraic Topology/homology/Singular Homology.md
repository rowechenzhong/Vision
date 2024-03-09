$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
A ==**singular $n$-simplex**== in a space $X$ is a continuous map $\Delta^n\to X$. We define $C_n(X)$ as the space of $n$-chains as usual, and define the boundary map by restricting to faces;$$\pa_n(\sigma) = \sum_i (-1)^i \sigma\vert_{[v_0,\dots, \hat{v_i},\dots, v_n]}.$$The ==**singular homology group**== is thus $H_n(X) = \ker \pa_n / \im \pa_{n+1}$.

It will turn out that the singular homology groups coincide with the [[Simplicial Homology]] groups for $\Delta$-complexes, but for now we make a more crude observation:
- Singular Homology is obviously more general than simplicial homology; each $C_n(X)$ is much larger.
- If one takes a space $X$ and assigns an $n$-simplex to each singular $n$-simplex, modding out by the obvious relations, we obtain a (large) $\Delta$-complex called $S(X)$ whose simplicial homology is manifestly the same as the singular homology.

See [[Reduced Homology Groups]].

This immediately induces a [[Chain Complexes|chain complex]] for the same reason as a [[Simplicial Homology]]. To make the dictionary complete, we need to prove two statements:
 - [[Maps of Spaces induce Chain Maps]]
 - [[Homotopies of maps induce homotopies of chain maps]]

# Introductory Problems

>[!problem] Disjoint Unions
>Compute the homology groups of the disjoint union $H_*(X\sqcup Y)$

>[!solution]-
>This is patently obvious; $C_n, B_n, Z_n, H_n$ are each direct sums of the corresponding objects.

>[!problem]
>Determine $C_*(\{*\})$ and its homology.

>[!solution]-
>Well:
> - $C_n(\{*\}) \cong \ZZ$ for $n\geq 0$ and $0$ otherwise.
> - $\pa_n = 1$ for even $n\geq 2$, and $0$ otherwise
> - Thus $B_n$ is $\ZZ$ for odd $n\geq 1$ and $0$ otherwise.
> - And $Z_n$ is $\ZZ$ for odd $n\geq 1$, $\ZZ$ for $n = 0$, and $0$ otherwise.
> - Thus $H_n$ is $\ZZ$ for $n = 0$, and $0$ otherwise.