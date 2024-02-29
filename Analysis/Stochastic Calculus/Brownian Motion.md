>[!definition] Brownian Motion
>Let $(X_t)_{t\geq 0}$ be a **continuous** random process in state space $\RR^d$. $X$ is a ==**Brownian motion**== if
>1. For all $s,t \geq 0$, $X_{s+t} - X_s\sim N(0, tI)$
>2. $X_{s+t} - X_s$ is independent of $\FFF_s^X = \sigma(X_u: u \leq s)$.

>[!idea] The legend🤩

Observe that the listed conditions are pointwise, thus we cannot hope to define $X$ without the continuity condition to bootstrap to $\RR$-power. We let $p(t,x,y) = (2\pi t)^{-d/2} e^{-(x-y)^2 / (2t)}$ from now on.

# The definition, Rephrased

Here is an explicit rephrasing of the two statements (this is by definition, not deep). For all $s,t\geq 0$, measurable $A\subset \RR^d$, and measurable $K\in \FFF_s^X$,
$$
\PP(K \cap \{X_{s+t} - X_s\in A\}) = \PP(K) \int_{A} p(t,0,x)dx
$$
Here is another rephrasing, which emphasizes the trajectory picture: for all bounded measurable functions $f:\RR^d\to \RR$ and all $s,t\geq 0$,
$$\EE[f(X_{s+t})| \FFF_s^X] = (P_t f)(X_s)$$where $P_t$ is the [[heat semigroup]].

Also see [[Wiener's Theorem]] for the worldline perspective.

# Basic Properties
### Finite-dimensional Distributions
To initialize our Brownian motion, we can set $X_0 = x$ for some $x\in \RR^d$. In this case the conditions can be expressed in finite distributions. For all $n\in \NN$ and all $0 = t_0\leq t_1 < \dots < t_n$, for any Borel set $B\subset (\RR^d)^n$,$$\PP((X_{t_1},\dots,X_{t_n})\in B) = \int_B \prod_i p(t_i - t_{i-1}, x_{i-1}, x_i)dx_i$$where $x_0 = x$.

By staring at components, any $d$-dimensional Brownian motion starting at $x$ can be obtained via $X_t = x + (X^1_t + \dots + X^d_t)$ where $\{(X^i_t)_{t\geq 0}\}_{1\leq i\leq d}$ are $d$ independent $1$-dimensional Brownian motions, and any particular set of such Brownian motions creates a $d$-dimensional Brownian motion.

### Finite-dimensional Moments
For all $i,j = 1,\dots, d$,$$\EE[X_t] = x,\qquad \Cov[X^i_s, X^j_t] = \EE[(X^i_s - x^i)(X^j_t - x^j)] = (s\land t)\delta_{ij}.$$Of course, a Gaussian is determined by its means and covariances. Thus, if $(X_t)_{t\geq 0}$ is a **continuous** [[Gaussian process]] with the above moments, it is automatically a Brownian motion starting at $x$.

### Scaling Laws
Let $\sigma > 0$ and $U\in O_d(\RR)$. Let $(X_t)_{t\geq 0}$ be a Brownian motion in $\RR^d$ starting at $0$. Then $\sigma X_{\sigma^{-2} t}$ and $(UX_t)_{t\geq 0}$ are also Brownian motions in $\RR^d$ starting at $0$.