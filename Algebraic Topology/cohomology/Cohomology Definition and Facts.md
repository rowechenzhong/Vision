Recall that the [[Singular Homology|Singular Complex]] counts embeddings of $\Delta^n$ in $X$.$$\dots \to C_{i+1}\stackrel{\pa_{i+1}}\to C_i \to \dots.$$
The singular homologies $H_i(X)$ just count the holes.

We now fix some abelian group $A$. Then, we can talk about dual groups $C_i^* = \Hom(C_i, A)$. This yields the transpose maps $d_{i-1}: C^*_{i-1}\to C^*_i$ effectively reversing all of the arrows, yielding a ==**cochain complex**==. Just to be clear, a cochain complex is literally just a chain complex, except you define the degrees to increase under your ==**codifferentials**==; take all your words and prefix them with ==**co**==. Hence:
- We have ==**cocycles**== $\ker d$ and ==**coboundaries**== $\im d$. 
- We have ==**cohomology groups**== $H^i(X,A) = \ker d / \im d$, and the elements are called ==**cohomology classes**==. If we pick $A$ to be a commutative ring (which you should do unless you're doing something crazy) then $H^i(X,A)$ is an $A$-module.

# Time to Blitz some Facts

- Cohomology is a **contravariant** functor (which should make sense because we reversed all the arrows in our complex). So any $f:X\to Y$ yields a pushforward map $f_*: H(X)\to H(Y)$ which gets pulled back to $H^i(Y)\to H^i(X)$.
	- Homotopic maps induce chain homotopies, so they induce the same homomorphisms on cohomology.
- Mayer-Vietoris and Relative Cohomology still work; we just reverse the arrows.