We will be discussing families of random variables $(X_t)_{t\geq 0}$.

- Such a family is ==**continuous**== if it is pointwise; for all $\omega \in \Omega$, the path $t\mapsto X_t(\omega): [0,\infty)\to \RR$ is continuous.
- Such a family is ==**cadlag**== if it is pointwise. (See [[cadlag]]). 

Then, a continuous random process can be considered as a random variable in $C([0, \infty), \RR)$ via $X(\omega) = \left(t\mapsto X_t(\omega): t\geq 0\right)$. Similarly, a cadlag random process is an RV in $D([0, \infty), \RR)$.

For all $n$ and $t_1 < \dots < t_n\in [0,\infty)$, consider the law $\mu_{t_1,\dots, t_n}$ on $\RR^n$ given by
$$\mu_{t_1,\dots,t_n}(A) = \PP\left((X_{t_1},\dots, X_{t_n})\in A\right),\qquad A\in \BBB(\RR^n)$$
We call all such laws ==**finite-dimensional distributions**== of a continuous or cadlag process. By definition the cylinder sets are a generating $\pi$-system, thus they determined uniquely the law of $X$.