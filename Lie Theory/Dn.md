---
aliases:
    - D_n
    - so_{2n}
    - so2n
    - SO2n
    - $\SO_{2n}$
    - $\so_{2n}$
---
This is a [[Simple Lie Algebra Data Page]]

| Lie group                   | Lie algebra | Root system $\Phi$ | $\abs{\Phi}$ | $\abs{\Delta}$ | $\abs{W}$   |     |     |
| --------------------------- | ----------- | ------------------ | ------------ | -------------- | ----------- | --- | --- |
| $\SO_{2n}$ (Or $\Spin(2n)$) | $\so_{2n}$  | $D_n$              | $2n(n-1)$    | $n$            | $2^{n-1}n!$ |     |     |

This consists of matrices which preserve the a fixed positive-definite symmetric inner form on $\CC^{2n}$. Euclidean geometry usually presents this as $\sum x_i^2$, which we will call the ==**classical**== or "naive" basis. In the ==**standard**== or "usual" presentation, this form is $\sum_i x_iy_i$; this is the basis in which the below basis and roots are presented.

$$
\eta = \left(\begin{array}{c | c}
0 & I_n \\
\hline
I_n & 0
\end{array}\right)
$$

Let $E = \RR^n$ and $\Phi$ consists of integer vectors of length $\sqrt{2}$. A choice of simple roots is $\alpha_i = e_i - e_{i+1}$ for $1\leq i\leq n - 1$ and $\alpha_n = e_{n-1} + e_n$.

In the standard presentation, $\so_{2n}$ consists of matrices

$$
\left(\begin{array}{c | c}
A & B \\
\hline
C & -A^T
\end{array}\right)
$$

where $B,C$ are skew-symmetric; one can check that this agrees with the dimension $2n^2 - n$.

Then, the Cartan subalgebra looks like $A = (x_1,\dots, x_n)$ along the diagonal with $b = c = 0$. The roots are as follows:

$$
e_i - e_j \implies \left(\begin{array}{c c | c c}
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 \\
\hline
0 & 0 & 0 & 0 \\
0 & 0 & -1 & 0
\end{array}\right),\qquad
e_i + e_j \implies \left(\begin{array}{c c | c c}
0 & 0 & 0 & 1 \\
0 & 0 & -1 & 0 \\
\hline
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right),\qquad
- e_i - e_j \implies \left(\begin{array}{c c | c c}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
\hline
0 & 1 & 0 & 0 \\
-1 & 0 & 0 & 0
\end{array}\right)
$$

(As usual, representative examples are shown with $n = 2$, $i = 1$, and $j = 2$). Observe that the roots $e_i - e_j$ come directly from $\gl_n\subset \so_{2n}$.