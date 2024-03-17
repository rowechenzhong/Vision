Suppose $X: (\Omega, \FFF, \PP)\to \RR_{\geq 0}$ is a non-negative random variable with $\EE[X] = 1$. Then, one can write a different probability measure on $\FFF$:
$$
\tilde{\PP}(A) = \EE[X\id_A],\qquad  A\in \FFF
$$

>[!idea]
>Observe that this is very different from the [[pushforward measure]], which induces a law on $\RR$ not $\Omega$.

Given $\tilde{\PP}$, this equation determines $[X]$ uniquely, but $[X]$ may not always exist. We say that $\tilde{\PP}$ has ==**density $[X]$ with respect to $\PP$**==.

A ==**probability density function**== is a special case of this. If $f$ is the PDF of a random variable $X: (\Omega, \FFF, \PP)\to (\RR, \BBB, \mu)$, then we would say $\PP\circ X^{-1}$ has density $[f]$ with respect to $\mu$.

Advanced:
- [[Probability Densities and Filtrations]]
- The [[Analysis/Probability/Radon-Nikodym]] generalize this to arbitrary ranges (not deep).
- The [[Analysis/Probability/Radon-Nikodym|Radon-Nikodym Theorem]] characterizes the existence of probability densities.