---

aliases:
  - fundamental weight
  - fundamental dominant weight
---

Fix some base $\Delta  = \{\alpha_1,\dots, \alpha_i\} \subset \Phi$. Then, a weight $\lambda$ is ==**dominant**== if all integers $\braket{\lambda | \alpha}$ are nonnegative, and ==**strongly dominant**== if all such integers are positive. Let $\Lambda^+$ be all the set of all dominant weights.

>[!idea]
>$\Lambda^+ = \overline{\mathfrak{C}(\Delta)}\cap \Lambda$, while $\mathfrak{C}(\Delta)$; $\Lambda \cap \mathfrak{C}(\Delta)$ is the set of strongly dominant weights.

Find the dual basis of the inverted base, $\{\lambda_i\}$ (where $\braket{\lambda_i, \alpha_j} = \delta_{i,j}$). These are dominant weights, and are called the ==**fundamental dominant weights**==.
- Each weight is conjugate under $\mathcal{W}$ to exactly one d-weight. If $\lambda$ is dominant, then $\sigma \lambda \prec \lambda$ for all $\sigma \in \mathcal{W}$. If $\lambda$ is strongly dominant, then $\sigma \lambda = \lambda$ iff $\sigma = 1$.
- If $\lambda$ is dominant then the number of $\mu \prec \lambda$ is finite.