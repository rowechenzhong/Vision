>[!definition] SDE
> Let $d, m\in \ZZ_{\geq 1}$. Let $\sigma$ be a locally bounded $\Hom(\RR^d, \RR^m)$-valued function and $b$ be a locally bounded $\RR^d$-valued function. A ==**stochastic differential equation**== is the formal equation
> $$
> E(\sigma, b): \qquad dX_t = \sigma(t, X_t)dB_t + b(t, X_t)dt.
> $$
> Such a SDE $E(\sigma, b)$ is solved by:
> - A filtered complete probability space $(\Omega, \FFF, (\FFF_t)_{t\in [0,\infty]}, \PP)$.
> - An $m$-dimensional BM $B$.
> - An $(\FFF_t)$-adapted path-continuous process $X$ on $\RR^d$ such that$$X_t = X_0 + \int_0^t \sigma(s, X_s)dB_s + \int_0^t b(s, X_s)ds.$$
> 
> If $X_0 = x$ AS, then we say $X$ is a solution of $E_x(\sigma, b)$.

>[!idea]
>It is very important to remember that an SDE does not specify the probability space nor the noise variable. This is analogous to physics modelling; we've been given a process and we can construct all this mathematical stuff however we want, so long as we describe what we see.
>
>But anyways, we'll often say that "$X$ is a solution to $E$" and leave implicit that there is also a suitable space and BM admitting this solution.

>[!definition] Some nice properties:
>Adjectives regarding $E(\sigma,b)$:
>- ==**Weak existence**== means that for every $x$, $E_x(\sigma, b)$ has a solution.
>- ==**Weak existence and weak uniqueness**== if additionally, all solutions to $E_x(\sigma, b)$ have the same law.
>- ==**Pathwise uniqueness**== if, upon fixing $(\Omega, \FFF, (\FFF_t), \PP)$ and $B$, any two solutions $X, X'$ such that $X_0 = X_0'$ AS are indistinguishable.
>
>Adjectives regarding a solution $X$ to $E_x(\sigma, b)$:
>- ==**Strong solution**== if $X$ is adapted wrt the completed canonical filtration of $B$.

Here is the general result, unproved and unused:

>[!theorem] Yamada-Watanabe
>Weak existence and pathwise uniqueness imply weak uniqueness.
>Under these conditions, for any choice of filtered space and BM $B$, there exists for every $x$ a unique strong solution of $E_x(\sigma, b)$.