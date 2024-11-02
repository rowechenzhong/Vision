Let $G$ be a real Lie group, and $\fg = T_1 G$.

The way we're going to do this is via ==**parameterized curves**==.

>[!claim] We can draw geodesics
>Let $x\in \fg$. There is a unique morphism of Lie groups $\gamma_x:\RR\to G$ such that $\gamma'(0) = x$, given by the solution to $\gamma'(t) = \gamma(t)x$.

>[!proof]- Handwave the proof
>By definition of a morphism, we require $\gamma(t + s) = \gamma(t)\gamma(s)$.
>
>Differentiating by $s$ at $s = 0$, we get
>$$
>	\gamma'(t) = \gamma(t)x
>$$
>
>This a solution of the ODE defined by $L_x$ corresponding to $x\in \fg$. It is well-known that this has a solution in a sufficiently small ball around the origin. Specifically, this equation has a unique solution with this initial condition defined on $\abs{t} < \eps$, and it can be shown that $\gamma(t)x = x\gamma(t)$ for $\abs{t} < \eps$. Then, one can observe $\gamma_1(t) = \gamma(s)\gamma(t)$ and $\gamma_2(t) = \gamma(st)$ both satisfy the differential equation under $\gamma_1(0) = \gamma_2(0) = \gamma(s)$, thus $\gamma_1 = \gamma_2$ and we exhibit the homomorphism.
>
>In particular, $x$ is invariant under the adjoint map for all $\gamma(t)$ as expected.)
>
>One lifts this to a solution for arbitrarily large $\abs{t}$ by using the group property.

This map is exactly what we want.

>[!definition] Exponential Map
>The ==**exponential map**== $\exp:\fg\to G$ is defined by $\exp(x) = \gamma_x(1)$.

>[!problem]
>Show that $\gamma_x(t) = \exp(tx)$.
>
>Thus, the flow defined by $R_x$ is given by $g\to \exp(tx)g$, and the flow defined by $L_x$ is given by $g\to g\exp(tx)$.
>
>Also, show that $\exp((s + t)x) = \exp(sx)\exp(tx)$

>[!solution]-
>This is clear. $\gamma_{tx}$ is precisely the solution to $\gamma'(\tau) = \gamma(\tau)tx$, but this solution is simply $\gamma(x) = \rho(tx)$ where $\rho$ solves $\rho'(\tau) = \gamma(\tau)x$.
>
>The stuff about flows is simply a restatement. For $L_x$, $g\exp(tx) = g\gamma_x(t)$, which is the solution to
>$$
>	\gamma'(t) = \gamma(t)x
>$$
>with initial condition $\gamma(0) = g$. Ditto for $R_x$.
>
>The third thing is stupid; this is just $\gamma_x(s + t) = \gamma_x(s)\gamma_x(t)$.

>[!theorem] Properties of Exponential Map
> 1. $\exp: \fg\to G$ is a regular map which is a diffeomorphism of a neighborhood of $0\in \fg$ onto a neighborhood of $1\in G$, with $\exp(0) = 1$ and $\exp'(0) = \Id_\fg$.
> 2. The exponential map commutes with morphisms. For any morphism of Lie groups $\phi:G\to K$ and $x\in T_1G$,
> $$
> 	\phi(\exp(x)) = \exp\left(\phi_*x\right)
> $$
> where $\phi_*$ is the differential of $\phi$ at $1$.
> ^interface

>[!proof]-
>1. The regularity is handwaved. $\gamma_0(t) = 1$, thus $\exp(0) = 1$. $\exp'(0)$ is a map from a vector space so this isn't a differential or anything (although the concepts coincide); we can simply give it a vector $x\in \fg$, and $\exp'(0)v$ should tell us $\frac{\der}{\der t}\exp(tx) = x$. Thus $\exp' = 1$.
>2. Both $\phi(\exp(tx))$ and $\exp(\phi_*(tx))$ satisfy the equation $\gamma'(t) = \gamma(t)\phi_*(x)$. Indeed,
> $$
> 	(\phi(\exp(tx)))' = \left(D_{\exp(tx)}\phi\right)\cdot \exp(tx)\cdot x = \exp(tx)D\phi_1x = \exp(tx)\phi_*x
> $$
> because it's not that deep, and
> $$
> 	(\exp(\phi_*(tx)))' = \exp(\phi_*(tx))\left(\phi_*(tx)\right)' = \exp(\phi_*(tx))\phi_*x
> $$
> because $\phi_*$ is just a linear map.