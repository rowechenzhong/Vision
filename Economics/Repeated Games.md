Given a stage game and an $n\in \ZZ_{\geq 0}$, its corresponding ==**repeated game**== consists of playing the same game $n$ times, where the infoset of each player is updated with the entire history at the beginning each "stage game."

If the stage game has one Nash Equilibrium, then by induction there is only one SPNE. However, if a stage game contains multiple NE, then the set of SPNE expands to include "cooperative strategies" where players may not play any NE in a particular stage game.

Given a stage game and a discount factor $\delta$, define the infinitely repeated game in the obvious way. The first main result is that OSDP still applies given continuity conditions on the full game. The second main result follows.
- A payout vector is ==**feasible**== if it is obtainable under some joint stage game strategy profile.
- The ==**pure-strategy minimax payoff**== is$$m_i = \min_{a_{-i}\in A_{-i}} \max_{a_i\in A_i} u_i(a_i, a_{-i}).$$This is not an obvious quantity to think of, I think. This gives you positional advantage, but allows everyone else to collude against you. The point is that you will always do at least this good in a Nash Equilibrium, because otherwise you would deviate.
- The ==**minimax payoff**== $\mu_i$ is the same, but over mixed strategies. Note $\mu_i \leq m_i$; you already have position so you don't benefit from randomizing, while others are strictly better off.
- A payout vector is ==**individually rational**== if $v_i\geq \mu_i$. 

>[!theorem] Folk Theorem
>Suppose $v$ is feasible. If it is strictly better than IR ($v_i > \mu_i$ for every player $i$) then there exists a $\eps\in (0, 1)$ such that for every $\delta > \eps$ there exists an SPNE obtaining $v_i$ in expectation.
>
>If $v_i > m_i$ for every $i$, then the SPNE can be in pure strategies.
