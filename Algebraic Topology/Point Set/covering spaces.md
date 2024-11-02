The main motivating example is the computation of $\pi_1(S^1)$. 
> [!example] Circle
 We're going to try to compute $\pi_1(S^1)$. Let $p: \RR\to S^1$ be the map $t\to e^{2\pi i t}$. While circles are complicated, $\RR$ should be the easiest space possible. Now, given any point $x_0\in S^1$ and small open neighborhood $x_0 \in U = (a,b)$, consider the pre-image $p^{-1}(U)$. If $U$ is sufficiently small, then $p^{-1}(U)$ is a disjoint union of open intervals, each of which is homeomorphic to $U$ by $p$. So we're in a branch-cut type situation. If I want to do any local operation inside of $U$, as long as I *pick* which pre-image of $U$ to work in, I can do it. 

Let me now describe the general situation. 
> [!definition] Covering Space
 We are given a map $p: \tilde{X}\to X$. An open set $U\in X$ is ==**evenly covered**== if $p^{-1}(U)$ is a disjoint union of open sets in $\tilde{X}$, each of which is mapped homeomorphically onto $U$ by $p$. Those open sets are called ==**sheets**==, and the preimage $p^{-1}(x_0)$ is called the ==**fiber**==. Then, if every $x\in X$ has an evenly covered neighborhood, we say that $p$ is a ==**covering map**== and $\tilde{X}$ is a ==**covering space**== of $X$. For any function $f: Y\to X$, we say that $\tilde{f}: Y\to \tilde{X}$ is a ==**lift**== of $f$ if $p\circ \tilde{f} = f$. 
 
> [!idea] 
 The key idea of covering spaces: 
>  
>  -  $\tilde{X}$ is a space that is *locally homeomorphic* to $X$. Thus, after *fixing the branch* of $p^{-1}(U)$, maps like paths can be lifted to $\tilde{X}$. 
>  
>  -  However, $\tilde{X}$ is *globally different* from $X$. By tracing lifting entire path from $X$ to $\tilde{X}$, we can detect this. 
>