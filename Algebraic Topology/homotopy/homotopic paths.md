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