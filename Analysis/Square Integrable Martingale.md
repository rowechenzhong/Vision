A ==**square integrable martingale**== $(M_t)_{t\geq 0}$ is just a [[Martingales in Continuous Time|martingale]] in $L^2$.

>[!claim]
>Let $0\leq s = t_0 < t_1 < \dots < t_p = t$. Then,$$\EE\left[\sum_{i = 1}^p\left(M_{t_i} - M_{t_{i-1}}\right)^2 | \FFF_s\right] = \EE\left[M_t^2 - M_s^2 | \FFF_s\right] = \EE\left[\left(M_t - M_s\right)^2 | \FFF_s\right]$$