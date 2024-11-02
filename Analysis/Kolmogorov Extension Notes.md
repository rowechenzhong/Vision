---
aliases:
  - KET
---
These are an extended set of notes on the [[Kolmogorov Extension]] theorem, in an attempt to gain a deeper understanding.

# The Extension Problem

Consider a set $X$, and a [[net]] $\{\Sigma_\nu: \nu \in J\}$ of $\sigma$-algebras on $X$ directed by inclusion. (For any $\Sigma_\mu, \Sigma_\nu$, there is some $\Sigma_\gamma \supset \Sigma_\mu, \Sigma_\nu$). Let $\{\PP_\nu: \nu \in J\}$ be a family of probability measures on $\Sigma_\nu$.

>[!definition]
>The family $\{\PP_\nu\}$ is ==**Kolmogorov consistent**== if $\Sigma_\nu \subset \Sigma_\mu$ implies $\PP_\nu\big\vert_{\Sigma_\mu} = \PP_\mu$. If so, $\{(\Sigma_\nu, \PP_\nu): \nu \in J\}$ is called a ==**Kolmogorov Net**==.

We assume so in the sequel. Let $A = \cup_{\nu \in J} \Sigma_\nu$; this is an algebra.

>[!idea] The Kolomogorov Extension Problem
>Is there a probability measure $\PP$ on $A$ that simultaneously extends every $\PP_\nu$?

There is only one possible candidate, which is $\PP(E) = \PP_\nu(E)$ on $E\in \Sigma_\nu$; these are consistent by definition. It is clear that $\PP$ is non-negative, $\PP(X) = 1$, and $\PP$ is finitely additive. Thus, we reduce to showing that $\PP$ is **countably additive**. If we can show this, $\PP$ is the ==**Kolmogorov extension**== of $\PP_\nu$ to $A$, and then [[Caratheodory extension Theorem]] bootstraps to $\sigma(A) = \sigma(\Sigma_\nu: \nu \in J)$.

By the [[Compact Class Bootstrap]], we have the following result:

>[!theorem] Abstract KET
>Let $\{(\Sigma_\nu, \PP_\nu):\nu\in J\}$ be a Kolmogorov net on $X$. Suppose there is a compact class $\mathscr{C}$ such that
>$$\forall \nu \in J \quad \forall E\in \Sigma_\nu,\qquad \PP_\nu(E) = \sup\left\{\PP_\nu(C): C\subset E, C\in \mathscr{C}\cap \Sigma_\nu\right\}.$$
>Then, there is a unique Kolmogorov extension to $\sigma\left(\bigcup_{\nu\in J} \Sigma_\nu\right)$.

Now, if you compute enough things, you obtain the usual [[Kolmogorov Extension]].

>[!todo] Finish this lol