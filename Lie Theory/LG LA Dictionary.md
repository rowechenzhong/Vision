$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
> [!theorem] Morphisms
> Let $\phi:G\to K$ induce $\phi_* : \Lie G \to \Lie K$. Then $H = \ker \phi$ is a **closed** Lie subgroup (which is obviously normal) with lie algebra $\hh = \ker \phi_*$.
> 
> This induces map $\overline{\phi}:G/H\to K$ which is an **immersion**. The image $\im \overline{\phi}$ is an immersed submanifold of $K$ Lie-isomorphic to $G / H$ with algebra $\im \phi_*\cong \fg / \hh$.

This is immediate by [[Vect(X)#^action-ker-im|this theorem]]. Note that if $V$ is a finite-dimensional representation of $G$ and $v\in V$, then $G_v$ is a closed Lie subgroup with Lie algebra $\fg_v = \{z\in \fg: zv = 0\}$.

# Fundamental Theorems of Lie Theory

>[!theorem] First Fundamental Theorem - Connected subgroups $\iff$ Lie subalgebras
>There is a bijection between connected Lie subgroups $H\subset G$ and Lie subalgebras $\hh\subset \fg$.

>[!theorem] Second Fundamental Theorem - Maps
>If $G,K$ are Lie groups with $G$ simply connected, then the map $\Hom(G,K)\to \Hom(\Lie G, \Lie K)$ via $\phi\to \phi_*$ is a bijection.

>[!theorem] Third Fundamental Theorem - Existence
>Any finite-dimensional Lie algebra admits a Lie group.

For $\KK\in \{\RR, \CC\}$, $G\mapsto \Lie G$ is an equivalence between the category of simply-connected $\KK$-Lie groups and finite-dimensional $\KK$-Lie algebras. [[LG + Homotopy|Any connected Lie group has the form $G / \Gamma$ where $G$ is simply connected and $\Gamma\subset G$ is a discrete central subgroup.]]



# Some details

>[!theorem]
>The ==**center**== $Z$ of a connected Lie group $Z$ is a closed (normal, commutative) Lie subgroup of $G$ with Lie algebra $\mathfrak z$. $G / Z(G)$ is called the ==**adjoint group**== of $G$, and is naturally isomorphic to the image of the adjoint representation $\Ad:G \to \GL(\fg)$.