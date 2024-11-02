First off, $y^2 = x(x-1)(x-\lambda)$ has no rational parameterization in $\char k\neq 2$ for $\lambda\not\in \{0,1\}$; this is by descent.

By writing a homogenous polynomial in SOS form, we obtain a weak Nullstensatz-form result for degree $\leq 2$. 

This lets us boostrap to degree $3$ (yay!). Here's what we have to say about cubics:
1. Give me $8$ distinct points, no $4$ collinear, no $7$ lying on a non-degenerate conic. The space of cubics passing through all $8$ points has dimension $2$. This gives the ==**Cayley–Bacharach theorem**==; $8$ points will determine the nineth.
2. The **Group Law** is really cool. Pick an irreducible cubic $C$ which doesn't have any cusps or bad things (the tangent line needs to exist uniquely at all points). Pick any origin on the cubic, called $O$. Call the second intersection of $XO$ with $C$, $\bar{X}$. Then, the group law sends $X,Y = \overline{XY\cap C}$ . The proof of associativity in the general case is really awesome and feels like HS projective black magic. The edge cases are waffled by continuity. This is an abelian group.
3. There is a normal form $Y^2 = X^3 + AX^2 + BX + C$; this simplifies the group law.