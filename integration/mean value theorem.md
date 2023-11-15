> [!theorem]
> Suppose $F$ is a function with a continuous derivative $f$. For any $a < b$, there exists a point $x\in (a,b)$ such that $f(x) = \frac{F(b) - F(a)}{b-a}$.

> [!claim]- Stupid lemma
> If $f'(x) > 0$ at $x$, then there is a neighborhood of $f$ which is increasing.

> [!proof]-
> Indeed, suppose $f'(x) > \eps > 0$. Then, by definition of the derivative, there exists a $\delta$ such that for all $\abs{x' - x} < \delta$ with $x' \neq x$, $\frac{f(x') - f(x)}{x' - x} > \eps - \delta > 0$. This suffices.

> [!proof]- Main Proof (Not deep)
> This is pretty clear. Consider the function $f - \frac{F(b) - F(a)}{b - a}(x-a) + F(a)$; we can assume $F(a) = F(b) = 0$.
> 
> Suppose for sake of contradiction that $f'(x)\neq 0$ for all $x\in (a,b)$. If $f'(x) > 0$ for all $x \in (a,b)$, then $f$ is increasing on $(a,b)$, contradiction. Thus, there exist points $a < \ell < r < b$ such that $\sgn f(\ell)\neq \sgn(f(r))$. By the [[Intermediate Value Theorem]], we conclude.