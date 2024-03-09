$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
You should really be thinking about a [[Delta Complex]] $X$, but Seidel's notes are right in doing everything in terms of [[semi-simplicial set|semi-simplicial sets]] $K$.

> [!definition] Chains
> A ==**chain**== is an element in $C_n(K) = \bigoplus_{\sigma\in K_n} \ZZ \sigma$. $C_n(K) = 0$ for all $n < 0$.

> [!definition] Boundary Map
> Define the ==**boundary map**== $\pa_n:C_n(K)\to C_{n-1}(K)$ via
> $$\pa_n(\sigma) = \sum_i (-1)^i \pa_n^i(\sigma).$$
> If the dimensions are clear, we just write $\pa$ (alternatively, let $\pa: \bigoplus C_n\to \bigoplus C_n$).

By geometry, it is completely obvious that

> [!problem] A wild chain complex appeared.
> $\pa_{n-1}\circ \pa_n = 0$.

> [!solution]- Okay fine
> We verify for a single $\sigma\in K_n$.
> $$
> \begin{align*}
> 	\pa_{n-1}\circ \pa_n \sigma &= \sum_{i\leq n-1} (-1)^i \pa_{n-1}^i(\sigma) \sum_{j\leq n} (-1)^j \pa_n^j(\sigma)\\
> 	&=\sum_{i\leq n-1} \sum_{j\leq i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&=\sum_{i\leq n-1} \sum_{j\leq i} (-1)^{i+j} \pa_{n-1}^j(\sigma) \pa_n^{i+1}(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&=\sum_{j\leq n-1} \sum_{i \geq j} (-1)^{i+j} \pa_{n-1}^j(\sigma) \pa_n^{i+1}(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&=\sum_{j\leq n-1} \sum_{i > j} (-1)^{i+j + 1} \pa_{n-1}^j(\sigma) \pa_n^{i}(\sigma) + \sum_{i\leq n-1}  \sum_{j > i} (-1)^{i+j} \pa_{n-1}^i(\sigma) \pa_n^j(\sigma)\\
> 	&= 0 
> \end{align*}
> $$

>[!definition] Homology Groups
>Thus, $B_n(K) = \im(\pa_{n+1})\subset Z_n(K) = \ker(\pa_n)$.
>
>We define the ==**$n$-the homology group**== $H_n = Z_n(K) / B_n(K)$.

Here is some advanced material:
- [[BG Complex]]
- [[Vietoris-Rips Complex]]