Wow, this page is going to be massive.

# Measure Theory
## Probability
Suppose $\mu$ is a probability measure on $\RR, \BBB_\RR$. The ==**Fourier transform**== or ==**characteristic function**== of $\mu$ is
$$\phi_\mu(t) = \int e^{itx} \der \mu(x)$$
from $\RR\to \CC$. If $X$ is a random variable with law $\mu$, then its characteristic function is $\EE[e^{itx}]$.

>[!idea] Properties
>This is well-defined for all $t\in \RR$ because of [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]]. Interestingly, this is also continuous in $t$; it is sequentially continuous by dominated convergence again. 

