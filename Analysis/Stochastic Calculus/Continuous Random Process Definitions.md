We will be discussing families of random variables $(X_t)_{t\geq 0}$.

- Such a family is ==**continuous**== if it is pointwise; for all $\omega \in \Omega$, the path $t\mapsto X_t(\omega): [0,\infty)\to \RR$ is continuous.
- Such a family is ==**cadlag**== if it is pointwise. (See [[cadlag]]). 

Then, a continuous random process can be considered as a random variable in $C([0, \infty), \RR)$ via $X(\omega) = \left(t\mapsto X_t(\omega): t\geq 0\right)$. Similarly, a cadlag random process is an RV in $D([0, \infty), \RR)$.

>[!idea] Borel Measure for a natural metrizable topology
>The $C([0,\infty),\RR)$ measure inherited from $\left.\BBB_R^{\otimes I}\right\vert_{C(t)}$ is equal to the metrizable topology of uniform convergence on compact time intervals; this is easily verified.

> [!idea]- Initial thoughts on the $\sigma$-algebra
> So, $\{x: x_t = 0\}$ is in the $\sigma$-algebra. If we're working with continuous or cadlag functions, then we can pinpoint $x$ on all values just by looking at a countable subset (e.g. $\{x_t: t\in \QQ\}$). So for any continuous/cadlag $f:\RR\to \RR$, $\{x: (\forall a\leq t \leq b\quad x_t = f(t)\}$ sounds like a measurable set. Ditto for $\{x: f \leq x \leq g\}$, or things like that. The exact details can be computed later.

If you restrict to a finite subset, you can get *finite-dimensional distributions*:
$$\mu_{t_1,\dots,t_n}(A) = \PP\left((X_{t_1},\dots, X_{t_n})\in A\right),\qquad A\in \BBB(\RR^n)$$
We call all such laws ==**finite-dimensional distributions**== of a continuous or cadlag process. By definition the cylinder sets are a generating $\pi$-system, thus they determined uniquely the law of $X$.

# Other topics
See [[Continuous Time Filtration]], [[Adapted Continuous-Time Processes]], and [[Continuous Time Stopping Times]]