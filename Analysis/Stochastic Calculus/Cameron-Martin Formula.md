---
aliases:
  - Cameron-Martin
---
# Solving our first SDE

Let $b$ be a bounded measurable function $\RR_+\times \RR$, which is bounded temporally by an $L^2$ function; there exists some $g\in L^2(\RR_+, \BBB(\RR_+), dt)$ such that $\abs{b(t,x)}\leq g(t)$ identically.

Notably, if $b$ is bounded on some $[0,A]\times \RR_+$ and vanishes on $t > A$ then we're chilling.

Now, let $B$ be an $(\FFF_t)$-BM. Consider the CLM $L_t = \int_0^t b(s, B_s)dB_s$ and its exponential martingale $D_t = \EEE(L)_t$.

Then, $\braket{L,L}_\infty = \int_0^t b(s,B_s)^2 ds < C < \infty$ for some constant $C$, and thus $\EE\left[\exp \frac12 \braket{L,L}_\infty\right] < \infty$. Hence, by Novikov's criterion, Girsanov's theorem applies and $D$ is a UI martingale. We now set $\QQ = D_\infty\cdot \PP$, such that $$\beta_t = B_t - \braket{B_t, L} = B_t - \int_0^t b(s,B_s)ds$$is an $(\FFF_t)$-BM under $\QQ$.

Flipping this around, we have obtained a solution $X = B$ to the SDE $dX_t = d\beta_t + b(t, X_t)dt$. This is really cool, because unlike the main sequence of our study of [[Stochastic Differential Equations Homepage|SDEs]], we are making no assumptions on the regularity of $b$; being bounded is enough.

# Cameron-Martin Formula

Suppose that $b(t,x) = g(t)$ is independent of $x$ now. Then, $h(t) = \int_0^t g(s)ds$ is just some (deterministic) function. We call the space of all such functions ==**Cameron-Martin space**==; this is just a regularity condition which says you "have a derivative in $L^2$." We then call $\dot h = g$.

>[!idea]
>This derivative is in the sense of distributions. I should figure out what distributions are at some point.

Under $\QQ = D_\infty\cdot \PP$ as before, $\beta_t = B_t - h(t)$ is a BM. But this means for every non-negative measurable $\Phi$ on the space of continuous functions $C(\RR_+, \RR)$,$$\EE_\PP\left[D_\infty\Phi(B)\right] = \EE_\QQ[\Phi(B)] = \EE_\QQ[\Phi(\beta + h)] = \EE_\PP[\Phi(B + h)].$$
>[!idea]- Do I understand the last equality?
>The last equality is because the value of $\EE_\PP[\Phi(B+h)]$ is a function solely of the pushforward measure $\PP\circ (B+h)^{-1}$ on $C(\RR_+,\RR)$, which is described completely by its finite-dimensional marginals, which are prescribed by the definition of Brownian motion, and are hence the same for $\QQ\circ (\beta + h)^{-1}$.

To rewrite it with all the integrals:

> [!theorem] Cameron-Martin Formula
> Let $W(dw)$ be the Wiener measure on $C(\RR_+, \RR)$, and let $h$ be a function in CM space. Then, for every non-negative measurable $\Phi: \CC(\RR_+,\RR)\to \RR_+$,
> $$
> \int W(dw)\Phi(w + h) = \int W(dw) \exp\left(\int_0^\infty \dot{h}(s)dw(s) - \frac12 \int_0^\infty \dot h(s)^2 ds\right)\Phi(w).
> $$

The integrals shown are with respect to a BM, so they can be interpreted as either Ito or Wiener integrals.