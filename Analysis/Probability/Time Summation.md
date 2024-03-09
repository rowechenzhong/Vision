---

aliases:
  - Maximal ergodic lemma
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Suppose $f$ is measurable on $(E,\mathcal{E}, \mu)$. I would like to understand the long-term statistical behavior of $f$ as its inputs are moved under [[Ergodic Transformations|measure-preserving transformation]] $\theta$ (not necessarily ergodic!)

>[!defn] Time summation
>Let $S_0(f) = 0$, and
>$$S_n(f) = f + f\circ \theta + \dots + f\circ \theta^{n-1}.$$

First, a claim, interesting in its own right:

>[!claim] Maximal ergodic Lemma
>Let $f$ be integrable, and let $S^* = \sup_{n\geq 0} S_n(f)$. Then,
>$$
>	\int_{S^* > 0} fd\mu\geq 0
>$$

Here, $S^* > 0$ means that there exists some $k$ where $S_k(\omega) > 0$. In other words, its okay to add $\omega$, because you will later be "saved" by the terms later in the sequence. The fact that this actually works is some combinatorics. (Note that $S_0 = 0$, and thus $S^*\geq 0$).

> [!proof]- Setup
> We're just going to approximate the whole thing with finite processes. Let $S^*_n = \max_{0\leq m\leq n} S_m$ and let $A_n = \{S^*_n > 0\}$. Clearly, $A_n\uparrow \{S^*>0\}$ thus by dominated converge it suffices to show
> $$
> \int_{A_n} fd\mu > 0
> $$

> [!proof]- Combinatorics
> Clearly, for $1\leq m\leq n$,
> $$
> 	S_m = f + S_{m-1}\circ \theta \leq f + S^*_n\circ \theta
> $$
> Thus, we have the stupid bounds
> - On $A_n$, $S^*_n\leq f + S^*_n\circ \theta$.
> - On $A_n^c$, $S^*_n = 0\leq S^*_n\circ \theta$.
> 
> Thus,
> $$\int_E S^*_n d\mu \leq \int_{A_n}fd\mu + \int_E S^*_n\circ \theta d\mu = \int_{A_n}fd\mu + \int_E S^*_n d\mu$$
> and we win.