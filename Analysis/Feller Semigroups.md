---
aliases:
  - Theorem on how to identify L
---
Let $E$ be a metrizable locally compact topological space which is countable at infinity. (So... $E = \RR^d$ works, and that's the only example I'll ever think about). $E$ has Borel $\sigma$-field. Let $C_0(E)$ denote all continuous real functions on $E$ which tend to $0$ at infinity, which is a Banach space for the supremum norm.

Great. The whole point of a Feller Semigroup is that we force $Q_t$ to be an operator on $C_0(E)$ and satisfy a path-wise regularity condition.

>[!definition] Feller Semigroup
>A transition semigroup is a ==**Feller Semigroup**== if
>- Each $Q_t$ is an operator on $C_0(E)$.
>- For each $f\in C_0(E)$, $\norm{Q_t f - f} \to 0$ as $t\to 0$.

>[!idea]
>The second line is non-trivially equivalent to the property that for each $f\in C_0(E)$, $Q_tf\to f$ pointwise as $t\to 0$.

A Markov process with respect to a Feller semigroup is called a ==**Feller Process**==.

> [!claim] Path Continuity!
> For fixed $f\in C_0(E)$, the mapping $\RR_+\to C_0(E)$ via $t\mapsto Q_t f$ is uniformly continuous! Indeed, $$\lim_{t\downarrow 0}\norm{Q_{s+t} - Q_s f} = \lim_{t\downarrow 0} \norm{Q_s ( Q_t f - f)} = 0,$$and the $Q_s$ are contractions.

We now summarize some straightforward analytic results.

>[!definition] Generator, Domain
>Let $L$ be the operator $Lf = \lim_{t\downarrow 0} \frac{Q_t f - f}{t}$. Let $D(L)$ be the ==**domain**== of $L$, which is simply the subspace of $C_0(E)$ on which $L$ converges.

The intuition is that $Q_t = e^{Lt}$. To this end:
- $D(L)$ is dense in $C_0(E)$.
- For any $\lambda$, $\{R_\lambda f: f\in C_0(E)\} = D(L)$.
- For $f\in D(L)$, $Q_s f \in D(L)$, and $L Q_s f = Q_s L f$.
- For every $f\in D(L)$, $Q_t = 1 + \int_0^t Q_s L ds$.
- $R_\lambda: C_0(E)\to D(L)$ and $\lambda - L: D(L)\to C_0(E)$ are inverses; in particular they are each bijective.
- Hence, given an $L$ defined on subspace $D(L)$, there is at most one unique semigroup $(Q_t)_{t\geq 0}$ corresponding to $L$.

>[!example]
>For brownian motion on $\RR$, after some computation we can show $D(L)$ is exactly $\{h\in C^2(\RR): h, h''\in C_0(\RR)\}$, and $Lh = \frac12 h''$. This coincides with your intuition on the heat equation.

# Identifying $D(L)$

>[!idea]
>In general, it is hard to identify $D(L)$ exactly. The following allows one to pick out individual elements.

Fixing $(Q_t)$, for each $x\in E$, we let $(X^x_t)_{t\geq 0}$ be a path-**cadlag** Feller process such that $\PP(X^x_0 = x) = 1$.

>[!theorem]
>Let $h,g\in C_0(E)$. Then, $h\in D(L)$ and $Lh = g$ iff for every $x\in E$,
>$$h(X^x_t) - \int_0^t g(X^x_s)ds$$ is a martingale wrt $(\FFF_t)$.

This is intuitive; $\EE[h^x_{t+s}] = Q_sh(X^x_t)$, and for small $ds$, $Q_{ds} = e^{Lds} = 1 + Lds$, thus $\pa_t \EE[h^x_t] = L h(X^x_t)$.

> [!example] nD Brownian motion via Ito's Formula!
> For any $h\in C^2(\RR^d)$, $$h(X_t) - \frac12 \int_0^t \Delta h(X_s) ds$$ is a CLM by Ito's formula. If $h, \Delta h \in C_0(\RR^d)$, then they are bounded, and this guy is bounded uniformly by some linear function. Hence it is a true martingale, $h\in D(L)$, and $Lh = \frac12 \Delta h$.
> 
> (Notice that we did not span $D(L)$, which would require more work, but is often unnecessary).