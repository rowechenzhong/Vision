$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
> [!definition] Measurable Function
> Let $(X, \AAA)$ and $(Y, \BBB)$ be measurable spaces. A function $f: X \to Y$ is ==**measurable**== if for every $B \in \BBB$, we have $f^{-1}(B) \in \AAA$.

If one is interested in [[real-valued measurable functions]], there is more intuition to be found.

> [!claim] Only need to check the generators.
> A function $(X,\AAA)\to (Y,\sigma(\BBB_0))$ is measurable iff for all $B\in \BBB_0$, $f^{-1}(B)\in \AAA$.

> [!idea]
> In topology, we only need to check the pre-images of a sub-basis to determine continuity. This is analogous.

> [!idea]
> Pre-images respect set operations. Given some function $f:A\to B$, where $A$ has a sigma-algebra, the collection of $F\subset B$ such that $f^{-1}(F)$ is measurable forms a sigma-algebra.

> [!proof]-
> In particular, the collection of $B\subset Y$ such that $f^{-1}(B)$ is measurable forms a $\sigma$-algebra; this fills all of $\sigma(\BBB_0)$.

For example, one needs only verify that the pre-image of $(a, \infty)$ is measurable when working with $(X,\AAA)\to \RR$.

> [!example]
> In particular, assuming we pick the Borel measure on two topological spaces $X$ and $Y$, continuous functions are measurable.
> 
> A (real-valued) measurable function *from* a Borel space is a ==**Borel function**== (so we point from $(E, \BBB(E))\to (\RR, \BBB)$).


Suggested reading:
- [[Measurable functions generate sigma algebras]].
- [[pushforward measure|Measurable functions induce measures]].
- [[Canonical equivalence classes of Measurable functions]]