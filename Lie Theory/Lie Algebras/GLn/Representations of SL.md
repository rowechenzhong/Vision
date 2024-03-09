$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
We will now compute the irreps of $\SL_n(\CC)$ through $\sl_n$. $\hh = \CC_0^n = \{x\in \CC^n: \sum_i x_i = 0\}$ as diagonal matrices with trace zero. In $\hh$, we let the matrix $(0,\dots,\underbrace{1}_i,\dots,0)$ be $\vec{e}_i$ (we will be conflating a lot of things).
>[!example] $\sl_3$
>$\hh$ contains, for instance,$$\begin{pmatrix}2&&\\&3&\\&&-5\end{pmatrix}$$which we embed as $(2,3,-5)$.

Thus $\hh^*$ is naturally isomorphic to $\CC^n / \CC_{\text{diag}}$ where $\CC_{\text{diag}} = Span((1,\dots,1))$, and I can pick simple roots $a^\vee_i = \vec{e}_i - \vec{e}_{i + 1}$, yielding fundamental weights $$\omega_i = (\underbrace{1,\dots,1}_i,0,\dots,0).$$
>[!example] $\sl_3$
>An element of $\sl_3$ with living in root space $\alpha_1^\vee = \vec{e}_1 - \vec{e}_{2} = (1,-1,0)$ must be an eigenvector of those elements of $\hh$; i.e. it looks like$$\begin{pmatrix}&1&\\&&\\&&\end{pmatrix}.$$A fundamental weight $\omega_2$ looks like $(1,1,0)$. Observe that the dot product of $(1,1,0)$ against $(1,-1,0)$ and $(0,1,-1)$ are $0$ and $1$, respectively.

Thus the dominant weights take the form $(m_1+\dots+m_{n-1}, m_2+\dots+m_{n-1},\dots,m_{n-1},0)$; non-increasing nonnegative integers.
# Fundamental Representations
Let $V = \CC^n$ be the irreducible ==**vector representation**== with basis $v_1,\dots, v_n$ and highest weight $v_1$ with weight $\omega_1$. Thus $L_{\omega_1} = V$.

>[!example] $\sl_3\curvearrowright \CC^3$
>We simply act via matrix multiplication. The action of the raising operators $e_{\alpha_i}$ on this space just moves the $i+1$-th coordinate to the $i$-th coordinate. One element of the highest weight space with with $\omega_1 = (1,0,0)$  is $(1,0,0)$, because if I try to use any $e_{\alpha_i}$, I hit air.

The trick to get higher-dimensional representations is to consider $\wedge^k V$; these are irreducible with a basis of $k$-blades. The highest weight vector is $v_1\wedge\dots\wedge v_k$ with weight $\omega_k$, thus $L_{\omega_k} = \wedge^m V$. Note that $\wedge^n V = \CC$ has the trivial representation, as the determinants are all $1$.

>[!example] $\sl_3\curvearrowright \wedge^2 \CC^3$
>This time, one element of the highest weight space with with $\omega_1 = (0,1,0)$  is $(1,0,0)\wedge (0,1,0)$. If I hit with $e_{\alpha_1}$, the two $(1,0,0)$ annihilate, and if I use $e_{\alpha_2}$, I hit air.

> [!example] $\SL_3\curvearrowright \wedge^2\CC^3$
> The Lie group $\SL_3$ operates via the exponential map a la [[Lie Theory/Fundamental Theorems of Lie Theory]]. In our specific framework, its good to note that diagonal matrices $e^h$ in $\SL_3$ exponentiate from $h\in \hh$, and so act by a scalar. Specifically, on weight space $\lambda \in \hh^*$, $h$ acts via $\lambda(h)$, thus $e^h$ acts via $e^{\lambda(h)}$.

Thus, the irreducible representation $L_\lambda$ for $\lambda = \sum_i m_i \omega_i$ is the [[All finite irreps are main diagonals|main diagonal]] of $\bigotimes_{i=1}^{n-1}\left(\wedge^i V\right)^{\otimes m_i}$.

> [!example] The $(2,1,0)$ irrep of $\sl_3$
> We want to find the main diagonal starting at $e_1\otimes (e_1\wedge e_2)\in \CC^3\otimes \wedge^2 \CC^3$.
> 
> You have to start by lowering it with $e_{-\alpha_1}$, obtaining $e_2\otimes (e_1\wedge e_2)$. Then, hit it with $e_{-\alpha_2}$, yielding $e_3\otimes (e_1\wedge e_2) + e_2\otimes(e_1\wedge e_3)$. You can hit this with anything now:
> - $e_2\otimes (e_2\wedge e_3)$
> - $2e_3\otimes (e_1\wedge e_3)$
> 
> Then you can hit these with more stuff to get the lowest weight vector, $e_3\otimes (e_2\wedge e_3)$. All in all, this guy is $7$-dimensional.
> 
> We can also quickly see that $(3,0,0)$ will be $S^3\CC^3$ which is $3 + 6 + 1 = 10$-dimensional, for instance.