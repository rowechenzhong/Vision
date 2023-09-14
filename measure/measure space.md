$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$> [!definition] Measure Space
> A ==**measure space**== is a triple $(\Omega, \AAA, \mu)$ where $\Omega$ is a set, $\AAA$ is a $\sigma$-[[measurable space|algebra of subsets]], and $\mu$ is a ==**measure**==, i.e. a function $\mu: \AAA \to [0,\infty]$. This $\mu$ is required to be countably additive, and $\mu(\emptyset) = 0$.
> In probability, $\Omega$ is commonly called the ==**state space**== or ==**outcome space**==, and elements of $\AAA$ are called ==**events**==.

> [!problem] Basic Properties
>
> 1. If $A\subseteq B$ are measurable, then $\mu(A) \leq \mu(B)$, because $\mu(B) = \mu(A) + \mu(B\setminus A)$.
> 2. We write $A_i \uparrow A$ if $A_1 \subseteq A_2 \subseteq \dots$ and $A = \bigcup_i A_i$. Then, 
> $$ \mu(A) = \lim_i \mu(A_i).$$ 
> 3. We write $A_i \downarrow A$ if $A_1 \supseteq A_2 \supseteq \dots$ and $A = \bigcap_i A_i$. If $\mu(A_1) < \infty$, then
> $$ \mu(A) = \lim_i \mu(A_i) $$

> [!solution]-
>
> 1. $B = A \cup (B \setminus A)$, and the two sets are disjoint.
> 2. $A = \bigcup_i (A_i \setminus A_{i-1})$, each of which is disjoint. This summation converges because its partial sums are increasing.
> 3. Apply the previous result to $A_1 \setminus A_i$.

> [!idea] Countable Additivity
> The problem with uncountable sets is that they're a bit too large. Example: Let $S$ be an uncountable set of positive real numbers. Then, if you split into buckets $(\frac{1}{n + 1}, \frac{1}{n}]$, then there are only countably many buckets, thus some bucket has infinitely many elements of $S$. Conclusion: if $S$ is uncountable, there exist finite sets that have arbitrarily large sums.

> [!idea] Almost Surely
> A property $P$ holds ==**almost surely**== if it holds for all $\omega \in \Omega$ except for a set of measure zero. In measure theory, essentially all statements are only true almost surely; measure theory cannot distinguish between two sets that differ by a set of measure zero.

> [!problem] Almost Sure Things
> A ==**probability space**== is a measure space $(\Omega, \AAA, \mu)$ where $\mu(\Omega) = 1$. Show that the intersection of countably many measurable sets of measure $1$ has measure $1$.

> [!solution]-
> Let $A_1, A_2, \dots$ be measurable sets of measure $1$. Then, their complements $\conj{A}_1, \conj{A}_2, \dots$ have measure $0$. By countable additivity, the union of these complements has measure $0$. Thus, the intersection of the $A_i$ has measure $1$.

[[Lebesgue Measure]]
