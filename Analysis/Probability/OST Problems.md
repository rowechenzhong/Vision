>[!claim] 18.615 tech
>Suppose $X$ is a supermartingale on some filtered probability space, and let $T$ be an a.s. finite stopping time. Prove that $\EE[X_T] \leq \EE[X_0]$ if at least one of the following conditions hold.
> 1. The process $X$ is bounded ($\exists M > 0: \forall n\geq 0, \abs{X_n} \leq M$ a.s.)
> 2. The process $X$ has bounded increments ($\exists M > 0 : \forall n\geq 0, \abs{X_{n+1} - X_n}\leq M$ a.s.) and $\EE[T] < \infty$.
>    
>If $X$ is a martingale, $\EE[X_T] = \EE[X_0]$ under these conditions.

>[!problem] Prove it

> [!solution]-
> The supermartingale case immediately implies the martingale case,
> so we only prove the supermartingale case.
> 
> First off, if $T$ were bounded, then the Bounded Optional Stopping Theorem would conclude. In particular, $\EE[X_{T\land n}] \leq \EE[X_0]$ for any constant $n\geq 0$. So all we want to show is that $\EE[X_{T\land n}] \to \EE[X_T]$. All we have to do is rip through [[Convergence properties of Lebesgue Integral|Fatou]] by providing an integrable function which dominates all $X_{T\land n}$ almost surely.  In the first case, $X_{T\land n}$ is dominated by $M$ almost surely, so we conclude.  In the second case, we need to use the condition $\EE[T] < \infty$ by expanding in terms of increments. We know $$     X_{T\land n} = X_0 + \sum_{t = 0}^{n-1} (X_{t+1} - X_t)\id_{t\leq T} $$ thus $$\begin{align*}     \abs{X_{T\land n}} &\leq \abs{X_0} + \sum_{t\geq 0} \abs{X_{t+1} - X_t}\id_{t\leq T}\\     &\leq \abs{X_0} + M\sum_{t\geq 0} \id_{t\leq T}\\     &\leq \abs{X_0} + M\EE[T] < \infty \end{align*}$$ The RHS of the top line is independent of $n$, and is our dominating function. We conclude.