$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Consider a [[Brownian Motion with Filtration]].

>[!claim] Simple Markov Property
>If $X_t$ is standard BM, for all $s\geq 0$, $(B_{s+t} - B_s)_{t\geq 0}$ is a standard BM independent of $\FFF_s$.

This is obvious.

>[!claim] Less simple Markov Property
>Actually, $(B_{s+t} - B_s)_{t\geq 0}$ is a standard BM independent of $\FFF_{s+}$.

This is because $B_{s+t} - B_s = \lim_{\eps\to 0} B_{s+t+\eps} - B_{s+\eps}$ by continuity, and limits preserve independence (which is obvious by considering the sigma algebras or something).

> [!theorem] Blumenthal
> Suppose $A\in \FFF^X_{0+}$. Then $\PP(A)\in \{0,1\}$.

Indeed, $A\in \sigma(B_t: t\geq 0)\pperp \FFF_{0+}$, thus just like [[Kolmogorov's Zero-One Law]] you win.

>[!claim] Strong Markov Property
>For any [[Stopping Time]] $T$ with $\PP(t < \infty) > 0$, set $B_t^{(T)} = \id_{T < \infty}(B_{T+t} - B_T)_{t\geq 0}$. Under the probability measure $\PP(\bullet | T < \infty)$, $B_t^{(T)}$ is a standard Brownian motion $\pperp \FFF_T$.

> [!proof] Dyadic on $T$ to make it countable, then remember definitions.

# Example Applications

>[!example] Brownian motion crosses $0$ i.o. near $0$.
>Almost surely:
> - For all $\eps > 0$, $\sup(B_s: s\in [0,\eps) > 0$ and $\inf(B_s: s\in [0,\eps) < 0$.
> - $\forall a\in \RR$, $T_a = \inf_{t\in \RR} B_t = a$ is finite (i.e. $\lim\sup B_t = +\infty$ and $\lim\inf B_t = -\infty$).

The first one is trivial. The second one observes that$$1 = \lim_{\delta\to 0} \PP\left(\sup\left\{B_s:s\in [0,1]\right\}\right)\geq \delta) = \lim_{\delta\to 0} \PP\left(\sup\left\{B_s:s\leq \left(\frac{a}{\delta}\right)^2\right\}\right)\geq a = \PP(T_a < \infty).$$Very cool!

An application of the strong markov property:

>[!example] Reflection Principle
>Let $S_t = \sup\{B_s: s\leq t\}$. Then, for all $0\leq a$ and $b\leq a$, $\PP(S_t \geq a, B_t\leq b) = \PP(B_t \geq 2a - b)$.

This is trivial, cool though.