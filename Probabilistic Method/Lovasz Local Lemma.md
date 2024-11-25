Suppose $\mathcal{A}_1, \dots, \mathcal{A}_n$ are some "bad" events. Under what condition can we show that $\PP(\mathcal{A}_1\cup\dots \cup \mathcal{A}_n) < 1$?

- The ==**Union bound**== is stupid.
- Suppose all $\mathcal{A}_1,\dots, \mathcal{A}_n$ are independent! This is still trivial.
- What if they are *mostly* independent?

>[!definition] Lovász Local Lemma (Symmetric Case)
>Let $\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_n$ be events in a probability space. Suppose that each event $\mathcal{A}_i$ is mutually independent of all the other events $\mathcal{A}_j$ except for at most $d$ of them, and that $\PP(\mathcal{A}_i) \leq p$ for all $i$.
> - If $ep(d+1) \leq 1$, where $e$ is the base of the natural logarithm, then
> $$
> \PP\left(\bigcap_{i=1}^{n} \overline{\mathcal{A}_i}\right) > 0,
> $$
> meaning that with positive probability, none of the events $\mathcal{A}_i$ occur.

This is a special case of the below theorem:

>[!theorem] Lovász Local Lemma (General, Lopsided Case)
>Let $\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_n$ be events in a probability space. For each $i$, let $N(i) \subseteq [n]$ be such that
> $$
> \PP\left[\mathcal{A}_i \mid \land_{j\in S} \overline{\mathcal{A}_j}\right] \leq \PP[\mathcal{A}_i] \quad \forall i \in [n], S \subseteq [n] \setminus (N(i) \cup \{i\}). \tag{$\star$}
> $$
> Let $0 < x_1,\dots, x_n < 1$ be real numbers such that:
> - $\PP[\mathcal{A}_i] \leq x_i \prod_{j\in N(i)} (1 - x_j)$ for all $i$
> Then,
> $$
> \PP\left(\bigcap_{i=1}^{n} \overline{\mathcal{A}_i}\right) \geq \prod_{i=1}^n (1 - x_i).
> $$
> meaning that with positive probability, none of the events $\mathcal{A}_i$ occur.

>[!idea] Usage
> The above theorem is "Lopsided," because instead of requiring full independence between $\mathcal{A}_i$ and everything outside $N(i)$, $(\star)$ requires that avoiding any bad events outside $N(i)\cup \{i\}$ *brings down* the probability of $\mathcal{A}_i$. Intuitively, this should make use "better off" than the symmetric case.

Usually, we don't need to use this lopsidedness property; we have full independence. See [[Random Injection Model]] for the canonical example which generates a lopsided dependency setup.

The absolutely canonical example of this is proving the existence of a graph of unbounded size satisfying a suitably
"local" property, such that the LLL dependency graph is also locally bounded and amenable to bounding. We present two advanced examples below.

Advanced topic: [[Algorithmic Local Lemma and Entropy Compression]]

# Advanced Example I

>[!example] Vertex-disjoint cycles in k-regular directed graphs
>Prove that every $k$-regular directed graph has at least $ck$ vertex-disjoint directed cycles, where $c > 0$ is some constant.

>[!idea]
>Experimenting with this problem, you will notice that the key difficulty is that in order to get a vanishing bound on a Gaussian-looking object, you need to get past the "core" of the Gaussian; you need something like $\PP(X < \mu - \omega(\sigma))$. The wiggle room we leverage in order to push the bound past this threshold is the fact that we are given an *exactly* $k$-regular graph; we can allow ourselves to be only approximately $k$-regular, and this brings our bound strictly below the core of the Gaussian.

Let $0 < \eps < 1$ be an absolute constant which we will fix later. Let $\delta_k = \eps^2 k^{-\eps}$.

>[!definition]
>A ==**nearly $k$-regular directed graph**== is a graph such that the indegree and outdegree of every vertex is in $[k(1 - \delta_k), k(1 + \delta_k)]$.

