---

aliases:
  - measure-preserving transformation
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Let $(E,\mathcal{E}, \mu)$ be a measure space. A measurable $\theta:E\to E$ is a ==**measure-preserving transformation**== if
$$
	\mu\circ \theta^{-1} = \mu
$$
on $\mathcal{E}$.

Then, given $\theta$, a measurable $A$ is ==**invariant**== if $\theta^{-1}(A) = A$. The set of invariant sets form a $\sigma$-algebra, denoted $\mathcal{E}_\theta$. A measurable function $f$ is invariant if and only if it is $\mathcal{E}_\theta$-measurable.

We say that $\theta$ is ==**ergodic**== if $\mathcal{E}_\theta$ contains only sets of measure $0$ and their complements.

> [!proof]- Verification
> $E\subset \mathcal{E}_\theta$ because $\theta^{-1}(E) = E$. Suppose $A\in \mathcal{E}_\theta$; then
> $$\theta^{-1}(E\setminus A) = \theta^{-1}(E)\setminus \theta^{-1}(A) = E\setminus A\implies E\setminus A\in \mathcal{E}_\theta.$$
> Finally, if $A_1,\dots A_n\in \mathcal{E}_\theta$, then
> $$
> 	\theta^{-1}\left(\bigcup_{i} A_i\right) = \bigcup_{i}\theta^{-1}\left(A_i\right) = \bigcup_{i} A_i
> $$
> as desired.

>[!example] Irrational Rotation
>Over $\RR/\ZZ$, $x\to x + \theta$ for irrational $\theta$ is ergodic.

>[!example] Bernoulli Shift
>Over $\RR^\NN$, sending $(x_1,x_2,\dots)\to (x_2,x_3,\dots)$ is ergodic.

# Problems

Show that if $\theta$ is ergodic and $f\to \RR$ is invariant, then $f = c$ almost everywhere for some constant $c$.