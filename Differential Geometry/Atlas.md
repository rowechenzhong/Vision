An ==**atlas**== is a collection of [[locally homeomorphic|local charts]] $(U_\alpha, \phi_\alpha)_{\alpha \in A}$ such that $\bigcup_{\alpha\in A} U_\alpha = X$.

Observations:
- If $X$ is compact, then a finite atlas exists.
- There is always a *countable* atlas, because we defined manifolds to have a countable basis.

# Transition maps

The local charts in an atlas can overlap, and they need to agree whenever they do. If $(U, \phi)$ and $(V, \psi)$ are two charts such that $V\cap U \neq \emptyset$, then we have the ==**transition map**==
$$\phi\circ \psi^{-1} : \psi(U\cap V)\to \phi(U\cap V)$$
This is automatically a homeomorphism between open subsets in $\RR^n$. One can impose more properties on the manifold through properties of this transition map.