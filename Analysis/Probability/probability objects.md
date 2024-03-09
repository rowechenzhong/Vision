$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
This page will port over the essential ideas from [[Measure Theory]] theory in the context of [[Probability]]:

-   A ==**probability space**== is a [[measure space]] $(\Omega, \FFF, \PP)$ where $\PP(\Omega) = 1$.
-   An ==**event**== is an element of $\FFF$.
-   The ==**probability**== of an event $A\in \FFF$ is $\PP(A)$.
# Random Variables

An $(S,\GGG)$-valued ==**random variable**== is a [[measurable functions|measurable function]] on a probability space $(\Omega, \FFF, \PP)$. By default, we assume that $S = \RR$ and $\GGG = \BBB(\RR)$.

By abuse of notation, we let the _pre-image_ of a set of real numbers $A$ be denoted $\{X\in A\}$. So what we really mean when we write $\{X\geq 5\}$ is the _set of events for which_ $X(A) \geq 5$. 

>[!definition] Law
>Recall that $X$, like all measurable functions, induces a [[measurable functions#^127729|pushforward measure]] $X_* \PP$ over $\RR$. This measure, called the ==**law**==, is denoted $\LL_X$ or $\mu_X$, and acts on measurable subsets $B\subset \BBB(\RR)$ as
> $$
 	\LL_X(B) = \PP(X^{-1}(B)) = \PP(X\in B)
> $$
> So we're really just using the partition picture of functions here. No surprises.

^c1cbb1

>[!definition] CDF
>This law is uniquely determines and is uniquely determined by the ==**cumulative distribution function**== $F(x) = \PP(X\leq x)$. It is increasing and right-continuous, any any such function induces a random variable, a la [[Stieltjes Measure]].

^a89c00

>[!defn] PDF
> Some random variables admit ==**probability density functions**== $f(x)$ which are nonnegative measurable functions from $(\RR, \BBB_\RR)$ such that for all Borel sets $B$, $\mu_X(B) = \int_\RR \id(B) f(x) \mu(d x)$ under the standard Lebesgue measure $\mu$.

To emphasize, not all RVs admit PDFs; the random variable $X = 0$ does not. (Advanced:) such a PDF is an example of a [[Probability Density]].