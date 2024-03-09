---

aliases:
  - simplicies
  - simplex
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

>[!idea]- Ignore
>
> > [!definition] The $n$-simplex
> > An ==**$n$-simplex**== $[v_0,\dots, v_n]$ is the convex hull of $n+1$ points $v_0, \dots, v_n$ where $\{v_i - v_0\}$ are independent.
> In this definition, the order of the vertices $(v_0,\dots, v_n)$ is important; an $n$-simplex is a tuple of vertices, not a set.

> [!example] Standard $n$-simplex
> The ==**standard**== $n$-simplex is $\Delta^n = \{(t_0,\dots, t_n)\in \RR^{n+1} : \sum t_i = 1, t_i\geq 0\}$.

There is a canonical linear homeomorphism from $\Delta^n$ to any $n$-simplex via barycentric coordinates.

>[!definition] Faces and boundary
> If one deletes a vertex of $[v_0,\dots, v_n]$, one obtains an $n-1$ simplex $[v_0,\dots, \hat{v_i}, \dots, v_n]$; this is called a ==**face**==. When we describe a face of an $n$-simplex, the coordinates will always be their order in the larger subsimplex. You can delete more vertices too.
> 
> The ==**boundary**== $\pa \Delta^n$ of a simplex is the union of all of its faces; the ==**open simplex**== $\mathring{\Delta}^n = \Delta^n - \pa \Delta^n$.

Obviously, there is a canonical linear inclusion $\epsilon^i_n: \Delta^{n-1}\to \Delta^n$ if $\Delta^{n-1}$ is a face of $\Delta^n$. To write it out:
$$
	\epsilon^i_n: (x_1,\dots, x_i, \dots, x_n) \to(x_1,\dots, 0, \dots, x_n)
$$

>[!problem]
>Show $\epsilon^i_n\circ \epsilon^j_{n-1} = \epsilon^{j+1}_n\circ \epsilon^i_{n-1}$ for $i\leq j$.