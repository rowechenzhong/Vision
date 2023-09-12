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
> [!definition] Pi system
> A ==**pi system**== on $\Omega$ is a collection of subsets that is closed under finite intersections.

^5c9b44

> [!definition] Lambda system
> A ==**lambda system**== on $\Omega$ is a collection of subsets such that:
>
> 1. $\Omega \in \Lambda$.
> 2. If $A,B \in \Lambda$ and $A \subseteq B$, then $B \setminus A \in \Lambda$.
> 3. If $A_1, A_2, \dots \in \Lambda$ and $A_i \uparrow A$, then $A \in \Lambda$.
>    
>    (This is sometimes called a ==**d-system**==).

The main idea is that these two definitions neatly partition the definition of a $\sigma$-algebra:

> [!theorem] $\pi + \lambda = \sigma$
>
> $\LL$ is a $\sigma$-algebra iff it is both a $\pi$-system and a $\lambda$-system.

> [!proof]
> First off, all $\sigma$-algebras are clearly $\pi$ systems, and satisfy the first two properties of $\lambda$-systems. The third property is simply a special case of countable unions.
>
> If you are a $\lambda$ system, then you have $\Omega$. Thus by the second condition you have complements. If you also a $\pi$ system, then finite intersections give you finite unions. Finally, given any collection $A_1, A_2,\cdots \in \LL$, their prefix unions $A_1\cup \cdots A_n$ are all in $\LL$, and thus by the third condition of $\lambda$-systems, their union is also in $\LL$.

> [!theorem] Dynkin's $\pi$-$\lambda$ Theorem
> Let $\mathcal{P}$ be a $\pi$-system, and $\LL$ be a $\lambda$-system. If $\mathcal{P} \subseteq \LL$, then $\sigma(\mathcal{P}) \subseteq \LL$.

> [!proof]-
>
> > [!claim]
> > The intersection of two $\lambda$-systems is a $\lambda$-system:
> >
> > 1. $\Omega$ lies in both.
> > 2. If $A \subset B$ lie in both, then $B\setminus A$ lies in both.
> > 3. If $A_1, A_2, \dots$ lie in both, then $A_1 \cup A_2 \cup \dots$ lie in both.
> >    To prove the theorem, let $\LL$ be the smallest $\lambda$-system containing $\mathcal{P}$, which can be obtained as the intersection of all $\lambda$-systems containing $\mathcal{P}$ (via Zorn's Lemma for instance). We will show that $\LL$ is a $\pi$-system, as this would show it is a $\sigma$-field.
>
> The trick now is to fix a $A\in \LL$ and let
>
> $$
>   \LL_A = \{ B\in \LL | A\cap B \in \LL\}
> $$
>
> It is clear that $\LL_A$ is a $\lambda$-algebra; thus $\LL_A = \LL$! This is precisely the desired.

> [!idea]
> Measure-theoretic proofs are difficult because we don’t have a closed form for all measurable subsets. Instead, we must first verify that a certain subset $\mathcal{P}$ has a property $\LL$ that we want. Then, Dynkin booststraps the results from $\mathcal{P}$ to its $\sigma$-algebra.
