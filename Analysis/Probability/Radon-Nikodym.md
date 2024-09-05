---
aliases:
  - Radon-Nikodym Theorem
  - Radon-Nikodym Derivatives
---
> [!definition] Radon-Nikodym Derivative
> Let $\mu$ and $\nu$ be two $\sigma$-finite measures on $(X, \mathcal{F})$. If there exists a measurable function $f: X \to \mathbb{R}$ such that
>
> $$
> \nu(A) = \int_A f d\mu
> $$
>
> for all $A \in \mathcal{F}$, then $f$ is called the ==**Radon-Nikodym derivative**== of $\nu$ with respect to $\mu$, and we write $f = \frac{d\nu}{d\mu}$.

>[!idea]
>Then, it is clear that e.g. $\int_X g d\nu = \int_X gf d\mu$.

> [!theorem] Radon-Nikodym Theorem
> Let $\mu$ and $\nu$ be two $\sigma$-finite measures on $(X, \mathcal{F})$. Then $\nu$ has a Radon-Nikodym derivative with respect to $\mu$ if and only if $\nu(A) = 0$ for all $A \in \mathcal{F}$ such that $\mu(A) = 0$. This derivative is unique $\mu$-AE.

We say that $\nu$ is [[absolutely continuous]] with respect to $\mu$.

It is obvious that this condition is _necessary_. We present a proof of this theorem in the case that $\mathcal{F}$ is countably generated, i.e. there exists a sequence $\{A_n\}_{n=1}^\infty$ such that $\mathcal{F} = \sigma(A_n)$. This is a sufficient condition for the theorem to hold, and it is satisfied in many cases of interest.

> [!proof] Todo