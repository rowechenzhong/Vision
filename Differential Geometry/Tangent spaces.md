$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$On (smooth/RA) manifolds $X$, a ==**derivation at**== $P$ is a functional on [[Germ|germs]] $D: O_P\to \RR$. This must satisfy the ==**Leibniz rule**==
$$
	D(fg) = D(f)g(P) + f(P)D(g)
$$
In particular, $D(1) = 0$.

We call the space of all such derivations $T_P X$, the ==**tangent space**==. This is a real vector space. (Everything ditto for CA manifolds).

 At first, this might seem really large, but it turns out that it's exactly what we think it is:

>[!claim] Basis
>Let $x_1,\cdots, x_n$ be local coordinates at $P$. Then $T_PX$ has basis
>$$
>	D_i(f) = \frac{\pa f}{\pa x_i}(0)
>$$

>[!proof] Boring, Todo

>[!idea]
>The elements of $T_PX$ are functionals of functions. (Differentiable) functions are locally "linear maps". Thus, elements of $T_PX$ are comparable with elements of $X$, and should be thought of as literally a space "tangent" to $X$ at $P$.

>[!idea]
>The point of confusion comes from notation. Previously, $x_i$ was a local coordinate - a function from $U\subset X$ to $\RR$). We have now written $D_i\in T_PX = \frac{\pa}{\pa x_i}$. This object has different type from $x_i$; it can be imagined as "the point with coordinates $(0,\dots, 1,\dots, 0)$."
>
>So $\pa_{x_i} = D_i$, but you should never write $\pa_{x_i} = x_i$. 
>
>$x_i$, as a function, is a ``covector," while objects like $\pa_{x_i} \in T_P X$ are vectors. To "contract" $\pa_{x_i}$ with a function $f$ is to evaluate $\pa_{x_i} f$, which is how much $f$ changes if you move by "$\eps x_i$", divided by $\eps$.
>
>For some reason, people write $v\in T_PX$ and then write $\pa_v : O(U)\to X$. I guess we're supposed to think $\pa_v\equiv v$. This is fine; just note that $\frac{\pa}{\pa x_i} \neq \pa_{x_i}$; we should write $\frac{\pa}{\pa x_i} \equiv \pa_{D_i} = D_i$.
>
>Of course, in the real world absolutely nobody gives a fuck.

>[!idea]
>You can extend derivations to algebras of regular functions, because the regular functions are elements of germs; you can write $\pa_v: O(U)\to \RR$.
