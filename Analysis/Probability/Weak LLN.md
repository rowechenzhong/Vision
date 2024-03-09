---

aliases:
  - WLLN
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Take [[Stupid LLN]] and smash it until we get what we want.

>[!theorem] Weak Law of Large Numbers
>Let $X, X_k$ be iid random variables such that $f(x) = x\PP\left(\abs{X} \geq x\right)\to 0$ as $x\to \infty$. Then, as $n\to \infty$, $\frac{S_n}{n} - \mu_n \to 0$ in probability, where $\mu_n = \EE\left(X; \abs{X} \leq n\right)$.

>[!proof]- Let's go
>We want to apply [[Stupid LLN#^stupid-lln|Stupid LLN]]. Let the $X_{n,k} = X_k$ and let $b_n = n$; interfacing complete. We copy + paste the conditions:
>1. $$ \sum_{k = 1}^n \PP\left( \abs{X_{n,k}} > b_n\right) = n\PP(\abs{X}\geq n)\to 0$$
> 2. $$ \frac{1}{b_n^2} \sum_{k = 1}^n \EE\left( X^2_{n,k} \id\left\{\abs{X_{n,k}} \leq b_n\right\}\right) = \frac{1}{n} \EE\left(X^2\id\left\{\abs{X}\leq n\right\}\right)$$
>    Let $Y_n = X_n \id\left\{\abs{X}\leq n\right\}$; then this is
>    $$\frac{1}{n}\int_0^{n^2} \PP\left(\abs{Y_n} \geq \sqrt{t}\right)\der t = \frac1n \int_0^n \PP\left(\abs{Y_n} \geq y\right)\cdot 2y\der y$$
>    Upper bound this shit to $\frac{2}{n}\int_0^n \PP\left(\abs{X}\geq y\right)\cdot y\der y \to 0$ and win.

>[!problem] Easier WLLN
> Let $X, X_k$ be iid with finite mean $\EE[X] = \mu$. Then $\frac{S_n}{n}\to \mu$ in probability.

(This easier version is obsolete given [[Strong LLN elementary proof]]).