In establishing the formalism of [[Stochastic Calculus Homepage|stochastic integrals]], one often writes boilerplate of the following form:

>[!idea] Boilerplate
>Fix any sequence $0 = t_0^n < \dots < t^n_{p_n} = t$ of subdivisions whose [[mesh]] tends to $0$. For any continuous $f:[0,T]\to \RR$,$$\int_0^t f(s)da(s)=\lim_{n\to \infty} \sum_{i = 1}^{p_n} f\left(t^n_{i-1}\right)\left(a\left(t_i^n\right) - a\left(t_{i-1}^n\right)\right).$$

In these situations I will adopt the following shorthand:
- Say "pick a mesh" to enter shorthand mode.
- $\lim \sum$ means $\lim_{n\to\infty} \sum_{i = 1}^{p_n}$. If the limit on the right hand side is over a random variable, then the limit is in probability.
- $t$ means $t^n_{i-1}$
- $\Delta \bullet$ or $\Delta \bullet(t)$ means $\bullet\left(t^n_i\right) - \bullet\left(t^n_{i-1}\right)$
- $\bullet$ or $\bullet(t)$ otherwise means $\bullet\left(t^n_{i-1}\right)$.
The above statement is thus written in the suggestive form:

>[!idea] Shorthand
> Pick a mesh. For any continuous $f:[0,T]\to \RR$,$$\int_0^t f(s)da(s) = \lim\sum f\Delta a.$$