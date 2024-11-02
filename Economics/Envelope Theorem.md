>[!theorem] Envelope Theorem
> Let $f(x, \theta)$ be a function where $x$ is chosen to maximize $f$ for a given parameter $\theta$. Denote the maximized value as $v(\theta) = \max_x f(x, \theta)$. Under regularity conditions, the derivative of $v(\theta)$ with respect to $\theta$ is given by:
>
> $$ \frac{dv(\theta)}{d\theta} = \frac{\partial f(x^*(\theta), \theta)}{\partial \theta} $$
>
> where $x^*(\theta)$ is the maximizer of $f(x, \theta)$ for the given parameter $\theta$.
>
> This result holds even though $x^*(\theta)$ may vary with $\theta$, because the envelope theorem focuses only on the direct effect of $\theta$ on $f$, ignoring the effect of changes in $x^*(\theta)$.

In the constrained version, we might want to consider $\vec{x}\in \RR^n$ subject to $g(\vec{x}) = 0$, and let $v(\theta) = \max_{\vec{x}: g(\vec{x}) = 0} f(\vec{x}, \theta)$. Under the constraint,$$
\frac{dv(\theta)}{d\theta} = \frac{\pa f}{\pa \theta}(x^*(\theta), \theta) + \frac{\pa f}{\pa x^\mu} \frac{\pa (x^*)^\mu(\theta)}{\pa \theta} 
$$Great. Now, note that $\frac{\pa f}{\pa x^\mu}\left(x^*, \theta \right)$. This thing is zero for any infinitesimal movement which locally respects the gradient of $g(\vec{x})$, i.e. any $\delta x^\mu$ such that $(\delta x^\mu) \pa_{x^\mu} g = 0$, because along $g$ we know that $\frac{\pa f}{\pa x_\mu}$ is maximized. The problem is that we can walk "into" the direction of $\frac{\pa g}{\pa x^\mu}(x^*(\theta), \theta)$ and then die.