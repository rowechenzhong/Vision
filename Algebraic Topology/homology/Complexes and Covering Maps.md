---
aliases:
  - covering maps and homology
---
Let $\pi: \tilde{X}\to X$ be a [[Regular Covering Spaces|regular]] covering map, with [[Deck Transformation|covering group]] $G$.

>[!claim]
>$C_*(\tilde{X})$ is a complex of free $\ZZ G$-modules, and $C_*(X) = \ZZ\otimes_{\ZZ G} C_*(\tilde{X})$.

$C_*(\tilde{X})$ is obviously a complex of free $\ZZ G$-modules, because $G$ consists of automorphisms of $\tilde{X}$. We wish to show that the map $p:C_*(\tilde{X})\to C_*(X)$ is surjective and has kernel $\{g \sigma \sim \sigma\}$. Well, $p$ is obviously surjective, because we can left any map $\Delta^n\to X$. $p$ obviously has said kernel, because:
- $p\circ \sigma = p\circ g\circ \sigma$.
- By [[unique lifting]], if $p\circ \sigma = p\circ \conj{\sigma}$, then there exists some $g\in G(X)$ such that $\sigma = g \circ \conj{\sigma}$.


By the [[Fundamental theorem of homology algebra]], $H_*(X) \cong H_*(\ZZ\otimes_{\ZZ G} C_*(\tilde{X}))$. Most notably, if $X$ is contractible, i.e. $C_*(\tilde{X})$ is some [[Free Resolution]] of $\ZZ$ as a $\ZZ G$ module, then $H_*(X) = H_*(\ZZ\otimes_{\ZZ G}C)$.

>[!idea]
>I don't actually understand this too well. Oh well! moving on.