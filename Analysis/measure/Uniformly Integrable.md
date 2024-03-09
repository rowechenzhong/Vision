---

aliases:
  - UI
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

>[!idea] A quick preview
>In the future, one will almost always prove $3$ versions of theorems: one for almost-sure, one for $L^1$, and one for $L^p$. UI connect AS and $L^1$.

> [!example] Integrable random variables vanish on vanishing sets
> Let $X$ be an [[constructing the Lebesgue Integral|integrable]] random variable. Set
> $$
> 	I_X(\delta) = \sup\left\{\EE[\abs{X}\id_A]: A\in \FFF, \PP(A)\leq \delta\right\}
> $$
> Then $I_X(\delta)\downarrow 0$ as $\delta\downarrow 0$.

> [!proof]- This is clear
> Otherwise, $\exists \eps >0$ and $A_n\in \FFF$ such that $\PP(A_n)\leq 2^{-n}$ and $\EE(\abs{X}\id_{A_n}) \geq \eps$ for all $n$; by Borel-Cantelli $\PP(A_n \ \text{i.o.}) = 0$. We now manually arrange for a $\lim\sup$ situation: note that for all $n$,
> $$
> 	\eps\leq \EE\left\{\abs{X}\id\left(\bigcup_{m\geq n}A_m\right)\right\}
> $$
> The RHS is a series of decreasing functions in $n$ which are bounded by the integrable function $\abs{X}$ and converge to $\abs{X}\id(A_n\ \text{i.o.})$... which integrates to $0$. Contradiction.

This property is a smoothness condition which we enjoy. Let's try to apply it to family of integrable random variables $\mathcal{X}$.

>[!definition] Uniform Integrability
> Write
> $$I_\mathcal{X} = \sup\{ I_X : X\in \mathcal{X}\}$$
> 
> $\mathcal{X}$ is ==**uniformly integrable**== or UI if $\mathcal{X}$ is bounded in $L^1$ and $I_\mathcal{X}(\delta)\downarrow 0$ as $\delta\downarrow 0$.
> 
> This is valid even if $\mathcal{X}$ is defined on different $\sigma$-algebras.

> [!example]- In general, $I_\mathcal{X}(\delta)$ will not converge to $0$ as $\delta \to 0$.
> Let $X_n = n$ identically; then $I_\mathcal{X}(\delta) = \infty$.

>[!idea] Interpreting the Definition
> Observe that $\mathcal{X}$ is [[Bounded in Lp|bounded in $L^1$]] iff $I_\mathcal{X}(1) < \infty$, so the condition is just making sure $I_\mathcal{X}(\delta) < \infty$ for all $\delta$.

>[!claim] Just check the hardest sets
>$\mathcal{X}$ is UI iff $$
>	\sup\left\{ \EE(\abs{X}\id_{\abs{X}\geq K} ): X\in \mathcal{X}\right\}\to 0
>$$ as $K\to \infty$.

>[!proof] Boring, TODO

Note that if $\mathcal{X}$ is bounded in $L^p$ for $p \in (1,\infty)$, then $\mathcal{X}$ is UI; on the flip side, $n\id(0, \frac1n)$ is in $L^1$ yet not UI.

>[!example] Large UI set
> For any integrable random variable $Y$, the set $$\mathcal{X} = \{X: X \text{ is a random variable}, \abs{X}\leq Y\}$$ is UI.

>[!example] Another Large UI set
>See [[Conditional Expectations are UI]].

The bridge is the [[L1 Convergence Theorem]].