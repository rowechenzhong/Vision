>[!definition] Convolution
>Let $X,Y$ be two independent random variables, and let $Z = X + Y$. These random variables have laws $\LL_X = \mu$ and $\LL_Y = \nu$, and we call $\LL_Z = \mu * \nu = \nu * \mu$. Similarly, the corresponding CDFs $F(x) = \PP(X\geq x)$ and $G(y) = \PP(Y\geq y)$ yield $H(z) = \PP(Z\geq z)$; we write $H = F * G = G * F$.

Explicitly,
$$(F * G)(z) = \int\int \id\{x + y \leq z\} \der \mu(x) \der \nu(y) = \int F(z - y)\der \nu(y)$$
This shows the (obvious) result that $\mu*\nu$ is well-defined, independent of the random variables $X,Y$. If they admit PDFs , then
$$(f*g)(z) = \int_\RR f(z-y)g(y)\der y$$
Considering the [[Fourier Transform]] yields the identity
$$\phi_{\mu * \nu} = \EE\left[e^{it(X + Y)}\right] = \EE\left[e^{itX}\right] \EE\left[e^{itY}\right] = \phi_\mu(t) \phi_\nu (t)$$