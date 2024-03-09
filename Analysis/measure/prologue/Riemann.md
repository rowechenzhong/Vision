> [!definition] Tagged Partition
> A ==**tagged partition**== $\mathcal{P} = ((x_0, x_1,\dots x_n), (x_1^*, \dots, x^*_n))$ of the interval $[a,b]$ is a finite sequence of points $a = x_0 < x_1 < \dots < x_n = b$ together with a choice of points $x_i^* \in [x_{i-1}, x_i]$ for each $i = 1, \dots, n$. We abbreviate $x_i - x_{i-1}$ as $\delta x_i$. The quantity $\Delta(\mathcal{P}) = \sup_{1\leq i\leq n} \delta x_i$ will be called the ==**norm**== of $\mathcal{P}$.

> [!definition] Riemann Sum
> Let $f: [a,b] \to \mathbb{R}$ be a bounded function and let $\mathcal{P} = ((x_0, x_1,\dots x_n), (x_1^*, \dots, x^*_n))$ be a tagged partition of $[a,b]$. The ==**Riemann sum**== of $f$ with respect to $\mathcal{P}$ is
>
> $$
>   \mathcal{R}(f, \mathcal{P}) = \sum_{i=1}^n f(x_i^*) \delta x_i
> $$
>
> If $\exists R\forall \eps > 0 \exists \delta > 0$ such that $\abs{\mathcal{R}(f, \mathcal{P}) - R} < \eps$ whenever $\Delta(\mathcal{P}) < \delta$, then we say that $f$ is ==**Riemann integrable**== on $[a,b]$ and we write
>
> $$
>   \int_a^b f(x) dx = R
> $$
>
> The number $R$ is called the ==**definite integral**== of $f$ over $[a,b]$.

There is an alternative definition for this integral that is more useful for proving properties of the integral.

> [!definition] Piecewise Constant Functions
> A function $f: [a,b] \to \mathbb{R}$ is a ==**piecewise constant function**== if there exists a partition of $[a,b]$ into finitely many intervals $I_1,\dots I_n$ such that $f$ is a constant $c_i$ on each $I_i$. Then, the ==**piecewise constant integral**== of $f$ over $[a,b]$ is defined as
>
> $$
>   \int_a^b f(x) dx = \sum_{i=1}^n c_i \abs{I_i}
> $$
>
> This can be easily shown to be independent of the choice of partition, and equal to the Riemann integral, thus there is no ambiguity in the notation.

> [!definition] Upper and Lower Darboux integrals
> Let $f: [a,b] \to \mathbb{R}$ be a bounded function. The ==**upper Darboux integral**== of $f$ over $[a,b]$ is defined as
>
> $$
>   \overline{\int_a^b} f(x) dx = \inf \left\{ \int_a^b g(x) dx \mid g \text{p.c. s.t.} f(x) \leq g(x) \right\}
> $$
>
> The ==**lower Darboux integral**== of $f$ over $[a,b]$ is defined as
>
> $$
>   \underline{\int_a^b} f(x) dx = \sup \left\{ \int_a^b g(x) dx \mid g \text{p.c. s.t.} f(x) \geq g(x) \right\}
> $$
>
> If $\overline{\int_a^b} f(x) dx = \underline{\int_a^b} f(x) dx$, then we say that $f$ is ==**Darboux integrable**== on $[a,b]$ and we refer to this quantity as the ==**Darboux integral**== of $f$ over $[a,b]$.

> [!theorem] Riemann Integrability
> Let $f: [a,b] \to \mathbb{R}$ be a bounded function. Then, $f$ is Riemann integrable if and only if it is Darboux integrable, and in this case, the Riemann integral is equal to the Darboux integral.

> [!proof] Riemann Integrability implies Darboux Integrability, and Riemann Integral equals Darboux Integral
> Fix an arbitrary $\eps > 0$. Find a $\delta$ for which the definition of RI holds, and then pick any partition $\mathcal{P}$ with norm at most $\delta$. Let $g$ be the p.c. function which is equal to the supremum of $f$ on each interval of $\mathcal{P}$. Then,
>
> -   $f\leq g$ everywhere.
> -   By definition,
>
> $$
> \overline{\int_a^b} f(x) dx \leq \int_a^b g(x) dx = \sum_{i=1}^n \sup_{x\in I_i} f(x) \abs{I_i} \leq \int_a^b f(x) dx + \eps
> $$
>
> A similar proof shows that $\underline{\int_a^b} f(x) dx \geq \int_a^b f(x) dx - \eps$. Since $\eps$ was arbitrary, we have that $f$ is Darboux integrable and the Riemann integral is equal to the Darboux integral.

> [!proof] Darboux Integrability implies Riemann Integrability
> For computational purposes, let $[a,b] = [0,1]$. Fix an arbitrary $\eps > 0$. By definition of Darboux Integrability, we are given a p.c. function $g$ such that
>
> -   $f \leq g$ everywhere.
> -   $\int_a^b g(x) dx \leq \underline{\int_a^b} f(x) dx + 0.001\eps$
>
> Let $\mathcal{P} = (I_1, \cdots I_n)$ be the partition on which $g$ is constant. Suppose further that the maximum value $f$ takes on anywhere is $M$, and the minimum value $g$ takes on anywhere is $N$.
>
> Now, let $\delta = \frac{0.001\eps}{n(M - N)}$. Let $\mathcal{P}'  (I'_1, \dots I'_m)$ be any tagged partition with norm at most $\delta$. Let $f'$ be the function induced by $\mathcal{R}(f, \mathcal{P}')$, i.e. $f' = f(x_i^*)$ on $I'_i$. Then:
>
> -   $f' < g$ for all $I'_i$ which lie strictly inside some $I_i$ -- that is, $f' \geq g$ on a finite number of intervals each which length at most $\frac{0.001\eps}{n(M - N)}$.
> -   $f'(x) - g(x)$ is at most $N - M$ everywhere.
> -   There are at most $2n$ of these intervals.
>
> Thus, $\mathcal{R}(f, \mathcal{P}') - \mathcal{R}(g, \mathcal{P}') \leq 0.002\eps$. To rehash, for any partition $\mathcal{P}'$ with norm at most $\delta$,
>
> $$
>   \mathcal{R}(f, \mathcal{P}') \leq \underline{\int_a^b} f(x) dx + 0.003\eps
> $$
>
> Repeat a similar exercise with the lower Darboux integral, obtaining a bound $\delta'$. Using $\min(\delta, \delta')$ as the bound in the definition of Rieman integrability, we obtain the desired result.