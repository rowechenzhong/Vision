---

aliases:
  - MCT
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

> [!theorem] AS MCT
> Let $X$ be an $L^1$-bounded supermartingale. Then, there exists an integrable $\FFF_\infty$-measurable random variable $X_\infty$ such that $X_n\to X_\infty$ almost surely as $n\to \infty$.

> [!idea] This is obvious
> Suppose you do not converge. Then, you contain an unbounded amount of [[upcrossings]]. This motivates us to perform strong bounds using the [[Doob's upcrossing inequality]], which turns out to kill immediately.

>[!proof]-
> Let
> $$\Omega_\infty = \{\lim\inf \abs{X_n} < \infty\},\qquad \Omega_{a,b} = \{U[a,b] < \infty\}$$
> for $a<b\in \QQ$. Then, let
> $$\Omega_0 = \Omega_\infty \cap \bigcap_{a < b\in \QQ} \Omega_{a,b}$$
> Observe that $X_n(\omega)$ converges iff $\Omega \in \Omega_0$. By [[Convergence properties of Lebesgue Integral|Fatou]] and [[Doob's upcrossing inequality|Doob]],
> $$\EE[\lim\inf \abs{X_n}] \leq \lim\inf \EE\abs{X_n},\qquad (b-a)\EE[(U[a,b])] \leq \abs{a} + \sup_{n\geq 0} \EE\abs{X_n}$$
> We said that $X$ was $L^1$-bounded though! So $\EE[U[a,b]]$ and $\EE[\lim\inf\abs{X_n}]$ is finite, and thus $U[a,b]$ and $\lim\inf \abs{X_n}$ are finite almost surely. Thus the countable union of $\Omega_{a,b}$ and $\Omega_0$ is also almost sure.
> 
> So why not let $X_\infty = \lim_{n\to \infty} X_n \id_{\Omega_0}$ (pointwise)? Then $X_n \to X_\infty$ almost surely, $X_\infty$ is $\FFF_\infty$-measurable, and $\abs{X_\infty}\leq \lim\inf\abs{X_n}$, thus $X_\infty$ is integrable.

Now, we use the [[L1 Convergence Theorem|UI bridge]] for the first (important) time.

> [!theorem] $L^1$ MCT
> Suppose $X$ is a UI martingale. Then, there exists $X_\infty \in L^1(\FFF_\infty)$ such that $X_n\to X_\infty$ almost surely and in $L^1$. $X_n = \EE(X_\infty | \FFF_n)$ almost surely for all $n\geq 0$.

> [!idea]- We expect $X_\infty$ to look like this. Think, don't read this.
> As a random process adapted to a filtration, $X$ branches like a tree; we pretend the tree terminates and has leaves. But if you know all the leaves, you also know all nodes of the tree; they're exactly the expected value over the sub-tree. It's completely unsurprising that this works to create martingales as well.

> [!proof]-
> By the AS MCT, we already know there exists an almost-sure limit $X_n\to X_\infty \in L^1(\FFF_\infty)$. By the [[L1 Convergence Theorem]], we win.
> 
> Now, for all $m\geq n$,
> $$
> \norm{X_n - \EE[X_\infty | \FFF_n]}_1 = \norm{\EE(X_m - X_\infty | \FFF_n)}_1\leq \norm{X_m - X_\infty}_1
> $$
> Taking the limit as $m\to \infty$, we find $\norm{X_n - \EE[X_\infty | \FFF_n]}_1 = 0$ as desired.


%%[!part]- idiotic verification; this is obvious.
In the below, $X$ is *not* $\FFF$ measurable.
$$
\begin{align*}
\EE\left[\abs{\EE[X | \FFF]}\right]
&= \EE\left[\left(\id_{\EE[X|\FFF] \geq 0} - \id_{\EE[X|\FFF] \geq 0}\right) \EE[X | \FFF]\right] \\
&= \EE\left[\EE[X \left(\id_{\EE[X|\FFF] \geq 0} - \id_{\EE[X|\FFF] \geq 0}\right)| \FFF]\right] \\
&= \EE\left[X \left(\id_{\EE[X|\FFF] \geq 0} - \id_{\EE[X|\FFF] \geq 0}\right)\right]\\
&= \EE\left[\abs{X}\right] + 2\EE[X \id_{X \geq 0\land \EE[X|\FFF] < 0}] - 2\EE[X \id_{X < 0\land \EE[X|\FFF] \geq 0}]\\
&\geq \EE[\abs{X}]
\end{align*}
$$ %%

> [!claim]
> On the other hand, for all $Y\in L^1(\FFF_\infty)$, if I let $X_n = \EE[Y | \FFF_n]$, $(X_n)_{n\geq 0}$ is a UI martingale such that $X_n\to Y$ AS in and $L^1$.

> [!proof]-
> This is a martingale by the [[Conditional Expectation|tower property]], and [[Conditional Expectations are UI|obviously]] uniformly integrable. Thus we know it has an AS + $L^1$ limit; we just need to show its actually $Y$. This is clear; for all $A\in \FFF_n$,
> $$\EE(X_\infty \id_A) = \EE(X_n \id_A) = \EE(Y \id_A)$$
> and we know the $\FFF_n$ generate $\FFF_\infty$, thus this is true for all $A\in \FFF_\infty$; thus $X_\infty = Y$ AS.

The $L^p$ case looks almost identical, for $p\in (1, \infty)$. 

> [!theorem] $L^p$ MCT
> Suppose $X$ is $L^p$ bounded. Then, there exists $X_\infty \in L^p(\FFF_\infty)$ such that $X_n\to X_\infty$ almost surely and in $L^p$. $X_n = \EE(X_\infty | \FFF_n)$ almost surely for all $n\geq 0$.

> [!proof] Todo (Use AS MCT and Doob's Lp inequality)

Also see the [[Backwards MCT]].