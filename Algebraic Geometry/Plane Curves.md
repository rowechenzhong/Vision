The projective plane $k\PP^2$ contains rays in $k^3$, $(X,Y,Z)$. We consider loci $C = \{X: f(X) = 0\}$ where $f$ is a homogenous polynomial in $3$ coordinates or **form**.

We discuss low-degree curves (linear, quadratic) which have **parameterizations** $C = H(k\PP)$; in the linear case this looks like $(U,V)\to (U, 0 ,V)$, and in the quadratic case any non-singular (line pair, doubled line, vanishing, etc) plane curve is projectively equivalent ($\GL_k(3)$) to $XZ = Y^2$ and thus parameterized by $(U,V)\to (U^2, UV, V^2)$.

Because of these parameterizations, we quickly obtain the $\min(\deg f, \deg g) \leq 2$ case of ==**Bezout's Theorem**==. In the general form: $k$ is AC; let $C$ be some conic (quadratic plane curve, possibly degenerate) and $D$ be some degree-$d$ plane curve such that $C$ is not a subset of $D$; then $C\cap D$ is exactly $2d$ for a suitable definition of multiplicity.

This is immediate, because by re-parameterization, if $D$ is the zero set of $g$, then $g(U^2, UV, V^2)$ is exactly a degree-$2d$ form, hence has exactly $2d$ roots . Hence by "counting," we obtain the following olympiad geometry results:
1. Suppose I place $n\leq 5$ points in the plane, no $4$ of which are collinear. Then, the space of all $2$-forms vanishing on these points is $6-n$ dimensional.
2. In a pencil (linear interpolation) of conics, there are exactly $3$ degeneracies (with multiplicity), because degeneracy of a conic is exactly degeneracy of the determinant of the $3\times 3$ matrix, which is a $3$-form. If the four common points of the pencil are distinct, then the degeneracies will be the $3$ line pairs.
3. [[Sylvester's Determinant]]