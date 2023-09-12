$$
\require{physics}

% Misc
\newcommand{\cbrt}[1]{\sqrt[3]{#1}}
\newcommand{\sgn}{\text{sgn}}
\newcommand{\ii}[1]{\textit{#1}}
\newcommand{\eps}{\varepsilon}

% Expected Value
\newcommand{\EE}{\mathbb E}
\newcommand{\PP}{\mathbb P}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}

\newcommand{\pperp}{\perp\kern-6pt\perp}

% Lol relativity
\newcommand{\LL}{\mathcal{L}}
\newcommand{\pa}{\partial}

% Inequalities
\newcommand{\cyc}{\sum\limits_{\mathrm{cyc}}}
\newcommand{\sym}{\sum\limits_{\mathrm{sym}}}
\newcommand{\cycprod}{\prod_{\mathrm{cyc}}}
\newcommand{\symprod}{\prod_{\mathrm{sym}}}

\newcommand{\eq}[1]{\stackrel{#1}{=}}
\newcommand{\rgeq}[1]{\stackrel{#1}{\geq}}
\newcommand{\rleq}[1]{\stackrel{#1}{\leq}}

% Sets
\newcommand{\CC}{\mathbb C}
\newcommand{\FF}{\mathbb F}
\newcommand{\NN}{\mathbb N}
\newcommand{\QQ}{\mathbb Q}
\newcommand{\RR}{\mathbb R}
\newcommand{\ZZ}{\mathbb Z}
\newcommand{\SSS}{\mathbb S}
\newcommand{\II}{\mathbb I}

% Geometry
\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\newcommand{\dang}{\measuredangle} %% Directed angle
\newcommand{\ray}[1]{\overrightarrow{#1}}
\newcommand{\seg}[1]{\overline{#1}}
\newcommand{\arc}[1]{\wideparen{#1}}
\newcommand{\pow}{\text{pow}} %% Power


% Complex Bashing
\newcommand{\conj}[1]{\overline{#1}}
\DeclareMathOperator{\cis}{cis}

% NT
\newcommand{\jacobi}[2] {\genfrac{(}{)}{1.5pt}{}{\,#1\,}{#2}}
\DeclareMathOperator*{\lcm}{lcm}
\DeclareMathOperator*{\ord}{ord}

\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Derivative
\newcommand{\der}{\ \mathrm {d}}

% Unit Vectors
\newcommand{\ihat}{\boldsymbol{\hat{\textbf{\i}}}}
\newcommand{\jhat}{\boldsymbol{\hat{\textbf{\j}}}}
\newcommand{\khat}{\boldsymbol{\hat{\textbf{k}}}}
\newcommand{\rhat}{\boldsymbol{\hat{\textbf{r}}}}
\newcommand{\that}{\boldsymbol{\hat{\mathbf{\theta}}}}

% Operators
\newcommand{\xx}{\hat{x}}
\newcommand{\pp}{\hat{p}}
\newcommand{\ee}{\hat{E}}
\renewcommand{\aa}{\hat{a}} % aa makes an a with a dot on top.
\newcommand{\bb}{\hat{b}}
\renewcommand{\AA}{\hat{a}}
\newcommand{\BB}{\hat{B}}

\newcommand{\ad}{\hat{a}^\dagger}

% Groups
\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}
\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}

% Linalg
\DeclareMathOperator*{\range}{range}
\DeclareMathOperator*{\nul}{null}
\DeclareMathOperator*{\Tr}{Tr}

% Homomorphism
\DeclareMathOperator{\Hom}{Hom}
% Endomorphism
\DeclareMathOperator{\End}{End}

\newcommand{\id}{1\!\!1}

\newcommand{\GL}{\mathbb{GL}}
\newcommand{\SL}{\mathbb{SL}}

% Measure Theory
\newcommand{\AAA}{\mathscr{A}}
\newcommand{\BBB}{\mathscr{B}}
\newcommand{\FFF}{\mathscr{F}}
\newcommand{\GGG}{\mathscr{G}}
\newcommand{\HHH}{\mathscr{H}}

\DeclareMathOperator{\ess}{ess}
$$

Here are some basic point-set calculations to familiarize yourself with the topology of [[covering spaces|covering spaces]], before we dive into the algebra side of things. More advanced results are linked.

> [!example] Restriction
 Suppose $p:\tilde{X} \to X$ is a covering space and let $A\subset X$ be a subspace. Then $\tilde{A} = p^{-1}(A)$ is a covering space via the restriction $p|_{\tilde{A}}$. 

 This is clear; for any $a\in A$, pick an evenly covered $U\subset X$ in $X$. Then, $U\cap A$ will be evenly covered in $A$. 
 
> [!example] Products of Covering Spaces
 Suppose $p_x: \tilde{X}\to X$ and $p_y : \tilde{Y}\to Y$ are covering spaces. Then $\tilde{X}\times \tilde{Y}$ is a covering space of $X\times Y$ via the map $p_x\times p_y: \tilde{X}\times \tilde{Y}\to X\times Y$. 

 This is also clear; for any $(x,y)\in X\times Y$, pick evenly covered neighborhoods $U\subset X$ and $V\subset Y$. Then, $U\times V$ is evenly covered in $X\times Y$. 
 
> [!example] Hausdorff
 A *small covering space* $p : \tilde{X}\to X$ is a covering space such that $0 < \abs{p^{-1}(x)} < \infty$ for all $x$. In small covering spaces, $X$ is Hausdorff iff $\tilde{X}$ is Hausdorff. 

> [!proof]-
 Given $X$ is Hausdorff: pick $a,b\in \tilde{X}$. If $a$ and $b$ lie in the same fiber, then they are clearly separated by disjoint open sets. Otherwise, project to $p(a)$ and $p(b)$, find separated neighborhoods $A$ and $B$, take the union with suitable evenly covered neighborhoods, and project back. Given $\tilde{X}$ is Hausdorff: pick $a,b\in X$ with evenly-covered neighborhoods $U$ and $V$. Then, consider their fibers $p^{-1}(a)$ and $p^{-1}(b)$; these are finite sets. For each pair of elements in $(\tilde{a}_i, \tilde{b}_j) \in p^{-1}(a)\times p^{-1}(b)$, one can pick separated open neighborhoods of $\tilde{a}$ and $\tilde{b}$ called $\tilde{U}_{i,j} \subset \tilde{U}_i$ and $\tilde{V}_{i,j} \subset \tilde{V}_j$ respectively. Take the union of all $p\left(\tilde{U}_{i,j}\right)$, which remains an open set, and call it $U'$; ditto for $V'$. Then $U'$ and $V'$ are the disjoint open separating sets as desired. 

There is a similar result on [[compact covering spaces|compactness]].

A very important example that deserves its own page is the [[chaining covering spaces|chaining of covering spaces]].
