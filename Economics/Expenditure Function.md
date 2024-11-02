---
aliases:
  - Hicksian Demand
  - Compensated Demand
  - Slutsky Equation
---
Solve the indirect utility function for income; $E(p_x, p_y, u)$ defined such that $V(p_x, p_y, E(p_x, p_y, u)) = u$.

This yields the ==**Hicksian**== or ==**compensated**== demands; in order to obtain utility $u$ with these prices, what is the GTO amount of $x$ to buy? $x^c(p_x, p_y, u)$.

# Properties (14.04)
1. Homogenous with degree 1 if you hold $u$ fixed.
2. Sheperd's Lemma$$x^c(p_x, p_y, u) = \frac{\pa E}{\pa p_x}.$$
4. $E$ is concave in $(p_x, p_y)$ holding $u$ fixed. Notably, the self-substitution effect is negative $\frac{\pa x^c}{\pa p_x}\leq 0$ as expected.
5. Cross-price Slutsky Equation
$$\frac{\pa x^c}{\pa p_y} = \frac{\pa x^*}{\pa p_y} + \frac{\pa x^*}{\pa I} y^*.$$We like to call $\frac{\pa x^*}{\pa I} y^*$ the ==**income effect**== (of compensation); this is notably not the same thing as the [[Quantification|Income Elasticity]] (there is an extra factor of $y^*$). The same equation holds for $x,y$ equal by the way. We like to call $\frac{\pa x^c}{\pa p_x}$ the ==**substitution effect**== (which measures the effect of substituting to every other product in the market).

> [!proof]- Sheperd's Lemma
> In GTO, $p_x x + p_y y = I$, and I want to maximize $u(x,y)$; thus $\frac{\pa u}{\pa x}(x^*, y^*) = \lambda p_x$ and $\frac{\pa u}{\pa y}(x^*, y^*) = \lambda p_y$. Uhh, the Lagrange thing here is $\LL(x,y,\lambda, I) = u(x, y) - \lambda(p_xx + p_yy - I)$. What's $\frac{\pa u^*}{\pa I}$? Well, $x,y,\lambda$ are chosen to optimize this guy, so note that $\frac{d u^*}{dI} = \frac{d\LL(x^*(I),y^*(I),\lambda(I), I)}{dI} = \frac{\pa \LL}{\pa I} = \lambda$. Sure, whatever. $u^*$ means the same thing as $V(I, p_x, p_y)$, so like sure we've found that this $\lambda$ guy is just $\frac{\pa V}{\pa I}$.
> 
> For $\frac{\pa V}{\pa p_x}$, we do the same thing; the full Lagrangian here is $\LL(x, y, \lambda, I, p_x, p_y) = u(x, y) - \lambda(p_xx + p_yy - I)$, but we always extremize over $x, y, \lambda$. When I say $\frac{\pa V}{\pa p_x}$, I really mean $\frac{\pa}{\pa p_x}\left(\max_{x,y,\lambda} \LL\right)\big\vert_{p_y, I}$, which is obviously just $-\lambda x$.
> 
> Okay, take the total derivative of $V(p_x, p_y, E(p_x, p_y, u)) = u$ with respect to $p_x$ or something.$$
> \frac{\pa V}{\pa p_x} + \frac{\pa V}{\pa I} \frac{\pa E}{\pa p_x} = 0.
> $$Great. Magically, we find the desired expression.