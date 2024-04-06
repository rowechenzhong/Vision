---
aliases:
  - QV
  - Quadratic Variation
---
# Initial Interface

>[!theorem] Quadratic Variation Uniqueness and Existence
>Let $M$ be a CLM. There exists an **increasing process** called the ==**Quadratic Variation**== $\braket{M, M}$, unique up to indistinguishability, such that $M_t^2 - \braket{M,M}_t$ is a CLM.

>[!theorem] QV is Variance additivity along a mesh a.s.
>For every $t > 0$, pick a mesh.
> $$\braket{M,M}_t = \lim\sum \Delta M^2$$
>>[!idea]- Expand
>>$$\braket{M,M}_t = \lim_{n\to \infty} \sum_{i = 1}^{p_n} \left(M_{t^n_i} - M_{t^n_{i-1}}\right)^2$$
>>[[types of convergence|in probability]].

>[!example] Brownian Motion
>$\braket{B,B}_t = t$.

Uniqueness is clear because FVP $\cap$ CLM = $\{0\}$. The proof of existence and the characterization follow from elementary but somewhat involved proofs, omitted.

# Basic Properties

- Let $M$ be a CLM and $T$ a stopping time. Then a.s. for all $t\geq 0$, $\braket{M^T, M^T}_t = \braket{M,M}_{t\land T}$.
- If $M$ is a CLM and $M_0 = 0$, then $\braket{M, M} = 0$ iff $M = 0$. Indeed, if $M_t^2$ is a nonnegative CLM then [[Continuous Local Martingales|it is a supermartingale]], thus $\EE[M_t^2] \leq \EE[M_0^2] = 0$ and $M_t = 0$ a.s. for all $t$.

>[!idea] $L^2$ is strong
>The following bounds are really good, and occur a lot in practice. The moment you shield $\braket{M,M}$, everything becomes regular.

> [!claim] $L^2$ bounds
> Suppose $M$ is a CLM with $M_0 \in L^2$.
> - $M$ is a true martingale bounded in $L^2$ iff $\EE[\braket{M,M}_\infty] < \infty$. This also implies $M^2 - \braket{M,M}$ is a UI martingale.
> - $M$ is a true martingale such that $M_t \in L^2$ for all $t\geq 0$ iff $\EE[\braket{M,M}_t] < \infty$ for every $t\geq 0$. This also implies $M^2 - \braket{M, M}$ is a martingale.

> [!proof]- Forward, part 1
> Suppose $M$ is a true martingale bounded in $L^2$, i.e. $\sup_{t\geq 0} \EE[M_t^2] = \frac{C}{4} < \infty$. By [[Discrete Doob's Lp Inequalities|Doob's Lp inequality]], $\EE[\sup_{t\geq 0} M_t^2] \leq C$ which is really good.
> 
>>[!idea]
>>Now, if $M$ were a martingale, we would be done, because
>>$$\EE\left[\braket{M,M}_t\right] = \EE[M^2_t] \leq \EE[\sup_s M_s^2] \leq C$$ and we can use monotone convergence because $\braket{M,M}$ is IP.
> 
> So we shield with $S_n = \inf\{t\geq 0: \braket{M,M}_t\geq n\}$. The CLM $(M^2)^{S_n} - \braket{M,M}^{S_n}$ is dominated by $\sup M_s^2 + n$, thus$$\EE[\braket{M,M}^{S_n}_t] \leq C$$as desired. If we take $n$ to $\infty$, this recovers $\EE[\braket{M,M}_t]\leq C$, and if we take $t\to \infty$ we conclude by monotone convergence.

The other directions are more of the same flavor of proof, omitted.

>[!problem] Lol
>Prove part 2 using part 1. (No calculations!)