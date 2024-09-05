---
aliases:
  - usual conditions
---
# Continuous-time filtration

Very soon, we will care that $(\Omega, \FFF, \PP)$ is endowed with a ==**continuous-time filtration**==, which is just a [[filtration]] indexed with real numbers: $\FFF_s\subseteq \FFF_t\subseteq \FFF$ for $s \leq t$, and $\FFF_\infty = \sigma(\FFF_t: t\geq 0)$. These correspond to information as usual.

The continuity of the real numbers makes some things slightly different though; think causality from statmech. First, consider the following object:
$$\FFF_{t+} = \bigcap_{s > t} \FFF_s$$
This is in general not equal to $\FFF_t$ (it is larger) and specifies the amount of information known after processing $t$. If $\FFF_{t+} = \FFF_t$ for all $t$, then the filtration is said to be ==**right-continuous**==. Observe that $(\FFF_{t+})$ is itself a filtration, which is automatically right-continuous.

>[!idea] Waffle
> I would imagine that "$\FFF_{t-} = \bigcup_{s < t} \FFF_s$" would be more relevant, but I guess I don't know what I'm talking about.

Consider $\mathscr{N} = \{X: \exists X\subset A\in \FFF_\infty, \PP(A) = 0\}$, the class of all $(\FFF_\infty,\PP)$-negligible sets. We say that the filtration is ==**complete**== if $\mathscr{N}\subset \FFF_0$. Any filtration can be completely simply by allowing $\FFF'_t = \sigma(\FFF_t, \sigma(\mathscr{N}))$, yielding the ==**completed filtration**==. Augmenting a $\sigma$-field with negligible sets does not alter independence properties, or much else at all (see [[complete measure space]]).

We say that $(\FFF_t)_{t\geq 0}$ specifies the ==**usual conditions**== if it is complete and right-continuous.

>[!idea] Let me try to interpret these
>$\FFF_\infty$ is basically $\FFF$, from my understanding (it's just the whole universe). $\mathfrak{N}$ is the set of all measure-$0$ events, and because these don't affect anything, I suppose it is totally fine (a housekeeping trick?) to ensure that we know whether we're in them from the beginning.
>
>The second condition is interesting; we want our $\FFF$ to be "right-continuous". I don't quite understand why!