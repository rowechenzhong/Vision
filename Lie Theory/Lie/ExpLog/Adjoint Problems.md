$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
> [!problem] Commutative Lie Groups
> If $G$ is commutative, then $[x,y] = 0$ for all $x,y\in \fg$.

>[!solution]-
>Completely obvious by [[Adjoint Coincidence]].

>[!problem] Lie is a functor
>Let $G,H$ be lie groups and $\phi:G\to H$ a morphism of Lie groups. Then, $\phi^*:\fg\to \hh$ preserves the commutator:
>$$
>	\phi^*([x,y]) = [\phi^*(x), \phi^*(y)]
>$$
>
>In particular, for all $g\in G$, $g\in G$, the map $\Ad(g):G\to G$ is a morphism whose differential preserves the commutator:
> $$
> \Ad_G(g)([x,y]) = [\Ad_G(g)(x), \Ad_G(g)(y)]
> $$
>^Lie-functor

>[!solution]-
>We just need to show this for small $(x,y)$, because both sides are bilinear in $x,y$ and we can scale through constants. We already saw that $\phi$ commuted with the exponential map here: [[Exponential Map (Interface)]]. Recall [[How to invert the commutator]]. Observe that
>$$
>\begin{align*}
>	\exp(\phi^*([x,y])) &= \phi(\exp([x,y]))\\
>						&= \phi(\exp(x)\exp(y)\exp(x)^{-1}\exp(y)^{-1})\\
>						&= \exp(\phi^*(x))\exp(\phi^*(y))\exp^{-1}(\phi^*(x))\exp^{-1}(\phi^*(y))\\
>						&= \exp\left([\phi^*(x), \phi^*(y)]\right)
>\end{align*}
>$$
>and $\exp$ is a diffeomorphism for small $\hh$.