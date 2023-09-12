$$
\require{physics}

% Misc
\newcommand{\cbrt}[1]{\sqrt[3]{#1}}
\newcommand{\sgn}{\text{sgn}}
\newcommand{\ii}[1]{\textit{#1}}
\newcommand{\eps}{\varepsilon}

% Expected Value
\newcommand{\EE}{\mathbb E}
\newcommand{\PP}{\mathbb P}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}

\newcommand{\pperp}{\perp\kern-6pt\perp}

% Lol relativity
\newcommand{\LL}{\mathcal{L}}
\newcommand{\pa}{\partial}

% Inequalities
\newcommand{\cyc}{\sum\limits_{\mathrm{cyc}}}
\newcommand{\sym}{\sum\limits_{\mathrm{sym}}}
\newcommand{\cycprod}{\prod_{\mathrm{cyc}}}
\newcommand{\symprod}{\prod_{\mathrm{sym}}}

\newcommand{\eq}[1]{\stackrel{#1}{=}}
\newcommand{\rgeq}[1]{\stackrel{#1}{\geq}}
\newcommand{\rleq}[1]{\stackrel{#1}{\leq}}

% Sets
\newcommand{\CC}{\mathbb C}
\newcommand{\FF}{\mathbb F}
\newcommand{\NN}{\mathbb N}
\newcommand{\QQ}{\mathbb Q}
\newcommand{\RR}{\mathbb R}
\newcommand{\ZZ}{\mathbb Z}
\newcommand{\SSS}{\mathbb S}
\newcommand{\II}{\mathbb I}

% Geometry
\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\newcommand{\dang}{\measuredangle} %% Directed angle
\newcommand{\ray}[1]{\overrightarrow{#1}}
\newcommand{\seg}[1]{\overline{#1}}
\newcommand{\arc}[1]{\wideparen{#1}}
\newcommand{\pow}{\text{pow}} %% Power


% Complex Bashing
\newcommand{\conj}[1]{\overline{#1}}
\DeclareMathOperator{\cis}{cis}

% NT
\newcommand{\jacobi}[2] {\genfrac{(}{)}{1.5pt}{}{\,#1\,}{#2}}
\DeclareMathOperator*{\lcm}{lcm}
\DeclareMathOperator*{\ord}{ord}

\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Derivative
\newcommand{\der}{\ \mathrm {d}}

% Unit Vectors
\newcommand{\ihat}{\boldsymbol{\hat{\textbf{\i}}}}
\newcommand{\jhat}{\boldsymbol{\hat{\textbf{\j}}}}
\newcommand{\khat}{\boldsymbol{\hat{\textbf{k}}}}
\newcommand{\rhat}{\boldsymbol{\hat{\textbf{r}}}}
\newcommand{\that}{\boldsymbol{\hat{\mathbf{\theta}}}}

% Operators
\newcommand{\xx}{\hat{x}}
\newcommand{\pp}{\hat{p}}
\newcommand{\ee}{\hat{E}}
\renewcommand{\aa}{\hat{a}} % aa makes an a with a dot on top.
\newcommand{\bb}{\hat{b}}
\renewcommand{\AA}{\hat{a}}
\newcommand{\BB}{\hat{B}}

\newcommand{\ad}{\hat{a}^\dagger}

% Groups
\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}
\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}

% Linalg
\DeclareMathOperator*{\range}{range}
\DeclareMathOperator*{\nul}{null}
\DeclareMathOperator*{\Tr}{Tr}

% Homomorphism
\DeclareMathOperator{\Hom}{Hom}
% Endomorphism
\DeclareMathOperator{\End}{End}

\newcommand{\id}{1\!\!1}

\newcommand{\GL}{\mathbb{GL}}
\newcommand{\SL}{\mathbb{SL}}

% Measure Theory
\newcommand{\AAA}{\mathscr{A}}
\newcommand{\BBB}{\mathscr{B}}
\newcommand{\FFF}{\mathscr{F}}
\newcommand{\GGG}{\mathscr{G}}
\newcommand{\HHH}{\mathscr{H}}

\DeclareMathOperator{\ess}{ess}
$$
This is some magic, found [here](https://people.math.umass.edu/~yaoli/ptrl.pdf) Let's squeeze water from stone.

>[!theorem] Strong Law of Large Numbers
>Let $X, X_k$ be iid with finite mean $\EE[X] = \mu$. Then $\frac{S_n}{n}\to \mu$ **almost surely**.

# Motivated Proof

(Skip to the following section for the no-nonsense proof).

The **almost surely** win condition means we've got to prove a statement about measure $0$. This is a "pure" measure theory win condition. Let's write out explicitly what we need to prove;
$$\PP\left( \lim_{n\to \infty} \frac{S_n}{n}\to \mu\right) = 1 \iff \PP\left(\exists \eps \forall M \exists n > M, \abs{\frac{S_n}{n} - \mu} > \eps\right) = 0$$
Simple enough. Now, if any such $\eps$ exists, we might as well take it to be rational; thus the LHS is a countable union. Thus it is equivalent to prove
$$\forall \eps > 0, \qquad \PP\left(\forall M \exists n > M, \abs{\frac{S_n}{n} - \mu} > \eps\right) = 0$$
In other words, $\abs{\frac{S_n}{n} - \mu} > \eps$ *almost never occurs infinitely often.* This inspires us to use the [[Borel-Cantelli]] lemma, which says we need only prove
$$\forall \eps > 0,\qquad \sum_n \PP\left(\abs{\frac{S_n}{n} - \mu} > \eps\right) <\infty$$
And the event we're looking at now looks like a friendly Chebyshev bound! Easy right? Unfortunately, the interior does not follow easily from anywhere; we have no conditions on our $S_n$'s, and the variance might not even be defined.

Thus, we need to do some truncation on our $X$'s. Let $X = X^+ - X^-$, and then $X^+_n$ and $X^-_n$ each satisfy the theorem. So let's solve in the $X^+$ case, which implies the result.

Let's truncate by $Y_k = X_k \id\left\{X_k\leq k\right\}$, and let $T_n = \sum_{i\leq n} Y_n$ (everything now has finite, but not bounded a priori, variance).  How badly does differ from our $X_k$'s? It turns out that $Y_k \approx X_k$ in the best way possible:

>[!claim] $X_n\neq Y_n$ finitely many times almost surely

>[!proof]
>Indeed, $\sum_{n = 1}^\infty \PP\left(X_n\neq Y_n\right) = \sum_n \PP\left(X_n > n\right)$. But $\EE[X_1] = \int_0^\infty \PP(X > x)\der x$, which is strictly larger. So we apply Borel-Cantelli again.

Thus, it suffices to prove 
$$\forall \eps > 0,\qquad \sum_n \PP\left(\abs{\frac{T_n}{n} - \mu} > \eps\right) <\infty$$
This is actually Chebyshev all over again, because $\mu = \EE[X] = \lim_{n\to \infty} \EE[Y_n] = \lim_{n\to\infty} \frac{\EE[T_n]}{n}$.

>[!idea]- Failed attempt
For learning purposes, I'm going to try this even though I know it doesn't work. (Intuitively, the denominators are harmonic and grow too fast).
> 
> $$\begin{align*}
> 	\sum_n \PP\left(\abs{\frac{T_n}{n} - \mu} > \eps\right) &\leq \sum_n \frac{\Var(T_n)}{n^2\eps^2}\\
> 	&= \sum_n \frac{1}{n^2\eps^2}\sum_{m = 1}^n \Var(Y_m)\\
> 	&= \sum_n \frac{1}{n^2\eps^2}\sum_{m = 1}^n \int_0^m 2x\PP(X\geq x)\der x\\
> 	&= \sum_{m} \left(\sum_{n\geq m} \frac{1}{n^2\eps^2}\right) \int_0^m 2x\PP(X\geq x)\der x\\
> 	&= \sum_{m} \int_0^m \PP(X\geq x) \left(2x\sum_{n\geq m} \frac{1}{n^2\eps^2}\right)\der x\\
> 	&= \int_0^\infty \PP(X\geq x) \underbrace{2x\sum_{m\geq x} \left(\sum_{n\geq m} \frac{1}{n^2\eps^2}\right)}_\star \der x
> \end{align*}$$
> It suffices to uniformly bound $\star$ on $x$. Unfortunately, $\star$ is actually $\infty$ for all $x$.

The final key idea is that we really don't need to check *all* $n$ in the following quantification:
$$\PP\left(\forall M \exists n > M, \abs{\frac{T_n}{n} - \mu} > \eps\right) = 0$$
Let's pick an $\alpha$ and let $k_n = \ceil{\alpha^n}$. If we could show
$$\forall \alpha > 0,\qquad \PP\left(\forall M \exists n > M, \abs{\frac{T_{k_n}}{k_n} - \mu} > \eps\right) = 0$$
Then we would also be done, because for any $n$, I can find an $m$ such that
$$
	\frac{T_{k_m}}{\alpha k_m} \leq \frac{T_{k_m}}{n}\leq \frac{T_n}{n} \leq \frac{T_{k_{m+1}}}{n}\leq \alpha \frac{T_{k_{m+1}}}{k_{m+1}}
$$
and this is supposed to be true for all $\alpha$.

With this modification, the desired result *does* follow. Let's get on with it! In the following lines, any $C$ means some constant (function of $\eps$ and $\alpha$) which we don't care about.
$$\begin{align*}
	\sum_n \PP\left(\abs{\frac{T_{k_n}}{k_n} - \mu} > \eps\right) &\leq \sum_n \frac{\Var(T_{k_n})}{k_n^2\eps^2}\\
	&= \sum_n \frac{1}{k_n^2\eps^2}\sum_{m = 1}^{k_n} \Var(Y_m)\\
	&= \sum_n \frac{1}{k_n^2\eps^2}\sum_{m = 1}^{k_n} \int_0^m 2x\PP(X\geq x)\der x\\
	&= \sum_{m} \left(\sum_{n:k_n\geq m} \frac{1}{k_n^2\eps^2}\right) \int_0^m 2x\PP(X\geq x)\der x\\
	&\leq C\sum_{m} \frac{1}{m^2}\int_0^m 2x\PP(X\geq x)\der x\\
	&= C\int_0^\infty \PP(X\geq x) \underbrace{2x\sum_{m\geq x}\frac{1}{m^2}}_\star \der x
\end{align*}$$
Of course, if $x\leq 10$, then the expression is at most $2\cdot 10\cdot \frac{\pi^2}{6}$. The expression is also bounded by, $\frac{2x}{x-1}$, and thus is at most $3$ for $x\geq 10$. We conclude that this quantity is at most $C\cdot 100\cdot \EE[X]<\infty$. We win.

# Speedrun

Todo LOL

>[!part] Setup

First off, we can write $X = X^+ - X^-$, and then $X^+_n$ and $X^-_n$ each satisfy the theorem. So let's solve in the $X^+$ case, which implies the result. Let's truncate by $Y_k = X_k \id\left\{X_k\leq k\right\}$, and let $T_n = \sum_{i\leq n} Y_n$. For any $\eps > 0$, let's pick an $\alpha$ (determined later) and let $k_n = \ceil{\alpha^n}$. By Chebyshev's inequality,
$$\begin{align*}
\sum_n \PP\left\{ \abs{\frac{T_{k_n} - \EE[T_{k_n}]}{k_n}} > \eps\right\} &\leq 
\end{align*}$$
