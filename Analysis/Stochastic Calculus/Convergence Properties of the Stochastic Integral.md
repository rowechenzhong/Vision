---
aliases:
  - Dominated Convergence
  - dominated convergence
  - DCT
---
> [!theorem] Dominated Convergence Theorem
> Let $X$ be a CSM as usual and pick some locally bounded progressive processes $(H^n)_{n\in \NN}$, $H$, and $K$. Suppose $K\geq 0$, $H^n_s\to H_s$ a.s. for all $s\leq t$, and $\abs{H^n_s}\leq K_s$. In other words, we have the usual dominated limit.
> 
> Then, for any fixed $t$, $$\int_0^t H_s^n dX_s\to \int_0^t H_s dX_s$$in probability.

Split $X = M + A$; the $\int HdA$ converges by DCT.

Define $T_k = \inf\left\{r: \int_0^t K_s^2 d\braket{M,M}_s \geq k\right\}\land t$. This is useful, because$$\EE\left[\left(\int_0^{T_k} \left(H_s^n - H_s\right) dM_s\right)^2\right] \leq \EE\left[\underbrace{\int_0^{T_k}\left(H_s^n - H_s\right)^2 d\braket{M,M}_s}_{R_n}\right]$$(we consider $H' = \id_{s\leq T_k} \left(H_s^n - H_s\right)$, then $\EE[(H'\cdot M)^2_\infty]\leq \EE\left[\left(H'^2\cdot \braket{M,M}\right)_\infty\right]$ apply the isometry identities). Then, by DCT, $R_n\to 0$ almost surely. In fact, $R_n\leq 4\int_0^{T_k} K_s^2 d\braket{M,M}_s\leq 4k$ by the construction of $T_k$, thus $R_n$ is dominated and $\EE[R_n] \to 0$ almost surely.

Great. Thus,$$\PP\left(\abs{\int_0^t H_s^ndM_s - \int_0^t H_sdM_s} \geq \eps\right) = \lim \PP\left(\abs{\int_0^{T_k} (H_s^n - H_s)dM_s} \geq \eps\right).$$