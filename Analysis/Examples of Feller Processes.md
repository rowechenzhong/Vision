# Jump Processes on a Finite State Space

If $\abs{E} < \infty$ with discrete topology, all cadlag $f\in D(E)$ are of the following form:

![[Pasted image 20240422144120.png]]

The $T_i$ form an increasing sequence of stopping times. By Markov, we really only need to discuss the distribution of $(T_1, X_{T_1}$. The main results:

> [!claim] Wait along an exponential process, and then jump independently of how long you waited.
> Under $P_x$, there is some real number $q(x)\geq 0$ such that $T_1$ is $q(x)$-exponential. If $q(x) > 0$, then $T_1$ and $X_{T_1}$ are independent under $P_x$.
> 
> Recall that a $\lambda$-exponential RV has distribution $\PP(U > r) = e^{-\lambda r}$. If $r = 0$, then $U = \infty$ a.s.; such a state is absorbing.

We assume $q(y) > 0$ everywhere now.

>[!claim] Generator (Informal)
>Let $\Pi(x,y) = \PP_x(X_{T_1} = y)$. Note that $\Pi(x,\bullet)$ is a probability measure and $\Pi(x,x) = 0$.
>
>The generator $L$ has domain $D(L) = C_0(E) = B(E)$. For every $\phi\in B(E)$ and $x\in E$,$$L\phi(x) = \sum_{y\in E} L(x,y) \phi(y),\qquad L(x,y) = \begin{cases}
>q(x)\Pi(x,y) & y\neq x\\
>-q(x) & y = x
>\end{cases}$$

$L(x,y)$ is the instantaneous rate of transition from $x$ to $y$.

>[!claim] 18.615 (Informal)
>The jump times $T_1 < T_2 < \dots$ are all finite $\PP_x$-AS, and $X_{T_i}$ form a discrete Markov chain with TK $\Pi$. Conditioned on $(X_{T_i})$, $(T_{i+1} - T_i)$ are still independent and $q(X_{T_i})$-exponentially distributed.

# Levy Processes

>[!definition] Levy Process
>A ==**pre-Levy Process**== $Y$ is a real process such that:
>1. $Y_0 = 0$ a.s.
>2. For every $0\leq s \leq t$, $(Y_t - Y_s)\pperp \sigma(Y_r: 0\leq r \leq s)$, and $Y_t - Y_s$ has the same law as $Y_{t-s}$.
>3. $Y_t\to 0$ in probability as $t\downarrow 0$.
>   
> Then, for all $t\geq 0$, we can let $Q_t(0,dy)$ be the law of $Y_t$. For all $x\in \RR$, we can let $Q_t(x,dy)$ be the image of $Q_t(0,dy)$ under translation.
> 
> This collection forms a Feller semigroup, and thus $Y$ is a Feller process. A ==**Levy Process**== is a cadlag modification.

Example: Brownian motion.

# Continuous-State Branching Processes

Imagine cell growth. Okay, define this object.

>[!definition] CSBP
>A ==**Continuous-State Branching Process**== is a Markov process such that for each $x,y\in \RR_+$ and $t\geq 0$,$$Q_t(x,\bullet)* Q_t(y, \bullet) = Q_t(x+y,\bullet).$$
>
>Here, $*$ means convolution.

Notably, $Q_t(0,\bullet) = \delta_0$ for every $t\geq 0$. Also, if $X,X'$ are two independent CSBPs with the same semigroup, then $X + X'$ is also a CSBP with semigroup $Q$.

These processes are also well-understood. Notably, if:
1. $Q_t(x,\{0\}) < 1$ for every $x > 0$ and $t > 0$ (i.e., populations don't just die for small enough $x$).
2. $Q_t(x,\bullet)\to \delta_x(\bullet)$ as $t\downarrow 0$ in [[Random Measure|weak convergence of probability measures]], i.e. you don't do infinitely many things in finite time.
then $Q$ is Feller.