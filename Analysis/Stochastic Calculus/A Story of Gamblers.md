This is a [[story]].

# Prelude: The Multiverse
From elementary conceptions of probability, we imagine a universe which can take on many different values, whose entries are chosen "randomly." Perhaps these values lie in some continuum, or very large space. This is hard to describe mathematically, and we abandon this.

Picture instead a vast ensemble of universes $\Omega$, one for each possible outcome. Any particular experiment or **random variable** yields results which differ between these universes, but the granularity of the results of the random variable likely do not partition the entire ensemble. Random variables are thus thought of as functions from $\Omega$ to some space of results, which may be $\RR$, a finite set, or some other exotic object such as the space of infinite sequences of coin flips, $X:\Omega\to E$. The probability of a certain result occurring, $\PP(X \in A)\equiv \PP(X^{-1}(A))$, is thus a map from *subsets* of $\Omega$ to $\RR_{\geq 0}$. 

>[!todo] Let's get to the good stuff.

# Flying with Martingales

>[!idea]
>"Martingales" have always sounded like the name of a bird to me.

We now add a time axis to our multiverse, by considering a collection of random variables $\{X_t\}_{t\in I}$, where $I$ is some totally ordered set e.g. $\RR_{\geq 0}$ or $\ZZ_{\geq 0}$. We wish to speak of causality, and we expect our multiverse to branch accordingly. This is naturally accomplished in the multiverse picture: as time passes, our understanding of our seed is partitioned into finer and finer measure spaces. This is a **filtration** $(\FFF_t)_{t\in I}$, and random processes which respect causality are **adapted**; all random processes are adapted in this story.

A **martingale** is a process whose value represents its future expectation; $\EE[X_t | \FFF_s] = X_s$ for $s\leq t$. Equality is composed of two inequalities, and it is often more natural to prove theorems on *submartingales* and *supermartingales*, for which we write $\leq$ and $\geq$ instead.

### An optional stop