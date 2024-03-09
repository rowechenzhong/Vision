Alright, things are getting interesting now. 

> [!example] Kernel
 Let's look at $C_\infty([0,1])$, the continuous bounded functions on $[0,1]$ (bounded is redundant). Let $K:[0,1]^2 \to \RR$ be a continuous function. Then, we can define an operator $$ Tf(x) = \int_0^1 K(x,y)f(y) \der y $$ $K$ is called the ==**kernel**== of $T$. This is linear! 

 We are particularly interested in *continuous* linear operators, defined in the usual manner. By linearity and things, this turns out to be really strong. 
 
> [!definition] Operators
 The ==**operator norm**== on $T:V\to W$ is defined $$ \norm{T} = \sup_{v\in V : \norm{v} = 1} \norm{Tv}_W = \sup_{v\in V} \frac{\norm{Tv}_W}{\norm{v}_V} $$ An operator is ==**bounded**== if this norm is not infinite. The space of ==**bounded**== linear operators from $V$ to $W$ is denoted $\BB(V,W)$. 

>[!idea]
You might notice that this is analogous to the $\infty$-norm. The analogous $p$-norms are called the [[Schatten Norm]].

> [!problem] 
 A linear operator $T: V\to W$ is continuous iff there exists $C > 0$ such that $\norm{Tv}_W\leq C\norm{v}_V$ for all $v\in V$, i.e. it is bounded.

> [!solution]-
 Suppose $T$ is continuous. Then, the ball $B = \{v : \norm{v} < 1\}$ is by definition open. Thus the preimage $T^{-1}(B)$ is open, and contains $0$. Thus there exists some $\delta > 0$ such that $B_\delta(0) \subseteq T^{-1}(B)$. Thus we can pick $C$ = $1/\delta$, because one can scale any vector so its norm is $1 / \delta - \eps$, and then $Tv$ is at most $1$. 
> > [!idea] 
>  On the other hand, taking $\delta$ to be the supremum of possible $\delta$, this $C = 1/\delta$ is maximal. 
> 
>  Suppose now that $T$ is bounded. Over metric spaces, continuity is equivalent to sequential continuity. Thus, pick some sequence $\{v_n\}\to v$ in $V$; we observe that $$ \norm{Tv_n - Tv}_W = \norm{T(v_n - v)}_W \leq C\norm{v_n - v}_V $$ The RHS vanishes, thus by squeeze theorem the LHS vanishes in the limit, as desired. 

 For example, observe that the above $T$ was bounded by $C = \sup_{x,y\in [0,1]} \abs{K(x,y)}$, and thus automatically continuous. 
 
> [!problem] 
 Show that $\BB(V,W)$ is a normed space under the operator norm. 

> [!solution]-
 First, we should show that $\BB(V,W)$ is a vector space. This is clear from triangle inequality on $W$, etc. Next, we want the operator norm to be a norm. 
>  
>  
>  
>  -  The norm is definite because if $\norm{Tv}$ is identically $0$ then $T$ is identically $0$. 
>  
>  -  Homogeneity follows from $$ \norm{\lambda T} = \sup_{v\in V: \norm{v} = 1} \norm{\lambda Tv} = \abs{\lambda} \sup_{v\in V: \norm{v} = 1} \norm{Tv} = \abs{\lambda} \norm{T} $$ 
>  
>  -  Triangle inequality follows from $$ \norm{T + S} = \sup_{v\in V: \norm{v} = 1} \norm{(T+S)v} \leq \sup_{v\in V: \norm{v} = 1} \norm{Tv} + \norm{Sv} \leq \norm{T} + \norm{S} $$ 
>  
>  
> > [!idea] 
> Observe that all properties followed from the norm on $W$, not $V$. We expect the topological properties of $\BB(T,W)$ to be heavily dependent on $W$.
> 
>  

 Now, the main thing to update your intuition on is that **we only care about bounded (i.e. continuous) linear maps.** This causes a lot of vanilla linear algebra to fail. 
 
> [!example] Injective $\centernot\implies$ Invertible
 In the space $\ell^2$ of square summable sequences, the operator $$ Ta = \left\{ \frac{a_1}{1}, \frac{a_2}{2}, \frac{a_3}{3}, \dots \right\} $$ is continuous and injective, but not surjective. For instance, it cannot hit the sequence $b = (1, 1/2, 1/3, \dots)\in \ell^2$. Thus $T$ is not invertible. This shows injectivity does not imply invertibility.

>[!example] Invertible $\centernot\implies$ what you think it means
> If we work over $\ell^\infty$, then the above function is continuous, injective, and surjective. It is a logical fact that this implies the function has an inverse; in our case it is $$ T^{-1}a = \left\{ a_1, 2a_2, 3a_3, \dots \right\} $$. However this is clearly not bounded. So the definition of an invertible operator is that it must be a homeomorphism as well; its inverse must also be continuous.

We do have one saving grace; invertibility works as expected over [[banach|Banach spaces]]. See [[zabreikos]]!

> [!problem] 
 An operator $T\in \BB(V,W)$ is ==**isometric**== if it preserves the norm. Show that isometric operators must be injective. 
 
> [!solution]-
 This is trivial.