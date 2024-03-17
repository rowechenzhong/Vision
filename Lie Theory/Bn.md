---
aliases:
    - B_n
    - so_{2n+1}
    - so2n+1
    - SO2n+1
    - $\SO_{2n+1}$
    - $\so_{2n+1}$
---
This is a [[Simple Lie Algebra Data Page]]

| Lie group                       | Lie algebra  | Root system $\Phi$ | $\abs{\Phi}$ | $\abs{\Delta}$ | $\abs{W}$ |     |     |
| ------------------------------- | ------------ | ------------------ | ------------ | -------------- | --------- | --- | --- |
| $\SO_{2n+1}$ (Or $\Spin(2n+1)$) | $\so_{2n+1}$ | $B_n$              | $2n^2$       | $n$            | $2^nn!$   |     |     |

This consists of matrices which preserve the a fixed positive-definite symmetric inner form on $\CC^{2n+1}$. Euclidean geometry usually presents this as $\sum x_i^2$, which we will call the ==**classical**== or "naive" basis. In the ==**standard**== or "usual" presentation, this form is $\sum_i x_iy_i + z^2$. This is the basis in which the below basis and roots are presented.

$$
\eta = \left(\begin{array}{c | c | c}
1 & 0 & 0 \\
\hline
0 & 0 & I_n \\
\hline
0 & I_n & 0
\end{array}\right)
$$

Let $E = \RR^n$ and $\Phi$ consists of integer vectors of length $\sqrt{2}$ plus all unit vectors. A choice of simple roots is $\alpha_i = e_i - e_{i+1}$ for $1\leq i\leq n - 1$ and $\alpha_n = e_n$.

In the standard presentation, $\so_{2n+1}$ consists of matrices $g$ such that $g\eta + \eta g^\top = 0$
$$
\left(\begin{array}{c | c | c}
0 & u & -w \\
\hline
w & A & B \\
\hline
-u & C & -A^T
\end{array}\right)
$$

where $B,C$ are skew-symmetric; one can check that this agrees with the dimension $2n^2 + n$.

Then, the Cartan subalgebra looks like $A = (x_1,\dots, x_n)$ along the diagonal with $b = c = 0$. The roots are as follows:

$$
e_i - e_j \implies \left(\begin{array}{c | c c | c c}
0 & 0 & 0 & 0 & 0 \\
\hline
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
\hline
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 & 0
\end{array}\right),\qquad
e_i + e_j \implies \left(\begin{array}{c | c c | c c}
0 & 0 & 0 & 0 & 0 \\
\hline
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & -1 & 0 \\
\hline
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{array}\right),\qquad e_i \implies \left(\begin{array}{c | c c | c c}
0 & 0 & 0 & -1 & 0 \\
\hline
1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
\hline
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)
$$

and all of the negatives arise from transposition. (As usual, representative examples are shown with $n = 2$, $i = 1$, and $j = 2$). Observe that the roots $e_i - e_j$ come directly from $\gl_n\subset \so_{2n}$