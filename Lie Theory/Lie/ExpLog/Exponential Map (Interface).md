This is an [[interface]]. See [[Exponential Map (Construction)]].

>[!theorem] Properties of Exponential Map
> 1. $\exp: \fg\to G$ is a regular map which is a diffeomorphism of a neighborhood of $0\in \fg$ onto a neighborhood of $1\in G$, with $\exp(0) = 1$ and $\exp'(0) = \Id_\fg$.
> 2. For any particular $x\in \fg$, $t\to \exp(tx)$ is a homomorphism of real Lie groups.
> 4. The exponential map commutes with morphisms. For any morphism of Lie groups $\phi:G\to K$ and $x\in T_1G$,
> $$
> 	\phi(\exp(x)) = \exp\left(\phi_*x\right)
> $$
> where $\phi_*$ is the differential of $\phi$ at $1$.
> ^interface

# Problems

See [[Various Adjoint maps]].

>[!problem] Importance of $Ad$
>For all $g\in G$ and $x\in \fg$, $g\exp(x)g^{-1} = \exp(Ad_g x)$.

>[!solution]-
>Consider the map $\phi:G\to G$ via $h\to ghg^{-1}$. Then, by definition, $\phi_* = \Ad_g$, so this is just the previous property.

We can see the bridge being built now; $\fg$ completely describes $G$.

>[!problem]
>Suppose $G$ is a connected Lie group and $\phi:G\to K$ is a morphism of Lie groups. Then, $\phi$ is completely determined by the linear map $\phi_*:T_1G\to T_1K$.

>[!solution]-
>Indeed, $\phi(\exp(x)) = \exp(\phi_*(x))$. We know that $\exp$ is a diffeomorphism $\uu\to \fg$ on some neighborhoods $0\in \uu\subset \fg$ and some $1\in U\subset G$. Thus, $\phi(g)$ is completely specified on $g\in U$ by $\phi_*$.
>
>Because [[Lie Subgroups#^homomorphisms-tight|homomorphisms are tight]], we conclude.