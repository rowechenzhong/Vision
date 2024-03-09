---

aliases:
  - KET
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

These are an extended set of notes on the [[Kolmogorov Extension]] theorem, in an attempt to gain a deeper understanding.

# The Extension Problem

Consider a set $X$, and a [[net]] $\{\Sigma_\nu: \nu \in J\}$ of $\sigma$-algebras on $X$ directed by inclusion. (For any $\Sigma_\mu, \Sigma_\nu$, there is some $\Sigma_\gamma \supset \Sigma_\mu, \Sigma_\nu$). Let $\{\PP_\nu: \nu \in J\}$ be a family of probability measures on $\Sigma_\nu$.

>[!definition]
>The family $\{\PP_\nu\}$ is ==**Kolmogorov consistent**== if $\Sigma_\nu \subset \Sigma_\mu$ implies $\PP_\nu\big\vert_{\Sigma_\mu} = \PP_\mu$. If so, $\{(\Sigma_\nu, \PP_\nu): \nu \in J\}$ is called a ==**Kolmogorov Net**==.

We assume so in the sequel. Let $A = \cup_{\nu \in J} \Sigma_\nu$; this is an algebra.

>[!idea] The Kolomogorov Extension Problem
>Is there a probability measure $\PP$ on $A$ that simultaneously extends every $\PP_\nu$?

There is only one possible candidate, which is $\PP(E) = \PP_\nu(E)$ on $E\in \Sigma_\nu$; these are consistent by definition. It is clear that $\PP$ is non-negative, $\PP(X) = 1$, and $\PP$ is finitely additive. Thus, we reduce to showing that $\PP$ is **countably additive**. If we can show this, $\PP$ is the ==**Kolmogorov extension**== of $\PP_\nu$ to $A$, and then [[Caratheodory extension Theorem]] bootstraps to $\sigma(A) = \sigma(\Sigma_\nu: \nu \in J)$.

By the [[Compact Class Bootstrap]], we have the following result:

>[!theorem] Abstract KET
>Let $\{(\Sigma_\nu, \PP_\nu):\nu\in J\}$ be a Kolmogorov net on $X$. Suppose there is a compact class $\mathscr{C}$ such that
>$$\forall \nu \in J \quad \forall E\in \Sigma_\nu,\qquad \PP_\nu(E) = \sup\left\{\PP_\nu(C): C\subset E, C\in \mathscr{C}\cap \Sigma_\nu\right\}.$$
>Then, there is a unique Kolmogorov extension to $\sigma\left(\bigcup_{\nu\in J} \Sigma_\nu\right)$.

Now, if you compute enough things, you obtain the usual [[Kolmogorov Extension]].

>[!todo] Finish this lol