$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$Here's a pretty legendary extension of Lebesgue measure. 
> [!definition] Topological Group
A ==**topological group**== is a group $G$ with a topology such that 
> -  Multiplication $G\times G\to G$ is continuous. 
> -  Inversion $G\to G$ is continuous. 

 
> [!definition] LCA Group
 A ==**locally compact abelian group**== is an abelian topological group $G$ which is locally compact. 

 Lol. Anyways: 
> [!definition] Haar Measure
 Let $G$ be a locally compact abelian group. A ==**Haar measure**== on $\BBB(G)$ is a measure $\mu$ that is: 
> -  ==**Group invariant:**== $\mu(gA) = \mu(A)$ for all $g\in G$ and $A\in \BBB(G)$. 
> -  $\mu(K) < \infty$ for any compact $k\in \BBB(G)$. 
> -  If $S$ is measurable, then $\mu(S) = \inf \mu(U)$ where $U$ is open and $S\subset U$. 
> -  If $U$ is open, then $\mu(U) = \sup \mu(S)$ where $S$ is compact and $S\subset U$. 

 In fact, this measure is *unique* up to scaling. This is fucking overpowered.