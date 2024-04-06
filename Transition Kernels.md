>[!idea] Markov Chains!
>At each time step of a (discrete-time finite-state-space) Markov chain on state spaces $\{(E_t,\FFF_t)\}$, we map a state $x_t\in E_t$ to probability measure over the possible next states, $\kappa_{x_t}:\FFF_{t+1}\to [0,1]$. This is usually encapsulated by a transition matrix on $E_t\times E_{t+1}$, but this fails epically if $E_{t+1}$ is anything wilder than a countable set. Obviously the correct thing to do is write $\kappa: E_t\times \FFF_t\to \FFF_{t+1}$. And preferably this should be measurable in $E_t$ as well...

Let $(S, \FFF)$ and $(T, \GGG)$ be two measurable spaces.

>[!definition] Transition Kernel
> A ==**Transition Kernel**== is a function $\kappa: (S\times \GGG)\to [0,+\infty]$ such that:
> - For any fixed $B\in \GGG$, $\kappa(\bullet, B)$ is $\FFF$-measurable.
> - For any fixed $s\in S$, $\kappa(s, \bullet)$ is a measure on $(T, \GGG)$.

There are *many* subclasses of these transition kernels, which end up being a recurring character in measure theory.
- If all $\kappa_s$ are probability measures, then we obtain a [[Markov Kernel]]!
- If $(S,\FFF) = (\Omega, \FFF,\PP)$, then we obtain a [[Random Measure]]! Usually, we let $(T,\GGG)$ be a complete separable metric space, and make sure all $\kappa_s$ are locally finite.