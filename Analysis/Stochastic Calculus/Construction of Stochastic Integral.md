---
aliases:
  - stochastic integral
---
If you anticipated a gory but reasonably satisfying bootstrapping episode, you're absolutely right. Here's the roadmap to define "$\int_0^t H_s dX_s = \sum H\Delta X$" where $H$ is a locally bounded progressive process and $X$ is a CSM.

- Start with $X$ as a martingale bounded in $L^2$.
- Extend to $X$ as a CLM.
- Extend to $X$ as a CSM, by adding the FVP integral ($H\cdot X$ should be bilinear!)

# Martingales Bounded in $L^2$

### Defining $\Hh^2$

Let $\Hh^2$ be the space of all **continuous** martingales which are **bounded in $L^2$** such that $M_0 = 0$ up to indistinguishability. We know that these inject into $L^2$ via $M_\infty$. We can pullback the form to $(M,N)_{\Hh^2} = \EE\left[M_\infty N_\infty\right]$.

>[!claim] $\Hh$ under $(\bullet,\bullet)_{\Hh^2}$ is a Hilbert space.

>[!idea]- How to path-find this proof.
> The claim is that the space is complete under this norm, which is not obvious solely because of path-continuity. Pointwise convergence is trivial. We essentially know one way to show a limit of continuous functions is continuous, which is via uniform convergence. We know essentially one way to get such a supremum bound, which is Doob. Write up the details.

>[!proof]- Boring
> Well, give me a Cauchy sequence $(M^i)$; their images $M^i_\infty$ admit a limit in $L^2$ called $M^\infty_\infty$. We want to use $\EE[M^\infty_\infty | \FFF_t]$, but this doesn't work immediately, so we go the other way.
> 
> Doob's inequality in $L^2$ shows that $\EE\left[\sup_{t\geq 0}\left(M^n_t - M^m_t\right)^2\right]\leq 4 \EE\left[ \left(M^n_\infty - M^m_\infty\right)^2\right]$, thus $M^n_t$ as a function of $t$ converges uniformly in $L^2$. Extract a subsequence such that $\EE\left[\sup_{t\geq 0}\abs{M^{n_{i+1}}_t - M^{n_i}_t}\right]^2 < \EE\left[\sup_{t\geq 0}\left(M^{n_{i+1}}_t - M^{n_i}_t\right)^2\right] < 100^{-i}$, thus $\EE[\sum_{i\geq 1} \sup_{t\geq 0} \abs{M_t^{n_{i+1}} - M_t^{n_i}}] < \infty$ and $\sum_{i\geq 1} \sup_{t\geq 0} \abs{M_t^{n_{i+1}} - M_t^{n_i}} < \infty$ almost surely. Along these events $M_t$ converges uniformly, and we can let $M^\infty_t$ be the (continuous) uniform limits of these paths. Let $M^\infty_t = 0$ otherwise. For fixed $t$ this limit is obviously an $L^1$ and $L^2$ limit.
> 
> Then, $M_t^\infty = \lim_{n\to \infty} \EE[M^n_\infty | \FFF_t]$ where the limit is in the AS sense. By dominated convergence theorem using the constants above, this is $=\EE[M^\infty_\infty | \FFF_t]$ as desired.

Okay, that's the differential. Given some $M\in \Hh^2$, what's allowed to be in the integrand? Well, let $L^2(M) = L^2(\Omega \times \RR_+, \PPP, dP d\braket{M,M}_s)$ where the measure assigns$$\EE\left[\int_0^\infty \id_A(\omega,s) d\braket{M,M}_s\right]$$to the set $A\in \PPP$. This is the set of [[Adapted Continuous-Time Processes|progressive]] processes such that$$\EE\left[\int_0^\infty H_s^2 d\braket{M,M}_s\right] < \infty.$$modulo $H_s = 0$ $d\braket{M,M}$ a.e. a.s., and has an inner product $(\bullet,\bullet)_{L^2(M)}$ and norm $\norm{H}_{L^2(M)}$.

