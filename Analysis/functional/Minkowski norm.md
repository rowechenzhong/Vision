Extending the Euclidean norm to this spaces of the form "$\CC^X$" takes a bit of work, because you need to integrate. It's much easier to try $\CC^\NN$. 

> [!example] $\ell^p$ space
For any sequence $\{x_i\}_{i=1}^\infty$ of complex numbers, and for any $1\leq p \leq \infty$, we define the ==**$\ell^p$ norm**== of $x$ to be $$ \norm{a}_p = \left(\sum_{i=1}^\infty \abs{x_i}^p\right)^{1/p}. $$ The ==**$\ell^p$ space**== is the set of all sequences which are bounded in $\ell^p$ norm. 

For instance, $\{1, 1/2, 1/3, \dots\}$ is in $\ell^p$ for all $p > 1$, but *not* in $\ell^1$.

>[!proof]- This is a normed space
Alright, we need to check triangle inequality again. Fortunately, we already have the [[Euclidean norm#^minkowski|Minkowski inequality]] for any finite prefix, and this is just sufficient.

>[!problem]
>Check that if we make the natural $p = \infty$ extension (take the supremum of the sequence instead), we arrive at the [[infinity norm]].