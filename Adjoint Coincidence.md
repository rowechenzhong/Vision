For $x\in \fg$, we can define the linear map $\ad_x:\fg\to \fg$ via $\ad_x(y) = [x,y]$. The claim is that this is actually [[Various Adjoint maps|the same adjoint as before]].

>[!theorem] Adjoint Coincidence
>$\ad_x = \Ad_{\fg}(x)$.

>[!claim]
>$\log\left(\exp(x)\exp(y)\exp(x)^{-1}\exp(y)^{-1}\right) = [x,y]$ to third order (by which we mean $O(x^3, x^2y, xy^2, y^3)$).

>[!idea]
>This makes sense because everything is analytic and $x,y\in\fg$ are vectors, so the LHS can be expanded...

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

Let's just show this for general curves. Fix $x$ and $y$. Let $X(t)$ and $Y(s)$ be parameterized curves on $G$ such that $X(0) = Y(0) = 1$, $X'(0) = x$, and $Y'(0) = y$; we're just launching some curves out of $1$ in the $x$ and $y$ directions. Then,
$$
	[x,y] = \lim_{s,t\to 0} \frac{\log(X(t)Y(s)X(t)^{-1}Y(s)^{-1})}{ts}
$$
This is fine; let $x(t) = \log X(t)$ and $y(t) = \log Y(t)$; then by the claim
$$\begin{align*}
	\log\left(\exp(x(t))\exp(y(t))\exp(x(t))^{-1}\exp(y(s))^{-1}\right) &= [x(t), y(s)] + O(\dots)\\
	& = ts([x, y] + o(1))
	\end{align*}
$$
as $t,s\to 0$. This shows the stronger statement. Thus, for instance,
$$
	[x,y] = \lim_{s,t\to 0} \frac{\log(\exp(tx)\exp(sy)\exp(tx)^{-1}\exp(sy)^{-1})}{ts}
$$


Now, recall that
$$
Ad_{\fg}(x)(y) = \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=s=0}
$$
This is equal to
$$
\begin{align*}
Ad_{\fg}(x)(y) &= \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\exp(ty)^{-1}\right)\right|_{t=s=0}\\
&= \left.\frac{\der}{\der s}\left\{\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=0}\right.\\
&+ \left.\left. \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right\}_{t=0} \frac{\der}{\der t}\exp(ty)^{-1}\right|_{s=0}\\
&= \left.\frac{\der}{\der s}\left\{\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=0} - y\right\}\\
&= \Ad_\fg(x)(y)
\end{align*}
$$
Which... looks pretty familiar, lol. Nice lmao.