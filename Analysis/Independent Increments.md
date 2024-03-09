$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Here are an important class of [[Martingales in Continuous Time|CTMs]]. We say that a process $(Z_t)_{t\geq 0}$ on a vector space has ==**independent increments**== if $Z$ is adapted and, for every $0\leq s < t$, $Z_t - Z_s$ is independent of $\FFF_s$.

>[!example] Martingales seeded by independent increments
>  If $Z$ is real-valued, then
> 1. If $Z\in L^1$, then $Z_t - \EE[Z_t]$ is a martingale.
> 2. If $Z\in L^2$, then $Z_t^2 - \EE[Z_t^2]$ is a martingale.
> 3. If, for some $\theta\in \RR$, $\EE[e^{\theta Z_t}] < \infty$ for all $t\geq 0$, then $e^{\theta Z_t} / \EE[e^{\theta Z_t}]$ is a martingale.

>[!example] Doob
>Let $B_t$ be a brownian motion. Then $B_t^2 - t$ is a continuous martingale

>[!example] Exponential Martingales of Brownian Motion
>$\exp\left(\theta B_t - \theta^2 t/2\right)$ for $\theta > 0$ is a continuous martingale.

>[!example] GWN Martingales
> More generally, for any $f\in L^2(\RR_+, \BBB, dt)$, centered Gaussians $Z_t = \int_0^t f(s)dB_s$ have independent increments, thus$$\int_0^t f(s)dB_s,\qquad \left(\int_0^t f(s)dB_s\right) - \int_0^t f(s)^2ds,\qquad \exp\left(\theta\int_0^t f(s)dB_s - \frac{\theta^2}{2}\int_0^t f(s)^2ds\right)$$
> are all Poisson processes.

The [[Poisson Process]] is another example of a process, this time discrete-valued, which has independent increments. This creates its own class of martingales.