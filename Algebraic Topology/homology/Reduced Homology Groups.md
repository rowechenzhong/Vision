$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
> [!problem]
> Suppose $X$ decomposes into path-connect components $\{X_\alpha\}$. Show that $H_n(X)$ is naturally isomorphic with the direct sum $\bigoplus_\alpha H_n(X_\alpha)$.

> [!solution]-
> A singular simplex has PC image, so $C_n(X)$ splits. $\pa_n$ respects this splitting, thus $H_n(X)$ does too.

>[!problem]
>Compute $H_0(X)$.

> [!solution]
> If $X$ is PC, $C_0(X)$ is $\bigoplus_{x\in X} \ZZ x$. For all spaces, $C_{-1}$ is defined to be $0$, thus $\pa_0 = 0$ and $\ker \pa_0 = C_0(X)$. We claim $\im \pa_1$ is exactly the kernel of $\eps: C_0(X)\to \ZZ, \sum_x n_x x\to \sum_x n_x$. This kernel lies in $\im \pa_1$, because $X$ is path-connected. This kernel contains $\im \pa_1$, by staring at its formula. Thus $H_0(X)\cong \ZZ$. If $X$ is not PC, then $H_0(X) \cong \bigoplus_\alpha \ZZ$.

>[!idea]
>This solution can be thought of as considering the unique $-1$-simplex with no vertices; then $\eps \equiv \pa_{-1}$.

>[!problem]
>Let $X$ be a point. Show $H_n(X) = 0$ for $n > 0$ and $H_0(X) = \ZZ$.

For these reasons, we like to define the ==**reduced Homology groups**== $\tilde{H}_n(X)$ which are the homology groups of the augmented chain complex ending $C_0(X) \stackrel{\eps}{\to} \ZZ\to 0$.