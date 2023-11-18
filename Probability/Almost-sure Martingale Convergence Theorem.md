> [!theorem] AS MCT
> Let $X$ be an $L^1$-bounded supermartingale. Then, there exists an integrabl $\FFF_\infty$-measurable random variable $X_\infty$ such that $X_n\to X_\infty$ almost surely as $n\to \infty$.

> [!idea] This is obvious
> Suppose you do not converge. Then, you contain an unbounded amount of [[upcrossings]]. This motivates us to perform strong bounds using the [[Doob's upcrossing inequality]], which turns out to kill immediately.

>[!proof]-
> Let
> $$\Omega_\infty = \{\lim\inf \abs{X_n} < \infty\},\qquad \Omega_{a,b} = \{U[a,b] < \infty\}$$
> for $a<b\in \QQ$. Then, let
> $$\Omega_0 = \Omega_\infty \cap \bigcap_{a < b\in \QQ} \Omega_{a,b}$$
> Observe that $X_n(\omega)$ converges iff $\Omega \in \Omega_0$. By [[Convergence properties of Lebesgue Integral|Fatou]] and [[Doob's upcrossing inequality|Doob]],
> $$\EE[\lim\inf \abs{X_n}] \leq \lim\inf \EE\abs{X_n},\qquad (b-a)\EE[(U[a,b])] \leq \abs{a} + \sup_{n\geq 0} \EE\abs{X_n}$$
> We said that $X$ was $L^1$-bounded though! So $\EE[U[a,b]]$ and $\EE[\lim\inf\abs{X_n}]$ is finite, and thus $U[a,b]$ and $\lim\inf \abs{X_n}$ are finite almost surely. Thus the countable union of $\Omega_{a,b}$ and $\Omega_0$ is also almost sure.
> 
> So why not let $X_\infty = \lim_{n\to \infty} X_n \id_{\Omega_0}$ (pointwise)? Then $X_n \to X_\infty$ almost surely, $X_\infty$ is $\FFF_\infty$-measurable, and $\abs{X_\infty}\leq \lim\inf\abs{X_n}$, thus $X_\infty$ is integrable.