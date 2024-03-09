As a scaffold, we will be defining $(B_t)_{t\in \RR_{\geq 0}}$ as $G([0,t])$ where $G$ is a [[Gaussian White Noise|GWN]] with Lebesgue intensity. This is not unique in general, because the GWN isn't either.

>[!claim]- (Trivially) Equivalent Definitions
>All of the following are equivalent to being a pBM.
>1. $(X_t)_{t\geq 0}$ is a centered Gaussian process with covariance $K(s,t) = s\land t$.
>2. $X_0 = 0$ a.s., and for every $0\leq s < t$, $X_t - X_s$ is independent of $\sigma(X_r, r\leq s)$ and distributed as $N(0, t-s)$.
>3. $X_0 = 0$ a.s., and for every choice of $0 = t_0 < t_1 <\dots < t_p$, $X_{t_i} - X_{t_{i-1}}$ are independent and distributed as $N(0, t_i - t_{i-1})$.