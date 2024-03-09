Suppose $(X_n)_{n\geq 1}$ are a sequence of IID random variables with mean $\mu$ and variance $\sigma^2$. Fix $a < 0 < b$ and set
$$T = \inf\{n\geq 0: S_n\leq a \lor S_n \geq b\}$$
Then, $\EE[T] < \infty$, and $\EE[S_T] = \mu\EE[T]$.

Moreover, in the case $\mu = 0$, $\EE[S_T^2] = \sigma^2 \EE[T]$.

Otherwise, if we can find $\lambda^*\neq 0$ such that $\EE[e^{\lambda^*X_1}] = 1$, then $\EE[e^{\lambda^*S_T}] = 1$ as well.

>[!todo] Huh, prove this