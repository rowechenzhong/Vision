[[Derivations are Lie Algebras]]. Thus, if you consider the vector space of vector fields on $X$, $Vect(X)$ is as well. This is deep; given an action $a:G\times X\to X$,
$$
\begin{align*}
G &&\to &&&\fg\\
a\downarrow && &&&\downarrow a_*\\
X &&\to &&&Vect(X)
\end{align*}
$$
# Induced Action

Let $G$ be a Lie group with lie algebra $\fg$ and $X$ be a manifold with an [[LG + Actions|action]] $a: G\times X\to X$. Then, for any $z\in \fg$, consider the vector field $a_*(z)$ on $X$ via
$$(a_*(z)f)(x) = \frac{d}{dt}\bigg\vert_{t = 0} f(\exp(-tz)x)$$i.e. $a_*(z)$ is the induced vector field.

>[!idea]- Thinking it through
>Like, $a:G\times X\to X$ is a mapping, and we are taking the derivative of this mapping with respect to the $G$-coordinate in the $z$ direction. Like uh, for any $x\in X$, let $a_x: G\to X$ via $a_x(g) = gx$. Then, $a_* = -D(a_\bullet)_1$.

>[!proof]- To be clear
>$$
> \begin{align*}
> 	\underbrace{\frac{d}{dt}\bigg \vert_{t = 0} f(\exp(-tz) x)}_{\in \KK}
> 	&= Df_x \ \underbrace{\frac{d}{dt}\bigg \vert_{t = 0}\left(a_x(\exp(-tz))\right)}_{\in TX_x}\\
> 	&= Df_x \ D(a_x)_1 \ \underbrace{\frac{d}{dt}\bigg \vert_{t = 0} \left(\exp(-tz)\right)}_{\in TG_1}\\
> 	&= -Df_x \ D(a_x)_1 \ z
> \end{align*}
> $$

Why is there a negative sign there? Well, the whole point is that we want to multiply on the left, but multiplication usually goes on the right. What am I waffling about. Let's compute it.

>[!claim] Homomorphism of Lie Algebras
>We have
>$$a_*([z,w]) = [a_*(z), a_*(w)].$$

>[!proof]- Calculus
> I was hoping there was a box I could plug this through, but I'm not smart enough to find it. No matter; the calculus is routine:$$
> \begin{align*}
> 	\lim_{t\to 0} \frac{f(\exp(-t^2[z,w])x) - f(x)}{t^2}
> 	&= \lim_{t^2\to 0} \frac{f(\exp(wt)\exp(zt)\exp(-wt)\exp(-zt)x) - f(x)}{t^2}\\
> 	&= \lim_{t^2\to 0} \frac{f(\exp(-zt)\exp(-wt)x) - f(\exp(-wt)\exp(-zt)x)}{t^2}\\
> 	&= \lim_{t^2\to 0} \frac{f(\exp(-zt)\exp(-wt)x) - f(\exp(-wt)x) - f(\exp(-zt)x) + f(x)}{t^2} - \text{antisymmetric}\\
> 	&= \frac{d}{ds}\bigg\vert_{s=0} \frac{d}{dt}\bigg\vert_{t=0}f(\exp(-zs)\exp(-wt))(x) - \text{antisymmetric}\\
> 	&= a_*(z)a_*(w)f - \text{antisymmetric}\\
> 	&= [a_*(z), a_*(w)]
> \end{align*}
> $$

# Properties

We have linear maps $a_{*x}:\fg \to T_xX$ via $a_{*x}(z) = a_*(z)(x)$.

>[!theorem]
>The stabilizer $G_x$ is a closed subgroup of $G$ with lie algebra $\fg_x = \ker a_{*x}$.
>
>The map $G / G_x$ via $g\mapsto gx$ is an immersion. Thus $Gx$ is an immersed submanifold of $X$, and$$T_x(Gx) \cong \im(a_{*x}) \cong \fg / \fg_x.$$
>
>^action-ker-im

>[!proof]- Main Proof
> 
> First off, $G_x$ is the preimage of closed set $\{x\}$ under a continuous map, thus $G_x$ is automatically closed in $G$. As a stabilizer, it is also automatically a subgroup. However, we didn't show it was a [[Lie Subgroups|lie subgroup]], which needs to be an [[Immersed Submanifold]]. It suffices to exhibit a neighborhood $U$ of $1\in G$ such that $U\cap G_x$ is a closed submanifold of $U$ with $T_1(U\cap G_x) = \fg_x$.
> 
> $\fg_x$ is a Lie ideal because its a kernel of a lie algebra homomorphism.
> 
>>[!claim] Claim
>>If $z\in \fg_x$, $\exp(tz)\in G_x$.
>
>>[!proof]-
>>For any $z\in \fg_x$, $\exp(tz)x$ is a solution to $\gamma'(t) = a_{*\gamma(t)}(z)$ with initial condition $\gamma(0) = x$. $\gamma\equiv x$ is a solution, thus $\exp(tz)x = x$.
> 
>Let $\uu$ be a complement of $\fg_x$; $\fg = \fg_x \oplus \uu$. Then $a_{*x}:\uu \to T_xX$ is injective by linear algebra (we took out the kernel). Thus the map $\uu\to X$ via $u\to \exp(u)x$ is injective for small $u$, thus for small $u\in \uu$, $\exp(u) \in \fg_x$ iff $u = 0$.
> 
> However, in a small neighborhood of $1\in G$, all elements can be written $\exp(u)\exp(x)$ with $u \in \uu, x\in \fg$. Thus $\{\exp(tz)\} = G_x$, as desired.
> 
> This immediately shows that $G/G_x: g\to gx$ is an immersion; around $1$, this map $\fg / \fg_x\to T_x X$ is injective as desired. The image is $Gx$, which is thus by definition an [[Immersed Submanifold]] (it is globally injective because $G/G_x$ ensures this set-theoretically). The tangent space follows immediately.