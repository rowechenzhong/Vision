---
aliases:
  - GWN
---
>[!definition] Gaussian White Noise
>Let $(E,\GGG)$ be a measurable space. Let $\mu$ be a $\sigma$-finite measure. A ==**Gaussian White Noise**== with ==**intensity**== $\mu$ is an isometry $G$ from $L^2(E,\GGG,\mu)$ into a [[Gaussian Spaces|centered Gaussian space]] $H$:$$\EE[G(f)G(g)] = \int fg d\mu,\qquad f,g\in H\subset L^2(E,\GGG,\mu).$$

>[!example]
>If $f = \id_A$ with $\mu(A) < \infty$, then $G(\id_A)\sim N(0, \mu(A))$. We write $G(A) = G(\id_A)$.
>
>If $A_1,\dots, A_n\in \GGG$ are finite and disjoint, $(G(A_i))_i$ is a Gaussian vector in $\RR^n$ with diagonal covariance matrix.
>
>If $A$ is finite, and a disjoint union of $A_1,A_2,\dots\in \GGG$, then $\id_A = \sum \id_{A_i}$, and $G(A) = \sum G(A_i)$ in $L^2(\Omega, \FFF,\PP)$. (In fact, the partial sums form a martingale, thus the series [[Martingale Convergence Theorems|converges AS]]).

> [!proof]- Construction
> Pick any orthonormal basis $\{f_i: i\in I\}$ of $L^2(E,\GGG,\mu)$, and pick some probability space $(\Omega, \FFF,\PP)$ on which we can construct a collection $(X_i)_{i\in I}$ of independent $N(0,1)$ RVs (see [[Ionescu-Tulcea]]). Then, let
> $$
> G(f) = \sum_{i\in I} \braket{f|f_i} X_i
> $$
> 
>> [!idea]
>> Recall that [[hilbert|Parseval's identity]] holds regardless of whether your Hilbert space is separable. The summation above contains at most countably many nonzero terms, and is thus well-defined.
> 

>[!idea] A Fake Measure
>When we do things like try to construct the [[Weiner Integral]], we will often want to think of $G$ as a sort of measure on $(E,\GGG)$, which takes values in $H$. The above properties show why! Unfortunately, it is *not* true that $G(\bullet)(\omega)$ is a measure, in general. Let us learn the true story.

>[!idea] Confusion point: the GWN for $\mu$ is not necessarily unique!

>[!claim] Extracting the Intensity
>Let $A\in \GGG$ be finite. Suppose there exists a sequence of partitions of $A$, $A = A_1^n\cup\dots\cup A_{k_n}^n$, whose [[mesh]] tends to $0$. Then, the sequence
>$$\lim_{n\to \infty} \sum_{j\leq k_n} G(A^n_j)^2 \stackrel{L^2}{\to} \mu(A).$$

>[!proof]- Second Moment Method
> Please observe that the LHS is a random variable, while the RHS is a constant! For any $n$, $\{G(A_i^n)\}_i$ are independent, and $\EE[G(A_j^n)^2] = \mu(A_j^n)$. Then$$\EE\left[\left(\sum_{j\leq k_n} G(A^n_j)^2 - \mu(A)\right)^2\right] = 2\sum_{j\leq k_n} \mu(A^n_j)^2$$because if $X\sim N(0,\sigma^2)$, $\Var(X^2) = 2\sigma^4$. The RHS vanishes because it is bounded by $\left(\sup_j \mu(A_j^n)\right)\mu(A)$.