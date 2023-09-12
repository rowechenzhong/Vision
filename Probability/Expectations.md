Integration turns into the [[expected value]] of a random variable.

> [!definition] Covariance
> The ==**covariance**== of two random variables $X,Y \in L^2$ is
> $$\Cov(X,Y) = \EE\left(\left(X - \EE[X]\right)\left(Y - \EE[Y]\right)\right) = \EE(XY) - \EE[X]\EE[Y]$$
> If $\Cov(X,Y) = 0$, then we say $X$ and $Y$ are ==**uncorrelated**==. Finally, the ==**variance**== of $X\in L^2$ is $\Var(X) = \Cov(X,X)$.

So, surprisingly, we care about some $L^2$-space tech, such as 

> [!Cauchy-Schwarz]
> For any two random variables $X,Y\in L^2$, $\EE(\abs{XY}) \leq \norm{X}_2 \norm{Y}_2$.

>[!todo] Prove this lol