Alright, give me a commutative ring, inclusions. You care about *all* of these.

- Integral Domain. This means that UHHHHHHHHHHHH I have no idea XD OHHHH wait this means that if $xy = 0$, then $x = 0$ or $y = 0$. (Rules out things like $\ZZ/6$). Okay, we only consider ID's from now on, because otherwise common sense doesn't work.
	- $x$ is a ==**divisor**== of $y$ if there exists a $z$ such that $y = xz$; we write $x\mid y$. Note that units divide everything and do not affect divisibility relations. Let the ==**positive elements**== of a ring denote formal equivalence classes modulo units (I just made this term up); then divisibility is a poset (obviously) stratified by positive elements. (These classes might not have representatives that form a multiplicative monoid in general, I think).
	- Note $x\mid y$ iff $yR\subset xR$ in a general ring.
	- Some things work exactly how you expect:
		- $a \mid b$ implies $ac \mid bc$ set theoretically.
	- Other things don't. $\ZZ[\sqrt{-5}]$ where $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 2\cdot 3 = 6$ is my favorite example.
- GCD Domain. This means that UHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH UMMMMMMMMMMMMMM gcds exist. 
	- For all $x,y$, there exists an element $z = \gcd(x,y)$ such that $z\mid x$, $z\mid y$, and any other element $p\mid x$ and $p\mid y$ divides $p\mid z$. Equivalently, LCMs exist, and $xy / z$ works.
	- Equivalently, for all $x,y$, there exists a unique minimal principle ideal $(z)$ such that $(x,y)\subset (z)$. This doesn't have to be saturated though.
	- In a GCD domain, divisibility forms a distributive lattice, so things finally start actually making sense. For instance, here's some trivial facts:
		- $\gcd(ab, ac) = a\gcd(b,c)$.
		- In particular, if $\gcd(b,c) = 1$, then $a = \gcd(ab, ac)$. If, furthermore, $b\mid ac$, then $b\mid a$.
		- In general, if $b\mid ac$, then $b\mid \gcd(b,c)\gcd(a,b)$; this follows immediately.
	- A ==**prime**== $p$ is a non-zero non-unit which is not the product of any pair of non-zero non-units.
	- A ==**prime factorization**== is $z = \prod p_i^{k_i}$ (up to units, we're working with positive elements), $k_i\in \ZZ_{\geq 0}$, $\sum k_i$ finite.
		- These might not exist yet. But in GCDs, such prime factorizations are unique. After all, if prime $p\mid ab$, then $p\mid a$ or $p\mid b$. Uniqueness is because if $\prod p_i^{k_i}$ and $\prod q_i^{\ell_i}$ purport to be different prime factorizations, WLOG they are disjoint by division -- but then everything has to vanish.
	- GCD domains are under $A\to A[x]$.
		- **Gauss' Lemma**: the product of two ==**primitive**== (gcd of all coefficients is $1$) polynomials is primitive. This is a pure grid $\sum_i a_ia_{n-i}$, where you assert $p\mid a_nb_m\implies p\mid a_n \lor p\mid b_m$ repeatedly. This is really deep, because it essentially says the divisibility poset on $A[x]$ splits into an $A$ component and an orthogonal primitive $A[x]$ component.
		- **Main Corollary:** Then, work over the field of fractions $k$, where $k[x]$ is a Euclidean. If $p,q\in A[x]$ are primitive with $p\mid q$ over $k[x]$, then $p\mid q$ over $A[x]$. Indeed, say $pr = q$. Take the GCD of the denominators on $r$ to yield $a$ such that $pr' = qa$, and then factor out a $s\mid r'$ so $r'' = r'/s$ is primitive. We have $pr'' s = qa$. Take the GCD of all elements on each side to yield $s = a$, gg.
		- This is now immediate: for (split into primitive and constant) $ap,bq\in A[x]$, find their GCD $r$ under $k[x]$. WLOG $r\in A[x]$ is primitive, because $A$ are units in $k[x]$; then use $\gcd(a,b)r$. Then, for any (split into primitive and constant) $cs\in A[x]$, if $s\mid p$ and $s\mid q$ in $A[x]$, this also holds in $k[x]$, and thus $s\mid r$ in $k[x]$, but then $s\mid r$ in $A[x]$. Furthermore, by taking GCD of all coefficients in $ap$ and $bq$, we get $c \mid \gcd(a,b)$.
- UFD. This means that every element $z$ exhibits a unique prime factorization. 
	- In a UFD $x\mid y$ iff $k_i \leq \ell_i$ for each $i$. Indeed, if $x\mid y\implies xz = y$, then $k_i + \ell_i = m_i$, else there are two factorizations.
	- All UFDs are GCDs because of this.
	- Existence appears to be trivial, except that you might get an infinite tree. The immediate problem is that some ideals might get generated by infinite chains; $I_1\subset I_2\subset\dots$ might never stabilize.
		- A ring is ==**Noetherian**== if none of these exist; any infinite chain of ideals stabilizes.
		- Noetherianism is not necessary though. A domain is ==**atomic**== if every nonzero nonunit admits a factorization; combined with the GCD condition we win.
	- If you're Noetherian and a GCD, then you're automatically a UFD.
	- UFDs are closed under polynomials; $A$ UFD implies $A[x]$ UFD. **This means that if you start doing algebraic geometry on a field or something, UFDs are as bad as it ever gets**.
		- We're already a GCD, so I just have to find some factorization.
		- We start with (const/prim) $ap\in A[x]$, jump to $k[x]$ which is a UFD and factor $p$; normalize denominators to get a product of primitives plus some constant in $k$, win by Gauss' lemma.
- PID. This means that every ideal is principal.
	- All PIDs are Noetherian UFDs:
		- GCDs are given by intersection of ideals
		- Given $I_1\subset I_2\subset\dots$, their union is an ideal, and thus $(x)$, and thus $x\in I_n$ for some $n$, but then $I_n = (x)$.
	- More importantly, $(x,y) = (\gcd(x,y))$ is saturated, i.e. $\gcd(x,y) = rx + sy$.
- Euclidean Domain. This means you're looking at a mf who smells like a $\ZZ$ or $k[x]$, where division with remainder works.
	- In $k[x]$, division by remainder means that any $a\in R$ and $b\in R_{\neq 0}$ admit at least one quotient and remainder $a = bq + r$ with $r = 0$ or $r$'s degree less than $q$. In $\ZZ$, this is the same, with $r = 0$ or $0\leq \abs{r} < q$.
	- This means that you admit an ==**Euclidean function**== $f:R\setminus \{0\}\to \ZZ_{\geq 0}$.
	- This immediately yields a Bezout-like PID.
- Fields. You know what a field is LOL.