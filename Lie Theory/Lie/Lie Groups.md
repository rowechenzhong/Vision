$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
This is the [[homepage]] for Lie Groups

# Introduction

The aim of group theory is to provide a mathematical framework for understanding symmetries. In the past, we have mainly discussed finite or otherwise *discrete* groups, which model *discrete* symmetries:

>[!example] Discrete Symmetries
>For instance, the symmetries of a set with $n$ elements give rise to the symmetric group $S_n$, while the symmetries of a regular $n$-gon form the dihedral group $D_n$. The symmetries of a tetrahedron yield $A_4$.

Lie group theory deals with continuous symmetries, which are families of symmetries depending continuously on multiple real parameters.

>[!example] $SO(3)$
A quintessential example of a Lie group is the group $SO(3)$ representing the rotational symmetries of the 2-dimensional sphere. In this case, the parameters are described by the Euler angles $\phi$, $\theta$, $\psi$.

>[!example] Other examples
> 1. **Orthogonal Group $O(n)$**: This group represents the symmetries of Euclidean space. In particular, $O(2)$ represents rotations in a 2-dimensional plane, and $O(3)$ represents rotations in 3-dimensional space.
> 
> 2. **Special Orthogonal Group $SO(n)$**: This is a subgroup of $O(n)$ consisting of rotations without reflections. For example, $SO(2)$ represents rotations in a 2-dimensional plane without flips.
> 
> 3. **Unitary Group $U(n)$**: This group represents the symmetries of complex vector spaces. It consists of unitary transformations.
> 
> 4. **Special Unitary Group $SU(n)$**: This is a subgroup of $U(n)$ consisting of unitary transformations with determinant 1. It plays a fundamental role in quantum mechanics.

Remarkably, unlike ordinary parametrized curves and surfaces, Lie groups are completely characterized by their linear behavior near the identity element. This leads to the concept of the **Lie algebra** associated with a **Lie group**. This notion allows us to express the theory of continuous symmetries in purely algebraic terms, offering an extraordinarily efficient method for their study. The objective of these notes is to provide a thorough examination of Lie groups and Lie algebras, as well as the interplay between them, illustrated with numerous examples.

>[!idea]
The theory of Lie groups was established in the latter half of the 19th century by the Norwegian mathematician Sophus Lie, in whose honor it is named. It has since been further developed by numerous mathematicians over the past 150 years, finding wide-ranging applications in mathematics and especially in physics.

# Sequence

First, we cover some prerequisite material:
- [[Topology review for Lie|Topology]]
- [[Topological Groups]]
- [[Differential Geometry]]

### Lie Groups
We now begin the study of Lie groups, proper.
- [[Lie/Lie groups/Lie groups]]
- [[LG + Homotopy]]
- [[Lie Subgroups]]
- [[Homogenous Spaces]]

How Lie groups act on spaces:
- [[LG + Actions]]
- [[LG + Representations]]
- [[LG + Tensor Fields]]
- [[LG Tangent Space]] (A collection of ideas).

### Exponent and Logarithm

Motivation:
- [[14 classical Lie groups]].
- [[Exponential and Logarithmic maps on Linear Maps

From the Exp/Log direction:
- [[Exponential Map (Interface)]]
- [[Logarithm Map]]
- [[Commutator]]
  
- [[Various Adjoint maps]]
- [[Adjoint Coincidence]]

- [[Exponential Map Problems]]
- [[Adjoint Problems]]
### The bridge

We execute the legendary bridge which we've had intuition on but black-boxed since middle school:

- [[Lie Algebra]]
- [[Tangent spaces of Lie groups are Lie Algebras]]
- [[Lie algebra Cat words]]
- [[Lie Subalgebras and Ideals]]