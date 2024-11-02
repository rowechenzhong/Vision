---
aliases:
  - Marshallian Demand
---
>[!idea]
>There are no real ideas here, just lots of words.

# Basics

A ==**utility function**== is a measure of the satisfaction that an agent assigns to a state of the universe. Rational agents act to optimize utility functions.

A utility function encodes ==**preferences**== (a complete ordering on the states of the world).
- If this is all that we care about (such that increasing functions of utility functions are identified) we say the utility function is ==**ordinal**==.
- Else, it is ==**cardinal**==; we assign meaning to the absolute size of the utility function. This is required to meaningfully represent expectations; we otherwise cannot easily compare actions that yield probabilistic distributions over states of the universe.

We usually model the world as containing $L$ ==**commodities**==, such that the possible states of the universe are ==**consumption sets**== in $\RR_{>0}^L$ . In this case, we usually model that utility functions are ==**monotonically increasing**== (this is called ==**non-satiation**==). 

We assume cardinal monotonic utilities with only minor modifications in the sequel.

The ==**marginal utility**== of $X$ is $MU_x = \frac{\pa U}{\pa X}$. The ==**marginal rate of substitution**== is $MRS_{1,2} = \frac{MU_1}{MU_2}$.

# Indirect Utility Functions

As the most elementary example, we are given an exogenous price vector $p\in \RR^L$ and a quantity vector $x$ constrained to the income $I$ by ==**budget set**== $x\in B(p, I) = \{x: p\cdot x\leq I\}$. Then obviously we select $x^*(p,I) = \arg\max_{x\in B(p,I)} u(x)$, obtaining utility $v(p,I) = \max_{x\in B(p,I)} u(x)$.

Then $v$ is the ==**indirect utility function**== and $x^*(p,I)$ is the ==**Marshallian demand correspondence**== (correspondence because in full generality $x^*$ is a set; if unique, then this is the ==**M.d. function**==). The Md function is sometimes also called the ==**Walrasian demand function**==.

When we do not state otherwise, $v$ and $x^*$ are defined as in the above example. In this case, observe $v$ is strictly increasing in income, decreasing in prices, and homogenous when both prices and income are scaled.

Main article: [[Indirect Utility Function]]

# Quasilinear Utility Function

If your utility function includes money or a linear function of money, then your indirect utility will be of the form $v(p) + I$.

Indeed, if your utility function looks like $u(x, x_1,\dots, x_n) = x + \theta(x_1,\dots, x_n)$ at prices $p_0, p_1,\dots, p_n$, then by Lagrange multipliers, we obtain $x^*_i = \left(\frac{\pa \theta}{\pa x_i}\right)^{-1}\left(\frac{p_i}{p}\right)$ for each $i\geq 1$ and $x = \frac{I - \sum p_ix_i}{p}$. 

We almost always make the assumption of a quasilinear utility function; when looking at agents with zero market impact, the exogenous prices can be tucked away into the constant $v(p)$ term. This simplifies the analysis.

Main article: [[Quasi-linear Utility Function]]