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
Let $U\subset V$ be an open subset of a vector space. Let $f:U\to W$ be a continuous function, and $p\in U$. Suppose there exists a linear map $T:V\to W$ such that
$$
\lim_{\norm{v}_V\to 0} \frac{\norm{f(p + v) - f(p) - T(v)}}{\norm{v}_V} = 0
$$
Then, $T$ is the ==**total derivative**== of $f$ at $p$, we let $(Df)_p = T$, and we say $f$ is ==**differentiable at**== $p$. As usual, if $f$ is differentiable at all points, then $f$ is ==**differentiable**==.

Nobody actually cares about anything other than $W = \RR^1$ because you can project, so I'll do that from now on, such that $(Df)_p \in V^\vee$. It is a terrible accident that $V^\vee \cong V$, thus $Df$ can be interpreted as a vector in its own right called the *gradient*; this is morally reprehensible and we will never use this.

# Partial derivative

Alternatively, you can pick a basis. Given $e_1,\dots, e_n$ and dual basis $e_1,\dots, e_n$ of $V$, the ==**$i$-th partial derivative**== of $f:U\to \RR$ is
$$
	\frac{\pa f}{\pa e_i}(p) = \lim_{t\to 0} \frac{f(p+te_i) - f(p)}{t}
$$
just as you expect. This reduces to what you learned in high school:

>[!problem] Components
>If $Df$ exists, then so do the partials, and
> $$
> 	Df = \sum_i \frac{\pa f}{\pa e_i}e_i^\vee
> $$

>[!solution]-
>If $Df_p$ exists, then we can take the limit along the $v = te_i$ as $t\to 0$, yielding
>$$
>	0 = \lim_{t\to 0} \frac{f(p + te_i) - f(p) - tT(e_i)}{t}\implies Df_p(e_i) = \frac{\pa f}{\pa e_i} e^\vee_i
>$$
>Thus all partials exist, and we can expand $Df$ in the $\{e_i^\vee\}$ basis.

In words, "the total derivative is a matrix full of partial derivatives." This yields the [[Jacobian matrix]] in the general case.


>[!problem] Continuous Partials implies differentiable
>Let $f:U\to \RR$, and suppose that $\frac{\pa f}{\pa e_i}$ is both defined and continuous for each $i$. Then $f$ is differentiable.
>
>Show that $$f(x,y) = \begin{cases}\frac{xy}{x^2 + y^2} & (x,y)\neq (0,0)\\ 0 & (x,y) = (0,0)\end{cases}$$ is a counterexample if we drop the continuous condition.

>[!solution]-
>Walk along each component. It is important that $\frac{\pa f}{\pa e_i}$ is differentiable for each $i$, or the rate of change of each line might not be bounded.
>
>Specifically, let $w_i = v_1e_1+\dots+v_i e_i$. After walking along each component, it suffices to prove
>$$
>\lim_{\norm{v}_V \to 0} \frac{\norm{f(p + w_i + v_{i+1}e_{i+1}) - f(p + w_i) - \frac{\pa f}{\pa e_i}(p) v_i}}{\norm{v}} = 0
>$$
>Fix $\delta > 0$.
>
>There exists an $\eps_1$ such that for all $\norm{v_{i+1}} < \eps_1$,
>$$
> \norm{f(p + w_i + v_{i+1}e_{i+1}) - f(p + w_i) - \frac{\pa f}{\pa e_i}(p + w_i) v_i} < 0.001\delta v_i
>$$
>Thus, there also exists an $\eps_2$ such that for all $\norm{v} < \eps_2$ the above statement holds (as $C_1\norm{v}\leq \norm{v_2} \leq C_2\norm{v}$ for some constants $C_1, C_2$).
>
>There exists an $\eps_3$ such that for all $\norm{w} < \eps_3$,
>$$
>\norm{\frac{\pa f}{\pa e_i}(p + w_i) - \frac{\pa f}{\pa e_i}(p)} < 0.001\delta
>$$
>Combining everything, we get our result.







