> [!theorem] Lifting Property
 Suppose you are given a map $F:Y\times I \to X$. I give you a a branch-cut / \"initial condition\" $\tilde{F}: Y\times \{0\} \to \tilde{X}$, which is a lift of $F$ over $Y\times \{0\}$. Then $\tilde{F}$ can be extended to a unique lift $\tilde{F}: Y\times I \to \tilde{X}$. 
 
> [!proof]-
> Fix $y_0$. For all $t\in I$, by definition of covering space, there exists an evenly-covered open neighborhood of $F(y,t)$; by the product topology, we can take it to be of the form $U\times (a,b)$. Now, $\{y_0\} \times I$ is compact. Thus, there exists a neighborhood $y_0\subset N$ and a finite partition $0 = t_0 < t_1 < \cdots < t_m = 1$ of $I$ such that for each $i$, $F(N\times [t_i, t_{i+1}])$ is contained in some evenly-covered neighborhood. Each one of these $m$ blocks is homeomorphically mapped via $p^{-1}$, with branch cut given inductively. This construction uniquely determines $\tilde{F}(N\times I)$, by inspection. Repeat for all $y_0\in Y$. By uniqueness of the previous construction, all such $\tilde{F}(N\times I)$ agree on their overlaps. Thus we conclude. 

This generalizes to the [[lifting criterion]] and [[unique lifting]] property. 

> [!example] Lifting a Path
 Suppose $Y$ is a point. Then, the statement is: for any path $f: I\to X$ starting at $x_0$, and any selection of $\tilde{x}_0\in p^{-1}(x_0)$, there exists a unique lift $\tilde{f}: I\to \tilde{X}$ starting at $\tilde{x}_0$. 

 
> [!example] Lifting a Homotopy
 For any homotopy $f_t: I\to X$ of paths starting at $x_0$, and each $\tilde{x}_0\in p^{-1}(x_0)$, there exists a unique lifted homotopy $\tilde{f}_t: I\to \tilde{X}$ starting at $\tilde{x}_0$. This is true, because we can write $F(x,t) = f_t(x)$. Then, $F(x,0)$ can be uniquely lifted by the previous theorem. We apply this theorem a second time to lift $F(x,t)$ to $\tilde{F}(x,t)$. To verify that $\tilde{F}(0,t)$ and $\tilde{F}(1,t)$ are constant (as required for path homotopies), we note that $F(0,t)$ and $F(1,t)$ are constant, and thus their lifts are constant. 

 
> [!example] Circle
 Okay, let $f:I\to S^1$ be any loop from basepoint $x_0 = 1$. Then, $f$ lifts to a path $\tilde{f}: I\to \RR$ starting at $0$. $f(1) = 1\in S^1$, thus $\tilde{f}(1) = n$ for some $n\in \ZZ$. Well, I can write down a different path that looks the same: let $\omega_n:I\to S^1$ via $\omega_n(t) = e^{2\pi i n t}$. Then $\tilde{\omega}_n(t) = nt$. $\RR$ is simply connected, so $\tilde{f}$ and $\tilde{\omega}_n$ are homotopic. Dropping through $p$ gives us a homotopy between $f$ and $\omega_n$. Finally, we need to show that $\omega_1 \neq \omega_0$. But if they were, then we could lift a homotopy between them, which is absurd, because they don't even have the same endpoints in $\RR$. Thus: each loop in $S^1$ is homotopic to a unique $\omega_n$; this $\omega_n$ compose homomorphically to $\ZZ$, so $\pi_1(S^1) = \ZZ$.