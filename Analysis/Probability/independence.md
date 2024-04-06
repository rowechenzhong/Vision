---
aliases:
  - independent
---
>[!definition] Independent
>A set of events $\{A_\alpha: \alpha\in I\}$ are ==**mutually independent**== if for all finite subsets $J\subset I$,
>$$\PP\left(\bigcap_{\alpha \in J} A_\alpha \right) = \prod_{\alpha\in J} \PP(A_\alpha)$$
>
>Sometimes one also talks about independence of *collections* of events, $\{\mathcal{C}_\alpha, \alpha \in I\}$. In this case, it means that all choices of $A_\alpha\in \mathcal{C}_\alpha$ are independent. In particular, one can talk about independence of $\sigma$-algebras.
>
>If$\abs{I} = 2$, we write $A \pperp B$ and say $A$ and $B$ are ==**independent**==.

>[!defn] Independent RVs
>A set of random variables $\{X_\alpha:\alpha\in I\}$ are ==**mutually independent random variables**== [[Measurable functions generate sigma algebras|if their $\sigma$-algebras]] are independent.

>[!problem]
>For a sequence of real-valued RVs $\{X_n\}_{n\in \NN}$, this is equivalent to
>$$
>	\PP(X_1\leq x_1,\dots X_n\leq x_n) = \PP(X_1\leq x_1)\dots \PP(X_n\leq x_n)
>$$
>for all $n$ and $x_1,\dots, x_n\in \RR$.

>[!idea] Processes
>Such a sequence of RVs is often thought of as a process, where the indices index time. The $\sigma$-algebra $\FFF_n = \sigma(X_1,\dots X_n)$ contains those events that depend solely on $X_1, \dots, X_n$, and represents all historical information about the system at time $n$.

# Key example

> [!example]
> Consider when we have a [[product measure]] $(\Omega, \FFF, \PP)$. Then, one can define $X_\alpha(\omega) = f_\alpha(\omega_\alpha)$, where each random variable is a function of exactly one coordinate.

In this case, our intuition says that these random variables should be independent. Indeed, the pre-image of $B\in \BBB_\RR$ is
$$X^{-1}_\alpha(B) = f^{-1}_\alpha(B)\times \prod_{\gamma\neq \alpha} \Omega_\gamma$$
which has measure $\PP_\alpha(f^{-1}_\alpha(B))$ by construction. Then, finite products look like
$$ \PP_J\left(\prod_\alpha\in J f^{-1}_\alpha(B_\alpha)\right) = \prod_{\alpha \in J} \PP_\alpha\left(f^{-1}_\alpha(B_\alpha)\right)$$
which is also by definition.

It's also intuitively obvious that this is essentially the only possibility. If $\{X_\alpha: \alpha \in I\}$ are RVs, I can write
$$X(\omega) = (X_\alpha(\omega))_{\alpha \in I} \in \RR^I$$
and construct pushforward map $(\Omega, \FFF, \PP) \to \left(\RR^I, \bigotimes_{\alpha\in I} \BBB_\RR, \LL_X\right)$ where $\LL_X = X_\sharp \PP$ as usual. In this case, $X_\alpha$ are independent RVs iff $\LL_X$ is our product measure!

> [!todo] Prove this LOL