>[!claim]
>There is some $c$ such that in every nearly $k$-regular directed graph, there are at least $ck$ vertex-disjoint directed cycles.

To prove this, we'll establish the following key subclaim:

>[!claim] Main Subclaim
>For sufficiently large $k$, given a nearly $k$-regular directed graph $G$, there exists a partition of the vertices of $G$ into two subgraphs $H_1$ and $H_2$ such that each of $H_1$ and $H_2$ are nearly $\frac{k}{2}$-regular.

This implies our main claim because:
1. Any nearly $k$-regular graph for $k \geq 1$ contains at least one cycle (since each vertex has indegree and outdegree ≥ 1)
2. We can apply induction to $H_1$ and $H_2$ to obtain at least $c\frac{k}{2} + c\frac{k}{2} = ck$ vertex-disjoint directed cycles

The construction is to color each vertex red or blue uniformly at random and apply LLL to show this works with positive probability.

>[!proof]- Details of the dependency graph
>**Bad Events:**
>For each vertex $v$, let $A_v$ be the event that (assuming $v$ is colored red):
> - $v$ has < $\frac{k}{2}(1 - \delta_{k/2})$ red in-neighbors
> - $v$ has < $\frac{k}{2}(1 - \delta_{k/2})$ red out-neighbors
> - $v$ has > $\frac{k}{2}(1 + \delta_{k/2})$ red in-neighbors
> - $v$ has > $\frac{k}{2}(1 + \delta_{k/2})$ red out-neighbors
>
>**Dependency Structure:**
>Two events are connected if their vertices share any in-neighbors or out-neighbors. Each event has at most $100k^2$ dependent events.

Then, using Chernoff bounds on the sum of outdegree i.i.d. Bernoulli random variables $X$:
$$
\PP(X < \frac{k}{2}(1 - \delta_{k/2})) \leq \exp(-Ck^{1-\eps})
$$
where $C = \frac{1}{8} \eps^4 (2^\eps - 1)^2$ is positive.

>[!proof]- Chernoff Bound Calculation
>Specifically, let us upper-bound the probability that the sum of (the outdegree of $v$) i.i.d. Bernoulli random variables, $X$, is less than $\frac{k}{2}\left(1 - \delta_{k/2}\right)$.
>
> Well, this is clearly maximized when the outdegree of $v$ is minimal, at $k(1 - \delta_k)$. In that case $\mu = \frac{k}{2}\left(1 - \delta_k\right)$ and $n = k(1-\delta_k)$, such that Chernoff on $\lambda = \frac{1}{\sqrt{k(1-\delta_k)}}\left( \frac{k}{2}\left(\delta_{k/2} - \delta_k\right)\right)$ says that
> $$
> \PP\left(X < \frac{k}{2}\left(1 - \delta_{k/2}\right)\right) = \PP\left(X < \mu - \lambda \sqrt{n}\right) \leq \exp\left( - \lambda^2 / 2\right) = \exp\left( - \frac{1}{2k(1-\delta_k)}\left( \frac{k}{2}\left(\delta_{k/2} - \delta_k\right)\right)^2\right).
> $$
> It's time to plug in $\delta_k = \eps^2 k^{-\eps}$ and $\delta_{k/2} = \eps^2 (k/2)^{-\eps}$.
> We get an exponent of
> $$
> -\frac{1}{2k(1-\eps^2 k^{-\eps})}\left( \frac{k}{2}\left(\eps^2 (k/2)^{-\eps} - \eps^2 k^{-\eps}\right)\right)^2 = -\frac{k^{1-\eps}}{8} \frac{\eps^4 \left(2^\eps - 1\right)^2}{1 - \eps^2 k^{-\eps}} \leq -Ck^{1-\eps}
> $$

