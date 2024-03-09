A sequence of probability measures $\mu_n: n\in \NN$ on a metric space $E$ is *tight* if for all $\eps > 0$, there exists a compact set $K$ such that $\mu_n(E\setminus K)\leq \eps$ for all $n$.

>[!idea]
>In other words, the bulk of the $\mu_n$'s do not run off to the infinity. You just need to make sure you can always "draw a finite ball at the origin containing $1-\eps$ of each probability measure" (I'm picturing $\RR^d$).

> [!theorem] Prohorov
> If $\mu_n$ are tight, then there exists a subsequence $\mu_{n_k}$ which converges weakly to some probability measure $\mu$ on $E$.

>[!idea]
>This is sort of crazy. If $E$ is compact to begin with, the set of probability measures on $E$ is sequentially compact. It's a Arzelà–Ascoli type thing. Completely wild.