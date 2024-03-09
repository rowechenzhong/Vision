---

aliases:
  - covering maps and homology
---
$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$

Let $\pi: \tilde{X}\to X$ be a [[Regular Covering Spaces|regular]] covering map, with [[Deck Transformation|covering group]] $G$.

>[!claim]
>$C_*(\tilde{X})$ is a complex of free $\ZZ G$-modules, and $C_*(X) = \ZZ\otimes_{\ZZ G} C_*(\tilde{X})$.

$C_*(\tilde{X})$ is obviously a complex of free $\ZZ G$-modules, because $G$ consists of automorphisms of $\tilde{X}$. We wish to show that the map $p:C_*(\tilde{X})\to C_*(X)$ is surjective and has kernel $\{g \sigma \sim \sigma\}$. Well, $p$ is obviously surjective, because we can left any map $\Delta^n\to X$. $p$ obviously has said kernel, because:
- $p\circ \sigma = p\circ g\circ \sigma$.
- By [[unique lifting]], if $p\circ \sigma = p\circ \conj{\sigma}$, then there exists some $g\in G(X)$ such that $\sigma = g \circ \conj{\sigma}$.


By the [[Fundamental theorem of homology algebra]], $H_*(X) \cong H_*(\ZZ\otimes_{\ZZ G} C_*(\tilde{X}))$. Most notably, if $X$ is contractible, i.e. $C_*(\tilde{X})$ is some [[Free Resolution]] of $\ZZ$ as a $\ZZ G$ module, then $H_*(X) = H_*(\ZZ\otimes_{\ZZ G}C)$.

>[!idea]
>I don't actually understand this too well. Oh well! moving on.