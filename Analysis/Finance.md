# Black-Scholes

We want to price options, lol.

An option is a derivative giving you the right but not obligation to purchase an asset at some strike price at some specified future time.

$V(S,T) = (S - K)^+$. Compute $V(S, t)$ for $t < T$. We assume $S$ follows [[Geometric Brownian Motion]]. Applying Ito's formula,$$dV(S_t, t) = \frac{\pa V}{\pa S}dS_t + \frac{\pa V}{\pa t} dt + \frac{\pa^2 V}{\pa S^2} d\braket{S}_t.$$We want to hedge out all risk associated with the stock price. Consider a portfolio containing $-1$ option and $+\Delta_t$ stock. Then, $\Delta_t = \frac{\pa V}{\pa S}(S_t, t)$ such that the value of your portfolio is $\Pi_t =-V_t + \Delta_t S_t$, and evolves via $d\Pi_t = - \frac{\pa V}{\pa t} dt + \frac{\pa^2 V}{\pa S^2} \sigma^2 S^2 dt$; this is risk-free; it's literally deterministic.

There is also a money market with risk-free rate $r$. There is no arbitrage, hence $d\Pi_t = r\Pi_t dt$.

We conclude that

>[!theorem] Black-Scholes Equation
>$$\frac{\pa V}{\pa t} + \frac12 \sigma^2 S^2 \frac{\pa^2 V}{\pa S^2} + rS \frac{\pa V}{\pa S} - rV = 0.$$

# Risk-Neutral Measure

TODO