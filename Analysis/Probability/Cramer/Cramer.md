>[!theorem]
> Let $X, X_i$ be iid random variables. If $m(\theta) = \EE[e^{\theta X}]$ is finite for some $\theta > 0$, then $\EE[X] = \mu\in [-\infty, \infty)$, and for any $\mu < a < x_{\text{max}} = \ess\sup X$ (the [[Essential Supremum]]), the sum $S_n = \sum_i X_i$ satisfies the ==**large deviations principle**==:
> $$
> -\lim_{n\to \infty} \frac{1}{n} \log\left(\PP\left(S_n \geq na\right)\right) = I(a)
> $$
> where $I(a) = \sup_{\theta\in \RR} [\theta a - \kappa(\theta)]$ is the [[Generating Functions#^legendre-dual|Legendre Dual]] of $\kappa$.

>[!idea] Intuition from 6.7800
>The most efficient way to achieve a large deviation $S_n \geq na$ (equivalently, conditioned on $S_n\geq na$ ...) is by making $X_1,\cdots X_n$ all behave like a collection of samples from $\PP_\theta$, choosing $\theta$ such that $\EE_\theta[X] = a$.

# Proof

Note that $m(\theta) < \infty$ implies $X$ cannot be really big, but it doesn't show $X$ can't be really negative, thus $\mu = -\infty$ is possible.


>[!proof]- Easy Upper bound
> Somehow, the upper bound is incredibly weak, and falls immediately. For any $\theta \geq 0$,
> $$\PP\left(S_n \geq na\right)\leq \PP\left(e^{\theta S_n}\geq e^{\theta na}\right)\leq \frac{\EE[e^{\theta S_n}]}{e^{\theta na}}=\frac{\EE[e^{\theta X}]^n}{e^{\theta na}}\implies -\frac1n \log \PP\left( S_n\geq na\right) \geq \sup_{\theta\geq 0}[\theta a - \kappa(\theta)]$$
> trivially, by Markov, and by independence.

>[!idea]- Why is the upper bound *so* weak?
> I think conditioned on $S_n\geq na$, $S_n$ is almost certainly exactly $na$. Thus $\EE[e^{\theta S_n}]\approx \EE[e^{\theta S_n}:S_n < na] + \PP\left(S_n\geq na\right)e^{\theta na}$. Then, $\EE[e^{\theta S_n}:S_n < na]$ is probably around $e^{\mu \theta n} \ll e^{\theta na}$. Not sure.
> Exponential distillation is really powerful, creating these ultra-sharp borders in the limit.

>[!proof]- Stupid extension
>The range $\sup_{\theta\in \RR}$ is intentional; we claim we don't care about $\theta < 0$. First off, note that $\theta\notin (\theta_-, \theta_+)$ are irrelevant because $\kappa = \infty$. Recalling that $\kappa$ is strictly convex on $(\theta_-, \theta_+)$ ($\mu < \ess \sup X$ ensures we don't have a point mass), and $\kappa'(\theta)\to \mu < a$ as $\theta\downarrow 0$, we see that $\kappa'(\theta) < a$ for $\theta \leq 0$.

>[!idea] Cheating
>We prove the lower bound in the case where $\sup_{\theta \in \RR}\left(\theta a - \kappa(\theta)\right)$ is attained at some value $\theta_a \in (\theta_-, \theta_+)$. We know $0 < \theta_a < \mu$ is a critical point of $\theta a - \kappa(\theta)$. I actually have no idea how this isn't the case, given that $\kappa$ is literally infinitely differentiable, but I guess we continue. 

>[!proof]- Upper bound
>Guided by intuition, the key idea is to **tilt the distribution until $S_n\geq na$ is no longer a large deviation event**.
>
>For example, if our original distribution was the [[Generating Functions#^joint-tilted|joint tilted distribution]] over some $\theta > \theta_a$, then convexity says $\EE_\theta[X] = \kappa'(\theta) > \kappa'(\theta_a) = a$. Then, [[WLLN]] says that $\PP_\theta(S_n\geq na) = 1$!
>
>Following the plan, we write
>$$\PP\left(S_n\geq na\right) = \EE_\theta\left[\frac{m(\theta)^n}{e^{\theta S_n}}\cdot \id\left\{S_n\geq na\right\}\right]$$
>The problem is that the $e^{\theta S_n}$ out front isn't bounded. But we can patch the issue by reducing to the case where $S_n \in [na, nb]$ for some $b > \kappa'(\theta)$.
>$$\geq \EE_\theta\left[\frac{m(\theta)^n}{e^{\theta nb}}\cdot \id\left\{S_n\in [na, nb]\right\}\right] = \frac{m(\theta)^n}{e^{\theta nb}} (1 - o(1)))$$
>Ripping through the constants for legitimacy,
>$$-\lim_{n\to \infty} \frac1n \log\left(\PP\left(S_n \geq na\right)\right) \leq \theta b - \kappa(\theta)$$
>This is true for all $\theta > \theta_a$ and all $b > \kappa'(\theta)$, so it is true for $\theta = \theta_a$ and $b = \kappa'(\theta_a)$ (because the RHS is a continuous function in $\theta, b$). We win.