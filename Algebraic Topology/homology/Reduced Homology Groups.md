> [!problem]
> Suppose $X$ decomposes into path-connect components $\{X_\alpha\}$. Show that $H_n(X)$ is naturally isomorphic with the direct sum $\bigoplus_\alpha H_n(X_\alpha)$.

> [!solution]-
> A singular simplex has PC image, so $C_n(X)$ splits. $\pa_n$ respects this splitting, thus $H_n(X)$ does too.

>[!problem]
>Compute $H_0(X)$.

> [!solution]
> If $X$ is PC, $C_0(X)$ is $\bigoplus_{x\in X} \ZZ x$. For all spaces, $C_{-1}$ is defined to be $0$, thus $\pa_0 = 0$ and $\ker \pa_0 = C_0(X)$. We claim $\im \pa_1$ is exactly the kernel of $\eps: C_0(X)\to \ZZ, \sum_x n_x x\to \sum_x n_x$. This kernel lies in $\im \pa_1$, because $X$ is path-connected. This kernel contains $\im \pa_1$, by staring at its formula. Thus $H_0(X)\cong \ZZ$. If $X$ is not PC, then $H_0(X) \cong \bigoplus_\alpha \ZZ$.

>[!idea]
>This solution can be thought of as considering the unique $-1$-simplex with no vertices; then $\eps \equiv \pa_{-1}$.

>[!problem]
>Let $X$ be a point. Show $H_n(X) = 0$ for $n > 0$ and $H_0(X) = \ZZ$.

For these reasons, we like to define the ==**reduced Homology groups**== $\tilde{H}_n(X)$ which are the homology groups of the augmented chain complex ending $C_0(X) \stackrel{\eps}{\to} \ZZ\to 0$.