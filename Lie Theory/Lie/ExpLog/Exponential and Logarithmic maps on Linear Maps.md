The main point of writing out the [[14 classical Lie groups]] was to motivate the exponential and logarithmic maps in the context of linear algebra.

Recall:

> [!definition] Exponential and Logarithmic Maps
> We have an analytic function $\exp: \gl_n(\KK)\to \GL_n(\KK)$ via
>
> $$
> 	\exp(a) = \sum_{n = 0}^\infty \frac{a^n}{n!}
> $$
>
> and a function $\log:\GL_n(\KK)\to \gl_n(\KK)$
>
> $$
> 	\log A = -\sum_{n = 1}^\infty \frac{(1-A)^n}{n}
> $$
>
> which is analytic near $1\in \GL_n(\KK)$ and well-defined if the spectral radius of $1-A$ is less than $1$.

These satisfy:

> [!claim]
>
> 1.  They are mutually inverse.
> 2.  They are conjugation-invariant.
> 3.  $d\exp_0 = d\log_1 = \Id$
> 4.  If $xy = yx$, then $\exp(x + y) = \exp(x)\exp(y)$. If $XY = YX$ then $\log(XY) = \log X + \log Y$ (for $X,Y$ sufficiently close to $1$).
> 5.  For $x\in \gl_n(\KK)$, the map $t\to \exp(tx)$ is a homomorphism of Lie groups $k\to \GL_n(\KK)$.
> 6. $\det \exp(a) = \exp(\Tr a)$ and $\log(\det A) = \Tr(\log A)$.

So:

>[!example] $\SL_n$ is a Lie Group
>The group $G = \SL_n$ satisfies $\det A = 1$, so for $A$ close to $1$ $\Tr \log A = 0$; thus $\log A\in \sl_n(\KK) = \fg$, the space of matrices with trace $0$. This defines a local chart near $1\in G$, showing that $G$ is a manifold. 

Ditto for the other classical groups. The key relationship is:

>[!claim]
>Every classical group $G$ is a Lie group. We have:
>- $\fg = T_1G\subset \gl_n$.
>- If $\uu\subset \gl$ is a small neighborhood of $0$ and $U = \exp(\uu)$ then $\exp$ and $\log$ define mutually inverse diffeomorphisms between $\uu\cap \fg$ and $U\cap G$.