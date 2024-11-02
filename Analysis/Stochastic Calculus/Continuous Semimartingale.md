---
aliases:
  - continuous semimartingales
  - CSMs
  - CSM
---
>[!definition] Continuous Semimartingale
>If $M$ is a CLM and $A$ is a FVP, then $X = M + A$ is a ==**continuous semimartingale**==.

This decomposition $X = M + A$ is the ==**canonical decomposition**== and is unique up to indistinguishability because CLM $\cap$ FVP $=\{0\}$.

>[!definition] Braket of Two CSMs
>Suppose $X = M+A$ and $Y = M'+A'$. Then $\braket{X,Y} = \braket{M,M'}$.

>[!claim]
>Give me a mesh. This is $\lim_{n\to \infty} \sum_{i = 1}^{p_n}\left(X_{t_i^n} - X_{t_{i-1}^n}\right)\left(Y_{t_i^n} - Y_{t_{i-1}^n}\right)$ in probability.

>[!idea] Intuition: $\sum \Delta M\Delta A \to 0$, $\sum \Delta A\Delta A'\to 0$.

>[!proof]- Uniform continuity $\implies$ supremum bound
> Comparing against$$
> \lim_{n\to \infty} \sum \left(M_{t_i^n} - M_{t_{i-1}^n}\right)\left(M'_{t_i^n} - M'_{t_{i-1}^n}\right)
> $$we just want to show that the cross-terms $$\sum_{i = 1}^{p_n} \left(M_{t_i^n} - M_{t_{i-1}^n}\right)\left(A'_{t_i^n} - A'_{t_{i-1}^n}\right),\qquad \sum_{i = 1}^{p_n} \left(A_{t_i^n} - A_{t_{i-1}^n}\right)\left(A'_{t_i^n} - A'_{t_{i-1}^n}\right)$$vanish in the limit. But like, this is not that deep; the absolute value of these guys is at most$$\left(\sup \Delta M\right)\sum \Delta A',\qquad \left(\sup \Delta A\right) \sum \Delta A'.$$Continuous functions are uniformly continuous on compact domains, and $\sum \Delta A' \leq \int_0^t \abs{dA}_s < \infty$ by definition of FVP thus we conclude.