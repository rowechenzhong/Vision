Remember the [[Independent Increments|exponential martingale]]?

> [!claim] Exponential CLM
> Let $M$ be a CLM. For every $\lambda \in \CC$,
> $$\EEE(\lambda M)_t = \exp\left(\lambda M_t - \frac{\lambda^2}{2} \braket{M,M}_t\right)$$
> is a CLM of the form
> $$\EEE(\lambda M)_t = e^{\lambda M_0} + \lambda \int_0^t \EEE(\lambda M)_s dM_s$$

>[!proof]- This is immediate from the [[Ito Formula]].
> Let $F(x,y) = \exp\left(\lambda x - \frac{\lambda^2}{2} y\right)$. Then,$$F(M_t, \braket{M,M}_t) = F(0,0) + \int_0^t \lambda F\left(M_s, \braket{M,M}_s\right) dM_s - \cancel{\int_0^t \frac{\lambda^2}{2} F\left(M_s, \braket{M,M}_s\right) d\braket{M,M}_s} + \cancel{\int_0^t \frac{\lambda^2}{2} F\left(M_s, \braket{M,M}_s\right) d\braket{M,M}_s}$$as desired.

>[!idea]
>For $\lambda \in \RR$ this is clearly a supermartingale! If you can trick $\EEE$ to be bounded, then you might obtain a true martingale (such as by taking $\lambda = i$ and seeing if $\braket{M,M}_t$ is bounded AS by a constant)...

You can actually invert this:

>[!claim] Inverting the exponential martingale
>Let $D$ be a CLM taking strictly positive values. Then, there exists a unique CLM $L$ such that $D_t = \exp\left(L_t - \frac12\braket{L,L}_t\right) = \EEE(L)_t$. In fact,$$L_t = \log D_0 + \int_0^t D_s^{-1} dD_s.$$

>[!proof] This is immediate from the [[Ito Formula]].

Most famously used in [[Girsanov's Theorem]]!