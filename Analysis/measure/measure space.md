> [!definition] Measure Space
> A ==**measure space**== is a triple $(\Omega, \AAA, \mu)$ where $\Omega$ is a set, $\AAA$ is a $\sigma$-[[measurable space|algebra of subsets]], and $\mu$ is a [[measure]].
> 
> In probability, $\Omega$ is commonly called the ==**state space**== or ==**outcome space**==, and elements of $\AAA$ are called ==**events**==.

> [!problem] Basic Properties
>
> 1. If $A\subseteq B$ are measurable, then $\mu(A) \leq \mu(B)$, because $\mu(B) = \mu(A) + \mu(B\setminus A)$.
> 2. We write $A_i \uparrow A$ if $A_1 \subseteq A_2 \subseteq \dots$ and $A = \bigcup_i A_i$. Then, 
> $$ \mu(A) = \lim_i \mu(A_i).$$ 
> 3. We write $A_i \downarrow A$ if $A_1 \supseteq A_2 \supseteq \dots$ and $A = \bigcap_i A_i$. If $\mu(A_1) < \infty$, then
> $$ \mu(A) = \lim_i \mu(A_i) $$

> [!solution]-
>
> 1. $B = A \cup (B \setminus A)$, and the two sets are disjoint.
> 2. $A = \bigcup_i (A_i \setminus A_{i-1})$, each of which is disjoint. This summation converges because its partial sums are increasing.
> 3. Apply the previous result to $A_1 \setminus A_i$.

> [!idea] Countable Additivity
> The problem with uncountable sets is that they're a bit too large. Example: Let $S$ be an uncountable set of positive real numbers. Then, if you split into buckets $(\frac{1}{n + 1}, \frac{1}{n}]$, then there are only countably many buckets, thus some bucket has infinitely many elements of $S$. Conclusion: if $S$ is uncountable, there exist finite sets that have arbitrarily large sums.

> [!idea] Almost Surely
> A property $P$ holds ==**almost surely**== if it holds for all $\omega \in \Omega$ except for a set of measure zero. In measure theory, essentially all statements are only true almost surely; measure theory cannot distinguish between two sets that differ by a set of measure zero.

> [!problem] Almost Sure Things
> A ==**probability space**== is a measure space $(\Omega, \AAA, \mu)$ where $\mu(\Omega) = 1$. Show that the intersection of countably many measurable sets of measure $1$ has measure $1$.

> [!solution]-
> Let $A_1, A_2, \dots$ be measurable sets of measure $1$. Then, their complements $\conj{A}_1, \conj{A}_2, \dots$ have measure $0$. By countable additivity, the union of these complements has measure $0$. Thus, the intersection of the $A_i$ has measure $1$.

The most famous measure is the [[Lebesgue Measure]] over $\RR$.