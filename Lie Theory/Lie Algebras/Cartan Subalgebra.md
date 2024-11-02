---
aliases:
  - strongly regular elements
---
TODO: explain what this is.

# Strongly Regular Elements

> [!example] CSAs of $\sl_n$.
> Choose any diagonal matrix $x\in \fg = \sl_n$ with distinct eigenvalues. Observe a dense subspace of $\sl_n$ is conjugate to such an element. Then, its centralizer $C(x)$, the diagonal matrices, is a Cartan subalgebra, and indeed all Cartan sub-algebras are obtained in this way (as will be clear after this section).

Following this example, we hope that all CSAs of all semi-simple Lie algebras $\fg$ look like centralizers of a generic element. This is true.

>[!definition]
> A ==**regular**== or ==**strongly regular**== element of a Lie algebra is a "generic" element. Explicitly, it is an element for which the dimension of the $0$-geigenspace of $\ad x$ is minimal in $\fg$.

>[!claim]- The set of strongly regular elements in $\fg$ is connected, dense and open in $\fg$.
>This follows from considering the characteristic polynomial $P_x(t)$ of $\ad x$, and waffling about zeros of complex polynomials.

>[!example] $\sl_n$
>In $\sl_n$, no matter what diagonal matrix you take, $\ad x$ will still have a kernel containing all the diagonal matrices. But if two of your diagonal entries are the same, or you have a non-zero geigenspace, you have a much bigger kernel.

This yields the further intuition that the $\inf \dim \ker \ad x = \dim \hh$. This is also true.

TODO: deliver more punchlines on this easy topic