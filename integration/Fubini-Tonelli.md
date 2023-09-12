> [!theorem] Fubini-Tonelli
> Let $(S, \GGG, \lambda)$ and $(T, \HHH, \rho)$ be finite measure spaces, and define $(\Omega, \FFF, \mu) = (S\times T, \GGG \otimes \HHH, \lambda \times \rho)$. Let $f:(\Omega, \FFF)\to \RR$ be measurable. If $f\geq 0$ (**Fubini**) or $f$ is integrable (**Tonelli**), then
> $$ \int_S \int_T f(x,y) \der \rho(y) \der \lambda(x) = \int_\Omega f\der \mu = \int_T \int_S f(x,y) \der \lambda(x) \der \rho(y).$$

Actually, there's an implicit claim here; if $f(x,y): \Omega\to \RR$ is integrable, then the following are also integrable:
- for all $x\in S$, $f(x,\bullet):T\to \RR$.
- $\int_S f(x, y) \der\lambda(x): T\to \RR$.

Anyways, we follow the [[measure theory function scaffold|standard scaffold]].

> [!part]- Indicator functions
> Multiple steps! First, consider when $f(x,y) = \id_{X\times Y}$ where $X,Y$ are measurable. In this case, the conclusion is clear. Next up, by [[box product measure#^cross-sections-measurable|cross section lemma,]] we know that for all $F\in \FFF$, $F_x = \{y\in T: (x,y)\in F\}$ is measurable in $T$. We essentially repeat the same trick: let $\FFF_0$ be the set of all $F\in \FFF$ such that $\rho(F_x)$ is measurable and
> $$\int_S \rho(F_x) d\lambda(x) = \mu(F).$$
> Note that the $\pi$-algebra of rectangles lie in $\FFF_0$. $\FFF_0$ forms a $\lambda$-algebra, because
> - $\Omega\in \FFF_0$ because it is a rectangle.
> - If $F_1, F_2\in \FFF_0$ with $F_1 \supseteq F_2$, then $\rho((E_1\setminus E_2)_x) = \rho(E_{1,x}) - \rho(E_{2,x})$. 
> - If $F_1\cdots \in \FFF_0$ such that $F_i\uparrow F$, then the limit $F$ lies in $\FFF_0$ by continuity from below and monotone convergence theorem.
> [$\pi-\lambda$](pi lambda system) concludes.

> [!part]- Everything else
> The result is true for simple functions by linearity:
> - The desired functions are measurable because they're just sums.
> - Yea everything is just sums
> The result is true for nonnegative functions by [[Convergence properties of Lebesgue Integral#^Monotone-Convergence|Monotone Convergence]] and [[real-valued measurable functions#^sf-approx|approximation by simple functions]], and true for all integrable functions by signage casework.


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
