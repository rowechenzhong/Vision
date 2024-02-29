>[!claim]
>Suppose $I\subset L$ is an ideal of semisimple $L$, and $J\subset I$ is an ideal in $I$. Then $J$ is an ideal in $I$.

A priori, this means $[I,L]\subset I$ and $[I,J]\subset J$, but we don't know $[L,J]\subset J$, and there exist counterexamples. [[Semisimple Lie Algebras]] are just too cracked.

However, semisimple says $L = I\oplus I^\perp$ for some $I^\perp$. Thus, for all $x = a + b\in L$ and $j\in J$,
$$[j, x] = [j,a] + [j,b] = [j,a]\in I$$
and we win. We know $[j,b] = 0$ because $[I, I^\perp] = 0$, lol.