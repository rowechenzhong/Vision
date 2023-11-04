> [!theorem] Change of Variables
> Suppose we have maps $(\Omega, \FFF, \PP) \stackrel{X}{\to} (S, \GGG, \mu) \stackrel{f}{\to} (\RR, \BBB, \nu)$. Let $Y = f\circ X$. In other words, $X$ is a random variable, and $Y = f(X) \in \RR$ is a function of $X$. Suppose $f\geq 0$ or $Y$ is integrable. Then,
> $$ \EE[Y] = \int_S f\der \mu $$
> i.e.
> $$ \int_\Omega f(X(\omega)) \der \PP(\omega) = \int_S f(x) \der( X_\sharp \PP)(x).$$

In particular, one can take $(S, \GGG) = (\RR, \BBB)$ and $f(x) = x$; then
$$ \EE[X] = \int_\RR x \der (X_\sharp \PP)(x)$$
as expected.

# Proof

This is our first major usage of the [[Convergence properties of Lebesgue Integral|convergence theorems]]; we will follow the [[measure theory function scaffold|standard scaffold]].

> [!part]- Indicators
> If $f = \id_E$ with $E$ measurable, then both sides each $\PP(X\in E)$.

> [!part]- Simple Functions
> If $f = \sum_{i=1}^n c_i \id_{E_i}$, we apply linearity to show both sides equal $\sum_{i=1}^n c_i \PP(X\in E_i)$.

> [!part]- Nonnegative Functions
> [[real-valued measurable functions#^sf-approx|One can find]] simple functions $f_n\uparrow f$. Then, by [[Convergence properties of Lebesgue Integral#^Monotone-Convergence|Monotone convergence]], we conclude that both sides are the limit
> $$\lim_{n\to \infty} \int_\Omega f_n(X(\omega)) \der \PP.$$

>[!part]- Absolutely Integrable
>Similarly, [[real-valued measurable functions#^sf-approx|one can find]] simple functions $f_n\to f$ such that $\abs{f_n} < \abs{f}$. Then, by [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]], we conclude that both sides are the limit
> $$\lim_{n\to \infty} \int_\Omega f_n(X(\omega)) \der \PP.$$