---
aliases:
  - Double Centralizer Property
  - Double Centralizer
  - Dual Centralizer
---
Let $V$ be a finite-dimensional vector space. Let $B\subset \End V$ be a direct sum of [[matrix algebras]]; this means that $B = \bigoplus_i \End U_i$ for some set of non-isomorphic $k$-vector spaces $U_i$. Let $A\subset \End V$ be the centralizer of $B$.

Then, representations over $B$ are completely reducible, thus$$V = \bigoplus_{i=1}^n W_i \otimes U_i$$where $U_i$ run through irreducible representations of $B$ and $W_i = \Hom_B(U_i, V)$ (these are possibly empty). $A$ is the centralizer of $B$ in $\End V$, thus $A = \bigoplus_i \End W_i$, and $W_i$ are actually irreducible $A$-modules as well. $B = \bigoplus \End U_i$.

>[!idea]
>The Double/Dual Centralizer Property is a generic phenomena about representations, and appears in other places where the above theorem does not strictly apply.