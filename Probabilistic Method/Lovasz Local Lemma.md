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

>[!example]
>Suppose you have a set of $n$ variables, and you want to avoid a set of $m$ bad events (e.g., a conflict in an assignment). If each bad event depends on at most $d$ other events and the probability of each bad event is small enough, the Lovász Local Lemma guarantees that it is possible to assign values to the variables such that none of the bad events occur.
>- For instance, in a graph coloring problem where you wish to color a graph with few colors while avoiding certain configurations, the Lovász Local Lemma can show that a valid coloring exists under certain conditions.