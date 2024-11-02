---
aliases: []
---
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