Setting $\eps = 0.1$ gives $C \approx 6.4 \cdot 10^{-8}$. The symmetric LLL applies if:
$$
e \cdot (100k^2 + 1) \cdot \exp(-Ck^{1-\eps}) < 1
$$
This inequality holds for sufficiently large $k$, completing the proof.

# Advanced Example II

The following example "stretches" the locality over a dependency graph with unbounded degree by observing that the probability in the LLL is a finite geometric series.

>[!example] Proper edge-coloring with three colors and large girth
> Prove that for every $\Delta$, there exists $g$ so that every bipartite graph with maximum degree $\Delta$ and girth at least $g$ can be properly edge-colored using $\Delta + 1$ colors so that every cycle contains at least three colors.

>[!claim]
> First off, there is a well-known non-probabilistic argument that for any bipartite graph with maximum degree $\Delta$, there is a proper edge coloring using $\Delta$ colors.

>[!proof]- Proof of Claim
> We first show the case where the bipartite graph is actually $\Delta$-regular. Then Hall's marriage lemma obviously applies, hence we can obtain a perfect matching. Removing these edges yields a $\Delta-1$-regular graph, and we can repeat this process until we have a $\Delta$-color proper edge coloring.
>
> We then just need to show that any graph with maximum degree $\Delta$ can be embedded into a $\Delta$-regular graph. This proceeds by induction on the number of edges. Suppose $H$ can be embedded in $\Delta$-regular graph $G$, and we'll show that this is true for any $H\cup \{e\}$ where $e$ is an edge. Let the vertices with non-zero degree in $H$ be $V$, and let $e$ connect $a$ and $b$.
> - If $a\notin V$ and $b\notin V$, then simply create a disjoint $K_{\Delta, \Delta}$ containing $e$, and yield $K_{\Delta, \Delta}\sqcup G$.
> - Else, if $a\in V$ and $b\notin V$, then select $c\in V$ such that $(a,c)\in G$, and let $G' = \{(a,b)\} \cup G\setminus \{(a,c)\}$. In $G'$, $b$ has degree $1$, while $c$ has degree $\Delta - 1$. Hence if we add a new vertex $d$ and connect $(c,d)$, we are left with $b$ and $d$ which each have degree $1$. We then add $2\Delta - 2$ new vertices, $\Delta-1$ on each side, and can spawn a $K_{\Delta, \Delta}\setminus \{(b,d)\}$. This, combined with $G'$ and edge $(c,d)$ yield the desired $\Delta$-regular graph.
> - If $a\in V$ and $b\in V$, then we can follow a very similar construction. Delete an arbitary $(a,c)$ and $(b,d)$ that were inside $G$, then introduce new vertices $e,f$ connected by $(c,e)$ and $(d,f)$. Finally, spawn $2\Delta - 2$ new vertices and create a $K_{\Delta, \Delta}\setminus \{(e,f)\}$ to complete the construction.

Great! Fix some proper $\Delta$-coloring of our bipartite graph $G$. We create a new graph with $\Delta+1$ colors by iid selecting each edge to be the original color with probability $1-\alpha$ and a new color $*$ with probability $\alpha$ (fixing $\alpha$ later). We now just need to show that there is a positive probability that none of two classes of bad events occur:
- Type $A_{i,j}$: that two adjacent edges $i$ and $j$ are colored $*$.
- Type $B_C$: that a cycle $C$ of length $\ell$ which originally had two colors has either no $*$'s at all, or $\geq \frac{\ell}{2}$ $*$'s. To emphasize, not every cycle is associated with an event of type $B_C$; only those which originally had two colors.

If neither of these happen, then the graph is clearly properly edge-colored because the original graph was properly edge-colored and no two of the new $*$'s are adjacent. In addition, every cycle has at least $3$ colors, because they each contain $*$, and additionally because they contain $> \frac{g}{2}$ of the original colors, they must contain at least two contiguous elements which were of the original coloring, and those two edges cannot be the same color.

