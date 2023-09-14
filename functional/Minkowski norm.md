$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$Extending the Euclidean norm to this spaces of the form "$\CC^X$" takes a bit of work, because you need to integrate. It's much easier to try $\CC^\NN$. 

> [!example] $\ell^p$ space
For any sequence $\{x_i\}_{i=1}^\infty$ of complex numbers, and for any $1\leq p \leq \infty$, we define the ==**$\ell^p$ norm**== of $x$ to be $$ \norm{a}_p = \left(\sum_{i=1}^\infty \abs{x_i}^p\right)^{1/p}. $$ The ==**$\ell^p$ space**== is the set of all sequences which are bounded in $\ell^p$ norm. 

For instance, $\{1, 1/2, 1/3, \dots\}$ is in $\ell^p$ for all $p > 1$, but *not* in $\ell^1$.

>[!proof]- This is a normed space
Alright, we need to check triangle inequality again. Fortunately, we already have the [[Euclidean norm#^minkowski|Minkowski inequality]] for any finite prefix, and this is just sufficient.

>[!problem]
>Check that if we make the natural $p = \infty$ extension (take the supremum of the sequence instead), we arrive at the [[infinity norm]].
