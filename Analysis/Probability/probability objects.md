This page will port over the essential ideas from [[Measure Theory]] theory in the context of [[Probability]]:

-   A ==**probability space**== is a [[measure space]] $(\Omega, \FFF, \PP)$ where $\PP(\Omega) = 1$.
-   An ==**event**== is an element of $\FFF$.
-   The ==**probability**== of an event $A\in \FFF$ is $\PP(A)$.
# Random Variables

An $(S,\GGG)$-valued ==**random variable**== is a [[measurable functions|measurable function]] on a probability space $(\Omega, \FFF, \PP)$. By default, we assume that $S = \RR$ and $\GGG = \BBB(\RR)$.

By abuse of notation, we let the _pre-image_ of a set of real numbers $A$ be denoted $\{X\in A\}$. So what we really mean when we write $\{X\geq 5\}$ is the _set of events for which_ $X(A) \geq 5$. 

>[!definition] Law
>Recall that $X$, like all measurable functions, induces a [[measurable functions#^127729|pushforward measure]] $X_* \PP$ over $\RR$. This measure, called the ==**law**==, is denoted $\LL_X$ or $\mu_X$, and acts on measurable subsets $B\subset \BBB(\RR)$ as
> $$
 	\LL_X(B) = \PP(X^{-1}(B)) = \PP(X\in B)
> $$
> So we're really just using the partition picture of functions here. No surprises.

^c1cbb1

>[!definition] CDF
>This law is uniquely determines and is uniquely determined by the ==**cumulative distribution function**== $F(x) = \PP(X\leq x)$. It is increasing and right-continuous, any any such function induces a random variable, a la [[Stieltjes Measure]].

^a89c00

>[!defn] PDF
> Some random variables admit ==**probability density functions**== $f(x)$ which are nonnegative measurable functions from $(\RR, \BBB_\RR)$ such that for all Borel sets $B$, $\mu_X(B) = \int_\RR \id(B) f(x) \mu(d x)$ under the standard Lebesgue measure $\mu$.

To emphasize, not all RVs admit PDFs; the random variable $X = 0$ does not. (Advanced:) such a PDF is an example of a [[Probability Density]].