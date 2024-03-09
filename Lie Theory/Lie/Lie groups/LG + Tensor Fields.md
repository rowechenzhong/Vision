$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
If a Lie group $G$ [[LG + Actions|acts on]] a manifold $X$, then it also acts on the tangent bundle $TX$! Indeed, for all $g\in G$, $p\in X$, $v\in T_pX$, send

$$
g((p, v)) = (gp, d_pg(v))
$$

where $d_pg$ is the [[Differential]] of $g$ at $p$ as usual. This extends to [[Tensor Fields]] as you would expect.

In particular $G$ acts on tensor fields _on itself_ via left and right translations; these actions are denoted $L_g$ and $R_g$ as usual. We say that a tensor field on $G$ is ==**left invariant**== if $L_gT = T$ for all $g\in G$, and ==**right invariant**== if $R_gT = T$ for all $g\in g$.

> [!idea]
> Actions by things in $g$ will slide the contents of our tensor bundle around; a left-invariant vector field (if one exists) is obtained by taking a vector and "spreading it around" $G$. This is completely trivial, actually, let's make this a theorem.

> [!theorem] Spread a vector like peanut butter
> For any $\tau\in \fg^k\otimes \fg^{*\otimes m}$, there exists a unique left-invariant tensor field $L_\tau$ whose value at $1$ is $\tau$. Thus, the space of such tensor fields is naturally isomorphic to $\fg^k\otimes \fg^{*\otimes m}$. Ditto for right actions.
>
> In particular, all Lie groups are [[frame|parallelizable]].

^b9afb7

This is blithingly obvious. After you have see the [[Various Adjoint maps]]:

> [!problem]
>$L_\tau$ is also right invariant iff $R_\tau$ is also left invariant iff $\tau$ is invariant under the [[Various Adjoint maps|adjoint representation]] $Ad_g$.

> [!solution]-
> Consider $L_\tau$. A right action by $g$ slides $(1,\tau)$ to $(g, (d_1R_g)\tau$. This is in $L_\tau$ iff
>
> $$
> 	(d_1R_g)\tau = (d_1L_g)\tau
> $$
>
> i.e. $\tau$ is invariant under the adjoint representation.