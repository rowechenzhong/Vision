$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
This is the [[homepage]] for axiomatic probability theory, which builds off of [[Measure Theory|measure theory]].

[[A Story of Gamblers]]

# Main Sequence

### Foundational
1. [[probability objects]]
2. [[Expectations]]
3. [[Conditional Expectation]] (Advanced, not used until Martingales)
4. [[independence]]
5. [[Basic Inequalities]]
6. [[Kolmogorov's Zero-One Law]]

### Branches
5. [[Measure Theoretic Fourier Transform]]
6. [[Ergodic Theory]]
7. [[Martingale Theory]]
8. [[Random Processes in Continuous Time]]

### Main Results

A ==**Law of Large Numbers**== is of the following form: if $X, X_i$ are (some set of nice properties) random variables, for which $X_i\to X$ (somehow), the empirical means $\overline{X}_n = \frac1n \sum X_i$ converge to $\EE[X]$ (in some sense). Filling in the blanks of this intuitive statement in different ways yield theorems of differing levels of difficulty. Here are two possible routes:

**From the ground up:**
1. [[Stupid LLN]]
2. [[Weak LLN]]
3. [[Strong LLN elementary proof]]
**Through Ergodic Theory**:
- [[SLLN via Birkhoff and von Neumann]]
**Through Martingale Theory:**
- [[SLLN via Martingales]]

==**Cramer's Theorem**== states that large deviations from the sample average are exponentially unlikely.
8. [[Generating Functions]]
9. [[Cramer Introduction]]
10. [[Cramer]]

The ==**Central Limit Theorem**== states that sample averages converge onto a normal distribution. It is essentially a direct consequence of Fourier analysis, and can be read immediately afterwards.
11. [[CLT Introduction]]
12. [[Central Limit Theorem]]