$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
We prove these results in the case of vector spaces $V, W$; the manifold case follows.

>[!theorem] Inverse function theorem.
> Let $V\cong W \cong \RR^n$. Let $U$ be a neighborhood of $x\in V$, and let $f:U\to W$ be a smooth map. Suppose $d_xf: \RR^n\to \RR^n$ is invertible for some $x\in U$. Then, there exists a neighborhood $x\in U'\subset U$ such that $f\big\vert_{U'} \to f(U')$ is a diffeomorphism (smooth and **invertible**). In this case,
> $$d_{f(x)}(f^{-1}) = (d_xf)^{-1}.$$
> 

Basically, you smash with the [[Contraction Mapping Theorem]].

>[!proof]- Finding the Inverse
> WLOG $x = 0$, $f(0)= 0$, and $D_0(f) = 1$ by linear transformation. Set $g(x) = f(x) - x$. $g\in C^1$ and $g'(0) = 0$ thus $$\forall\eps\exists \delta \forall z\in B(0,\delta)\quad g'(z)\in B(0,\eps).$$
> By mean value inequality on $t\mapsto g(x + t(y-x))$, for all $x,y\in B(0,\delta)$,
> $$\norm{g(y) - g(x)} \leq \norm{y - x}\sup_t \norm{g'(x + t(y-x))}\leq \eps\norm{y-x}.$$Picking $\eps < 1$, $g$ is a [[contraction mapping]] and we may apply the [[Contraction Mapping Theorem]]. Then $f$ is injective on $B(0,\delta)$, and $B(0, (1-\eps)\delta) \subset f(B(0,\delta)) \subset B(0, (1+\eps)\delta)$. Thus $f$ admits an inverse $f^{-1}: B(0, (1-\eps)\delta)\to B(0,\delta)$.

>[!proof]- Differentiability
> We claim that this $f^{-1}$ is differentiable with $d_y(f^{-1}) = \left(d_xf(f^{-1}(y))\right)^{-1}$. Pick $f(x) = y$ with $y\in B(0,(1-\eps)\delta)$ and $x\in B(0,\delta)$. For sufficiently small $h,k$ (such that everything fits inside the balls), $f(x + h) = y + k$, and $g(x + h) + x + h = y + k = g(x) + x + k$, or$$g(x + h) - g(x) = k - h \implies \norm{k - h} \leq \eps \norm{h} \implies \norm{k}\geq (1-\eps)\norm{h}$$
> This immediately implies
> $$
> 	\begin{align*}
> 	\lim_{\norm{k}\to 0} \frac{\norm{f^{-1}(y + k) - f^{-1}(y) - (d_xf)^{-1}k}}{\norm{k}}
> 	&= \lim_{\norm{k}\to 0} \frac{\norm{h - (d_xf)^{-1}k}}{\norm{k}}\\
> 	&= (1-\eps)(d_xf)^{-1}\left(\lim_{\norm{k}\to 0} \frac{\norm{(d_xf)h - k}}{\norm{h}}\right)\\
> 	&= 0
> 	\end{align*}.
> $$
> thus $f^{-1}$ has the intended derivative. This shows $f^{-1}$ is continuous.

>[!proof]- Smoothness
> Now, the fact that $d_y(f^{-1}) = i\circ df\circ f^{-1}$ shows that if $f$ is $C^k$, so is $f^{-1}$. Here, $i$ is the smooth matrix inversion map $T\to T^{-1}$.

# Deprecated?

>[!problem] Implicit Function
> Let $f_1,\dots, f_m$ be functions $\RR^n\to \RR$ which are ($C_k$/RA). Let $X\subset \RR_n$ be the set of points $P$ such that $f_i(P)= 0$ for all $i$. Suppose $df_i(P)$ are linearly independent for all such $P$. Use the [[implicit function theorem]] to show that $X$ is a topological manifold of dimension $n-m$ and equip it with a natural ($C_k$/RA) structure. Prove the analogous statement for holomorphic functions $\CC_n\to \CC$.

>[!proof]
>You can use the implicit functions to get homeomorphisms to $\RR^n$ on patches; these match up because everything is the desired regularity class and inverses and compositions are closed.

^1292a3

>[!todo]
>DO this!!! (better)