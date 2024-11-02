---
aliases:
  - Parseval
  - parseval
  - orthonormal basis
---
# Importing Theory 

Alright, this is what we've all been waiting for. It's time to learn how to do quantum physics correctly! For reference, let's restate the definition of the inner product that we know and love. 

> [!definition] Hermitian Inner Product
 Let $V$ be a vector space over $\CC$. An ==**inner product**== is a function $$ \braket{\bullet | \bullet}: V\times V \to \CC $$ such that 
> 
> 
> 
> - ==**Linearity in the second argument**==: For all $v,w\in V$ and $\alpha, \beta \in \CC$, $$ \braket{v | \alpha w + \beta z} = \alpha \braket{v|w} + \beta \braket{v|z} $$ 
> 
> - ==**Conjugate symmetry**==: For all $v,w\in V$, $$ \braket{v|w} = \conj{\braket{w|v}} $$ 
> 
> - ==**Positive definiteness**==: For all $v\in V$, $$ \braket{v|v} \geq 0 $$ and $\braket{v|v} = 0$ if and only if $v=0$. 
> 
> 


> [!definition] Pre-Hilbert Space
 A ==**pre-Hilbert space**== is a vector space $V$ over $\CC$ equipped with an inner product $\braket{\bullet | \bullet}$. The norm on this space is precisely $$ \norm{v} = \sqrt{\braket{v|v}} $$ 

>[!idea] Notation
>From now on, $V$ always denotes a pre-Hilbert space.

From basic linear algebra, we know 

> [!theorem] Cauchy-Schwarz Inequality
 For all $v,w\in V$, $$ \abs{\braket{v|w}} \leq \norm{v}\norm{w} $$ 

 This implies that the norm is actually a norm. All of the foundations from finite-dimensional linear algebra carry over. 
 
> [!theorem] Parallelogram Law
 For all $v,w\in V$, $$ \norm{v+w}^2 + \norm{v-w}^2 = 2\norm{v}^2 + 2\norm{w}^2 $$ 

 In particular: 
 
> [!problem] Continuity of the Inner Product
 Show that the inner product is continuous. 

>[!solution]- Not deep
 Suppose $v_1, v_2,\cdots$ and $w_1, w_2, \cdots$ are sequences in $V$ converging to $v$ and $w$ respectively. Then $$\begin{align*} \abs{\braket{v_n|w_n} - \braket{v|w}} & = \abs{\braket{v_n|w_n} - \braket{v|w_n} + \braket{v|w_n} - \braket{v|w}}     \\ & \leq \abs{\braket{v_n|w_n} - \braket{v|w_n}} + \abs{\braket{v|w_n} - \braket{v|w}} \\ & \leq \norm{v_n - v}\norm{w_n} + \norm{v}\norm{w_n - w} \end{align*}$$ which goes to $0$ as $n\to \infty$. 

Shit, all the old friends are back now. 

> [!definition] Orthogonal
 Two elements $u,v \in V$ are ==**orthogonal**== if $\braket{u |v} = 0$. A subset $S\subset V$ is ==**orthonormal**== if $\braket{u | v} = \delta_{u,v}$ for all $u,v\in S$. 

## Massive Upgrades 

We are go for launch. Let the topology fire. Our first main theorem, a stepping stone for all future work: 
 
> [!theorem] Bessel's Inequality
 Let $S$ be an orthonormal subset of $V$. Then, for all $v\in V$, $$ \sum_{e\in S} \abs{\braket{e | u}} \leq \norm{u}^2 $$ 


> [!idea] 
The definition of a sum of an arbitrary family of non-negative real numbers is the supremum of all sums of finite subsets.

 To give you an idea of just how powerful the inner product is: 

> [!problem] Finite Case
 Show that this is true for finite $S$. No topology required. 

> [!solution]-
 Following our finite-dimensional intuition, let the LHS be $v$ and write $$ 0\leq \norm{u - \sum_n \braket{e_n | u}e_n}^2 = \norm{u}^2 - \norm{\sum_n \braket{e_n | u} e_n}^2 $$ by direct computation. 

The theorem follows by definition, from the finite case. In particular, we are guaranteed to have only countably many nonzero terms. 

> [!definition] Maximal
 An orthonormal subset $S\subset V$ is ==**maximal**== if the only vector $v$ such that $\braket{e | v} = 0$ for all $e\in S$ is $v = 0$. 

> [!theorem] Maximal Orthonormal Subsets Exist
 Every pre-Hilbert space has a maximal orthonormal subset. 

> [!proof]- Textbook Zorn's Lemma.
  Let $\mathcal{C}$ be the set of all orthonormal subsets of $V$. Then $\mathcal{C}$ is partially ordered by inclusion. Let $\mathcal{A}$ be a chain in $\mathcal{C}$. Consider $\bigcup_{A\in \mathcal{A}} A$; this is still orthonormal, because the definition of orthonormal takes things $2$ at a time. So this is an upper bound for $\mathcal{A}$. By Zorn's Lemma, $\mathcal{C}$ has a maximal element. 
> 
> But then, if this maximal element is not an orthonormal basis, there is some $v\in V$ such that $\braket{e | v} = 0$ for all $e\in S$. But then $S\cup \{v\}$ is orthonormal, contradicting the maximality of $S$. 

> [!idea] Do you *see* how nice this is??
> The definition of orthonormal has $2$ $\exists$ quantifiers, no limits involved. Everything works beautifully.

> [!problem] Separable Spaces
 Every ==**separable**== pre-Hilbert space has a countable maximal orthonormal subset.
