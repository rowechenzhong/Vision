> [!theorem] Fubini-Tonelli
> Let $(S, \GGG, \lambda)$ and $(T, \HHH, \rho)$ be $\sigma$-finite measure spaces, and define $(\Omega, \FFF, \mu) = (S\times T, \GGG \otimes \HHH, \lambda \times \rho)$. Let $f:(\Omega, \FFF)\to \RR$ be measurable. If $f$ is integrable (**Fubini**) or $f\geq 0$ (**Tonelli**), then
> $$ \int_S \int_T f(x,y) \der \rho(y) \der \lambda(x) = \int_\Omega f\der \mu = \int_T \int_S f(x,y) \der \lambda(x) \der \rho(y).$$

Actually, there's an implicit claim here; if $f(x,y): \Omega\to \RR$ is integrable, then the following are also integrable:
- for all $x\in S$, $f(x,\bullet):T\to \RR$.
- $\int_S f(x, y) \der\lambda(x): T\to \RR$.

Anyways, we follow the [[measure theory function scaffold|standard scaffold]]; this proof works for finite measure spaces.

> [!part]- Indicator functions
> Multiple steps! First, consider when $f(x,y) = \id_{X\times Y}$ where $X,Y$ are measurable. In this case, the conclusion is clear. Next up, by [[box product measure#^cross-sections-measurable|cross section lemma,]] we know that for all $F\in \FFF$, $F_x = \{y\in T: (x,y)\in F\}$ is measurable in $T$. We essentially repeat the same trick: let $\FFF_0$ be the set of all $F\in \FFF$ such that $\rho(F_x)$ is measurable and
> $$\int_S \rho(F_x) d\lambda(x) = \mu(F).$$
> Note that the $\pi$-algebra of rectangles lie in $\FFF_0$. $\FFF_0$ forms a $\lambda$-algebra, because
> - $\Omega\in \FFF_0$ because it is a rectangle.
> - If $F_1, F_2\in \FFF_0$ with $F_1 \supseteq F_2$, then $\rho((E_1\setminus E_2)_x) = \rho(E_{1,x}) - \rho(E_{2,x})$. 
> - If $F_1\cdots \in \FFF_0$ such that $F_i\uparrow F$, then the limit $F$ lies in $\FFF_0$ by continuity from below and monotone convergence theorem.
> [$\pi-\lambda$](pi lambda system) concludes.

> [!part]- Everything else
> The result is true for simple functions by linearity:
> - The desired functions are measurable because they're just sums.
> - Yea everything is just sums
> The result is true for nonnegative functions by [[Convergence properties of Lebesgue Integral#^Monotone-Convergence|Monotone Convergence]] and [[real-valued measurable functions#^sf-approx|approximation by simple functions]], and true for all integrable functions by signage casework.