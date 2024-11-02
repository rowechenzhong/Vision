---
aliases:
  - Markov Chains
---
Let $(\FFF_{n})_{n \in \NN}$ be a filtration on a probability space $(E, \mathcal{E}, \PP)$.

In this paper, $E$ will be a countable set. Then, measures $\mu$ on $E$ are precisely given by their values on singletons sets $\mu_x = \mu(\{x\})$, and the integral of a function can be written as a "contraction"
$$\mu(f) = \mu \cdot f = \sum_{x \in E} \mu_x f(x).$$
Keeping in this linear algebra mindset, a ==**transition matrix**== on $E$ is a matrix $P = (p_{xy}: (x, y) \in E^2)$ such that each row is a probability distribution on $E$. That is, $p_{xy} \geq 0$ for all $x, y \in E$ and $\sum_{y \in E} p_{xy} = 1$ for all $x \in E$. See [[Linear Algebra Intuition for Markov Chains]].

> [!definition] Markov Chain
> An adapted process $(X_n)_{n \in \NN}$ is a ==**Markov chain with transition matrix**== $P$ if
> $$\forall n \in \NN \forall A \in \FFF_n \forall x,y\in E,\qquad A\subset \{X_n = x\}\land \PP(A) > 0 \implies \PP(X_{n+1} = y | A) = p_{xy}.$$

This is exactly what you think it means; if we currently have $\FFF_n$ knowledge, the transition probabilities are given by $p_{xy}$. If this is the case though, we get the 18.615 definition:

>[!claim] No extra knowledge
>If $(X_n)_{n\geq 0}$ is a random process and $\FFF_n = \sigma(X_k: k \leq n)$, then $X$ is a MC with initial distribution $\mu$ and transition matrix $P$ iff for all $n$ and $x_0,\dots, x_n\in E$,
>$$\PP(X_0 = x_0,\dots, X_n = x_n) = \mu_{x_0}p_{x_0x_1}\dots p_{x_{n-1}x_n}.$$

The markov transition induces a probability measure on the space of sequences $E^* = \{(x_n: n\geq 0)\}$. Let $X_n: E^*\to E$ via $X_n(x) = x_n$, and let $\mathcal{E}^* = \sigma(X_k:k\geq 0)$.

>[!claim] Unique induced measure
>For each $x\in E$, there is a unique probability measure $\PP_x$ on $(E^*, \mathcal{E}^*)$ such that $(X_n)_{n\geq 0}$ is a MC with transition matrix $P$ starting from $x$.

This is obvious; the previous claim tells you what your measure is on all cylinders. Integration over this measure is denoted $\EE_x$.

# Martingales from Markov Chains

> [!theorem] Functions on Markov Chains are martingales
> Let $X$ be adapted on $E$. Then, $X$ is a MC with transition matrix $P$ iff for all bounded functions $f:E\to \RR$,$$M^f_n = f(X_n) - f(X_0) - \sum_{k = 0}^{n-1} ((P - I)f)(X_k)$$ is a martingale.

This is a good test of whether you understood notation. 

>[!problem] Prove it.

>[!solution]- Notation Shuffling
> Well, by telescoping, the martingale condition is iff$$\EE[f(X_{n+1}) \id_A] = \EE[(Pf)(X_n)\id_A]$$for all $A\in \FFF_n$ for all bounded functions $f$. By linearity, this is iff the above is true for all point functions $f(x) = \delta_{xy}$ and $A\subset \{X_n = x\}$ for some $x,y$. In this context, the statement becomes
> $$\PP(X_{n+1} = y \land \id_A) = \EE\left(p_{xy} \id_A\right)$$
> as desired.

# Harmonic Functions

A bounded function $f$ on $E$ is ==**harmonic**== if $Pf = f$. Then $f(X_n)$ is a bounded martingale; by [[Martingale Convergence Theorems|MCT]] it admits an AS-$L^p$ limit for all $p < \infty$.

More generally, for $D\subset E$ a bounded function $f$ is ==**harmonic on $D$**== if $Pf\big\vert_D = f\big\vert_D$.

Harmonic functions are pretty tight. If $\pa D = E\setminus D$ and we fix a bounded $f$ on $\pa D$, it turns out that there is essentially one way to make a bounded harmonic function on $D$ which agrees with this (observe that the harmonic condition extends to edges depth-$1$ outside of $D$).

>[!theorem] Harmonic Extension
> Let $T = \inf \{n\geq 0: X_n\in \pa D\}$ and $u(x) = \EE_x\left(f\left(X_t\right)\id_{T\leq \infty}\right)$. Then, $u$ is bounded and harmonic in $D$, while $u = f$ on $\pa D$.
> 
> If $\PP_x(T < \infty) = 1$ for all $x\in D$, then $u$ is the unique bound extension of $f$ which harmonic in $D$.