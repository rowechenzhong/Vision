# Indistinguishability vs Stochastic Equivalence

In measure theory, we've only ever cared about things up to measure $0$. When discussing random processes, this is the absolute baseline, but sometimes we need to blur the equivalence classes even further, due to the uncountability of $\RR$.

Two random processes $X,Y$ are ==**indistinguishable**== or **==equivalent up to evanescence==** if there is some $A\subset \Omega$ with probability $1$ such that $\forall \omega \in A$, ($X_t(\omega) = Y_t(\omega)$ on all $t\geq 0$). For all intents, this means that $X$ and $Y$ are *literally equal*; you should already understand this from basic probability.

>[!idea]- Pedantic Point
>In general, $\{\forall t\in T, X_t = Y_t\}$ is not measurable. But whatever, I want there to be a superset of this with measure $0$.

Two random processes $X, Y$ satisfying $\forall t$ ($X_t = Y_t$ almost surely) are called ==**versions**== of each other, ==**modifications**== of each other, or ==**stochastically equivalent**==. It is clear that in general, this is strictly weaker than being indistinguishable!

>[!idea]
>Stochastically equivalent processes cannot be distinguished by looking at countable collections of timesteps $t$. Thus, theorems which only cite individual points (which we will have very few of!) will hold up to modifications.

>[!example]
>Suppose $T$ is a random variable on $[0,1]$ (i.e., $T:\Omega\to [0,1]$ as usual). Consider $X = 1_{t = T}$ and $Y = 0$. $X$ is distinguishable from $Y$. $X$ is a version of $Y$.

The reason why (left/right)-continuous/cadlag processes are important is that they let us hold $X$ with a countable set of timesteps.

>[!claim] Left-continuous representatives of stochastic equivalences are indistinguishable
>Let $X,Y$ be *left-continuous* stochastically equivalent processes. Then, they are indistinguishable!

Left as an exercise, but this is a completely trivial bridge.

# Worldlines vs Foliations
Let $W_d = C([0,\infty), \RR^d)$. For $t\geq 0$, the coordinate function $x_t:W_d\to \RR^d$ simply sends $x_t(w) = w(t)$; it picks out the value of that trajectory at time $t$. This yields the natural sigma algebra $\mathcal{W}_d = \sigma(x_t, t \geq 0)$. Then, if we had some probability measure on $\mathcal{W}_d$, $(x_t)$ would be a random process.

Well, given any continuous random process $X$ on $\RR^d$, there is an obvious measurable map $X:\Omega\to W_d$ via $X(\omega)(t) = X_t(\omega)$. This yields a pushforward measure on $W_d$, $\mu(A) = \PP(X \in A)$, which tells you the law over trajectories.