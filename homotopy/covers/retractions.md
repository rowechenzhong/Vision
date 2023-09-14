$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$
Retractions are the topological analogues of projection operators in linear algebra. 
> [!definition] Retraction
> A ==**retraction**== of a space $X$ onto a subspace $A\subset X$ is a continuous map $r:X\to X$ such that $r(X) = A$ and $r|_A = \id_A$. Equivalently, $r^2 = r$. 

> [!problem] Retractions are lame
 This is not a very strong condition; all spaces retract to points. 
 
> [!definition] Deformation Retraction
> Let $A\subset X$ be a subspace. If a retraction $r:X\to X$ is homotopic to the identity map $\id_X$, then we say $A$ is a ==**deformation retraction**== of $X$. 
 
> [!problem] Spinning Definitions
 Show that $X$ deformation retracts to $A$, then the inclusion $i: A\to X$ is a [[homotopy type|homotopy equivalence]].

> [!solution]-
 If $X$ deformation retracts to $A$, then the retraction $r:X\to X$ is a homotopic to $\id_X$. Let $r' : X\to A$ be $r$ but with the correct range. Then, $ir'\simeq \id_X$, and $r'i = \id_A$, as desired. 
