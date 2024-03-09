---

aliases:
  - Convergence in Distribution
  - converges weakly
  - in distribution
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Suppose $\mu$ is a [[Borel Measure|Borel Probability Measure]] on a metric space $E$. Let $\mu_n$ be a sequence of such measures. Then, ==**$\mu_n$ converges weakly to $\mu$**== if $\mu_n(f)\to \mu(f)$ for all continuous bounded $f$.

> [!claim] Portmanteau
> The following are equivalent.
> 1. $\mu_n\to \mu$ weakly.
> 2. $\lim\sup_n \mu_n(C) \leq \mu(C)$ for all closed sets $C$.
> 3. $\lim\inf_n \mu(G)\geq \mu(G)$ for all open sets $G$.
> 4. $\lim_n \mu_n(A) = \mu(A)$ for all Borel sets $A$ such that $\mu(\pa A) = 0$.

Over $\RR$ specifically, we can connect to the CDF.

>[!claim] Portmanteau
>Let $\{F_n\}$ and $F$ be the [[probability objects#^a89c00|CDFs]] of $\{\mu_n\}$ and $\mu$. $\mu_n\to \mu$ weakly on $\RR$ iff for all $x\in \RR$ such that $F$ is left-continuous, $F_n(x)\to F(x)$. The latter is often called ==**convergence in distribution**==.

Given a random variable $X$ on $E$ and a sequence of random variables $X_n$, $X_n\to X$ ==**weakly**== if $\mu_{X_n}\to \mu_X$ weakly. The random variables don't even have to be defined on the same probability space; this is purely a statement about their [[probability objects#^c1cbb1|laws]]. However, we do have the following result if $\mu_n\to \mu$ weakly:

> [!theorem] Skorokhod's representation Theorem
> Suppose that the support of $\mu$ is [[separable]] (which holds if, e.g., $E = \RR^d$). Then, there is *some* common probability space $(\Omega, \FFF, \PP)$ on which $E$-valued random variables $(X_n)$, $X$ can be defined, such that the laws of $X_n$ are $\mu_n$, and $X_n\to X$, $\PP$-almost surely (!!)

>[!idea]
>We're used to AS being way stronger than weak convergence, but that's not what this is saying at all. You can always find a bunch of random variables which witness your weakly converging laws, and because you have the freedom to pick them essentially however you want, you simply line them up such that they converge AS.

Finally, [[Prohorov's Theorem]] lets us extract a weak convergence from an *even weaker* condition.