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

% Operators
\newcommand{\xx}{\hat{x}}
\newcommand{\pp}{\hat{p}}
\newcommand{\ee}{\hat{E}}
\renewcommand{\aa}{\hat{a}} % aa makes an a with a dot on top.
\newcommand{\bb}{\hat{b}}
\renewcommand{\AA}{\hat{a}}
\newcommand{\BB}{\hat{B}}

\newcommand{\ad}{\hat{a}^\dagger}

% Woah, relativity
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

% Measure Theory
\newcommand{\AAA}{\mathscr{A}}
\newcommand{\BBB}{\mathscr{B}}
\newcommand{\FFF}{\mathscr{F}}
\newcommand{\GGG}{\mathscr{G}}
\newcommand{\HHH}{\mathscr{H}}

\DeclareMathOperator{\ess}{ess}

% A bunch of sets
\newcommand{\CC}{\mathbb C}
\newcommand{\FF}{\mathbb F}
\newcommand{\NN}{\mathbb N}
\newcommand{\QQ}{\mathbb Q}
\newcommand{\RR}{\mathbb R}
\newcommand{\ZZ}{\mathbb Z}
\newcommand{\SSS}{\mathbb S}
\newcommand{\II}{\mathbb I}

% Complex Bashing
\newcommand{\conj}[1]{\overline{#1}}
\DeclareMathOperator{\cis}{cis}


% A bunch of geometry
\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\newcommand{\dang}{\measuredangle} %% Directed angle
\newcommand{\ray}[1]{\overrightarrow{#1}}
\newcommand{\seg}[1]{\overline{#1}}
\newcommand{\arc}[1]{\wideparen{#1}}
\newcommand{\pow}{\text{pow}} %% Power

% Things about NT
\newcommand{\jacobi}[2] {\genfrac{(}{)}{1.5pt}{}{\,#1\,}{#2}}
\DeclareMathOperator*{\lcm}{lcm}
\DeclareMathOperator*{\ord}{ord}

\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}


% Linalg
\DeclareMathOperator*{\range}{range}
\DeclareMathOperator*{\nul}{null}
\DeclareMathOperator*{\Tr}{Tr}
\newcommand{\id}{1\!\!1}

% Other physics things
\newcommand{\der}{\ \mathrm {d}}

\newcommand{\ihat}{\boldsymbol{\hat{\textbf{\i}}}}
\newcommand{\jhat}{\boldsymbol{\hat{\textbf{\j}}}}
\newcommand{\khat}{\boldsymbol{\hat{\textbf{k}}}}
\newcommand{\rhat}{\boldsymbol{\hat{\textbf{r}}}}
\newcommand{\that}{\boldsymbol{\hat{\mathbf{\theta}}}}



% Lol, some groups
\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}
\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}

\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\End}{End}
\newcommand{\GL}{\mathbb{GL}}
\newcommand{\SL}{\mathbb{SL}}
$$
