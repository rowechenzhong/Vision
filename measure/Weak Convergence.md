---
aliases:
  - Convergence in Distribution
  - converges weakly
  - in distribution
---
Suppose $\mu$ is a [[Borel Measure|Borel Probability Measure]] on $\RR^d$. Let $\mu_n$ be a sequence of such measures. Then, ==**$\mu_n$ converges weakly to $\mu$**== if $\mu_n(f)\to \mu(f)$ for all continuous bounded $f$.

Given a random variable $X$ on $\RR^d$ and a sequence of random variables $X_n$, $X_n\to X$ ==**weakly**== if $\mu_{X_n}\to \mu_X$ weakly. The random variables don't even have to be defined on the same probability space; this is purely a statement about their [[probability objects#^c1cbb1|laws]].

This is equivalent to ==**convergence in distribution**==, which is when $F_n(x)\to F(x)$ for all $x\in \RR$ such that $F(x)$ is continuous. Here, $F$ are the [[probability objects#^a89c00|CDFs]].