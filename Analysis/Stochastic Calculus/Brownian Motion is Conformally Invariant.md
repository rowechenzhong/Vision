Let $Z = X + iY$ be a standard BM in $\CC = \RR^2$ and $f:\CC\to \CC$ be conformal i.e. holomorphic. It's immediately obvious that $f(Z) = U + iV$ obeys $$
df(Z)_t = f'(Z) dZ_t
$$because of [[Ito Formula|Ito's Formula]]. The second-order term vanishes because holomorphic maps are harmonic. In addition, $f'(Z)$ is obviously an orthogonal matrix scaled by $\abs{f'(Z)}$. By the [[Braket Chain Rule]], $$d\braket{U,U}_t = \frac{\pa U}{\pa X}\frac{\pa U}{\pa X}d\braket{X,X}_t + \frac{\pa U}{\pa Y}\frac{\pa U}{\pa Y}d\braket{Y,Y}_t = \abs{f'(Z)}^2dt =  d\braket{V,V}_t,\qquad d\braket{U,V}_t = \frac{\pa U}{\pa X}\frac{\pa V}{\pa X}d\braket{X,X}_t + \frac{\pa U}{\pa Y}\frac{\pa V}{\pa Y}d\braket{Y,Y}_t = 0$$
[[Continuous Martingales are Time-Changed Brownian Motion]]. Hence, allowing $A_t = \int_0^t \abs{f'(Z)}^2 dt$, there exist standard BMs $\tilde{U}_t$ and $\tilde{V}_t$ such that $U_t = \tilde{U}_{A_t}$ and $V_t = \tilde{V}_{A_t}$.

Finally, because $d\braket{U,V}_t = 0$, $\braket{\tilde{U},\tilde{V}} = 0$ as well; this is immediate by the mesh characterization. Hence by [[Levy's Characterization of Brownian Motion]], we conclude that $(\tilde{U},\tilde{V})$ is a standard $2$-dimensional Brownian Motion!

Very cool.

>[!idea] This doesn't work for $d > 2$.