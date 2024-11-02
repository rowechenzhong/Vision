As the most elementary example, we are given an exogenous price vector $p\in \RR^L$ and a quantity vector $x$ constrained to the income $I$ by ==**budget set**== $x\in B(p, I) = \{x: p\cdot x\leq I\}$. Then obviously we select $x^*(p,I) = \arg\max_{x\in B(p,I)} u(x)$, obtaining utility $v(p,I) = \max_{x\in B(p,I)} u(x)$.

Then $v$ is the ==**indirect utility function**== and $x^*(p,I)$ is the ==**Marshallian demand correspondence**== (correspondence because in full generality $x^*$ is a set; if unique, then this is the ==**M.d. function**==). The Md function is sometimes also called the ==**Walrasian demand function**==.

When we do not state otherwise, $v$ and $x^*$ are defined as in the above example. In this case, observe $v$ is strictly increasing in income, decreasing in prices, and homogenous when both prices and income are scaled.

### Key Properties (14.04):

1. ==**Homogeneity of degree zero**==; $V(kp_x, kp_y, kI) = V(p_x, p_y, I)$; (here, money itself is not counted as a good, so we're assuming the price of everything and money scaled).
2. ==**Roy's Identity**==; $x^* = - \frac{\pa V / \pa p_x}{\pa V/ \pa I}$. 
3. ==**Convex Iso-utility Curves**==

See [[Expenditure Function]]