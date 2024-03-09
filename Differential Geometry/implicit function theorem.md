$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
We are working in a [[banach]] space.

>[!theorem] Implicit Function Theorem
>Suppose $U\subset V$ and $f:U\to W$ is a smooth map. Suppose for some $x\in U$, $f(x) = y$, $D_xf$ is surjective, and $\ker(D_xf)$ admits a closed complement $C$.
>
>Then, there are neighborhoods $0\in U_1\subset \ker(D_x(f))$ and $0\in U_2\subset W$, and diffeomorphisms (charts!) $\phi:U_1\times U_2\to U$ and $\psi:U_2\to W$ such that $\psi p_2 = f\phi$, where $p_2$ is projection onto $U_2$.

WLOG $x = y = 0$; these values don't actually matter anyways. A typical point in $U = \ker(D_xf)\oplus C$ is $k\oplus c$. Note that $C$ is banach.



TODO: go back and reconcile these several different variants of the same theorem.

>[!theorem]
>Suppose $f: \RR^{n + m}\to \RR^m$ is a continuously differentiable function. Let $\RR^{n + m}$ have coordinates $(\vec{x}, \vec{y})$. Fix a point $(\vec{a}, \vec{b})$ with $f(\vec{a}, \vec{b}) = \vec{0}$. Consider the portion of the [[Jacobian matrix]] containing the partial derivatives with respect to $\vec{y}$, only. If
>$$
>	J_{f,\vec{y}}(\vec{a},\vec{b}) = \left[ \frac{\pa f_i}{\pa y_j}(\vec{a}, \vec{b})\right]
>$$
>is invertible, then there exists:
> - An open set $U\subset \RR^n$ containing $\vec{a}$.
> - A function $g:U\to \RR^m$ such that $g(a) = b$ and $f(\vec{x}, g(\vec{x})) = 0$ for all $x\in U$.
>   
>  Furthermore, if $f$ is $C^k$/RA, $g$ can be made $C^k$/RA. Finally, analogous statements hold for CA $f$.

In multivariable calculus, the ==**implicit function theorem**== is a tool that allows relations to be converted to functions of several real variables. It does so by representing the relation as the graph of a function. There may not be a single function whose graph can represent the entire relation, but there may be such a function on a restriction of the domain of the relation. The implicit function theorem gives a sufficient condition to ensure that there is such a function.

>[!problem] Inverse Function
>Show that if $f:\RR^n\to \RR^n$ is continuously differentiable with invertible Jacobian at $\vec{a}$, there exists an open neighborhoods $U$ and $V$ of $\vec{a}$ and $f(\vec{a})$ and function $g:V\to \RR^n$ such that $f(g(x))=x$ for all $x\in V$ and $g(f(x)) = x$ for all $x\in U$.

>[!solution]
>Well, the function $h:\RR^n\times \RR^n\to \RR^n: h(x,y) = x - f(y)$ is certainly a continuously differentiable function, and the portion of its Jacobian specified in the problem is invertible. Thus, there exists an open neighborhood $V$ of $f(\vec{a})$ and function $g$ such that $f(g(x)) = x$ for all $x\in V$. We also know that $g(f(g(x))) = g(x)$ for all $x\in V$-- but $g(x)$ contains an open ball around 



>[!idea]
>I have written this in a basis because this appears to be the common presentation. This is painful.


>[!theorem] Philosophically Correct Statement
>Suppose $f: V\oplus W \to Y$ is a continuously differentiable function. Fix a point $(v,w)$ with $f(v,w) = 0$; by differentiability, $Df: V\oplus W \to Y$ exists. There exists the natural inclusion $\iota: W\to V\oplus W$. If $Df\circ \iota$ is invertible, then there exists:
> - An open set $U\subset V$ containing $v$.
> - A function $g:U\to Y$ such that $g(a) = b$ and $f(x, g(x)) = 0$ for all $x\in U$.