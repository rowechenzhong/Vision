---
aliases:
  - Ito's Formula
---
Pick $(\Omega, \FFF, \FFF_t, \PP)$, and a **vector** of CSMs $X_t = (X^1_t,\dots, X^p_t)$. If $f: \RR^p\to \RR$ is twice continuously differentiable, then $$f(X_t) - f(X_0) = \int_0^t \pa_i f(X_s)dX^i_s + \int_0^t \frac12 \pa_i\pa_j f(X) d\braket{X^i, X^j}.$$
> [!proof]- Proof sketch for 1D case
> Pick a mesh and telescope the sum. By [[Taylor's Theorem]], one can pick $s_i\in [t_{i-1}, t_i]$ such that the LHS is $$f'(X_{t_{i-1}})(X_{t_i} - X_{t_{i-1}}) + \frac12 f''(X_{s_i})(X_{t_i} - X_{t_{i-1}})^2.$$The first term kills the corresponding term on the RHS. Actually, by uniform convergence, the RHS is at most $\max_{t_i} \abs{f''(X_{t_{i-1}}) - f''(X_{s_i})} \sum_{t} \Delta X^2\to 0$ away from$$\frac12 f''(X_{t_{i-1}})(X_{t_i} - X_{t_{i-1}})^2.$$We know that the sequence of random measures $\mu_n = \left(X_{t_i} - X_{t_{i-1}}\right)^2 \delta_{t_{i-1}}$ converges weakly to $\braket{X,X}_s$. Meanwhile, $f''(X_t)$ is a path-continuous random process. So our summation converges to $\int_0^t f''(X_s)d\braket{X,X}_s$.

> [!idea] Comment on Domain
> If $f$ is only defined and $C^2$ on an open subset $U\subset \RR^p$, e.g. $x\mapsto \log(x)$, we can proceed as follows.
> 
> Pick some open set $V\subset U$ with closure $\bar{V}\subset U$. This way, $T_V = \inf\{t: X_t\notin V\}$ is a [[Elementary Stopping Time Constructions|collision time]]. The key analytic fact is that a $C^2$ function $f\big\vert_{\bar{V}}$ on $\bar{V}$ can be extended to a $C^2$ function $\tilde{f}_{\bar{V}}: \RR^p\to \RR$ with derivatives matching those of $f$ on $\bar{V}$; this is by the [[Whitney Extension Theorem]]. Ito's theorem then gives us the canonical decomposition of the CSM $G(X^{T_V})$ as a function of the first and second derivatives of $F$ on $V$. If $X$ a.s. does not exit $U$, we can allow $V\uparrow U$. Observing that $G(X^{T_V})\id_{T_V = \infty} = G(X)\id_{T_V = \infty}$ and that $\PP\left(\sup\{T_V = \infty\}\right) = 1$ , we obtain Ito's formula verbatim.