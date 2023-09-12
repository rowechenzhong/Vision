# Eigenanalysis 
 
 We finally have the tools necessary to study eigenvalues, culminating in the spectral theorem. 
> [!problem] Inverses
 If $\norm{T} < 1$ is bounded, then $1 - T$ is invertible, and its inverse is the absolutely convergent series $$ (1 - T)^{-1} = \sum_{n=0}^\infty T^n. $$ 

 
> [!solution] 
 The series is clearly absolutely convergent, because the $k$-th term has norm $\norm{T^k} \leq \norm{T}^k$, We have $$ (1 - T)\sum_{n=0}^\infty T^n = \sum_{n=0}^\infty T^n - \sum_{n=0}^\infty T^{n+1} = I - T^{n+1} = I. $$ Similarly, $\sum_{n=0}^\infty T^n(1 - T) = I$. 

 Thus, 
> [!problem] 
 $\GL(\HH)$ is open. 

 Now, here are several closely related notions. 
> [!definition] Resolvent Set, Spectrum
 Let $T \in \BB(\HH)$. The ==**resolvent set**== of $T$ is $$ \Res(T) = \{ \lambda \in \CC : T - \lambda\in \GL(\HH)\}. $$ The ==**spectrum**== of $T$ is $$ \Spec(T) = \CC \setminus \Res(T) $$ 

 
> [!definition] Eigenthings
 Let $T \in \BB(\HH)$. If $T - \lambda$ is not injective, then there exists some nonzero $v \in \HH$ such that $Tv = \lambda v$. Then, $v$ is an ==**eigenvector**== of $T$, and $\lambda$ is an ==**eigenvalue**== of $T$. We let $E_\lambda$ denote the set of all eigenvectors with eigenvalue $\lambda$. 

 Unfortunately, injectivity, surjectivity, and invertibility do not coincide for infinite-dimensional linear maps. So while all eigenvalues are in the spectrum, the converse is not true. 
> [!theorem] 
 Let $A\in \BB(\HH)$. Then $\Spec(A)$ is a closed subset of $B_{\norm{A}}(0)$ in $\CC$. 

 Btw, by Liouville's theorem, $\Spec(A)\neq \emptyset$. ## Self-Adjoint 
 
 
> [!definition] Self-Adjoint
 A linear operator $T \in \BB(\HH)$ is ==**self-adjoint**== if $T = T^\dagger$. 

 Preliminary property: 
> [!problem] Trivial
 Show that $\braket{u | Tu}\in \RR$ for all $u$. 

 
> [!solution] 
 Take the adjoint. 

 Next, we will make steps towards the spectral theorem. 
> [!problem] 
 $\Spec(T)\subset [ - \norm{T}, \norm{T}]$. 

 
> [!problem] Tedious
 Show that $\norm{T} = \sup_{\norm{u} = 1} \abs{\braket{u | Tu}}$. 

 
> [!problem] 
 At least one of $\pm \norm{T}$ is in $\Spec(T)$. 

 
> [!problem] 
 Actually, let $a_- = \inf_{\norm{u} = 1} \braket{u | Tu}$ and $a_+ = \sup_{\norm{u} = 1} \braket{u | Tu}$. Then $a_-, a_+ \in \Spec(T)$, and $\Spec(T) \subset [a_-, a_+]$. 

 
> [!problem] Positive Operators
 A ==**positive operator**== is a self-adjoint operator such that $\braket{u | Tu} \geq 0$ for all $u$. Show $T$ is positive iff $\Spec(T) \subset [0, \infty)$. 

 ## Spectral Theory 
 
 We now restrict our attention to $T$ a *compact* self-adjoint operator. We basically know the entire roadmap towards the spectral theorem, because we've done this whole thing before in the finite-dimensional case; all we need to do is repeat everything with higher power. 
> [!problem] Finite Sanity Check
 If $\lambda \neq 0$ is an eigenvalue of $T$, then $E_\lambda$ is finite-dimensional. 

 
> [!problem] Orthogonality Result
 Distinct eigenspaces are orthogonal. 

 
> [!problem] Number of Eigenvalues
 The set of nonzero eigenvalues of $T$ is countable. If it is a countably infinite sequence $\lambda_1, \lambda_2, \dots$, then $\lambda_n \to 0$. 

 
