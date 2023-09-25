$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}$
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

