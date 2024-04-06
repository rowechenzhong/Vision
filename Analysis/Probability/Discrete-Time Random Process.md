---
aliases:
  - random process
---
A ==**random process**== is simply a sequence of random variables $X = (X_n)_{n\geq 0}$ over the same state space $(\Omega, \FFF, \PP)$. This induces a natural [[filtration]]
$$\FFF_n^X = \sigma(X_0,\dots, X_n)$$
representing knowledge of $X$ at causal time $n$.

We say that $(X_n)_{n\geq 0}$ is ==**adapted to a filtration $(\FFF_n)_{n\geq 0}$**== if $X_n$ is $\FFF_n$-measurable always. In other words, $\FFF_n^X\subseteq \FFF_n$; our knowledge of $X_n$ is captured by by $\FFF_n$.
# Adjectives

$X$ is ==**integrable**== if all $X_n$ are. $X$ is defined to be [[Uniformly Integrable]] in the usual sense. $X$ is ==**$L^p$ bounded**== if it is uniformly bounded; $\sup_{n\geq 0} \norm{X_n}_p < \infty$.