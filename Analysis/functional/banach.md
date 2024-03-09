# Banach Spaces 

Great. Let's get some tech on the board now. Recall that a topological space is ==**complete**== if every Cauchy sequence converges. 

> [!definition] Banach Space
A ==**Banach space**== is a normed vector space which is complete with respect to the metric induced by the norm. 

$B$ forever denotes a Banach space, and $C$ has Banach-space connotations.

## Summability 

> [!definition] Summable
Let $\{v_n\}_{n=1}^\infty$ be a sequence of vectors in a normed vector space $V$. Then the series $\sum_{n=1}^\infty v_n$ is ==**summable**== if the sequence of partial sums converges in $V$, and the limit is called the ==**sum**== of the series. If $\sum_{n=1}^\infty \norm{v_n}$ converges, then $\sum_{n=1}^\infty v_n$ is called ==**absolutely summable**==. 

Observe that if $\{v_n\}$ is absolutely summable, then the partial sums are Cauchy. You might not be convergent for the silly reason that $V$ might not be complete-- and in fact, this gives us a nice way to check whether $V$ is complete at all. 

> [!theorem] Banach iff absolutely summable implies summable
$V$ is Banach if and only if every absolutely summable series is summable. 

> [!proof]- Not Deep
If you're Banach already, Cauchy sequences converge so we're done. Suppose every absolutely summable series is summable. Then, for any Cauchy sequence, you can just pull out a subsequence of $N_i$ such that for all $a,b\geq N_i$, $$ \abs{v_a - v_b} < \frac{1}{2^i} $$ Thus the series $v_{N_{i+1}} - v_{N_i}$ is absolutely summable, so it converges. 


>[!theorem] $C_\infty(X)$ is a Banach Space
$C_\infty(X)$ is a Banach space under the $\infty$ norm. 

> [!proof]- Not deep either
We are given a sequence of functions $\{f_n\}_{n=1}^\infty$ which is Cauchy. In particular, they converge pointwise to some function $f_\infty$. We must show: 
>  -  $f_n$ also converges to $f_\infty$ in the $\infty$ norm. 
>  
>  -  $f_\infty$ is bounded and continuous. Don't forget this step! The whole point is to show that the limit is in $C_\infty(X)$. 
>  
>  To show $f_n$ converges to $f_\infty$ in the $\infty$ norm, for all $\delta$ we must exhibit an $N$ such that $\norm{f_n - f_\infty}_\infty < \delta$ for all $n \geq N$. Fine. We know that $\{f_n\}$ is Cauchy, so pick the $N$ such that $\norm{f_n - f_m}_\infty < 0.001\delta$ for all $n, m \geq N$. By definition of supremum, this means $$ \forall m \geq N \forall x\in X \abs{f_m(x) - f_N(x)} < 0.001\delta. $$ Then, we claim that $\norm{f_N - f_\infty} < 0.01\delta$. Suppose this were not true; then there exists some $x\in X$ such that $\abs{f_N(x) - f_\infty(x)} > 0.01\delta$. This implies for all $m \geq N$, $\abs{f_m(x) - f_\infty(x)} > 0.009\delta$, which contradicts the assumption that $f_\infty$ was the pointwise limit. This concludes the proof of convergence. Next up, let's show $f_\infty$ is bounded. Pick some $f_N$ such that $\norm{f_N - f_\infty} < 1$. Then, for all $x\in X$, $\abs{f_\infty(x)} \leq \abs{f_N(x)} + 1$. Since $f_N$ is bounded, so is $f_\infty$. Finally, we show $f_\infty$ is continuous. Fix any $x_0\in X$, and any $\delta \in \RR_{> 0}$; I need to exhibit an open set $x_0 \in U \subseteq X$ such that $f_\infty(U) \subseteq B_\delta(f_\infty(x_0))$. Well, there exists an $N_1$ such that for all $n \geq N_1$, $\norm{f_n - f_\infty} < 0.0001\delta$. There exists an $N_2$ such that for all $n \geq N_2$, $\abs{f_\infty(x_0) - f_n(x_0)} < 0.0001\delta$. Let $N = \max(N_1,N_2)$. Okay great, now observe that $f_N$ is continuous, so there exists an open set $x_0 \in U \subseteq X$ such that $f_N(U) \subseteq B_{0.0001\delta}(f_N(x_0))$. Perfect; this means that $f_\infty(U) \subseteq B_{0.0002\delta}(f_N(x_0))\subseteq B_{0.0003\delta}(f_\infty(x_0))$, which is all we wanted. 

> [!example] Convergent Sequences
Observe that $$ c_0 = \{a\in \ell^\infty: \lim_{j\to \infty} a_j = 0\} $$ is Banach. This is true because one can place the discrete metric on $\NN$ after which this falls right out.