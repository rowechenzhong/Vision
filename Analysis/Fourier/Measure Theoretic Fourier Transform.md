Suppose $\mu$ is a probability measure on $\RR, \BBB_\RR$. The ==**Fourier transform**== or ==**characteristic function**== of $\mu$ is
$$\hat{\mu} = \phi_\mu(t) = \int e^{itx} \der \mu(x)$$
from $\RR\to \CC$.

In particular, if $X$ is a random variable with law $\mu$, then its characteristic function is $\EE[e^{itX}]$. If $X$ also has a probability density $f(x)$, then this guy looks like$$
	 \phi_X(t) = \int e^{itx} f(x)\der x
$$The ==**$L^1$ Fourier Transform**== sends $f$ to $\hat{\mu}$; this can be conceptualized independent of the underlying $X$.

>[!thm] Properties
>This is well-defined and uniformly continuous for all $\RR$, and maps into the closed unit disk $D$.

>[!todo]- What the
> 
> Well, sure; let's show that it is well-defined first. Fix $t$; the function sure looks measurable to me lol. Then, by dominated convergence, this guy lies inside the closed unit disk everywhere. It is continuous in $t$ by the [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]] (use sequential continuity; the limit works).
> 
> We claim that its actually uniformly continuous. To this end, let's pick any $t$ and $\delta$; write
> $$
> \begin{align*}
> 	\abs{\EE[e^{i(t+\delta)X}] - \EE[e^{itX}]} &= \abs{\EE[e^{i(t+\delta)X} - e^{itX}]}\\
> 	&\leq \EE[\abs{e^{i\delta X} - 1}]\\
> 	&\to 0
> \end{align*}
> $$
> Where the limit is independent of the $t$ chosen.

Now, please recall the definition of a [[Convolution]].

>[!claim] Convolutions work
>$\widehat{\mu * \nu}(u) = \hat{\mu}(u)\hat{\nu}(u)$

This is clear; by definition, $\mu * \nu$ is the distribution of $X + Y$, so this is $\EE[e^{itX}e^{itY}] = \EE[e^{itX}]\EE[e^{itY}]$.
# Fourier Things

>[!theorem] Fourier Inversion Formula
>Let $f,\hat{f}\in L^1$. Then, $f(x) = \frac{1}{(2\pi)^d} \int_{\RR^d} \hat{f}(u) e^{-i\braket{u|x}}\der u$.

This is proved in the usual way: take a good kernel consisting of Gaussians.

>[!theorem] Plancherel Identity
>Let $f\in L^1\cap L^2$. Then, $\norm{\hat{f}}_2 = (2\pi)^{d/2}\norm{f}_2$.
>
>There is a unique Hilbert space automorphism (linear operator preserving the inner form) $F$ on $\mathcal{L}^2$ such that
>$$
>	(2\pi)^{d/2}F[f] = [\hat{f}]
>$$
>for all $f\in L^1 \cap L^2(\RR^d)$.

- [[Characteristic Functions and Distributions]]
- [[Characteristic Functions and Weak Convergence]]