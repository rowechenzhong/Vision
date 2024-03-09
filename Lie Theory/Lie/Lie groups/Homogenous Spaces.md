$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Suppose $G$ is a Lie group of dimension $n$, and $H\subset G$ is a closed Lie subgroup of dimension $k$. Then, the ==**homogenous space**== $G/H$ has a natural structure of an $n-k$ dimensional manifold, and the map $p:G\to G/H$ is a [[Fiber Bundle|fiber bundle]] with fiber $H$.

>[!proof]- Verification
>To verify this, well, pick any $\conj{g}\in G/H$, and I'll give you a chart. Let $g\in p^{-1}(\conj{g})$ be a representative (to prove something about a quotient, you always have to work in the ambient space). Then, $gH\subset G$ is an embedded submanifold (left translations are diffeomorphisms).
> 
> Pick a small [[transversal submanifold]] $U$ through $g$ (e.g., $U$ fits in a chart at $g$ where [[k-slicing theorem|k-slicing]] applies). Then, we claim that $UH$ is open. Indeed, for any $uh\in UH$, WLOG $h = 1$. Then one can find an open ball around $u$
> 
> If we pick $U$ to be a small open disk inside a chart at $g$, it is clear that $UH$ is an open set, thus $\conj{U}$ is open in the quotient topology. It is also clear that $p:U\to \conj{U}$ is a homeomorphism, which defines a local chart near $\conj{g}\in G/H$; such charts are easily checked to be regular.
> 
> The multiplication map $U\times H\to UH$ is a diffeomorphism, thus $p$ is a locally trivial fibration.

>[!idea]
>$G/H$ is not a group, generically; it is simply the set of left-cosets which has a natural manifold structure.

>[!theorem]
>We have a natural isomorphism $T_1(G/H)\cong T_1G / T_1H$.
> 
>If $H$ is also connected, then $p_0: \pi_0(G)\to \pi_0(G / H)$ is a bijection; this is basically clear.
>
>If $G$ is also connected, then we have a nontrivial exact sequence $\pi_1(H)\to \pi_1(G)\to \pi_1(G / H)\to 1$.
>
> If $H\trianglelefteq G$, then $G/H$ is a Lie group. 

>[!idea] Waffles
>There is a ==**long exact sequence of homotopy groups of a fibration**==



>[!proof]-
>$G/H$ is a group just because this is how groups work. Its operations are diffeomorphisms because we can compose through the fibration.
>
>$T_gG\to T_{\conj{g}} G/H$ is a surjective linear map with kernel $T_g gH$ (because $T_{\conj g} G/H$ in the above proof is isomorphic to $T_gU$). Thus, for $g = 1$ we get $T_1(G/H)\cong T_1G / T_1H$.