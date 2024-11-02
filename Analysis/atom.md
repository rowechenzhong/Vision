---
aliases:
  - atoms
---
Given measure space $(X,\Sigma, \mu)$, $A\in \Sigma$ is an ==**atom**== if $\mu(A) > 0$ and for all measurable $B\subset A$, $\mu(B)\in \{0,\mu(A)\}$. A measure is ==**non-atomic**== if there are no atoms.

In the case of a measure on $\RR$, if $A$ is an atom, then by repeatedly partitioning we obtain an $a\in A\subset \RR$ such that $\mu(\{a\}) > 0$. Thus, a measure is non-atomic iff there are no $a\in \RR$ such that $\mu(\{a\}) > 0$.