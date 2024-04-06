In this section, we'll be making extensive use of $L^2$ geometry to get some facts on the table.

>[!claim] $L^2$ WLLN
>Let $X, X_i \in L^2$ be **uncorrelated and identically distributed**; assume $\abs{\EE[X]} < \infty$. Then $\overline{X_n}\to \EE[X]$ in the $L^2$ norm and in probability, as $n\to \infty$.

>[!proof] Smash with $L^2$
>Well, $\norm{\overline{X} - \EE[X]}_2^2 = \frac{\Var(X)}{n}\to 0$.
>
>Chebyshev's inequality kills the other one; $\PP(\abs{X - \EE[X]} \geq \eps) = \frac{\Var(X)}{\eps^2}\to 0$.

>[!claim] Triangle $L^2$ WLLN
> Suppose you have a triangular array of **uncorrelated** $X_{i,j}\in L^2$ over $i\geq j$, such that $\Var(X_{n,k}) \leq C < \infty$ is bounded for all $k,n$. Then, if $S_n = \sum_k X_{n,k}$.
> $$ \frac{S_n - \EE[S_n]}{n}\to 0$$
> in $L^2$ and in probability, as $n\to \infty$.

> [!proof] One more time
> The $S_i$'s are uncorrelated (linearity) thus
> $$ \norm{ \frac{S_n - \EE[S_n]}{n}}_2^2 = \frac{1}{n^2} \sum_{k = 1}^n \Var(X_{n,k}) \leq \frac{C}{n}$$
> showing $L^2$ convergence. Chebyshev is the same:
> $$\PP(\abs{S_n - \EE[S_n]}\geq n\eps) \leq \frac{\Var\left(S_n\right)}{n^2 \eps^2}\leq \frac{C}{n \eps^2}\to 0$$

Okay, one more time with the $L^2$ stuff. I've got a triangular array of $Y_{n,k}$ over $n\geq k$; let $T_n = \sum_{k = 1}^n Y_{n,k}$. We assume that, for fixed $n$, $Y_{n,k}$ are **independent**.

> [!claim] WL for triangular Array
> Suppose there is a sequence $b_n \to \infty$ such that
> $$ \frac{1}{b_n^2} \sum_{k = 1}^n \EE\left( Y^2_{n,k}\right)\to 0.$$
> Then, $\frac{T_n - \EE[T_n]}{b_n}\to 0$ in probability.

>[!proof] One last time
>Look:
>$$ \norm{ \frac{T_n - \EE[T_n]}{b_n}}_2^2 = \frac{1}{b_n^2}\sum_{k = 1}^n \Var(Y_{n,k})$$
>and convergence in $L^2$ implies convergence in probability.

Now, we're not assuming $X_{n,k} \in L^2$ anymore; the training wheels are off. The following flagrantly ugly theorem sets up a series of $Y_{n,k}$'s which are nicer than the $X_{n,k}$'s, and proves WLLN on them.

> [!claim] WL for triangular Array
> Give me a sequence $b_n \to \infty$, and I'll define a set of filtered RVs and corresponding row summations.
> $$ Y_{n,k} = X_{n,k}\cdot \id\left\{ \abs{X_{n,k}} \leq b_n\right\},\qquad T_n = \sum_{k = 1}^n Y_{n,k}$$
> If, after filtering by $b_n$, things have reasonable variance
> $$ \frac{1}{b_n^2} \sum_{k = 1}^n \EE\left( Y^2_{n,k}\right)\to 0$$
> and $\PP(S_n\neq T_n)\to 0$, then $\frac{S_n - \EE[T_n]}{b_n}\to 0$ in probability.
>>[!idea]- Rewriting the claims
>>The first claim is achieved if the $b_n$'s expand to cover the $X$'s.
>> $$\PP(S_n\neq T_n) \leq \sum_{k = 1}^n \PP\left(X_{n,k} \neq T_{n,k}\right) = \sum_{k = 1}^n \PP\left( \abs{X_{n,k}} > b_n\right)\to 0$$
> ^stupid-lln

These assumptions are just some interfacing to make the previous claim relevant.

>[!proof]- Some cap
> If  $\PP(S_n\neq T_n) \leq \sum_{k = 1}^n \PP\left(X_{n,k} \neq T_{n,k}\right) = \sum_{k = 1}^n \PP\left( \abs{X_{n,k}} > b_n\right)$ which vanishes; thus the conclusion holds iff
> $$ \frac{T_n - \EE[T_n]}{b_n} \to 0$$
> in probabililty. Also, the $X_{n,k}$ were independent, thus the $Y_{n,k}$ are. Apply the previous theorem verbatim.