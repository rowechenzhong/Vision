Here is a summary of each lecture with key equations, highlighting the important concepts while discarding examples:

### Lecture 1: Introduction to Macroeconomics
- **Macroeconomics** studies aggregate economic activity and addresses key questions like what determines the size of economies, growth, unemployment, inflation, and exchange rates.
- **Key Topics:**
  - **The Crisis**: Post-2007 U.S. housing crisis led to a global economic downturn.
  - **National economies** (e.g., U.S., Eurozone, China) with varying growth, inflation, and unemployment rates.
  - **Output and Unemployment**: Macroeconomics studies these metrics across different countries.
- **Equations**:
  - Growth Rate: $g_t = \frac{Y_t - Y_{t-1}}{Y_{t-1}}$
  - Inflation Rate: $\pi_t = \frac{P_t - P_{t-1}}{P_{t-1}}$

>[!definition] Bank Reserves
>Bank Reserves are cash minimums that financial institutions must maintain to meet central bank requirements. These ensure that banks can meet sudden large demand for withdrawal and avoid catastrophic bank runs. Banks are otherwise incentivized to minimize ==**excess reserves**== on top of the ==**required reserve**== because cause earns no return.
>
>In the U.S., this ==**reserve ratio**== is maintained by the Federal Reserve.

>[!definition] Federal Funds Rate
>Banks can borrow from each other overnight in order to meet the reserve ratio. The interest that banks are allowed to charge is called the ==**Federal Funds Rate**==.
>
>As a last resort, banks can also borrow from the central bank at the ==**discount rate**== (which is higher than the FFR).

Why did the Federal Funds rate stop at zero?
- This constraint is known as the zero lower bound.
- If it were negative, then everyone would hold cash rather
than bonds.
Why are low interest rates a potential issue?
- Low interest rates limit the Fed’s ability to respond to
further negative shocks. (At the zero lower bound, this is called the **liquidity trap**).
- Low interest rates may lead to excessive risk taking by
investors to increase their returns.

>[!idea] $\downarrow$ FFR $\implies \uparrow$ borrowing $\implies \uparrow$ spending and investment.
>Hence lowering the rate can stimulate economic growth and prevent unemployment from rising.

>[!idea] $\uparrow$ FFR $\implies \downarrow$ borrowing $\implies \downarrow$ spending $\implies \downarrow$ pressure on prices $\implies \downarrow$ inflation.

---

### Lecture 2: Basic Macroeconomic Concepts
- **Key Concepts**:
  - **GDP** is:
	  - **Total value** of final goods and services produced. 
	  - **The Sum of Value Added** by each firm; the VA by a firm is the value of its production minus all intermediate goods.
	  - **Sum of incomes in the economy**: labor income (wages) and capital (also called profit) income.
  - **Nominal GDP** vs. **Real GDP**: 
    - Nominal GDP is valued at current prices, while Real GDP is adjusted for inflation; we measure in **chained (2009) dollars**; we only care about real GDP and denote it as $Y_t$; nominal GDP is denoted as $\$Y_t$.
    - DoC deals with change in quality by **Hedonic pricing**.
  - **Unemployment Rate**: Measures the percentage of people without a job but actively seeking work.
	  - $L = N + U$ Labor Force is Employment and Unemployment.
	  - Some workers are **discouraged** meaning they do not look for job.
  - **Inflation**: Sustained rise in the price level, measured using price indices such as the GDP deflator and the Consumer Price Index (CPI).
- **Equations**:
  - GDP growth is trivial $\frac{Y_t - Y_{t-1}}{Y_{t-1}}$.
  - GDP Deflator: $P_t = \frac{\text{Nominal GDP}_t}{\text{Real GDP}_t}$
  - Inflation: $\pi_t = \frac{P_t - P_{t-1}}{P_{t-1}}$
  - Unemployment Rate: $u_t = \frac{\text{Unemployed}}{\text{Labor Force}}$, Participation rate is labor force over total population.
  - Okun's Law: $\Delta u = -0.4(\Delta \text{GDP growth})$, intercept at output growth of 3\% to keep unemployment constant.