> ^prob-sep

> [!solution]-
 We already know a subset exists. Suppose it has uncountable cardinality; then by staring at $0.001$-balls around each element, we conclude $V$ is not separable. On the other hand, a constructive proof is via the Gram-Schmidt process. 

## The Apex of Spaces 

> [!definition] Hilbert Space
 A ==**Hilbert Space**== $\HH$ is a pre-Hilbert space that is complete. A ==**separable Hilbert Space**== is a Hilbert Space that is [[separable]]. A countable maximal orthonormal subset of a Hilbert Space is called an ==**orthonormal basis**==. 

>[!idea] Notation
> From now on, $\HH$ denotes a Hilbert Space.

We know one nontrivial example of a separable Hilbert space:

> [!example] $L^2(E)$
 Let $E$ be some measure space. Then $L^2(E)$, the space of measurable functions $f:E\to \CC$ with $\int_E \abs{f}^2 < \infty$ modulo measure $0$, is a Hilbert Space with inner product $$ \braket{f,g} = \int_E f\conj{g} $$ If $E = \NN$, we find $\ell^2$. If $\abs{E} < \infty$, we find the finite-dimensional inner product spaces we know and love. 

>[!idea] [measure theory - When is $L^2(X)$ separable? - MathOverflow](https://mathoverflow.net/questions/42310/when-is-l2x-separable)
>A master chef claims that $L^2(E)$ is separable iff $E$ is a disjoint union of:
>- Countably many points
>- The standard Borel space.

 Over Hilbert spaces, orthonormal bases behave in the nicest way possible:
 
> [!theorem] Fourier-Bessel Series
 Let $S$ be a maximal orthonormal basis for $\HH$. Then, for all $v\in \HH$, $$ v = \sum_{e\in S} \braket{e| v} e$$ where the sum converges in $L^2$-norm. 

 This is sometimes called ==**Parseval's Identity**==.
 
> [!proof]- Very Nice
 By Bessel's inequality, at most countably many $e\in S$ have $\braket{e | v} \neq 0$. This is fortunate, because otherwise the sum has no chance of being defined. Index those $e$ as $e_1, e_2,\cdots \in S$. Then, by Bessel's inequality again, we know that the partial sums $w_k$ form a Cauchy sequence; for any $\eps$, there exists a $K$ such that for all $N, M > K$, $$ \norm{\sum_{n=1}^N \braket{e_n | v} e_n - \sum_{n=1}^M \braket{e_n | v} e_n}^2 = \sum_{n=M+1}^N \braket{e_n | v}^2 < \eps $$ In *Hilbert* spaces, Cauchy sequences converge, thus the partial sums converge to some $w = \lim_{k\to \infty} w_k$. Now, for all $\braket{e | v} = 0$, $\braket{e | v - w_k} = 0$ for all $k$. If $\braket{e_i| v} \neq 0$, then $\braket{e | v - w_k} = 0$ for all $k\geq i$. By continuity of the inner product, $\braket{e | v - w} = 0$ for all $e$! But this means $v - w = 0$, by definition of maximal. 

Thus, we have a partial converse to [[hilbert#^prob-sep|this problem]], which also shows why we like the separability condition:

> [!problem] Hilbert Spaces are Separable
 Every Hilbert space with a countable orthonormal basis is separable. 

> [!solution]-
 Lol, this is kind of silly. Observe that the $a+bi$ for $a,b\in \QQ$ is countable. Then, consider all finite sequences of these $a + bi$. By Fourier-Bessel, this is dense in $\HH$. 

> [!idea] 
Thus, separability and countable orthonormal bases are the same concept in Hilbert spaces. This is really really nice, and coincides with my intuition about quantum physics a la Fock basis etc.

> [!problem] Parseval's Identity
 Let $S$ be a maximal orthonormal subset of $\HH$. Then, for all $v\in \HH$, $$ \norm{v}^2 = \sum_{e\in S} \abs{\braket{e| v}}^2 $$ 

>[!solution]-
 By Bessel, this sum is well-defined and everything. By Fourier-Bessel and continuity of the inner product, we find the answer. 

Finally, a complete characterization of separable Hilbert spaces:

> [!theorem] Everything is $\ell^2$
 Let $\HH$ be a separable infinite-dimensional Hilbert space. Then there exists a bijective bounded linear operator $T: \HH\to \ell^2$ such that for all $u,v\in \HH$, $$ \braket{u| v} = \braket{Tu | Tv} $$ In other words, $\HH$ is ==**isometrically isomorphic**== to $\ell^2$. 

> [!proof]-
 Write down an orthonormal basis $\{e_n\}$ and send $$ (Tu)_n = \braket{e_n | u} $$ This is: 
> 
> - Clearly linear in $u$. 
> - Injective, because if $Tu = 0$, then $\braket{e_n | u} = 0$ for all $n$, thus $u = 0$. 
> - Surjective, because given any $a \in \ell^2$, $$ \norm{a}^2 = \sum_{n=1}^\infty \abs{a_n}^2 < \infty $$ thus $T^{-1}(a)\in \HH$. 
> - Preserves the inner product by construction (and continuity of the inner product blah); this also automatically implies boundedness. 
 
> [!example] Fourier Series
 The subset of functions $$ \frac{1}{\sqrt{2\pi}} e^{inx},\qquad n\in \ZZ $$ is an orthonormal basis of $L^2([-\pi, \pi])$. We will prove these in a subsequent set of notes, because this requires measure theory.