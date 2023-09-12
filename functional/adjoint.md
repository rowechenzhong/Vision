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
# Adjoints 
 
 What's the other property of inner product spaces you know from basic linear algebra? The *canonical isomorphism* between a vector space and its dual space. Let's build up to that now. Our first result will be that quotient spaces, which were kind of ugly in the Banach setting, work exactly how we expect in Hilbert spaces. 
> [!theorem] Convex Length Minimizers
 Let $C$ be a nonempty closed convex subset of $\HH$. Then there exists a *unique* $v\in C$ such that $$ \norm{v} \leq \norm{u} $$ for all $u\in C$. 

 Recall that in Banach spaces, we can talk about infimums, but a minimum is not guaranteed. 
> [!proof] 
 Details left as an exercise. Let $d = \inf_{u\in C}\norm{u}$. Then, there exists a sequence $u_n$ such that $\norm{u_n} \to d$. By the parallelogram law, $$ \norm{\frac{u_n - u_m}{2}}^2\leq \norm{\frac{u_n + u_m}{2}}^2 + \norm{\frac{u_n - u_m}{2}}^2 - d^2 = \frac{1}{2}(\norm{u_n}^2 + \norm{u_m}^2) - d^2 $$ The RHS vanishes. Thus, $u_n$ is Cauchy. Closed subsets of Banach spaces are complete, thus its limit lies in $C$. Uniqueness is also by the parallelogram law. 

 Because of this, the subspace architecture of Hilbert spaces looks almost exactly like that of vector spaces; there's just a few pesky topological details. 
> [!definition] Orthogonal Complement
 Given any subspace $W\subset \HH$, the ==**orthogonal complement**== of $W$ is $$ W^\perp = \{v\in \HH : \braket{v| w} = 0\text{ for all }w\in W\} $$ 

 
> [!problem] Properties of Orthogonal Complements
 First, show this is a closed linear subspace of $\HH$. The technical difficulty that happens here is that there exist subspaces which aren't closed, but orthogonal complements can't tell the difference; show $W^\perp = \overline{W}^\perp$. With this in mind, show: 
>  
>  
>  
>  -  If $W$ is closed, then $\HH = W \oplus W^\perp$. 
>  
>  -  $\left(W^\perp\right)^\perp = \overline{W}$. 
>  
>  -  Thus, for closed $W$, there exists a projection operator $P_W$ onto $W$. 
>  
>  

 
> [!proof] 
 This is a linear subspace by computation. It is closed because of continuity of the inner product. $W^\perp \supset \overline{W}^\perp$, and if $v\in W^\perp$, $v\in \overline{W}^\perp$ by continuity of the inner product. If $W$ is closed, pick a $u\in \HH$. Let $w^\perp$ be length minimizer of $u + W$. For all $a\in W$, if $\braket{a | w^\perp}\neq 0$ then considering $w^\perp + \lambda a$ for $\abs{\lambda}\ll 1$ yields a contradiction. Thus $w^\perp \in W^\perp$. $u - w^\perp \in W$ by definition. To show uniqueness, observe $W\cap W^\perp = \{0\}$, because any element of $W\cap W^\perp$ satisfies $\braket{v| v} = 0$. Observe that it suffices to prove $\left(W^{\perp}\right)^\perp = W$ when $W$ is closed. Clearly $W\subset \left(W^{\perp}\right)^\perp$. Now, if $v$ is not in $W$, then $v = w + w^\perp$ where $w^\perp\neq 0$. In particular, $\braket{v | w^\perp} \neq 0$. Thus, $v$ is not in $\left(W^{\perp}\right)^\perp$. The projection operator is a projection by uniqueness; we want to show that it is linear. This is also clear by uniqueness, lol. 

 ## Riesz 
 
 And at long last, my (erroneous) dream from Banach spaces is actually true here: 
