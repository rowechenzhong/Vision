$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
A random variable $T:\Omega \to \ZZ_{\geq 0}\cup \{\infty\}$ is a ==**stopping time**== if $\{T\leq n\}\in \FFF_n$ for all $n\geq 0$.

> [!idea] You know this from 18.615!!
> One can determine if $T\leq n$ by looking at the information at time $n$!

> [!problem] Properties
> If $S,T$ are stopping times, $S\land T$ is a stopping time. 

### Induced algebra
We let
$$\FFF_T = \{A\in \FFF_\infty: \forall n \ A\cap \{T\leq n\}\in \FFF_n\}$$
>[!idea]
> This is the collection of futures $A$ such that, given we have stopped, we know whether or not $A$ will occur.

>[!proof] This is a $\sigma$-algebra (todo)

>[!idea]
 > Given that $S$ has occurred, I know whether or not $A$ will happen. If $T$ has occurred too, then obviously I know whether or not $A$ will happen; I can figure this out by looking at $S$.
 
>[!problem]
>If $S\leq T$, show $\FFF_S\subset \FFF_T$.

### Stopped Process

You can use a stopping time to stop a process. Given a process $X$, the ==**stopped process**== $X^T$ is
$$X^T_n(\omega) = X_{T(\omega) \land n}(\omega)$$
If $X$ is adapted/integrable, so is $X^T$.

We may wish to discuss the value of $X$ at its stopping time; let
$$
	X_T(\omega) = X_{T(\omega)}(\omega)
$$
whenever $T(\omega) < \infty$.
- If $T$ is bounded ($\{T = \infty\}$ has measure $0$), $[X_T]$ is well-defined.
- If $X_T$ admits an almost-sure limit $X_\infty$, we define $X_T = X_\infty$ on $\{T = \infty\}$ (this will be useful after we obtain the [[Martingale Convergence Theorems]]). 
- Otherwise... proceed at your own risk.

As expected, $[X^T_n]\to [X_T]$ in both cases.

> [!idea]
> At time $n$, suppose I know that $T$ occurred. Then I know the value of $T = m \leq n$. Thus I also know $X_{T(\omega)}$.

>[!problem]
>If $X$ is adapted, $X_T \id_{T < \infty}$ is an $\FFF_T$-measurable random variable.