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
[[projections are injective homomorphisms|To each suitable class of covering spaces, there exists a corresponding class of subgroups.]] This subgroup is given precisely by $p_*(\pi_1(\tilde{X}))$. What the Galois Correspondence does is show that this correspondence is surprisingly meaningful.
- First, we will show this correspondence exists by explicitly [[constructing the galois correspondence]].
- Then, we will demonstrate a **[[basepoint-preserving isomorphism classes correspond to subgroups|bijection]]** between the set of **basepoint-preserving isomorphism classes of path-connected covering spaces** and the **subgroups of $\pi_1(X, x_0)$**. 
- Next, we will show that if one ignores the basepoints, this same correspondence gives a **[[isomorphism classes correspond to conjugacy classes|bijection]]** between **isomorphism classes of path-connected covering spaces** and **conjugacy classes of subgroups of $\pi_1(X, x_0)$**. 
- Finally, we will show that the [[galois correspondence preserves the natural poset ordering]] on subgroups and covering spaces.

# Connected Components 

So far we have mainly discussed connected covering spaces, which are nice because they correspond to *surjective* actions under $\pi_1(X,x_0)$. You can probably expect what happens in the general case; the covering space won't be a single subgroup, but a whole bunch of them acting independently. 
> [!problem] 
Suppose $p:\tilde{X}\to X$ is a covering space of an ==*unloopable*== $X$. Exhibit a bijection between the connected components of $\tilde{X}$ and the *orbits* of the action of $\pi_1(X, x_0)$ on the fiber $p^{-1}(x_0)$. Then, take any particular lift $\tilde{x}_0 \in p^{-1}(x_0)$. Let $C$ be the connected component of $\tilde{X}$ containing $\tilde{x}_0$, which is naturally a covering space of $X$. Show that under the Galois correspondence, $C$ corresponds to the *stabilizer* of $\tilde{x}_0$. 

> [!solution]-
Orbits are a partition of $p^{-1}(x_0)$. Connected components also induce a partition of $p^{-1}(x_0)$. We wish to show that these partitions are the same; $\tilde{x}, \tilde{x}'\in p^{-1}(x_0)$ are in the same connected component iff there exists a homotopy class $[\gamma]$ lifting to a path from $\tilde{x}$ to $\tilde{x}'$. Well, this is completely trivial; if there's a path from $\tilde{x}$ to $\tilde{x}'$ in $X'$ then it projects down to a path in $X$, which must lift to the original path by unique lifting. On the other hand, if there exists any path from $\tilde{x}$ to $\tilde{x}'$ they must be in the same connected component. The stabilizer of $\tilde{x}_0$ is a subgroup of $\pi_1(X, x_0)$ which fixes $\tilde{x}_0$; it contains all $[\gamma]$ which lift to a loop at $\tilde{x}_0$ in $C$. $p_* \pi_1(C, \tilde{x}_0)$ contains precisely those paths which lift to a loop at $\tilde{x}_0$. 













































