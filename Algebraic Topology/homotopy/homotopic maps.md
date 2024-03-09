$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
> [!definition] Homotopic Maps
 Two maps $f_0$ and $f_1$ from $X$ to $Y$ are ==**homotopic**==, denoted $f_0\simeq f_1$, if there exists a continuous map $F: X\times I\to Y$ such that $F(x, 0)=f_0(x)$ and $F(x, 1)=f_1(x)$ for all $x\in X$. 

Also see [[homotopic paths]].

> [!idea] 
 If $X,Y$ are [[pointed spaces|pointed]], i.e. $f_0, f_1: (X, x_0)\to (Y, y_0)$, then we require $F(x_0, t) = y_0$ for all $t\in I$. This generalizes to multiple points. In the case of path homotopies, $x_\alpha \in \{0,1\}$ were special, for instance. 

 Now, we should take some time to prove that homotopic maps, as an equivalence relation, behave exactly as desired within the algebra of continuous maps.

> [!problem] Everything Works
> Show that: 
>  -  $\simeq$ is an equivalence relation (this should be identical to the path case). 
>  
>  -  If $f_0, f_1 : X\to Y$ are homotopic, for all $g:Y\to Z$ and $h:W\to X$, we have $g\circ f_0 \simeq g\circ f_1$ and $f_0\circ h\simeq f_1\circ h$. 
>  
>  

> [!solution]- 
 $f\simeq f$, because one can pick $F(x,t) = f(x)$. $f\simeq g \implies g\simeq f$, because one can pick $G(x,t) = F(x, 1-t)$. If $f_0\simeq f_1$ via $F(x,t)$ and $f_1\simeq f_2$ via $G(x,t)$, then $f_0\simeq f_2$ via $H(x,t) = F(x, 2t)$ for $t\in [0,1/2]$ and $H(x,t) = G(x, 2t-1)$ for $t\in [1/2, 1]$. Thus, we can speak of homotopy equivalence classes of maps $X\to Y$. Now, suppose $f_0\simeq f_1$ via $F(x,t)$. Then $gf_0 \simeq gf_1$ via $G(x,t) = g(F(x,t))$, and $f_0h\simeq f_1h$ via $H(x,t) = F(h(x), t)$. All of the above is true for pointed spaces as well; the worldline of the basepoint is fixed.