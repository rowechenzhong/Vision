If one ignores the basepoints, the Galois Correspondence gives a bijection between **isomorphism classes of path-connected covering spaces** and **conjugacy classes of subgroups of $\pi_1(X, x_0)$**. 
> [!theorem] Galois Correspondence Part 2
 Given some covering space $p: (\tilde{X}, \tilde{x}_0)\to (X, x_0)$ corresponding to subgroup $H_0 = p_*(\pi_1(\tilde{X}, \tilde{x}_0))$, we have to show two things: 
>  
>  
>  
>  -   Let $\tilde{x}_1\in p^{-1}(x_0)$ be some other basepoint. Observe that $p: (\tilde{X}, \tilde{x}_1)\to (X, x_0)$ is also a valid covering space. Then, the subgroup $p_*(\pi_1(\tilde{X}, \tilde{x}_1))$ is conjugate to $H_0$. 
>  
>  -  For any $H_1 = g^{-1} H g$, there exists a choice of basepoint $\tilde{x}_1\in p^{-1}(x_0)$ such that $p_*(\pi_1(\tilde{X}, \tilde{x}_1)) = H_1$. 
>  
>  

> [!proof] 
 You can literally write down the conjugation. Pick any path $\tilde{\gamma}$ from $\tilde{x}_0$ to $\tilde{x}_1$; $\gamma = p\tilde{\gamma}$ is a loop in $X$ based at $x_0$. Conjugating by this path yields the result.