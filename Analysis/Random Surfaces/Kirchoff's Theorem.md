The number of spanning trees of a graph $G$ is the determinant of any cofactor of the [[Laplacian matrix]].
See, the Laplacian matrix has determinant $0$, because $\begin{pmatrix}1\\\vdots\\1\end{pmatrix}$ is in the kernel. But like, consider any complementary subspace; then the Laplacian is a (ostensibly full-rank, in the case that the graph is connected) linear operator on $n-1$-dimensional space.

The number of spanning trees is then $\frac1n \lambda_1\dots \lambda_{n-1}$.