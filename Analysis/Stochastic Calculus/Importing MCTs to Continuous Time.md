See the discrete [[Martingale Convergence Theorems|MCT]].

> [!theorem] AS MCT
> Let $X$ be an $L^1$-bounded supermartingale. Then, there exists an integrable $\FFF_\infty$-measurable random variable $X_\infty$ such that $X_t\to X_\infty$ almost surely as $t\to \infty$.

> [!theorem] $L^1$ MCT
> Suppose $X$ is a UI martingale. Then, there exists $X_\infty \in L^1(\FFF_\infty)$ such that $X_t\to X_\infty$ almost surely and in $L^1$. $X_t = \EE(X_\infty | \FFF_t)$ almost surely for all $t\geq 0$.
> 
> On the other hand, for all $Y\in L^1(\FFF_\infty)$, if the filtration satisfies the usual conditions, $X_t = \EE[Y | \FFF_t]$ is a UI martingale such that $X_t\to Y$ AS in and $L^1$.

> [!theorem] $L^p$ MCT
> Suppose $X$ is an $L^p$-bounded martingale. Then, there exists $X_\infty \in L^p(\FFF_\infty)$ such that $X_t\to X_\infty$ almost surely and in $L^p$. $X_t = \EE(X_\infty | \FFF_t)$ almost surely for all $t\geq 0$.
> 
> On the other hand, for all $Y\in L^p(\FFF_\infty)$, if the filtration satisfies the usual conditions, $X_t = \EE[Y | \FFF_t]$ is a UI martingale such that $X_t\to Y$ AS in and $L^p$.