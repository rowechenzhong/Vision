# Normed Spaces 

Recall that a vector space is ==**finite-dimensional**== if every linearly dependent set is finite. Otherwise, it is ==**infinite-dimensional**==.

$X$ forever denotes a topological space.

Here is an example of an infinite-dimensional vector space: 

> [!definition] $C_\infty(X)$
$C_\infty(X)$ is the set of all functions $f: X \to \CC$ which are continuous and bounded. 

Functional analysis is the study of vector spaces with a topology. Infinite dimensional vector spaces are pretty hard to work in in general, because all linear algebra concepts have finite strength. Topology lets us deal with them.

> [!definition] Norm
A ==**norm**== on a vector space $V$ is a function $\norm{\bullet}: V \to \RR_{\geq 0}$ such that 
>  -  (==**Definiteness**==) $\norm{v} = 0 \iff v = 0$, 
>  -  (==**Homogeneity**==) $\norm{\lambda v} = \abs{\lambda} \norm{v}$, and 
>  -  (==**Triangle Inequality**==) $\norm{v + w} \leq \norm{v} + \norm{w}$.
> A vector space endowed with a norm is called a ==**normed vector space**==. 

This norm induces a metric on $V$ by $d(v, w) = \norm{v - w}$. 

> [!problem] Bruh
Show that this is a metric (symmetric, positive definite, triangle inequality). 

$V, W$ forever denote normed vector spaces over $\RR$ or $\CC$.

> [!idea] 
The second condition doesn't have to be satisfied by any old metric; its the source of linearity.

>[!problem]
>Show norms are continuous and commute with limits.

> [!problem] Scaling works
Show that scaling by a nonzero constant is a homeomorphism. 

So we'll end up writing "WLOG by scaling" a lot.

> [!problem] Sums of Closures
Let $A,B\subset V$ be arbitrary sets. Let $\overline{A}$ and $\overline{B}$ denote their closures, as usual. Show that $\overline{A} + \overline{B}\subseteq \overline{A + B}$. 

> [!solution] 
Recall that in metric spaces, the closure of a set is the set of all limits of convergent sequences in the set. Well, take any convergent sequence $\{a_n\}\to a$ in $A$ and any convergent sequence $\{b_n\}\to b$ in $B$. Then, $\{a_n + b_n\}$ converges to $a + b$ in $A + B$. 

# Major Examples

See the
- [[infinity norm]]
- [[Minkowski norm]], extending the [[Euclidean norm]].

Now that we have our first example, update your intuition: anything that relies on counting the elements of your basis probably fails.