$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!theorem] Important Properties of CTSTs.
>Suppose $S, T$ are [[Continuous Time Stopping Times|stopping times]].
>1. If $S\leq T$, then $\FFF_S\subset \FFF_T$.
>2. $S\land T$ and $S\lor T$ are both stopping times. $\FFF_{S\land T} = \FFF_S\cap \FFF_T$, and this sigma-algebra contains $\{S\leq T\}$.

>[!example] A difference between continuous and discrete processes
>Suppose $(X_n)_{n\geq 0}$ is adapted to $(\FFF_n)_{n\geq 0}$, where $n\in \ZZ_{\geq 0}$. If $T$ is a stopping time, then $X_T\in \FFF_T$. This is clear; for any Borel set $A$,$$
>\{X_T\in A\}\cap \{T\leq n\} = \bigcup_{k = 0}^n \left(\{X_k\in A\}\cap \{T = k\}\right)\in \FFF_n
>$$

>[!idea] Intuition
>In continuous time, such an argument does not hold, because we cannot take a naive union over uncountable times. This is why we add regularity conditions such as those found in [[Continuous Random Process Definitions]].

> [!theorem] Really Really stupid Properties of CSTs
> 1. $\FFF_T\subset \FFF_{t+}$. If $(\FFF_t)$ is right-continuous, then $\FFF_{T+} = \FFF_T$.
> 2. If $T = t$ is constant, $\FFF_T = \FFF_t$ and $\FFF_{T+} = \FFF_{t+}$.
> 3. If $T$ is a stopping time, then $T$ is $\FFF_T$-measurable.

>[!theorem] Slightly Stupid Properties of CSTs
>1. Let $T$ be a ST. Let $A\in \FFF_\infty$. Let$$T^A(\omega) = \begin{cases}
>    T(\omega)& \omega \in A\\
>    +\infty & \Omega \notin A
>    \end{cases}$$Then $A\in \FFF_T$ iff $T^A$ is a stopping time.
> 2. Let $T$ be a ST. A function $Y: \{T\leq \infty\}\to (E,\GGG)$ is $\FFF_T$-measurable (on the restricted measurable space) iff, for every $t\geq 0$, the restriction of $Y$ to $\{T\leq t\}$ is $\FFF_t$-measurable (on the restricted measurable space).
>

> [!theorem] Arithmetic Properties of CTSTs
> 
> 1. If $(S_n)$ is a monotonically increasing sequence of STs, then $S = \lim \uparrow S_n$ is also a stopping time.
> 2. If $(S_n)$ is a monotonically decreasing sequence of STs, let $S  =\lim\downarrow S_n$.
> 	1. $S$ is a stopping time of the filtration $\FFF_{t+}$, and $$\FFF_{S+} = \bigcap_n \FFF_{S_n+}.$$
> 	2. If $S_n$ is stationary, i.e. $\forall \omega \exists N(\omega)\forall n\geq N(\omega)$, $S_n(\omega) = S(\omega)$, then $S$ is actually a stopping time for $\FFF$, and $$\FFF_S = \bigcap_n \FFF_{S_n}.$$

> [!idea] Intuition
> 1. This is clear, because $\{S\leq t\} = \bigcap_i \{S_i\leq t\}$.
> 2. Unfortunately, $S > t$ does not play under limits.
> 	1. However, it is contained in $\FFF_s$ for all $s > t$.
> 	2. If you're eventually stationary, everything is easy.