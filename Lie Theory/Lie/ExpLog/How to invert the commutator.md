>[!claim] How to invert the commutator
>$\log\left(\exp(x)\exp(y)\exp(x)^{-1}\exp(y)^{-1}\right) = [x,y]$ to third order (by which we mean $O(x^3, x^2y, xy^2, y^3)$).
>^Commutator-Inverse

>[!idea]
>This makes sense because everything is analytic and $x,y\in\fg$ are vectors, so the LHS can be Maclaurin expanded...

>[!proof]-
>You can just expand. Start with
>$$
>	\exp(x + y + \frac12[x,y] + O(\dots))\exp(-x - y + \frac12[x,y] + O(\dots))
>$$
>which yields
>$$
>	\exp([x,y] + O(\dots))
>$$
>This is clear; everything cancels and the only possible contribution is $[x + y, -x-y] = 0$.