$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
Here is the example to keep in mind throughout the proof of Cramer's theorem.

>[!example] Discrete Calculation
>Suppose we iid random variables $X_1,\cdots X_n$ over the discrete distribution on $\{x_1,\cdots, x_k\}$ with positive probabilities $\{\pi_1,\dots, \pi_k\}$. Let us discuss the **large deviations** behavior of $$\PP\left(S_n\geq na\right)$$ when $\EE[X] < a < \ess \sup X$.

Then, the [[empirical measure]] $L^X_n$ itself is a random variable which is $\sigma(X_1,\cdots X_n)$-measurable; it can be visualized as an element of $[0,1]^k$. Of course, for any $\nu = (\nu_1,\cdots \nu_k)$, one can explicitly compute the probability
$$\PP\left(L^X_n = \nu\right) = \frac{n! \pi_1^{\nu_1} \cdot \dots \cdot \pi_k^{\nu_k}}{(n\nu_1)!\cdot \dots \cdot (n \nu_k)!} = \exp\left( - n D\left(\nu | \pi\right)  + o(n)\right)$$
where $D$ is the [[Kullback-Leibler Divergence]]. Now, we observe that $S_n = n\braket{x | L_n^x}$ is a function of $L^x_n$ only (the order does not matter). Thus,
$$\PP\left(S_n\geq na\right) = \sum_\nu \id\left(\braket{x,\nu}\geq a\right) \exp\left( - nD(\nu | \pi) + o(n)\right)$$
Well, there are at most $(n+1)^k$ possible $\nu$'s, so this whole summation actually collapses into the $o(n)$ term. By [[exponential distillation]],
$$-\frac1n\log \PP\left(S_n\geq na\right) = \inf_{\braket{x,\nu}\geq a}\left\{D(\nu | \pi)\right\} + o(1)$$
This is true for all $n$. Note that the $\inf$ implicitly ranges over $\nu$ in $(\ZZ / n)^k$, and this discretization changes with $n$. However, we also know $D(\bullet,\pi)$ is smooth, so taking the limit and allowing $\nu \in [0,1]^k$ shouldn't change anything. $D(\bullet, \pi)$ is also convex everywhere and globally minimized at $\nu = \pi$, which lies on the other side of the plane ($\braket{x, \pi} = \EE[X] < a$). Thus, we can take the infimum over $\braket{x, \nu} = a$. This is a constrained optimization problem in $\nu\in [0,1]^k$ with Lagrangian
$$D(\nu | \pi) + \rho\left(1 - \sum_j \nu_j\right) + \theta\left(\braket{x, \nu} - a\right)$$
Taking the $\nu_j$ partial yields
$$1 + \log \nu_j - \log \pi_j - \rho - \theta x_j = 0\implies \nu_j = \frac{\pi_j}{C} e^{\theta x_j}$$
Of course, $\rho$ says $C = m(\theta)$. Finally, $\theta$ says we must pick any $\theta = \theta_a$ such that
$$
\EE_\theta[X] = \frac{1}{m(\theta)}\sum_j \pi_j e^{\theta x_j} \cdot x_j = a
$$
This means $a = \frac{m'(\theta)}{m(\theta)} = \kappa'(\theta)$, so $\theta = \arg \sup_{\theta\in \RR}\left(\theta a - \kappa(\theta\right))$.

Anyways, this also means that $D(\nu | \pi) = \sum_j \nu_j \left(\theta_a x_j - \kappa(\theta)\right) = \theta a - \kappa(\theta)$, indicating that this $\theta a - \kappa(\theta)$ is a sort of fundamental object. The conclusion:
$$
	\lim_{n\to \infty} - \frac1n \PP\left(S_n\geq na\right) = \sup_{\theta \in \RR} \theta a - \kappa(\theta) = I(\theta)
$$
The LHS is known as the 

All of this motivates the definition of [[exponential tilting]]; in the large-deviation case, the distribution behaves as if it is tilted until the average is $na$.