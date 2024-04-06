---
aliases:
  - adapted
  - progressive
---
A random process $(X_t)_{t\geq 0}$ is ==**adapted**== if for every $t\geq 0$, $X_t$ is $\FFF_t$-measurable. It is ==**measurable**== if the mapping $(\omega, s)\mapsto X_s(\omega)$ on $\Omega\times [0,\infty)$ is measurable on $\FFF\otimes \BBB([0,\infty))$.

A random process is ==**progressive**== if for every $t\geq 0$, the mapping $(\omega,s)\mapsto X_s(\omega)$ is measurable for the $\sigma$-field $\FFF_t\otimes \BBB([0,t])$.

>[!idea]- This generates a ==**progressive $\sigma$-field**==.
>Details: let $\PPP_t$ be the sigma field $\{A \sqcup B: A\in \FFF_t\otimes \BBB([0,t]), B\subset \Omega\times (t,\infty)\}$; then $\PPP = \bigcap \PPP_t$. A random process is progressive iff it is measurable on $\PPP$ (this is obvious).

>[!claim]
>Suppose $(X_t)_{t\geq 0}$ takes values in a metric space equipped with its Borel $\sigma$-field. If $X$ is  adapted and right-continuous or left-continuous, then $X$ is progressive.