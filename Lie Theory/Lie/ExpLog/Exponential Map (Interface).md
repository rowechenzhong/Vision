$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
This is an [[interface]]. See [[Exponential Map (Construction)]].

>[!theorem] Properties of Exponential Map
> 1. $\exp: \fg\to G$ is a regular map which is a diffeomorphism of a neighborhood of $0\in \fg$ onto a neighborhood of $1\in G$, with $\exp(0) = 1$ and $\exp'(0) = \Id_\fg$.
> 2. For any particular $x\in \fg$, $t\to \exp(tx)$ is a homomorphism of real Lie groups.
> 4. The exponential map commutes with morphisms. For any morphism of Lie groups $\phi:G\to K$ and $x\in T_1G$,
> $$
> 	\phi(\exp(x)) = \exp\left(\phi_*x\right)
> $$
> where $\phi_*$ is the differential of $\phi$ at $1$.
> ^interface

# Problems

See [[Various Adjoint maps]].

>[!problem] Importance of $Ad$
>For all $g\in G$ and $x\in \fg$, $g\exp(x)g^{-1} = \exp(Ad_g x)$.

>[!solution]-
>Consider the map $\phi:G\to G$ via $h\to ghg^{-1}$. Then, by definition, $\phi_* = \Ad_g$, so this is just the previous property.

We can see the bridge being built now; $\fg$ completely describes $G$.

>[!problem]
>Suppose $G$ is a connected Lie group and $\phi:G\to K$ is a morphism of Lie groups. Then, $\phi$ is completely determined by the linear map $\phi_*:T_1G\to T_1K$.

>[!solution]-
>Indeed, $\phi(\exp(x)) = \exp(\phi_*(x))$. We know that $\exp$ is a diffeomorphism $\uu\to \fg$ on some neighborhoods $0\in \uu\subset \fg$ and some $1\in U\subset G$. Thus, $\phi(g)$ is completely specified on $g\in U$ by $\phi_*$.
>
>Because [[Lie Subgroups#^homomorphisms-tight|homomorphisms are tight]], we conclude.