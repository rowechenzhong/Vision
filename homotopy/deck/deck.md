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
# Deck Transformations 

We will continue exploring the nuances of the Galois correspondence. 
> [!definition] Deck Transformation
A ==**deck transformation**== is a homeomorphism $\phi: \tilde{X}\to \tilde{X}$ such that $p\circ \phi = p$. 

These are automorphisms (in the covering space sense) from $\tilde{X}$ to itself. The word \"deck\" is pretty good; I visualize $\tilde{X}$ as a deck of cards, and $\phi$ as a shuffling of the deck. Look at the pancake picture; its a permutation on every fiber. The set of all deck transformations is a group denoted $G(\tilde{X})$. As is thematic, we observe that such deck transformations encode discrete information in their action on fibers. In fact, this is basically as good as you can possibly expect: 



-  For ==*pc spaces*==, by the *unique lifting property,* a deck transformation $\phi$ is uniquely determined by where it sends a single point. For instance, $\phi$ has a fixed point iff it is the identity. 

-  Let $\{\tilde{x}_0, \tilde{x}_1\} \in p^{-1}(x)$. For ==*pc lpc spaces*==, by the *lifting criterion,* a deck transformation sending $\tilde{x}_0$ to $\tilde{x}_1$ exists if and only if $$ p_*(\pi_1(\tilde{X}, \tilde{x}_0)) = p_*(\pi_1(\tilde{X}, \tilde{x}_1)) $$ 

We can single out an especially symmetric class of covering spaces. 
> [!definition] Regular Covering Space
\label{defn:regular} A covering space $p: \tilde{X}\to X$ is ==**regular**== if for each $x\in X$, and each $\{\tilde{x}_0, \tilde{x}_1\}\in p^{-1}(x)$, there exists a deck transformation sending $\tilde{x}_0$ to $\tilde{x}_1$. Such a covering space is also called a ==**normal**== covering space. This is because a covering space is normal iff $H = p_*(\pi_1(\tilde{X}, \tilde{x}_0))$ is a normal subgroup of $\pi_1(X, x_0)$! 


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

This problem is a useful tool in conjunction with \href{ex:chaining}{the chaining lemma}. 
> [!solution] 
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


> [!solution] 
Let $G = \pi_1(X, x_0)$. Your intuition should be to find the *smallest* normal subgroup $N$ of $G$ such that $G/N$ is abelian. But we already have this; it's called $N = [G,G]$. The details: for normal covering spaces with $\pi_1(\tilde{X}) \cong N$, $G(\tilde{X}) \cong G / N$, so $\tilde{X}$ is abelian iff $G/N$ is. Pick the $\tilde{X}$ corresponding to $N = [G,G]$. For any other abelian covering space $\tilde{X}'$ with projection map $\pi:G\to G/N'$, $[G,G]\subset \ker \pi = N'$, thus $\tilde{X}$ is a cover of $\tilde{X}'$. This is unique up to isomorphism because of the universal property. 

## General Actions 

We now generalize the notion of a deck transformation to arbitrary actions on a space. 
> [!definition] Action
An ==**action**== of a group $G$ on a space $Y$ is simply a homomorphism $\rho: G\to Homeo(Y)$; think representation theory. We want $\rho$ to have the \"discreteness\" characteristic of deck transformations. Each $y \in Y$ should have a neighborhood $U$ such that $g_1(U)\cap g_2(U) \neq \emptyset$ implies $g_1 = g_2$ (In particular, $\rho$ is injective.) Such actions will be called ==**covering space actions**==. 

In particular, deck transformations are covering space actions, and wlog we can take $g_2 = 1$ in the definition. 
> [!theorem] Orbit Spaces
Of course, we can define ==**orbits**== for our action $Gy = \{g(y) \mid g\in G\}$. Then, $Y / G$ is called the ==**orbit space**==. In a normal covering space the orbits span the fibers, so $\tilde{X} / G(\tilde{X}) = X$. The important points: 
>  
>  
>  
>  -  $p: Y\to Y/G$ via $p(y) = Gy$ is a normal covering space. 
>  
>  -  If $Y$ is ==*pc*==, $G = G(Y)$ is the group of deck transformations. 
>  
>  


> [!proof] 
For any $y\in Y / G$, let's look at an element $\tilde{y}\in p^{-1}(y)$. By the definition of a covering space action, I can find a neighborhood $U$ of $y$ such that $p^{-1}(U)$ is a disjoint set of open sets, each of which is mapped homeomorphically to one another, and thus to $U$ as well. In other words, $U$ is evenly covered. This covering space is obviously normal, because two elements of $Y$ are in the same fiber iff they are in the same orbit iff there exists a deck transformation sending one to the other. Clearly $G$ is a subgroup of the group of all possible deck transformations. If $Y$ is pc, then consider any $y\in Y$ and deck transformation $f$. Then $f(y)$ is in the same fiber as $y$, so $f(y) = gy$ for some $g\in G$. $Y$ is pc, thus $f = g$. 

In particular, if $Y$ is also lpc, then $G\cong \pi_1(Y/G) / p_*(\pi_1(Y))$. 
> [!idea] 
Orbit spaces and covering space actions are a \"top-down\" approach to covering spaces. They feel different than our previous constructions, because in our previous constructions everything was based off of $X$; all the subgroups were subgroups of $\pi_1(X)$, and all the spaces were covering spaces of $X$. If you're considering subgroups of a fixed group $\pi_1(X)$, somehow this poset appears much more finite and reasonable. (Of course, this is imagined; the structure of the subgroups of $Z\ast Z$ is immense.) In any case, in order to get the groups to talk to each other in computations, you need to go down to the bottom of the poset, and perform computations in that \"largest\" group. 


