---
aliases:
  - QV
  - Quadratic Variation
---
# Initial Interface

We assume a complete filtration.

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

Uniqueness is clear because FVP $\cap$ CLM = $\{0\}$. The proof of existence and the characterization follow from elementary but somewhat involved proofs. Here are the main steps:
1. Consider a bounded $M$ and find a mesh on $[0,K]$. Then, define bounded martingale $X^n_t = \sum_1^{p_n} M_{t^n_{i-1}} \left(M_{t^n_i\land t} - M_{t^n_{i-1}\land t}\right)$.
2. Prove this lemma (big bash): $\lim_{n,m\to \infty} \EE\left[\left(X^n_K - X^m_K\right)^2\right] = 0$. No external lemmas are used.
3. By Doob's inequality in $L^2$, $\lim_{n,m\to \infty} \EE\left[ \left(\sup_{0\leq t\leq K} (X^n_t - X^m_t)\right)^2\right]\to 0$. We then obtain a pointwise AS-convergent sequence, and extract AS-continuous sample paths via uniform convergence.
4. Finish.

# Basic Properties

- Let $M$ be a CLM and $T$ a stopping time. Then a.s. for all $t\geq 0$, $\braket{M^T, M^T}_t = \braket{M,M}_{t\land T}$.
- If $M$ is a CLM and $M_0 = 0$, then $\braket{M, M} = 0$ iff $M = 0$. Indeed, if $M_t^2$ is a nonnegative CLM then [[Continuous Local Martingales|it is a supermartingale]], thus $\EE[M_t^2] \leq \EE[M_0^2] = 0$ and $M_t = 0$ a.s. for all $t$.

>[!idea] $L^2$ is strong
>The following bounds are really good, and occur a lot in practice. The moment you shield $\braket{M,M}$, everything becomes regular.

> [!claim] $L^2$ bounds
> Suppose $M$ is a CLM with $M_0 \in L^2$.
> - $M$ is a true martingale bounded in $L^2$ (we say $M\in \Hh$) iff $\EE[\braket{M,M}_\infty] < \infty$. This also implies $M^2 - \braket{M,M}$ is a UI martingale.
> - $M$ is a true martingale such that $M_t \in L^2$ for all $t\geq 0$ iff $\EE[\braket{M,M}_t] < \infty$ for every $t\geq 0$. This also implies $M^2 - \braket{M, M}$ is a martingale.

> [!proof]- Forward, part 1
> Suppose $M$ is a true martingale bounded in $L^2$, i.e. $\sup_{t\geq 0} \EE[M_t^2] = \frac{C}{4} < \infty$. By [[Discrete Doob's Lp Inequalities|Doob's Lp inequality]], $\EE[\sup_{t\geq 0} M_t^2] \leq C$ which is really good.
> 
>>[!idea]
>>Now, if $M^2 - \braket{M,M}$ were a martingale, we would be done, because
>>$$\EE\left[\braket{M,M}_t\right] = \EE[M^2_t] \leq \EE[\sup_s M_s^2] \leq C$$ and we can use monotone convergence because $\braket{M,M}$ is IP.
> 
> So we shield with $S_n = \inf\{t\geq 0: \braket{M,M}_t\geq n\}$. The CLM $(M^2)^{S_n} - \braket{M,M}^{S_n}$ is dominated by $\sup M_s^2 + n$, thus$$\EE[\braket{M,M}^{S_n}_t] \leq C$$as desired. If we take $n$ to $\infty$, this recovers $\EE[\braket{M,M}_t]\leq C$, and if we take $t\to \infty$ we conclude by monotone convergence.

The other directions are more of the same flavor of proof, omitted.

>[!problem] Lol
>Prove part 2 using part 1. (No calculations!)

>[!solution]-
>Consider $M^t_s = M_{s\land t}$.

A problem from your 676 midterm:

>[!claim] Exact characterization of $M_\infty$ existence
>Let $M$ be a CLM. The following two sets are AS equal:
>$$
>	\left\{\lim_{t\to\infty} M_t \text{ exists and is finite}\right\},\qquad \{\braket{M,M}_\infty < \infty\}
>$$


# Important Lemma

This lemma is so important for calculations; it's what makes our [[Riemann Summation Shorthand]] intuition tick. I will write out the full proof because I was confused about it for a long time.

> [!claim] The measures actually work
> Give me a mesh. Let $\mu_n$ be the [[Random Measure]] on $[0,t]$ which assigns weight $\left(X_{t_i} - X_{t_{i-1}}\right)^2$ to $\{t_{i-1}\}$, i.e. $$\mu_n = \sum_i \left(X_{t_i} - X_{t_{i-1}}\right)^2 \delta_{\{t_{i-1}\}}.$$
> The $\mu_n$ converge [[Random Measure|weakly in probability]] to $\mu$, the measure corresponding to $\braket{X,X}$.

>[!proof] Diagonalization
> Start by letting $D_n$ be the dyadics such that $D = \bigcup D_n$ is countable. By definition, for any particular $s\in D$, $\mu_n\left([0,s]\right)\to \braket{X,X}_s$ in probability. Often, we will desire that this holds for all $s$ at once. This is precisely what we're going to show here.
> 
> By diagonalization, we can extract a subsequence such that, for all $s\in D$, $\PP\left(\mu_n([0,s])\to \braket{X,X}_s\right) = 1$. This follows because any $\PP$-convergent sequence admits an AS-convergent subsequence.
> 
> However, then, $\PP\left( \bigcap_{s\in D} \left\{\mu_n([0,s])\to \braket{X,X}_s\right\}\right) = 1$.

>[!proof] Some quick analysis
> Hence, let $F_n$ be the CDF of $\mu_n$. $\PP\left(\bigcap_{s\in D} F_n(s)\to \braket{X,X}_s\right) = 1$. Because $F(s) = \braket{X,X}_s$ is path-continuous, on almost-sure $\omega$, for any $\eps > 0$, we can always find $\alpha < s < \beta$ inside $D$ such that $F(s) - \eps/2 < F(\alpha) \leq F(s) \leq F(\beta) < F(s) + \eps/2$. Then, there will exist an $n$ such that on all $m\geq n$, $F(s) - \eps < F_m(\alpha) < F_m(s) < F_m(\beta) < F(s) + \eps$.
> 
>>[!idea]
>>This could still have worked if $F(s)$ was merely taken to be right-continuous; the definition of weak convergence only requires this convergence to hold on every $s$ such that $F(s)$ is left-continuous.

>[!proof] Using the [[types of convergence|$\PP$ to AS boostrap]]
> Hence, we've shown that there is a subsequence of our original mesh along which $\mu_n\to \mu$ weakly, almost surely.
> 
> But nothing about our original mesh was special. This is true for any subsequence of our original mesh, thus we obtain that $\mu_n\to \mu$ weakly in probability.

>[!idea] Reminding myself how to use this
> Along our subsequence, for almost all $\omega$, for continuous (and hence bounded on compact $[0,t]$) $g(s)\in C_b$, $\int g(s) d\mu_n(s)\to \int g(s) d\mu(s)$. Notably, for any path-continuous random processes $g_s(\omega)$, $\int g(s) d\mu_n(s)\to \int g(s)d\mu(s)$ almost surely. This $Z_n = \int g(s)d\mu_n(s)$ is just some random variable.
> 
> Hence, for any path-continuous random process $g_s(\omega)$, along any subsequence of our mesh, there is some AS-convergent subsequence of $Z_n$'s. Thus, for all path-continuous random processes $g_s(\omega)$, $\int g(s)d\mu_n(s)\to \int g(s)d\mu(s)$ in probability.