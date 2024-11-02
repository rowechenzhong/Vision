# Four major types of firms
### Proprietorships
One individual or family.

### Partnerships
Share profits between people, and are all liable for losses.

### Corporations
==**Limited Liability**==, in that they are not financially responsible for debt.

Historically, organized in a pyramid structure. The modern corporation operates as a collection of semi-autonomous "business units" which buy and sell from each other.

### Non-profit Firm
Prohibited from distributing a profit to its owners. Not taxed. 

# Production Functions

Function from the amount of inputs to the amount of outputs. The ==**Cobb-Douglas Production function**== is $y = f(x_1,\dots, x_n) = a_0\prod x_i^{a_i}$. Isoquants are contour lines, and their 

Perfect complements in supply looks like $\min(x_1, x_2)$ while perfect substitutes look linear like $a_1x_1+ a_2x_2$.

The marginal product of an input is just the partial derivative.

Some inputs can be changed in the short-run, such as labor (classically) while other inputs cannot, such as capital equipment.

# Profit Maximization

$\pi$ means profit. Use first-order conditions too compute. Things are complements in production if $\frac{\pa^2 F}{\pa K \pa L}$ is positive (increasing $K$ increases the marginal product of $L$), and substitutes if negative.

# The Shadow Value

This is a dumb thing; if you have some production function $F(K,L)$ but you're constrained to $K = K_0$ which is sub-optimal, then the ==**shadow value**== of capital is $\frac{d \pi(K, L^*(K))}{dK}$.

(Because $L^*$ will not change $\pi$ to first order, this is just $\frac{\pa \pi}{\pa K}(K, L^*(K))$, but whatever.) In other words, it is the marginal value of the changing this constraint.

If $K$ is smaller than $K^*$, then (usually) this value is positive because we want to increase $K$; and vice-versa.

This constraint might be due to short-run effects. 

# Input Demand

The slope of an isoquant is called the ==**marginal rate of technical substitution**==; $RTS_{kl} = - \frac{dk}{d\ell}\big\vert_{q = \text{const}} = \frac{\pa f/\pa \ell}{\pa f/\pa k}$. 

The ==**elasticity of substitution**== (14.04 convention) is$$
\sigma = \frac{\pa \ln\left(k/\ell\right)}{\pa \ln RTS_{k\ell}},
$$i.e. if I change the RTS by a small relative amount, how much does $k/\ell$ change relatively.

>[!example]
> - If inputs are perfect complements, then $\sigma = 0$; $f(k, \ell) = \min(ak, b\ell)$ works because $k/\ell$ will always be fixed at $b/a$.
> - In Cobb-Douglas, $RTS = \frac{k}{\ell}$ so $\sigma = 1$.
> - If $f(k,\ell) = ak + b\ell$ (say) then there is infinite elasticity, because if we are currently in a marginal situation $a = b$, then increasing $RTS$ a tiny bit will step-function $k/\ell$ from $0$ to $\infty$.
> 
> These are best appreciated as the limits of the ==**Constant Elasticity of Substitution**== model,$$q = \left(ak^\beta  b\ell^\beta\right)^{\gamma / \beta},$$where $RTS = \frac{b}{a} \left(\frac{k}{\ell}\right)^{1 - \beta}$ and $\sigma = \frac{1}{1-\beta}$.

14.04: [[Technical Progress]]


# Types of Costs

They define a bunch of things, but nothing here is deep. We denote the short-run adjustable inputs are denoted $L$, while the short-run fixed inputs are denoted $K$. 
1. The ==**Short-run Total Cost**== (of producing some fixed quantity $q$, $SRTC(q | K)$, is $\min_L rK + wL$ conditioned on $f(K,L)\geq q$.
2. The ==**Short-run marginal cost**== is the derivative of SRTC with respect to $q$ with $K$ remaining fixed.
3. The ==**Short-run Average (Total) Cost**== is $\frac{SRTC(q|K)}{q}$.
4. The ==**Short-run Average Variable Cost**== is $\frac{SRTC(q|K) - SRTC(0|K)}{q}$.

![[Pasted image 20241006011726.png]]

This is a 14.04 diagram. S (label is in bottom-left) is pink. MC means the marginal cost (ever). SAVC means SAVC. SAC means SATC, where FSC means $SRTC(0 | K)$. SMC also means marginal cost, I think.

1. When the price is below $p_1$, $q_0$ is optimum. Duh.
2. When the price is $(p_1, p_2)$, it means that there are some quantities at which the marginal cost is less than the price, but this doesn't mean anything because we can never cover the original price.
3. When the price is $(p_2, p_3)$, then in the short-run it makes sense to produce, but note that we're still losing money; we're just losing less money than if we didn't open up.
4. When the price is above $p_3$, we're making bank.

Again, note that the pink line is discontinuous at $p_2$, the minimum of the SAVC.

The long-run analogous ones are:
1. The LRTC is a global minima because everything can vary.
2. The LRMC is dLRTC/dq.
3. The LRAC still LRTC/q.
4. The LRAVC is the same as the LRAC because there's no fixed values so $LRTC(0) = 0$.

![[Pasted image 20241006010021.png]]

This diagram shows LRMC and LRAC on the right, and LRTC on the left.

14.04 material: see [[Profit Maximization]].