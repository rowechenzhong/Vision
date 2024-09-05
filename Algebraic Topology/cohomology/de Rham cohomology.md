For Lie algebra, I really need to cook up a bunch of waffles quickly. So I'll bypass a structured understanding of cohomology theory in favor of practical computability.

# de Dham Complex

The ==**de Rham complex**== consists of $\Omega^i(M)$, the space of smooth complex-valued differential $i$-forms on $M$. The natural differential $d: \Omega^i\to \Omega^{i+1}$ yields a chain complex because $d^2 = 0$. The $i$-th ==**de Rham cohomology**== of $M$ is the quotient $\ker d / \im d$, the ==**closed**== forms (cocycles) mod the ==**exact**== forms (coboundaries).

If $M$ is compact, then $H^i(M,\CC)$ are finite dimensional. Nice. Then we define the ==**Betti numbers**==, which are their dimensions: $b_i(M) = \dim H^i(M,\CC)$.

>[!example] $b_0(M)$ is the number of connected components.

By the way, by [[Cartan's Magic Formula]], Lie derivatives map closed forms to exact forms, and thus annihilate your cohomology groups.

# Algebra Structure

The cup product of cohomology has a particularly nice form (bruh) when working over differential forms: it's just the wedge product we know and love. Hence $H^\bullet(M, \CC)$ is a graded-commutative associative $\CC$-algebra. Notably, any diffeomorphism $f:M\to N$ preserves the wedge product under pullback; $f^*$ is a graded algebra homomorphism. It's nice how everything works out like that.

# Lie Group things

See [[Chevalley-Eilenberg Complex]]!