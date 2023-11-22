Give me a [[Backwards Filtration]] $\hat{\FFF}_n$.

> [!theorem]
> For all $Y\in L^1(\FFF)$, $\EE(Y | \hat{\FFF}_n) \to \EE(Y | \hat{\FFF}_\infty)$, AS and in $L^1$.

>[!idea]
>This makes sure you understand the proofs we did in [[Martingale Convergence Theorems]] LOL.

>[!problem]
> Let $X_i = \EE[Y | \hat\FFF_i]$. Show $X_i$ admits an AS limit.

> [!solution]-
> Let
> $$\Omega_\infty = \{\lim\inf \abs{X_n} < \infty\},\qquad \Omega_{a,b} = \{U[a,b] < \infty\}$$
> for $a<b\in \QQ$. Then, let
> $$\Omega_0 = \Omega_\infty \cap \bigcap_{a < b\in \QQ} \Omega_{a,b}$$
> Observe that $X_n(\omega)$ converges iff $\omega \in \Omega_0$. Observe that for all prefixes, $\{X_{n-k}\}_{k = 1}^n$ is a martingale, thus taking the supremum, [[Doob's Maximal Inequalities|Doob]] applies verbatim. Thus by [[Convergence properties of Lebesgue Integral|Fatou]] and [[Doob's upcrossing inequality|Doob]],
> $$\EE[\lim\inf \abs{X_n}] \leq \lim\inf \EE\abs{X_n},\qquad (b-a)\EE[(U[a,b])] \leq \abs{a} + \sup_{n\geq 0} \EE\abs{X_n}$$
> But $\EE[\abs{X_n}]\leq \EE[\EE[\abs{Y} | \hat\FFF_n]] = \EE[\abs{Y}]<\infty$. 
> 
> So $\EE[U[a,b]]$ and $\EE[\lim\inf\abs{X_n}]$ is finite, and thus $U[a,b]$ and $\lim\inf \abs{X_n}$ are finite almost surely. Thus the countable union of $\Omega_{a,b}$ and $\Omega_0$ is also almost sure.
> 
> So why not let $X_\infty = \lim_{n\to \infty} X_n \id_{\Omega_0}$ (pointwise)? Then $X_n \to X_\infty$ almost surely, $X_\infty$ is $\FFF_\infty$-measurable, and $\abs{X_\infty}\leq \lim\inf\abs{X_n}$, thus $X_\infty$ is integrable.

>[!problem]
>Show $X_i$ admits an $L^1$ limit.
 
>[!solution]-
> [[Conditional Expectations are UI]]

>[!problem]
>Show $X_i$ converge to $\EE[Y | \hat\FFF_\infty]$ as desired.

