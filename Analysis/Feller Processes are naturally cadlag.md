> [!idea]- Reminder of Assumptions
> Let $E$ be a metrizable locally compact topological space which is countable at infinity, let $(\Omega, (\FFF_t)_{t\geq 0}, \PP)$ be a filtered probability space, and let $(Q_t)_{t\geq 0}$ be a Feller semigroup.

Let $\WFF_t$ be the completed right-continuous filtration $\WFF_t = \FFF_{t+} \lor \sigma(\mathscr{N})$ where $\mathscr{N}$ are the null sets of $\FFF_\infty$.

>[!theorem]
>Any $\FFF_t$-Feller process $(X_t)_{t\geq 0}$ with semigroup $(Q_t)_{t\geq 0}$ has a cadlag modification $\tilde{X}$ adapted to $\WFF_t$ which is a Feller process with semigroup $Q$.

Proof is boring and omitted. The main idea is that for every non-negative $h\in C_0$, $e^{-\lambda t}R_\lambda h(X_t)$ is a super-martingale. Super-martingales are naturally cadlag.