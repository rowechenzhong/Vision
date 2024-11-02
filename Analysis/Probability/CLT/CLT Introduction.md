Everyone knows approximately what the CLT says. Let's run through a few examples to get to the same page.

>[!definition] Normal distribution
>The random variable with density $\phi(x) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{x^2}{2}\right)$ is the ==**Standard Gaussian**==; this is denoted $X\sim N(0,1)$.

>[!example] Normal distributions add
>$S_n = \sum_{i = 1}^n X_i \sim N(0, n)$ is *also* Gaussian. This additive property means that Gaussians are a "fixed point" in the space of distributions under iterated addition. In particular, $\frac{S_n}{\sqrt{n}} = N(0,1)$.

>[!example] Normal tails
>If one calculates $\PP\left(\frac{S_n}{n}\geq \eps\right) = \PP\left(N(0,1)\geq \eps\sqrt{n}\right)$, this is on the order of $\frac{1}{2\pi}\exp\left( \frac{-n\eps^2}{2}\right)$ because Gaussians decay super-exponentially. This integral is in fact $\exp\left(-\frac{n\eps^2}{2} + o(n)\right)$, so we're basically dead on.