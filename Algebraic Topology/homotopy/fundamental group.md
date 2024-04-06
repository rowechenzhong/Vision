The key idea of homotopy theory is that one can construct a group out of loops. 
> [!definition] 
The ==**fundamental group**== of a space $X$ based at $x_0$ as the group of homotopy classes of loops based at $x_0$. This is denoted $\pi_1(X, x_0)$. In particular: 
>  
>  
>  
>  -  The identity element is the loop $p(t)=x_0$. 
>  
>  -  The inverse of a loop $p$ is the loop $q(t)=p(1-t)$. 
>  
>  -  The product of two loops $p$ and $q$ is the loop $$ (p\star q) = \begin{cases} p(2t)   & \text{if } t\leq \frac{1}{2} \\ q(2t-1) & \text{if } t>\frac{1}{2} \end{cases} $$ 
>  
>  To distinguish the equivalence classes from the paths, we denote the group element corresponding to path $p$ as $[p]$. 

Observe some trivialities: 

-  Suppose $x_0$ and $x_1$ are path-connected by $\gamma$. Then, via conjugation by $\gamma$, $\pi_1(X, x_0)\cong \pi_1(X, x_1)$. 

-  A space $X$ is ==**simply connected**== if $\pi_1(X, x_0)=1$ for all $x_0 \in X$. This is *stronger* than being path-connected; you also can't have any holes. 


> [!idea] 
Originally, my intuition was to \"drop all the basepoints,\" but it seems like they encode a certain *discrete* amount of information which is useful for algebraic topology. Just bear with me; they're useful, and you need to pay attention to them. 

Now, how do these groups interact with maps? 
> [!theorem] Continuous Maps yield Homomorphisms
Let $f: X\to Y$ be a continuous map between two spaces. Then $f$ induces the natural map on loops $$ p\mapsto f\circ p $$ This in turn generates a homomorphism, which we will forever denote $$ f_* : \pi_1(X, x_0)\to \pi_1(Y, f(x_0)) $$ via $$ [p]\mapsto [f\circ p] $$ 


> [!problem] 
Show that the above map $p\mapsto f\circ p$ generates a well-defined homomorphism $\pi_1(X, x_0)\to \pi_1(Y, f(x_0))$. 


> [!solution]-
Observe that our function acts on *equivalence classes* of loops. To show that this is well-defined as a function, we need to show that if $\gamma \simeq \delta$ in $X$, then $f\circ \gamma \simeq f\circ \delta$ in $Y$. This is obvious though; see a previous question. This function now obviously preserves identities, inverses, and composition. 


> [!idea] 
There is an additional nice property we might want this function to have: if $p$ in $X$ gets sent to $f\circ p$, and I have another loop $q'$ in $\tilde{X}$ which is homotopic to $f\circ p$, then there should exist some loop $q$ in $X$, homotopic to $p$, such that $f\circ q = q'$. In other words, you might want $$ f([p]) = [f\circ p] $$ *as sets*. Unfortunately, this is cap; let $Y$ be the interval, and let $f$ be the constant map to $0$. The good thing about *covering maps* (which we'll get to in a bit!) is that they *do* have this property. 


> [!theorem] Homotopic Maps and Homomorphism behave identically
Suppose $f,g: (X,x_0)\to (Y, y_0)$ such that $f\simeq g$. Then $f_*=g_*$. Suppose $h : (Y, y_0)\to (Z, z_0)$. Then, $h_*\circ f_* = (h\circ f)_*$. In particular, if $f$ is a homotopy equivalence, then $f_*$ is an isomorphism. 


> [!proof] 
For any loop $\gamma$ at $x_0$, $f^*([\gamma]) = g^*([\gamma])$ iff $f(\gamma) \simeq g(\gamma)$, but this is just a composition of homotopies. The second statement is by definition; for any curve $\gamma$, $$ (h_*\circ f_*)([\gamma]) = h_*([f\circ \gamma]) = [h\circ f\circ \gamma] = (h\circ f)_*([\gamma]) $$ If $f:(X,x_0)\to (Y, y_0)$ is a homotopy equivalence, then there exists a $g: (Y, y_0)\to (X, x_0)$ such that $g\circ f \simeq \id_X$ and $f\circ g \simeq \id_Y$. Then, $f_*\circ g_* = (\id_X)_* = \id_{\pi_1(X, x_0)}$ and $g_*\circ f_* = (\id_Y)_* = \id_{\pi_1(Y, y_0)}$. So $f_*$ is an isomorphism (with inverse $g_*$). 

Suppose $X$ deformation retracts onto $A\subset X$. Just like any other continuous map, the inclusion map $i:A\to X$ induces a homomorphism $\pi_1(A,x_0)\to \pi_1(X,x_0)$ for $x_0\in A$. For any loop $\gamma \simeq 1$ in $\pi_1(X,x_0)$, there exists the required homotopy $\gamma_t: I\to X$; but then $i\circ \gamma_t$ induces a homotopy $\gamma\simeq 1$ in $\pi_1(A, x_0)$. Thus $i^*$ is an *injective* homomorphism. As a corollary, $D^2$ does not retract onto its boundary, for instance.
## A word on graphs 


> [!example] Modding out a Tree
For a tree $T$ that is a subgraph of a connected graph $G$, the projection $G\to G/T$ is homotopy equivalence.