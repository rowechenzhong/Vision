---
aliases:
  - Signed Measure
  - signed measure
  - FVP
  - IP
  - Increasing Process
---
# Functions with Finite Variation

We consider continuous functions $\RR_+\to \RR$ in the sequel.

>[!definition] Finite signed Measure
>A finite signed measure $\mu$ is just the difference between two finite positive measures, $\mu_+ - \mu_-$, ditto for $\sigma$-finite.

>[!claim] Unique Disjoint Decomposition
>Over $[0,T]$, there exists a unique decomposition of any finite measure $\mu = \mu_+ - \mu_-$ such that $\mu_+$ and $\mu_-$ are supported on disjoint Borel sets $D_+$ and $D_-$.

> [!proof]- Radon-Nikodym kills
> Let $\nu = \mu_1 + \mu_2$. By [[Analysis/Probability/Radon-Nikodym|Radon-Nikodym]], there are two non-negative Borel functions $h_1, h_2$ on $[0,T]$ such that $\mu_1(dt) = h_1(t)\nu(dt)$ and $\mu_2(dt) = h_2(t)\nu(dt)$, thus $\mu(dt) = (h_1(t) - h_2(t))\nu(dt)$ which concludes because $\{h(t) > 0\}$ and $\{h(t) < 0\}$ are disjoint.
> 
> This is obviously unique.

Then, we define $\abs{\mu} = \mu_+ + \mu_-$, and observe $\frac{d\mu}{d\abs{\mu}} = \id_{D_+} - \id_{D_-}$.

>[!definition] FVP
> A continuous function $a:[0,T]\to \RR$ such that $a(0) = 0$ has ==**finite variation**== if there exists a signed measure $\mu$ on $[0,T]$ such that $a(t) = \mu([0,t])$  for $t\in [0,T]$. $\abs{\mu}$ is called the ==**total variation**== of $a$.
> 
> A continuous function $a:\RR_+\to \RR$ has finite variation if all of its restrictions to $[0,T]$ do.

In particular, $\mu$ cannot have [[atom|atoms]]; conversely, any non-atomic $\mu$ yields an FVP. There will not generically be an associated signed measure for $a:\RR_+\to \RR$ because of $\infty - \infty$; however, there is a unique $\sigma$-finite (positive) measure whose restriction is the total variation measure.

>[!idea] Source of confusion
>I managed to convince myself that the measures associated with FVPs were [[absolutely continuous]]. This is false, even though we require that all FVPs are continuous! Notably, any nondecreasing function is an FVP, and there exist continuous nondecreasing functions which are have derivative $0$ almost everywhere, like that cantor set construction.
>
>Thus, *not all FVPs are of the form $a(t) = \int_0^t f(t)dt$ for some measurable $f(t)$*. This is still reasonable intuition to have.
>
>>[!idea]- The mistake I made
>>$t\mapsto \mu([0,t])$ is continuous iff $\mu(\{t\}) = 0$ for all singletons. But the singletons do *not* generate the null sets -- they only encompass countable sets -- and uncountable null sets exist e.g. the dyadics.


# Integration against FVs

>[!definition] Integration against FVs!
> Start with the case of $a:[0,T]\to \RR$. If $f:[0,T]\to \RR$ is integrable under $\abs{\mu}$, we define$$\int_0^T f(s)da(s) = \int_{[0,T]} f(s)\mu(ds),\qquad \int_0^T f(s)\abs{da(s)} = \int_{[0,T]} f(s)\abs{\mu}(ds),$$and one can define $\int_0^t f(s)da(s)$ for $t < T$ in the obvious way. This can be extended to $a:\RR_+\to \RR$ in the obvious way.

In fact, $t\mapsto \int_0^t f(s)da(s)$ is a finite variation process; your signed measure assigns $\int_0^t \id_A f(s)da(s)$ to Borel sets $A$, which can be written $\mu'(ds) = f(s)\mu(ds)$.

>[!claim] Triangle Inequality
>$$\abs{\int_0^T f(s)da(s)}\leq \int_0^T \abs{f(s)} \abs{da(s)}.$$

> [!claim] FVP Integration over continuous functions looks like Reimann Integration
>Pick a mesh.$$\int_0^t\abs{da(s)} = \lim\sum \abs{\Delta a}.$$For any continuous $f:[0,T]\to \RR$,$$\int_0^t f(s)da(s) = \lim\sum f\Delta a.$$ 
> 
>>[!idea]- Expand
>> For any sequence $0 = t_0^n < \dots < t^n_{p_n} = t$ of subdivisions whose [[mesh]] tends to $0$,
>> $$\int_0^t \abs{da(s)}=\lim_{n\to \infty} \sum_{i = 1}^{p_n} \abs{a\left(t_i^n\right) - a\left(t_{i-1}^n\right)}.$$
>> For any continuous $f:[0,T]\to \RR$,$$\int_0^t f(s)da(s)=\lim_{n\to \infty} \sum_{i = 1}^{p_n} f\left(t^n_{i-1}\right)\left(a\left(t_i^n\right) - a\left(t_{i-1}^n\right)\right).$$

# Finite Variation Processes

>[!definition] Finite Variation Process, Increasing Process
>A ==**finite variation process**== is an adapted process whose sample paths have FV on $\RR_+$. A FVP $A$ with nondecreasing sample paths is called an ==**increasing process**==.

Note that any IP admits a limit in $[0,\infty]$, $A_\infty$.

>[!idea]
>One can make extensions to the cases where $A_0\neq 0$ or $A$ is merely cadlag, but we do not do so in the sequel. This book is very nice in that way!

The relation between FVP and IP is not deep. If $A$ is an FVP, then $V_t = \int_0^t \abs{d A_s}$ is IP. Then, $A_t = \frac12\left(V_t + A_t\right) - \frac12\left(V_t - A_t\right)$, so you are FVP iff you are the difference of two IPs.

>[!definition] Integration against FVPs!
>Let $A$ be FVP and let $H$ be progressive. $H$ is ==**integrable wrt $A$**== if$$\forall t \geq 0, \forall \omega \in \Omega, \int_0^t \abs{H_s(\omega)} \abs{dA_s(\omega)} < \infty.$$
>In other words, $H$ is path-integrable wrt $A$ on all $[0,t]$.
>
>Then, the process $H\cdot A$ is defined by
>$$
>	(H\cdot A)_t = \int_0^t H_s dA_s.
>$$

>[!claim] $H\cdot A$ is FVP

>[!example]
>If $A_t = t$ and $H$ is progressive and path-integrable, then $\int_0^t H_s ds$ is a FVP! By taking $H_s$ to be the Radon-Nikodym derivative of the $\mu$ associated with $A_t$ wrt Lebesgue, this should characterize all FVPs.

>[!idea] Obvious extension to a.s. path-integrability
>Suppose $H$ is a.s. path-integrable wrt $A$, say in a.s. event $B$, and **the filtration is complete.** Then, we can make the patch $H'_t(\omega) = H_t(\omega)\id_B$, which is still progressive because $\FFF$ is complete. This lets us define $H\cdot A = H'\cdot A$.

>[!claim] Associativity
>If $H,K$ are progressive and the quantities are defined, then $K\cdot (H\cdot A) = (KH)\cdot A$.