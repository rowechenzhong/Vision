$$
\require{physics}

% Misc
\newcommand{\cbrt}[1]{\sqrt[3]{#1}}
\newcommand{\sgn}{\text{sgn}}
\newcommand{\ii}[1]{\textit{#1}}
\newcommand{\eps}{\varepsilon}

% Expected Value
\newcommand{\EE}{\mathbb E}
\newcommand{\PP}{\mathbb P}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}

\newcommand{\pperp}{\perp\kern-6pt\perp}

% Lol relativity
\newcommand{\LL}{\mathcal{L}}
\newcommand{\pa}{\partial}

% Inequalities
\newcommand{\cyc}{\sum\limits_{\mathrm{cyc}}}
\newcommand{\sym}{\sum\limits_{\mathrm{sym}}}
\newcommand{\cycprod}{\prod_{\mathrm{cyc}}}
\newcommand{\symprod}{\prod_{\mathrm{sym}}}

\newcommand{\eq}[1]{\stackrel{#1}{=}}
\newcommand{\rgeq}[1]{\stackrel{#1}{\geq}}
\newcommand{\rleq}[1]{\stackrel{#1}{\leq}}

% Sets
\newcommand{\CC}{\mathbb C}
\newcommand{\FF}{\mathbb F}
\newcommand{\NN}{\mathbb N}
\newcommand{\QQ}{\mathbb Q}
\newcommand{\RR}{\mathbb R}
\newcommand{\ZZ}{\mathbb Z}
\newcommand{\SSS}{\mathbb S}
\newcommand{\II}{\mathbb I}

% Geometry
\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\newcommand{\dang}{\measuredangle} %% Directed angle
\newcommand{\ray}[1]{\overrightarrow{#1}}
\newcommand{\seg}[1]{\overline{#1}}
\newcommand{\arc}[1]{\wideparen{#1}}
\newcommand{\pow}{\text{pow}} %% Power


% Complex Bashing
\newcommand{\conj}[1]{\overline{#1}}
\DeclareMathOperator{\cis}{cis}

% NT
\newcommand{\jacobi}[2] {\genfrac{(}{)}{1.5pt}{}{\,#1\,}{#2}}
\DeclareMathOperator*{\lcm}{lcm}
\DeclareMathOperator*{\ord}{ord}

\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Derivative
\newcommand{\der}{\ \mathrm {d}}

% Unit Vectors
\newcommand{\ihat}{\boldsymbol{\hat{\textbf{\i}}}}
\newcommand{\jhat}{\boldsymbol{\hat{\textbf{\j}}}}
\newcommand{\khat}{\boldsymbol{\hat{\textbf{k}}}}
\newcommand{\rhat}{\boldsymbol{\hat{\textbf{r}}}}
\newcommand{\that}{\boldsymbol{\hat{\mathbf{\theta}}}}

% Operators
\newcommand{\xx}{\hat{x}}
\newcommand{\pp}{\hat{p}}
\newcommand{\ee}{\hat{E}}
\renewcommand{\aa}{\hat{a}} % aa makes an a with a dot on top.
\newcommand{\bb}{\hat{b}}
\renewcommand{\AA}{\hat{a}}
\newcommand{\BB}{\hat{B}}

\newcommand{\ad}{\hat{a}^\dagger}

% Groups
\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}
\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}

% Linalg
\DeclareMathOperator*{\range}{range}
\DeclareMathOperator*{\nul}{null}
\DeclareMathOperator*{\Tr}{Tr}

% Homomorphism
\DeclareMathOperator{\Hom}{Hom}
% Endomorphism
\DeclareMathOperator{\End}{End}

\newcommand{\id}{1\!\!1}

\newcommand{\GL}{\mathbb{GL}}
\newcommand{\SL}{\mathbb{SL}}

% Measure Theory
\newcommand{\AAA}{\mathscr{A}}
\newcommand{\BBB}{\mathscr{B}}
\newcommand{\FFF}{\mathscr{F}}
\newcommand{\GGG}{\mathscr{G}}
\newcommand{\HHH}{\mathscr{H}}

\DeclareMathOperator{\ess}{ess}
$$
This is the [[homepage]] for Lie Groups and Lie Algebras.

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
- [[topological manifolds|Manifolds]]
- 