>[!definition] Brownian Bridge
>Consider $(B_t - tB_1)_{t\in [0,1]}$; this is a Brownian Bridge.

Gaussians just work; this is the natural centered Gaussian process conditioned to be $0$ at $1$. It is known to be the limit (in a suitable sense) of basically any process of this form, by CLT or whatever I guess.

>[!example] A generic finite-dimensional limit
>Consider the cumulative sums of a random permutation of $(\underbrace{-1,\dots,-1}_N,\underbrace{1,\dots,1}_N)$, and linearly interpolate while scaling.

>[!idea] I think this idea is foreshadowing something
>This distribution is a unique stationary measure on the natural Markov chain over the admissible paths: in the above example, its called "pick a $\land$ or $\lor$ and flip it."