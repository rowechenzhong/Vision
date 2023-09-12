> [!definition] Measurable Function
> Let $(X, \AAA)$ and $(Y, \BBB)$ be measurable spaces. A function $f: X \to Y$ is ==**measurable**== if for every $B \in \BBB$, we have $f^{-1}(B) \in \AAA$.

> [!example]
> In particular, assuming we pick the Borel measure on two topological spaces $X$ and $Y$, continuous functions are measurable.

If one is interested in [[real-valued measurable functions]], there is more intuition to be found.

> [!claim] Only need to check the generators.
> A function $(X,\AAA)\to (Y,\sigma(\BBB_0))$ is measurable iff for all $B\in \BBB_0$, $f^{-1}(B)\in \AAA$.

> [!idea]
> In topology, we only need to check the pre-images of a sub-basis to determine continuity. This is analogous.

> [!idea]
> Pre-images respect set operations. Given some function $f:A\to B$, where $A$ has a sigma-algebra, the collection of $F\subset B$ such that $f^{-1}(F)$ is measurable forms a sigma-algebra.

> [!proof]-
> In particular, the collection of $B\subset Y$ such that $f^{-1}(B)$ is measurable forms a $\sigma$-algebra; this fills all of $\sigma(\BBB_0)$.

For example, one needs only verify that the pre-image of $(a, \infty)$ is measurable when working with $(X,\AAA)\to \RR$.

> [!definition] Pushforward Measure
> Let $(X, \AAA, \mu)$ and $(Y, \BBB)$ be measure spaces, and let $f: X \to Y$ be a measurable function. Then, the ==**pushforward measure**== $f_\sharp\mu$ on $B\in \BBB$ is defined by $f_\sharp\mu(B) = \mu(f^{-1}(B))$.
