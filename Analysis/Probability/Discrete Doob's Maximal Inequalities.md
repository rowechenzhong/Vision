---
aliases:
  - Doob's Maximal Inequalities
  - Doob
---
The process $X^*_n = \sup_{k\leq n} \abs{X_k}$ is a good measure of regularity. Set $X^* = \sup_{n\geq 0}\abs{X_n}$. These guys are just increasing envelopes bounding $X$, and can themselves be bounded. All of these are, philosophically, an extension of [[Basic Inequalities|Markov's Inequality]] to the Martingale case. See also the closely related [[Discrete Doob's Lp Inequalities|Lp Inequalities]].

There are three variants of this which apply to subtlely different situations.

> [!thm] 676 Maximal Inequality
> If $X$ is a submartingale (not necessarily non-negative), then $\lambda \PP(X^*_n \geq \lambda)\leq \EE[\abs{X_0} + 2\abs{X_n}]$.

>[!idea]
>This is kind of cool, because the RHS is a function of solely $X_n$ and $X_0$.

> [!proof]- Markov inspired bash
> This one takes a lot more effort to prove, because without the non-negative condition, you care about if the submartingale goes down more than you expect.
> 
> Let $T = \inf\{k\geq 0: \abs{X_k}\geq \lambda\}$ be the stopping time under consideration. This is equal to $\infty$ if this never occurs; we won't be using OST, because $\abs{X_t}$ isn't a submartingale or anything. The proof proceeds similarly to [[Basic Inequalities|Markov's Inequality]]:$$
> \begin{align*}
> 	\lambda \PP(X^*_n\geq \lambda) &= \lambda \sum_{t =0}^n \PP(X_t\geq \lambda, T \geq t) + \PP(X_t\leq -\lambda, T \geq t)\\
> 	&\leq \sum_{t =0}^n \EE(X_t \id_{X_t\geq \lambda, T \geq t}) - \EE(X_t\id_{X_t\leq -\lambda, T \geq t})\\
> 	&= \sum_{t =0}^n \EE(X_t \underbrace{\id_{T\geq t}}_{\in \FFF_{t-1}}) - \EE(X_t \id_{X_t < \lambda, T \geq t}) - \EE(X_t\id_{X_t\leq -\lambda, T \geq t})\\
> 	&\leq \sum_{t =0}^n \underbrace{\EE(X_{t-1} \id_{T\geq t})}_{\text{Markov}} - \EE(X_t \id_{\abs{X_t} < \lambda, T \geq t}) - 2\EE(X_t\id_{X_t\leq -\lambda, T \geq t})\\
> 	&\leq \sum_{t =0}^n \EE(X_{t-1} \id_{T\geq t}) - \EE(X_t \id_{T \geq t + 1}) - 2\underbrace{\EE(X_n\id_{X_t\leq -\lambda, T \geq t})}_{\text{Markov}}\\
> 	&=\EE[X_0] - \EE[X_n\id_{T = \infty}] - 2\EE[X_n\id_{T\leq n, X_T \leq -\lambda}]\\
> 	&\leq \EE[X_0] + 2\EE[\abs{X_n}]
> \end{align*}
> $$

# Weak Forms

>[!thm] Wikipedia Maximal Inequality
>Let $X$ be a submartingale (not necessarily non-negative). For all $\lambda \geq 0$, let $E = \max_{1\leq i\leq n}X_i \geq \lambda$. 
>$$\lambda \PP\left(E\right)\leq \EE[X_n\id_E] \leq \EE[X_n^+]$$

>[!proof]- Easy
>Let $E_i$ be the event $i =\inf\{j: X_j \geq \lambda\}$ and $E = \bigcup E_i$ be the desired. Then,$$\begin{align*}\lambda \PP(E) &= \lambda \sum \PP(E_i)\leq \sum \EE[X_i\id_{E_i}]\\&\leq \sum \EE[X_n\id_{E_i}] = \EE[X_n\id_E]\leq \EE[X_n^+]\end{align*}$$as desired.

>[!theorem] 675 Maximal Inequalities
>Let $X$ be a martingale or non-negative submartingale. Then, for all $\lambda \geq 0$,
> $$\lambda\PP(X^*_n\geq \lambda)\leq \EE\left(\abs{X_n} \id_{X^*_n\geq \lambda}\right).$$
> This immediately implies
> $$\lambda \PP(X^* \geq \lambda) \leq \sup_{n\geq 0} \EE[\abs{X_n}].$$

This is trivial given the Wikipedia version. Alternatively, here's a direct proof:

> [!proof]- Use BOST
> The martingale case immediately reduces to the non-negative submartingale case, so we will consider only that. Consider the bounded ST
> $$T = \inf\{k\geq 0: X_k\geq \lambda\} \land n\leq n$$
> By [[Optional Stopping Theorem|BOST]],
> $$\begin{align*}\EE[X_n]&\geq \EE[X_T]\\
> &= \EE[X_T \id_{X^*_n\geq \lambda}] + \EE[X_T \id_{X^*_n < \lambda}]\\
> &\geq \lambda\PP(X^*_n\geq \lambda) + \EE[X_n \id_{X^*_n < \lambda}]\end{align*}$$
> where in the first case $T$ resolves to a value causing $X_T\geq \lambda$, and in the second case $X_T$ resolves to at least $X_n$.