
> [!theorem] Lifting Property
 Suppose you are given a map $F:Y\times I \to X$. I give you a a branch-cut / \"initial condition\" $\tilde{F}: Y\times \{0\} \to \tilde{X}$, which is a lift of $F$ over $Y\times \{0\}$. Then $\tilde{F}$ can be extended to a unique lift $\tilde{F}: Y\times I \to \tilde{X}$. 
 
> [!proof]-
> Fix $y_0$. For all $t\in I$, by definition of covering space, there exists an evenly-covered open neighborhood of $F(y,t)$; by the product topology, we can take it to be of the form $U\times (a,b)$. Now, $\{y_0\} \times I$ is compact. Thus, there exists a neighborhood $y_0\subset N$ and a finite partition $0 = t_0 < t_1 < \cdots < t_m = 1$ of $I$ such that for each $i$, $F(N\times [t_i, t_{i+1}])$ is contained in some evenly-covered neighborhood. Each one of these $m$ blocks is homeomorphically mapped via $p^{-1}$, with branch cut given inductively. This construction uniquely determines $\tilde{F}(N\times I)$, by inspection. Repeat for all $y_0\in Y$. By uniqueness of the previous construction, all such $\tilde{F}(N\times I)$ agree on their overlaps. Thus we conclude. 

This generalizes to the [[lifting criterion]] and [[unique lifting]] property. 
> [!example] Lifting a Path
 Suppose $Y$ is a point. Then, the statement is: for any path $f: I\to X$ starting at $x_0$, and any selection of $\tilde{x}_0\in p^{-1}(x_0)$, there exists a unique lift $\tilde{f}: I\to \tilde{X}$ starting at $\tilde{x}_0$. 

 
> [!example] Lifting a Homotopy
 For any homotopy $f_t: I\to X$ of paths starting at $x_0$, and each $\tilde{x}_0\in p^{-1}(x_0)$, there exists a unique lifted homotopy $\tilde{f}_t: I\to \tilde{X}$ starting at $\tilde{x}_0$. This is true, because we can write $F(x,t) = f_t(x)$. Then, $F(x,0)$ can be uniquely lifted by the previous theorem. We apply this theorem a second time to lift $F(x,t)$ to $\tilde{F}(x,t)$. To verify that $\tilde{F}(0,t)$ and $\tilde{F}(1,t)$ are constant (as required for path homotopies), we note that $F(0,t)$ and $F(1,t)$ are constant, and thus their lifts are constant. 

 
> [!example] Circle
 Okay, let $f:I\to S^1$ be any loop from basepoint $x_0 = 1$. Then, $f$ lifts to a path $\tilde{f}: I\to \RR$ starting at $0$. $f(1) = 1\in S^1$, thus $\tilde{f}(1) = n$ for some $n\in \ZZ$. Well, I can write down a different path that looks the same: let $\omega_n:I\to S^1$ via $\omega_n(t) = e^{2\pi i n t}$. Then $\tilde{\omega}_n(t) = nt$. $\RR$ is simply connected, so $\tilde{f}$ and $\tilde{\omega}_n$ are homotopic. Dropping through $p$ gives us a homotopy between $f$ and $\omega_n$. Finally, we need to show that $\omega_1 \neq \omega_0$. But if they were, then we could lift a homotopy between them, which is absurd, because they don't even have the same endpoints in $\RR$. Thus: each loop in $S^1$ is homotopic to a unique $\omega_n$; this $\omega_n$ compose homomorphically to $\ZZ$, so $\pi_1(S^1) = \ZZ$. 

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
