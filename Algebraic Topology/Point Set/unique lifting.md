This, combined with the [[lifting criterion]] describe how one can lift arbitrary maps.
> [!theorem] Unique Lifting Property
 Suppose two lifts $\tilde{f}_1, \tilde{f}_2: Y\to \tilde{X}$ of $f$ agree at one point $y\in Y$, and $Y$ is ==*connected*==. Then $\tilde{f}_1 = \tilde{f}_2$. 

> [!proof]- 
 Note that we didn't say $Y$ was path-connected, but we clearly need to use the connectedness condition. Thus, there is exactly one way to proceed: we need to show $\{y: \tilde{f}_1(y) = \tilde{f}_2(y)\}$ is both open and closed. There is also only one way for two lifts to be distinct, which is for them to be in separate branches. So let's just zoom in on that. For *any* point $y\in Y$, we should pick an evenly covered open neighborhood $U$ of $f(y)$, then let $\tilde{U}_1$ and $\tilde{U}_2$ be the sheets containing $\tilde{f}_1(y)$ and $\tilde{f}_2(y)$ respectively. By continuity, there is a neighborhood $N$ of $y$ which is mapped into $\tilde{U}_1$ by $\tilde{f}_1$ and into $\tilde{U}_2$ by $\tilde{f}_2$. Then: 
>  
>  
>  
>  -  If $\tilde{f}_1(y) = \tilde{f}_2(y)$, then $\tilde{U}_1 = \tilde{U}_2$, and $p$ is a homeomorphism from $\tilde{U}_1 = \tilde{U}_2$ to $U$, so $\tilde{f}_1 = \tilde{f}_2$ on $N$. 
>  
>  -  If $\tilde{f}_1(y) \neq \tilde{f}_2(y)$, then $\tilde{U}_1 \neq \tilde{U}_2$, so actually $\tilde{f}_1(N)$ and $\tilde{f}_2(N)$ are disjoint. In particular, they are not equal on $N$. 
>