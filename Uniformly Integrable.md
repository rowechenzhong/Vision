Let $X$ be an [[constructing the Lebesgue Integral|integrable]] random variable. Set
$$
	I_X(\delta) = \sup\left\{\EE[\abs{X}\id_A]: A\in \FFF, \PP(A)\leq \delta\right\}
$$
Then $I_X(\delta)\downarrow 0$ as $\delta\downarrow 0$.

> [!proof]- This is clear
> Otherwise, $\exists \eps >0$ and $A_n\in \FFF$ such that $\PP(A_n)\leq 2^{-n}$ and $\EE(\abs{X}\id_{A_n}) \geq \eps$ for all $n$; by Borel-Cantelli $\PP(A_n \ \text{i.o.}) = 0$. We now manually arrange for a $\lim\sup$ situation: note that for all $n$,
> $$
> 	\eps\leq \EE\left\{\abs{X}\id\left(\bigcup_{m\geq n}A_m\right)\right\}
> $$
> The RHS is a series of decreasing functions in $n$ which are bounded by the integrable function $\abs{X}$ and converge to $\abs{X}\id(A_n\ \text{i.o.})$... which integrates to $0$. Contradiction.

Let $\mathcal{X}$ be a family of random variables. If we define $I_\mathcal{X}$ to supremum over $\mathcal{X}$ as well, in general $I_\mathcal{X}(\delta)$ will not converge to $0$.

For $1\leq p \leq \infty$, $\mathcal{X}$ is ==**bounded in $L^p$**== if $\sup_{X\in \mathcal{X}} \norm{X}_p < \infty$. $\mathcal{X}$ is ==**uniformly integrable**== or UI if $\mathcal{X}$ is bounded in $L^1$ and $I_\mathcal{X}(\delta)\downarrow 0$ as $\delta\downarrow 0$.

Note that if $\mathcal{X}$ is bounded in $L^p$ for $p \in (1,\infty)$, then $\mathcal{X}$ is UI; on the flip side, $n\id(0, \frac1n)$ is in $L^1$ yet not UI.

For any integrable random variable $Y$, the set $$\mathcal{X} = \{X: X \text{ is a random variable}, \abs{X}\leq Y\}$$ is UI.

>[!claim] Alternative Characterization
>$\mathcal{X}$ is UI iff $$
>	\sup\left\{ \EE(\abs{X}\id_{\abs{X}\geq K} ) \right\}: X\in \mathcal{X}\to 0
>$$ as $K\to \infty$.

>[!proof] Boring, TODO

This was all setup for [[L1 Convergence Theorem]].