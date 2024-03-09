$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
For $x\in \fg$, the [[Commutator|commutator]] defines a linear map $\ad_x:\fg\to \fg$ via $\ad_x(y) = [x,y]$. The claim is that this is actually [[Various Adjoint maps|the same adjoint as before]]; this is a key part of the bridge, and can be boxed as an [[interface]].

>[!theorem] Adjoint Coincidence
>$$
>	[x,y] = \left.\frac{\der}{\der t}\right|_{t = 0} \Ad_{\exp(xt)}(y)
>$$
# Proof

>[!claim] Express the commutator in terms of limits
> Fix $x$ and $y$. We launch two curves out of $1$ in the $x$ and $y$ directions: let $X(t)$ and $Y(s)$ be parameterized curves on $G$ such that $X(0) = Y(0) = 1$, $X'(0) = x$, and $Y'(0) = y$. 
> 
> Then,
>$$
> 	[x,y] = \lim_{s,t\to 0} \frac{\log(X(t)Y(s)X(t)^{-1}Y(s)^{-1})}{ts}
> $$
> 
> Thus, for instance,
> $$
> 	[x,y] = \lim_{s,t\to 0} \frac{\log(\exp(tx)\exp(sy)\exp(tx)^{-1}\exp(sy)^{-1})}{ts}
> $$

>[!proof]- Not that deep.
> Recall [[How to invert the commutator]].
> Let $x(t) = \log X(t)$ and $y(t) = \log Y(t)$. Then,
> $$\begin{align*}
> 	\log\left(\exp(x(t))\exp(y(t))\exp(x(t))^{-1}\exp(y(s))^{-1}\right) &= [x(t), y(s)] + O(\dots)\\
> 	& = ts[x, y] + o(1)
> 	\end{align*}
> $$
> as $t,s\to 0$.

Recall that
$$
Ad_{\fg}(x)(y) = \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=s=0}
$$
This is equal to
$$
\begin{align*}
Ad_{\fg}(x)(y) &= \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\exp(ty)^{-1}\right)\right|_{t=s=0}\\
&= \left.\frac{\der}{\der s}\left\{\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=0}\left.\exp(ty)\right|_{t=0}\right.\\
&+ \left.\left. \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right\}_{t=0} \frac{\der}{\der t}\exp(ty)^{-1}\right|_{s=0}\\
&= \left.\frac{\der}{\der s}\left\{\Ad_G(\exp(sx))(y) \right. - y\right\}\\
&= \Ad_\fg(x)(y)
\end{align*}
$$