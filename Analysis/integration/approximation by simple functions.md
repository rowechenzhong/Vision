> [!theorem] Approximation by Simple Functions
> $f:\Omega \to \RR$ is measurable iff there exists a sequence of [[simple functions]] $f_n$ such that $f_n \to f$ pointwise. If $f\geq 0$, one can choose these $f_n$ such that $f_n\uparrow f$; otherwise one can still ensure $\abs{f_n}\uparrow \abs{f}$.
> 
> In the case that $f$ is an $L^p$ space, we find that the simple functions are dense in $L^p$ under $\norm{\bullet}_p$.
> ^sf-approx

> [!proof]- Forward
> Suppose $f$ is measurable. Then $f^{-1}((a,\infty))$ is measurable for all $a\in \RR$. We use the density of rationals in reals to construct a sequence of simple functions that converge to $f$ pointwise. Let
> $$
> A_{n,k} = f^{-1}\left(\left( \frac{k}{2^n}, \frac{k+1}{2^n} \right]\right).
> $$
> Then $A_{n,k}$ are disjoint and measurable. Define the simple functions
> $$
> f_n = \sum_{\abs{k} \leq n\cdot 2^n} \frac{k}{2^n} \id_{A_{n,k}}.
> $$
> (The ugly summation range ensures that each $f_n$ is a finite sum, but in the limit we can access all of $\RR$).
>
> Fix $x\in \Omega$. By construction, for all $n > f(x)$, $0 < f(x) - f_n(x) < 2^{-n}$. Thus $f_n(x) \to f(x)$ pointwise. If you want $f_n\uparrow f$, truncate the beginning; if you're in the general case, do casework on signage of $f$.

> [!proof]- Backwards
> On the other hand, suppose $f_n \to f$ pointwise.
> 1. Then, for any $x \in f^{-1}((a,\infty))$, there exists an $M$ such that $x\in f^{-1}_n((a,\infty))$ for all $n > M$.
> 2. Then $f^{-1}_n((a,\infty)) \to f^{-1}((a,\infty))$ as sets.
> 3. In particular, 
> $$ B_m = \bigcup_{n\geq M} f_n^{-1}((a,\infty)) $$
> are a sequence of measurable set, thus
> $$ f^{-1}((a,\infty)) = \bigcap_{m\geq 0} B_m $$
> is measurable.

This proof is sort of the same as this problem:

>[!problem] Monotone Class Theorem
>Let $(\Omega, \FFF)$ be a measurable space and let $\AAA$ be a $\pi$-system generating $\FFF$. Let $V$ be a vector space of **bounded** functions $f:E\to \RR$ such that:
>- $1\in V$ and $1_A\in V$ for all $A\in \AAA$.
>- For any sequence of **nonnegative** $f_n\in V$, if $f_n\uparrow f$ is also bounded, then $f\in V$.
>
>Then, $V$ contains every bounded measurable function.

>[!solution]-
>The collection $\{A\in \FFF, A_1\in V\}$ is a $\lambda$-system containing $\AAA$, and we thus have all indicators. Then the approximation lemma above kills.

>[!idea]
>For all results on this page, you can use $\pi-\lambda$ to get a stronger version.
>
>Suppose $\AAA$ is a $\pi$-system on a $\sigma$-finite $E$ generating $\mathcal{E}$, with $\mu(A) < \infty$ for all $A\in \AAA$. Let
> $$
> 	V_0 = \left\{\sum_{k\leq n} a_k \id_{A_k}:a_k\in \RR, A_k\in \AAA, n\in \NN\right\}
> $$
> i.e. all simple functions over $\AAA$.
> 
> Then you can use $V_0$ instead of all simple functions, because it generates all simple functions anyways.

%% # Lp stronger variant

There is a slightly stronger variant for $L^p$ spaces:

> [!theorem]
> Let $\AAA$ be a $\pi$-system on a $\sigma$-finite $E$ generating $\mathcal{E}$, with $\mu(A) < \infty$ for all $A\in \AAA$. Let
> $$
> 	V_0 = \left\{\sum_{k\leq n} a_k \id_{A_k}:a_k\in \RR, A_k\in \AAA, n\in \NN\right\}
> $$
> i.e. all simple functions over $\AAA$.
> 
> Then, for all $1\leq p <\infty$, $V^0$ is a dense subset of $L^p$.

[!proof] Boring
All $\id_A\in L^p$, thus $V_0\subset L^p$. Let $V$ contain all $f$ which are approximated by $V_0$; by Minkowski, $V$ is a vector space.

We quickly find that $\id_A\in V$ for all $A$, but this implies $\id_E\in V$ for all measurable $E$. Thus $V$ contains all simple functions. For $f\in L^p$, approximate by simple functions, then %%