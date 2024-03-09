$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
We will be discussing families of random variables $(X_t)_{t\geq 0}$.

- Such a family is ==**continuous**== if it is pointwise; for all $\omega \in \Omega$, the path $t\mapsto X_t(\omega): [0,\infty)\to \RR$ is continuous.
- Such a family is ==**cadlag**== if it is pointwise. (See [[cadlag]]). 

Then, a continuous random process can be considered as a random variable in $C([0, \infty), \RR)$ via $X(\omega) = \left(t\mapsto X_t(\omega): t\geq 0\right)$. Similarly, a cadlag random process is an RV in $D([0, \infty), \RR)$.

>[!idea] Borel Measure for a natural metrizable topology
>The $C([0,\infty),\RR)$ measure inherited from $\left.\BBB_R^{\otimes I}\right\vert_{C(t)}$ is equal to the metrizable topology of uniform convergence on compact time intervals; this is easily verified.

> [!idea]- Initial thoughts on the $\sigma$-algebra
> So, $\{x: x_t = 0\}$ is in the $\sigma$-algebra. If we're working with continuous or cadlag functions, then we can pinpoint $x$ on all values just by looking at a countable subset (e.g. $\{x_t: t\in \QQ\}$). So for any continuous/cadlag $f:\RR\to \RR$, $\{x: (\forall a\leq t \leq b\quad x_t = f(t)\}$ sounds like a measurable set. Ditto for $\{x: f \leq x \leq g\}$, or things like that. The exact details can be computed later.

If you restrict to a finite subset, you can get *finite-dimensional distributions*:
$$\mu_{t_1,\dots,t_n}(A) = \PP\left((X_{t_1},\dots, X_{t_n})\in A\right),\qquad A\in \BBB(\RR^n)$$
We call all such laws ==**finite-dimensional distributions**== of a continuous or cadlag process. By definition the cylinder sets are a generating $\pi$-system, thus they determined uniquely the law of $X$.

# Other Topics
From here, you should learn about
- [[Continuous Time Filtration]]
- [[Adapted Continuous-Time Processes]]
- [[Continuous Time Stopping Times]]
- [[Elementary Properties of Continuous Stopping Times]]
- [[Elementary Stopping Time Constructions]]
- [[Index Progressive Process at Stopping Time]]

Make sure you have all of the [[Continuous Stopping Time Intuition]]!