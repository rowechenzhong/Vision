A ==**Bayesian game**== contains:
- A set of players $N$, types $\{T_i\}_{i\in N}$, and allocations $\Theta$.
- A probability distribution $p$ on $\Theta\times T$.
- A set $A_i$ of actions for each player $i$.
- A VNM utility function $u_i: A\times \Theta\times T\to \RR$.
Gameplay:
- ==**ex-ante**==: Nature deals $\theta, t$.
- ==**interim**==: gameplay
- ==**ex-post**==: cash out
Strategies are $T_i\to A_i$ mappings.

Then, the concept of Nash equilibrium is equivalent (modulo zero-probability types) to$$s_i^*(t_i) = \arg\max_{a_i\in A_i} \EE\left[u_i\left(a_i, s^*_{-i},\theta, t\right) | t_i\right].$$Mixed strategies can be defined similarly.