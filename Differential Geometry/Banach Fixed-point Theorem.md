---
aliases: []
---
>[!theorem] Banach Fixed-point
>Let $(X,d)$ be a non-empty complete metric space. Any [[contraction mapping]] $T$ admits a unique fixed point $x^*\in T$.

In fact, for any arbitrary $x_0\in X$, consider the sequence $(x_n)_{n\in \NN}$ via $x_n = T(x_{n-1})$. Then $\lim_{n\to \infty} x_n = x^*$. This obvious corollary immediately motivates the proof.

>[!proof]- Fun! Try it yourself.
> Start with some $x_0\in X$ and generate sequence $(x_n)$. This sequence is Cauchy and thus converges to some limit $x^*$. We claim $T(x^*) = x^*$; indeed, this is true by sequential continuity of $T$. This is obviously unique, because one can consider the inequality applied to two purported fixed points.