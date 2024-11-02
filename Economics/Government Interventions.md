>[!idea]14.04 Content: [[Taxes]]

# Effects of Taxes

A tax imposed on the seller moves the supply curve up by ==**constant tax**== $t$, ditto for consumer and demand. Dead weight loss is this:
![[Pasted image 20240914213016.png]]
and is sad.

Fall in quantity, diversion of revenue to government, $O(t^2)$ dead-weight loss.

One can compute these things with elasticity to first order. The new equation we have is that $p_b = (1 + t)p_s$ due to a ==**percentage tax**== $t$. (This is also called an ==**ad valorem tax**==)

A small proportional tax increases the price to the buyer by $\frac{\eta t}{\eta + \eps}$ and decreases the price to the seller by $\frac{\eps t}{\eta + \eps}$. The quantity falls by $\frac{\eta \eps t}{\eta + \eps}$.

### Excess Burden of Taxation

We want to quantify dead-weight loss.

They start using new variable names but these are the same symbols we had before, marginal cost of quantity $q$ is $c(q)$ (supply) and the marginal value is $v(q)$ (demand). The tax is thus $v(q^*) = (1+t)c(q^*)$ and we can compute that:
- the tax revenue is $T = tq^*c(q^*)$, maximized when $t_{max} = \frac{\eps}{\eps - 1}\left( \frac1\eps + \frac1\eta\right)$. (This is the maximization you get if you assume that the local calculations hold indefinitely, shrug)
- The ==**gains from trade**== is the consumer surplus PLUS the producer surplus PLUS the tax revenue. This decreases as we increase tax due to dead weight loss:
  $$
  \frac{dGFT}{dT} = -\frac{\eps}{\eps - 1} \frac{t}{t_{\text{max}} - t}
  $$
  where $T$ here is the actual tax revenue lol.

# Price Floors and Ceilings

- A price floor/ceiling sets the minimum allowable price for a product or service..
- If a price floor is set below the market equilibrium price, it does not influence the market. However, if it is above the equilibrium price, it leads to excess supply.
- The economic inefficiency caused by a price floor, termed ==**deadweight loss**==, represents the loss in societal value from goods that are produced but not sold, based on their demand and production costs.
![[Pasted image 20240914215149.png]]
- This diagram is a **lower bound** on deadweight loss, but in practice it will be higher because some mfs who actually wanted to buy it in the price range $(demand(q_d), demand(q_s)]$ exclusive will end up buying it. Optimally, only the mfs who actually wanted to buy it at the price $demand(q_s)$ buy it, thus obtaining the maximum utility gain, but IRL this can't really happen. Other solutions only trade-off the utility; the best you can do is probably randomization idk.
- Price floors disrupt market efficiency, leading to fewer transactions, wasted resources on unneeded production, and higher production costs than necessary.
- Besides causing underproduction, price ceilings can result in inefficient resource allocation and may promote black markets and discriminatory practices.

# The politics of price controls.

>[!idea]
>Both demand and supply are *more elastic in the long run* i.e. if there is a sustained high price over a long period of time, the supply will rise more and more and the demand will drop more and more.

This is because like, if you're looking into apartment rent or something, if the rent increases, you can't just leave, so your demand stays constant against your will. Unfortunate. But give time, you're out of there.

Thus, we have a SRS curve (short-run supply) and a LRS curve (long-run supply).

Okay, now we have the price control. This price control is set at the current SRS equilibrium, and in the short-term, everything's okay because everyone's very inelastic. This is politically good short-term, and politicians only care about the short-term. In the long term, everyone gets fucked, because:
- The core reasons:
	- demand for apartments will grow as the city population grows. So, demand goes up.
	- supply of apartments goes down because of property tax increases or whatever.
	- These are examples of things that can happen, but ostensibly people expected the price to go up, which is why they put the price control on.
- So what happens? Well, in the short-term, nothing happens and people are sort of okay.
- In the long term, the curves just move, and we get the shortage. Meanwhile, the "new SRS" curve is always the LRS against the rent control, because the short-term is just wherever the demanders currently are.

This is an example of tyranny of the majority.

# Price support

Price floor PLUS a government purchase of surplus.

![[Pasted image 20240914225240.png]]

The overall inefficiency generated is the vertical shading as usual due to customers who would otherwise be benefiting from the trade who won't trade because of the high prices, and the horizontal shading which is due to the cost of creating all of the extra product that the government bought for no reason.

The good thing is that there's no black market (only the government has all of this surplus).

# Quotas 
- Maximal production quantity. This can be implemented in many ways, but the example is a "taxi driver medallion."
- This transfers wealth from buyers to sellers essentially immediately, and future generations pay for the program. No surpluses arise.
	- What does this mean. Well, consider the taxi drivers.
	- Immediately, the taxi drivers which want to drive the least are eliminated, because they cannot afford the medallion. The supply curve basically gets moved upwards by the price of the medallion. However, all taxi drivers which *can* afford the medallion are suddenly getting paid a lot more. Bink?
	- The major winners are anyone who magically got a medallion for free, such as people grandfathered into the system. Let's assume that this is the case. This is the "wealth transfer to the sellers;" people who have a medallion but don't actually like driving taxis enough to justify holding the medallion can sell the medallion.
	- The major losers are the customers, who will now forever have to pay more to ride taxis. Smoge.
- Tradable quotas can mitigate the problem that quotas don't evolve and become more inefficient with time.