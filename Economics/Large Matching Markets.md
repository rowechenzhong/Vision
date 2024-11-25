We define a family of games $G^n$. Fix constants $\bar{q}$, $\tilde{q}$, and $k$. For each $n$, $G^n$ is an imperfect-information game between:
- $n$ colleges with quota $\bar{q}$. Colleges cannot exceed their quota of students. The quotas are private.
- $\tilde{q} n$ students.
- The utility function of each college is hedonic (additive) where the utility of each particular student $0 < u_c(\{s\}) < 1$ is always positive. The $1$ is a technical bound, which is equivalent by scaling to positing an upper bound on any college-student pair.
- The preferences of students are (ordinal? cardinal? notes are unclear) private information. Each student's preference is modeled with uniform prior (notes are unclear on meaning).
- Students and colleges submit their preference lists simultaneously (the preference list of a college can differ from their utility function in this game?) DA is applied under the reported preferences (DA is college-proposing deferred acceptance?)

>[!theorem] Kojima Pathak
>Given $\eps > 0$, there exists $n$ such that for all $m$, truth-telling by every agent is an $\eps$-Nash equilibrium in $G^m$.

A strategy profile is an $\eps$-Nash equilibrium if no player can gain more than $\eps$ by unilateral deviation.

DA is strategy-proof for students (I guess we're talking about CPDAA?)