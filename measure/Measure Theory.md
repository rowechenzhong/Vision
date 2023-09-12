This is the [[homepage|home page]] for measure theory.

# Introduction

In mathematics, the concept of a measure is a generalization and formalization of geometrical measures (length, area, volume) and other common notions, such as magnitude, mass, and probability of events. These seemingly distinct concepts have many similarities and can often be treated together in a single mathematical context.

Let's try to motivate measures with some simple examples from probability.

> [!example] Uniform Distribution
> Let $X$ be a random variable ``uniformly distributed" on the interval $[0,1]$. Then, for instance, we might say that the probability that $X$ takes on a value in the interval $[a,b]$ is $b-a$.

> [!example] Dice Roll
> Let $X$ be a random variable representing the outcome of a roll of a fair six-sided die. Then, for instance, we might say that the probability that $X = 3$ is $1/6$, and the probability that $X\in \{1,2,3\}$ is $1/2$. This is easily generalized to the "counting measure" on any finite set.

Both of these examples are instances of a more general concept: a measure. You will immediately notice that there are two essential components to a measure:

-   A set of objects, $S$. In the uniform distribution example, the objects are the real numbers in $[0,1]$, and in the dice roll example, the objects are the integers $\{1,2,3,4,5,6\}$.
-   A function $\mu$ that assigns a "size" to _subsets_ of $S$. In the uniform distribution example, the size of $[a,b]\subset S$ is $\mu([a,b]) = b-a$. In the dice roll example a is its length, and in the dice roll example, the size of an object is its probability.

There is a much less obvious third component to measures. It turns out that for $S$ that are larger than a finite set, [[vitali|it is impossible]] to assign a measure to _all_ subsets of $S$ without violating some basic assumptions about how measures should behave. However, one very rarely needs to be able to measure all sets; it is usually sufficient to be able to measure a large collection of so-called "measurable" sets.

# Main Sequence

If you would like, you can check out an [[measure prologue|extended prologue]].

First, the formal definition of a measure space.

1. [[measurable space]]
2. [[measure space]]

Next, we will _construct_ the most important measure spaces, starting with the real numbers.

3. [[Lebesgue Measure]]
4. [[Caratheodory Extension Theorem]]
5. [[Stieltjes Measure]]
6. [[Haar Measure]]
7. [[Standard Measure Construction]]

From here, one can study integration over measures, which is a large subject.

7. [[Integration]]

There is also more to be discussed in "point-set measure theory"

8.  [[box product measure]]
9.  [[product measure]]

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
