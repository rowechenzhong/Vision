A ==**filtered algebra**== is achieved by $\{0\}\subset F_i\subset F_{i+1}\subset A$ with $A = \bigcup F_i$ such that $F_mF_n\subset F_{n+m}$. For example, $\Cl(V)$ (see [[Clifford Algebra Construction]]) is obviously filtered by asserting $V\subset F_1$, but it's not graded yet.

Given a filtered algebra, we can give it a grading by assigning $G_0 = F_0$, $G_n = F_n / F_{n-1}$, and $\gr A = \bigcup G_i$. We define the maps on $G_n\times G_m\to G_{n+m}$ via $(x + F_{n-1})(y+F_{m-1}) = x\cdot y + F_{n+m-1}$, and extending linearly.

It is clear that $\gr A$ is well-defined, associative (if $A$ is), and unital (if $A$ is, and $1\in F_0$).

Now, obviously $\gr A$ and $A$ are isomorphic as vector spaces. Unfortunately, they are not isomorphic as algebras; this is to be expected because we essentially broke all semidirect to direct sums.