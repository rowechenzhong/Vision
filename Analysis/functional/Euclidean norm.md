> [!example] Euclidean Norm
Over $\RR^n$ or $\CC^n$, one can define the ==**Euclidean norm**== for any $1\leq p \leq \infty$ via $$ \norm{x}_p = \left(\sum_{i=1}^n \abs{x_i}^p\right)^{1/p}. $$ If $p = 2$, we recover the usual Euclidean norm. If $p = \infty$, this degenerates to a supremum. 

We should show this is a norm. Scaling and definiteness are trivial. The triangle inequality is given by the following lemma. 

>[!claim] Minkowski's Inequality
>The Euclidean norm satisfies the triangle inequality.
>^minkowski



> [!proof]-
This is a long-winded bit of oly ineq. First off, recall ==**Holder's inequality:**== if $n \in \NN$, $\{a_k\}_{k=1}^n$ and $\{b_k\}_{k=1}^n$ are sequences of complex numbers, and if $1< p < \infty$ and $1/p + 1/q = 1$, then $$ \sum_{k=1}^n \abs{a_k b_k} \leq \left(\sum_{k=1}^n \abs{a_k}^p\right)^{1/p} \left(\sum_{k=1}^n \abs{b_k}^q\right)^{1/q}. $$ Alright great. Now, consider that by the triangle inequality, $$ \sum_{k = 1}^n \abs{a_k + b_k}^p \leq \sum_{k=1}^n \abs{a_k} \abs{a_k + b_k}^{p-1} + \abs{b_k} \abs{a_k + b_k}^{p-1} $$ and by H\"older's inequality, $$ \leq \left(\sum_{k = 1}^n \abs{a_k}^p\right)^{1/p} \left(\sum_{k = 1}^n \abs{a_k + b_k}^p\right)^{\frac{p-1}{p}} + \left(\sum_{k = 1}^n \abs{b_k}^p\right)^{1/p} \left(\sum_{k = 1}^n \abs{a_k + b_k}^p\right)^{\frac{p-1}{p}} $$ which implies ==**Minowski's inequality:**== $$ \left(\sum \abs{a_k + b_k}^p\right)^{1/p}\leq \left(\sum \abs{a_k}^p\right)^{1/p} + \left(\sum \abs{b_k}^p\right)^{1/p}. $$ This is precisely the statement of the triangle inequality for the $\ell^p$ norm over finite sequences.