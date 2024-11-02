>[!definition] Dead Weight Burden of Tax
>The ==**dead weight burden**== (also known as dead-weight loss) of a tax refers to the efficiency loss associated with a tax on goods, which arises due to changes in consumer behavior in response to the tax.

# Why Lump-sum taxes are better than Ad Valorum taxes

>[!definition] Two types of Taxes
>1. ==**Lump-sum tax T**==: deduct $T$ from the consumer's income $I$.
>2. ==**Ad valorum tax**==: increase $p_x$ by $t$.

In the ad valorum tax, the amount of income necessary to preserve the utility of the consumer is $I = E(p_x + t, p_y, u)$. We can Taylor expand this guy for small $t$:$$
E(p_x, p_y, u) = E(p_x + t, p_y, u) - t \frac{\pa E}{\pa p_x}(p_x + t, p_y, u) + \frac{t^2}{2} \frac{\pa^2 E}{\pa p_x^2}(p_x + t, p_y, u)
$$recall that in the [[Expenditure Function]] we computed $\frac{\pa E}{\pa p_x} = x^c$, so we rewrite this as$$
E(p_x, p_y, u) = E(p_x + t, p_y, u) - t x^c + \frac{t^2}{2} \frac{\pa x^c}{\pa p_x}.
$$(all quantities on RHS evaluated at taxation $(p_x + t, p_y, u)$). Cool. The amount of revenue $R_{AV}$ we raise is exactly $tx^c(p_x + t, p_y, u)$. An ad valorum tax on $x$ causes a decrease in quantity of $x$ purchased by substitution to $y$ which can be approximated by:$$
\Delta x = -t \frac{\partial x^c}{\partial p_x} \Big|_{u=\text{const}}.
$$so yeah, we find that the amount of income consumers needed *before* the tax is $E(p_x, p_y) = I - R_{AV} - \frac{t}{2}\Delta x$ where $I$ is the amount of income consumers need *now*.

The equivalent lump-sum tax could snatch up all of this money, $R_{\text{lump}} = T = R_{AV} + \frac{t}{2}\Delta x$ which is obviously better.

---
When the price of a good, say $x$, changes from $p_a$ to $p_b$, the consumer's welfare is impacted. Originally, I was rocking utility $u_a$ with my income of $I = e(p_a, u_a)$. After the change occurs, my income is still $I = e(p_a, u_a)$. That's annoying, because at price $p_b$ I can only get utility $u_b = V(p_b, I)$.

Okay, how much utility did I lose? Utility can't be easily converted into money (if money isn't one of the products, non-quasilinear...) so there are two good ways to quantify this:

>[!idea] Compensation for Price Changes
> - The ==**Compensating Variation**== is $e(p_b, u_b) - e(p_b, u_a)$. The price change already happened, and you're compensating the customer by the amount that they need to preserve $u_a$.
> - The ==**Equivalent Variation**== is $e(p_a, u_b) - e(p_a, u_a)$. The price change hasn't happened yet, and this is how much the customer would pay you to keep it that way.
> The ==**Naive (Slutsky) Variation**==: it's just $x(p_a - p_b)$; this doesn't account for the change in the quantity the customer buys.

If $p_b > p_a$, then EV $\geq$ Naive $\geq$ CV. This vanishes if the utility is quasilinear, i.e. in the absence of income effects.

# Cost of Living Indices

In the US, the consumer price index plays this role (CPI).

>[!definition] Cost of Living Index
>The ==**cost of living index**== measures changes in the amount of money required to maintain a certain utility level.
>
>- ==**True cost of living index**==:
>$$
>\frac{E(p_b^x, p_b^y, u^a)}{p_a^x x_a + p_a^y y_a}.
>$$
>- ==**Conventional index**== (used in practice) over-estimates inflation, because it does not compute the correct new $x^b, y^b$.
>$$
>\frac{p_b^x x_a + p_b^y y_a}{p_a^x x_a + p_a^y y_a}.
>$$
>
>Note: The true index is less than or equal to the conventional index, with equality only if there is no substitution or if all prices change in the same proportion.