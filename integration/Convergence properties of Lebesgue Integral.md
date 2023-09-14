$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$# Baby Monotone Convergence

All of the major inequality results in this section are consequences of one theorem.
> [!claim] Baby Monotone Convergence
> Let $f_n: \Omega \to [0,\infty]$ be a sequence of measurable functions $f_n \uparrow f$. The claim is $$ \int_\Omega f \der \mu = \lim_{n\to \infty} \int_\Omega f_n \der \mu. $$

> [!proof]-
> Obviously LHS $\geq$ RHS. Fix some simple $0\leq s \leq f$. Let $\Lambda = \{x : s(x) = f(x)\}$; we don't care about these. By definition, we have to show $$ \int_\Omega s \der \mu \leq \lim_{n\to \infty} \int\_\Omega f_n \der \mu. $$ Thus, we should focus on characterizing the sets $B^s_n$ where $$ B^s_n = \{x\in \Omega \mid s(x) \leq f_n(x)\}. $$ We observe that:
>
> -   $f_n$ are nondecreasing, so $B^s_n \subseteq B^s_{n+1}$ for all $n$.
>
> -   If $$ s = \sum_{i = 1}^m c_i \chi\left(s^{-1}(c_i)\right), $$ then $$ B^s_k = \bigcup_{i=1}^m \{f_k^{-1}([c_i, \infty])\cap s^{-1}(c_i)\}. $$ Thus each $B^s_k$ is measurable.
>
> -   $\bigcup_{k=1}^\infty B^{s,t}_k = \Omega\setminus \Lambda$. After all, such an $x_0$ satisfies $$ f_k(x_0)< s(x_0) $$ \_for all $k$_; the LHS approaches $f(x_0)$, thus equality must be achieved.
>
> Thus, by the second two points, we find that $$ \int_{\Omega\setminus \Lambda} s \der \mu = \sup_{k\to \infty} \int_{B^s_k} s \der \mu \leq \sup_{k\to \infty} \int\_{\Omega\setminus \Lambda} f_k \der \mu. $$

## Fatou's Lemma

Using the baby monotone convergence theorem, it is straightforward to prove

> [!theorem] Fatou's Lemma
> Let $f_n: \Omega \to [0,\infty]$ be a sequence of measurable functions. Then $$ \int_\Omega \liminf_{n\to \infty} f_n \der \mu \leq \liminf_{n\to \infty} \int\_\Omega f_n \der \mu. $$
> ^Fatou

> [!problem] Prove it
> Let $g_n(x) = \inf_{k\geq n} f_k(x)$ and go.

Then, funnily enough, we can turn right around and prove a stronger monotone convergence theorem:

> [!problem] Monotone Convergence Theorem
> Let $f_n: \Omega \to [0,\infty]$ be a sequence of measurable functions such that $\lim_n f_n = f$, and $f_n \leq f$ for all $n$. Then $$ \int_\Omega f \der \mu = \lim_{n\to \infty} \int_\Omega f_n \der \mu. $$ Use Fatou's Lemma.
> ^Monotone-Convergence

Note that the \"monotone\" in the name is a bit of a misnomer; we don't require $f_n$ to be nondecreasing. Here's the result on absolutely integrable functions:

> [!problem] Fatou-Lebesgue Theorem
> Let $f_n: \Omega \to \RR$ be a sequence of measurable functions. Suppose that this exists some bound on these functions, $g:\Omega\to \RR$, for which $\abs{f_n} \leq g$ for all $n$ and $\int_\Omega g \der \mu < \infty$. Then
> $$\int_\Omega \liminf_{n\to \infty} f_n \der \mu \leq \liminf_{n\to \infty} \int_\Omega f_n \der \mu$$
> $$\leq \limsup_{n\to \infty} \int_\Omega f_n \der \mu \leq \int_\Omega \limsup_{n\to \infty} f_n \der \mu.$$
> ^Fatou-Lebesgue

And here's a special case of that:

> [!problem] Dominated Convergence Theorem
> Let $f_n: \Omega \to \RR$ be a sequence of measurable functions such that $\lim_n f_n = f$ exists. Suppose that there exists an absolutely integrable bound on these functions, $g:\Omega\to \RR$, for which $\abs{f_n} \leq g$ for all $n$. Then, $$ \int_\Omega f \der \mu = \lim_{n\to \infty} \int_\Omega f_n \der \mu. $$
> ^Dominated-Convergence

## Almost Everywhere

There are actually a few [[types of convergence]]. Most of the above theorems hold with the assumptions replaced by **almost everywhere** convergence.