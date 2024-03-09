You should really be thinking about a [[Delta Complex]] $X$, but Seidel's notes are right in doing everything in terms of [[semi-simplicial set|semi-simplicial sets]] $K$.

> [!definition] Chains
> A ==**chain**== is an element in $C_n(K) = \bigoplus_{\sigma\in K_n} \ZZ \sigma$. $C_n(K) = 0$ for all $n < 0$.

> [!definition] Boundary Map
> Define the ==**boundary map**== $\pa_n:C_n(K)\to C_{n-1}(K)$ via
> $$\pa_n(\sigma) = \sum_i (-1)^i \pa_n^i(\sigma).$$
> If the dimensions are clear, we just write $\pa$ (alternatively, let $\pa: \bigoplus C_n\to \bigoplus C_n$).

By geometry, it is completely obvious that

> [!problem] A wild chain complex appeared.
> $\pa_{n-1}\circ \pa_n = 0$.

> [!solution]- Okay fine
> We verify for a single $\sigma\in K_n$.
> $$
> \begin{align*}
> 	\pa_{n-1}\circ \pa_n \sigma &= \sum_{i\leq n-1} (-1)^i \pa_{n-1}^i(\sigma) \sum_{j\leq n} (-1)^j \pa_n^j(\sigma)\\
> 	&=\sum_{i\leq n-1} \sum_{j\leq i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&=\sum_{i\leq n-1} \sum_{j\leq i} (-1)^{i+j} \pa_{n-1}^j(\sigma) \pa_n^{i+1}(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&=\sum_{j\leq n-1} \sum_{i \geq j} (-1)^{i+j} \pa_{n-1}^j(\sigma) \pa_n^{i+1}(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&=\sum_{j\leq n-1} \sum_{i > j} (-1)^{i+j + 1} \pa_{n-1}^j(\sigma) \pa_n^{i}(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&= 0 
> \end{align*}
> $$

>[!definition] Homology Groups
>Thus, $B_n(K) = \im(\pa_{n+1})\subset Z_n(K) = \ker(\pa_n)$.
>
>We define the ==**$n$-the homology group**== $H_n = Z_n(K) / B_n(K)$.

Here is some advanced material:
- [[BG Complex]]
- [[Vietoris-Rips Complex]]