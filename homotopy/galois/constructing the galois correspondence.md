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
First, we'll go all the way to the top of the chain, by constructing the covering space corresponding to the subgroup $\{1\}$. Such a space must be simply-connected.

> [!theorem] Universal Cover
  Given an [[unloopable]] space $X$ with a basepoint $x_0\in X$, there exists a simply-connected covering space $\tilde{X}$ of $X$ called the ==**universal cover**==.

> [!idea] 
Suppose $x\in X$ has a neighborhood $U$ for which the inclusion $\pi_1(U,x)\to \pi_1(X,x)$ is trivial. Then, $U$ is called ==**semilocally simply-connected**==. Equivalently, all loops inside $U$ are contractible in $X$. Contrast this with the notion of locally simply-connected spaces, where all loops inside $U$ are contractible in $U$. If all points in $x$ admit a semilocally simply-connected neighborhood, then $X$ is called ==**semilocally simply-connected**==. In any case, this condition is clearly necessary; each point $x\in X$ must have an evenly-covered neighborhood, and if $\tilde{X}$ is to be simply-connected then that neighborhood must be semilocally simply-connected.

 Let's construct this thing. 
 
> [!proof]-
 \todo{Fill out the details of this long-ass proof.} The *set* $\tilde{X}$ is $$ \tilde{X} = \{[\gamma]: \gamma \text{ is a path in $X$ starting at $x_0$}\} $$ The function $p:\tilde{X}\to X$ sending $[\gamma]$ to $\gamma(1)$ is surjective, because $X$ is path-connected. Great. We want to put the most natural possible topology on this guy. 
> > [!part]- Finding a Basis for $X$
>  Let $\mathcal{U}$ be the collection of path-connected semilocally simply-connected open sets $U\subset X$. Then, for each $U\in \mathcal{U}$, we have a trivial map $\pi_1(U)\to \pi_1(X)$, which is independent of the basepoint chosen in $U$. For any path-connected subspace $V\subset U$, the inclusion $\pi_1(V)\to \pi_1(U)\to \pi_1(X)$ is also guaranteed to be trivial, so $V\in \mathcal{U}$ as well. $X$ is locally path-connected, so the collection of path-connected open sets forms a basis for the topology of $X$. Thus $\mathcal{U}$ is a basis as well. 
> 
>  
> > [!part]- Finding a Basis for $\tilde{X}$
>  Given any $U\in \mathcal{U}$ and path $\gamma$ from $x_0$ to a point in $U$, let $$ U_{[\gamma]} = \{[\gamma\eta] | \eta \text{ is a path in $U$ with $\eta(0) = x_0$}\} $$ This is clearly well-defined. Also, $p:U_{[\gamma]}\to U$ is bijective. Finally, $U_{[\gamma]} = U_{[\gamma']}$ if $[\gamma']\in U_{[\gamma]}$. We claim these form a basis. Well, for any $[\rho]\in U_{[\gamma]}\cap V_{[\eta]}$, $U_{[\rho]} = U_{[\gamma]}$ and $V_{[\rho]} = V_{[\eta]}$. $\mathcal{U}$ was a basis, so we can pick $W\in \mathcal{U}$ inside $U\cap V$, and choose $W_{[\rho]}$ as our basis element. 
> 
>  Thus, the bijective $p$ from before is a homeomorphism from $U_{[\gamma]}$ to $U$, and in particular $p$ is continuous. It is also a covering space. Then we show $\tilde{X}$ is simply connected. 

 Awesome. The key idea to finishing the Galois Correspondence will be to *identify points* using the *discrete data of* $p^{-1}(x_0)$. 
> [!theorem] Galois Correspondence Part 0
> Suppose $X$ is unloopable. For every subgroup $H\subset \pi_1(X, x_0)$, there is a covering space $p:(X_H,\tilde{x}_0) \to (X, x_0)$ such that $p_*(\pi_1(X_H, \tilde{x}_0)) = H$. 

 
> [!proof]-
 \todo{Write in details blah} Let $X_H$ be $\tilde{X}$ modulo the relation $[\gamma]\sim [\gamma']$ if $\gamma(1) = \gamma'(1)$ and $[\gamma \conj{\gamma'}]\in H$. We claim $X_H$ is still a covering space via $p:[\gamma]\to \gamma(1)$. This is because for all $\eta$ and $[\gamma]\sim [\gamma']$, $[\gamma] = [\gamma']$ iff $[\gamma\eta] = [\gamma'\eta]$. Let $\tilde{x}_0\in X_H$ be the equivalence class of the constant path $[1]$ at $x_0$. The image of $p_*(\pi_1(X_H, \tilde{x}_0))$ are those loops in $X$ whose lifts remain loops; thus a $\gamma \in X$ is in the image iff $[\gamma]\sim [1]$ i.e. $[\gamma]\in H$. 

> [!idea] 
 After constructing the universal cover you won't ever need the construction again; it has the universal property. For instance, you won't need it on the following problem, which is mostly about arrow chasing.

> [!problem] 
 Let unloopable $X,Y$ admit universal covers $\tilde{X}$ and $\tilde{Y}$. Show that if $X\simeq Y$, then $\tilde{X}\simeq \tilde{Y}$. 

 \todo{Insert diagram} 
 
> [!solution]-
 Let $f:X\to Y$ be our homotopy equivalence with $fg = gf = 1$. Observe that $f\circ p_x : \tilde{X}\to X$ has trivial image in the fundamental group, and thus admits a lift $\tilde{f}$. (We create a basepoint for this step then immediately forget about it). Similarly, let $p_x\circ \tilde{g} = g\circ p_y$. Observe that at ground level we have $g f p_x\simeq p_x$. $g f p_x$ lifts to $\tilde{g} \tilde{f}$ (by a brief arrow chase), thus we can lift this entire homotopy to a homotopy from $\tilde{g} \tilde{f}$ to some $\phi$. Please be careful in this step! We know that $\id$ is a lift of $p_x$, so we'd be tempted to celebrate immediately, but homotopy lifting only lets us fix one end of the interval. We now need to show $\phi \simeq 1$. We know that $p_x \circ \phi = p_x$; in more humane terms, $\phi$ preserves the fibers of $p_x$. Thus, for any fixed $\tilde{x}\in \tilde{X}$, I can find some deck transformation $\Psi$ which undoes $\Psi\circ \phi(x) = x$. Yet clearly $\Psi\circ \phi$ is yet another lift of $p_x$! By the unique lifting property, $\Psi\circ \phi = 1$ over *all* of $\tilde{X}$. Thus, $\Psi \tilde{g} \tilde{f} \simeq \Psi \phi = 1$. Running this argument a second time concludes. 

 In practice, nobody really uses the above constructions. People just draw the covering spaces they desire and show that they work. After we discuss some more theory, we'll be able to do this too. 
 
> [!problem] 
 Let $a$ and $b$ be the generators of $\pi_1(S^1\vee S^1)$ as usual. Determine the covering space corresponding to the normal subgroup $N(\langle a^2, b^2, (ab)^4\rangle)$ by hand (no theorems, but you should verify it's correct!) 

 \todo{Draw diagram} 
 
> [!solution]-
 The desired covering space looks like $8$ circles joined in a loop. It is a covering space by inspection. The basepoint $x_0$ is lifted to $8$ points, thus the degree of $\pi_1(\tilde{X}, \tilde{x}_0)$ in $\pi_1(X, x_0)$ is $8$. Finally, observe that $a^2, b^2, (ab)^4$ lie in this subgroup. There is exactly one normal subgroup of index $8$ which contains these elements, thus we are done. 
