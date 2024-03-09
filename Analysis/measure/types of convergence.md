There are $3$ main types of convergence of functions $(\Omega, \FFF, \mu)\to (\RR, \BBB_\RR)$ relevant for our purposes; each implies the next. Given a sequence of functions $f_n$ and another function $f$,
1. $f_n\to f$ ==**pointwise**== if $f_n(\omega)\to f(\omega)$ for all $\omega$.
2. $f_n\to f$ ==**with respect to $\mu$ almost everywhere**== if$$\mu\left( \left\{\omega: \lim_{n\to\infty} f_n(\omega) \neq f(\omega)\right\}\right) = 0$$
3. $f_n\to f$ **==in $\mu$-measure==** if for all $\eps > 0$, 
   $$ \lim_{n\to \infty} \mu\left( \left\{\omega: \abs{f_n(\omega) - f(\omega)} \geq \eps\right\}\right) = 0$$
In [[Probability]] theory, these are called pointwise, **==almost sure==**, and **==in probability==** convergence.

Other common types of convergence:
 - Convergence in $L^2$ norm. This implies convergence in $\mu$-measure on probability measures.
 - [[Weak Convergence|Convergence in Distribution]].

> [!todo] prove this shit smh

# Random Problems

>[!problem]
> Show $f_n\to f$ ae if $$
> 	\forall \delta>0 \qquad \PP\left(\exists N: \forall m > N, \abs{f_m(\omega) - f(\omega)} > \delta\right) = 0
> $$

>[!problem]
>Suppose $X_1, X_2,\cdots$ converge in probability. Show they also converge almost surely along some subsequence.

>[!solution]- Boring
> WLOG $X = 0$.
> 
> Okay! Suppose $X_1, X_2,\dots,\to X$ in probability, i.e. for all $\frac1n > 0$, there exists an $a_n$ such that for all $m \geq a_n$, 
> $$
> 	\mu\left(\{\omega: \abs{X_m(\omega)}\geq \frac1n\}\right)\leq \frac1n
> $$
> In this subsequence, for all $\frac1n$,
> 
> $$
> 	\mu\left(\{\omega: \lim_{m\to \infty} \abs{X_{a_m}(\omega)} \geq \frac1n\}\right) = 0
> $$
> 
> right? Because it's an intersection of a bunch of sets, so by monotonicity it must have measure $< \frac1n$ for all $n$; this means it has measure $0$.
> 
> Okay?
> 
> But then, a countable union of measure-0 sets is measure zero. So we're done.

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

>[!problem] Convergence in Distribution is pretty good
>Suppose $X_n\to X$ in distribution. Then, there are random variables $\tilde{X}_n$ defined one a common probability space $(\Omega, \FFF, \PP)$ such that $\tilde{X}$ has the same distribution as $X$, $\tilde{X}_n$ has the same distribution as $X_n$, and $\tilde{X}_n\to \tilde{X}$ almost surely.