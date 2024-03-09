---

aliases:
  - regular covering space
  - regular
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

> [!definition] Regular Covering Space
> A covering space $p: \tilde{X}\to X$ is ==**regular**== if for each $x\in X$, and each $\{\tilde{x}_0, \tilde{x}_1\}\in p^{-1}(x)$, there exists a deck transformation sending $\tilde{x}_0$ to $\tilde{x}_1$. Such a covering space is also called a ==**normal**== covering space. This is because a covering space is normal iff $H = p_*(\pi_1(\tilde{X}, \tilde{x}_0))$ is a normal subgroup of $\pi_1(X, x_0)$! 

> [!proof] 
Pretty cool, right? There's a chain of logic here which is pretty clear, you just need to know the definitions. Let $\gamma$ be a loop which lifts to a path from $\tilde{x_0}$ to $\tilde{x_1}$. The following are equivalent: 
>  
>  
>  
>  -  $[\gamma] \in N(H)$, the normalizer of $H$. 
>  
>  -  $[\gamma] H [\conj{\gamma}] = H$. 
>  
>  -  $p_*(\pi, (\tilde{X}, \tilde{x}_0)) = p_*(\pi_1(\tilde{X}, \tilde{x}_1))$. 
>  
>  -  There exists a deck transformation sending $\tilde{x}_0$ to $\tilde{x}_1$. 
>  
>  Thus, the covering space is normal (the preceding statements hold *for all* $x, \tilde{x}_0, \tilde{x}_1$) if and only if $H$ is normal (*all* $[\gamma]$ lie in $N(H)$). 

Taking this to the general case, we observe that 

> [!theorem] 
$G(\tilde{X})$ is isomorphic to $N(H) / H$. 

> [!proof] 
We exhibit a surjective $\Psi: N(H) \to G(\tilde{X})$ with kernel $H$. There's really only one way to do this! Given a loop $[\gamma]\in N(H)$, we know there exists a unique deck transformation $\phi$ sending $\tilde{x}_0$ to $\tilde{x}_1$. We define $\Psi([\gamma]) = \phi$. $\Psi$ is then a homomorphism, because composing the loops corresponds to nesting conjugations. This is surjective by the above discussion, and the kernel is $H$ by definition. 

In particular, for the universal cover $\tilde{X}$, $G(\tilde{X}) = \pi_1(X, x_0)$. Shouldn't be too surprising, if you understood the discussion on universal covers. 

> [!problem] Chaining Normal Covering Spaces
Given covering maps $p:X\to Y$ and $q:Y\to Z$, suppose $q\circ p: X\to Z$ is normal. Show $p$ is normal. Hint: assume $X$ is connected at first. 

This problem is a useful tool in conjunction with the [[chaining covering spaces|chaining lemma]].

> [!solution]- 
Our hands are again forced; this problem makes sure you understand all the tools. Let's pick a $y\in Y$, let $z = q(y)$, and let $x,x' \in p^{-1}(y)$. $q\circ p$ is normal, so we can find a homeomorphism $\phi:X\to X$ such that $qp\phi = qp$ and $\phi(x) = x'$. The main idea is that $\phi$ *almost works*. Suppose $X$ was connected. Then, one observes that $p\phi$ is a lift of $qp\phi$, while $p$ is a lift of $qp$. Both $p\phi$ and $p$ send $x$ to $y$, so by the uniqueness of lifts, they must actually be equal. Thus $p\phi = p$ is a deck transformation with respect to $X\to Y$, which sends $x$ to $x'$. The bugfix is to look at connected components of $X$. Suppose $x\in C$ and $x'\in C'$, where $C$ and $C'$ are connected components of $X$. $\phi$, as a homeomorphism, performs a permutation on the connected components which sends $C$ to $C'$. $p\phi:C\to Y$ is a lift of $qp\phi:C\to Z$ and $p:C\to Y$ is a lift of $qp:C\to Z$. Both send $x$ to $y$, so they must be equal. 
>  
>  
>  
>  -  If $C = C'$, the desired deck transformation is obtained by performing $\phi$ on $C$ and leaving $X\setminus C$ fixed. 
>  
>  -  If $C\neq C'$, then use $\phi$ on $C$, $\phi^{-1}$ on $C'$, and leave $X\setminus (C\cup C')$ fixed. 
>  
>  We conclude. 


> [!problem] Universal Abelian Covering Space
Given ==*unloopable*== space $X$, call a path-connected covering space $\tilde{X}$ ==**abelian**== if it is normal and $G(\tilde{X})$ is abelian. Show that $X$ has an abelian covering space $\tilde{X}$, unique up to isomorphism, that satisfies the following universal property: $\tilde{X}$ is a cover of every other abelian covering space of $X$. 


> [!solution]-
Let $G = \pi_1(X, x_0)$. Your intuition should be to find the *smallest* normal subgroup $N$ of $G$ such that $G/N$ is abelian. But we already have this; it's called $N = [G,G]$. The details: for normal covering spaces with $\pi_1(\tilde{X}) \cong N$, $G(\tilde{X}) \cong G / N$, so $\tilde{X}$ is abelian iff $G/N$ is. Pick the $\tilde{X}$ corresponding to $N = [G,G]$. For any other abelian covering space $\tilde{X}'$ with projection map $\pi:G\to G/N'$, $[G,G]\subset \ker \pi = N'$, thus $\tilde{X}$ is a cover of $\tilde{X}'$. This is unique up to isomorphism because of the universal property.