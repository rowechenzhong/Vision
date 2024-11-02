---
aliases:
  - measure-preserving transformation
---
Let $(E,\mathcal{E}, \mu)$ be a measure space. A measurable $\theta:E\to E$ is a ==**measure-preserving transformation**== if
$$
	\mu\circ \theta^{-1} = \mu
$$
on $\mathcal{E}$.

Then, given $\theta$, a measurable $A$ is ==**invariant**== if $\theta^{-1}(A) = A$. The set of invariant sets form a $\sigma$-algebra, denoted $\mathcal{E}_\theta$. A measurable function $f$ is invariant if and only if it is $\mathcal{E}_\theta$-measurable.

We say that $\theta$ is ==**ergodic**== if $\mathcal{E}_\theta$ contains only sets of measure $0$ and their complements.

> [!proof]- Verification
> $E\subset \mathcal{E}_\theta$ because $\theta^{-1}(E) = E$. Suppose $A\in \mathcal{E}_\theta$; then
> $$\theta^{-1}(E\setminus A) = \theta^{-1}(E)\setminus \theta^{-1}(A) = E\setminus A\implies E\setminus A\in \mathcal{E}_\theta.$$
> Finally, if $A_1,\dots A_n\in \mathcal{E}_\theta$, then
> $$
> 	\theta^{-1}\left(\bigcup_{i} A_i\right) = \bigcup_{i}\theta^{-1}\left(A_i\right) = \bigcup_{i} A_i
> $$
> as desired.

>[!example] Irrational Rotation
>Over $\RR/\ZZ$, $x\to x + \theta$ for irrational $\theta$ is ergodic.

>[!example] Bernoulli Shift
>Over $\RR^\NN$, sending $(x_1,x_2,\dots)\to (x_2,x_3,\dots)$ is ergodic.

# Problems

Show that if $\theta$ is ergodic and $f\to \RR$ is invariant, then $f = c$ almost everywhere for some constant $c$.