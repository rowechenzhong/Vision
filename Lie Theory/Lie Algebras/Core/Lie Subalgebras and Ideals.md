$\require{physics}\newcommand{\cbrt}[1]{\sqrt[3]{#1}}\newcommand{\sgn}{\text{sgn}}\newcommand{\ii}[1]{\textit{#1}}\newcommand{\eps}{\varepsilon}\newcommand{\EE}{\mathbb E}\newcommand{\PP}{\mathbb P}\newcommand{\Var}{\mathrm{Var}}\newcommand{\Cov}{\mathrm{Cov}}\newcommand{\pperp}{\perp\kern-6pt\perp}\newcommand{\LL}{\mathcal{L}}\newcommand{\pa}{\partial}\newcommand{\AAA}{\mathscr{A}}\newcommand{\BBB}{\mathscr{B}}\newcommand{\FFF}{\mathscr{F}}\newcommand{\GGG}{\mathscr{G}}\newcommand{\HHH}{\mathscr{H}}\newcommand{\Ff}{\mathcal{F}}\newcommand{\Gg}{\mathcal{G}}\newcommand{\Hh}{\mathcal{H}}\DeclareMathOperator{\ess}{ess}\newcommand{\CC}{\mathbb C}\newcommand{\FF}{\mathbb F}\newcommand{\NN}{\mathbb N}\newcommand{\QQ}{\mathbb Q}\newcommand{\RR}{\mathbb R}\newcommand{\ZZ}{\mathbb Z}\newcommand{\KK}{\mathbb K}\newcommand{\SSS}{\mathbb S}\newcommand{\II}{\mathbb I}\newcommand{\conj}[1]{\overline{#1}}\DeclareMathOperator{\cis}{cis}\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}\DeclareMathOperator*{\range}{range}\DeclareMathOperator*{\nul}{null}\DeclareMathOperator*{\Tr}{Tr}\DeclareMathOperator*{\tr}{Tr}\newcommand{\id}{1\!\!1}\newcommand{\Id}{1\!\!1}\newcommand{\der}{\ \mathrm {d}}\newcommand{\Zc}[1]{\ZZ / #1 \ZZ}\newcommand{\Zm}[1]{\left(\ZZ / #1 \ZZ\right)^\times}\DeclareMathOperator{\Hom}{Hom}\DeclareMathOperator{\End}{End}\newcommand{\GL}{\mathbb{GL}}\newcommand{\SL}{\mathbb{SL}}\newcommand{\SO}{\mathbb{SO}}\newcommand{\OO}{\mathbb{O}}\newcommand{\SU}{\mathbb{SU}}\newcommand{\U}{\mathbb{U}}\newcommand{\gl}{\mathfrak{gl}}\newcommand{\sl}{\mathfrak{sl}}\newcommand{\so}{\mathfrak{so}}\newcommand{\su}{\mathfrak{su}}\newcommand{\uu}{\mathfrak{u}}\newcommand{\fg}{\mathfrak{g}}\newcommand{\hh}{\mathfrak{h}}\DeclareMathOperator{\Ad}{Ad}\DeclareMathOperator{\ad}{ad}\DeclareMathOperator{\Rad}{Rad}\DeclareMathOperator{\im}{im}\renewcommand{\BB}{\mathcal{B}}\newcommand{\HH}{\mathcal{H}}\DeclareMathOperator{\Lie}{Lie}\DeclareMathOperator{\Mat}{Mat}$
>[!thm]
>Suppose $H\subset G$ is a Lie subgroup with algebras $\hh$ and $\fg$. Then:
> - $\hh\subset \fg$ is a Lie subalgebra.
> - If $H \trianglelefteq G$ then  $\hh$ is a Lie ideal in $\fg$.
> - If $\hh$ is  a Lie ideal in $\fg$, and $G,H$ are connected, then $H\trianglelefteq G$.

> [!proof]- Subalgebra
> The claim is just that for any $x,y\in \hh$. $[x,y]\in \hh$. Well, for all sufficiently small $s,t$ we have
> $$
> 	\frac{1}{ts}\log(\underbrace{\exp(tx)\exp(sy)\exp(-tx)\exp(-sy)}_{\in H})\in \hh
> $$
> Thus the limit as $s,t\to 0$ is in $\hh$ too. It's not that deep. Alternatively, you can show this slightly more directly; we know that $[x,y] = \frac{\der}{\der t}\Ad_{\exp(xt)}y$ at $t = 0$, but $\Ad_G(\exp(xt))(\exp(sy))\in H$ for all $x,y,s,t$ so $\Ad_{\fg}(\exp(xt))$ points into $\hh$.
> 
> Basically, no problems here.

> [!proof]- Normal $\implies$ ideal
> Now, suppose $ghg^{-1}\in H$ for all $g\in G$, $h\in H$. Then, we wish to show that for all $x\in \fg$ and $y\in \hh$, $[x,y]\in \hh$. Okay, fine; this is the limit of
> $$
> 	\frac{1}{ts}\log(\underbrace{\exp(tx)\exp(sy)\exp(-tx)}_{\in H}\exp(-sy))\in \hh
> $$
> Alternatively, observe that once again $\Ad_G(\exp(xt))$ sends $H$ into $H$, and thus $\hh$ into $\hh$.

>[!claim] An Identity
>$\Ad_{\exp(x)} = \exp(\ad_\fg x)\in \GL(\fg)$.

> [!part]- (Annoying)
> I hope this is our final usage of actual diffeq. We prove this by parameterizing $x$ to $xt$.
> On one hand, we have $\Ad_{\exp(xt)}$. This guy follows the differential equation
> $$
> \begin{align*}
> 	\frac{\der}{\der t}\gamma(t) &= \frac{\der}{\der t}\Ad_{\exp(xt)}\\
> 	&=\left.\frac{\der}{\der \tau}\Ad_{\exp(x\tau)\exp(xt))}\right|_{\tau = 0}\\
> 	&= \left.\frac{\der}{\der \tau}\Ad_{\exp(x\tau))}\right|_{\tau = 0} \Ad_{\exp(xt)}\\
> 	&= \ad_\fg(x)\cdot \frac{\der}{\der \tau}(\exp(x\tau)) \Ad_{\exp(xt)}\\
> 	&= \ad_\fg(x)\Ad_{\exp(xt)}
> \end{align*}
> $$
> and $\Ad_{\exp(xt)}$ is $1$ when $t = 0$. But $\exp\left(t\ad_\fg x\right)$ also satisfies this diffeq. So we win.

> [!proof]- Ideal $\implies$ Normal
> Finally, if $[\fg, \hh] = \hh$, then we claim that $H\trianglelefteq G$. This is also clear; we know that for all small $x\in \fg$ and $y\in \hh$,
> $$
> 	\exp(x)\exp(y)\exp(x)^{-1} = \exp\left(\Ad_{\exp(x)} y\right)
> $$
> We want to show that $\Ad_{\exp(x)} y$ lies in $\hh$. According to the lemma it is $\exp(\ad_\fg(x))y$. Of course, $\ad_\fg(x) = [x,\bullet] \in \gl(\hh)$, so $\exp(\ad_\fg(x))\in \gl(\hh)$, and we conclude.