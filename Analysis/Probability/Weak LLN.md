---
aliases:
  - WLLN
---
Take [[Stupid LLN]] and smash it until we get what we want.

>[!theorem] Weak Law of Large Numbers
>Let $X, X_k$ be iid random variables such that $f(x) = x\PP\left(\abs{X} \geq x\right)\to 0$ as $x\to \infty$. Then, as $n\to \infty$, $\frac{S_n}{n} - \mu_n \to 0$ in probability, where $\mu_n = \EE\left(X; \abs{X} \leq n\right)$.

>[!proof]- Let's go
>We want to apply [[Stupid LLN#^stupid-lln|Stupid LLN]]. Let the $X_{n,k} = X_k$ and let $b_n = n$; interfacing complete. We copy + paste the conditions:
>1. $$ \sum_{k = 1}^n \PP\left( \abs{X_{n,k}} > b_n\right) = n\PP(\abs{X}\geq n)\to 0$$
> 2. $$ \frac{1}{b_n^2} \sum_{k = 1}^n \EE\left( X^2_{n,k} \id\left\{\abs{X_{n,k}} \leq b_n\right\}\right) = \frac{1}{n} \EE\left(X^2\id\left\{\abs{X}\leq n\right\}\right)$$
>    Let $Y_n = X_n \id\left\{\abs{X}\leq n\right\}$; then this is
>    $$\frac{1}{n}\int_0^{n^2} \PP\left(\abs{Y_n} \geq \sqrt{t}\right)\der t = \frac1n \int_0^n \PP\left(\abs{Y_n} \geq y\right)\cdot 2y\der y$$
>    Upper bound this to $\frac{2}{n}\int_0^n \PP\left(\abs{X}\geq y\right)\cdot y\der y \to 0$ and win.

>[!problem] Easier WLLN
> Let $X, X_k$ be iid with finite mean $\EE[X] = \mu$. Then $\frac{S_n}{n}\to \mu$ in probability.

(This easier version is obsolete given [[Strong LLN elementary proof]]).