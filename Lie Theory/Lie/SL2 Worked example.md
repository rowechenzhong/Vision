Let $L = \sl(2,\FF)$. Its standard basis is
$$
	x = \begin{pmatrix}0 & 1\\0 & 0\end{pmatrix},\qquad y = \begin{pmatrix}0 & 0\\1 & 0\end{pmatrix},\qquad h = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}
$$
Then, $[hx] = 2x$, $[hy] = -2y$, and $[xy] = h$. Let $L\curvearrowright V$ be an irreducible module.

$h$ is semisimple, thus $h$ acts diagonally on $V$, because the abstract and usual JD's coincide. Thus we can discuss ==**weight spaces**== $V_\lambda = \{v: hv = \lambda v\}$; if $V_\lambda \neq 0$, $\lambda$ is a ==**weight**==. Clearly $x$ and $y$ lift and lower weights by $2$. The ladder terminates, thus there must exist some $V_\lambda \neq 0$ with $V_{\lambda + 2} = 0$; then any vector in $V_\lambda$ is a ==**maximal vector**== (of weight $\lambda$). Do the usual double-sided annihilation argument.

>[!theorem]
>Let $V$ be an irreducible module for $L$. Let $m + 1 = \dim V$.
>
>Relative to $h$, $V$ is a direct sum of $V_\mu$, where $\mu\in \{m, m-2,\dots, -(m-2), m\}$. Each $V_\mu$ has dimension $1$.
>
>Up to scaling, $V$ has a unique maximal vector, whose weight is $m$.
>
>The action of $L$ on $V$ is then fixed. There exists at most one irreducible $L$-module of each possible dimension $m + 1$ for $m\geq 0$

By applying Weyl's theorem, we have the result for *any* module;

>[!theorem]
>If $L\curvearrowright V$, then the eigenvalues of $V$ are all integers which have multiplicities symmetric about $0$, etc.
>
>Moreover, in any decomposition of $V$, the number of summands is exactly $\dim V_0 + \dim V_1$.