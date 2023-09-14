$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$> [!definition] Pre-Measure
> A [[pre-measure]] on an [[measurable space#^algebra|algebra]] or [[semi-algebra]] $\AAA_0$ is a function $\mu_0: \AAA_0 \to [0,\infty]$ such that $\mu_0(\emptyset) = 0$ and $\mu_0$ is countably additive -- if $A_1,\cdots \in \AAA_0$ are disjoint, and $\bigsqcup A_i \in \AAA_0$, then
>
> $$
>  \mu_0\left(\bigsqcup A_i\right) = \sum \mu_0(A_i).
> $$

One way to create a pre-measure is the [[semialgebra extension]].

> [!example] Premeasure bootstrapping
> Suppose $\mu:\AAA_0 \to [0,\infty)$ is a function which is **finitely** additive. If for any sequence $B_n\in \AAA_0$ with $B_n\downarrow \emptyset$, we have $\mu(B_n)\downarrow 0$, then $\mu$ is also countably additive (and is thus a pre-measure).

> [!proof] Boring todo

