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
- If $M,N$ are continuous martingales bounded in $L^2$, $MN - \braket{M,N}$ is a UI martingale.
	- $\braket{M,N}_\infty$ exists in AS+$L^1$.
	- $\EE[M_\infty N_\infty] = \EE[M_0N_0] + \EE[\braket{M,N}_\infty]$.
- Two CLMs are ==**orthogonal**== if $\braket{M,N} = 0$ (iff $MN$ is a CLM).
	- If orthogonal $M,N$ are bounded in $L^2$, $M_SN_S$ is the UI martingale, and OST applies.
	- Independent BMs are orthogonal. Indeed, $\frac{B + B'}{\sqrt{2}}$ is also a BM, so compute.
- Computational claim again: the natural sequence of random signed measures $$\mu_n = \sum_i \left(X_{t_i} - X_{t_{i-1}}\right)\left(Y_{t_i} - Y_{t_{i-1}}\right) \delta_{\{t_{i-1}\}}.$$converge [[Random Measure|weakly in probability]] to $\mu$, the signed measure corresponding to $\braket{X,Y}$.

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
> 



%% # Some Computations

These computations were used for my 676 final project. Recorded here.

>[!claim]
For a subdivision $\Delta$ of $[0,t]$ and $\lambda\in [0,1]$, we set $t_i^\lambda = t_i + \lambda(t_{i+1} - t_i)$. Let $X = M+A$ and $Y = N+B$ be two CSMs while $H$ is adapted, and let $\abs{X}, \abs{Y},\abs{H}$ all be bounded by a constant $M$. We let $$K^\lambda_\Delta = \sum_i H_{t_i} \left\{\left(X_{t_i^\lambda} - X_{t_i}\right)\left(Y_{t_i^\lambda} - Y_{t_i}\right) - \braket{X,Y}_{t_i}^{t^\lambda_i}\right\}.$$We now wish to show that
> $$
> \lim_{\abs{\Delta}\to 0} \sup_\lambda \EE\left[\left(K^\lambda_\Delta\right)^2\right] = 0
> $$

Observe the problem reduces to the case $X = Y$ a CLM (and thus martingale), because polarization works.

In these circumstances, $M = X^2 - \braket{X,X}$ is a UI martingale. Then, for $i < j$,$$
\EE\left[H_{t_j}\left\{\left(X_{t_j^\lambda} - X_{t_j}\right)^2 - \braket{X,X}_{t_j}^{t^\lambda_j}\right\}\bigg\vert \FFF_{t_j}\right] = 0 \implies \EE\left[H_{t_i}\left\{\left(X_{t_i^\lambda} - X_{t_i}\right)^2 - \braket{X,X}_{t_i}^{t^\lambda_i}\right\}H_{t_j}\left\{\left(X_{t_j^\lambda} - X_{t_j}\right)^2 - \braket{X,X}_{t_j}^{t^\lambda_j}\right\}\right] = 0
$$
Hence, we are left to bound$$
\EE\left[\sum_i \left\{\underbrace{H_{t_i}\left\{\left(X_{t_i^\lambda} - X_{t_i}\right)^2 - \braket{X,X}_{t_i}^{t^\lambda_i}\right\}}_{\delta_i}\right\}^2\right].
$$
First let's show that this guy is even finite. This turns out to be really really annoying.

>[!proof]- This is actually really annoying, and I really could not find a faster way to do this despite being stuck on this problem for a week.
> First off, we drop the $H_{t_i}$ because its bounded by $M$.
> We have:
> $$
> \underbrace{\sum_i \left(X_{t_i^\lambda} - X_{t_i}\right)^4}_\star \leq \left(\sup_i \left(X_{t_i^\lambda} - X_{t_i}\right)^2\right)\sum_i\left(X_{t_i^\lambda} - X_{t_i}\right)^2 \leq (2M)^2\sum_i\left(X_{t_i^\lambda} - X_{t_i}\right)^2
> $$
> Then,
> $$
> \EE\left[\sum_i\left(X_{t_i^\lambda} - X_{t_i}\right)^2\right] \leq \EE\left[\sum_i\left(X_{t_i^\lambda} - X_{t_i}\right)^2 + \left(X_{t_{i+1}} - X_{t_i^\lambda}\right)^2\right] = \EE\left[X_t^2 - X_0^2\right] < \infty
> $$
> Thus, $\star$ has finite expectation.
> 
> The next term is trivial:
> $$
> \EE\left[\sum_i \left(X_{t_i^\lambda} - X_{t_i}\right)^2\braket{X,X}_{t_i}^{t^\lambda_i}\right] \leq \EE\left[(2M)^2 \sum_i \braket{X,X}_{t_i}^{t^\lambda_i} \right] \leq (2M)^2 \EE\left[\braket{X,X}_t\right] < \infty
> $$
> 
> The last term is actually annoying. As far as I can tell, here's the fastest way to do this:
> $$
> \EE\left[\sum_i \left(\braket{X,X}_{t_i}^{t_i^\lambda}\right)^2\right]\leq \EE\left[\left(\sum_i \braket{X,X}_{t_i}^{t_i^\lambda}\right)^2\right]\leq \EE\left[\braket{X,X}_t^2\right] \lesssim M^4
> $$
> where the last inequality is up to a universal constant via the [[The BDG Inequalities|BDG inequalities]].

Now, we use a Cauchy-Schwarz type trick, which would yield a really elegant solution if merely showing the answer was finite wasn't so terribly difficult.$$
\EE\left[\sum_i \delta_i^2\right]^2 \leq \EE\left[(\sup_i \delta_i)\sum_i \delta_i \right]^2 \leq \EE\left[\left(\sup_i \delta_i\right)^2\right]\EE\left[\left(\sum_i \delta_i\right)^2 \right] = \EE\left[\left(\sup_i \delta_i\right)^2\right]\EE\left[\sum_i \delta_i^2 \right]
$$
Thus, we find that $\EE\left[\sum_i \delta_i^2\right]\leq \EE\left[\left(\sup_i \delta_i\right)^2\right]$. This guy is finite (because it's less than $\sum_i \delta_i^2$, which we've shown is finite). Also, $X$ and $\braket{X,X}$ are continuous functions on a compact interval, hence this guy vanishes identically -- in words, for any $\eps > 0$, there exists a $\eta$ such that for all $\alpha < \eta$, $\abs{\left(X^{t+\alpha}_t\right)^2 - \braket{X,X}^{t_i^\lambda}_{t_i}}\leq \eps$. Hence, the supremum over $\lambda$ and the $\abs{\Delta}\to 0$ limits work automatically.

> [!claim]
> If $\lambda = 1$, then
> $$
> \lim_{\abs{\Delta}\to 0}  \sum_i H_i \left(X_{t^\lambda_i} - X_{t_i}\right)\left(Y_{t^\lambda_i} - Y_{t_i}\right) = \lambda \int_0^t H_sd\braket{X,Y}_s
> $$
> in $L^2$.

This should be trivial. We just showed that the LHS approaches$$
\sum_i H_{t_i}\left\{\braket{X,Y}_{t_i}^{t_{i+1}}\right\}
$$in $L^2$, so we just want to evaluate$$
\EE\left[\left\{\sum_i H_{t_i}\left\{\braket{X,Y}_{t_i}^{t_{i+1}}\right\} - \int_0^t H_sd\braket{X,Y}_s\right\}^2\right]
$$
We forever denote $[s] = \sup \{t_i \leq s\}$. This is just $\int_0^t \left(H_{[s]} - H_s \right)d\braket{X,Y}_s$. We apply dominated convergence theorem $\omega$-wise, so this vanishes for each $\omega$. We then apply dominated convergence theorem on this function of $\omega$, which also vanishes. So we're done.

>[!claim] A completely unrelated and trivial claim
>Suppose $F$ is $C^1$ on $\RR$. Prove that
>$$
>\lim_{n\to \infty} \sum_\Delta \left(F(X_{t_{i+1}}) - F(X_{t_i})\right)^2 = \int_0^t F'(X_s)^2 d\braket{X,X}_s
>$$
>in probability.

Indeed, $F$ has *uniformly continuous* derivative $F'$ on $[-K,K]$, hence by Taylor,$$
= \sum_\Delta F'(X_{t_i^\alpha})^2 (X_{t_{i+1}} - X_{t_i})^2
$$Now, by uniform continuity of $X_{t^\alpha_i}$, we know that for any $\eps$ and $\delta$, there is some $\abs{\Delta}$ such that for any smaller $\Delta$, with probability $\geq 1 - \delta$, the entire error term is at most $\sum_\Delta \eps (X_{t_i+1} - X_{t_i})^2\to 0$. So we conclude. %%