$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
A ==**$\ZZ[G]$-module**== is an abelian group $A$ endowed with a left group action $x\to gx$ which is distributive on the right (in other words... it is a module in the usual sense).

A module is called ==**free over $\ZZ[G]$**== if one can find a $\ZZ$-basis on $\ZZ[G]$, indexed $e_{g, \lambda}$, such that $ge_{h,\lambda} = e_{gh, \lambda}$ (in other words, you are of the form $\ZZ[G]^{\otimes \Lambda}$).

See: [[Coinvariants of a ZG module]]

# Building $\ZZ[G]$-modules from $G$-sets

For any set $X$, the ==**free abelian group on $X$**== is $\ZZ[X]$, the free abelian group with basis $(e_x)_{x\in X}$. If $G$ is a group, then $\ZZ[G]$ also has a ring structure via $e_g\cdot e_h = e_{gh}$.

If $X$ happens to be a $G$-set (a set endowed with a left group action) then the action of $G$ on $X$ induces a $\ZZ[G]$-module structure on $\ZZ[X]$. Indeed, elements $g$ act on $e_x$ via $ge_x = e_{gx}$. It's not that deep.

>[!idea]
>In the case that $X = G$, note that $\ZZ[X] = \ZZ[G]$ is exactly the ring $\ZZ[G]$... as a left module over itself. Nothing surprising.

For any family $(X_\lambda)_{\lambda\in \Lambda}$ of sets,$$\ZZ\left[\bigsqcup_{\lambda\in \Lambda} X_\lambda\right] \cong \bigoplus_{\lambda\in \Lambda} \ZZ[X_\lambda].$$In the case that $(X_\lambda)$ is actually a bunch of $G$-sets, then this also induces an isomorphism of $\ZZ[G]$-modules. This is pretty stupid; they're both direct sums.

# Free $G$-sets

Suppose now that $X$ is a free $G$-set, meaning $X\cong \bigsqcup_{\lambda \in \Lambda} G$ as $G$-sets for some index set $\Lambda$. (In other words, you have a bunch of $(g, \lambda)$ which get rotated within themselves by $G$). The resulting $\ZZ[G]$ module, $\ZZ[X]$, is just$$\ZZ[X] \cong \ZZ[G]^{\oplus \Lambda}.$$In other words, we can find a basis $e_{h,\lambda}$ such that the action of $g$ is just $e_{h,\lambda}\to e_{gh,\lambda}$.