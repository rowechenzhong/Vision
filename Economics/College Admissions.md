A ==**college admissions problem**== is a four-tuple $(C,S,q,R)$ where:
- $C = \{c_1,\dots, c_m\}$ are colleges
- $S = \{s_1,\dots, s_n\}$ are students
- $q = (q_{c_1},\dots, q_{c_m})$ are college capacities
- $R = (R_{c_1},\dots, R_{c_m}, R_{s_1}, \dots, R_{s_n})$ are preferences.
	- Each $R_s$ is a preference relation over $C\cup \{\emptyset\}$
	- Each $R_c$ is a preference relation over $2^S$!!
	- $P_c, P_s$ are strict preferences derived from $R_c$ and $R_s$.

A college preference $R_c$ is ==**responsive**== iff:
- It contains the following prism: for each $T\subset S$ with $\abs{T} < q_c$ and every $s\in S\setminus T$, $(T\cup \{s\})P_c T \iff \{s\} P_c \emptyset$.
- Along the $(1,\dots, 1)$ slices of the cube, it is locally a prism, or something: for every $T\subset S$ with $\abs{T} < q_c$ and all $s, s'\in S\setminus T$, then $(T\cup \{s\})P_c(T\cup \{s'\}) \iff \{s\} P_c \{s'\}$.

We forever assume college preferences are responsive.

>[!idea] Rigidity
>This doesn't "fix" anything in the sense that there is not a substantially simpler description. Knowing that $\emptyset \prec \{1\} \prec \{2\} \prec \{3\}$ still induces a non-trivial hasse diagram where $\{1,2\}$ and $\{3\}$ are incomparable. However, along $(1,\dots, 1)$ slices it is fixed by the level-$1$ permutation.
>
>However, for some reason the notes seem to ignore this subtlety, and the theory operates as if the "important parts" of the preference function are completely determined by the preference on $\emptyset, \{s_1\}\dots,\{s_n\}$ only. This is not a theoretical defect, it's an intuitive defect...

A matching is a correspondence $\mu: C\cup S\to C\cup S$. The notation in the notes is kind of bad; I interpret this as the union $\mu$ of two functions $\mu_C: c\to 2^S$ and $\mu_S: s\to 2^C$ such that $\abs{\mu(c)}\leq q_c$, $\abs{\mu(s)}\leq 1$, and $s\in \mu(c)\iff \mu(s)\in c$. In other words, you draw a bipartite graph, where each $c$ has degree $\leq q_c$ and each $s$ has degree $\leq 1$.

One immediately defines the notions of ==**blocked by a (college, student, pair)**==, individually rational, and stable. These are not immediately obvious because these notions are in a sense about small finite-case coalitions, and one needs to write down which finite cases to check.
- $\mu$ is blocked by $c$ if $\exists s\in \mu(c)$ such that $\emptyset P_c s$. The intuition here is that colleges can determine to reject on a per-student basis.
- $\mu$ is blocked by $s$ if $\emptyset P_s \mu(s)$.
- $\mu$ is blocked by $(c,s)$ if:
	- $cP_s \mu(s)$ and $s'\in \mu(c)$ such that $\{s\}P_c \{s'\}$.
		- i.e. a college would kick a different student to allow them in
		- This doesn't seem very reasonable to me; why not allow the college to kick *many* students to allow an angel in? I guess I need to update my intuition from the finiteness being "a bounded number of colluding agents" to "a bounded number of atomic operations." Does not sound rational at all.
	- or $\abs{\mu(c)} < q_c$ and $\{s\} P_c \emptyset$. 

>[!definition] CPDAA, or SPDAA
>CPDAA: A college with $r$ standing offers proposes to their top $q_c - r$ remaining acceptable students which have not rejected them yet. Students hold most preferred acceptable offers.
>
>SPDAA: analogous.

>[!idea] College $\implies$ marriage
>Divide each college into $q_{c_i}$ people and match. Given a marriage, we obtain a college admission, and given a college admission, we obtain a marriage.

>[!claim] Stability Lemma
>A college admission is stable iff its corresponding marriage is stable.

I don't think the admissions problem as written is natural. We defined college admissions so we could use this lemma to nuke everything.
- There is a lattice of stable assignments.
- SPDAA produces $\mu^S$ and CPDAA produces $\mu^C$, which are student-optimal and college-optimal. These are maxima and minima on the stable lattice.
- There is no IR matching that makes each student strictly better off than $\mu^S$.
- There exists no stable and SP mechanism.
- Truth-telling is dominant for students under SPDAA.

New results:

- A college that does not fill all its positives at some stable matching is assigned the same set of students in every matching.
- If $\mu$ and $\nu$ are two stable matching, then either:
	- for all $s\in \mu(c)\setminus \nu(c)$ and $s'\in \nu(c)\setminus \mu(c)$, $\{s\} P_c \{s'\}$.
	- for all $s\in \mu(c)\setminus \nu(c)$ and $s'\in \nu(c)\setminus \mu(c)$, $\{s'\} P_c \{s\}$.
- There exists no stable mechanism under which truth-telling is dominant for all colleges.

# School Choice Problem
The ==**school choice problem**== does not treat colleges (which are public schools, in this case) as agentic; their preferences are publicly known (usually due to legislation, anti-segregation, etc) and the mechanism consequently does not have to be strategy proof against the schools. Thus SPDAA, also known as the ==**Gale-Shapley student optimal stable mechanism**==, is quite a good choice in this context. It has the following benefits (repeated from above):
- It is ==**stable**==. No college would be willing to kick out a student for another student who also actually wants to attend. The (Abdulkadiroğlu and Sönmez - 2003) paper calls this eliminating ==**justified envy**==.
- It Pareto dominates any other stable mechanism.
- It is strategy-proof for the students (which are the only agents, anyways!)

However, there are examples which demonstrate that it is NOT Pareto efficient (for students!) in general!!

>[!example] (Hastily written)
>Schools $123$, students $abc$.
>$1acb, 2bac, 3bac, a213, b123, c123$.

On the other hand, if you *really* only care about the preferences of the students and want the preferences of the schools to serve only as guidance, you can simply let the preferences of the schools serve as priorities for the TTC algorithm. (Here, I mean the bipartite student-preferring TTC algorithm, where in a cycle each student gets the school they point to). This is of course IR, PE, and SP.