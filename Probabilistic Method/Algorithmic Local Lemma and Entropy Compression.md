>[!definition] Random variable model
>Let $\{x_i : i \in I\}$ be a collection of independent random variables. Let $E_1, \ldots, E_n$ be events where each $E_i$ depends only on the variables indexed by some subset $B_i \subseteq I$ of variables. A canonical dependency graph for the events $E_1, \ldots, E_n$ has vertex set $[n]$ and an edge $ij$ whenever $B_i \cap B_j \neq \emptyset$.

>[!definition] Moser–Tardos "fix-it" Algorithm
>**Input:** a set of variables and events in the random variable model  
>**Output:** an assignment of variables avoiding all bad events
>
>1. Initialize by setting all variables to arbitrary values
>2. While there is some violated event:
>    - Pick an arbitrary violated event and uniformly resample its variables

>[!theorem] Moser and Tardos 2010
>In the "fix-it" algorithm, letting $A_1,\ldots, A_n$ denote the bad events, suppose there are $x_1, \ldots, x_n \in [0,1)$ such that:
>$$
>P(A_i) \leq x_i \prod_{j \in N(i)} (1-x_j) \text{ for all } i \in [n]
>$$
>then for each $i$:
>$$
>\text{E}[\text{number of times that }A_i\text{ is chosen for resampling}] \leq \frac{x_i}{1-x_i}
>$$

This implies that the expected runtime of the algorithm is at most $\sum_{i=1}^n \frac{x_i}{1-x_i}$, which although not polynomial, is very fast for large classes of problems.

>[!idea] Las Vegas vs Monte Carlo
>The Moser–Tardos algorithm is a Las Vegas algorithm, in that it always outputs a correct answer, but its running time is a random variable.
>
>A Monte Carlo algorithm is one that has a deterministic running time, but outputs an incorrect answer with some small probability.

# Proof for $k$-CNFs

Here is a special case. We'll prove a slightly different result in the same spirit as the Moser–Tardos algorithm.

>[!definition] Moser's "fix-it" algorithm for $k$-CNFs
>**Input:** a $k$-CNF $F$
>**Output:** a satisfying assignment
>1. Initialize by setting all variables to arbitrary values;
>2. While there is some violated clause $C$:
>    - fix($C$);
>
>Subroutine fix($C$):
>1. Resample the variables in $C$ uniformly at random;
>2. While there is some violated clause $D$ that shares a variable with $C$:
>    - fix($D$);

>[!theorem] Correctness of Moser's algorithm
>Given a $k$-CNF where every clause shares variables with at most $2^k/8$ other clauses, Moser's algorithm outputs a satisfying assignment with expected running time at most polynomial in the number of variables and clauses.

Of course, for each $C$, we enter fix($C$) from the main loop at most once.

>[!claim]
>Fix the $k$-CNF $F$, as well as a clause $C_0$ and some assignment of variables.
>
>Upon executing fix($C_0$), for any $\ell \geq n$, the probability that there are at least $\ell$ *recursive calls* to fix is at most $2^{-\ell + n + 1}$.

This claim shows the expected number of recursive calls within a single outer call to fix($C_0$) is at most $n + O(1)$, which concludes.

The proof applies entropy compression to show that the sum of the execution trace and final output must be at least $nk$. 