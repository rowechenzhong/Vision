$I = [n]$ are agents, $A$ are social alternatives, each agent has a private type in $T_i$, and public ==**utility functions**== $u_i: T_i\times A\to \RR$.

The ==**state space**== is $T = \prod_i T_i$ consisting of states (all private information).

Each agent can submit a message in $M_i$, and $\varphi: M\to A$ is a ==**mechanism**==. This induces a strategic game called "pick a message and try to get the best utility from the mechanism." We call $v_i(t_i, m) = u_i(t_i, \varphi(m))$.

A ==**strategy**== is $s_i:T_i\to M_i$, and $S_i = M_i^{T_i}$, and $S = \prod S_i$. Given $s\in S$ and $t\in T$, we can consider $s(t) = \left(s_i(t_i)\right)_{i\in I}$. 

Great. The first major definitions are as follows.

A strategy profile $s\in S$ is a ==**dominant-strategy equilibrium**== if *everyone* dominates *all possible deviations by all other parties*. That's super strong. Specifically, for all agents $i\in I$, for all types $t_i\in T_i$, for all possible deviations by everyone else $m_{-i}\in \prod_{j\neq i} M_j$, and for all alternative messages $m_i \in M_i$, $$
	v_i\left(t_i, \left(s_i(t_i), m_{-i}\right)\right) \geq v_i\left(t_i, \left(m_i, m_{-i}\right)\right) 
$$
> [!idea] Perfect-information case -- Nash Equilibrium
> Suppose we have perfect information, i.e. $T_i = \{*\}$ are each singletons. Then a ==**Nash Equilibrium**== is when for all $i\in I$, for all possible deviations by all other parties $m_{-i}\in \prod_{j\neq i} M_j$, and for all alternative messages $m_i \in M_i$,$$v_i\left(m_i^t, m_{-i}^t\right)\geq v_i\left(m_i^t, m_{-i}^t\right)$$where we're using the obvious notation and dropping all $t$'s. 

The usual Nash Equilibrium