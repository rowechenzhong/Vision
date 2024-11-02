Here are some basic point-set calculations to familiarize yourself with the topology of [[covering spaces|covering spaces]], before we dive into the algebra side of things. More advanced results are linked.

> [!example] Restriction
 Suppose $p:\tilde{X} \to X$ is a covering space and let $A\subset X$ be a subspace. Then $\tilde{A} = p^{-1}(A)$ is a covering space via the restriction $p|_{\tilde{A}}$. 

 This is clear; for any $a\in A$, pick an evenly covered $U\subset X$ in $X$. Then, $U\cap A$ will be evenly covered in $A$. 
 
> [!example] Products of Covering Spaces
 Suppose $p_x: \tilde{X}\to X$ and $p_y : \tilde{Y}\to Y$ are covering spaces. Then $\tilde{X}\times \tilde{Y}$ is a covering space of $X\times Y$ via the map $p_x\times p_y: \tilde{X}\times \tilde{Y}\to X\times Y$. 

 This is also clear; for any $(x,y)\in X\times Y$, pick evenly covered neighborhoods $U\subset X$ and $V\subset Y$. Then, $U\times V$ is evenly covered in $X\times Y$. 
 
> [!example] Hausdorff
 A *small covering space* $p : \tilde{X}\to X$ is a covering space such that $0 < \abs{p^{-1}(x)} < \infty$ for all $x$. In small covering spaces, $X$ is Hausdorff iff $\tilde{X}$ is Hausdorff. 

> [!proof]-
 Given $X$ is Hausdorff: pick $a,b\in \tilde{X}$. If $a$ and $b$ lie in the same fiber, then they are clearly separated by disjoint open sets. Otherwise, project to $p(a)$ and $p(b)$, find separated neighborhoods $A$ and $B$, take the union with suitable evenly covered neighborhoods, and project back. Given $\tilde{X}$ is Hausdorff: pick $a,b\in X$ with evenly-covered neighborhoods $U$ and $V$. Then, consider their fibers $p^{-1}(a)$ and $p^{-1}(b)$; these are finite sets. For each pair of elements in $(\tilde{a}_i, \tilde{b}_j) \in p^{-1}(a)\times p^{-1}(b)$, one can pick separated open neighborhoods of $\tilde{a}$ and $\tilde{b}$ called $\tilde{U}_{i,j} \subset \tilde{U}_i$ and $\tilde{V}_{i,j} \subset \tilde{V}_j$ respectively. Take the union of all $p\left(\tilde{U}_{i,j}\right)$, which remains an open set, and call it $U'$; ditto for $V'$. Then $U'$ and $V'$ are the disjoint open separating sets as desired. 

There is a similar result on [[compact covering spaces|compactness]].

A very important example that deserves its own page is the [[chaining covering spaces|chaining of covering spaces]].