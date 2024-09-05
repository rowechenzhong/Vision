---
aliases:
  - Convergence in Distribution
  - converges weakly
  - in distribution
---
>[!idea]
>Unfortunately the below results do not immediately work for signed measures (in particular, there's obviously no reason that the inequalities shown should hold).

Suppose $\mu$ is a [[Borel Measure|Borel Probability Measure]] on a metric space $E$. Let $\mu_n$ be a sequence of such measures. Then, ==**$\mu_n$ converges weakly to $\mu$**== if $\mu_n(f)\to \mu(f)$ for all continuous bounded $f$.

> [!claim] Portmanteau
> The following are equivalent.
> 1. $\mu_n\to \mu$ weakly.
> 2. $\lim\sup_n \mu_n(C) \leq \mu(C)$ for all closed sets $C$.
> 3. $\lim\inf_n \mu_n(G)\geq \mu(G)$ for all open sets $G$.
> 4. $\lim_n \mu_n(A) = \mu(A)$ for all Borel sets $A$ such that $\mu(\pa A) = 0$.

Over $\RR$ specifically, we can connect to the CDF.

>[!claim] Portmanteau
>Let $\{F_n\}$ and $F$ be the [[probability objects#^a89c00|CDFs]] of $\{\mu_n\}$ and $\mu$. $\mu_n\to \mu$ weakly on $\RR$ iff for all $x\in \RR$ such that $F$ is left-continuous, $F_n(x)\to F(x)$. The latter is often called ==**convergence in distribution**==.

Given a random variable $X$ on $E$ and a sequence of random variables $X_n$, $X_n\to X$ ==**weakly**== if $\mu_{X_n}\to \mu_X$ weakly. The random variables don't even have to be defined on the same probability space; this is purely a statement about their [[probability objects#^c1cbb1|laws]]. However, we do have the following result if $\mu_n\to \mu$ weakly:

> [!theorem] Skorokhod's representation Theorem
> Suppose that the support of $\mu$ is [[separable]] (which holds if, e.g., $E = \RR^d$). Then, there is *some* common probability space $(\Omega, \FFF, \PP)$ on which $E$-valued random variables $(X_n)$, $X$ can be defined, such that the laws of $X_n$ are $\mu_n$, and $X_n\to X$, $\PP$-almost surely (!!)

>[!idea]
>We're used to AS being way stronger than weak convergence, but that's not what this is saying at all. You can always find a bunch of random variables which witness your weakly converging laws, and because you have the freedom to pick them essentially however you want, you simply line them up such that they converge AS.

Finally, [[Prohorov's Theorem]] lets us extract a weak convergence from an *even weaker* condition.