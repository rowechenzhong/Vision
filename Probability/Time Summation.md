---
aliases:
  - Maximal ergodic lemma
---
Suppose $f$ is measurable on $(E,\mathcal{E}, \mu)$. I would like to understand the long-term statistical behavior of $f$ as its inputs are moved under [[Ergodic Transformations|measure-preserving transformation]] $\theta$ (not necessarily ergodic!)

>[!defn] Time summation
>Let $S_0(f) = 0$, and
>$$S_n(f) = f + f\circ \theta + \dots + f\circ \theta^{n-1}.$$

First, a claim, interesting in its own right:

>[!claim] Maximal ergodic Lemma
>Let $f$ be integrable, and let $S^* = \sup_{n\geq 0} S_n(f)$. Then,
>$$
>	\int_{S^* > 0} fd\mu\geq 0
>$$

Here, $S^* > 0$ means that there exists some $k$ where $S_k(\omega) > 0$. In other words, its okay to add $\omega$, because you will later be "saved" by the terms later in the sequence. The fact that this actually works is some combinatorics. (Note that $S_0 = 0$, and thus $S^*\geq 0$).

> [!proof]- Setup
> We're just going to approximate the whole thing with finite processes. Let $S^*_n = \max_{0\leq m\leq n} S_m$ and let $A_n = \{S^*_n > 0\}$. Clearly, $A_n\uparrow \{S^*>0\}$ thus by dominated converge it suffices to show
> $$
> \int_{A_n} fd\mu > 0
> $$

> [!proof]- Combinatorics
> Clearly, for $1\leq m\leq n$,
> $$
> 	S_m = f + S_{m-1}\circ \theta \leq f + S^*_n\circ \theta
> $$
> Thus, we have the stupid bounds
> - On $A_n$, $S^*_n\leq f + S^*_n\circ \theta$.
> - On $A_n^c$, $S^*_n = 0\leq S^*_n\circ \theta$.
> 
> Thus,
> $$\int_E S^*_n d\mu \leq \int_{A_n}fd\mu + \int_E S^*_n\circ \theta d\mu = \int_{A_n}fd\mu + \int_E S^*_n d\mu$$
> and we win.