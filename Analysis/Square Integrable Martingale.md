---
aliases:
  - Variances Add
  - variances add
---
A ==**square integrable martingale**== $(M_t)_{t\geq 0}$ is just a [[Martingales in Continuous Time|martingale]] in $L^2$. These are important cases of interest, because our development of [[Continuous Semimartingale|continuous semimartingales]] will operate in $L^2$, and we will discover that the "noise" of $M_t$ scales quadratically in deep ways.

>[!claim] Variances Add
>Let $0\leq s = t_0 < t_1 < \dots < t_p = t$. Then,$$\EE\left[\sum_{i = 1}^p\left(M_{t_i} - M_{t_{i-1}}\right)^2 | \FFF_s\right] = \EE\left[M_t^2 - M_s^2 | \FFF_s\right] = \EE\left[\left(M_t - M_s\right)^2 | \FFF_s\right]$$

>[!example] Brownian Motion
>The above expression is exactly sum of variances;$$\EE\left[\left(M_t - M_s\right)^2 | \FFF_s\right] = (t-s)^2.$$This is *the* canonical example of this property of martingales.