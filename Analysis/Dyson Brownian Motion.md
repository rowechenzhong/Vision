>[!definition] Dyson Brownian Motion
>Given a Hermitian matrix whose entries are IID Brownian motion, the eigenvalues $\lambda_1 \geq \dots \geq \lambda_n$ satisfy
>$$
>d\lambda_i = dB_i + \sum_{j\neq i} \frac{dt}{\lambda_i - \lambda_j}
>$$

>[!thm] This is non-intersecting BM.
>$\lambda_1,\dots, \lambda_n$ is equal in distribution of $(B_1,\dots, B_n)$ conditioned on them never intersecting.

Define: $h(x) = \PP_x[A]$ is probability of $A$ conditioned on $X_0 = x$.

$P^t(x, dy) \equiv \PP_x\left[X_t\in dy\right]$, hence by Baye's rule, $\tilde{P}^t(x, dy) \equiv \PP_x\left[X_t\in dy | A\right] = \frac{h(y)}{h(x)} P^t(x, dy)$.

>[!claim] Doob's $h$-transform
>Given an SDE $dX_t = \mu(X_t)dt + dB_t$, we have an $h$-transformed matrix with the extra term $\nabla h_c(X_t)$.




>[!definition] Vandermonde Determinant
>For $x\in \RR^n$, $V_n(x) = \prod_{i < j} (x_i - x_j)$.

Then, $$A_c = \{V_n(B_t) \text{ hits $c$ before $0$}\}.$$
Then, let $A = \lim_{c\to \infty} A_c$; claim this is the same as $\{B_i \text{ never intersect}\}$.

>[!todo] What

Main proof:

Starting with $dX_t = dB_t$, the $h_c$-transformed SDE is $d\tilde{X}^i_t = \pa_i h_c(\tilde{X}_t)dt + dB_t$. You literally just compute the derivative of the Vandermonde determinant and its gg.

# Top Eigenvalue is the same as the Airy Process

Make each coordinate Orsen-Uhlenbeck instead.

Now, the stationary distribution is called the Gaussian Unitary Ensemble. $z_{ii}\sim N_k(0,2)$ and $z_{ij}\sim N_\CC(0,1)$.

Interesting things were cooked:
[[Determinantal Point Processes]]
[[Fredholm Determinant]]
[[Tracy-Widom]]
[[Eyhard Mchta]]

Make the graph connected: [[Probability]]