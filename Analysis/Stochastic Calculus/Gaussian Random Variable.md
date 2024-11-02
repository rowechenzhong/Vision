>[!definition] Mean and Covariance
>A ==**$d$-dimension GRV**== is $X: \Omega\to \RR^d$ such that $\braket{X, u}$ is a GRV for all $u\in \RR^d$.
> 
>Then, there exists a ==**mean**== $\mu = \EE[X]\in \RR^d$ and ==**covariance matrix**== $\sigma = \Cov(XX^\top) = \EE[(X - \EE[X])^\top (X - \EE[X])]$ such that $\EE[\braket{u, X}] = \braket{u, \EE[X]}$ and $\EE[(\braket{u,X} - \braket{u, \EE[X]})(\braket{X,v} - \braket{\EE[X],v})] = \sigma$.

>[!claim] The law of $X$
>The law of $X$ is uniquely determined by $\mu = \EE[X]$ and $\sigma= \Cov(X X^\top)$.

>[!idea] This is not an existence proof.

> [!proof]- Fourier Transform
> $$\underbrace{\varphi_X(\theta)}_{\RR^d\to \CC} = \EE[e^{i\braket{\theta, X}}]$$
> and you can compute the RHS from the definition, because I know that $\braket{\theta, X}$ is a Gaussian with mean $\braket{\theta, \mu}$ and variance $\braket{\theta | \sigma | \theta}$. It is well known that the mapping from laws to characteristic functions is injective.

If $\Sigma$ is positive definite and invertible, then it can be written $\Sigma = A A^\top$, and you can apply $\mu + AZ$ to a standard normal GRV to obtain density$$\frac{1}{(2\pi \det \Sigma)^{1/2}} \exp\left( - \frac12 \left(x - \mu)^\top \Sigma^{-1}(x - \mu)\right)\right).$$If $\Sigma$ is not invertible, then the Gaussian lives in a lower-rank subspace and does not admit a density.

>[!claim] For gaussians, independent $\iff$ uncorrelated.

$\implies$ is trivial. 

>[!claim] The components of a GRV are independent iff $\Sigma$ is diagonal
>^claim-GRV-independent-diagonal