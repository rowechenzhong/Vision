
The purpose of this little document is to prove some foundational results about $L^p$ spaces, which are one massive class of Banach spaces. Results from both [[Measure Theory]] and [[Functional Analysis]] will be used.

# Definitions 


> [!definition] $L^p$ Norm
 Let $E$ be a measure space; let $f: E \to \CC$ be a measurable function. For any $1\leq p < \infty$, we define $$ \norm{f}_p = \left( \int_E \abs{f}^p \right)^{1/p} $$ If $p = \infty$, we define $$ \norm{f}_\infty = \inf \{ M \in \RR : \mu(\abs{f(x)} < M) = 0\} $$ 

 For bounded continuous functions, $\norm{f}_\infty$ is the usual sup norm. 
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

 By littlewood's first principle \todo{Go prove this at some point, it's written in your notebook} and dominated convergence principle, we conclude that $L^p([a,b])$ is a Banach space, and can be thought of as a ==**completion**== of the continuous functions. \end{document} 









