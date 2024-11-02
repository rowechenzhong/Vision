> [!theorem] Dambis-Dubins-Schwarz
> Let $M$ be a CLM such that $\braket{M,M}_\infty = \infty$ a.s.. Then, there exists a BM $\left(\beta_s\right)_{s\geq 0}$ such that a.s., for all $t\geq 0$,$$M_t = \beta_{\braket{M,M}_t}.$$

- We write $\beta$ and not $B$ to remind ourselves that $\beta$ will not be adapted with respect to $\left(\FFF_t\right)$, but rather a time-changed filtration.
- $\braket{M,M}_\infty = \infty$ can be dropped!

>[!proof]- Proof sketch
> The details of the proof seem unenlightening. Here's the breakdown. I ignore all almost-sure details (and more).
> - The intuition is that we want to use the increasing process $\braket{M,M}_t$ to measure time. To this end:
> 	- The time change is exactly $\tau_r = \inf\{t\geq 0: \braket{M,M}_t \geq r\}$
> 	- The BM is exactly $\beta_r = M_{\tau_r}$. (Thus, "$\beta_{\braket{M,M}_t} = M_{\tau_{\braket{M,M}_t}} = M_t$").
> 	- The filtration is $\GGG_r = \FFF_{\tau_r}$.
> - Now, we simply show $\beta_s$ and $\beta_s^2 - s$ are martingales.
> 	- $\beta_s$ is obviously a martingale:$$\EE\left[\beta_s | \GGG_t\right] = \EE\left[M_{\tau_s} | \FFF_{\tau_t}\right] = \beta_t$$
> 	- $\beta^2_s - s$ is also obviously a martingale:$$\EE[\beta_s^2 - s | \GGG_t] = \EE[M_{\tau_s}^2 - \braket{M,M}_{\tau_s} | \FFF_{\tau_t}] = M^2_{\tau_t} - \braket{M,M}_{\tau_t} = \beta^2_t - t.$$

>[!claim] Random technical Proposition
>Let $M, N$ be two CLMs with $M_0 = N_0 = 0$. Suppose $\braket{M,M}_t = \braket{N,N}_t$ for all $t\geq 0$, $\braket{M,N}_t = 0$ for every $t\geq 0$, a.s., and $\braket{M,M}_\infty = \braket{N,N}_\infty = \infty$, a.s..
>
>Then, the corresponding BMs $\beta$ and $\gamma$ are independent.

Proof omitted; you want to show that $\braket{\beta, \gamma} = 0$ and hit with [[Levy's Characterization of Brownian Motion]].