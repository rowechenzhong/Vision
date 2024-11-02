---
aliases:
  - premeasure
  - premeasures
  - pre-measures
---
> [!definition] Pre-Measure
> A [[pre-measure]] on an [[measurable space#^algebra|algebra]] or [[semi-algebra]] $\AAA_0$ is a function $\mu_0: \AAA_0 \to [0,\infty]$ such that $\mu_0(\emptyset) = 0$ and $\mu_0$ is countably additive -- if $A_1,\cdots \in \AAA_0$ are disjoint, and $\bigsqcup A_i \in \AAA_0$, then
>
> $$
>  \mu_0\left(\bigsqcup A_i\right) = \sum \mu_0(A_i).
> $$

One way to create a pre-measure is the [[semialgebra extension]].

> [!example] Premeasure bootstrapping
> Suppose $\mu:\AAA_0 \to [0,\infty)$ is a function which is **finitely** additive. If for any sequence $B_n\in \AAA_0$ with $B_n\downarrow \emptyset$, we have $\mu(B_n)\downarrow 0$, then $\mu$ is also countably additive (and is thus a pre-measure).

> [!proof]- Trivial
> Consider some sequence $A_1,\dots\in \AAA_0$ such that $A = \bigsqcup A_i \in \AAA_0$. Then, $B_i = A\setminus \left(\bigsqcup_{i\leq n} A_i\right)\in \AAA_0$. $B_i\downarrow \emptyset$, thus $\mu(B_n)\downarrow 0$, and $\mu\left(\bigsqcup_{i\leq n} A_i\right) = \mu(A) - \mu(B_i) \uparrow \mu(A)$ as desired.