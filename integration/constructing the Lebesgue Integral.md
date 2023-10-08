We follow the [[measure theory function scaffold|usual scaffold]]. Technical detail: some later parts of this construction will only work in the case of [[sigma finite measures|$\sigma$-finite measures]].

We first define the integral of [[indicator functions]]:

> [!definition] Integral of Indicator Functions
> The integral of an indicator function $\id_{A}$ is defined as $$ \int_\Omega f\der \mu = \mu(A). $$

There is exactly one way to extend this to [[simple functions]]:

> [!definition] Integral of Simple Functions
> Let $f = \sum_{i=1}^n c_i \id_{A_i}$ be a simple function. Then we define $$ \int_\Omega f\  d\mu  = \sum_{i=1}^n c_i \mu(A_i). $$

> [!proof]- This is self-consistent
> There may be more than one way of partitioning a simple function into indicators; we would like to show all possible integrals are the same. Let $f = \sum_{i=1}^n c_i \id_{A_i} = \sum_{j=1}^m d_j \id_{B_j}$ be two such partitions. Then, we can write
> $$\sum_{i=1}^n c_i \mu(A_i) = \sum_{i=1}^n \sum_{j=1}^m c_i \mu(A_i\cap B_j)$$
> However, if $A_i\cap B_j \neq \emptyset$, then $c_i = d_j$, because both are equal to the value of $f$ on $A_i\cap B_j$. Thus, this is equal to
> $$\sum_{j=1}^m d_j \sum_{i=1}^n \mu(A_i\cap B_j) = \sum_{j=1}^m d_j \mu(B_j)$$
> as desired. In particular, this definition is compatible with indicator functions.

As an additional step, we'll define the integral for ==doubly bounded measurable functions==, which are measurable $f: (\Omega, \FF, \mu) \to \RR$ such that $\sup_{\omega \in \Omega} \abs{f(\omega)} < \infty$ *and* $\mu(\{f\neq 0\}) < \infty$. We're taking this step to keep everything finite before we start adding infinities along the domain and range.

> [!definition] Integral of Doubly Bounded Measurable Functions
> Let $f$ be a doubly bounded measurable function. Then we define $$ \int_\Omega f\  d\mu = \sup \left\{ \int_\Omega g\  d\mu \mid g \text{ is simple}, g \leq f \right\} = S. $$

This is clearly consistent with the previous definition. 

> [!claim] Discretize the range to compute the supremum.
> This illustrates the main trick. $$S = \int_\Omega f\der \mu = \inf \left\{ \int_\Omega g\der \mu \mid g \text{ is simple}, g \geq f \right\} = I.$$

> [!proof]-
> Clearly $S\geq I$. Discretize; let
> $$g_m = \left(\frac{\ceil{mf} - 1}{m}\right)\cdot \id_{\{f\neq 0\}} \leq f \leq \frac{\ceil{mf}}{m} = h_m$$
> Observe that $f$ is doubly-bounded and measurable, thus $g_m$ and $h_m$ are simple functions. Then clearly $\int_\Omega g_m \der \mu \leq I \leq S \leq \int_\Omega h_m \der \mu$, so $S - I \leq \int_\Omega h_m - \int_\Omega g_m = \frac{1}{m}\mu(\{f\neq 0\})$. Since this is true for all $m$, $S - I = 0$.

We extend this to all nonnegative measurable functions:

> [!definition] Integral of Nonnegative Measurable Functions
> Let $f\in L^+(\Omega)$. Then we define $$ \int_\Omega f\  d\mu = \sup \left\{ \int_\Omega g\  d\mu \mid g \text{ is doubly bounded }, 0\leq g \leq f \right\} = S. $$

This is clearly consistent with the definitely for doubly-bounded functions. We've introduce infinities in the domain and range, and that's *all we did*:

> [!claim] No surprises
> Pick any $\Omega_m\uparrow \Omega$ [[sigma finite measures|with finite measure]]. Let $f_n(\omega) = \min(f(\omega),n) \id_{\Omega_n}$. Then
> $$\int_\Omega f\der \mu = \sup_{n\to \infty} \int_\Omega f_n\der \mu.$$
> 

> [!proof]- Bash
> LHS $\geq$ RHS trivially. If the RHS is $\infty$ we conclude. Else, for any db $0\leq g \leq f$ and any $\eps > 0$, I've got to show that there exists an $n$ such that $$\int_\Omega g \der \mu \leq \int_\Omega f_n \der \mu + \eps.$$
> By db, $\sup g \leq m$ for some integer $m$ and $S = \{\omega : g(\omega) \neq 0\}$ has finite measure. For all $n > m$,
> $$\int_{\Omega} g\der  \mu \leq \int_{\Omega_n\cap S} f_n \der \mu + \int_{S \setminus \Omega_n} g\der  \mu \leq \int_{\Omega_n} f_n \der \mu + \mu\left(S\setminus \Omega_n\right)\cdot m$$
> $\mu\left(S\setminus \Omega_n\right)$ goes to $0$, thus we conclude.

> [!idea] What are we waiting for?
> Why didn't we just consider all $\Omega\to \RR$ from the start? Well, we're pretty good at adding and multiplying $+\infty$'s to $+\infty$'s, but the moment we take $\infty - \infty$, things die.

> [!definition] Integral of Integrable Functions
> Let $f:(\Omega, \FFF) \to (\RR, \BBB)$ be measurable. Then, let the positive and negative parts of $f$ be $$ f^+(x) = \max\{f(x), 0\}, \quad f^-(x) = \max\{-f(x), 0\}. $$
> Everything is measurable, so we can finally define $$ \int_\Omega f = \int_\Omega f^+ - \int_\Omega f^-. $$
> As long as $\int_\Omega f^+$ and $\int_\Omega f^-$ are not both $\infty$, we say $f$ is ==__integrable__==.

> [!idea]
> This may be more restrictive than you were expecting! The domain is of high importance here; the function $f(x) = 1$ over $\RR$ is _not_ integrable, but $f(x) = 1$ over $[0,1]$ is.