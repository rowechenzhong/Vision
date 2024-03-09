# Metric Space Review

Everything in functional analysis uses really nice topology; everything is a metric space. Thus, we can use "easier" definitions of continuity etc; $\NN$ power is $\RR$ power. Here are some relevant metric space lemmas which should be utterly clear. 

> [!problem] The Metric is Continuous
As a function from $X\times X\to \RR$, the metric $d$ is continuous. 

> [!solution]-
We use sequential continuity. Observe $$ d(x,y) - d(x_i, x) - d(y_i, y)\leq d(x_i, y_i) \leq d(x,y) + d(x_i, x) + d(y_i, y). $$ so we conclude by squeeze theorem. 

In particular, distances commute with limits; $\lim d(x_i, y) = d(x,y)$ for fixed $y$. Next up: whenever I have two metric spaces $X$ and $Y$, I will always assume that $X\times Y$ has the product metric. This is the metric where $$ d((x_1, y_1), (x_2, y_2)) = d_X(x_1, x_2) + d_Y(y_1, y_2). $$ This makes the product of complete spaces complete, for instance.
# Poset Review 

> [!definition] Partial Order
A ==**partial order**== is a relation $\leq$ on a set $X$ such that 
>  
>  
>  
>  -  $x \leq x$ for all $x\in X$. 
>  
>  -  If $x \leq y$ and $y \leq x$, then $x = y$. 
>  
>  -  If $x \leq y$ and $y \leq z$, then $x \leq z$. 
>  
>  If for all $x,y\in X$, either $x \leq y$ or $y \leq x$, then we say that $\leq$ is a ==**total order**==. 


> [!definition] Poset Things
Let $A\subset X$. 
>  
>  
>  
>  -  An ==**upper bound**== of $A$ is an element $x\in X$ such that $a \leq x$ for all $a\in A$. 
>  
>  -  If for all other upper bounds $y$ of $A$, $x \leq y$, then $x$ is a ==**supremum**==. 
>  
>  -  If $x$ is actually in $A$, then $x$ is a ==**maximum**== of $A$. 
>  
>  On the other hand, a ==**maximal**== element of $A$ is an element $x\in A$ such that for all $a\in A$, $x\leq a$ iff $x = a$. All maximums are maximal, but maximal elements are otherwise an unrelated idea. We define ==**lower bound**==, ==**infimum**==, ==**minimum**==, and ==**minimal**== similarly. 

More stupid theorems that should be in my Sys1: 

> [!problem] Infimums Add
If $A, B$ are nonempty subsets of $\RR$, then $\inf_{a\in A, b\in B}( a + b) = \inf A + \inf B$. 

> [!solution]- 
Let $\inf(A+B) = Z$, $\inf A = X$, $\inf B = Y$. We are told that: 
>  
>  
>  
>  -  For all $a \in A, b\in B$, $a + b \geq Z$. However, for all $\eps > 0$, there exist $a\in A, b\in B$ such that $a + b < Z + \eps$. 
>  
>  -  For all $a \in A$, $a \geq X$, and for all $b \in B$, $b \geq Y$. However, for all $\eps > 0$, there exist $a\in A, b\in B$ such that $a < X + \eps$ and $b < Y + \eps$. 
>  
>  Alright. Suppose $X + Y = Z + \eps$ where $\eps > 0$. Then, there exist $a+b < Z + \eps$. This contradicts the fact that $X + Y \leq a + b$. Alternatively, suppose $X + Y + 2\eps =  Z$ where $\eps > 0$. Then, there exist $a < X +\eps$ and $b < Y + \eps$. This contradicts the fact that $a + b \geq Z$. 


> [!problem] Infimums Really Add
If $S_n$ are a bunch of nonempty subsets of $\RR_{\geq 0}$, then $$ \sum_{n = 1}^\infty \inf S_n = \inf \left\{ \sum_{n = 1}^\infty s_n : s_n \in S_n \text{ for all } n\right\} = \inf \sum S_n $$ The sum on the left is guaranteed to converge. 


> [!idea] 
We consider countable sums because uncountable sums of positive real numbers are guaranteed to be infinite.

> [!solution]-
First, we show LHS $\leq$ RHS. Pick all $s_n \in S_n$. Then, $$ \sum_{n = 1}^\infty \inf S_n \leq \sum_{n = 1}^\infty s_n. $$ because it is true termwise, and thus true for all partial sums, and thus true in the limit. Thus the LHS is a lower bound of $\sum S_n$, and thus $\leq$ the infimum. Great! For the other direction, we show $\eps + \text{LHS} \geq \text{RHS}$ for all $\eps > 0$. $$ \eps + \sum_{n = 1}^\infty \inf S_n = \sum_{n = 1}^\infty \inf S_n + \frac{\eps}{2^n} $$ Thus there exist some $s_n \in S_n$ such that $$ \sum_{n = 1}^\infty \inf S_n + \frac{\eps}{2^n} \geq \sum_{n = 1}^\infty s_n\geq \inf \sum S_n $$ win. 


> [!definition] Chain
A ==**chain**== is a totally ordered subset of a poset. 

>[!defn] Zorn's Lemma
>If every chain in a poset $X$ has an upper bound, then $X$ has a maximal element.

This is ==**axiomatic**==, equivalent to the axiom of choice.
# Linear Algebra Review
Before we start putting topologies onto vector spaces, I would like to re-emphasize that all vector space definitions have finite power.
-  Given a set of vectors $S$, the ==**span**== of $S$ consists of **finite** linear combinations of $S$.
-  A set of vectors $S$ is ==**linearly independent**== if every **finite** subset of $S$ is linearly independent. 
-  A ==**Hamel basis**== (what we are used to calling a basis) is a linearly independent and spanning set $S$. 

We ought to show that all vector spaces have a Hamel basis. 

> [!theorem] Hamel Basis
Every vector space has a Hamel basis. 

> [!proof] 
This is a basic application of Zorn's lemma. Let $V$ be a vector space. and let $X$ be the set of all linearly independent subsets of $V$; this is a poset under inclusion. Let $E$ be a chain in $X$. Then, $M = \bigcup E$ is an upper bound of $E$: 
>  
>  
>  
>  -  Any finite subset of $M$ is a subset of some element of $E$, and thus linearly independent. 
>  
>  -  By definition, $M$ includes all elements of $E$. 
>  
>  Thus by Zorn's lemma, we pick a maximal element $S$ of $X$. This must be spanning, else we can concatenate a vector to $S$ to get a larger linearly independent set. 

Cool. Let's move.