---

aliases:
  - Markov Chains
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

While discussing Markov chains, $E$ will forever be a countable set. Then, measures $\mu$ on $E$ are precisely given by their values on singletons sets $\mu_x = \mu(\{x\})$, and the integral of a function can be written as a "contraction"
$$\mu(f) = \mu \cdot f = \sum_{x \in E} \mu_x f(x).$$
Keeping in this linear algebra mindset, a ==**transition matrix**== on $E$ is a matrix $P = (p_{xy}, x, y \in E)$ such that each row is a probability distribution on $E$. That is, $p_{xy} \geq 0$ for all $x, y \in E$ and $\sum_{y \in E} p_{xy} = 1$ for all $x \in E$. Let $(\FFF_{n})_{n \in \NN}$ be a filtration on a probability space $(E, \mathcal{E}, \PP)$.  See [[Linear Algebra Intuition for Markov Chains]].

> [!definition] Markov Chain
> An adapted process $(X_n)_{n \in \NN}$ is a ==**Markov chain with transition matrix**== $P$ if
> $$\forall n \in \NN \forall A \in \FFF_n \forall x,y\in E,\qquad A\subset \{X_n = x\}\land \PP(A) > 0 \implies \PP(X_{n+1} = y | A) = p_{xy}.$$

This is exactly what you think it means; if we currently have $\FFF_n$ knowledge, the transition probabilities are given by $p_{xy}$. The only slight difference is that $\FFF_n$ might be finer than $\sigma(X_1,\dots, X_n)$. If this is the case though, we get the 18.615 definition:

>[!claim] No extra knowledge
>If $(X_n)_{n\geq 0}$ is a random process and $\FFF_n = \sigma(X_k: k \leq n)$, then $X$ is a MC with initial distribution $\mu$ and transition matrix $P$ iff for all $n$ and $x_0,\dots, x_n\in E$,
>$$\PP(X_0 = x_0,\dots, X_n = x_n) = \mu_{x_0}p_{x_0x_1}\dots p_{x_{n-1}x_n}.$$

The markov transition induces a probability measure on the space of sequences $E^* = \{(x_n: n\geq 0)\}$. Let $X_n: E^*\to E$ via $X_n(x) = x_n$, and let $\mathcal{E}^* = \sigma(X_k:k\geq 0)$.

>[!claim] Unique induced measure
>For each $x\in E$, there is a unique probability measure $\PP_x$ on $(E^*, \mathcal{E}^*)$ such that $(X_n)_{n\geq 0}$ is a MC with transition matrix $P$ starting from $x$.

This is obvious; the previous claim tells you what your measure is on all cylinders. Integration over this meausre is denoted $\EE_x$.