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
We're trying to upgrade to [[Integration]], so from now on most of our [[measurable functions]] will point into the reals, extended reals, or the [[complex-valued measurable functions|complex numbers]]. On the other hand, the domain is pretty unimportant; $\Omega$ is some arbitrary [[measure space]]. 

The set of all measurable functions from $\Omega$ to $\RR_{\geq 0}$ is sometimes denoted $L^+(\Omega)$. Obligatory results, left as an exercise.

> [!theorem] Making Measurable Functions
> 1. Given $f,g: \Omega \to \RR$ are measurable functions and $c \in \RR$, then $cf, f + g, fg$ are all measurable.
> 2. Let $f_n: \Omega \to \RR$ be a sequence of measurable functions. Then the pointwise supremum and infimum are measurable.
> 	1. Consequently,
>    $$
>    \lim \sup_{n\to \infty} f_n(x) = \inf_{n\geq 1} \sup_{k\geq n} f_k(x)
>    $$
>    and $\lim \inf$ are also measurable.
> 	2. Most importantly, if these coincide, that is, if the functions converge pointwise, then the limit is measurable; this extends to the complex case as well
> 3. Suppose $\Omega$ is a [[complete measure space]]. If $f,g: \Omega\to [-\infty, \infty]$ agree almost everywhere, then they are both measurable or both not measurable.

> [!solution]- Part 1
> 1. First, we show $(cf)^{-1}((a,\infty))$ is measurable for all $a\in \RR$. Since $f$ is measurable, $f^{-1}((a/c,\infty))$ is measurable. Therefore, $(cf)^{-1}((a,\infty)) = f^{-1}((a/c,\infty))$ is measurable.
> 2. Next, let's show that $(f+g)^{-1}((a,\infty))$ is measurable for all $a\in \RR$. Since $f,g$ are measurable, $f^{-1}((q,\infty))$ and $g^{-1}((a - q,\infty))$ are both measurable for all $q\in \QQ$. Now, observe that
> $$(f+g)^{-1}((a,\infty)) = \bigcup_{q\in \QQ} \left( f^{-1}((q,\infty)) \cap g^{-1}((a - q,\infty)) \right)$$
> because if $f(\omega) + g(\omega) > a$, there exists a rational $q$ such that $f(\omega) > q$ and $g(\omega) > a - q$. Since unions of measurable sets are measurable, we conclude that $(f+g)^{-1}((a,\infty))$ is measurable.
> 3. Finally, let's show $(fg)^{-1}((a,\infty))$ is measurable for all $a\in \RR$. Assume first that $a > 0$. Note that
> $$ (fg)^{-1}((a,\infty)) = \bigcup_{q > 0, q \in \QQ} \left( f^{-1}((q,\infty)) \cap g^{-1}((a/q,\infty)) \right) \cup \left( f^{-1}((-\infty, -q)) \cap g^{-1}((-\infty, -a/q)) \right) $$
> This also yields $a = 0$ by countable unions. If $a < 0$, then
> $$ (fg)^{-1}((a,\infty)) = \bigcup_{q > 0, q \in \QQ} \left( f^{-1}((-q, \infty)) \cap g^{-1}((a/q,\infty)) \right) \cup \left( f^{-1}((q,\infty)) \cap g^{-1}((-a/q, \infty)) \right) $$

> [!solution]- Part 2
> We first consider the pointwise supremum. Let $f_n: \Omega \to \RR$ be a sequence of measurable functions. Then, as sets,
> $$ \left\{ x \in \Omega \mid \sup_{n\geq 1} f_n(x) > a \right\} = \bigcup_{n\geq 1} \left\{ x \in \Omega \mid f_n(x) > a \right\} $$
> Since each $f_n$ is measurable, each set in the union is measurable, and thus the union is measurable. Therefore, the supremum is measurable. The infimum is similar (use $(-\infty, a)$ in the definition of measurability).

> [!solution]- Part 3
> Suppose $f$ is measurable. Then $\mu\left(f^{-1}((a,\infty)) \Delta g^{-1}((a,\infty))\right) = 0$ for all $a\in \RR$ (because the set in question is a subset of the set $\{x: f(x)\neq g(x)\}$, which has outer measure zero, and thus has measure $0$). Since $f$ is measurable, $g$ is measurable as well. (All sets with outer measure $0$ are measurable). The converse is similar.

The characterization that is most amenable to verifying implementation details is the following.

> [!theorem] Approximation by Simple Functions
> $f:\Omega \to \RR$ is measurable iff there exists a sequence of [[simple functions]] $f_n$ such that $f_n \to f$ pointwise. If $f\geq 0$, one can choose these $f_n$ such that $f_n\uparrow f$; otherwise one can still ensure $\abs{f_n}\uparrow \abs{f}$.
> ^sf-approx

> [!proof]- Forward
> Suppose $f$ is measurable. Then $f^{-1}((a,\infty))$ is measurable for all $a\in \RR$. We use the density of rationals in reals to construct a sequence of simple functions that converge to $f$ pointwise. Let
> $$
> A_{n,k} = f^{-1}\left(\left( \frac{k}{2^n}, \frac{k+1}{2^n} \right]\right).
> $$
> Then $A_{n,k}$ are disjoint and measurable. Define the simple functions
> $$
> f_n = \sum_{\abs{k} \leq n\cdot 2^n} \frac{k}{2^n} \id_{A_{n,k}}.
> $$
> (The ugly summation range ensures that each $f_n$ is a finite sum, but in the limit we can access all of $\RR$).
>
> Fix $x\in \Omega$. By construction, for all $n > f(x)$, $0 < f(x) - f_n(x) < 2^{-n}$. Thus $f_n(x) \to f(x)$ pointwise. If you want $f_n\uparrow f$, truncate the beginning; if you're in the general case, do casework on signage of $f$.

> [!proof]- Backwards
> On the other hand, suppose $f_n \to f$ pointwise.
> 1. Then, for any $x \in f^{-1}((a,\infty))$, there exists an $M$ such that $x\in f^{-1}_n((a,\infty))$ for all $n > M$.
> 2. Then $f^{-1}_n((a,\infty)) \to f^{-1}((a,\infty))$ as sets.
> 3. In particular, 
> $$ B_m = \bigcup_{n\geq M} f_n^{-1}((a,\infty)) $$
> are a sequence of measurable set, thus
> $$ f^{-1}((a,\infty)) = \bigcap_{m\geq 0} B_m $$
> is measurable.
