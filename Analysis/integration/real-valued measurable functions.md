We're trying to upgrade to [[Integration]], so from now on most of our [[measurable functions]] will point into the reals, extended reals, or the [[complex-valued measurable functions|complex numbers]]. On the other hand, the domain is pretty unimportant; $\Omega$ is some arbitrary [[measure space]]. 

>[!idea]
>From now on, a "measurable function" without qualifiers has a tendency to point into $\RR$, and a "non-negative measurable function" will always point into $[0,\infty]$.

The set of all measurable functions from $\Omega$ to $\RR_{\geq 0}$ is sometimes denoted $L^+(\Omega)$. Obligatory results:

> [!theorem] Making Measurable Functions
> 1. Given $f,g: \Omega \to \RR, [0,\infty], \CC$ are measurable functions and $c \in \KK$, then $cf, f + g, fg$ are all measurable.
> 2. Let $f_n: \Omega \to \RR, [0,\infty]$ be a sequence of measurable functions. Then, the pointwise supremum and infimum are measurable. (If $\RR$, you need to check that the sup and inf are still real-valued).
> 	1. Consequently,
>    $$
>    \lim \sup_{n\to \infty} f_n(x) = \inf_{n\geq 1} \sup_{k\geq n} f_k(x)
>    $$
>    and $\lim \inf$ are also measurable.
> 	2. Most importantly, if these coincide, that is, if the functions converge pointwise, then the limit is measurable. This works for $\RR, [0,\infty], \CC$. 
> 3. Suppose $\Omega$ is a [[complete measure space]]. If $f,g: \Omega\to [-\infty, \infty]$ agree almost everywhere, then they are both measurable or both not measurable.

> [!solution]- Part 1
> 1. First, we show $(cf)^{-1}((a,\infty))$ is measurable for all $a\in \RR$. Since $f$ is measurable, $f^{-1}((a/c,\infty))$ is measurable. Therefore, $(cf)^{-1}((a,\infty)) = f^{-1}((a/c,\infty))$ is measurable.
> 2. Next, let's show that $(f+g)^{-1}((a,\infty))$ is measurable for all $a\in \RR$. Since $f,g$ are measurable, $f^{-1}((q,\infty))$ and $g^{-1}((a - q,\infty))$ are both measurable for all $q\in \QQ$. Now, observe that
> $$(f+g)^{-1}((a,\infty)) = \bigcup_{q\in \QQ} \left( f^{-1}((q,\infty)) \cap g^{-1}((a - q,\infty)) \right)$$
> because if $f(\omega) + g(\omega) > a$, there exists a rational $q$ such that $f(\omega) > q$ and $g(\omega) > a - q$. Since unions of measurable sets are measurable, we conclude that $(f+g)^{-1}((a,\infty))$ is measurable.
> 3. Finally, let's show $(fg)^{-1}((a,\infty))$ is measurable for all $a\in \RR$. Assume first that $a > 0$. Note that
> $$ (fg)^{-1}((a,\infty)) = \bigcup_{q > 0, q \in \QQ} \left( f^{-1}((q,\infty)) \cap g^{-1}((a/q,\infty)) \right) \cup \left( f^{-1}((-\infty, -q)) \cap g^{-1}((-\infty, -a/q)) \right) $$
> This also yields $a = 0$ by countable unions. If $a < 0$, then
> $$ (fg)^{-1}((a,\infty)) = \bigcup_{q > 0, q \in \QQ} \left( f^{-1}((-q, \infty)) \cap g^{-1}((a/q,\infty)) \right) \cup \left( f^{-1}((q,\infty)) \cap g^{-1}((-a/q, \infty)) \right) $$

> [!solution]- Part 2
> We first consider the pointwise supremum. Let $f_n: \Omega \to \RR$ be a sequence of measurable functions. Then, as sets,
> $$ \left\{ x \in \Omega \mid \sup_{n\geq 1} f_n(x) > a \right\} = \bigcup_{n\geq 1} \left\{ x \in \Omega \mid f_n(x) > a \right\} $$
> Since each $f_n$ is measurable, each set in the union is measurable, and thus the union is measurable. Therefore, the supremum is measurable. The infimum is similar (use $(-\infty, a)$ in the definition of measurability).

> [!solution]- Part 3
> Suppose $f$ is measurable. Then $\mu\left(f^{-1}((a,\infty)) \Delta g^{-1}((a,\infty))\right) = 0$ for all $a\in \RR$ (because the set in question is a subset of the set $\{x: f(x)\neq g(x)\}$, which has outer measure zero, and thus has measure $0$). Since $f$ is measurable, $g$ is measurable as well. (All sets with outer measure $0$ are measurable). The converse is similar.

The characterization that is most amenable to verifying implementation details is the [[approximation by simple functions]].