In general, $\exp(x+y)\neq \exp(x)\exp(y)$ (this isn't even true for matrices). The map
$$
	\mu(x,y) = \log\left(\exp(x)\exp(y)\right)
$$
expresses the product in $G$ in the coordinate chart induced by $\log$. $\mu(x,0) = \mu(0,x) = x$, thus $\mu$ can be (Maclaurin) expanded on some neighborhood $U\times U\to \fg$ to
$$
	\mu(x,y) = x + y + \frac12\mu_2(x,y) + \dots
$$
where $\mu_2$ is a skew-symmetric bilinear form. The map $\mu_2$ is called the ==**commutator**==, and we denote $[x,y] = \mu_2(x,y)$. Flipping it back around, we have the (tautological) identity

>[!theorem] Baker-Campbell-Hausdorff Formula
>$$
>	\exp(x)\exp(y) = \exp(x + y + \frac12[x,y] + \cdots)
>$$

>[!example] $\GL$
>In the case of $G = \GL_n(\KK)$, we can explicitly write
>$$
>\begin{align*}
>	\exp(x)\exp(y)
>	&= \left(1 + x + \frac{x^2}{2} + \cdots \right)\left(1 + y + \frac{y^2}{2} + \cdots \right)\\
>	&= 1 + x + y + \frac{(x+y)^2}{2} + \frac{xy - yx}{2} + \cdots\\
>	&= \exp\left(x + y + \frac{xy - yx}{2} + \cdots \right)
>\end{align*}
>$$
>thus $[x,y] = xy - yx$ and the commutator coincides with the usual definition.

[[Adjoint Coincidence|This is true in more generality]].

A slightly more natural stepping stone is here:
- [[How to invert the commutator]]