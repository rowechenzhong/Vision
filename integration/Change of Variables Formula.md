> [!theorem] Change of Variables
> Suppose we have maps $(\Omega, \FFF, \PP) \stackrel{X}{\to} (S, \GGG, \mu) \stackrel{f}{\to} (\RR, \BBB, \nu)$. Let $Y = f\circ X$. In other words, $X$ is a random variable, and $Y = f(X) \in \RR$ is a function of $X$. Suppose $f\geq 0$ or $Y$ is integrable. Then,
> $$ \EE[Y] = \int_S f\der \mu $$
> i.e.
> $$ \int_\Omega f(X(\omega)) \der \PP(\omega) = \int_S f(x) \der( X_\sharp \PP)(x).$$

In particular, one can take $(S, \GGG) = (\RR, \BBB)$ and $f(x) = x$; then
$$ \EE[X] = \int_\RR x \der (X_\sharp \PP)(x).$$
as expected.

# Proof

This is our first major usage of the [[Convergence properties of Lebesgue Integral|convergence theorems]]; we will follow the [[measure theory function scaffold|standard scaffold]].

> [!part]- Indicators
> If $f = \id_E$ with $E$ measurable, then both sides each $\PP(X\in E)$.

> [!part]- Simple Functions
> If $f = \sum_{i=1}^n c_i \id_{E_i}$, we apply linearity to show both sides equal $\sum_{i=1}^n c_i \PP(X\in E_i)$.

> [!part]- Nonnegative Functions
> [[real-valued measurable functions#^sf-approx|One can find]] simple functions $f_n\uparrow f$. Then, by [[Convergence properties of Lebesgue Integral#^Monotone-Convergence|Monotone convergence]], we conclude that both sides are the limit
> $$\lim_{n\to \infty} \int_\Omega f_n(X(\omega)) \der \PP.$$

>[!part]- Absolutely Integrable
>Similarly, [[real-valued measurable functions#^sf-approx|one can find]] simple functions $f_n\to f$ such that $\abs{f_n} < \abs{f}$. Then, by [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]], we conclude that both sides are the limit
> $$\lim_{n\to \infty} \int_\Omega f_n(X(\omega)) \der \PP.$$
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
