$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!theorem] Nilpotent Representation Lemma
>Let $L$ be a subalgebra of $\gl(V)$, where $\dim V < \infty$. This occurs universally; I'm just representing $L$ over $V$.
>
>If $L$ consists of nilpotent endomorphisms and $V\neq 0$, then there exists nonzero $v\in V$ such that $Lv = 0$.

>[!claim]
>Let $x\in \gl(V)$ be a nilpotent endomorphism. Then $\ad x$ is also nilpotent.

This is clear, because left and right translation by $x$ (sending $y\to xy$ and $y\to yx$) are each nilpotent in $\End(\End V))$.
The converse is clearly not true; $1\in \gl(\CC^n)$ is ad-nilpotent yet not nilpotent.

>[!idea]
>Nilpotent linear transformations admit an eigenvector (no shit).

> [!proof]- Long, tedious
> We use induction on $\dim L$; $\dim L = 0$ is clear.
> 
> If $K\neq L$ is any subalgebra (not necessarily an ideal) of $L$, then for all $k\in K$, $\ad k$ is nilpotent by the preceding claim. Thus $K$ acts on $L$ via $k\to \ad k$. This induces an action on the *vector space* $L / K$. Thus, $K$ can be thought of as a subalgebra of $\gl(L/K)$!
> 
>> [!idea]
>> Recall that subalgebras satisfy $[K,K]\subset K$, thus this action on the vector space is well-defined.
> 
> Thus, there exists some $x + K$ annihilated by $K$, i.e. $[x,K]\subset K$; $K\subsetneq N_L(K)$.
> 
> Suppose $K$ is a *maximal* proper subalgebra of $L$. Then, $N_L(K)\neq K$, thus $N_L(K) = L$, and $K$ is an ideal of $L$. Now, suppose $\dim L/K > 1$. Pick any $x \in L/K$; the span of $x$ is a one-dimensional subalgebra of $L/K$, which means $K + x$ is a proper subalgebra of $L$, contradiction. Thus $\dim L / K = 1$ and $L = K + \FF z$ for any $z\in L - K$.
> 
> By hypothesis, $W = \{v\in V: Kv = 0\}$ is non-empty. $K$ is an ideal, thus $KLW = 0$ because $xyw = yxw - [y,x]w = 0$; this means $LW \subset W$. Therefore, let $z$ act on $W$; it admits an eigenvector $v$. Then $Lv = 0$ as desired.

# Corollaries

[[Engel's Theorem]]

>[!theorem] Flags!
>If $L\subset \gl(V)$ consists of nilpotent endomorphisms, then there is a [[composition series]] $(V_i)$ such that $LV_i\subset V_{i-1}$ for all $i$.

This is clear; we pick $v\in V$ killed by $L$, take the flag from $L / (\FF v)$, and stick $V_1 = \FF v$ to the end.

>[!theorem] Center overlaps all ideals
>If $L$ is nilpotent and $K$ is a nonzero ideal of $L$, then $K\cap Z(L)\neq 0$.

Indeed, $L$ acts on $K$ via the adjoint representation, thus $[Lx] = 0$ for some $x\in K$.