> [!theorem] Doob Upcrossing
> Let $X$ be a [[Discrete-time Martingale|supermartingale]]. Let $U_n[a,b]$ be the number of [[upcrossings]] by $X$ including time $n$. Then,
> $$(b-a)\EE(U_n[a,b]) \leq \EE[(X_n - a)^-].$$

The most common application is to take the supremum of both sides to bound $U[a,b]$:$$(b-a)\EE[U[a,b]] \leq \sup_n \EE[(X_n - a)^-]$$
> [!idea] Why is this obvious?
> You cannot make money on a supermartingale. Consider the following strategy: if $X_t \leq a$, immediately buy one share if you have not already; if $X_t\geq b$, immediately sell your share if you own one. At $n$, you are forced to sell out if necessary; this is your only source of loss. The expected profit is at least $(b-a)\EE[U_n[a,b]]$, and the expected loss is at most $\EE[(X_n - a)^-]$.

> [!proof]- Smash with BOST
> Let's define $T_0 = n\land \inf \{i\geq 0: X_i \leq a\}$, and define recursively $S_i = n\land \inf\{i\geq T_i, X_i \geq b\}$, $T_i = n\land \inf\{i\geq S_{i-1}, X_i \leq a\}$. Check that$$X_{S_i} - X_{T_i} = \id_{U_n = i-1, X_{T_i} \leq a}\left(X_n - X_{T_i}\right) + \id_{U_n\geq i} \left(X_{S_i} - X_{T_i}\right)\geq \id_{U_n = i-1} (X_n - a)^- + \id_{U_n\geq i}(b - a),$$then cite $\EE[X_{S_i}]\geq \EE[X_{T_i}]$ and add.