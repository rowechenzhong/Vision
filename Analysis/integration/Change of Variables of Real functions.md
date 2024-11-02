>[!example]
>This can be proven independently, but for all $\phi:[a,b]\to \RR$ continuously differentiable, for all non-negative Borel functions $f:[\phi(a), \phi(b)]\to \RR$,
>$$
>	\int_{\phi(a)}^{\phi(b)} f(y)\der y = \int_a^b f(\phi(x))\phi'(x)\der x
>$$

> [!proof]- Direct, so I feel better
> Are you serious right now. I'll show this for all intervals. If $f$ is the indicator on the interval $[\ell, r]\subset [\phi(a), \phi(b)]$, then we wish to show
> $$
> 	\mu([\ell, r]) = \int_{[a,b]\cap \phi^{-1}(E)} \phi'(x)\der x
> $$
> Fine I guess you have to pass through the [[Fundamental Theorem of Calculus]].
> 

>[!todo]
>What was this massacre. Go fix it.

> [!proof]- Huh, what are you saying (this is cap)
> Indeed, let's say WLOG $\phi'(x) > 0$ by like translating by a linear function or whatever; then $\phi$ is increasing and thus invertible on its domain, with continuous inverse. Then, $\phi$ is a random variable with PDF $\phi'$ by definition. We can let $g(y) = f(y)\phi'(\phi^{-1}(y))$; this is a composition of Borel functions and thus Borel. We wish to show:
> $$
> \begin{align*}
> 	\int_{\phi(a)}^{\phi(b)} g(y)\phi'(\phi^{-1}(y))^{-1}\der y&= \int_a^b g(\phi(x))\der x
> \end{align*}
> $$
> This would follow if $\phi'(\phi^{-1}(y))^{-1}\der\mu(y)$ was the pushforward measure $\der(\phi_\sharp \mu)$. But this is kind of clear; $\phi_\sharp \mu = \mu\circ \phi^{-1}$.