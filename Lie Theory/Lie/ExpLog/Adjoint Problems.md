> [!problem] Commutative Lie Groups
> If $G$ is commutative, then $[x,y] = 0$ for all $x,y\in \fg$.

>[!solution]-
>Completely obvious by [[Adjoint Coincidence]].

>[!problem] Lie is a functor
>Let $G,H$ be lie groups and $\phi:G\to H$ a morphism of Lie groups. Then, $\phi^*:\fg\to \hh$ preserves the commutator:
>$$
>	\phi^*([x,y]) = [\phi^*(x), \phi^*(y)]
>$$
>
>In particular, for all $g\in G$, $g\in G$, the map $\Ad(g):G\to G$ is a morphism whose differential preserves the commutator:
> $$
> \Ad_G(g)([x,y]) = [\Ad_G(g)(x), \Ad_G(g)(y)]
> $$
>^Lie-functor

>[!solution]-
>We just need to show this for small $(x,y)$, because both sides are bilinear in $x,y$ and we can scale through constants. We already saw that $\phi$ commuted with the exponential map here: [[Exponential Map (Interface)]]. Recall [[How to invert the commutator]]. Observe that
>$$
>\begin{align*}
>	\exp(\phi^*([x,y])) &= \phi(\exp([x,y]))\\
>						&= \phi(\exp(x)\exp(y)\exp(x)^{-1}\exp(y)^{-1})\\
>						&= \exp(\phi^*(x))\exp(\phi^*(y))\exp^{-1}(\phi^*(x))\exp^{-1}(\phi^*(y))\\
>						&= \exp\left([\phi^*(x), \phi^*(y)]\right)
>\end{align*}
>$$
>and $\exp$ is a diffeomorphism for small $\hh$.