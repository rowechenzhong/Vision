---
aliases:
  - Poisson
  - Poisson distribution
---
A ==**Poisson distribution**== with ==**rate**== $\lambda$ is $\frac{\lambda^k e^{-\lambda}}{k!}$ over $\ZZ_{\geq 0}$.

A ==**Poisson process**== $(N_t)_{t\geq 0}$ is an increasing right-continuous random process over $\ZZ_{\geq 0}$ such that:
- $N_0 = 0$.
- $N_t$ has [[Independent Increments]].
- $N_t$ has a Poisson distribution with parameter $\lambda t$.