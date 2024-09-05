Here are an important class of [[Martingales in Continuous Time|CTMs]]. We say that a process $(Z_t)_{t\geq 0}$ on a vector space has ==**independent increments**== if $Z$ is adapted and, for every $0\leq s < t$, $Z_t - Z_s$ is independent of $\FFF_s$.

>[!example] Martingales seeded by independent increments
>  If $Z$ is real-valued, then
> 1. If $Z\in L^1$, then $Z_t - \EE[Z_t]$ is a martingale.
> 2. If $Z\in L^2$, then $Z_t^2 - \EE[Z_t^2]$ is a martingale.
> 3. If, for some $\theta\in \RR$, $\EE[e^{\theta Z_t}] < \infty$ for all $t\geq 0$, then $e^{\theta Z_t} / \EE[e^{\theta Z_t}]$ is a martingale.

>[!example] Doob
>Let $B_t$ be a brownian motion. Then $B_t^2 - t$ is a continuous martingale

>[!example] Exponential Martingales of Brownian Motion
>$\exp\left(\theta B_t - \theta^2 t/2\right)$ for $\theta > 0$ is a continuous martingale.

>[!example] GWN Martingales
> More generally, for any $f\in L^2(\RR_+, \BBB, dt)$, centered Gaussians $Z_t = \int_0^t f(s)dB_s$ have independent increments, thus$$\int_0^t f(s)dB_s,\qquad \left(\int_0^t f(s)dB_s\right) - \int_0^t f(s)^2ds,\qquad \exp\left(\theta\int_0^t f(s)dB_s - \frac{\theta^2}{2}\int_0^t f(s)^2ds\right)$$
> are all martingales.

> [!idea]- After you've read about the stochastic integral
> These are continuous (admit continuous modifications)! Indeed, $f(s)\in L^2(\RR_+, \BBB, dt)$ is the (deterministic) progressive process $f_s = f(s)$. This satisfies $\EE\left[\int_0^\infty f(s)^2 d\braket{B,B}_s\right] = \int_0^\infty f(s)^2ds < \infty$, thus $f\in L^2(B)\subset L^2_{\text{loc}}(B)$. Then, the stochastic integral with respect to the continuous martingale $B$ yields a continuous random process, which is a priori a continuous local martingale, but of we just showed $\EE[\braket{f\cdot B, f\cdot B}_\infty] < \infty$, thus $f\cdot B$ is a true martingale bounded in $L^2$.
> 
> Notably, $\EE[(f\cdot B)_t] = 0$, and $\EE[(f\cdot B)_t^2] = \EE[\braket{f\cdot B, f\cdot B}_t] = \EE\left[\left(f^2\cdot \braket{B,B}\right)_t\right] = \int_0^t f(s)^2 ds$. (You already knew that though, because the theory of [[Gaussian Spaces]] told you that $\int_0^t \bullet dB_s\equiv G(\bullet)$ was an isometry from $L^2(\RR_+,\BBB,dt)$ to the Gaussian space $\subset L^2(\Omega,\FFF,\PP)$).
> 
> Ito's formula doesn't really help you get the $\EE[e^{\theta (f\cdot B)_t}]$; instead use your brain cells and observe this is a Laplace transform of a Gaussian.

The [[Poisson Process]] is another example of a process, this time discrete-valued, which has independent increments. This creates its own class of martingales.