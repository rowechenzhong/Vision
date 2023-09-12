>[!theorem]
>Suppose $f: \RR^{n + m}\to \RR^m$ is a continuously differentiable function. Let $\RR^{n + m}$ have coordinates $(\vec{x}, \vec{y})$. Fix a point $(\vec{a}, \vec{b})$ with $f(\vec{a}, \vec{b}) = \vec{0}$. Consider the portion of the [[Jacobian matrix]] containing the partial derivatives with respect to $\vec{y}$, only. If
>$$
>	J_{f,\vec{y}}(\vec{a},\vec{b}) = \left[ \frac{\pa f_i}{\pa y_j}(\vec{a}, \vec{b})\right]
>$$
>is invertible, then there exists:
> - An open set $U\subset \RR^n$ containing $\vec{a}$.
> - A function $g:U\to \RR^m$ such that $g(a) = b$ and $f(\vec{x}, g(\vec{x})) = 0$ for all $x\in U$.

In multivariable calculus, the ==**implicit function theorem**== is a tool that allows relations to be converted to functions of several real variables. It does so by representing the relation as the graph of a function. There may not be a single function whose graph can represent the entire relation, but there may be such a function on a restriction of the domain of the relation. The implicit function theorem gives a sufficient condition to ensure that there is such a function.