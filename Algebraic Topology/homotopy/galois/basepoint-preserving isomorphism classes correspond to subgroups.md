There is a **bijection** between the set of **basepoint-preserving [[isomorphic covering spaces|isomorphism classes of path-connected covering spaces]]** and the **subgroups of $\pi_1(X, x_0)$**. 
> [!theorem] Galois Correspondence Part 1
 Let $p_1: (\tilde{X}_1,\tilde{x}_1)\to (X,x_0)$ an $p_2: (\tilde{X}_2,\tilde{x}_2)\to (X,x_0)$ be path-connected covering spaces. Then, $p_1$ and $p_2$ are isomorphic iff $$ p_{1*}(\pi_1(\tilde{X}_1, \tilde{x}_1)) = p_{2*}(\pi_1(\tilde{X}_2, \tilde{x}_2)) $$ 

> [!proof] 
 First, the easy direction. If $\tilde{X_1}$ and $\tilde{X_2}$ are literally homeomorphic spaces, then clearly $$ p_{1*}(\pi_1(\tilde{X}_1, \tilde{x}_1)) = p_{2*}(\phi(\pi_1(\tilde{X}_1, \tilde{x}_1))) = p_{2*}(\pi_1(\tilde{X}_2, \tilde{x}_2)) $$ The other direction is by lifting $p_1$ through $p_2$ via Lifting Criterion (!!) and vice-versa.