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
By replacing homomorphisms with [[homotopy|homotopies]], one can greatly generalize the notion of a space.

The identity function $X\to X$ is now expanded to an entire homotopy class. In this sense, the notion of an inverse must be broadened. We say that $f:X\to Y$ is a ==**homotopy equivalence**== (read: \"invertible in the homotopic sense\") if there exists $g:Y\to X$ such that $g\circ f\simeq \id_X$ and $f\circ g\simeq \id_Y$. 

If any such homotopic equivalence exist between two spaces $f:X\to Y$, then we say that $X$ and $Y$ have the same ==**homotopy type**==, and write $X\simeq Y$. 
 
> [!idea] 
Homotopy Theory cannot discern between spaces that are homotopy equivalent.
 
> [!idea] 
 As is standard in these category-theoretic type situations, the objects are second-class citizens, with their properties governed by the morphisms between them. 

> [!problem] 
 Show that $gf \simeq \id_X$ and $fh \simeq \id_Y$ implies $g\simeq h$; this is pure symbol-pushing.
 >
 Thus $f$ is a homotopy equivalence if and only if there exist $g,h$ such that $g\circ f\simeq \id_X$ and $f\circ h\simeq \id_Y$.
 >
 >One last exercise: $f:X\to Y$ is a homotopy equivalence iff there exist $g:W\to X$, $h:Y\to Z$ such that $gf$ and $fh$ are homotopy equivalences. 
 >
 >Push the symbols around until you're comfortable with them; they're literally just arrows.
 
> [!problem] 
 Show that homotopy type is an equivalence relation. 

> [!idea] 
Homotopy equivalence of spaces is a much coarser classification than homeomorphism of spaces (clearly homeomorphisms are homotopy equivalences).

> [!example] Contractible
 Spaces that are homotopy equivalent to a point are called ==**contractible**==. Examples include: 
>  
>  
>  
>  -  $\RR^n$ for any $n$. 
>  
>  -  Any convex subset $X\subset \RR^n$. 
>  
>  

> [!example] Circle
 The Mobius band and cylinder are homotopy equivalent to a circle. We show this for a cylinder $[0,1]\times \CC^1$; the Mobius band is similar. Indeed, let $f: [0,1]\times S^1\to S^1$ via $(r,\theta)\to \theta$, and let $g$ send $\theta \to (0, \theta)$. Then, $f\circ g$ sends $(r,\theta)\to (0,\theta)$, which is homotopy equivalent to the identity via $\gamma_t(r,\theta) = (rt,\theta)$ and $g\circ f$ is literally the identity. 

> [!example] Punctured Torus
 The once-punctured surface of genus $g$ is homotopy equivalent to a wedge of $2g$ circles. 
