> [!theorem] Vitali
> Recall the definition of a [[measure space]]. Suppose we want a measure space on $[0,1]$ to satisfy the following additional basic properties:
>
> 1. The length of an interval $[a,b]$ is $b-a$.
> 2. It should be translation invariant: $\mu(A) = \mu(A + x)$ for any $x \in \RR$. (Here, $A + x$ is the set $\{\floor{a + x} : a \in A\}$.)
> 3. We desire to measure _all_ subsets of $[0,1]$. [[measurable space|This is the part that goes wrong]].
>
> It is impossible to construct such a measure.

> [!proof]
> Construct a set $A$ by selecting a representative from each cost of $\RR/\QQ$. By countable additivity, the measure of $[0,1]$ is $0$ if $\mu(A) = 0$, and $\infty$ otherwise.