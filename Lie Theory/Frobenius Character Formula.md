>[!theorem] Frobenius Character Formula
>The character value of $\chi_\lambda(\sigma)$ is the coefficient of $x_1^{\lambda_1 + N - 1}\dots x_N^{\lambda_N}$ in the polynomial
>$$\prod_{i < j}(x_i - x_j) \cdot \prod_i (x^i_1+\dots x^i_n)^{m_i}$$
# Proof

>[!idea]- Weyl Character Formula
>$$\chi_\lambda = \frac{\sum_{w\in W} (-1)^{\ell(w)}e^{w(\lambda + \rho)}}{\Delta},\qquad \Delta = \sum_{w\in W}(-1)^{\ell(w)} e^{w\rho}.$$

By the [[Weyl Character Formula]], the characters of the representations of $\GL_n$ are given by$$s_\lambda(x_1,\dots, x_n) = \frac{\sum_{s\in S_n} \det(s) x^{\lambda_1 + N - 1}_{s(1)}\dots x^{\lambda_n}_{s(n)}}{\prod_{i < j} (x_i - x_j)} = \frac{\det(x_i^{\lambda_j + N - j})}{\prod_{i < j}(x_i - x_j)}$$We call $s_\lambda$ a ==**Schur Polynomial**==.

> [!idea] Why?
> The Weyl group of $\sl_n$ is $S_n$, and the length $\ell(w)$ of an element just describes the minimum number of adjacent transpositions necessary to create $w$, whose parity is obviously its sign. What does $e^{w(\lambda + \rho)}(x_1,\dots, x_n)$ mean. Well, $x_1,\dots, x_n$ are actually supposed to be lie algebra elements. This by definition should act as $x_i^{w(\lambda + \rho)_i}$, which is $x_1^{\lambda_{w(i)} + \lambda_{w(i)}}$. But you can just invert the permutation, so we're fine.

>[!example] $S^mV$
>$$s_{(m)}(x_1,\dots, x_n) = \sum_{1\leq j_1\leq\dots\leq j_m\leq n} x_{j_1}\dots x_{j_m} = h_m(x_1,\dots,x_n)$$where $h_m$ is the $m$-th ==**complete symmetric function.**==

>[!example] $\wedge^mV$
>$$s_{(1,\dots,1)}(x_1,\dots, x_n) = \sum_{1< j_1<\dots< j_m< n} x_{j_1}\dots x_{j_m} = e_m(x_1,\dots,x_n)$$where $e_m$ is the $m$-th ==**elementary symmetric function.**==

Consider the element $x\otimes \sigma\in \End(V^{\otimes N})$, where $x = \diag(x_1,\dots, x_n)\in \End(V)$ and $\sigma\in S_N$ is a permutation (this acts by applying $x$ to each $V$, then permuting the $V$'s with $\sigma$). Suppose $\sigma$ has $m_i$ cycles of length $i$. Then,$$\Tr\big\vert_{V^{\otimes N}} (x\otimes \sigma) = \prod_i(x^i_1+\dots+x^i_n)^{m_i}.$$(This is literally by definition of trace). On the other hand, using Schur-Weyl duality, we have big brain decomposition go$$\Tr\big\vert_{V^{\otimes N}} (x\otimes \sigma) =  \sum_\lambda \chi_\lambda(\sigma) s_\lambda(x)$$where $\chi_\lambda(\rho) = \Tr\big\vert_{\pi_\lambda}(\sigma)$ is the character of $\pi_\lambda$ in $S_N$. Equating, multiplying by $\prod_{i < j}$, and extracting coefficients, we obtain the theorem.