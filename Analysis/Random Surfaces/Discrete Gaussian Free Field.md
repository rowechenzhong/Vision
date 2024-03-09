$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!definition] DGFF
>The ==**discrete GFF on $D$ with Dirichlet boundary conditions**== is the centered Gaussian vector $(\Gamma(x))_{x\in D}$ whose density function is
$$p(\gamma) \sim \exp\left( -\frac12 \frac{\mathcal{E}_D(\gamma)}{2d}\right),\qquad \gamma \in \RR^D,$$
where $\mathcal{E}_{D}$ is the ==**energy function**==$$\mathcal{E}_D(F) = \sum_{e\in E_{\bar{D}}} \abs{\nabla F(e)}^2.$$

>[!idea]
>We can add a $\sigma$ to the denominator of the expression; this amounts to scaling $\gamma$.

### Resampling Procedure
If we condition on $(\Gamma(y))_{y\in D\setminus\{x\}}$, $\Gamma(x)$ is distributed as
$$\sim \exp\left( - \frac{1}{4d} \sum_{y: y\sim x} \abs{\gamma_x - h(y)}\right) = \exp\left( - \frac12 (\gamma_x - \bar{h}(x))^2\right)$$
This immediately implies $\Gamma(x) - \overline{\Gamma(x)}\sim N(0,1)$ for all $x$. Consider the Markov Chain on $\Ff_{(D)}$, where on each step we choose a point $x\in D$ uniformly at random (any distribution supported on $D$ works) and replace $h(x)$ with $\bar{h}(x) + N(0,1)$. This is the ==**resampling procedure**== under which the GFF is the stationary distribution. 

### Covariance Function
Denote the ==**covariance function**== $\Sigma(x,y) = \Sigma_x(y) = \EE[\Gamma(x)\Gamma(y)]$. Observe that$$
\begin{align*}
	\Sigma_x(y) &= \EE[\Gamma(x)\Gamma(y)]\\
	&= \EE[\Gamma(x)\bar{\Gamma}(y)] + \underbrace{\EE[\bar\Gamma(x)(\Gamma(y) - \bar{\Gamma}(y))]}_0\\
	&+ \EE[(\Gamma(x) - \bar{\Gamma}(x))(\Gamma(y) - \bar{\Gamma}(y))]\\
	&= \overline{\Sigma_x}(y) + \id_{x=y}\\
	\implies \Delta \Sigma_x(y) &= -\id_{x = y}
\end{align*}
$$where the underbraced expression is $0$ by the resampling procedure.