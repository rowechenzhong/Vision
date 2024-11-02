> [!definition] Minuscule Weight
> A [[Dominant Weights|dominant integral weight]] $\omega$ such that $(\omega, \beta)\leq 1$ for all positive coroots $\beta$.

>[!idea]
> One can learn the theory of $\GL_n(\CC)$ before reading this; it turns out that $\GL_n(\CC)$ is completely beautiful *because* all its fundamental weights are minuscule.

>[!claim] Equivalent Characterizations
>- $\omega$ is minuscule
>- all weights of $L_\omega$ belong to $W\omega$.
>- The weights of $L_\omega$ are exactly $W\omega$.
>- If $\lambda$ is dominant integral and $\omega - \lambda \in Q_+$, then $\lambda = \omega$.

This implies that $\chi_\omega = \sum_{\gamma \in W \omega} e^\gamma$.

>[!claim] Tensor products are easy
>For all dominant integral $\lambda$, $$L_\omega \otimes L_\lambda = \oplus_{\gamma \in W\omega} L_{\lambda + \gamma}.$$ We set $L_{\lambda + \gamma} = 0$ if $\lambda + \gamma$ is not dominant.

>[!claim] Counting Minuscule Weights
>Each coset of $P/Q$ contains exactly one minuscule weight, thus the number of minuscule weights is exactly $\det A$, where $A$ is the Cartan matrix.

>[!todo]
>Add $\GL_n(\CC)$ implications!