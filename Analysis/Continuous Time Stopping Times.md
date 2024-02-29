This is just a usual [[Stopping Time]]. A random variable $T:\Omega\to [0,\infty]$ is a ==**stopping time**== if $\{T\leq t\}\in \FFF_t$ for all $t\geq 0$. For a stopping time $T$,$$\FFF_T = \{A\in \FFF_\infty: A\cap \{T\leq t\}\in \FFF_t,\quad \forall t\geq 0\}.$$Just like in the finite case, $\FFF_T$ stores all information we know given we have stopped.

Next up, the "result process" $X_T(\omega) = X_{T(\omega)}(\omega)$, and left undefined if $T(\omega) = \infty$ and $X_t(\omega)$ does not converge as $t\to \infty$. Finally, the ==**stopped process**== $X^T_t(\omega) = X_{T(\omega)\land t)}(\omega)$.

See [[Elementary Properties of Continuous Stopping Times]]