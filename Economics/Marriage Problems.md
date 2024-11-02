A ==**marriage problem**== is a triple $(M, W, R)$ where $M$ is a set of men, $W$ is a set of women, and we have (non-strict) preference functions $R_m\in \Pi^{W\cup \{m\}}$ and $R_w\in \Pi^{W\cup \{m\}}$.

Here, $mR_m w$ if man $m$ finds woman $w$ unacceptable. A matching is a permutation $\mu: M\cup W\to M \cup W$ satisfying the obvious conditions.

A matching $\mu$ is ==**Pareto efficient**== in the normal sense. There are some other terms though, which generalize the IR idea.
- A matching $\mu$ is ==**blocked**== by $i\in M\cup W$ if $iP_i \mu(i)$ ($i$ does not find the matching acceptable). If it is not blocked by anyone, it is ==**individually rational**==.
- A matching $\mu$ is ==**blocked by a pair**== $(m, w)\in M\times W$ if $wP_m \mu(m)$ and $mP_w\mu(w)$.
- A matching is ==**stable**== (essentially, IR against individuals and male-female pairs) if it is not blocked by any individual or pair.

> [!definition] Man-proposing deferred acceptance algorithm
> Each man records a set of women who have rejected them.
> Each woman records a single man who is their current most preferred proposal.
> 
> While true:
> - Each man $m$ who was rejected on the preceding step proposes to their top acceptable choice who has not rejected them yet.
> - Each woman holds her most preferred acceptable proposal to date, and rejects the rest. In particular, a woman my reject a man she previously accepted.
> - If on this step, no man was rejected, terminate.
>   
>Note that women weakly improve throughout the process and men weakly get worse off, hence the algorithm terminates (due to monovariant).

>[!theorem] MPDAA produces a valid matching

$\mu$ is stable because it is obviously IR, and a woman would never leave a better man for a worse man, hence the matching is never blocked by a pair.

>[!theorem] Stable Matchings
>1. MPDAA produces a ==**man-optimal stable matching**== $\mu^M$ which is *maximal* in the poset induced by men.
>2. It is also *minimal* in the poset induced by women!
>3. The ==**rural hospitals theorem**== says the set of agents matched is the same in all stable matchings.

Maximality and minimality are three-line arguments, and the rural hospitals theorem follows by sandwiching between the two theorems.

> [!theorem] Lattice Theorem
> The ==**join**== of two stable matchings $\mu$ and $\mu'$ is $\mu \lor_M \mu'$ which assigns each man the more preferred of his two assignments under $\mu$ and $\mu'$ the less preferred of her two assignments under $\mu$ and $\mu'$. The ==**meet**== is defined analogously.
> 
> The join and meet of two stable matchings are stable matchings.

>[!theorem] You can't get strictly better than MPDAA for all men
>Even if we permit blocking pairs, there is no IR matching $\nu$ such that $\nu(m) P_m \mu^M(m)$ for all $m\in M$; you cannot make all men strictly better off.

# Mechanisms

A mechanism $\varphi$ is ==**stable**== if $\varphi(R)$ is stable for all $R$ (where $R$ is the set of responses), ditto for PE and IR. Of course, stable $\implies$ PE and IR. Let $\phi^M$ and $\phi^W$ select the man-optimal and woman-optimal stable matchings for each problem.

>[!theorem] There exists no stable and SP mechanism

>[!proof]- Proof by counterexample
>todo, it's very simple between only two men and two women in opposing configuration; a man can defect by reporting that his less favored woman is unacceptable.

>[!theorem] $\phi^M$ is SP for men