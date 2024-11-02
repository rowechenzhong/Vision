# For sets

A ==**monotone class**== is a collection of subsets of $\Omega$ which are closed under monotone limits $A_i\uparrow A$ and $A_i\downarrow A$. Take a look at [[pi lambda system|Dynkin's Theorem]], and prove the following results.

>[!problem] Algebra $+$ MC $=\sigma$
>An algebra of sets of $\Omega$ is a $\sigma$-algebra iff it is a monotone class.

(An algebra is closed under finite unions and complements).

>[!solution]-
> $\sigma$-algebra $\implies$ monotone class is trivial. To verify a monotone class algebra is a $\sigma$-algebra we need only verify countable unions. But this is trivial: given $(A_i)_{i\in \NN}$ create $B_i = \bigcup_{j\leq i} A_i$ and apply monotone class.

>[!problem]
>The intersection of an arbitrary family of monotone classes $\{\AAA_i\}_{i\in I}$ is a monotone class.

>[!theorem] Monotone Class Theorem
>For any algebra $\AAA$, the smallest monotone class containing $\AAA$ (that is, the union of all such) is precisely $\sigma(\AAA)$.

>[!problem] Prove this

> [!solution]- Fully analogous to Dynkin. 
> Let $\FFF$ be the union of all monotone classes containing $\AAA$. Show that all of the following are monotone classes containing $\AAA$$$
> \FFF^{(1)} = \{A\in \mathcal{X}: \bar{A}\in \mathcal{X}\},\qquad \FFF^{(2)} = \{A\in \mathcal{X}: A\cup B\in \mathcal{X} \quad \forall B\in \AAA\}
> $$thus $\FFF = \FFF^{(1)} = \FFF^{(2)}$. Then, show$$
> \FFF^{(3)} = \{A\in \mathcal{X}: A\cup B\in \mathcal{X} \quad \forall B\in \mathcal{X}\}
> $$is a monotone class containing $\AAA$, which concludes.

# For Functions

This is the more well-known one.

>[!theorem] Monotone Class Theorem
>Let $(\Omega, \FFF)$ be a measurable space and let $\AAA$ be a $\pi$-system generating $\FFF$. Let $V$ be a vector space of **bounded** functions $f:E\to \RR$ such that:
>- $1\in V$ and $1_A\in V$ for all $A\in \AAA$.
>- For any sequence of **nonnegative** $f_n\in V$, if $f_n\uparrow f$ is also bounded, then $f\in V$.
>
>Then, $V$ contains every bounded measurable function.

See [[approximation by simple functions]].