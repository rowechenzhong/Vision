Let's go top to bottom. TODO: finish this!

[!example] Angular Momentum
Start with the angular momentum algebra $\fg = \su(2)$ with $[J_i, J_j] = i\eps_{ijk} J_k$.

First, we can rewrite in terms of $J_\pm = J_x \pm iJ_y$, isolating a Cartan subalgebra $\{J_z\}$; $[J_z, J_\pm] = \pm J_\pm$, thus $\ad J_z$ is semisimple.

We now observe that we have a root space decomposition; $\Phi = \{+1, -1\}\in \RR^1$, $\fg_1 = \{J_+\}$, and $\fg_{-1} = \{J_-\}$. As expected, $[\fg_\alpha \fg_\beta] = \fg_{\alpha + \beta}$, and each root space is one-dimensional.

Now, consider any finite-dimensional representation $\rho:\fg \curvearrowright V$; we will not write $\rho$ by abuse of notation. The Cartan subalgebra always diagonalizes over $\rho$, thus we can organize $V$ by their weight. Then, it is clear that $\fg_\alpha$ moves elements of your representation by $\alpha$ between weight spaces.

In our particular example, this just means $J_+$ raises your eigenvalue of $J_z$ and $J_-$ lowers your eigenvalue of $J_z$.


On an unrelated note, $[J_+, J_-] = 2J_z$.

$\fg$ is simple with Cartan subalgebra $\fg_0$. Simultaneously diagonalize $\fg_0$ to get weights
$$h_i\ket{\mu} = \mu_i \ket{\mu}$$