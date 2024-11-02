Let's spend an afternoon discussing a collection of problems.

Let $I$ be a set of agents and $H$ be a finite set of houses, where $\abs{I} = \abs{H}$. Our goal is to find a bijection $\mu: I\to H$.

Let $\succ$ be a list of preferences over the houses, an element of $\Pi^I$ where $\Pi$ is all permutations (strict preferences) on $H$; this completes a ==**housing allocation problem**== $(I, H, \succ)$. There is then the natural induced notion of Pareto efficiency.

> [!idea]- Pareto Efficiency
> To spell it out, $\mu$ ==**Pareto dominates**== $\nu$ if $\mu(i) \succeq \nu(i)$ for all $i\in I$, and there exists $i$ such that $\mu(i) \succ \nu(i)$ for some $i$.
> 
> $\mu$ is ==**Pareto Efficient**== if it is maximal in this poset on $\Pi^I$.

There are generally multiple Pareto efficient matchings, so we should place some more restrictions on this problem to yield a deterministic solution. Enter the Housing Market!
# Housing Markets - Core

Suppose each agent is given an initial endowment $h: I\to H$, which the agents own; this completes a ==**housing market**== $(I, H, \succ, h)$. Then, one can define natural concepts of "optimality resistant to collusion;"

> [!definition] Core Matching
> $\eta$ is in the ==**core**== of the housing market $(I, H, \succ, h)$ if there is no coalition $T\subset I$ which can defect obtaining a strictly better allocation for themselves.
> 
>> [!idea]- Coalition
>> There should not exist $T\subset I$ and matching $\nu$ such that $\nu(I) = h(I)$, $\nu(i)\succeq_i h(i)$ for all $i\in T$, and $\nu(i)\succ \eta(i)$ for some $i\in T$
### Gale's TTC

> [!definition] Gale's TTC
> Initially, no house or agent is assigned.
> While there still exist unassigned agents:
> 1. Draw the directed graph with unassigned agents as vertices, each pointing to their top choice among all currently unassigned houses.
> 2. There exists at least one cycle. Choose any cycle and implement its allocation.
>    
>We generally denote the $k$-th cycle chosen as $C_k$, and write $C(i) = k$ for $i\in I$ if $i\in C_k$.

>[!theorem] Gale's TTC
>There is exactly one matching $\eta(h)$ in the core, which can be constructed by Gale's Top Trading Cycles algorithm.

Gale's TTC is in the Core because it is "greedily" so. This construction will become our foundation for thinking about the Core.

> [!proof]- Gale's TTC produces a matching in the Core
> Consider any smallest coalition $T$ (all coalitions are non-trivial, because there exists an element of the coalition which strictly benefits). Let $k = \arg\min_{i\in T} C(i)$. If $C_k\subset T$, then $T\setminus C_k$ is still a coalition, hence $C_k\not\subset T$. Hence there exists some $i\in C_k$ such that the top choice of $i$ in $C_k$ does not lie in $T$, contradiction.

There are steps in Gale's algorithm where we may select one of many cycles. These decisions all "commute," intuitively because a cycle is immutable once it is created; it cannot be altered by outside agents. To actually prove this, we just cite optimality.

> [!proof]- There are no other matchings in the Core
> Consider some other matching $\nu$. Let $S = \{i: \nu(i)\neq \eta(i)\}\subset I$. Let $i = \arg\min_{i\in S} C(i)$ and $k = C(i)$. Then, $C_k$ is a coalition.

>[!idea]- Competitive Equilibrium (Unimportant)
> We now give a non-Pareto definition of optimality, given an initial endowment.
> 
>>[!definition] Competitive Equilibrium
>>A matching $\mu$ and price vector $p$ form a ==**competitive equilibrium**== $(\mu, p)$ if for all $i\in I$, $\mu(i) = \sup_{\succ_i}\left\{j\in H: p_j \leq p_{h(i)}\right\}$.
>>
>>We say a matching $\mu$ is a competitive equilibrium if there exists any price vector $p\in \RR^n$ which makes $(\mu, p)$ a CE.
> 
> Gale's TTC is blithely obviously CE (proof left to the reader).

### Strategy-Proofness

Core, as a direct mechanism, is strategy-proof. This is readily seen, and the proof is left to the reader.

A mechanism is ==**individually rational**== if there do not exist any coalitions of size $1$.

>[!theorem] Ma 1994
>Core is the *only* mechanism which is PE, IR, and SP.

The intuition:
- Core is strategy proof because all houses ranked above $\nu(i)$ are completely in-accessible to $i$ through deviation.
- Conversely, if a mechanism does not assign $\nu(i)$ to $i$, $i$ can loudly complain by deviating to assign their starting allocation a utility which is immediately below $\nu(i)$, and then claim that the mechanism violates IR.

The proof is quite simple under this intuition.

