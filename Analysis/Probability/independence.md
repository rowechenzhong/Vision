---

aliases:
  - independent
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

>[!definition] Independent
>A set of events $\{A_\alpha: \alpha\in I\}$ are ==**mutually independent**== if for all finite subsets $J\subset I$,
>$$\PP\left(\bigcap_{\alpha \in J} A_\alpha \right) = \prod_{\alpha\in J} \PP(A_\alpha)$$
>
>Sometimes one also talks about independence of *collections* of events, $\{\mathcal{C}_\alpha, \alpha \in I\}$. In this case, it means that all choices of $A_\alpha\in \mathcal{C}_\alpha$ are independent. In particular, one can talk about independence of $\sigma$-algebras.
>
>If$\abs{I} = 2$, we write $A \pperp B$ and say $A$ and $B$ are ==**independent**==.

>[!defn] Independent RVs
>A set of random variables $\{X_\alpha:\alpha\in I\}$ are ==**mutually independent random variables**== [[Measurable functions generate sigma algebras|if their $\sigma$-algebras]] are independent.

>[!problem]
>For a sequence of real-valued RVs $\{X_n\}_{n\in \NN}$, this is equivalent to
>$$
>	\PP(X_1\leq x_1,\dots X_n\leq x_n) = \PP(X_1\leq x_1)\dots \PP(X_n\leq x_n)
>$$
>for all $n$ and $x_1,\dots, x_n\in \RR$.

>[!idea] Processes
>Such a sequence of RVs is often thought of as a process, where the indices index time. The $\sigma$-algebra $\FFF_n = \sigma(X_1,\dots X_n)$ contains those events that depend solely on $X_1, \dots, X_n$, and represents all historical information about the system at time $n$.

# Key example

> [!example]
> Consider when we have a [[product measure]] $(\Omega, \FFF, \PP)$. Then, one can define $X_\alpha(\omega) = f_\alpha(\omega_\alpha)$, where each random variable is a function of exactly one coordinate.

In this case, our intuition says that these random variables should be independent. Indeed, the pre-image of $B\in \BBB_\RR$ is
$$X^{-1}_\alpha(B) = f^{-1}_\alpha(B)\times \prod_{\gamma\neq \alpha} \Omega_\gamma$$
which has measure $\PP_\alpha(f^{-1}_\alpha(B))$ by construction. Then, finite products look like
$$ \PP_J\left(\prod_\alpha\in J f^{-1}_\alpha(B_\alpha)\right) = \prod_{\alpha \in J} \PP_\alpha\left(f^{-1}_\alpha(B_\alpha)\right)$$
which is also by definition.

It's also intuitively obvious that this is essentially the only possibility. If $\{X_\alpha: \alpha \in I\}$ are RVs, I can write
$$X(\omega) = (X_\alpha(\omega))_{\alpha \in I} \in \RR^I$$
and construct pushforward map $(\Omega, \FFF, \PP) \to \left(\RR^I, \bigotimes_{\alpha\in I} \BBB_\RR, \LL_X\right)$ where $\LL_X = X_\sharp \PP$ as usual. In this case, $X_\alpha$ are independent RVs iff $\LL_X$ is our product measure!

> [!todo] Prove this LOL