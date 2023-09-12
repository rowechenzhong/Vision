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
# Normed Spaces 

Recall that a vector space is ==**finite-dimensional**== if every linearly dependent set is finite. Otherwise, it is ==**infinite-dimensional**==.

$X$ forever denotes a topological space.

Here is an example of an infinite-dimensional vector space: 

> [!definition] $C_\infty(X)$
$C_\infty(X)$ is the set of all functions $f: X \to \CC$ which are continuous and bounded. 

Functional analysis is the study of vector spaces with a topology. Infinite dimensional vector spaces are pretty hard to work in in general, because all linear algebra concepts have finite strength. Topology lets us deal with them.

> [!definition] Norm
A ==**norm**== on a vector space $V$ is a function $\norm{\bullet}: V \to \RR_{\geq 0}$ such that 
>  -  (==**Definiteness**==) $\norm{v} = 0 \iff v = 0$, 
>  -  (==**Homogeneity**==) $\norm{\lambda v} = \abs{\lambda} \norm{v}$, and 
>  -  (==**Triangle Inequality**==) $\norm{v + w} \leq \norm{v} + \norm{w}$.
>  
>  A ==**seminorm**== satisfies homogeneity and the triangle inequality, but not definiteness. A vector space endowed with a norm is called a ==**normed vector space**==. 

This norm induces a metric on $V$ by $d(v, w) = \norm{v - w}$. 

> [!problem] Bruh
Show that this is a metric (symmetric, positive definite, triangle inequality). 

$V, W$ forever denote normed vector spaces over $\RR$ or $\CC$.

> [!idea] 
The second condition doesn't have to be satisfied by any old metric; its the source of linearity.

>[!problem]
>Show norms are continuous and commute with limits.

> [!problem] Scaling works
Show that scaling by a nonzero constant is a homeomorphism. 

So we'll end up writing "WLOG by scaling" a lot.

> [!problem] Sums of Closures
Let $A,B\subset V$ be arbitrary sets. Let $\overline{A}$ and $\overline{B}$ denote their closures, as usual. Show that $\overline{A} + \overline{B}\subseteq \overline{A + B}$. 

> [!solution] 
Recall that in metric spaces, the closure of a set is the set of all limits of convergent sequences in the set. Well, take any convergent sequence $\{a_n\}\to a$ in $A$ and any convergent sequence $\{b_n\}\to b$ in $B$. Then, $\{a_n + b_n\}$ converges to $a + b$ in $A + B$. 


# Major Examples

See the
- [[infinity norm]]
- [[Minkowski norm]], extending the [[Euclidean norm]].

Now that we have our first example, update your intuition: anything that relies on counting the elements of your basis probably fails.