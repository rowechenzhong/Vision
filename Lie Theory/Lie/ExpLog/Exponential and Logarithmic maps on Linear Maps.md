$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
The main point of writing out the [[14 classical Lie groups]] was to motivate the exponential and logarithmic maps in the context of linear algebra.

Recall:

> [!definition] Exponential and Logarithmic Maps
> We have an analytic function $\exp: \gl_n(\KK)\to \GL_n(\KK)$ via
>
> $$
> 	\exp(a) = \sum_{n = 0}^\infty \frac{a^n}{n!}
> $$
>
> and a function $\log:\GL_n(\KK)\to \gl_n(\KK)$
>
> $$
> 	\log A = -\sum_{n = 1}^\infty \frac{(1-A)^n}{n}
> $$
>
> which is analytic near $1\in \GL_n(\KK)$ and well-defined if the spectral radius of $1-A$ is less than $1$.

These satisfy:

> [!claim]
>
> 1.  They are mutually inverse.
> 2.  They are conjugation-invariant.
> 3.  $d\exp_0 = d\log_1 = \Id$
> 4.  If $xy = yx$, then $\exp(x + y) = \exp(x)\exp(y)$. If $XY = YX$ then $\log(XY) = \log X + \log Y$ (for $X,Y$ sufficiently close to $1$).
> 5.  For $x\in \gl_n(\KK)$, the map $t\to \exp(tx)$ is a homomorphism of Lie groups $k\to \GL_n(\KK)$.
> 6. $\det \exp(a) = \exp(\Tr a)$ and $\log(\det A) = \Tr(\log A)$.

So:

>[!example] $\SL_n$ is a Lie Group
>The group $G = \SL_n$ satisfies $\det A = 1$, so for $A$ close to $1$ $\Tr \log A = 0$; thus $\log A\in \sl_n(\KK) = \fg$, the space of matrices with trace $0$. This defines a local chart near $1\in G$, showing that $G$ is a manifold. 

Ditto for the other classical groups. The key relationship is:

>[!claim]
>Every classical group $G$ is a Lie group. We have:
>- $\fg = T_1G\subset \gl_n$.
>- If $\uu\subset \gl$ is a small neighborhood of $0$ and $U = \exp(\uu)$ then $\exp$ and $\log$ define mutually inverse diffeomorphisms between $\uu\cap \fg$ and $U\cap G$.