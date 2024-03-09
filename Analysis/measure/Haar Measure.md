Here's a pretty legendary extension of Lebesgue measure. 
> [!definition] Topological Group
A ==**topological group**== is a group $G$ with a topology such that 
> -  Multiplication $G\times G\to G$ is continuous. 
> -  Inversion $G\to G$ is continuous. 

 
> [!definition] LCA Group
 A ==**locally compact abelian group**== is an abelian topological group $G$ which is locally compact. 

 Lol. Anyways: 
> [!definition] Haar Measure
 Let $G$ be a locally compact abelian group. A ==**Haar measure**== on $\BBB(G)$ is a measure $\mu$ that is: 
> -  ==**Group invariant:**== $\mu(gA) = \mu(A)$ for all $g\in G$ and $A\in \BBB(G)$. 
> -  $\mu(K) < \infty$ for any compact $k\in \BBB(G)$. 
> -  If $S$ is measurable, then $\mu(S) = \inf \mu(U)$ where $U$ is open and $S\subset U$. 
> -  If $U$ is open, then $\mu(U) = \sup \mu(S)$ where $S$ is compact and $S\subset U$. 

 In fact, this measure is *unique* up to scaling. This is really overpowered.