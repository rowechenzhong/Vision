---
aliases:
  - Singular Complex
---
A ==**singular $n$-simplex**== in a space $X$ is a continuous map $\Delta^n\to X$. We define $C_n(X)$ as the space of $n$-chains as usual, and define the boundary map by restricting to faces;$$\pa_n(\sigma) = \sum_i (-1)^i \sigma\vert_{[v_0,\dots, \hat{v_i},\dots, v_n]}.$$The ==**singular homology group**== is thus $H_n(X) = \ker \pa_n / \im \pa_{n+1}$.

It will turn out that the singular homology groups coincide with the [[Simplicial Homology]] groups for $\Delta$-complexes, but for now we make a more crude observation:
- Singular Homology is obviously more general than simplicial homology; each $C_n(X)$ is much larger.
- If one takes a space $X$ and assigns an $n$-simplex to each singular $n$-simplex, modding out by the obvious relations, we obtain a (large) $\Delta$-complex called $S(X)$ whose simplicial homology is manifestly the same as the singular homology.

See [[Reduced Homology Groups]].

This immediately induces a [[Chain Complexes|chain complex]] for the same reason as a [[Simplicial Homology]]. To make the dictionary complete, we need to prove two statements:
 - [[Maps of Spaces induce Chain Maps]]
 - [[Homotopies of maps induce homotopies of chain maps]]

# Introductory Problems

>[!problem] Disjoint Unions
>Compute the homology groups of the disjoint union $H_*(X\sqcup Y)$

>[!solution]-
>This is patently obvious; $C_n, B_n, Z_n, H_n$ are each direct sums of the corresponding objects.

>[!problem]
>Determine $C_*(\{*\})$ and its homology.

>[!solution]-
>Well:
> - $C_n(\{*\}) \cong \ZZ$ for $n\geq 0$ and $0$ otherwise.
> - $\pa_n = 1$ for even $n\geq 2$, and $0$ otherwise
> - Thus $B_n$ is $\ZZ$ for odd $n\geq 1$ and $0$ otherwise.
> - And $Z_n$ is $\ZZ$ for odd $n\geq 1$, $\ZZ$ for $n = 0$, and $0$ otherwise.
> - Thus $H_n$ is $\ZZ$ for $n = 0$, and $0$ otherwise.