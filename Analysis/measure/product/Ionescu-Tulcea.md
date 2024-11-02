> [!theorem]
> Let $(\Omega_\alpha, \FFF_\alpha, \PP_\alpha)_{\alpha \in I}$ be probability spaces. There is a unique probability measure $\PP$ on the [[product space]] $(\prod_{\alpha\in I} \Omega_\alpha, \bigotimes_{\alpha\in I} \FF_\alpha)$ such that $\PP_J = \bigotimes_{\alpha \in J} \PP_\alpha$ for any finite $J$.

In other words, everything we desire of our [[product measure]] is possible.

# Proof

>[!part] Context
>Begin with the generating algebra
>$$ \AAA_0 = \{(\pi_J)^{-1}(E_J) = E_J\times \Omega_{I\setminus J}: \abs{J} < \infty, E_J\subset \FFF_J\}$$
> As desired, we define
> $$ \PP(E_J \times \Omega_{I\setminus J}) = \left( \bigotimes_{\alpha \in J} \PP_\alpha\right)(E_J)$$
> We now wish to show that $\PP$ is a pre-measure; this concludes.

> [!part]- Well-defined and Finitely additive (Boring, skip)
> This just means that there's multiple ways to describe a set as $E_J \times \Omega_{I\setminus J}$, say if $E_J$ contains a few $\Omega$'s. But then, by box product measure, this just means we multiply by $1$ a few times.
> 
> This is simple, because everything is finite. If
> $$ E_{J_1} \times \Omega_{I\setminus J_1} \sqcup \dots \sqcup E_{J_n} \times \Omega_{I\setminus J_n} = E_J \times \Omega_{I\setminus J}$$
> then we can just consider the $J_{\text{max}} = J_1\cup J_2\cdots \cup J$; by well-definedness we can assume all the $J_i$'s are this $J_{\text{max}}$, and then this follows because $\bigotimes_{\alpha \in J_{\text{max}}} \PP_\alpha$ is a valid measure.

The interesting part:

> [!claim] Vanishing on Vanishing sequences
> We wish to show $\PP(B_n)\downarrow 0$ for all sequences $B_n\in \AAA_0$ such that $B_i\downarrow \emptyset$.

> [!proof]
> Observe that this whole sequence has at most countable strength. There exist finite index sets $J_i\uparrow J$ where $J$ is countable such that $B_i = E_{J_i} \times \Omega_{I\setminus J_i}$. So we can write
> $$ B_n = E_n \times \Omega_{J\setminus J_n} \times \Omega_{I\setminus J}$$
> and forget about $\Omega_{I\setminus J}$.
> 
> We now let $\PP^i = \bigotimes_{\alpha\in J_{i}\setminus J_{i-1}} \PP_i$; these are finite box products over $\Omega_{J_i \setminus J_{i-1}}$, so we don't care. Alternatively one can integrate over $J_{i}\setminus J_{i-1}$ integrals in each step in the below proof; everything still works.
> 
> The main tactic now is to draw the following triangular grid:
> 
> | | | | | |
> |-|---|---|---|---|
> | $\PP(\Omega) = 1$ | | | | |
> | $\PP(B_1) = \int \id_{E_1} \der \PP^1$ | $\id_{E_1}$ | | | |
> | $\PP(B_2) = \int \int \id_{E_2} \der \PP^2 \der \PP^1$ | $\int \id_{E_2} \der \PP^2$ | $\id_{E_2}$ | | |
> | $\PP(B_3) = \int \int \int \id_{E_3} \der \PP^3 \der \PP^2 \der \PP^1$ | $\int \int \id_{E_3} \der \PP^3 \der \PP^2$ | $\int \id_{E_3} \der \PP^3$ | $\id_{E_3}$ | |
> | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$
> | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $\dots$
> 
> Observe that:
> - Each column (which possibly contains functions) is monotonically decreasing, bounded, and nonnegative.
> - Each column thus admits a limit, which we have written as $g_i$ in the bottom row.
> - Row $i$ is the integral of row $i+1$ over $\PP^{i}$.
> - This holds even for the bottom-most row, because we may interchange the limit and integral by [[Convergence properties of Lebesgue Integral#^Dominated-Convergence|Dominated Convergence]].
> 
> Now: if $0 < \eps = g_1 = \int g_2(\omega_1) \der \PP^1$, then there must exist a value of $\omega_1\in \Omega_{J_1}$ such that $\eps \leq g_2(\omega_1) = \int g_2(\omega_1, \omega_2) \der \PP^2$. Then, there must exist a pair $(\omega_1, \omega_2)\in \Omega_{J_2}$ such that $\eps \leq g_2(\omega_1, \omega_2)$. By induction, we determine a sequence $\omega_i \in \Omega_{J_i\setminus J_{i-1}}$ such that $g_n(\omega_1,\dots \omega_n) \geq \eps$.
> 
> We now pass everything back up the columns, which are nondecreasing upwards, to obtain that $\id_{B_n}(\omega_1\dots \omega_n) = 1$. Thus $(\omega_1,\omega_2,\dots)\in \Omega_J$ lies in $\bigcap B_i$, contradicting our assumption.