> [!theorem] Fredholm Alternative
 Let $A$ be a compact operator (dropping self-adjointness for the time being), and let $\lambda \neq 0$ be real. Then the range of $A - \lambda$ is closed. 

 In particular, if $A$ is self-adjoint, then $(A-\lambda)(\HH) = \ker(A-\lambda)^\perp$. Thus, ether $A-\lambda$ is bijective, or $E-\lambda$ is nontrivial and finite-dimensional. In particular, 
> [!problem] Largest Eigenvalue
 Let $T$ be nonzero. Then, there is some nonzero eigenvalue $\lambda_1$ with $\lambda_1 = \sup_{\norm{u} = 1} \abs{\braket{u | Tu}}$. 

 By subtracting these off one at a time, 
> [!problem] Maximum Principle
 The nonzero eigenvalues of $T$ can be ordered $\abs{\lambda_1} \geq \abs{\lambda_2} \geq \dots$ including multiplicity such that we have pairwise orthonormal eigenvectors $\{u_k\}$ for $\lambda_k$ satisfying $$ \abs{\lambda_j} = \sup_{\norm{u} = 1, u\perp u_i \forall i < j} \abs{\braket{u | Tu}}. $$ 

 At last: 
> [!theorem] Spectral Theorem
 Suppose $\HH$ is separable. If $\abs{\lambda_1} \geq \abs{\lambda_2}\geq \dots$ are the nonzero eigenvalues of $T$ counted with multiplicity and with corresponding orthonormal eigenvectors $\{u_k\}$, then $\{u_k\}_k$ is an orthonormal basis for $\overline{T(\HH)}$. This basis can be completed by an orthonormal basis $\{f_j\}$ of $\ker T$ such that $\{u_k\}\cup \{f_j\}$ forms an orthonormal basis for $\HH$. 












































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

% Operators
\newcommand{\xx}{\hat{x}}
\newcommand{\pp}{\hat{p}}
\newcommand{\ee}{\hat{E}}
\renewcommand{\aa}{\hat{a}} % aa makes an a with a dot on top.
\newcommand{\bb}{\hat{b}}
\renewcommand{\AA}{\hat{a}}
\newcommand{\BB}{\hat{B}}

\newcommand{\ad}{\hat{a}^\dagger}

% Woah, relativity
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

% Measure Theory
\newcommand{\AAA}{\mathscr{A}}
\newcommand{\BBB}{\mathscr{B}}
\newcommand{\FFF}{\mathscr{F}}
\newcommand{\GGG}{\mathscr{G}}
\newcommand{\HHH}{\mathscr{H}}

\DeclareMathOperator{\ess}{ess}

% A bunch of sets
\newcommand{\CC}{\mathbb C}
\newcommand{\FF}{\mathbb F}
\newcommand{\NN}{\mathbb N}
\newcommand{\QQ}{\mathbb Q}
\newcommand{\RR}{\mathbb R}
\newcommand{\ZZ}{\mathbb Z}
\newcommand{\SSS}{\mathbb S}
\newcommand{\II}{\mathbb I}

% Complex Bashing
\newcommand{\conj}[1]{\overline{#1}}
\DeclareMathOperator{\cis}{cis}


% A bunch of geometry
\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\newcommand{\dang}{\measuredangle} %% Directed angle
\newcommand{\ray}[1]{\overrightarrow{#1}}
\newcommand{\seg}[1]{\overline{#1}}
\newcommand{\arc}[1]{\wideparen{#1}}
\newcommand{\pow}{\text{pow}} %% Power

% Things about NT
\newcommand{\jacobi}[2] {\genfrac{(}{)}{1.5pt}{}{\,#1\,}{#2}}
\DeclareMathOperator*{\lcm}{lcm}
\DeclareMathOperator*{\ord}{ord}

\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}


% Linalg
\DeclareMathOperator*{\range}{range}
\DeclareMathOperator*{\nul}{null}
\DeclareMathOperator*{\Tr}{Tr}
\newcommand{\id}{1\!\!1}

% Other physics things
\newcommand{\der}{\ \mathrm {d}}

\newcommand{\ihat}{\boldsymbol{\hat{\textbf{\i}}}}
\newcommand{\jhat}{\boldsymbol{\hat{\textbf{\j}}}}
\newcommand{\khat}{\boldsymbol{\hat{\textbf{k}}}}
\newcommand{\rhat}{\boldsymbol{\hat{\textbf{r}}}}
\newcommand{\that}{\boldsymbol{\hat{\mathbf{\theta}}}}



% Lol, some groups
\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}
\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}

\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\End}{End}
\newcommand{\GL}{\mathbb{GL}}
\newcommand{\SL}{\mathbb{SL}}
$$
