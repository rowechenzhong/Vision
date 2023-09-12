There are $3$ main types of convergence of functions $(\Omega, \FFF, \mu)\to (\RR, \BBB_\RR)$ relevant for our purposes; each implies the next. Given a sequence of functions $f_n$ and another function $f$,
1. $f_n\to f$ ==**pointwise**== if $f_n(\omega)\to f(\omega)$ for all $\omega$.
2. $f_n\to f$ ==**with respect to $\mu$ almost everywhere**== if
   $$\mu\left( \left\{\omega: \lim_{n\to\infty} f_n(\omega) \neq f(\omega)\right\}\right) = 0$$
3. $f_n\to f$ **==in $\mu$-measure**== if for all $\eps > 0$, 
   $$ \lim_{n\to \infty} \mu\left( \left\{\omega: \abs{f_n(\omega) - f(\omega)} \geq \eps\right\}\right) = 0$$
In [[Probability]] theory, these are called pointwise, **==almost sure==**, and **==in probability==** convergence.
Finally, there is convergence in $L^2$ norm, which is what it sounds like. This implies convergence in $\mu$-measure on probability measures.
> [!todo] prove this shit smh

# Random Problems

>[!problem]
>Suppose $X_1, X_2,\cdots$ converge in probability. Show they also converge almost surely along some subsequence.

>[!problem] Cauchy in Probability
>Suppose $X_1, X_2, \dots$ are random variables such that
>$$\forall \eps > 0, \lim_{m,n\to \infty} \PP\left(\abs{X_m - X_n} \geq \eps\right)\to 0$$
>Then, we say $X_i$ are **==Cauchy in Probability==**. Show that there exists a random variable $X$ such that $X_i\to X$ almost surely.

> [!solution]-
> Ummm, first lets unpack some quantifiers.
>$$\forall \eps,\delta > 0 \quad \exists M \forall m,n\geq M\qquad \PP\left(\abs{X_m - X_n} \geq \eps\right) < \delta$$
>And we want to show that there exists an $X$ such that
>$$\forall \eps,\delta > 0 \quad \exists N \forall n\geq N\qquad \PP\left(\abs{X_n - X}\geq \eps\right) < \delta$$
>
>> [!proof]- There almost surely exists a convergent subsequence.
>>Cool. For all $k$, I construct an $M_k$ such that for all $m,n\geq M_k$, $$\PP\left(\abs{X_m - X_n}\geq 0.01 \cdot 2^{-k}\right) < 0.01 \cdot 2^{-k}$$
>>
>>The event that $\abs{X_{M_k} - X_{M_{k+1}}} < 0.01 \cdot 2^{-k}$ (which is an event, because it is the preimage of an interval under a measurable function) occurs with probability $0.01 \cdot 2^{-k}$. Let $E$ be the event that only finitely many such discrepancies occur (this is clearly a countable union of intersections, and is thus an event). By [[Borel-Cantelli]], $\PP(E) = 1$.
>>
>>Thus let $X$ equal the limit of $X_{M_k}$ on $E$, and set $X = 0$ elsewhere. This is a random variable because it is the limit of random variables.
>
>>[!proof]- Verification
>> 
>> Now, if $\eps,\delta > 2^{-k}$, we can select $N = M_k$. For all $n\geq M_k$, 
>> - $\abs{X_n - X_{M_k}} < 0.01\cdot 2^{-k}$ with probability at least $1 - 0.01\cdot 2^{-k}$.
>> - $\abs{X_m - X_{m +1}} < 0.01 \cdot 2^{-m}$ for all $m\geq k$ with probability at least $1 - 0.01\cdot \left(2^{-k} + 2^{-k-1} + \cdots\right)$.
>>   
>>Thus, with probability at least
>>$$1 - 0.01\cdot 2^{-k} - 0.01\cdot \left(2^{-k} + 2^{-k-1} + \cdots\right) > 1 -  2^{-k} > 1 - \delta,$$
>>we have
>>$$\abs{X_n - X} < 0.01\cdot \left(2^{-k} + 2^{-k} + 2^{-k-1} + \dots\right) < 2^{-k} < \eps$$
>>as desired.