> [!proof]-
> 
> Let $\nu$ denote the core matching in a housing market setup $(I, H, \succ, \mu)$.
> 
> 1. **Modified Preferences**: Construct a new preference relation, $\succ'_i$, for each agent $i$ by positioning their endowed house $h_i$ just below $\nu(i)$ in preference order.
> 
> 2. **Claim 1**: $\varphi(\succ') = \nu$, where $\varphi$ is any PE, IR, and SP mechanism, and $\nu$ is the only PE and IR matching under $\succ'$.
>     - **Proof**: For the preference profile $\succ$, let $C_1, \ldots, C_k$ represent the cycles in the Top Trading Cycle (TTC) mechanism, and let $\nu'$ denote the outcome of mechanism $\varphi(\succ')$.
>     - Consider the agents in the first cycle $C_1$. For an agent $a_\ell \in C_1$ assigned to $\nu(a_\ell)$, since $\varphi$ is IR, each agent in $C_1$ receives their most preferred choice under $\nu$.
>     - Thus, $\nu'(a_\ell) = h_\ell$ for each agent in $C_1$, and since agents strictly prefer $\nu(a_\ell)$ under $\succ'$, the mechanism would fail Pareto efficiency if $\nu' \neq \nu$ for any agent in $C_1$.
>     - Repeating this argument for cycles $C_2, C_3, \dots$ implies that $\varphi(\succ')$ must match $\nu$ across all agents.
> 
> 3. **Claim 2**: $\varphi(\succ) = \nu$.
>     - Start with one agent $i$, and incrementally alter the preference order from $\succ$ to $\succ'$, replacing each agent’s preference individually.
>     - By strategy-proofness, $\varphi_i(\succ'_i, \succ_{-i}) \succeq'_i \varphi_i(\succ) = \nu(i)$ and $\nu(i) = \varphi_i(\succ) \succeq_i \varphi_i(\succ'_i, \succ_{-i})$. But $\{h: h \succ_i' \nu(i)\}$ and $\{h: h \succ_i \nu(i)\}$ are the same set, hence $\nu(i) = \varphi_i(\succ'_i, \succ_{-i})$ for each step.

# Housing Lotteries

We now return to the original problem of house allocation. Such a problem is underspecified, so we will be exploring randomized solutions.

>[!theorem]
>==**Simple Serial Dictatorship**== is a method of house allocation. Give an ordering $f: [n]\to I$, SSD simply assigns $f(1)$ their top pick, $f(2)$ their top pick among remaining houses, etc.
>
>SSD is CE and SP.

This is essentially trivial, and the proof is left to the reader.

>[!idea] (Abdulkadiro˘glu & S¨onmez 1998)
>One deep result is that SSD under a random permutation $f$ and Core under a random initial allocation yield the same distribution.

### Lotteries
> [!definition] Lottery
> A ==**lottery**== is a probability distribution over feasible assignments, formally denoted by:
> $$
>	L = \sum \alpha_\mu \cdot \mu
> $$
>  where $\alpha_\mu \in [0, 1]$ is the probability weight of assignment $\mu: I\to H$.
>  
>  People like to write these as matrices (which contain strictly less information); $P = [p_{ih}]$, where $p_{ih}$ is the probability of agent $i$ receiving house $h$. The random assignment induced by lottery $\sum \alpha_\mu \cdot \mu$ is just
>$$
> P = \sum \alpha_\mu \cdot \pi(\mu)
>$$
>where $\pi(\mu)$ is the corresponding permutation matrix.

There are many ways to define efficiency over such a random allocation. A lottery is ==**ex-post efficient**== if it assigns positive weight to only Pareto-efficient assignments.

Two lotteries are called ==**equivalent**== if they induce the same random assignments, this definition indicates that we'll ignore data on the joint distributions in the sequel.

Here's a silly result:
>[!theorem] Birkhoff-von Neumann Theorem
>Any bistochastic matrix can be expressed as a convex combination of permutation matrices.

>[!example]-
>    $$
>    P = \begin{pmatrix} 0.5 & 0.5 & 0 \\ 0 & 0.5 & 0.5 \\ 0.5 & 0 & 0.5 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + \frac{1}{2} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}
>$$


### Cardinal Treatment

Simply assign Von Neumann–Morgenstern utility functions. A ==**ex-ante efficiency**== is defined in the obvious way by the expectation of this utility function. In the sequel, we throw away these cardinal utility functions.

### Ordinal Treatment

There still exist probability distributions over allocations that are strictly preferred by agents over other probability distributions! Namely, distribution $p$ is preferable to distribution $q$ over $H$ if *every* compatible utility function would prefer $p$ to $q$ - we simply use the poset induced by lexicographic ordering via the ordinal preference function.

>[!definition] Stochastic Dominance and Ordinal efficiency
>Given two random consumptions $P_i$ and $Q_i$ with strict preference $\succ_i$:
>  $$
>  \forall h \in H, \quad \sum_{h' \succeq_i h} p_{ih'} \geq \sum_{h' \succeq_i h} q_{ih'}
>  $$
> A random assignment $P$ is ==**ordinally efficient**== if it is not stochastically dominated by any other random assignment under the preference ordering $\succ$.


### Probabilistic Serial (PS) Mechanism

Let's realize an OE mechanism. Each house is treated as a real-valued reservoir, and agents will simultaneously "eat" from their top choices at the same rate the house is consumed, moving to second choices as needed.

This is greedily OE, and the proof is tedious but essentially clear.

>[!idea]
>The notion of SP is not well-defined here, because ordinal preferences do not induce a total ordering over the space of probability distributions. If one assigns a VNM utility function, PS may not be SP.
>
>However, suppose we fix just a *single* agent $i$'s utility function $u_i$. There exists some $N$ such that if $n\geq N$, then no matter what the utility functions of $j\neq i$ are, it is dominant for $i$ to truth-tell under SP.