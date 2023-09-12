 Van Kampen's theorem computes the [[fundamental group|fundamental group]] of the union of two spaces.
 
  Let's set up the notation. \todo{draw a diagram lol} 
 -  $X$ is a union of path-connected open subsets $A_\alpha$ for $\alpha \in \mathcal{A}$, such that each $A_\alpha$ contains basepoint $x_0$. We drop references to this basepoint from now on. 
 -  Let $$ F = \underset{\alpha\in\mathcal{A}}\ast \pi_1(A_\alpha) $$ be the free group. 
 For every $U, V, W \in \mathcal{A}$: 
 -  $U\cap V\cap W$ is path-connected. 
 -  There exists natural homomorphisms $$ i_U: \pi_1(U\cap V) \stackrel{i_U}{\to} \pi_1(U) \stackrel{k_U}{\to} \pi_1(X) $$ via topological inclusion. 
 -  There exists natural inclusion homomorphism $$ j_U: \pi_1(U)\to F. $$
 By the universal property of the free group, there exists a natural homomorphism $$ \Phi:F\to \pi_1(X) $$ compatible with each $k_U$. 
 
> [!theorem] Van Kampen's Theorem
> $\Phi$ is surjective. Let $N$ be the smallest normal subgroup containing $$ \left(j_U\circ i_U(\gamma)\right) \left( j_V \circ i_V(\gamma) \right)^{-1} $$ for all $\gamma\in \pi_1(U\cap V)$ for all $U,V \in \mathcal{A}$. Then $\ker \Phi = N$. 

 In a sense, this should be obscenely obvious. If I start from $x_0$, what can I do? I can walk around inside $U$ until I get back to $U\cap V$, or walk around inside $V$ until I get back to $U\cap V$, and eventually I execute some arbitrary string of elements in $U$ and $V$ and wind up back at $x_0$. Obviously I shouldn't double-count nontrivial loops inside $U\cap V$, so I need to mod out by all of those. 
 
> [!proof]- Proof $\Phi$ is surjective
 You literally do what I just said. Pick any loop $\gamma:I\to X$. Then, the preimage of $U$ on $I$ is a collection of open sets. By the definition of a basis, we can split each open set into a union of open intervals. The interval is compact, thus we can extract a finite subcover $(a_i, b_i)$ ordered by increasing $a_i$. WLOG no interval contains another, and WLOG no two adjacent intervals are members of the same open set $U$ or $V$. Let $s_0 = [0, \frac{a}]$, $s_i = \frac{a_i + b_{i-1}}{2}$ for $i = 1, 2, \cdots, n$, and $s_{n+1} = 1$. By construction, each $\gamma([s_i, s_{i+1}])$ lies entirely inside either $U$ or $V$, and each $\gamma(s_i)$ lies inside $U\cap V$. By hypothesis, we can also connect each $\gamma(s_i)$ to $x_0$ by a path in $U\cap V$, $\beta_i$. Thus, the entire $\gamma$ is a concatenation of loops inside $U$ or $V$: $$ \gamma = \gamma([s_0, s_1])\beta_1^{-1}\quad \beta_1^1 \gamma([s_1, s_2])\beta_2^{-1}\quad \cdots \quad \beta_n^1 \gamma([s_n, s_{n+1}]) $$ 
  
> [!proof]- Proof $N\subset \ker \Phi$
 This is basically tautological. For any path $\gamma$ inside $U\cap V$, the inclusions $j_U\cap i_U$ and $j_V\cap i_V$ map $\gamma$ to the exact same loop inside $X$. So of course this is an element of the kernel. 

 I will return to show the hard part of this proof someday, maybe, if I ever have the time.
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