>[!example]
>If $M$ is Brownian motion (say, stopped at time $t$ so we're bounded in $L^2$), then $L^2(M)$ is just $\EE\left[\norm{H(\omega)}_2^2\right] < \infty$.

We now identify a set of ==**elementary processes**==, which are more or less exactly what you expect:

>[!definition] Elementary Processes
>An ==**elementary process**== is a progressive process$$H_s(\omega) = F(\omega) \id_{(t,s]}$$where $t < s$ and $F$ is a bounded $\FFF_t$-measurable random variable.

More generally, any finite linear combination is also called an elementary process:$$H_s(\omega) = \sum_{i = 0}^{p-1} H_{(i)}(\omega) \id_{(t_i,t_{i+1}]}(s)$$where $0 = t_0 < \dots < t_p$ and each $H_{(i)}$ is a bounded $\FFF_{t_i}$-measurable random variable.

The collection of (equivalence classes of) elementary processes forms a linear subspace of $L^2(M)$ called $\mathscr{E}$.

>[!claim] $\mathscr{E}$ is dense in $\Hh$.

> [!proof]- Proof ideas are sort of interesting
> Let $X_t = \int_0^t K_u d\braket{M,M}_u$. The key idea is that for all $\FFF_s$-measurable $F$, applying orthogonality to $H_r(\omega) = F(\omega)\id_{(s,t]}(r)$ yields $\EE[F(X_t - X_s)] = 0$. Thus $X$ is a martingale, but it is also an FVP, thus it vanishses.

### Stochastic Integral for Elementary Processes

Finally, we obtain the definition of the stochastic integral for elementary processes!

> [!definition]
> Let $M\in \Hh^2$. For every $H\in \mathcal{E}$, define$$\left(H\cdot M\right)_t \equiv \int_0^t H_sdM_s\equiv \sum_{i = 0}^{p-1} H_{(i)} \left(M_{t_{i+1}\land t} - M_{t_i\land t}\right)$$ is the ==**stochastic integral of $H$ with respect to $M$.**==

The mapping $H\mapsto H\cdot M$ extends to an isometry $L^2(M)\hookrightarrow \Hh^2$ with the same notation.

>[!idea]
>Why is this the correct definition?

>[!theorem] Characterization
>$H\cdot M$ is the unique martingale in $\Hh^2$ such that $\braket{H\cdot M, N} = H\cdot \braket{M,N}$ for all $N\in \Hh^2$.

...that's your interface!

>[!idea] $\sum \Delta(\sum H\Delta M)\Delta N = \sum H \Delta M \Delta N = \sum H\Delta\left(\sum \Delta M \Delta N\right)$.

>[!example] Notable Consequence
>For $M\in \Hh^2$ and $H\in L^2(M)$, $\braket{H\cdot M, H\cdot M} = H\cdot \braket{M, H\cdot M} = H\cdot (H\cdot \braket{M, M}) = H^2\cdot \braket{M,M}$ i.e. the quadratic variation of $H\cdot M$ is $\int_0^t H_s^2 d\braket{M,M}_s$.

> [!example] Continuation
> Let $H\in L^2(M)$. If $K$ is progressive, $KH\in L^2(M)$ iff $K\in L^2(H\cdot M)$.
> 
> In this case, $(KH)\cdot M = K\cdot (H\cdot M)$, because for all $N\in \Hh^2$, $$\braket{(KH)\cdot M, N} = (KH)\cdot \braket{M,N} = K\cdot \left(H\cdot \braket{M,N}\right) = K\cdot \braket{H\cdot M, N} = \braket{K\cdot (H\cdot M), N}$$

### Side Note: Stopped Processes

Notation: $(\id_{[0,T]})_s(\omega) = \id_{0\leq s\leq T(\omega)}$.

>[!idea] $\Hh$ is closed under stopped processes.
>For $M\in \Hh$, $\EE[\braket{M^T,M^T}_\infty] = \EE[\braket{M,M}_T]$, but this guy is an increasing process so it's $\leq \EE[\braket{M,M}_\infty] < \infty$. Thus, $\Hh$ is closed under stopped processes.

>[!claim] If you stop buying a stock, the stock might as well stop moving.
>$\left(\id_{[0,T]} H\right)\cdot M = (H\cdot M)^T = H\cdot M^T$.

> [!proof]- Easy Exercise
> We basically want to pass the $T$ to the FVP integral where it is handled ($\star$). $$\id_{[0,T]}H\cdot \braket{M,N} = H\cdot \left(\id_{[0,T]}\cdot \braket{M,N}\right) \stackrel{\star}{=} H\cdot \braket{M,N}^T = H\cdot \braket{M^T,N}$$and uhhh$$\braket{(H\cdot M)^T, N} = \braket{H\cdot M, N}^T = \left(H\cdot \braket{M,N}\right)^T\stackrel{\star}{=} \id_{[0,T]}H\cdot \braket{M,N}.$$

# Local Martingales

This time, let $M$ be a CLM. We let $L^2(M) = L^2(\Omega \times \RR_+, \PPP, dP d\braket{M,M}_s)$ again, consisting of progressive processes $H$ such that$$\EE\left[\int_0^\infty H_s^2d\braket{M,M}_s\right] < \infty.$$
>[!idea] Strength
This should strike you as odd though, because this is a $\EE[\braket{H\cdot M,H\cdot M}_\infty] < \infty$ condition, which implies a true martingale bounded in $L^2$ -- it's too strong. Changing the $\infty$ to a $t$ would also be too strong, because it corresponds to $H\cdot M$ being a true martingale bounded in $L^2$.

Correspondingly, let $L^2_{\text{loc}}(M)$ be the collection of progressive processes $H$ such that, with probability $1$, for all $t\geq 0$, $$\int_0^t H_s^2d\braket{M,M}_s < \infty.$$
>[!example]
>If $M$ is Brownian motion, then $L^2_{\text{loc}}(M)$ says $\norm{H(\omega)}_2^2 < \infty$ almost surely.

Here is the extension, plus all of our claims from before.

> [!claim] Stochastic Integral Extension
> One can extend the definition of the stochastic integral to $(H,M)\mapsto H\cdot M$ on $L^2_{\text{loc}}(M)\times \text{CLM}\to \text{CLM}$ such that:
> - For $M,H$ in $\Hh\times L^2(M)$, it coincides with our old definition.
> - $H\cdot M$ is the unique CLM starting from $0$ such that for every CLM $N$, $\braket{H\cdot M, N} = H\cdot \braket{M,N}$.
> - If $H\in L^2_{\text{loc}}(M)$ and $K$ is progressive, then $K\in L^2_{\text{loc}}(H\cdot M)$ iff $KH\in L^2_{\text{loc}}(M)$. Then, $K\cdot (H\cdot M) = KH\cdot M$.
> - If $T$ is a stopping time, $\left(\id_{[0,T]} H\right)\cdot M = (H\cdot M)^T = H\cdot M^T$.

# Continuous Semi-martingales

Finally, let $X = M + A$. We want $H\cdot X = H\cdot M + H\cdot A$, which means we must restrict our integrand to $L^2_{\text{loc}}(M)\cap L^1(A)$.

Let's focus our attention on ==**locally bounded progressive process**==, which are a progressive process $H$ such that$$\forall t\geq 0,\qquad\sup_{s\leq t} \abs{H_s} < \infty$$almost surely. Then, LBPPs are integrable with respect to all FVPs, and thus all CSMs! Indeed, $$\forall t \geq 0, \forall \omega \in \Omega, \int_0^t \abs{H_s(\omega)} \abs{dA_s(\omega)} \leq \sup_{s\leq t} \abs{H}_s \int_0^t \abs{dA_s(\omega)}< \infty.$$Similarly, LBPP $\subset L^2_{\text{loc}}(M)$.$$\forall t\geq 0, \forall \omega \in \Omega, \int_0^t H_s(\omega)^2 d\braket{M,M}_s\leq \sup_{s\leq t}\abs{H}_s^2 \int_0^t d\braket{M,M}_s < \infty$$

>[!idea] Continuous adapted processes are automatically LBPP.

>[!definition] Stochastic Integral
>Given a CSM $X$ and an LBPP $H$, $H\cdot X = H\cdot M + H\cdot A$ is a CSM.

>[!claim] Elementary Properties
>- $(H,X)\mapsto H\cdot X$ is bilinear.
>- $H\cdot (K\cdot X) = (HK)\cdot X$ if $H,K$ are LBPP
>- For any stopping time $T$, $(H\cdot X)^T = H\id_{[0,T]}\cdot X = H\cdot X^T$.

> [!claim] Behavior on Elementary Processes
> Given $H_s(\omega) = \sum_{i = 0}^{p-1} H_{(i)}(\omega) \id_{(t_i,t_{i+1}]}(s)$,
> 
> $$(H\cdot X)_t = \sum_{i = 0}^{p-1} H_{(i)}\left(X_{t_{i+1}\land t} - X_{t_i\land t}\right)$$