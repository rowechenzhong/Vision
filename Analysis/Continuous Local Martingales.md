>[!definition] Continuous Local Martingale
>An adapted path-continuous process $M$ such that $M_0 = 0$ a.s. is a ==**Continuous Local Martingale**== if there exists a nondecreasing sequence of stopping times $T_n\uparrow \infty$ such that for every $n$, $M^{T_n}$ is a UI martingale.

>[!example] This Gambler will be ruined by time $k$, but they don't know when
>Let $T = \inf\{t: B_t = 1\}$; note $T < \infty$ a.s., so wlog $T < \infty$ always. Consider the process
>$$
>\begin{cases}
>	B^T_{tT/k}: t < k\\
>	1: t \geq k
>\end{cases}
>$$
>This is intuitively a stopped martingale; you should verify this!