# Paths
> [!definition] Homotopic
 Two [[path|paths]] $p$ and $q$ from $x_0$ to $x_1$ in a space $X$ are ==**homotopic**== if there exists a continuous function $F: I\times I\to X$ such that $F(0, t)=p(t)$, $F(1, t)=q(t)$, $F(t,0) = x_0$, and $F(t,1) = x_1$ for all $t\in I$. 
 
![[homotopy.png]]
> [!problem] 
 Show that this is an equivalence relation. 

> [!solution]-
> All paths $p$ are homotopic to themselves $F(t,s) = p(s)$. If $F(t,s)$ is a homotopy between $p$ and $q$, then $F(1-t,s)$ is a homotopy between $q$ and $p$. Finally,
> if $F(t,s)$ and $G(t,s)$ are homotopies from $p$ to $q$ and $q$ to $r$, then the function which is $F(2t, s)$ for $t \leq \frac12$ and $G(2t-1, s)$ for $t \geq \frac12$ is a homotopy from $p$ to $r$.

 We thus speak of ==**homotopy classes**== of paths from $x_0$ to $x_1$. In addition to throwing away the parameterization, we also throw away irrelevant local decisions in choosing our path. Thus, these classes are far more important than the paths themselves. This occurs in higher generality. A key idea of homotopy theory is to "throw away" suitably local decisions in a continuous function to obtain a homotopy class. Then, these homotopy classes will be amenable to studying the global structure of the space. 

# Maps 

> [!definition] Homotopic Maps
 Two maps $f_0$ and $f_1$ from $X$ to $Y$ are ==**homotopic**==, denoted $f_0\simeq f_1$, if there exists a continuous map $F: X\times I\to Y$ such that $F(x, 0)=f_0(x)$ and $F(x, 1)=f_1(x)$ for all $x\in X$. 

 
> [!idea] 
 If $X,Y$ are [[pointed spaces|pointed]], i.e. $f_0, f_1: (X, x_0)\to (Y, y_0)$, then we require $F(x_0, t) = y_0$ for all $t\in I$. This generalizes to multiple points. In the case of path homotopies, $x_\alpha \in \{0,1\}$ were special, for instance. 

 Now, we should take some time to prove that homotopic maps, as an equivalence relation, behave exactly as desired within the algebra of continuous maps. 
> [!problem] Everything Works
> Show that: 
>  -  $\simeq$ is an equivalence relation (this should be identical to the path case). 
>  
>  -  If $f_0, f_1 : X\to Y$ are homotopic, for all $g:Y\to Z$ and $h:W\to X$, we have $g\circ f_0 \simeq g\circ f_1$ and $f_0\circ h\simeq f_1\circ h$. 
>  
>  

> [!solution]- 
 $f\simeq f$, because one can pick $F(x,t) = f(x)$. $f\simeq g \implies g\simeq f$, because one can pick $G(x,t) = F(x, 1-t)$. If $f_0\simeq f_1$ via $F(x,t)$ and $f_1\simeq f_2$ via $G(x,t)$, then $f_0\simeq f_2$ via $H(x,t) = F(x, 2t)$ for $t\in [0,1/2]$ and $H(x,t) = G(x, 2t-1)$ for $t\in [1/2, 1]$. Thus, we can speak of homotopy equivalence classes of maps $X\to Y$. Now, suppose $f_0\simeq f_1$ via $F(x,t)$. Then $gf_0 \simeq gf_1$ via $G(x,t) = g(F(x,t))$, and $f_0h\simeq f_1h$ via $H(x,t) = F(h(x), t)$. All of the above is true for pointed spaces as well; the worldline of the basepoint is fixed. 






































