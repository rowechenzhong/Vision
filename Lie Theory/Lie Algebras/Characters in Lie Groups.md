---
aliases:
  - character
  - characters
---
The ==**character**== of a lie group, is defined, initially, exactly the same as that of a finite-dimensional representation $V$:$$\chi_V(g) = \Tr\big\vert_V(g).$$However, in the case of interest (semisimple lie algebras), we can say a lot about this character. In particular, fix a CSA $\hh\subset \fg$ and $h\in \hh$. Then,$$\chi_V(h) \equiv \chi_V(e^h) = \sum_{\mu\in P} \dim V[\mu] e^{\mu(h)}$$where $P$ is the weight lattice. By a massive abuse of notation, we then write$$\chi_V = \sum_{\mu \in P} \dim V[\mu] e^\mu,$$where $e^\mu$ is the analytic function on $\hh$ mapping $h\mapsto e^{\mu(h)}$. 

>[!idea] More abuse
>Consider the group algebra $\ZZ[P]$, which is just the free abelian group generated by $P$. There is an injective linear map from this space to the analytic functions on $\hh$, sending the generator $\lambda$ to $e^\lambda$. We thus regard $\ZZ[P]$ as a subspace of the analytic functions on $\hh$, and write $\chi_V\in \ZZ[P]$.

# Generalization

>[!idea]
>This section to extends the above definition to a larger regime where it makes sense, including infinite-dimensional vector spaces.

A set of weights is called ==**integrally bounded**== if is contained in the union of sets $\lambda^i - Q_+$ for a finite collection of weights $\lambda^1,\dots, \lambda^N\in P$.

>[!definition]
>The category $\mathcal{O}_\text{int}$ is the category of representations $V$ of $\fg$ with weight composition into finite-dimensional weight spaces $V = \oplus_{\mu\in P} V[\mu]$ such that $P(V)$ is integrally bounded.

As an illustrative example, all [[Verma Module|Verma modules]] with integral weight live in this category, and so do direct sums of such, and quotients of such. Notably, all weights have to be integral in this definition.

>[!idea]
>Usually, we add the condition that $V$ is a finitely-generated $U(\fg)$-module, i.e. it is literally a quotient of a direct sum of Verma modules. We won't do that here.

We can then extend the purely algebraic construction above. Specifically, let $\mathcal{R}$ be the ring of formal series $a = \sum_{\mu \in P} a_\mu e^\mu$, such that the set of nonzero $a_\mu$ is integrally bounded. Then, $\chi_V\in \mathcal{R}$ is defined by the above definition.

Clearly, $\chi_{V\otimes U} = \chi_V\chi_U$, and if $0\to X\to Y\to Z \to 0$ is a SES in $\mathcal{O}$, then $\chi_Y = \chi_X + \chi_Z$.

> [!example] Verma Modules and Weyl Denominators
> Let $V = M_\lambda$ be a [[Verma Module]]. As a vector space, $M_\lambda \cong U(\mathfrak{n}_-)v_\lambda$ and $U(\mathfrak{n}_-) = \bigoplus_{\alpha\in R_+} \CC[e_{-\alpha}]$. Thus,$$\chi_{M_\lambda} = \frac{e^\lambda}{\prod_{\alpha\in R_+} (1 - e^{-\alpha})}.$$Usually, one writes$$\chi_{M_\lambda} = e^{\lambda + \rho}{\Delta},\qquad \Delta = \prod_{\alpha\in R_+} (e^{\alpha/2} - e^{-\alpha/2}).$$where $\Delta$ is the ==**Weyl Denominator**==.

See:
- [[Sign Character]]
- [[Weyl Character Formula]]