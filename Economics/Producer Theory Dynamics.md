# Reactions of Competitive Firms

![[Pasted image 20240916145147.png]]

Okay, in this model that we're using now, $MC(q)$ my not be strictly increasing on $q \geq 0$ ; this makes the problem more interesting.

![[Pasted image 20240916152110.png]]

In this [Econ Graph | Desmos](https://www.desmos.com/calculator/lpnvizghzt), MC is in red, the total cost is in purple, and the utility curve for a specific price is in blue. Obviously, we should pick the maximum around $q = 5$. There is a phase transition, at which point the optimum becomes $q = 0$.

The minimum AVC is the short-run shut-down cost. The minimum of ATC is the long-run shut-down cost.

# Economies of Scale and Scope

(Dis)Economy of Scale = larger scale lowers (raises) cost.
- EoS because of specialized equipment etc, amortizing fixed costs.
- Dis-EoS because of:
	- Managerial overhead
	- System slack

Also industry level; increase in the production of PCs will lower the price of disc drives, scale economy. ==**External economy of scale**== means it  doesn't matter whether one firm or many firms are responsible for the increased production.
- The thing is, even with external economy of scale, there might be firm-level diseconomies of scale. The size of any individual firm is limited, but if you add more firms, the total output of the industry goes up while prices go up sublinearly.
- External diseconomies of scale if a larger industry drives up input prices, e.g. soybean production increase requires you to use suboptimal land to expand.
- External economy of scale if an increase in output permits the creation of more specialized tech, because R+D is more lucrative.

Economy of Scope = larger scope (produce several goods) is better.
- Boeing: commercial and military jets, amortized R+D costs.

In economies of scale, paying each input their marginal product is not possible usually, because$$
x_1\frac{\pa f}{\pa x_1} + \dots + x_n \frac{\pa f}{\pa x_n} > f(x_1,\dots, x_n).
$$
They want to define this EoS iff full scaling. $f(\lambda x_1,\dots, \lambda x_n) > \lambda f(x_1,\dots, x_n)$ for all $\lambda > 1$.

# Dynamics with Constant Costs


![[Pasted image 20240923145752.png]]

New diagram just dropped.

- The Demand curve is per-period. It just exists.
- The short-run-supply has a cutoff at some critical price, below which the optimal quantity is $0$ (recall the cubic curve phase transition thing).
- In the short-run, the quantity that gets produced is $Q_0$. Makes sense.
- However, this diagram shows something special: we're currently in a state where the Long-run-supply is also exactly at this price level.

Recall that the LRATC, long-run average total cost, at the industry level, is supposed to reflect any external diseconomy or economy of scale. In this particular diagram, we are showing an example where this is NO external EOS. To be explicit, the LRATC graphs the average total cost, meaning total cost used by the entire industry, divided by quantity, at each value of the quantity. This assumes that such quantity is distributed in a GTO manner across the economy.

The LRS is the supply at each particular price point in the long-run. In the long-run, the suppliers will all optimize. Thus, in the long term, if price falls below the MINIMUM average TOTAL cost (not the minimum average variable cost, as in the short-term), then it would be GTO to simply stop producing and shut down. Meanwhile, if the price goes ABOVE the minimum average total cost, then the producers will increase their production, driving costs down; in the limit where there are many many producers, in the long term this will drive the cost down to the minimum average total cost of the *single most efficient producer*.

Anyways, in the diagram show, the industry is in equilibrium. All firms are indifferent to shutting down versus starting up (and thus they don't, because there are obviously short-term costs to shutting down/starting up that we're ignoring) because they're producing exactly at their minimum average total cost. Also, there is no excess output and no consumer is rationed (so the consumers are indifferent to buying more or less as well).

Okay now suppose demand increases. The short-term change is obvious. The long-term change is that the price is higher than the LRATC, so producers are doing long-term activities (investments) as well which pushes the SRS curve forwards; at any given price, producers can make more. I guess the LRS doesn't change? We're not talking about actual technological inventions here which push the asymptotic LRS; we're more talking about buying more of existing tech to replace old tech.

![[Pasted image 20240923152121.png]]

Great, not deep. In the decrease case, we're about the same.
![[Pasted image 20240923152645.png]]

Here, the long-run decrease in supply is due to firms exiting (??? I don't get that part) and possible disinvestment (selling off big machines for older smaller less-efficient machines for short-term economic gain).

However, if the short-term demand decrease is large enough, we get immediate exits. This is qualitatively different, but I guess it's not that complicated conceptually. Here.
![[Pasted image 20240923152921.png]]

# General Long-run Dynamics

Not much new here?

The interesting thing is that while SRS and SRD are obviously non-decreasing and non-increasing, because of effects like "economy of scale," the LRS could be decreasing. The analogous phenomena for LRD is for long-term demand to be *increasing*; this is called ==**network externality**==, where the addition of more users to a product increases the product's value, e.g. a telephone.