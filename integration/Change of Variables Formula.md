$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$> [!theorem] Change of Variables
> Suppose we have maps $(\Omega, \FFF, \PP) \stackrel{X}{\to} (S, \GGG, \mu) \stackrel{f}{\to} (\RR, \BBB, \nu)$. Let $Y = f\circ X$. In other words, $X$ is a random variable, and $Y = f(X) \in \RR$ is a function of $X$. Suppose $f\geq 0$ or $Y$ is integrable. Then,
> $$ \EE[Y] = \int_S f\der \mu $$
> i.e.
> $$ \int_\Omega f(X(\omega)) \der \PP(\omega) = \int_S f(x) \der( X_\sharp \PP)(x).$$

In particular, one can take $(S, \GGG) = (\RR, \BBB)$ and $f(x) = x$; then
$$ \EE[X] = \int_\RR x \der (X_\sharp \PP)(x).$$
as expected.

# Proof

This is our first major usage of the [[Convergence properties of Lebesgue Integral|convergence theorems]]; we will follow the [[measure theory function scaffold|standard scaffold]].

> [!part]- Indicators
> If $f = \id_E$ with $E$ measurable, then both sides each $\PP(X\in E)$.

> [!part]- Simple Functions
> If $f = \sum_{i=1}^n c_i \id_{E_i}$, we apply linearity to show both sides equal $\sum_{i=1}^n c_i \PP(X\in E_i)$.

> [!part]- Nonnegative Functions
> [[real-valued measurable functions#^sf-approx|One can find]] simple functions $f_n\uparrow f$. Then, by [[Convergence properties of Lebesgue Integral#^Monotone-Convergence|Monotone convergence]], we conclude that both sides are the limit
> $$\lim_{n\to \infty} \int_\Omega f_n(X(\omega)) \der \PP.$$

>[!part]- Absolutely Integrable
>Similarly, [[real-valued measurable functions#^sf-approx|one can find]] simple functions $f_n\to f$ such that $\abs{f_n} < \abs{f}$. Then, by [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]], we conclude that both sides are the limit
> $$\lim_{n\to \infty} \int_\Omega f_n(X(\omega)) \der \PP.$$