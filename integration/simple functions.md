$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$> [!definition] Simple Functions
> A function $f: \Omega \to \RR$ is ==**simple**== if it can be written
> $$ f = \sum_{i=1}^n c_i \id_{A_i} $$
> where $c_i \in \RR$ and $A_i$ are disjoint *measurable sets*.

Simple functions are obviously [[real-valued measurable functions]].

> [!problem] Verification
> Simple functions are closed under addition, products, and scalar multiplication.

> [!solution]-
> Let $f = \sum_{i=1}^n c_i \id_{A_i}$ and $g = \sum_{j=1}^m d_j \id_{B_j}$ be simple functions.
>
> - $$f+g = \sum_{i=1}^n \sum_{j=1}^m (c_i + d_j) \id_{A_i \cap B_j}.$$
> - $$fg = \sum_{i=1}^n \sum_{j=1}^m c_i d_j \id_{A_i \cap B_j}.$$
> - $$cf = \sum_{i=1}^n c c_i \id_{A_i}.$$
>
> These point to a common trick: when we a set is cut up into a finite/countable number of pieces in two different ways, one simply considers the finite/countable pieces of the form $A_i \cap B_j$.