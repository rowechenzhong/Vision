Now, we polarize the [[Quadratic Variation of Continuous Local Martingales|Quadratic Variation]].

>[!definition] Braket of two CLMs
>If $M,N$ are CLMs, the ==**braket**== $\braket{M,N}$ is the FVP
>$$
>	\braket{M,N} = \frac12\left(\braket{M+N,M+N} - \braket{M,M} - \braket{N,N}\right).
>$$

Just by bilinear properties,
- $\braket{M,N}$ is the unique FVP such that $MN - \braket{M,N}$ is a CLM.
- Given a mesh on $[0,t]$,$$\braket{M,N}_t = \lim\sum \Delta M \Delta N = \lim_{n\to \infty} \sum \left(M_{t_i^n} - M_{t_{i-1}^n}\right)\left(N_{t_i^n} - N_{t_{i-1}^n}\right)$$in probability.
- For every $T$, $\braket{M^T,N^T} = \braket{M^T,N} = \braket{M,N}^T$.
- If $M,N$ are continuous martingales bounded in $L^2$, $MN - \braket{M,N}$ is UI.
	- $\braket{M,N}_\infty$ exists in AS+$L^1$.
	- $\EE[M_\infty N_\infty] = \EE[M_0N_0] + \EE[\braket{M,N}_\infty]$.
- Two CLMs are ==**orthogonal**== if $\braket{M,N} = 0$ (iff $MN$ is a CLM).
	- If orthogonal $M,N$ are bounded in $L^2$, $M_SN_S$ is the UI martingale, and OST applies.
	- Independent BMs are orthogonal. Indeed, $\frac{B + B'}{\sqrt{2}}$ is also a BM, so compute.

And of course, we have to drop the Cauchy-Schwarz.

> [!theorem] Kunita-Watanabe
> Let $M,N$ be CLMs and $H,K$ be measurable processes. Then,
> $$\left(\int_0^\infty \abs{H_s}\abs{K_s} \abs{d\braket{M,N}_s}\right)^2\leq \left(\int_0^\infty H_s^2 d\braket{M,M}_s\right)\left(\int_0^\infty K_s^2 d\braket{N,N}_s\right)$$almost surely.

>[!idea] Heuristically, $\sum HK\Delta M \Delta N \leq \sqrt{\sum H^2\Delta M^2}\sqrt{K^2 \Delta N^2}$

>[!proof]- Apply Cauchy Schwarz four times
> In this proof, $\bullet^t_s = \bullet_t - \bullet_s$ as notation. By staring at the limits in probability, for almost every $\omega$, for all $s < t$ we have$$\abs{\braket{M,N}^t_s} \leq \sqrt{\braket{M,M}^t_s} \sqrt{\braket{N,N}^t_s}$$by the Cauchy-Schwarz inequality. We fix such a $\omega$ and proceed with a purely deterministic argument.
> 
> We now solve it for the case where $H,K$ are $\id_{[s,t]}$ in hopes of a monotone class bootstrap. This is immediate by Cauchy-Schwarz:$$\int_s^t\abs{d\braket{M,N}_s} = \lim \sum \abs{\Delta \braket{M,N}}\leq \sqrt{\lim \sum \Delta\braket{M,M}}\sqrt{\lim \sum \Delta\braket{M,M}} = \sqrt{\braket{M,M}^t_s}\sqrt{\braket{N,N}^t_s}.$$We now solve it for the case where $H = K = \id_A$ where $A$ is a finite union of disjoint intervals. This follows again from the Cauchy-Schwarz inequality. The ends can be open or closed because all measures are non-atomic.
> 
> We now claim to have solved it for all $H = K = \id_A$ on all Borel $A$. Observe that the collection of $A$ on which this statement is true is:
> - Closed under increasing and decreasing sequential limits.
> 	- The RHS limit holds because of measures are continuous under such limits.
> 	- The LHS limit holds because of MCT and Fatou.
> - Contains all finite unions of intervals. This is a semi-algebra generating the Borel $\sigma$-algebra. By [[Monotone Class Theorem]] this implies the whole $\sigma$-algebra lies in this collection.
> 
> Now, let $H = \sum_{i} \lambda_i \id_{A_i}$ and $K = \sum_i \mu_i \id_{A_i}$ be arbitrary non-negative simple functions with bounded support. The conclusion again follows from yet another application of Cauchy Schwarz:
> $$
> \sum_i \lambda_i \mu_i \int_{A_i} \abs{d\braket{M,N}_s} \leq \left(\sum_i \lambda_i^2 \int_{A_i}d\braket{M,M}_s\right)^{1/2}\left(\sum_i \mu_i^2 \int_{A_i}d\braket{N,N}_s\right)^{1/2}.
> $$
> Finally, every non-negative Borel function is a monotone increasing limit of simple functions with bounded support ([[approximation by simple functions]]) thus [[Convergence properties of Lebesgue Integral|Monotone Convergence]] concludes.
