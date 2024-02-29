> [!definition] Measurable Function
> Let $(X, \AAA)$ and $(Y, \BBB)$ be measurable spaces. A function $f: X \to Y$ is ==**measurable**== if for every $B \in \BBB$, we have $f^{-1}(B) \in \AAA$.

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

> [!example]
> In particular, assuming we pick the Borel measure on two topological spaces $X$ and $Y$, continuous functions are measurable.
> 
> A (real-valued) measurable function *from* a Borel space is a ==**Borel function**== (so we point from $(E, \BBB(E))\to (\RR, \BBB)$).


Suggested reading:
- [[Measurable functions generate sigma algebras]].
- [[pushforward measure|Measurable functions induce measures]].
- [[Canonical equivalence classes of Measurable functions]]