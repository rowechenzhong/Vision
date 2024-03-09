$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!theorem] Intrinsic Definition ($k$-slicing theorem)
>Let $Y$ be an $n$-dimensional manifold, and let $k$ be an integer such that $0\leq k\leq n$. A $k$-dimensional [[Embedding|embedded submanifold]] of $Y$ is a subset $X\subset Y$ such that for every point $p \in X$ there exists an [[atlas|chart]] $(U, \phi)$ such that $\phi(X\cap U)$ is the intersection of a $k$-dimensional [[plane]] with $\phi(U)$.
>
>In this case, $X$ is a manifold under the subspace topology from $Y$, and the pairs $(X\cap U, \phi_{X\cap U})$ form an atlas for the structure on $X$.

%% >[!claim] A lemma
>Suppose $X\subset Y$ is endowed with the subspace topology, and $f:X\to Z$ is a continuous map under said subspace topology. Then, $X$ is [[locally closed]].

This is actually really stupid. $f:X\to Z$ is a continuous map, thus the pre-image of $Z$, $X$ itself, must be an open set. Loading. %%

>[!claim]
> Suppose $F:X\to Y$ embeds $X$ into $Y$. Then, $X$ is open in its closure. This is called being [[locally closed]].

>[!proof]- Some cap
>For each point $x\in F(X)$, there is a neighborhood $U$ in $Y$ such that $U\cap F(X) = U\cap C$ for some closed set $C$ in $Y$.
>
>Proof: take a chart of $x$ (in $Y$!!) called $(V, \phi)$. We now consider $V\cap F(X)$; this is an open set in the $F(X)$-topology, thus it is homeomorphically mapped to an open neighborhood of $x$ in the $X$ topology. I can thus find a chart of $x$ in the $X$ topology, say $(U', \psi)$, which lies completely inside $F^{-1}(V)$. We now further assert that the closure of $U'$ (in the $X$ topology) lies completely inside $F^{-1}(V)$; this is trivial because $U'$ is homeomorphic to $\RR^n$.
> 
>Now, pushing $U'$ forward again through $F$, we find that there must exist an open set $U\in Y$ such that $U\cap F(X) = F(U')$. Pick this $U$. $\conj{F(U')} = F(\conj{U'})$ is a closed set, and clearly $U\cap \conj{F(U')} = F(U')$, because $F(U')\subset U$, $F(U')\subset \conj{F(U')}$, and $U\cap \conj{F(U')}\subset U\cap V\cap \conj{F(U')}$.

>[!todo]
>Make sure this is not cap

>[!proof]- This is what you expect.
>Suppose we start from the first definition. By identifying $X$ with $F(X)$, we find (by definition of manifold) that for every point $p\in X$, there exists a chart $(V,\psi)$; a subset $V\subset X$ which is open in $X$ homeomorphic to an open set $W\subset \RR^k$ under $\psi:V\to W$.
>
>What it means for $V$ to be open in $X$ is that $V = U'\cap X$ for some open $U'\subset Y$. Now, pick a chart $(U,\phi)$ inside $U'$ which maps to $W'\subset \RR^n$ (wlog $U = U'$). By taking $\phi\circ \psi^{-1}$ we have a regular function $\RR^k\to \RR^n$ which maps homeomorphically into its image. At $\psi(p)$, this function has some derivative which spans a subspace; use any $n-k$ linearly independent vectors which are not in this subspace to fill out the basis, such that we have a function $f:\RR^n\to \RR^n$ such that
>$$
>	f(q) = (\psi^{-1}(q)_1,\dots, \psi^{-1}(q)_k, 0, \dots, 0)
>$$
>for all $q\in \phi(V)$.
>
>For some sufficiently small open neighborhood of $\psi^{-1}(p)$, this function is invertible by construction. Then, $f\circ \phi$ is the desired chart.