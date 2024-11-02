Here is another [[point-set results on covering spaces|point-set]] result.
> [!example] Compactness
 In small covering spaces, $X$ is compact iff $\tilde{X}$ is compact. 
 
> [!proof] 
 Given $X$ is compact: Let $\{\tilde{U}_\alpha\}$ be an open cover of $\tilde{X}$. Pick any $x\in X$, and an evenly-covered neighborhood $V$ of $x$. Then, $p^{-1}(V)$ is a disjoint union of open sets $\{\tilde{V}_i\}_{i\leq n}$ containing the fiber $p^{-1}(x) = \{\tilde{x}_i\}_{i\leq n}$, respectively. Now, $\{\tilde{U}_\alpha\}$ was an open cover. Thus, for each element of the fiber $p^{-1}(x)$, I can find an open set $\tilde{U}_i$ containing $\tilde{x}_i$. Let $\tilde{K}_i = \tilde{U}_i\cap \tilde{V}_i$, which is an open neighborhood of $\tilde{x}_i$ which is now inside $\tilde{U}_i$. As a covering space, I know that $\tilde{U}_i$ is mapped homeomorphically to $U$ by $p$. Thus, $\tilde{K}_i$ is mapped homeomorphically to some open set $K_i$ in $U\subset X$. Finally, let $K = \cap K_i$. 
>  
>  
>  
>  -  $x\in K$ is a neighborhood. 
>  
>  -  $K$ is evenly covered. 
>  
>  -  The pre-image of $K$ is a finite union of $\tilde{K}_i$'s, each of which is a subset of some $\tilde{U}_\alpha$. 
>  
>  Perfect! Construct such a $K$ for each $x\in X$, and extract a finite subcover. This lifts to a finite subcover consisting of a finite number of $\tilde{K}_i$'s, each of which can be expanded to some $\tilde{U}_\alpha$. 
> 
> 
>  Given $\tilde{X}$ is compact: observe that the continuous image of a compact set is compact. 

> [!idea] 
> A covering space is called *proper* if the pre-image of any compact set is compact. Any proper space must be small, thus our argument shows that the proper spaces are precisely the small covering spaces.
>