$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$Given two measure spaces $(S, \FFF,\mu)$,  and $(T, \GGG, \lambda)$, we will construct a product measure space $(S\times T, \FFF\otimes \GGG, \mu \otimes \lambda)$. The ==**product space**== has set $\Omega = S\times T$ . The ==**product $\sigma$-field**== is $\FFF\otimes \GGG = \sigma(S_0)$.
$$ S_0 = \{A\times B: A\in \FFF, B \in \GGG\}$$
Observe that $S_0$ is a [[semi-algebra]]. This should be reminiscent of the [[box product]] from topology; compare the following results to analogous topological results.

> [!example] Cross-sections are measurable
> Suppose $E$ is a measurable set in $S\times T$. Then for any fixed $x$, $E_x = \{y\in T: (x,y)\in E\}$ is measurable in $T$.
> ^cross-sections-measurable

>[!proof]-
> Consider all sets $E\in \FFF\otimes \GGG$ such that $E_x$ is measurable! Observe that this is a $\sigma$-algebra containing $S_0$. Thus it contains the whole thing!

By the [[Standard Measure Construction]], we need only exhibit a pre-measure on the [[semi-algebra]] $S_0$ given in the product space construction, and one is naturally handed to us.

>[!theorem] Boxes work
>The function $(\mu\otimes \lambda): S_0\to [0,\infty]$ given by
>$$ (\mu\otimes \lambda)(A\times B) = \mu(A)\times \lambda(B)$$
>is a pre-measure.

>[!proof] Boring, todo.

> [!theorem] Products are associative
> One can write $\mu_1\otimes \mu_2\otimes\cdots \mu_n$ and everything works correctly.

>[!proof]- Boring, todo.
