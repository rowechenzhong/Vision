$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
This set of ideas comes before we create the bridge, but it will be an essential stepping stone.

When working with differentials in $\RR^n$, we don't distinguish between "infinitesimal movement by $(0,1)$ at $(0,0)$" versus "infinitesimal movement by $(0,1)$ at $(2,3)$," because the tangent space at $(0,0,0)$ is naturally identified with that at $(2,3)$. In vanilla differential geometry, $T_xM$ and $T_yM$ cannot be canonically identified, so one must make this distinction.

Recall that [[LG + Tensor Fields#^b9afb7|we can create a natural tangent bundle on $G$]]. The reason this is important is that $(1,x)\in T_1G$ and $d_1L_g(1,x)\in T_gG$ ***can now be canonically identified;*** they are both "infinitesimal left movement by $x$." Similarly, $d_1R_gx\in T_gG$ can also be identified with $x$; it is "infinitesimal right movement by $x$."

To this end, let's let $\fg = T_1G$, and pick some $x\in \fg$. We will abbreviate $T_1L_gx$ to $gx$ in the future, and $T_1R_gx$ to $xg$.

The question now is how to do calculations. We've [[Differential|defined the differential]], but the equation there is hopelessly ugly. As you might hope, in Lie, because of the above principles, one can think about vectors in $\fg$ simply as vectors, without referencing all of the germ garbage. We will never explicitly write a vector in $T_gG$ for $g\neq 1$ again; we will perform all computations with things like $gx$, $x\in \fg$, and replace all computations involving $d_g\phi$ with $d_1\phi$.

Here's the main computational claim, which is not deep and codifies this:

>[!claim] Shift differentials of homomorphisms
>Let $\phi:G\to H$ be a homomorphism of Lie groups sending $g\to h$. For any $x\in \fg$,
>$$(d_g\phi)(gx) = h(d_1\phi(x))$$
>

Recall that we're supposed to think $gx \equiv x$, $hx\equiv x$. In that case, this is just saying "$d_g\phi \equiv d_1\phi$," which is completely expected; a group homomorphism is basically linear.

>[!proof]-
> Indeed, observe
> $$\begin{align*}
> (d_g\phi)(gx) &= \left((d_g\phi)\circ (d_1 L_g)\right)x\\
> &= d[\phi\circ L_g]x\\
> &= d[L_h\circ \phi] x\\
> &= \left((d_1L_h)\circ (d\phi_1)\right)x\\
> &= h\left(d\phi_1(x)\right)
> \end{align*}$$
>