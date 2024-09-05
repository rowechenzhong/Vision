Let's get some intuition. You're a gambling addict who's flipping coins for a dollar, but you pay a cent every time you play. This is a supermartingale; it has negative drift term. The basic idea is that if you weigh the coin to win more often, you can turn yourself into a martingale. Not that deep!

Suppose I've got a semi-martingale like $B_t - t$. This guy drifts downwards. We're going to try to turn it into a CLM by changing the probability measure from $\PP$ to $\QQ$.

>[!idea] Stupid observation
>The notion of a FVP does not depend on the probability measure, unlike a CLM. Also, $\braket{X,Y}$ has a mesh approximation which is measure-agnostic (assuming mutual AC). Hence, we will be sliding FVP's across $\PP$ to $\QQ$, where the definition of a CLM will change.

# Setup

Alright, let $(\Omega, (\FFF_t), \PP)$ be a right-continuous complete filtered probability space. Let $\QQ$ a probability measure on $(\Omega, \FFF)$ which absolutely continuous with respect to $\PP$ on $\FFF_\infty$. Let's figure out what $\QQ$ looks like at a fixed finite time! For every $t\in [0,\infty]$, our probability measure on $\FFF_t$ is $\PP\big\vert_{\FFF_t}$, and we can construct a [[Analysis/Probability/Radon-Nikodym|Radon-Nikodym]] derivative $D_t = \frac{d\QQ}{d\PP\big\vert_{\FFF_t}}$ which is defined $\PP\big\vert_{\FFF_t}$-almost surely.

>[!claim]
>$D$ is a UI martingale. Its [[super-martingales are naturally cadlag|cadlag modification]] satisfies $$D_T = \frac{d\QQ}{d\PP\big\vert_{\FFF_T}}.$$
>
>If we also assume that $\PP$ is absolutely continuous wrt $\QQ$ on $\FFF_\infty$, then $\PP$-almost surely, $\inf_{t\geq 0} D_t > 0$.

>[!proof]- Boring
> $D$ is like, *obviously* a UI martingale:$$\EE_\PP[\id_A D_t] =\EE_\PP[\id_A\EE_\PP[D_\infty | \FFF_t]].$$
> Then, optional stopping theorem holds, so $\EE_\PP[\id_A D_\infty] = \EE_\PP[\id_A D_T]$ for all $A\in \FFF_T$, and we get the claim. The proof of the last part is not interesting.

Okay, now, let's cook. Let $\PP$, $\QQ$ be mutually AC on $\FFF_\infty$ from now on. We also assume that $D_t$ actually has continuous sample paths from now on. In this case, $D_t^{-1}$ also has continuous sample paths, and $D_t^{-1} = \frac{d\PP}{d\QQ\big\vert_{\FFF_t}}$ as you would expect.

>[!claim] XD
>Given adapted path-continuous $X$ and stopping time $T$, $(XD)^T$ is a martingale under $\PP$ iff $X^T$ is a martingale under $\QQ$.

It suffices to show one direction by symmetry. This is essentially obvious, and one can write out the rescaling argument. Thus, if $XD$ is a CLM under $\PP$, then $X$ is a CLM under $\QQ$! We can rewrite this with Ito's formula:

>[!theorem] Girasanov
>$\PP$ and $\QQ$ are mutually AC, and $D_t = \frac{d\QQ}{d\PP\big\vert_{\FFF_t}}$ is required to have continuous sample paths.
>Let $L$ be the unique CLM such that $D_t = \EEE(L)_t$. For any CLM $M$ under $\PP$, $\tilde{M} = M - \braket{M,L}$ is a CLM under $\QQ$!

# Interpretation

First of all, the class of CSMs under $\PP$ and $\QQ$ are the same. Any CSM $X = M + A$ on $\PP$ is the CSM $\left(M - \braket{M,L}\right) + A + \braket{M,L}$ on $\QQ$. Let's go ahead and call the mapping $M\to \tilde{M}$, $\GGG_\PP^\QQ$. 

Also, note that the $D_t^{-1} = \EEE(-\tilde{L})_t$ where $\tilde{L}$ is the corresponding CLM under $\QQ$, $L - \braket{L,L}$. Basically, the CLM parts are always going to be the same; we're always sliding FVP's across $\PP$ and $\QQ$ in order to enforce properties. It is then immediate that the mappings $\GGG^\QQ_\PP$ and $\GGG_\QQ^\PP$ are inverses.

Also, $\GGG_\PP^\QQ$ commutes with the stochastic integral. Indeed, it suffices to consider the integral against CLMs, because the LBPP-FVP integral is measure-agnostic; a quick computation suffices.

Finally, a quick Levy calculation shows $(\FFF_t)$-BMs are mapped to $(\FFF_t)$-BMs under $\QQ$.

# Usage

Often, we start with some CLM $L$ such that $L_0 = 0$ and $\braket{L,L}_\infty < \infty$ AS on $\PP$ and want to create a $\QQ$ using $D_t = \EEE(L)$. This works iff $\EEE(L)$ is a continuous UI martingale.

>[!idea]- We're already pretty close.
>$L_\infty$ exists and is finite AS. Thus, $\EEE(L)_t$ is a supermartingale which converges AS to $\EEE(L)_\infty = \exp\left(L_\infty - \frac12 \braket{L,L}_\infty\right)$ which is finite and nonzero AS, thus the $\QQ$ with density $\EEE(L)$ on $\PP$ is a valid probability measure which is mutually AC. By Fatou's Lemma,
> $$
> \EE\left[\lim\inf_t \EEE(L)_t\right]\leq \lim\inf_t \EE\left[\EEE(L)_t\right] \leq \EE\left[\EEE(L)_0\right] = 1.
> $$
> Thus, if $\EE\left[\EEE(L)_\infty \right] = 1$ exactly, then $\EEE(L)$ is a UI martingale (and this is clearly only if).

>[!claim] Novikov's Criterion and Kazamaki's Criterion
>Let $L$ be a CLM such that $L_0 = 0$. Then,
>1. $\EE\left[\exp \frac12 \braket{L,L}_\infty\right] < \infty$.
>2. $L$ is a UI martingale, and $\EE\left[\exp \frac12 L_\infty\right] < \infty$.
>3. $\EEE(L)$ is a UI martingale.
>
>$(1)\implies (2) \implies (3)$.