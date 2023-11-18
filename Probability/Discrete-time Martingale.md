---
aliases:
  - supermartingale
  - martingale
  - submartingale
---
A ==**martingale**== is a discrete-time adapted integrable random process $(X_n)$ such that, for all $n\geq 0$,
$$\EE(X_{n+1} | \FFF_n) = X_n$$
If equality is replaced by $\leq$, then $X$ is a ==**supermartingale**== (its expectation decreases). If equality is replaced by $\geq$, $X$ is a ==**submartingale**== (its expectation increases).

For example, if $X$ is a martingale, then $\abs{X}$ is a non-negative submartingale.