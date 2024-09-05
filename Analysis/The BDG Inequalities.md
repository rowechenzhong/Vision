---
aliases:
  - BDG inequalities
---
As in [[Discrete Doob's Maximal Inequalities|Doob's Maximal Inequalities]], for all CLM $M$, set $M^*_t = \sup_{s\leq t} \abs{M_s}$.

>[!theorem] Burkholder-Davis Gundy
>For every real $p > 0$, there exist two constants $c_p, C_p > 0$ depending only on $p$, such that for every CLM $M$ with $M_0 = 0$ ,
>$$c_p\EE\left[ \braket{M,M}^{p/2}_\infty\right] \leq \EE\left[ \left(M^*_\infty\right)^p\right] \leq C_p \EE\left[\braket{M,M}_\infty^{p/2}\right].$$

Observe that one can replace all the $\infty$'s with a stopping time $T$ by considering $M^T$.

The proof involves casework on $p$, and we will present only the RHS of the inequality where $p\geq 2$, as this is where [[Ito Formula|Ito's Formula]] is used. Unrelatedly, the LHS for $p\geq 4$ was proved in your pset.

>[!proof]
> We first consider bounded $M$, such that $M\in \Hh^2$. Applying Ito's formula to the $C^2$ function $\abs{x}^p$ (!) we obtain$$\abs{M_t}^p = \int_0^t p\abs{M_s}^{p-1} \sgn(M_s)dM_s + \frac12\int_0^t p(p-1) \abs{M_s}^{p-2} d\braket{M,M}_s.$$The first term is a martingale in $\Hh^2$ (because so is $M_s$, and this is valid for anything in $L^2(M)$). Thus,$$\EE\left[\abs{M_t}^p\right]\leq \frac{p(p-1)}{2}\EE\left[\int_0^t \abs{M_s}^{p-2} d\braket{M,M}_s\right]$$

>[!idea] The takeaway
>Proving $\EE$-statements is possible with Ito, so long as the CLM part can be coerced to be a true martingale.

>[!proof]- Arguments not involving Ito conclude.
> $$\leq \frac{p(p-1)}{2} \EE\left[\left(M^*_t\right)^{p-2} \braket{M,M}_t\right].$$By Holder's inequality,$$\leq \frac{p(p-1)}{2} \EE\left[\left(M^*_t\right)^p\right]^{\frac{p-2}{p}} \EE\left[ \braket{M,M}^{p/2}_t\right]^{\frac{2}{p}}.$$
> By Doob's inequality,$$\EE\left[\left(M^*_t\right)^p\right] \leq \left(\frac{p}{p-1}\right)^p \EE\left[\abs{M_t}^p\right].$$
> which we can combine with the previous result. Let $t\to \infty$ to kill. For general $M$, consider $M^{T_n}$ where $T_n = \inf\{t\geq 0: \abs{M_t} = n\}$ and let $n\to \infty$ to kill (all parts converge by MCT).

>[!claim] Corrolary
>If $M$ is a CLM with $M_0 = 0$, then if $\EE\left[\braket{M,M}^{1/2}_\infty\right] < \infty$, $M$ is a UI martingale. Indeed, $\EE[M^*_\infty] < \infty$, thus $M$ is dominated by $M^*_\infty\in L^1$.
>
>Immediately, if $\EE\left[\braket{M,M}_t^{1/2}\right] < \infty$ for all $t$, then $M$ is a martingale.

Recall that if $\EE\left[\braket{M,M}_\infty\right] < \infty$, then $M\in \Hh^2$, which is stronger.

> [!example] Strength and bounds
> Suppose $M$ is a CLM and $H$ is progressive:
> - If $\int_0^t H_s^2 d\braket{M,M}_s < \infty$ for all $t$ a.s. , then we say $H\in L^2_{loc}(M)$, and $H\cdot M$ is a CLM. This is the minimal condition to be integrable.
> - If $\EE\left[\left(\int_0^t H_s^2 d\braket{M,M}_s\right)^{1/2}\right] <\infty$ for all $t$, then $H\cdot M$ is a true martingale.
> - If $\EE\left[\left(\int_0^\infty H_s^2 d\braket{M,M}_s\right)^{1/2}\right] <\infty$, then $H\cdot M$ is a true UI martingale.
> - If $\EE\left[\int_0^t H_s^2 d\braket{M,M}_s\right] <\infty$ for all $t$, then $H\cdot M$ is a true martingale with $(H\cdot M)_t\in L^2$.
> - If $\EE\left[\int_0^\infty H_s^2 d\braket{M,M}_s\right] <\infty$, then $H\cdot M$ is a true martingale bounded in $L^2$.