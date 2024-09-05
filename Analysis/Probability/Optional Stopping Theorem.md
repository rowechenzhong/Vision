---
aliases:
  - OST
  - BOST
---
Here is a basically trivial result:

>[!theorem] Bounded Optional Stopping Theorem
> Let $X$ be an adapted integrable [[Discrete-Time Random Process|process]].
> 
> The following are equivalent:
> 1. $X$ is a [[Discrete-time Martingale|supermartingale]].
> 2. For all bounded [[Stopping Time|stopping times]] $T$, and all stopping times $S$,
>    $$\EE[X_T | \FFF_S] \leq X_{S\land T}.$$
> 3. For all stopping times $T$, $X^T$ is a supermartingale.
> 4. For all bounded stopping times $S$ and $T$ with $S\leq T$,
>     $$\EE[X_T]\leq \EE[X_S].$$

We usually look at $(1) \implies (4)$. For submartingales, $\EE[X_T]\geq \EE[X_S]$, and for martingales $\EE[X_T] = \EE[X_0]$.

Here is a slightly more advanced upgrade, accessible after reading [[Martingale Convergence Theorems]].

> [!theorem] Optional Stopping Theorem
> Suppose $X$ is a UI martingale. Then it admits an AS and $L^1$ limit, and thus $X_\infty$ is defined everywhere. For **any** stopping times $S,T$, we have $\EE(X_T) = \EE(X_0)$ and
> $$\EE(X_T | \FFF_S) = X_{S\land T}$$

# Proofs

> [!proof]- (1) $\implies$ (2) \[not bad\]
> If $X$ is a supermartingale, $S\geq 0$ and $T\leq n$, then
> $$X_T = X_{S\land T} + \sum_{k = 0}^n (X_{k+1} - X_k)\id_{S\leq k < T}$$
> This is not deep, its just literally true.
> 
> Both $\{S\leq k\}$ and $\{T > k\}$ are in $\FFF_k$ (you always know if you've stopped in $S$ but not $T$). Pick some $A\in \FFF_S$. Then, $B = A\cap \{S\leq k\}\in \FFF_k$ too (by definition of $\FFF_S$). Thus,
> $$\EE[(X_{k+1} - X_{k})\id_{S\leq k < T}\id_A] \leq 0$$
> >[!idea]- Computing this guy, because I'm slow.
> >Recall that by definition, $\EE[X | \FFF]$ is a $\FFF$-measurable random variable such that $\EE[\EE[X|\FFF] \id_A] = >\EE[X \id_A]$ for all $A\in \FFF$. Thus,
>> $$
>> \EE[(X_{k+1} - X_k)\id_B] \leq \EE\big[(X_{k+1} - \EE[X_{k+1}|\FFF_k])\id_B] = 0
>> $$
> 
> So, if we take our summation, multiply it by $\id_A$, and take the expectation, we get
> $$\EE[X_T\id_A] \leq \EE[X_{S\land T}\id_A]$$
> This implies $(2)$.
> 
>> [!idea]- Why?
>> Recall that $f\leq g$ almost everywhere means $\{\omega: f(\omega) > g(\omega)\}$ has measure $0$. This guy is a priori measurable. In our case, let it be $A$. Then,
>> $$
>> \EE[X_T\id_A]  = \EE[\EE[X_T|\FFF_S]\id_A] > \EE[X_{S\land T}\id_A]
>> $$
>> contradiction.

> [!proof]- (2) $\implies$ (3) \[obvious\]
> Give me some stopping time $T$. Then, $T\land n+1$ is another stopping time, and $S = n$ is a stopping time. Note $n\land (T\land n+1) = T\land n$. Thus,
> $$
> \EE[X_{T\land n+1} | \FFF_n] \leq X_{T\land n}
> $$
> as desired.

> [!proof]- (2) $\implies$ (4) \[obvious\]
> Our theorem reads
> $$\EE[X_T | \FFF_S] \leq X_S$$
> and we can take the global expectation of both sides.

> [!proof]- (3) $\implies$ (1) \[blindingly obvious\]
> Take $T = \infty$.

> [!proof]- (4) $\implies$ (1) \[cute!\]
> Fix some $n$. We wish to show that for all $A\in \FFF_n$,
> $$\EE[X_{n+1} \id_A] \leq \EE[X_n \id_A]$$
> You can do this by letting $S = \id_A\cdot n + \id_{A^c}\cdot (n+1)$, and $T = n+1$. This way, our expression reads
> $$\EE[X_{n+1}] \leq \EE[X_S] = \EE[\id_A X_n + \id_{A^c} X_{n+1}]$$
> as desired.

> [!proof]- Optional Stopping Theorem
> I mean, we're almost there already. By BOST
> $$
> 	\EE[X_{T\land n} | \FFF_S]  =X_{S\land T\land n}
> $$
> Thus, we just need to show things converge properly. We know $X^{S\land T}_n\to X_{S\land T}$ AS and $X^T_n\to X_T$ AS already, but this isn't enough to show the LHS converges; we need $L^1$ strength.
> 
> Well, it would suffice to show $X^T_n$ were UI. This is true, because BOST says $$X_{T\land n} = \EE[X_n | \FFF_{T\land n}] = \EE[X_\infty | \FFF_{T\land n}].$$ and [[Conditional Expectations are UI]]. So we're done.