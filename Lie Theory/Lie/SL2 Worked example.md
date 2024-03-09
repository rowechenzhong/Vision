$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Let $L = \sl(2,\FF)$. Its standard basis is
$$
	x = \begin{pmatrix}0 & 1\\0 & 0\end{pmatrix},\qquad y = \begin{pmatrix}0 & 0\\1 & 0\end{pmatrix},\qquad h = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}
$$
Then, $[hx] = 2x$, $[hy] = -2y$, and $[xy] = h$. Let $L\curvearrowright V$ be an irreducible module.

$h$ is semisimple, thus $h$ acts diagonally on $V$, because the abstract and usual JD's coincide. Thus we can discuss ==**weight spaces**== $V_\lambda = \{v: hv = \lambda v\}$; if $V_\lambda \neq 0$, $\lambda$ is a ==**weight**==. Clearly $x$ and $y$ lift and lower weights by $2$. The ladder terminates, thus there must exist some $V_\lambda \neq 0$ with $V_{\lambda + 2} = 0$; then any vector in $V_\lambda$ is a ==**maximal vector**== (of weight $\lambda$). Do the usual double-sided annihilation argument.

>[!theorem]
>Let $V$ be an irreducible module for $L$. Let $m + 1 = \dim V$.
>
>Relative to $h$, $V$ is a direct sum of $V_\mu$, where $\mu\in \{m, m-2,\dots, -(m-2), m\}$. Each $V_\mu$ has dimension $1$.
>
>Up to scaling, $V$ has a unique maximal vector, whose weight is $m$.
>
>The action of $L$ on $V$ is then fixed. There exists at most one irreducible $L$-module of each possible dimension $m + 1$ for $m\geq 0$

By applying Weyl's theorem, we have the result for *any* module;

>[!theorem]
>If $L\curvearrowright V$, then the eigenvalues of $V$ are all integers which have multiplicities symmetric about $0$, etc.
>
>Moreover, in any decomposition of $V$, the number of summands is exactly $\dim V_0 + \dim V_1$.