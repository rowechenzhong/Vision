> [!theorem] Naturally Cadlag
> Assume that the filtration satisfies the [[Continuous Time Filtration|usual conditions]]. If $X$ is a super-martingale such that $t\mapsto \EE[X_t]$ is right-continuous, then $X$ has a modification with [[cadlag]] sample paths, which is also a $\FFF_t$-supermartingale.

Notably, all martingales admit cadlag modifications. The modification is $X_{t+}$ modulo a negligible set.

# Proof from Doob

Here are lemmas:

> [!claim] Left and Right limits
> Let $X$ be a supermartingale, and $D$ be a countable dense subset of $\RR_+$.
> 
> Then, the restriction to $D$ has right-limits and left-limits almost surely;
> $$X_{t+}(\omega) \equiv \lim_{s\downarrow t: s\in D} X_s(\omega),\qquad X_{t-}(\omega) := \lim_{s\uparrow t, s\in D} X_s(\omega).$$

>[!claim] Right limits are supermartingales, lol
>$X_{t+}\in L^1$ for every $t > 0$, and $X_t\geq \EE[X_{t+} | \FFF_t]$.
>
>If $t\mapsto \EE[X_t]$ is right-continuous, this is equality. $(X_{t+})$ is a supermartingale with respect to the filtration $\FFF_{t+}$.