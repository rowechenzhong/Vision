$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$Algebraic topologists care about things like normal subgroups.
# Normal things 


> [!definition] Coset
Let $H\subset G$ be a subgroup of a group $G$. A ==**left coset**== of $H$ in $G$ is a set of the form $$ gH = \{gh \mid h\in H\} $$ for some $g\in G$. Similarly, a ==**right coset**== is $$ Hg = \{hg \mid h\in H\} $$ 


> [!definition] Normal Subgroup
A subgroup $H\subset G$ is ==**normal**== if for all $g\in G$, $gHg^{-1} = H$. This is denoted $H\trianglelefteq G$. Given a subgroup $H$, the ==**normalizer**== of $H$ is $$ N(H) = \{g\in G \mid gHg^{-1} = H\} $$ A subgroup is normal iff it is the kernel of some homomorphism. 


> [!definition] Quotient Group
Given a normal subgroup $H\trianglelefteq G$, the ==**quotient group**== $G/H$ is the set of cosets of $H$ in $G$, with the group operation $$ (g_1H)(g_2H) = (g_1g_2)H $$ Its universal property is that for any group $K$ and any homomorphism $f: G\to K$ such that $H\subset \ker f$, there exists a unique homomorphism $\phi: G/H\to K$ such that $\phi\circ \pi = f$, where $\pi: G\to G/H$ is the canonical projection. 


> [!definition] Generators
Let $S\subset G$ be a subset of a group $G$. The ==**subgroup generated**== by $S$ is $$ \langle S \rangle = \bigcap_{S\subset H\leq G} H $$ where $H$ ranges over all subgroups of $G$ containing $S$. Equivalently, $\langle S \rangle$ contains all finite words using elements of $S$ and their inverses. The ==**normal subgroup generated**== by $S$ is $$ \langle\langle S \rangle\rangle = \bigcap_{S\subset H\trianglelefteq G} H $$ 

# Abelian Groups 


> [!definition] Abelian
A group $G$ is ==**abelian**== if $gh = hg$ for all $g, h\in G$. Given a subgroup $H\subset G$, the ==**centralizer**== of $H$ is $$ C(H) = \{g\in G \mid gh = hg \text{ for all } h\in H\} $$ 


> [!definition] Commutator
The ==**commutator**== of $g, h\in G$ is $$ [g, h] = ghg^{-1}h^{-1} $$ The ==**commutator subgroup**== of $G$ is $$ [G, G] = \langle\langle [g, h] \mid g, h\in G \rangle\rangle $$ 


> [!definition] Abelianization
The ==**abelianization**== of $G$ is $$ G/[G, G] $$ For any homomorphism $f: G\to A$ where $A$ is abelian, $[G, G]\subset \ker f$ so there exists a unique homomorphism $\phi: G/[G, G]\to A$ such that $\phi\circ \pi = f$, where $\pi: G\to G/[G, G]$ is the canonical projection. 

# Free things 


> [!definition] Free Product
Given a collection of groups $\{G_i\}_{i\in I}$, the ==**free product**== $\ast_{i\in I} G_i$ is the coproduct in the category of groups. That is, any map $f_i: G_i\to H$ for $i\in I$ factors uniquely through a homomorphism $\phi: \ast_{i\in I} G_i\to H$. 

One construction is as follows: consider all finite words using elements of $\bigcup_{i\in I} G_i$ and their inverses. A *reduction* consists of replacing a substring of elements all from the same $G_i$ with their product, or removing any identity element. A *reduced* word is one which cannot be reduced further. The free product is the set of all reduced words, with the group operation being concatenation of words followed by reduction. 
> [!definition] Free Group
A ==**free group**== $F_S$ on a set $S$ is the group $$ \ast_{s\in S} \ZZ = \langle S \rangle $$ 

Equivalently, a free group is a group with a map $i: S\to F_S$ such that for any group $G$ and any map $f: S\to G$, there exists a unique homomorphism $\phi: F_S\to G$ such that $\phi\circ i = f$. The construction is as follows: $F_S$ is the set of all finite words using elements of $S$ and their inverses, with the group operation being concatenation of words. 
> [!definition] Presentation
A ==**presentation**== of a group $G$ is a pair $(S, R)$ where $S$ is a set and $R\subset F_S$ is a subset of the free group on $S$ such that $G\cong F_S / \langle\langle R \rangle\rangle$. All groups have a presentation, given by $S = G$ and $R$ the set of all relations in $G$. 




















