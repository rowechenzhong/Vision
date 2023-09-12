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
> [!definition] Moment Generating Function
> Given a random variable $X$, the ==**moment generating function**== is the function $m(\theta) = \EE\left[e^{\theta X}\right]$.

This funny-looking function concerned me when I first saw it. It's clearly somewhere in $(0,\infty]$, but we're not guaranteed to be finite for any $\theta$ except for $0$. First, observe that if $a < b < c$, then $e^b < e^a + e^c$, thus the region where this is finite is some interval $(\theta_-, \theta_+)$, (possibly with closed ends) containing $0$. So as long as this is intervals isn't $\{0\}$, we can perform some analysis on it.
In fact, this function is *very* well-behaved on this interval:

>[!theorem]
>Suppose there exist $\theta_- < 0 < \theta_+$ such that $m(\theta) < \infty$ on $(\theta_-, \theta_+)$. Then:
>- $\EE[X^k]$ exists and is finite for all $k\geq 1$.
>- $m(\theta)$ is a **smooth function** with derivative $m^{(k)}(\theta) = \EE[X^k e^{\theta X}] < \infty$.
> - In particular, if $\theta_+ > 0$,  $m^{(k)}(\theta) \to \EE[X^k]$ as $\theta\downarrow 0$.

>[!proof]
> $\EE[X^k]$ is defined and finite if $\EE[\max(0, X^k)]$ and $\EE[-\min(0, X^k)]$ are finite (by definition), but each side is dominated by an exponential (observe we really need $\theta_- < 0 < \theta_+$ for this; one can easily find counterexamples otherwise).
> 
> Uhh, todo finish later.

This object is the partition function of
> [!definition] Exponential Tilting
> For any $\theta\in (\theta_-, \theta_+)$, define a probability measure
> $$P_\theta(A) = \EE\left[\id_A \frac{e^{\theta X}}{m(\theta)}\right]$$
> This reweighting obeys
> $$\EE_\theta[f(X)] = \EE\left[f(X) \frac{e^{\theta X}}{m(\theta)}\right]$$

>[!proof]- This is a probability measure (TODO)
>Todo: boring

>[!example] Joint Tilted Distribution
>Now, we're going to extend the tilted probability measure to a sequence of i.i.d. $X_i$'s. [[Ionescu-Tulcea]] constructs a product measure respecting finite prefixes:
>$$\PP_\theta\left(\prod_{i = 1}^n A_i\right) = \EE\left[\prod_{i = 1}^n \id\left\{X_i\in A_i\right\} \frac{e^{\theta X_i}}{m(\theta)}\right]$$
>Then, expectations behave correctly (as one can check):
>$$\EE_\theta\left[f(X_1,\dots, X_n)\right] = \EE\left[f(X_1,\dots,X_n) \frac{e^{\theta S_n}}{m(\theta)^n}\right]$$
>^joint-tilted


>[!definition] Cumulant Generating Function
>The ==**cumulant generating function**== of a random variable is $\kappa(\theta) = \log m(\theta)$.

Again, this object plays nicely with the tilted distribution:

>[!idea] Moments
>Note that
>$$\kappa'(\theta) = \frac{m'(\theta)}{m(\theta)} = \EE\left[\frac{Xe^{\theta X}}{m(\theta)}\right] = \EE_\theta\left[X\right]$$
>and
>$$\kappa''(\theta) = \frac{m''(\theta)}{m(\theta)} - \left(\frac{m'(\theta)}{m(\theta)}\right)^2 = \EE_\theta\left[X^2\right] - \EE_\theta[X]^2 = \Var_\theta(X).$$
>
>Thus, assuming that your probability distribution isn't a point mass, $\kappa$ is **strictly convex** on $(\theta_-, \theta_+)$!

> [!definition] Legendre Dual
> $I(a) = \sup_{\theta\in \RR}[\theta a - \kappa(\theta)]$ is the ==**Legendre dual**== of $\kappa$. 
>^legendre-dual
