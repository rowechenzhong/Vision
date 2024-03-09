$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!definition] Mean and Covariance
>A ==**$d$-dimension GRV**== is $X: \Omega\to \RR^d$ such that $\braket{X, u}$ is a GRV for all $u\in \RR^d$.
> 
>Then, there exists a ==**mean**== $\mu = \EE[X]\in \RR^d$ and ==**covariance matrix**== $\sigma = \Cov(XX^\top) = \EE[(X - \EE[X])^\top (X - \EE[X])]$ such that $\EE[\braket{u, X}] = \braket{u, \EE[X]}$ and $\EE[(\braket{u,X} - \braket{u, \EE[X]})(\braket{X,v} - \braket{\EE[X],v})] = \sigma$.

>[!claim] The law of $X$
>The law of $X$ is uniquely determined by $\mu = \EE[X]$ and $\sigma= \Cov(X X^\top)$.

>[!idea] This is not an existence proof.

> [!proof]- Fourier Transform
> $$\underbrace{\varphi_X(\theta)}_{\RR^d\to \CC} = \EE[e^{i\braket{\theta, X}}]$$
> and you can compute the RHS from the definition, because I know that $\braket{\theta, X}$ is a Gaussian with mean $\braket{\theta, \mu}$ and variance $\braket{\theta | \sigma | \theta}$. It is well known that the mapping from laws to characteristic functions is injective.

If $\Sigma$ is positive definite and invertible, then it can be written $\Sigma = A A^\top$, and you can apply $\mu + AZ$ to a standard normal GRV to obtain density$$\frac{1}{(2\pi \det \Sigma)^{1/2}} \exp\left( - \frac12 \left(x - \mu)^\top \Sigma^{-1}(x - \mu)\right)\right).$$If $\Sigma$ is not invertible, then the Gaussian lives in a lower-rank subspace and does not admit a density.

>[!claim] For gaussians, independent $\iff$ uncorrelated.

$\implies$ is trivial. 

>[!claim] The components of a GRV are independent iff $\Sigma$ is diagonal
>^claim-GRV-independent-diagonal