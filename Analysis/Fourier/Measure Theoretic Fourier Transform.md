$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Suppose $\mu$ is a probability measure on $\RR, \BBB_\RR$. The ==**Fourier transform**== or ==**characteristic function**== of $\mu$ is
$$\hat{\mu} = \phi_\mu(t) = \int e^{itx} \der \mu(x)$$
from $\RR\to \CC$.

In particular, if $X$ is a random variable with law $\mu$, then its characteristic function is $\EE[e^{itX}]$. If $X$ also has a probability density $f(x)$, then this guy looks like$$
	 \phi_X(t) = \int e^{itx} f(x)\der x
$$The ==**$L^1$ Fourier Transform**== sends $f$ to $\hat{\mu}$; this can be conceptualized independent of the underlying $X$.

>[!thm] Properties
>This is well-defined and uniformly continuous for all $\RR$, and maps into the closed unit disk $D$.

>[!todo]- What the
> 
> Well, sure; let's show that it is well-defined first. Fix $t$; the function sure looks measurable to me lol. Then, by dominated convergence, this guy lies inside the closed unit disk everywhere. It is continuous in $t$ by the [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]] (use sequential continuity; the limit works).
> 
> We claim that its actually uniformly continuous. To this end, let's pick any $t$ and $\delta$; write
> $$
> \begin{align*}
> 	\abs{\EE[e^{i(t+\delta)X}] - \EE[e^{itX}]} &= \abs{\EE[e^{i(t+\delta)X} - e^{itX}]}\\
> 	&\leq \EE[\abs{e^{i\delta X} - 1}]\\
> 	&\to 0
> \end{align*}
> $$
> Where the limit is independent of the $t$ chosen.

Now, please recall the definition of a [[Convolution]].

>[!claim] Convolutions work
>$\widehat{\mu * \nu}(u) = \hat{\mu}(u)\hat{\nu}(u)$

This is clear; by definition, $\mu * \nu$ is the distribution of $X + Y$, so this is $\EE[e^{itX}e^{itY}] = \EE[e^{itX}]\EE[e^{itY}]$.
# Fourier Things

>[!theorem] Fourier Inversion Formula
>Let $f,\hat{f}\in L^1$. Then, $f(x) = \frac{1}{(2\pi)^d} \int_{\RR^d} \hat{f}(u) e^{-i\braket{u|x}}\der u$.

This is proved in the usual way: take a good kernel consisting of Gaussians.

>[!theorem] Plancherel Identity
>Let $f\in L^1\cap L^2$. Then, $\norm{\hat{f}}_2 = (2\pi)^{d/2}\norm{f}_2$.
>
>There is a unique Hilbert space automorphism (linear operator preserving the inner form) $F$ on $\mathcal{L}^2$ such that
>$$
>	(2\pi)^{d/2}F[f] = [\hat{f}]
>$$
>for all $f\in L^1 \cap L^2(\RR^d)$.

- [[Characteristic Functions and Distributions]]
- [[Characteristic Functions and Weak Convergence]]