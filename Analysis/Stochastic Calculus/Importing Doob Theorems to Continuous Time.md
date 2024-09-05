Recall [[Discrete Doob's Maximal Inequalities]], [[Discrete Doob's Maximal Inequalities|Doob's Lp Inequality]], and [[Doob's upcrossing inequality]] (all of which reduced to the super-martingale case). We can import them all immediately to the cadlag setting, in the following way:
- Write $\mathbb{D}_n = 2^{-n}\ZZ$ and $\mathbb{D} = \bigcup \mathbb{D}_n$.
- For any cadlag random process $X$, let $X^* = \sup_{t\geq 0} \abs{X_t}$ and $X^{(n)*} = \sup_{t\in \mathbb{D}_n} \abs{X_t}$. By the cadlag property, $X^{(n)}\to X^*$ (pointwise) as $n\to \infty$.
- Then, cadlag martingales $X$ turn to discrete-time martingales $(X_t)_{t\in \mathbb{D}_n}$ for the filtrations $(\FFF_t)_{t\in \mathbb{D}_n}$, ditto for half-martingales. In the limit, all of the preceding identities hold verbatim.

Nobody cares about Doob's upcrossing inequality though. The whole point of that guy is to launch off this chain of analysis that shows [[super-martingales are naturally cadlag]].