>[!claim] Borel-Cantelli Lemma
> Let $E_1, E_2,\dots\in \FFF$ be a sequence of events in some measure space. If the sum of the measures of the events is finite
> $$\sum_n \mu\left(E_n\right) < \infty$$
> Then the measure that infinitely many occur is $0$;
> $$\mu\left(\limsup_{n\to \infty} E_n\right) = 0$$

This is pretty clear; $$\mu\left(\bigcap_n \bigcup_{k\geq n} E_k\right)\leq \mu\left(\bigcup_{k\geq n} E_k\right) \leq \sum_{k\geq n} \mu(E_k)$$ for all $n$, but the RHS goes to $0$ as $n\to \infty$.

There is a partial converse:

>[!claim] Second Borel-Cantelli Lemma
>Let events $E_1,E_2,\dots\in \FFF$ be independent. If the sum of the probabilities of the events is infinite
>$$
>	\sum_n \PP(E_n) = \infty
>$$
>then they occur infinitely often almost surely
>$$
>	\PP\left(\limsup_{n\to \infty} E_n\right) = 1
>$$

This is also clear.