$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
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

3. [[Lebesgue Measure]] (More advanced alternative: [[Compact Class Bootstrap]])
4. [[Caratheodory Extension Theorem]]
5. [[More examples of measures]]


From here, one can study integration over measures, which is a large subject.

6. [[Integration]]

There is also more to be discussed in "point-set measure theory"

7.  [[box product measure]]
8.  [[product measure]]