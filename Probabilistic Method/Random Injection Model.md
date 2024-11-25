Let $X$ and $Y$ be finite sets with $|X| \leq |Y|$. A ==**matching**== is a subset of edges of $K_{X, Y}$ such that each vertex in $X$ is incident to at most one edge in the matching. A ==**complete matching**== is an injection.

>[!definition] Random Injection Model yields Nonnegative Dependence graph
>We select a complete matching uniformly at random. For a given matching $F$ (not necessarily complete) in $K_{X, Y}$, let $A_F$ denote the event that $F \subseteq M$.
>
>Let $F_1, \ldots, F_n$ be matchings in $K_{X, Y}$. The ==**canonical negative dependency graph**== for the events $A_{F_1}, \ldots, A_{F_n}$ has one vertex for each event, and an edge between the events $A_{F_i}$ and $A_{F_j}$ ($i \neq j$) if $F_i$ and $F_j$ are not vertex disjoint.

>[!theorem] RIM admits LLL
>Let $F_0$ be a matching in $K_{X, Y}$ such that $F_0$ is vertex disjoint from $F_1 \cup \cdots \cup F_k$. Then
>$$
>\PP[A_{F_0} \mid \land_{i\in [k]} \overline{A_{F_i}}] \leq \PP[A_{F_0}]
>$$
>hence the [[Lovasz Local Lemma|Lopsided Local Lemma]] applies.