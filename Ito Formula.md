Pick $(\Omega, \FFF, \FFF_t, \PP)$, and a **vector** of CSMs $X_t = (X^1_t,\dots, X^p_t)$. If $f: \RR^p\to \RR$ is twice continuously differentiable, then $$f(X_t) - f(X_0) = \int_0^t \pa_i f(X_s)dX^i_s + \int_0^t \frac12 \pa_i\pa_j f(X) d\braket{X^i, X^j}.$$

> [!proof] Proof sketch for 1D case
> Pick a mesh and telescope the sum. By [[Taylor's Theorem]], one can pick $s_i\in [t_{i-1}, t_i]$ such that the LHS is $$f'(X_{t_{i-1}})(X_{t_i} - X_{t_{i-1}}) + \frac12 f''(X_{s_i})(X_{t_i} - X_{t_{i-1}})^2.$$The first term kills the corresponding term on the RHS. Actually, by uniform convergence, the RHS is at most $\max_{t_i} \abs{f''(X_{t_{i-1}}) - f''(X_{s_i})} \sum_{t} \Delta X^2\to 0$ away from$$\frac12 f''(X_{t_{i-1}})(X_{t_i} - X_{t_{i-1}})^2.$$We now consider the sequence of random measures $\mu_n = \left(X_{t_i} - X_{t_{i-1}}\right)^2 \delta_{t_i}$.

> [!claim] A deceptively tedious claim
> $\mu_n\to \mu$ [[Random Measure|in distribution in probability]] where $\mu$ is the measure corresponding to the FVP $\braket{X,X}$.
%% 
The claim is that for all bounded continuous random processes $f$, for all $\eps$,
$$\lim_{n\to \infty} \PP\left(\abs{\int_0^{t} f_sd\braket{X,X}_s - \sum_{i = 0}^{j_n - 1} f_{t_i}\left(X_{t_{i+1}} - X_{t_i}\right)^2} \geq \eps\right) = 0.$$

Approach one. $f\cdot 


The proof proceeds as follows. $f_s$ is path-continuous, thus for each $\omega$, find some sequence $0 = T_0 < T_1 < \dots < T_p = t$ such that for all $T_i < s < T_{i+1}$, $\abs{f(s) - f(T_i)} < \frac{\eps}{M}$ which is a constant. This is a single partition, not a whole sequence of partitions, and contains finitely many terms. Thus, for all $\gamma,\delta$ we can find an $N$ such that for all $m \geq N$,
$$
\PP\left(\abs{})
$$ %%

I have no idea how to do this, asdf.

Thus, our summation converges to $\int_0^t f''(X_s)d\braket{X,X}_s$, gg.