> [!theorem] Riesz Representation
 Let $\HH$ be a Hilbert space. For all $f\in \HH'$, there exists a unique $v\in \HH$ such that $$ f = \bra{v} $$ 

 
> [!idea] 
Just as in the finite-dimensional case, this should be an isometric antilinear map... shrug!

 
> [!proof] 
 As expected, this follows directly from convex length minimizers. If $f = 0$, $v = 0$. Otherwise, $f^{-1}(1)$ is a convex set; it is closed because it is the preimage of $\{1\}$; thus it admits a length minimizer $v$. Let $N$ be the nullspace of $f$; actually $f^{-1}(1) = v + N$, so by variational reasons $v\perp N$. Then, $\CC v \oplus N = V$, because any $u$ is the sum of $u - f(u)v$ and $f(u)v$, the first of which is in $N$. We claim that $f = \frac{\bra{v}}{\braket{v| v}}$. Indeed, for all $u$, $$ f(u) = f\left( \frac{\braket{v | u}v}{\braket{v | v}} + u - \frac{\braket{v | u}v}{\braket{v | v}} \right) $$ The second item is perpendicular to $v$ by construction, and thus in the nullspace. Thus $f(u) = \braket{v | u}/\braket{v | v}$ as desired. This is unique by construction, but also because if $v,v'$ both worked, then $f(v - v')$ would yield $v = v'$. 

 ## Adjoints 
 
 Using the Riesz representation theorem, we can define adjoints like we did in the finite-dimensional case. 
> [!definition] Adjoint
 For any $A\in \BB(\HH, \HH)$, there is a unique $A^\dagger \in \BB(\HH, \HH)$ called the ==**adjoint**== such that $$ \braket{A^\dagger u | v} = \braket{u | Av} $$ for all $u, v \in \HH$. In fact, $\norm{A} = \norm{A^\dagger}$. 

 
> [!proof] 
 First off, we want to show that $A^\dagger$ uniquely exists, as a function. Given some $u$, observe that $\braket{u | Av}$ is a linear functional of $v$. It is also bounded, because $$ \braket{u | Av}\leq \norm{u}\norm{A}\norm{v} $$ Thus, by Riesz, there is some unique $w$ such that $\braket{w | v} = \braket{u | Av}$ for all $v$. Define $A^\dagger u = w$. Thus, we can unambiguously talk about the *function* $A^\dagger$; we'll show that this function has all the properties we want. $A^\dagger$ is linear, because \begin{align*} \braket{A^\dagger(u_1 + \lambda u_2) | v} & = \braket{u_1 + \lambda u_2 | Av}                                 \\ & = \braket{u_1 | Av} + \conj{\lambda} \braket{u_2 | Av}            \\ & = \braket{A^\dagger u_1 | v} + \braket{\lambda A^\dagger u_2 | v} \\ & = \braket{A^\dagger u_1 + \lambda A^\dagger u_2 | v} \end{align*} Finally, we want to show that $\norm{A^\dagger} = \norm{A}$. We have $$ \norm{A^\dagger} = \sup_{\norm{u} = 1} \norm{A^\dagger u} $$ But we know that $A^\dagger u$ is supposed to be the Riesz counterpart of the functional $f_u(v) = \braket{u | Av}$; thus this is actually $$ \sup_{\norm{u} = 1, \norm{v} = 1} \abs{\braket{u | Av}}\leq \sup_{\norm{v} = 1} \norm{Av} = \norm{A} $$ where the inequality is by Cauchy Schwarz. Equality is achieved at $u = \frac{Av}{\norm{Av}}$. 

 
> [!problem] Sort of Rank-Nullity
 If $A\in \BB(\HH, \HH)$, then $$ \left(A(\HH)\right)^\perp = \ker A^\dagger $$ 

 
> [!solution] 
 As sets, $$ \{v: \forall u\in \HH, \braket{u | Av} = 0\} = \{v: \forall u\in \HH, \braket{A^\dagger u | v} = 0\} $$ 

























