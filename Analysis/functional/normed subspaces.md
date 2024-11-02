We're going to continue figuring out how topology interacts with linear algebra. 

Given a ==**subspace**== as in linear algebra, the topology on this subspace is the usual subspace topology, which is the coarsest topology that makes the inclusion map continuous. Equivalently, intersect all open sets with the subspace. Equivalently, we inherit the metric from the ambient space. 

> [!problem] Did you forget topology?
A subspace $W$ of $B$ is Banach iff it is closed. 

> [!solution]-
Replace the word \"Banach\" with \"complete\" and this is point-set topology. Suppose $W$ is Banach. Consider any sequence of elements $\{w_i\}$ in $W$ that converges in $B$ to $w$. This sequence must be Cauchy (because convergence implies Cauchy). Thus, by completeness of $W$, $w\in W$. Thus, $W$ is sequentially closed, i.e. closed. Suppose $W$ is closed. Then, any Cauchy sequence in $W$ is also a Cauchy sequence in $B$, so it converges in $B$. Since $W$ is closed, this limit is in $W$, so $W$ is complete. 

> [!definition] Quotient by Null vectors
Let $\norm{\bullet}$ be a *seminorm* (not necessarily positive definite) on vanilla vector space $V$. Then, let $W$ be the set of all $v\in V$ such that $\norm{v} = 0$; these are called the ==**null vectors**== of $\norm{\bullet}$. Then, we can define a norm on $V/W$ by $\norm{v+W} = \norm{v}$. 

There are actually three things to verify: 

> [!problem] 
The null vectors form a subspace. 

> [!solution]-
Observe that $\norm{0} = 0$, so $0\in W$. Now, suppose $v,w\in W$. Then, $$ \norm{v+w} \leq \norm{v} + \norm{w} = 0 $$ so $v+w\in W$. Finally, suppose $v\in W$ and $a\in \RR$. Then, $$ \norm{av} = \abs{a}\norm{v} = 0 $$ so $av\in W$. 

> [!problem] 
Our function is well-defined; $\norm{v+W}$ is independent of the choice of $v$. 

> [!solution]-
For any $v\in V$, $w\in W$, $$ \norm{v} - \norm{w} \leq \norm{v + w}\leq \norm{v} + \norm{w} $$ as desired. 

> [!problem] 
The norm on $V/W$ is a norm. 

> [!solution]-
We are clearly **positive semidefinite**; $0 = \norm{v + W} = \norm{v}$. **Homogeneity** and the **triangle inequality** are directly inherited from $V$. 

> [!definition] Quotient by Closed Subspace
Let $V$ be a normed vector space as usual, and let $W$ be a *closed* subspace of $W$. Then, we can define a norm on $V/W$ in the dumbest way possible: $$ \norm{v+W} = \inf_{w\in W} \norm{v+w} $$ 

Let's verify this works; its a little tedious to be honest. 

> [!idea] 
When I saw this, I desperately wanted the \"arginf\" $w$ to be unique, defined, and actually just the projection onto the $W$-subspace, as is the case in a finite-dimensional inner product space. This is complete cap, and is a wake-up call of the level of generality we're at. Don't worry, things should get much better later when we restrict to Hilbert spaces.

>[!problem] Easy part
>Show $\norm{\bullet}$ is positive semidefinite and homogenous.

> [!solution]-
This is clearly well-defined, at least. $\norm{v + W} = 0$ iff $v\in W$, so we're **positive semidefinite**. **Homogeneity** works because one can scale $w\to \alpha w$ and be totally fine.

>[!problem] Triangle Inequality
>Show
>$$ \norm{a + W} + \norm{b + W} \geq \norm{a+b + W} $$ for all $a,b\in V$.

>[!solution]
> $$\begin{align*}\inf_{w\in W} \norm{a + w} + \inf_{w'\in W} \norm{b + w'} & = \inf_{w,w'\in W} \norm{a + w} + \norm{b + w'} \\ & \geq \inf_{w,w'\in W} \norm{a+b + w + w'}       \\ & = \inf_{w\in W} \norm{a+b + w} \end{align*}$$
>
Again, we need to delicately step around the infimums, because we're not sure whether they can be achieved.

\todo{I'm actually not sure if they can be achieved. I should figure that out at some point.} 

> [!theorem] 
Let $W\subset B$ be a closed subspace. Then, $B/W$ is a Banach space. 

> [!proof] 
Suppose the series $\sum_n \norm{v_n + W}$ converges. By definition of $\norm{v_n + W}$, for each $n\in \NN$, I can find a $w_n\in W$ such that $$ \norm{v_n + w_n}\leq \norm{v_n + W} + 2^{-n} $$ (by definition of infimum). This is good, because $\sum_n \norm{v_n + w_n} < \infty$; then because $B$ is Banach, the summation goes through in $B$; there is some $v$ such that $$ v = \sum_n (v_n + w_n) \in B $$ Great; now we just want to show that $v+W = \sum_n (v_n + W)$. Well (and let's be careful here), $$\begin{align*} \lim_{N\to \infty} \norm{v + W - \sum_{n=1}^N (v_n + W)} & = \lim_{N\to \infty} \norm{( v - \sum_{n=1}^N v_n) + W}        \\ & = \lim_{N\to \infty} \norm{\sum_{n=N+1}^\infty (v_n + w_n)} \end{align*}$$
The tail vanishes, so we're done.