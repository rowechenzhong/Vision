Here's a basic application of the probabilistic method.

>[!example] Any graph $G$ with $m$ edges admits a bipartite subgraph with $\geq \frac{m}{2}$ edges.

Indeed, consider the following probabilistic construction. We partition $V$ into two parts, uniformly at random (across all $2^V$ possibilities), and then remove edges within each part. If we can show that the resulting bipartite graph has at least $\frac{m}{2}$ edges in expectation, then we would be done, because this implies that there exists **at least** one graph with $\geq \frac{m}{2}$ edges!

Well... yea this just works LOL. Each edge exists with probability $\frac12$. 

# Ramsey Numbers

>[!definition] Ramsey Numbers
>An ==**$k$-color Ramsey number**== $R(k; n_1, n_2, \dots, n_k)$ is the smallest positive integer $N$ such that, for any way of coloring the edges of a complete graph on $N$ vertices with $k$ colors, there is at least one monochromatic complete subgraph on $n_i$ vertices in color $i$ for some $i$.
> - For example, the **Ramsey number $R(2; m, n)$** is the smallest number of vertices $N$ such that any red-blue edge coloring of a complete graph on $N$ vertices contains a red $K_m$ or a blue $K_n$ (i.e., a monochromatic complete subgraph on $m$ or $n$ vertices).

>[!example]
>Consider the Ramsey number $R(3, 3)$, which represents the smallest number $N$ such that any edge coloring of a complete graph on $N$ vertices with two colors (say red and blue) will always contain a monochromatic triangle.
>- It is known that $R(3, 3) = 6$. This means that in any red-blue edge coloring of $K_6$ (a complete graph on $6$ vertices), there will always be at least one monochromatic triangle, either all-red or all-blue.
>- If you try to color the edges of $K_5$, you can avoid creating a monochromatic triangle, which shows that $R(3, 3)$ must be greater than $5$.

>[!theorem] Ramsey's Theorem (1929)
>$R(k, \ell) < \infty$ for all $k,\ell$.

>[!example] Erdos, 1947
>If $\binom{n}{k} 2^{1 - \binom{k}{2}} < 1$, then $R(k, k) > n$.
>
>This gives the bound
>$$
>R(k,k) > 2^{k/2} k! \left(\frac{1}{e\sqrt{2}} + o(1)\right)
>$$

Here's the proof: color each edge of $K_n$ IID at random.

Then, there are $\binom{n}{k}$ possible $K_k\subset K_n$, and each has $2^{1 - \binom{k}{2}}$ chance of being mono-$\chi$. Hence we conclude.

>[!idea] Finding hay in the haystack is hard. Smoge.

>[!theorem] Recent Developments
>The upper bound is like $R(k,k) \leq (4 - c + o(1))^k$ where $c\sim 10^{-7}$.

Um. Are we dumb or smth.

A fucking nuke appears. [[Lovasz Local Lemma]]