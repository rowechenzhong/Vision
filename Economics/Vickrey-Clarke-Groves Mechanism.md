The Vickrey-Clarke-Groves (VCG) mechanism is a method for achieving efficient outcomes in social choice problems where participants have private information about their preferences. The mechanism ensures that individuals truthfully report their preferences, leading to a socially efficient outcome.
- Let there be a set of agents $N = \{1, 2, \dots, n\}$.
- Let $D$ represent the set of possible social outcomes (or decisions).
- Each agent $i \in N$ has a private type $t_i$, which determines their utility function $v_i(t_i, d)$, where $d \in D$ is the social outcome.
$$
\begin{align*}
\text{Outcome: } d^*(t) &= \arg \max_{d \in D} \sum_{i=1}^{n} v_i(t_i, d)\\
\text{Transfer: } y_i(t) &= \sum_{j \neq i} v_j(t_j, d^*(t)) - \sum_{j \neq i} v_j(t_j, d^*(t_{-i}))\\
\text{Individual Utility: } u_i(t_i, t) &= v_i(t_i, d^*(t)) + y_i(t) = \sum_{j} v_j(t_j, d^*(t)) - \sum_{j \neq i} v_j(t_j, d^*(t_{-i}))
\end{align*}
$$
where:
- $d^*(t)$ is the efficient outcome when all agents' types are reported.
- $d^*(t_{-i})$ is the efficient outcome when agent $i$ is excluded from the decision-making process (i.e., $t_{-i} = (t_1, t_2, \dots, t_{i-1}, t_{i+1}, \dots, t_n)$).
- The transfer $y_i(t)$ represents the difference in the welfare of the other agents when agent $i$ is included versus when agent $i$ is excluded. This is called the marginal contribution of agent $i$ to society.

In the VCG mechanism, truthful reporting of an agent's type $t_i$ maximizes their utility, as their payment $y_i$ is designed to account for their contribution to the overall welfare. Thus, truth-telling is a dominant strategy for each agent. The VCG mechanism is efficient and strategy-proof, but it may result in a budget deficit in some cases.