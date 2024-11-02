Let $\sigma > 0$ and $r\in \RR$. Then, the ==**geometric Brownian motion**== is the solution to $$dX_t = \sigma X_t dB_t + rX_t dt.$$
By Ito's formula on $\log X_t$,
$$
X_t = X_0 \exp\left( \sigma B_t + \left(r - \frac{\sigma^2}{2}\right)t\right).
$$

This has the nice property that successive ratios are independent:
$$
	\frac{X_{t_2} - X_{t_1}}{X_{t_1}}, \frac{X_{t_3} - X_{t_2}}{X_{t_2}},\dots
$$
This has applications to mathematical finance. In the [[Black-Scholes equation]], it is used the model the price of the underlying asset to a derivative.