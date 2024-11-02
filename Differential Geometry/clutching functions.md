If $p:E\to X$ is a [[Vector Bundle|vector bundle]], then $X$ has an open cover $\{U_\alpha\}$; each one trivializes as above via a diffeomorphism $$g_\alpha: p^{-1}(U_\alpha)\to U_\alpha \times k^n$$
These are basically just coordinate charts, so they have transition maps. These are called ==**clutching functions**== in the literature:
$$
	h_{\alpha\beta}: U_\alpha\cap U_\beta\to \GL_n(k)
$$
(which is holomorphic if $E$ is a holomorphic bundle). These satisfy some obvious consistency conditions:
1. $h_{\alpha\beta}(x) = h_{\beta\alpha}(x)^{-1}$.
2. $h_{\alpha\beta}(x)\circ h_{\beta\gamma}(x) = h_{\alpha\gamma}(x)$ on $U_\alpha\cap U_\beta \cap U_\gamma$.

Thus, we have the following constructive definition:

>[!definition] Constructive Vector Bundle.
>Start from a disjoint union $\bigsqcup_\alpha U_\alpha \times k^n$, and identify points according to
>$$
>	h_{\alpha\beta}:(x,v)\in U_\beta \times K^n \sim (x, h_{\alpha\beta}(x)v)\in U_\alpha \times K^n
>$$

Of course, this non-constructive definition is morally wrong, and works for non-linear fiber bundles too.