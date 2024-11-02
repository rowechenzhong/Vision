---
aliases:
  - CTST
  - ST
  - Stopping time
  - stopping time
  - stopping times
---
This is just a usual [[Stopping Time]]. A random variable $T:\Omega\to [0,\infty]$ is a ==**stopping time**== if $\{T\leq t\}\in \FFF_t$ for all $t\geq 0$. For a stopping time $T$,$$\FFF_T = \{A\in \FFF_\infty: A\cap \{T\leq t\}\in \FFF_t,\quad \forall t\geq 0\}.$$Just like in the finite case, $\FFF_T$ stores all information we know given we have stopped.

Next up, the "result process" $X_T(\omega) = X_{T(\omega)}(\omega)$, and left undefined if $T(\omega) = \infty$ and $X_t(\omega)$ does not converge as $t\to \infty$. Finally, the ==**stopped process**== $X^T_t(\omega) = X_{T(\omega)\land t}(\omega)$.

A thing unique to continuous time is that, even if $T$ is not a stopping time of $\FFF_t$, it might still be a stopping time of $\FFF_{t+}$. Observe $T$ is a stopping time of $\FFF_{t+}$ iff $\{T < t\}\in \FFF_t$ for all $t > 0$. We then write
$$\FFF_{T+} = \{A\in \FFF_\infty: A\cap \{T < t\}\in \FFF_t,\quad \forall t> 0\}$$

See [[Elementary Properties of Continuous Stopping Times]]