![[Pasted image 20241009131103.png]]
- Phillips Curve: change in inflation is around constant when unemployment at 6\%, with a negative slope.
![[Pasted image 20241009131158.png]]
---
### Lecture 3: The Goods Market
- **Key Concepts**:
  - **Aggregate Demand**: Defined by $Z = C + I + G + X - IM$, where $Z$ is the demand for goods.
  - **Consumption Function**: $C = c_0 + c_1(Y_D)$, where $Y_D = Y - T$ is disposable income.
  - **Equilibrium Output**: Occurs when production $Y$ equals aggregate demand $Z$.
- **Equations**:
  - Equilibrium: $Y = \frac{1}{1 - c_1}(c_0 + \bar{I} + G - c_1 T)$
  - Autonomous Spending: $c_0 + \bar{I} + G - c_1T$
  - Multiplier: $\frac{1}{1 - c_1}$

---

### Lecture 4: Financial Markets
- **Key Concepts**:
  - **Demand for Money**: $M_d = \$Y \cdot L(i)$, where $L(i)$ is a decreasing function of the interest rate.
  - **Money Supply**: Controlled by the central bank through open market operations.
  - **Interest Rate Determination**: Equilibrium in financial markets sets the interest rate.
  - **Liquidity Trap**: Occurs when interest rates are at zero, limiting monetary policy.

Money are used for transactions, but it pays no interest.
- Two types of money: currency and checkable deposits.
- Bonds pay a positive interest rate, i (the rate of interest), but cannot be used for transaction.

Central banks set the Money Supply $M_s$ (which equals $M_d$ at equilibrium) by conducting (expansionary/contractionary) open market operations to (expand/contract) the supply of money by (buying/selling) bonds. The Fed typically decides to change the interest rate instead.

---

### Lecture 5: IS-LM Model
- **Key Concepts**:
  - **IS Relation**: Represents equilibrium in the goods market where $Y = C(Y - T) + I(Y, i) + G$.
	  - $Z = C(Y - T) + I(Y, i) + G$ is the demand curve, often notated as "ZZ" on the $Z$ vs $Y$ graph, which equals $Y$ at equilibrium.
	  - Investment $I$ is a function of the production $Y$ and the interest rate $i$.
	  - The "IS curve" is the IS relation graphed on the $i$ vs $Y$ graph.
  - **LM Curve**: Represents equilibrium in the financial market where real money demand equals supply $\frac{M}{P} = Y\cdot L(i)$. Usually, the fed can just choose a desired $\bar{i}$ and change $M$ to achieve it.
  - **Fiscal and Monetary Policy**: Changes in government spending/taxes shift the IS curve, while changes in money supply shift the LM curve.
- **Equations**:
  - IS Relation: $Y = C(Y - T) + I(Y, i) + G$
  - LM Relation: $M/P = Y L(i)$
  - Fiscal Policy: $G - T$
  - Monetary Policy: $M$

---

### Lecture 6: Extended IS-LM Model
- **Key Concepts**:
  - **Risk Premium Equation**: Super naively, if there is a probability $p$ of defaulting, banks have to charge a premium of $x = \frac{(1 + i)p}{1 - p}$.
  - Real Interest Rate: $r = i - \pi^e$ where $\pi_e$ is the expected inflation. The Fed knows what $\pi^e$ is, so it can just set $r$ directly.
  - Combining this with the expected inflation, we obtain that the "effective" interest rate faced by borrowers is $i - \pi^e + x$. Hence $Y = C(Y - T) + I(Y, i - \pi^e + x) + G$.
  - **Financial Markets**: Introduces the risk premium ($x$) and probability of default ($p$).
  - **Real Interest Rate**: Central bank controls the real policy rate, affecting borrowing rates.
  - **Financial Crises**: IS curve shifts left during crises, leading to lower output.
