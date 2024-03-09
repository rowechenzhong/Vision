---

aliases:
  - centered Gaussian space
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

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