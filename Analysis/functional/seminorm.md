A ==**seminorm**== is a like a [[normed|norm]]; it satisfies homogeneity and the triangle inequality, but not definiteness. 
-  (==**Homogeneity**==) $\norm{\lambda v} = \abs{\lambda} \norm{v}$, and 
-  (==**Triangle Inequality**==) $\norm{v + w} \leq \norm{v} + \norm{w}$.

>[!problem]
>Show that seminorms are convex.

>[!solution]-
>Pick some $u,v$ with $\norm{u} = a$ and $\norm{v} = b$; then
>$$
>	\norm{\lambda u + (1-\lambda)v}\leq \lambda\norm{u} + (1-\lambda)\norm{v}
>$$
>by triangle inequality, as desired.


>[!problem]
>Show that a seminorm is continuous iff $p^{-1}([0, 1))$ contains an open ball.

>[!solution]-
>Well, we wish to show that for any $p(v)\in \RR$ and $\eps > 0$, there exists an open set $U\subset X$ such that $p(v)\in p(U)\subset (a-\eps, a+\eps)$. Well okay, I know $p^{-1}([0, \eps))$ contains an open ball $V$, so consider $v + V$ and use triangle inequality.