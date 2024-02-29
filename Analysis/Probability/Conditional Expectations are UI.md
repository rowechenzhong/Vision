>[!claim] Conditional Expectations are UI
>If $X\in L^1$, then the set of all $Y = \EE[X | \GGG]$ for $\GGG\subset \FFF$ a sigma algebra is [[Uniformly Integrable]].

> [!proof]- 
> This is quite believable; conditional expectations cause functions to become smoother, and UI is a smoothness condition.  First off, integrable functions are UI, so $\forall \eps > 0\exists \delta > 0$ such that
> $$\forall \PP(A)\leq \delta \qquad \EE\left(\abs{X}\id_A\right) \leq \eps$$
> By Jensen, $\abs{Y}\leq \EE[\abs{X} | \GGG]$, thus $\EE[\abs{Y}] \leq \EE[\abs{X}]$. We can choose a $\lambda < \infty$ such that $\EE(\abs{X}) \leq \lambda \delta$. By Markov,
> $$
> \PP(\abs{Y}\geq \lambda)\leq \frac{E(\abs{Y})}{\lambda} \leq \delta
> $$
> So
> $$
> 	\EE[\abs{Y} \id_{\abs{Y}\geq \lambda}]\leq \EE\left(\abs{X}\id_{\abs{Y}\geq \lambda}\right) \leq \eps
> $$
> 
> We did it this way (instead of just slapping any arbitrary $\id_A$ on it) because some arbitrary $\id_A$ may not be able to get pulled into the expectation.