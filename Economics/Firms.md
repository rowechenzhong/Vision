Same type of problem; we have firms $F$ and workers $I$.
- Each worker has some $u^i(f, s)$ which is their utility for working for firm $f$ at wage $s$.
- Each firm optimizes $\pi(C, s) = y(C) - \sum_{i\in C} s_i$.

The argmax subsets form $D^f(s)$ where $s$ are the fixed salary vectors demanded.

Workers are ==**gross substitutes**== for a firm if the demand for a worker $j$ does not go down when the salary of another worker $i$ goes up. Specifically, $\forall \tilde{s} \geq s$ (nondecreasing salary vector), for all $C\in D^f(s)$, $\exists \tilde{C}\in D^f(\tilde{s})$ under the new salaries such that for all $j$ such that $\tilde{s}_j = s_j$ (workers whose salaries did not change), $j\in \tilde{C}$ (the demand for $j$ did not decrease). We assume gross substitutes in the sequel.

A matching is a function $\mu: I\to F\cup \{\emptyset\}$, and an allocation is a matching plus a salary schedule. IR means that nobody would rather unmatch.

> [!definition] Kelso-Crawford Auction
> This is like Firm-Proposing Deferred Acceptance Algorithm. Initialize all salaries to $0$. Repeat:
> 1. Each firm makes an offer to their most preferred set of workers under $D^f(s)$. **Offers CANNOT be withdrawn; the argmax is solely over the remaining workers**.
> 2. Each worker evaluates all offers and holds the best acceptable.
> 3. Terminate if no rejections were made. Increase the salaries by infinitesimal.

Note that:
- Actually, in step 1, even if firms were allowed to withdraw, they would not (locally) be incentivized (strictly) to do so, by gross substitution.
- Worker's best offer (best salary-firm utility) is non-decreasing throughout the process.

>[!theorem]
>The KC auction terminates, producing an allocation in the core which is weakly preferred by every firm to every other core allocation.