Events of type $A$ are going to be way more common. They have probability $\alpha^2$ of occurring, so let's allow $x_{A_{i,j}} = 10^{10}\alpha^2$. An event of type $B$ can be upper-bounded crudely by a Chernoff bound:
$$
    \PP(B_C)\leq (1-\alpha)^{\ell} + \exp\left( - \frac{\eps^2}{1 + \eps}\mu\right) = (1-\alpha)^{\ell} + \exp\left( - \frac12\left(1 - 2\alpha\right)^2 \ell\right)
$$
where $\eps = \frac{1}{2\alpha} - 1$ and $\mu = \alpha \ell$. The second probability is basically tiny compared to the first for sufficiently small $\alpha$, because it looks like $(e^{-1/2} + O(\alpha))^\ell$.  

I'm going to set $\alpha = 10^{-100}\Delta^{-1}$ and observe that $\PP(B_C)\leq 2(1 - \alpha)^\ell$. I'm going to set $x_{B_C} = 2\cdot 10^{10} (1 - \alpha)^{0.99\ell}$. One can set $g$ sufficiently large such that $x_{B_C} < 1$ for all $\ell$.

Fine. Now, any particular event of type $A_{i, j}$ has at most $4\Delta$ events of type $A$ which share an edge with it. The super important observation is that although there are up to $2\Delta^{\ell - 2}$ cycles of length $\ell$ which share an edge with $(i, j)$, there are only at most $2\Delta$ events of type $B$ which share an edge with $(i, j)$, because if you fix the two desired colors and your starting edge, there is at most exactly one cycle (of *any* length!!) which contains solely those two colors; your path is completely fixed! Hence our probability is lower-bounded by
$$
    \alpha^2 \leq 10^{10}\alpha^2 \left(1 - 10^{10}\alpha^2\right)^{4\Delta} \left(1 - 2\cdot 10^{10} (1 - \alpha)^{0.99 g}\right)^{2\Delta}.
$$
So it suffices to show that
$$
    1\leq 10^{10} \left(1 - 4\Delta 10^{10}\alpha^2\right)\left(1 - 4\cdot \Delta \cdot 10^{10} (1 - \alpha)^{0.99 g}\right).
$$
or
$$
    1\leq 10^{10} \left(1 - 4\cdot 10^{-190}\Delta^{-1}\right)\left(1 - 4\cdot \Delta \cdot 10^{10} (1 - \alpha)^{0.99 g}\right).
$$
Well, $1 - \alpha < 1$, so we can pick some $g$ such that this is true.

Completely analogously, we now consider events of type $B_C$. Let $\ell = \abs{C}$. We have at most $2\Delta \ell$ events of type $A$ which share an edge with $B_C$, and at most $2\Delta \ell$ events *total* of type $B$ which share an edge with $B_C$. Hence we just need to show
$$
    2(1 - \alpha)^\ell \leq 2\cdot 10^{10} (1 - \alpha)^{0.99\ell} \left(1 - 10^{10}\alpha^2\right)^{2\Delta \ell} \left(1 - 2\cdot 10^{10} (1 - \alpha)^g\right)^{2\Delta \ell}.
$$
It suffices to show that
$$
    (1 - 10^{-100}\Delta^{-1})^{0.01} \leq \left(1 - 2\cdot  10^{-190}\Delta^{-1}\right) \left(1 - 2\cdot 10^{10} (1 - \alpha)^g\cdot 2\Delta\right).
$$
Note that $1 - \alpha < 1$, so we can pick some $g$ such that the second term is arbitarily close to $1$. Hence it suffices to show
$$
    (1 - 10^{-100}\Delta^{-1}) < \left(1 - 2\cdot  10^{-190}\Delta^{-1}\right)^{100}
$$
but it is clear that
$$
    (1 - 10^{-100}\Delta^{-1}) < \left(1 - 2\cdot 100\cdot  10^{-190}\Delta^{-1}\right)
$$
so we're done.
