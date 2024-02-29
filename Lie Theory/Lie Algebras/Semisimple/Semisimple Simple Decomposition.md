Let $L$ be semisimple. Then, $L = L_1\oplus \dots \oplus L_n$ which are ==**simple**==.
1. Any ideal of $L$ is a direct sum of those simple ideals.
2. Every [[simple ideal]] of $L$ is exactly one of those $L_i$.

>[!idea]
>Basically, $L$ is really really strong. I cannot stress this enough. Everything works.
# Proof

We use the [[Killing Form]] to split $L$. Let $I$ be an arbitrary ideal of $L$. Let $I^\perp = \{x\in L: \kappa(x,I) = 0\}$. This is an ideal, by the associativity of $\kappa$. [[Cartan's Criterion]] says that $I\cap I^\perp$ is solvable. But $L$ was supposed to be [[Semisimple Lie Algebras|semisimple]], so this guy vanishes. Now, we find [[ideals are transitive in semisimple lie algebras]].

Corollaries:
- Let $I$ be some ideal of $L$. $[LI]\subset I$ is a non-empty ideal, because $Z(L) = 0$, thus $[LI] = I$, lol. But this means $I = [L_1I]\oplus\dots [L_nI]$. Consider some $[L_i I]$. This is an ideal of both $L_i$, and is thus either $0$ or $L_i$. We conclude.
- The next statement is clear.