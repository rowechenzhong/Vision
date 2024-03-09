$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!example]
>This can be proven independently, but for all $\phi:[a,b]\to \RR$ continuously differentiable, for all non-negative Borel functions $f:[\phi(a), \phi(b)]\to \RR$,
>$$
>	\int_{\phi(a)}^{\phi(b)} f(y)\der y = \int_a^b f(\phi(x))\phi'(x)\der x
>$$

> [!proof]- Direct, so I feel better
> Are you serious right now. I'll show this for all intervals. If $f$ is the indicator on the interval $[\ell, r]\subset [\phi(a), \phi(b)]$, then we wish to show
> $$
> 	\mu([\ell, r]) = \int_{[a,b]\cap \phi^{-1}(E)} \phi'(x)\der x
> $$
> Fine I guess you have to pass through the [[Fundamental Theorem of Calculus]].
> 

>[!todo]
>What was this massacre. Go fix it.

> [!proof]- Huh, what are you saying (this is cap)
> Indeed, let's say WLOG $\phi'(x) > 0$ by like translating by a linear function or whatever; then $\phi$ is increasing and thus invertible on its domain, with continuous inverse. Then, $\phi$ is a random variable with PDF $\phi'$ by definition. We can let $g(y) = f(y)\phi'(\phi^{-1}(y))$; this is a composition of Borel functions and thus Borel. We wish to show:
> $$
> \begin{align*}
> 	\int_{\phi(a)}^{\phi(b)} g(y)\phi'(\phi^{-1}(y))^{-1}\der y&= \int_a^b g(\phi(x))\der x
> \end{align*}
> $$
> This would follow if $\phi'(\phi^{-1}(y))^{-1}\der\mu(y)$ was the pushforward measure $\der(\phi_\sharp \mu)$. But this is kind of clear; $\phi_\sharp \mu = \mu\circ \phi^{-1}$.