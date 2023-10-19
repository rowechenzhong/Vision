For $x\in \fg$, the [[Commutator|commutator]] defines a linear map $\ad_x:\fg\to \fg$ via $\ad_x(y) = [x,y]$. The claim is that this is actually [[Various Adjoint maps|the same adjoint as before]]; this is a key part of the bridge, and can be boxed as an [[interface]].

>[!theorem] Adjoint Coincidence
>$$
>	[x,y] = \left.\frac{\der}{\der t}\right|_{t = 0} \Ad_{\exp(xt)}(y)
>$$
# Proof

>[!claim] Express the commutator in terms of limits
> Fix $x$ and $y$. We launch two curves out of $1$ in the $x$ and $y$ directions: let $X(t)$ and $Y(s)$ be parameterized curves on $G$ such that $X(0) = Y(0) = 1$, $X'(0) = x$, and $Y'(0) = y$. 
> 
> Then,
>$$
> 	[x,y] = \lim_{s,t\to 0} \frac{\log(X(t)Y(s)X(t)^{-1}Y(s)^{-1})}{ts}
> $$
> 
> Thus, for instance,
> $$
> 	[x,y] = \lim_{s,t\to 0} \frac{\log(\exp(tx)\exp(sy)\exp(tx)^{-1}\exp(sy)^{-1})}{ts}
> $$

>[!proof]- Not that deep.
> Recall [[How to invert the commutator]].
> Let $x(t) = \log X(t)$ and $y(t) = \log Y(t)$. Then,
> $$\begin{align*}
> 	\log\left(\exp(x(t))\exp(y(t))\exp(x(t))^{-1}\exp(y(s))^{-1}\right) &= [x(t), y(s)] + O(\dots)\\
> 	& = ts[x, y] + o(1)
> 	\end{align*}
> $$
> as $t,s\to 0$.

Recall that
$$
Ad_{\fg}(x)(y) = \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=s=0}
$$
This is equal to
$$
\begin{align*}
Ad_{\fg}(x)(y) &= \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\exp(ty)^{-1}\right)\right|_{t=s=0}\\
&= \left.\frac{\der}{\der s}\left\{\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=0}\left.\exp(ty)\right|_{t=0}\right.\\
&+ \left.\left. \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right\}_{t=0} \frac{\der}{\der t}\exp(ty)^{-1}\right|_{s=0}\\
&= \left.\frac{\der}{\der s}\left\{\Ad_G(\exp(sx))(y) \right. - y\right\}\\
&= \Ad_\fg(x)(y)
\end{align*}
$$