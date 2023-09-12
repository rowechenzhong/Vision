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

> [!example] Euclidean Norm
Over $\RR^n$ or $\CC^n$, one can define the ==**Euclidean norm**== for any $1\leq p \leq \infty$ via $$ \norm{x}_p = \left(\sum_{i=1}^n \abs{x_i}^p\right)^{1/p}. $$ If $p = 2$, we recover the usual Euclidean norm. If $p = \infty$, this degenerates to a supremum. 

We should show this is a norm. Scaling and definiteness are trivial. The triangle inequality is given by the following lemma. 

>[!claim] Minkowski's Inequality
>The Euclidean norm satisfies the triangle inequality.
>^minkowski



> [!proof]-
This is a long-winded bit of oly ineq. First off, recall ==**Holder's inequality:**== if $n \in \NN$, $\{a_k\}_{k=1}^n$ and $\{b_k\}_{k=1}^n$ are sequences of complex numbers, and if $1< p < \infty$ and $1/p + 1/q = 1$, then $$ \sum_{k=1}^n \abs{a_k b_k} \leq \left(\sum_{k=1}^n \abs{a_k}^p\right)^{1/p} \left(\sum_{k=1}^n \abs{b_k}^q\right)^{1/q}. $$ Alright great. Now, consider that by the triangle inequality, $$ \sum_{k = 1}^n \abs{a_k + b_k}^p \leq \sum_{k=1}^n \abs{a_k} \abs{a_k + b_k}^{p-1} + \abs{b_k} \abs{a_k + b_k}^{p-1} $$ and by H\"older's inequality, $$ \leq \left(\sum_{k = 1}^n \abs{a_k}^p\right)^{1/p} \left(\sum_{k = 1}^n \abs{a_k + b_k}^p\right)^{\frac{p-1}{p}} + \left(\sum_{k = 1}^n \abs{b_k}^p\right)^{1/p} \left(\sum_{k = 1}^n \abs{a_k + b_k}^p\right)^{\frac{p-1}{p}} $$ which implies ==**Minowski's inequality:**== $$ \left(\sum \abs{a_k + b_k}^p\right)^{1/p}\leq \left(\sum \abs{a_k}^p\right)^{1/p} + \left(\sum \abs{b_k}^p\right)^{1/p}. $$ This is precisely the statement of the triangle inequality for the $\ell^p$ norm over finite sequences. 
