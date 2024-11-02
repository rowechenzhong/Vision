>[!idea] Physicists:
>Wait, you can't always do this?

>[!theorem]
> Let $U\subset \RR$ be open, and write a function $f:U\times E\to \RR$. We expect that
> $$
> 	\frac{\der}{\der t}\int_E f(t,x)\mu(dx) = \int_E \frac{\pa f}{\pa t}(t,x)\mu(dx)
> $$
> This is true (and all quantities are defined) if:
> 1. Your objects are actually defined:
> 	1. $f(t,\bullet)$ is integrable for all $t$.
> 	2. $f(\bullet, x)$ is differentiable for all $x$.
> 2. You have this stupid regularity condition which lets you apply dominated convergence:$$\forall x,t \qquad \abs{\frac{\pa f}{\pa t}(t,x)} \leq g(x)$$
>    for some integrable $g$.

> [!proof]- You know how this is going to go
> Okay fine. Ummmm, fix a $t\in U$. Let's consider a sequence $h_n\to 0$ such that $t+h_n$ lies inside $U$. Let our differences be
> $$
> 	\frac{f(t + h_n, x) - f(t, x)}{h_n} - \frac{\pa f}{\pa t}(t,x)
> $$
> By definition of partial derivative, this goes to $0$ for all $x\in E$. Thus, for all $t$, $\frac{\pa f}{\pa t}(t, \bullet)$ is a limit of measurable functions and thus measurable as well (this isn't true in general I think). By the third condition, $\frac{\pa f}{\pa t}(t, \bullet)$ is integrable.
> 
> By the [[mean value theorem]],  $\abs{\frac{f(t+h_n, x) - f(t,x)}{h_n}}$ is equal to $\frac{\pa f}{\pa t}(t + \delta, x)$ for some $\delta < h_n$. Thus this is upper bounded by $g(x)$ as well, and we can execute dominated convergence.
> $$
> \begin{align*}
> \int_E \frac{\pa f}{\pa t}(t,x)\mu(dx) &= \lim \int_E \frac{f(t + h_n, x) - f(t, x)}{h_n}\mu(dx)
> \end{align*}
> $$
> Tada, win.
> $$
> \begin{align*}
> &= \lim \frac{1}{h_n}\left\{\int_E f(t + h_n,x)\mu(dx) - \int f(t,x)\mu(dx)\right\}\\
> &= \frac{\der}{\der t} \int_E f(t,x)\mu(dx)
> \end{align*}
> $$
>