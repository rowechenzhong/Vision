$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
A ==**lie algebra**== over a field $k$ is a vector space $\fg$ over $k$ equipped with a ==**lie bracket**== $[\bullet, \bullet] : \fg \times \fg \to \fg$ which is

-   Bilinear
-   Skew-symmetric
-   Satisfies the ==**Jacobi Identity**==
    $$[[x,y],z] + [[y,z],x] + [[z,x],y] = 0$$

>[!example] Linear Lie Algebras
>Any subspace of $\gl_n(\KK)$ closed under the commutator is called a ==**Linear Lie Algebra**==.

>[!example] Canonical Construction
>Given an algebra $A$, the commutator $[x,y] = xy - yx$ yields a Lie algebra. The associative algebra $A$ is then called the ==**enveloping algebra**== of the resulting Lie algebra.
>
>It will later turn out that all Lie algebras can be embedded in such an algebra in this manner!

The most legendary example: [[Tangent spaces of Lie groups are Lie Algebras]].

Sometimes, we like to think of $[x,\bullet] = \Ad_x$ as a map in its own right. In this case, it is a derivation, and $x\to \Ad_x$ is the ==**adjoint representation**== of $\fg$.

Another example: [[Derivations are Lie Algebras]]. Thus, [[Vect(X)]].

>[!problem] Random problem
>Let $L$ over an algebraically closed field and let $x\in L$. Show that the subspace of $L$ spanned by eigenvectors of $\ad x$ is a subalgebra.

> [!solution]-
> Indeed, if $[x,y] = \alpha y$ and $[x,z] = \beta z$, then $[x,[y,z]] = [[x,y],z] + [y, [x,z]] = (\alpha+\beta)[y,z]$.

# Intro Subsequence
- [[Lie algebra Cat words]]
- [[Derivations are Lie Algebras]]
- [[Useful Ideals]]
- [[Automorphisms]]
- [[Linear Algebra and Lie Algebra]]

Basic concepts:
- [[Solvability and Nilpotency]]
- [[Lie's Theorem]]
- [[Jordan Canonical Form]]
- [[Engel's Theorem]]
- [[Cartan's Criterion]]

Massive amounts of theory:
- [[Semisimple Lie Algebras]]
- [[Lie Algebras and Bilinear Forms]]
- [[Killing Form]]