> [!problem] 
Let $G$ be a CSA on a ==*pc, lpc*== space $X$. Each subgroup $H\subset G$ determines a composition of covering spaces $X\to X/H \to X/G$. Let us analyze this correspondence. 
>  
>  
>  
>  -  *Any* ==*path-connected*== space $Y$ such that $X\to Y\to X/G$ is a covering space is isomorphic to $X/H$ for some $H\subset G$. 
>  
>  -  Consider two ==*path-connected*== covering spaces $X/H_1$ and $X/H_2$ of $X/G$. Show these are isomorphic iff $H_1$ and $H_2$ are conjugate subgroups of $G$. 
>  
>  -  Show that $X/H \to X/G$ is normal iff $H \trianglelefteq G$. In this case, show the group of deck transformations is $G/H$. 
>  
>  


> [!idea] 
[Group Theory] Here are the relevant group-theoretic observations: 
>  
>  
>  
>  -  Suppose $N\trianglelefteq G$ and $N\trianglelefteq H$. If $H\subset G$, then $H/N \subset G/N$. 
>  
>  -  Suppose $N,A,B$ are subgroups of $G$, $N\trianglelefteq A$, $N\trianglelefteq B$, and $N\trianglelefteq G$. Then $A$ is conjugate to $B$ in $G$ iff $A/N$ is conjugate to $B/N$ in $G/N$. 
>  
>  -  Suppose $N\trianglelefteq H \subset G$ and $N\trianglelefteq G$. Then $H\trianglelefteq G$ iff $H/N \trianglelefteq G/N$, in which case $G/H \cong (G/N) / (H/N)$. 
>  
>  


> [!solution] 
The first observation is hidden. If $G$ is a CSA, then $X\to X/G$ is a *normal* covering space! Thus by the chaining lemmas, $X\to Y$ is a normal covering space as well, and $Y = X / H$ for some CSA $H$. Well, $$ H = \pi_1(Y) / p_*(\pi_1(X)),\qquad G = \pi_1(X/G) / p_*(\pi_1(X)) $$ $Y$ is a cover of $X/G$, so $\pi_1(Y) \subset \pi_1(X/G)$, thus $H\subset G$. Next, observe that $X/H_1$ and $X/H_2$ are isomorphic covering spaces of $X/G$ iff $\pi_1(X/H_1)$ and $\pi_1(X/H_2)$ are conjugate, by the Galois correspondence. But this is true iff $\pi_1(X/H_1) / \pi_1(X)$ is conjugate to $\pi_1(X/H_2) / \pi_1(X)$ in $\pi_1(X/G) / \pi_1(X)$! Finally, $X/H \to X/G$ is normal iff $\pi_1(X/H) \trianglelefteq \pi_1(X/G)$ by the Galois correspondence. But $H = \pi_1(X/H) / \pi_1(X)$ and $G = \pi_1(X/G) / \pi_1(X)$, so this is equivalent to $H\trianglelefteq G$. The group of deck transformations is then $\pi_1(X/G) / \pi_1(X/H) = G/H$. To see this last point explicitly: all normal sequences of this form actually have a special deck structure. Each deck transformation is a permutation on the fibers of the fiber of $x_0$. Pick some specific $x_0\in X/G$ shooting up to $\tilde{x}_0, \tilde{x}_1, \dots \in X/H$. Suppose $\tilde{x}_i$ lifts to $\tilde{x}_{ij}$ in $X$. Then, any deck transformation must \"factorize\" in the sense that if $\tilde{x}_{i1}$ is sent to $\tilde{x}_{ab}$, then $\tilde{x}_{ij}$ are all sent to $\tilde{x}_{ac}$ for some $c(j)$. This can be seen combinatorially after drawing some diagrams. 


> [!problem] Shared Universal Cover
Suppose $Y$ is pc, lpc, and simply-connected. Let $G_1$ and $G_2$ be subgroups of $Homeo(Y)$ which are CSA on $Y$. This means $p_1: Y\to Y/G_1$ and $p_2: Y\to Y/G_2$ are normal covering spaces. 
>  
>  
>  
>  -  Show that if $Y/G_1$ and $Y/G_2$ are homotopic, $G_1\cong G_2$. 
>  
>  -  Show that $Y/G_1$ and $Y/G_2$ are homeomorphic and one can find a homeomorphism $\phi: Y/G_1 \to Y/G_2$ such that $p_2 g = \phi \circ p_1$, if $gG_1g^{-1} = G_2$ are conjugate subgroups of $Homeo(Y)$. 
>  
>  


> [!solution] 
If $Y/G_1$ and $Y/G_2$ are homotopic, so $$ G_1 \cong \pi_1(Y/G_1) / \pi_1(Y) \cong \pi_1(Y/G_2) / \pi_1(Y) \cong G_2 $$ On the other hand, the map $p_2 g$ sends $y$ to $gG_1 y$, and thus factors through $p_1$ to yield $g_Y: Y/G_1 \to Y/G_2$ sending $G_1 y$ to $gG_1 y$. Repeating the opposite direction, this is a homeomorphism. 





































