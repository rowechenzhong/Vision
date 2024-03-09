$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
The results on this page are strictly stronger than the results in [[SLLN via Birkhoff and von Neumann]] and [[Strong LLN elementary proof]]. Let's commit arson :D

Consider the partial sums $S_n = X_1 + \dots + X_n$ where $X_i$ are independent.

# Basic SLLN

> [!theorem]
> Suppose $X_n$ are IID integrable, and let $\mu = \EE(X_1)$. Then, $\frac{S_n}{n}\to \mu$ as $n\to \infty$, AS + $L^1$.

The basic idea is that $\EE[X_1 | S_n] = \frac{S_n}{n}$, which allows us to apply [[Backwards MCT]].

Build the natural backwards filtration and write the tail sigma-algebra:
$$\hat{\FFF}_n = \sigma(S_m : m\geq n),\qquad \mathfrak{T}_n = \sigma(X_{n+1},\dots), \qquad \mathfrak{T} = \bigcap_n \mathfrak{T}_n$$
Observe that $\hat{\FFF}_n = \sigma(S_n, \mathfrak{T}_n)$. Because $X_1\pperp \mathfrak{T}_n$ and by symmetry,
$$\EE[X_1 | \hat\FFF_n] = \EE[X_1 | S_n] = \frac{S_n}{n}$$
almost surely, thus by BMCT $\frac{S_n}{n}\to \EE[X_1 | \hat\FFF_\infty]$ in AS+$L^1$.

>[!claim] The core reason SLLN works
>$\lim_{n\to \infty} \frac{S_n}{n}$ is $\mathfrak{T}_m$-measurable for all $m$ (modulo a measure-$0$ set).

>[!proof]
> Fix $m$ and $x\in \RR$. The set $\{\lim_{n\to \infty} \frac{S_n}{n} = x\}$ is $\mathfrak{T}_m$-measurable, because it is equal to $\{\lim_{n\to \infty} \frac{S_n - S_m}{n}\}$ for all $\abs{S_m} < \infty$ (an almost-sure event), and this guy is clearly $\mathfrak{T}_m$-measurable.

Thus $\EE[X_1 | \hat{\FFF}_\infty]$ is $\mathfrak{T}$-measurable. By [[Kolmogorov's Zero-One Law|K$01$]], this means it is constant almost surely. Taking expectations, it is $\EE[X_1]$ almost surely.