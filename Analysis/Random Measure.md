---
aliases:
  - weak convergence of probability measures
  - weakly in probability
---
A ==**random measure**== is a locally finite [[Transition Kernels|transition kernel]] $\zeta$ from a probability space $(\Omega, \FFF,\PP)$ to a separable complete metric space $(E, \GGG)$. Local finiteness means that $\zeta(\omega, B) < \infty$ for all bounded measurable sets $B\in \GGG$, $\PP$-almost surely.

Equivalently, it is a measure-valued random element -- subject to a couple of regularity properties again. Let $\tilde{M}$ be the collection of measures on $(E,\GGG)$. Let's give this space a $\sigma$-algebra! For all bounded measurable $\tilde{B}\in E$, we have a natural function $\mu\mapsto \mu(\tilde{B})$. We declare $\tilde{M}$ to have the $\sigma$-algebra induced by all such mappings. A random measure is then a random element of $\tilde{M}$ which is almost surely locally finite.

# Weak Convergence

A sequence of random measures $\mu_n$ converges weakly in probability to a possibly random measure $\mu$ if for all bounded continuous functions $f$ and all $\eps > 0$,$$\lim_{N\to \infty} \PP\left(\braket{\mu_n , f} - \braket{\mu, f} > \eps\right) = 0.$$Similarly, $\mu_n\to \mu$ weakly almost surely if for all bounded continuous $f$, $\braket{\mu_n, f}\to \braket{\mu, f}$ almost surely.

These are sometimes rewritten "in distribution in probability" etc.

# Weak Topology

>[!idea]
> This coincides with the usual definition of [[Weak Convergence]]. My understanding from skimming various sources is that everything is quite reasonable. Volatile, I haven't dug deep or verified these claims.

The weak topology is generated by the sub-basis $\{\mu : \abs{\int fd\mu - x} < \eps\}$ for all $x\in \RR$ and $\GGG$-measurable $f$.