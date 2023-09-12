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
There are $3$ main types of convergence of functions $(\Omega, \FFF, \mu)\to (\RR, \BBB_\RR)$ relevant for our purposes; each implies the next. Given a sequence of functions $f_n$ and another function $f$,
1. $f_n\to f$ ==**pointwise**== if $f_n(\omega)\to f(\omega)$ for all $\omega$.
2. $f_n\to f$ ==**with respect to $\mu$ almost everywhere**== if
   $$\mu\left( \left\{\omega: \lim_{n\to\infty} f_n(\omega) \neq f(\omega)\right\}\right) = 0$$
3. $f_n\to f$ **==in $\mu$-measure**== if for all $\eps > 0$, 
   $$ \lim_{n\to \infty} \mu\left( \left\{\omega: \abs{f_n(\omega) - f(\omega)} \geq \eps\right\}\right) = 0$$
In [[Probability]] theory, these are called pointwise, **==almost sure==**, and **==in probability==** convergence.
Finally, there is convergence in $L^2$ norm, which is what it sounds like. This implies convergence in $\mu$-measure on probability measures.
> [!todo] prove this shit smh

# Random Problems

>[!problem]
>Suppose $X_1, X_2,\cdots$ converge in probability. Show they also converge almost surely along some subsequence.

>[!problem] Cauchy in Probability
>Suppose $X_1, X_2, \dots$ are random variables such that
>$$\forall \eps > 0, \lim_{m,n\to \infty} \PP\left(\abs{X_m - X_n} \geq \eps\right)\to 0$$
>Then, we say $X_i$ are **==Cauchy in Probability==**. Show that there exists a random variable $X$ such that $X_i\to X$ almost surely.

> [!solution]-
> Ummm, first lets unpack some quantifiers.
>$$\forall \eps,\delta > 0 \quad \exists M \forall m,n\geq M\qquad \PP\left(\abs{X_m - X_n} \geq \eps\right) < \delta$$
>And we want to show that there exists an $X$ such that
>$$\forall \eps,\delta > 0 \quad \exists N \forall n\geq N\qquad \PP\left(\abs{X_n - X}\geq \eps\right) < \delta$$
>
>> [!proof]- There almost surely exists a convergent subsequence.
>>Cool. For all $k$, I construct an $M_k$ such that for all $m,n\geq M_k$, $$\PP\left(\abs{X_m - X_n}\geq 0.01 \cdot 2^{-k}\right) < 0.01 \cdot 2^{-k}$$
>>
>>The event that $\abs{X_{M_k} - X_{M_{k+1}}} < 0.01 \cdot 2^{-k}$ (which is an event, because it is the preimage of an interval under a measurable function) occurs with probability $0.01 \cdot 2^{-k}$. Let $E$ be the event that only finitely many such discrepancies occur (this is clearly a countable union of intersections, and is thus an event). By [[Borel-Cantelli]], $\PP(E) = 1$.
>>
>>Thus let $X$ equal the limit of $X_{M_k}$ on $E$, and set $X = 0$ elsewhere. This is a random variable because it is the limit of random variables.
>
>>[!proof]- Verification
>> 
>> Now, if $\eps,\delta > 2^{-k}$, we can select $N = M_k$. For all $n\geq M_k$, 
>> - $\abs{X_n - X_{M_k}} < 0.01\cdot 2^{-k}$ with probability at least $1 - 0.01\cdot 2^{-k}$.
>> - $\abs{X_m - X_{m +1}} < 0.01 \cdot 2^{-m}$ for all $m\geq k$ with probability at least $1 - 0.01\cdot \left(2^{-k} + 2^{-k-1} + \cdots\right)$.
>>   
>>Thus, with probability at least
>>$$1 - 0.01\cdot 2^{-k} - 0.01\cdot \left(2^{-k} + 2^{-k-1} + \cdots\right) > 1 -  2^{-k} > 1 - \delta,$$
>>we have
>>$$\abs{X_n - X} < 0.01\cdot \left(2^{-k} + 2^{-k} + 2^{-k-1} + \dots\right) < 2^{-k} < \eps$$
>>as desired.
