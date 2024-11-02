Recall the definitions of [[Externalities]], [[Utility functions#Indirect Utility Functions]]. 

Basically, if agent $A$ can affect agent $B$, and there are no contractually binding methods for agent $B$ to alter agent $A$'s actions, then we will have suboptimal conditions. This is completely obvious.

# Raw notes
There's this like, supply-demand curve right, and there's a total surplus because of the difference between the price at quantity there. Blah. The market price maximizes market equilibrium.

1. Wallraising auctioneer. Where does the equilibrium come from? A major weakness of the undergraduate story is how do we get to the market price. Answer: Auction.
2. Why perfect competition? Monopoly creates ==**dead-weight loss**==. Price, Demand, MR, MC. The delta between MR and MC is the markup. That's called dead-weight loss (its profit for the company).
### Coase Theorem and missing markets

Consider like two agents $i = 1,2$ which are small w.r.t the economy (no price impact).
 Each has wealth $w_i$, and the goods consumed in the economy are some vector $\vec{x}$. Player one moves as $h\in \RR_+$.
Indirect utilities take the form $v_i(p, w_i, h) = \phi_i(h) + w_i$. The agent's objective function depends only on $h$ and $w_i$. We suppress dependence on $p$ because our guys can't touch that.

$\phi$ is twice differentiable and $\phi'' < 0$ everywhere. We also waffle that all maximization problems have interior solutions. An allocation is $((x_i)_{i \in 1,2}, h)$. I.e., the good consumed by $1$ and $2$ and the level of music or the move $h$.

A competitive equilirbium is a price and allocation pair such that individuals maximize their utility given prices and prices clear markets.

We care about how $h$ is determined. To solve for the competitive equilibrium, then max holding $p$ constant, then max $p$.

There's no market for $h$ yet, so we just maximize $\phi'_1(h^\star) = 0$. That's pretty stupid. $\phi'_2$ has no say.

A ==**Pareto optimal allocation**== is one such that you can't make any consumer strictly better without hurting someone else.

First welfare theorem: competitive equilibrium is Pareto-optimal.
Second welfare-theorem: Any pareto-optimal allocation can be achieved as a competitive equilibrium with lump sum transfers.

Previously, people thought they would use Quotas. but this is dumb because you can't figure out $\phi$.

Also people thought that you might put a tax on it. But that's also stupid. Pigouvian Corrective Tax.

Consumer 1 internalizes the externality that she imposes on consumer 2.

So anyways, quotas and taxes are bad because you need too much information.

Coase, two major problems:
- Lack of clearly specified property rights.
- Transaction costs.

Imagine we have clearly specified property rights and consumer 2 has control over whether $h$ is allowed. So consumer $2$ makes a take-it-or-leave-it offer demanding $T$ for permission to use $h$.