---
aliases:
  - chaining lemma
---
> [!example] Chaining Covering Spaces
 Given maps $p:X\to Y$ and $q:Y\to Z$, suppose both $q$ and $p\circ q$ are covering maps. If $Z$ is ==*locally connected*==, then $p$ is a covering map. 

This is another basic [[point-set results on covering spaces|point-set result]], but it is especially nice because it only references the arrows.

> [!proof]- 
 This is one of those proofs where your hand is forced at every turn. Pick a $y \in Y$, and let $z = q(y)$, such that $y\in q^{-1}(z)$. We can use all the conditions now; pick a connected neighborhood $U$ of $z$ which is evenly covered by $q$ and $q\circ p$. We know that $$ q^{-1}(U) = \bigsqcup_{\alpha\in A} V_\alpha $$ and $$ (p\circ q)^{-1}(U) = \bigsqcup_{\beta\in B} W_\beta $$ where each $V_\alpha$ and $W_\beta$ are homeomorphic to $U$. In particular, they are all connected. Now, suppose $y\in V$. We want to show that $V$ is evenly covered, and we're going to use that the image of a connected open set is connected. Pick some $W_\beta$. 
>  
>  
>  
>  -  Suppose $p(W_\beta)$, which is connected, does *not* intersect $V$. Then we don't care about it. 
>  
>  -  Suppose $p(W_\beta)$ *does* intersect $V$. By set theory, I know that $p(W_\beta)\in \bigsqcup_{\alpha\in A} V_\alpha$. But $p(W_\beta)$ is supposed to be connected, and each $V_\alpha$ is disjoint, thus $p(W_\beta)\subset V$. Then, I can go from $W$ to $U$ via $q\circ p$, then to $V$ via $q^{-1}$ (which is a homeomorphism from $U$ to $V$)! Thus $W$ is homeomorphic to $V$. 
>  
>  By set theory, I know that $p^{-1}(V)$ is contained in $\bigsqcup W_\beta$. Thus $V$ is evenly covered.s