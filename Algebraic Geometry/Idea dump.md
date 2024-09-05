A ==**variety**== is a locus defined by a polynomial equation. $V = \{P\in k^n: f_i(P) = 0\}\subset k^n$. I want to study $V$. What questions do I ask?
1. **Number theory:** If $k = \QQ$, we find ==**Diophantine Problems**== e.g. FLT.
2. **Topology:** if $k = \RR, \CC$, how does $V$ look?
3. **Singularities:** near $P\in V$, how do functions behave? Lol. Vague.

In these next few sections, we will be looking at cases where the dimensions are small and the polynomials are special such that ingenuity can solve problems and provide insight into the structure of the general theory. We will use Smith for the actual theory.

If $U\subset \RR^2$ is open (say), there are many rings of functions $U\to \RR$ which we might care about:
- $C^0$. An in-depth study yields the topological category.
- $C^\infty$. An in-depth study yields the differentiable category, differentiable manifolds, etc.
- Analytic (which is denoted $C^\omega$); this is RA geometry.
- $\RR[X]$ are the polynomials. **In algebraic geometry, we will be focusing on $\RR[X]$**.
Each of these inclusions going up are huge gap in knowledge and theory -- $C^1$ has measure zero in $C^0$, RA functions can be extended to CA functions on a domain and are hence very rigid in contrast to the $\exp(-1/x^2)$ nonsense which works for $C^\infty$, etc.

# Geometry from Polynomials

$\RR[X]$ is a countable dimensional $\RR$-space!! Rational functions keep it countable, and we're nowhere close the richness of $C^\omega$. It is miraculous that a "geometry" can be constructed out of these functions. There are many difficulties involved in setting up this theory.
1. $\forall \eps \exists \delta$ is out the fucking window XD. Commutative algebra takes the place of calculus. See the [[Nullstenllensatz]].
2. It is necessary to work with partially defined functions (??? why is this deep, just restrict a domain, what's the problem) I still don't know what a regular function is oops! We'll see. Regular maps, morphisms, the category, all need to think about this -- shrug. They're only going to define varieties with respect to an ambient space; the correct way is via sheaves. Lol! We'll see that later :)

The perspective of UAG's book is that we won't really care about these details, because almost all algebraic varieties we actually are about are quasiprojective, and our unnatural definitions will be totally fine.

# "Purely algebraically defined"

Every $\RR$ result generalizes immediately to finite fields! This is kind of cool and deep. [[Crash course on Fields]].