$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!idea] Physicists:
>Wait, you can't always do this?

>[!theorem]
> Let $U\subset \RR$ be open, and write a function $f:U\times E\to \RR$. We expect that
> $$
> 	\frac{\der}{\der t}\int_E f(t,x)\mu(dx) = \int_E \frac{\pa f}{\pa t}(t,x)\mu(dx)
> $$
> This is true (and all quantities are defined) if:
> 1. Your objects are actually defined:
> 	1. $f(t,\bullet)$ is integrable for all $t$.
> 	2. $f(\bullet, x)$ is differentiable for all $x$.
> 2. You have this stupid regularity condition which lets you apply dominated convergence:$$\forall x,t \qquad \abs{\frac{\pa f}{\pa t}(t,x)} \leq g(x)$$
>    for some integrable $g$.

> [!proof]- You know how this is going to go
> Okay fine. Ummmm, fix a $t\in U$. Let's consider a sequence $h_n\to 0$ such that $t+h_n$ lies inside $U$. Let our differences be
> $$
> 	\frac{f(t + h_n, x) - f(t, x)}{h_n} - \frac{\pa f}{\pa t}(t,x)
> $$
> By definition of partial derivative, this goes to $0$ for all $x\in E$. Thus, for all $t$, $\frac{\pa f}{\pa t}(t, \bullet)$ is a limit of measurable functions and thus measurable as well (this isn't true in general I think). By the third condition, $\frac{\pa f}{\pa t}(t, \bullet)$ is integrable.
> 
> By the [[mean value theorem]],  $\abs{\frac{f(t+h_n, x) - f(t,x)}{h_n}}$ is equal to $\frac{\pa f}{\pa t}(t + \delta, x)$ for some $\delta < h_n$. Thus this is upper bounded by $g(x)$ as well, and we can execute dominated convergence.
> $$
> \begin{align*}
> \int_E \frac{\pa f}{\pa t}(t,x)\mu(dx) &= \lim \int_E \frac{f(t + h_n, x) - f(t, x)}{h_n}\mu(dx)
> \end{align*}
> $$
> Tada, win.
> $$
> \begin{align*}
> &= \lim \frac{1}{h_n}\left\{\int_E f(t + h_n,x)\mu(dx) - \int f(t,x)\mu(dx)\right\}\\
> &= \frac{\der}{\der t} \int_E f(t,x)\mu(dx)
> \end{align*}
> $$
>