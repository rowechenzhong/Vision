Here is one of a long series of correspondences which show how [[basepoints provide discrete information]].

> [!theorem] 
 The number of sheets of a path-connected $\tilde{X}$ over $X$ is equal to the index of $p_*(\pi_1(\tilde{X}, \tilde{x}_0))$ in $\pi_1(X, x_0)$. 

> [!proof]-
 Let $H = p_*(\pi_1(\tilde{X}, \tilde{x}_0))$ be the subgroup in question. The identifying property of $H$ is that any $[h]\in H$ lifts to a *loop* in $\tilde{X}$ which ends at $\tilde{x}_0$; this is not true of a general loop in $X$! Thus, consider the function $\Phi$ which sends cosets $H[g]$ to the endpoint $\tilde{g}(1)\in p^{-1}(x_0)$. We know $\tilde{X}$ is path connected, thus any $\tilde{x}_0' \in p^{-1}(x_0)$ can be joined to $\tilde{x}_0$ by some path $\tilde{g}$ which projects to a loop in $X$. Thus $\Phi$ is surjective. Suppose that $\Phi(H[g_1]) = \Phi(H[g_2])$. Then, $g_1 \conj{g_2}$ lifts to a loop in $\tilde{X}$ based at $\tilde{x_0}$; thus $[g_1][g_2]^{-1}\in H$ and $H[g_1] = H[g_2]$. Thus $\Phi$ is injective.