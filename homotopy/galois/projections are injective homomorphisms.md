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
The fact that covering maps induce subgroups of the [[fundamental group]] is what motivates the entire study of the [[galois correspondence]].
> [!theorem] Projections are injective homomorphisms
Let $p: \tilde{X}\to X$ be a covering map. Then, $p_*: \pi_1(\tilde{X}, \tilde{x}_0)\to \pi_1(X, x_0)$ is injective. Furthermore, the image subgroup consists of exactly those homotopy classes of loops in $X$ whose lifts remain loops. 

> [!proof]-
> Our primary tool will be the [[lifting property]]. 
 This is trivial, so we'll write out all the details. We must analyze the kernel of $p_*$. Pick some loop $\gamma$ at $\tilde{x}_0$ in $\tilde{X}$ for which $[\gamma]$ gets mapped to the trivial loop in $X$. In other words, $p\circ \gamma$ is a loop in $X$ at $x_0$, which is homotopic to the trivial loop. By the lifting property, this *uniquely* lifts to a homotopy in $\tilde{X}$. $p\circ \gamma$ lifts to $\gamma$ itself. The trivial loop is stationary at $x_0$, so it lifts to a constant loop at $\tilde{x}_0$. Thus, $\gamma$ is homotopic to the constant loop at $\tilde{x}_0$. Next up: suppose $\gamma$ is a loop in $X$ whose lift remains a loop. This implies that *all* of $[\gamma]$ lifts to loops, via the lifting property. Then clearly all of $[\gamma]$ is part of the image of $p_*$; each loop is the image of its lift. On the other hand, if $\gamma$ is in a homotopy class of loops in the image of $p_*$, then at least some element of this class had a lift, so the whole class has a lift by the lifting property. 

> [!idea] 
 This might feel kind of strange. A projection sends $X$ to $\tilde{X}$, which is ostensibly \"larger\" to $X$. We just showed that $p_*$ was injective, meaning that $\pi_1(\tilde{X})$ is a subgroup of $\pi_1(X)$. These actually don't contradict each other, because our groups will feel very \"free,\" and free groups behave strangely. 
