---

aliases:
  - centered Gaussian space
---

>[!definition] (Centered) Gaussian Space
>This is a closed linear subspace of $L^2$ containing **only gaussian variables**.

>[!idea]
>Consider $L^2(\Omega, \FFF, \PP)$. This is a Hilbert space with inner product$$\braket{X, Y} = \EE[XY].$$ This is the ambient space of which our GS is a subspace.

>[!idea]
>This is very tight. Being a GRV is a statement about the distribution, agnostic to the mapping from $\Omega$. Adding two GRVs will generically not result in a GRV. As such, the following example is essentially the most general example of a GRV.

>[!example]
>If $X$ and $Y$ are $1$-dimensional GRV, $Span(X,Y)$ form a GS iff $(X,Y)$ is JG.

>[!idea]
>In the finite-dimensional case, I think all GS are made by the following construction.

>[!example]
>Fix $Z\sim N(0, \Sigma)$ with full-rank $\Sigma$. For $v\in \RR^n$, set $Gv = \braket{Z, v}$; then $G$ is a linear map from $\RR^d$ to a GS. Notably,$$\EE[\braket{Gu, Gv}] = \braket{\sqrt{\Sigma}u, \sqrt{\Sigma} v} = u^\top \Sigma v.$$
>If $\Sigma = \id$, then $G$ is an isometry.

> [!claim] Orthonormal GS $\iff$ independent
> Let $(H_\alpha)_{\alpha \in I}$ be a *set* of linear subspaces of a GS $H$. The $\sigma$-algebras $(\sigma(H_\alpha))_{\alpha \in I}$ are mutually independent iff the subspaces $H_\alpha$ are pairwise orthonormal. 

This is proved by [[Gaussian Random Variable#^claim-GRV-independent-diagonal]].


# Projections

>[!claim] Conditional expectation among GRV $\iff$ orthogonal projection of GS

Suppose $\begin{pmatrix}X\\Y\end{pmatrix}\sim N\left( \begin{pmatrix}0\\0\end{pmatrix}, \begin{pmatrix}a & b \\ b & c\end{pmatrix}\right)$. What is the law of $Y$ given $X$? The ambient GS is $H = span(X,Y)$.

Well, $Y = Y^\parallel + Y^\perp$, where $Y^\parallel\in span(X)$ and $Y^\perp \perp span(X)$, such that $Y^\parallel$ is the orthogonal projection of $Y$ onto $span(X)$. We compute that $Y^\parallel = \frac{b}{a} X$ and $Y^\perp = Y - \frac{b}{a} X$.

Thus um $Y | X \sim N(\frac{b}{a} - X, c - \frac{b^2}{a})$.

### Projections onto arbitrary things

>[!claim]
>Suppose $H\subset L^2(\Omega, \FFF, \PP)$ is a gaussian space and $K\subset H$ is a closed linear subspace. If $X\in H$, then $X | \sigma(K) \sim N(proj_K(X), \EE[X - proj_k(X)]^2)$.

>[!idea]
>For general non-gaussian $X$ and subset $K\subset L^2$, it doesn't make sense to write $X | \sigma(K)$. Instead, you write $\EE[X | \sigma(K)] = proj_{K'}(X)$ where $K' = L^2(\Omega, \sigma(K), \PP)$.
>
>For example, $K = span(Y)$ v.s. $K' = \{f(Y): f \text{ is a measurable function}\}$.