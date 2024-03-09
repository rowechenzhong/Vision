The purpose of this little document is to prove some foundational results about $L^p$ spaces, which are one massive class of Banach spaces. Results from both [[Measure Theory]] and [[Functional Analysis]] will be used.

# Definitions 

> [!definition] $L^p$ Norm
> Let $E$ be a measure space; let $f: E \to \CC$ be a measurable function. For any $1\leq p < \infty$, we define $$ \norm{f}_p = \left( \int_E \abs{f}^p \right)^{1/p}. $$ If $p = \infty$, we define $$ \norm{f}_\infty = \inf \{ M \in \RR : \mu(\abs{f(x)} < M) = 0\} $$ 

>[!idea]
>For bounded continuous functions, $\norm{f}_\infty$ is the usual sup norm. 

> [!idea]
> When we're doing probability, we usually want $\RR$ instead of $\CC$; everything still works. I basically don't care about $\CC$ unless we're doing Hilbert things.

>[!idea]- Notation
>If I omit the $p$ subscript, $p = 1$ if we're doing probability and $p = 2$ if we're working in a Hilbert space. I probably don't do this often.

> [!theorem] 
 Holder's inequality and Minkowski's inequality hold for $L^p$ spaces. 
 
> [!definition] $L^p$ Space
 Consider the set of functions $E\to \CC$, modulo measure $0$. The set of all such equivalence classes such that $\norm{f}_p < \infty$ is denoted $L^p(E)$. 

 We ought to show that this is a normed space. 
 
> [!proof]- 
 Note that the norm is well-defined over equivalence classes, because integrals do not change over measure $0$ sets; this also shows we are positive semi-definite. Homogeneity follows from $$ \norm{cf}_p = \left( \int_E \abs{cf}^p \right)^{1/p} = \abs{c} \left( \int_E \abs{f}^p \right)^{1/p} = \abs{c} \norm{f}_p $$ (this also shows closure under scaling.) Triangle inequality follows from Minkowski's inequality (this also shows closure under addition.) 

 Note that by monotone convergence theorem, we can take the definition for $L^p(E)$ where $E\subset \RR$ to be $$ \lim_{n\to \infty} \int_{[-n,n]\cap E} \abs{f}^p < \infty $$ We know that Riemann and Lebesgue integrals agree on $[a,b]$, so this lets us actually compute things. 
 
> [!problem] Lol
 All functions bounded by $\abs{f(x)}\leq C(1 + \abs{x})^{-\alpha}$ for some $C\geq 0$ and $\alpha > 1$ are in $L^p(\RR)$ for all $p\geq 1$. 

>[!theorem]
>$L^p$ spaces are complete.


 %% By littlewood's first principle \todo{Go prove this at some point, it's written in your notebook} and dominated convergence principle, we conclude that $L^p([a,b])$ is a Banach space, and can be thought of as a ==**completion**== of the continuous functions. \end{document} %% 
# Problems

>[!problem] P convergence implies L1 convergence
> Suppose $X_i\to X$ converge in probability, and $\abs{X_i} <C$ for all $i$. Then $X_i\to X$ in $L^1$.

> [!solution]-
> Indeed, pick an $\eps$; I'll find an $N$ such that $\forall M>N\ \mu(\abs{X_i - X}) < \eps$. By convergence in probability, there exists an $N$ such that
> $$\forall M>N\ \mu(\abs{X_i - X} > 0.00001\eps) < 0.00001\eps/C$$
> This finishes, because then
> $$
> 	\mu(\abs{X_i - X})\leq \frac{0.00001\eps}{C}\cdot C + 0.00001\eps < \eps
> $$
# Monotonicity of Lp

>[!problem] Examples
>In general, say, over $\RR$, $L^p(\RR)$ and $L^q(\RR)$ are not contained in one another for $1\leq p < q \leq \infty$. Show this explicitly.

> [!solution]-
> Indeed, let's work on $\RR_{>0}$. Let $f = (x+1)^{-1/p}$. This clearly diverges in $L_p$ but converges in $L_q$.
> 
> If $q <\infty$, on the other hand, consider $f = x^{-1/q}$ for $x < 1$ and $0$ elsewhere. This converges in $L^p$ because $x^{-p/q}$ integrates to $x^{1-p/q} \frac{q}{q-p}$ but explodes near $0$ in $L^q$.
> 
> If $q = \infty$, just let $f = x^{-\frac{0.9}{p}}$; the integral of $x^{-0.9}$ converges near $0$, yet $x^{-0.9/p}$ is unbounded near $0$.

> [!problem] On Probability Measures
> However, if your domain has measure $1$, which we write $L^p(\PP)$, then $L^p(\PP)\supset L^q(\PP)$ for all $1\leq p < q \leq \infty$.
 
> [!solution]-
> Suppose $q\neq \infty$. Applying Jensen to $\abs{x}^{q/p}$ which is convex,
> $$\norm{X}_p = \EE[\abs{X}^p]^{1/p} = c(\EE[\abs{X}^p])^{1/q} \leq (\EE[c(\abs{X}^p)]^{1/q} = \EE[\abs{X}^q]^{1/q} = \norm{X}_q$$
> If $q = \infty$, then $\ess\sup \abs{X} = M < \infty$. Thus $\ess\sup \abs{X}^p = M^p < \infty$.