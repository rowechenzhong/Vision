---
aliases:
  - Birkhoff
---
>[!theorem] Birkhoff
> Suppose $(E,\mathcal{E}, \mu)$ is $\sigma$-finite, and $f$ is integrable on $E$. Then, there exists an invariant function $\bar{f}$ , with $\mu(\abs{\bar{f}}) < \mu(\abs{f})$, such that $S_n(f) / n \to \bar{f}$ a.e. as $n\to \infty$.

The intuition here is that as things get scrambled by $\theta$, all of your $S_n(f) / n$ should approach their "average" through their $\theta$-futures. This average is obviously $\theta$-invariant.

> [!proof] TODO
> The strategy is to show
> $$D(a,b) = \liminf_n \frac{S_n}{n} < a < b < \limsup_n \frac{S_n}{n}$$
> has measure $0$ for all $a < b$; this quickly implies the result.
> 
> You do this by subtracting a constant from $S_n$, then applying [[Time Summation|Maximal ergodic lemma]].