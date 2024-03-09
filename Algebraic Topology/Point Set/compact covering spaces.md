$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Here is another [[point-set results on covering spaces|point-set]] result.
> [!example] Compactness
 In small covering spaces, $X$ is compact iff $\tilde{X}$ is compact. 
 
> [!proof] 
 Given $X$ is compact: Let $\{\tilde{U}_\alpha\}$ be an open cover of $\tilde{X}$. Pick any $x\in X$, and an evenly-covered neighborhood $V$ of $x$. Then, $p^{-1}(V)$ is a disjoint union of open sets $\{\tilde{V}_i\}_{i\leq n}$ containing the fiber $p^{-1}(x) = \{\tilde{x}_i\}_{i\leq n}$, respectively. Now, $\{\tilde{U}_\alpha\}$ was an open cover. Thus, for each element of the fiber $p^{-1}(x)$, I can find an open set $\tilde{U}_i$ containing $\tilde{x}_i$. Let $\tilde{K}_i = \tilde{U}_i\cap \tilde{V}_i$, which is an open neighborhood of $\tilde{x}_i$ which is now inside $\tilde{U}_i$. As a covering space, I know that $\tilde{U}_i$ is mapped homeomorphically to $U$ by $p$. Thus, $\tilde{K}_i$ is mapped homeomorphically to some open set $K_i$ in $U\subset X$. Finally, let $K = \cap K_i$. 
>  
>  
>  
>  -  $x\in K$ is a neighborhood. 
>  
>  -  $K$ is evenly covered. 
>  
>  -  The pre-image of $K$ is a finite union of $\tilde{K}_i$'s, each of which is a subset of some $\tilde{U}_\alpha$. 
>  
>  Perfect! Construct such a $K$ for each $x\in X$, and extract a finite subcover. This lifts to a finite subcover consisting of a finite number of $\tilde{K}_i$'s, each of which can be expanded to some $\tilde{U}_\alpha$. 
> 
> 
>  Given $\tilde{X}$ is compact: observe that the continuous image of a compact set is compact. 

> [!idea] 
> A covering space is called *proper* if the pre-image of any compact set is compact. Any proper space must be small, thus our argument shows that the proper spaces are precisely the small covering spaces.
>