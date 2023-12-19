> [!theorem] Functions on Markov Chains are martingales
> Let $X$ be adapted on $E$. Then, $X$ is a MC with transition matrix $P$ iff for all bounded functions $f:E\to \RR$,$$M^f_n = f(X_n) - f(X_0) - \sum_{k = 0}^{n-1} ((P - I)f)(X_k)$$ is a martingale.

This is a good test of whether you understood notation. 

>[!problem] Prove it.

>[!solution]- Notation Shuffling
> Well, by telescoping, the martingale condition is iff$$\EE[f(X_{n+1}) \id_A] = \EE[(Pf)(X_n)\id_A]$$for all $A\in \FFF_n$ for all bounded functions $f$. By linearity, this is iff the above is true for all point functions $f(x) = \delta_{xy}$ and $A\subset \{X_n = x\}$ for some $x,y$. In this context, the statement becomes
> $$\PP(X_{n+1} = y \land \id_A) = \EE\left(p_{xy} \id_A\right)$$
> as desired.