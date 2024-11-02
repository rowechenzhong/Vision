>[!theorem] Wiener
>For all $d\geq 1$ and all $x\in \RR^d$, there exists a unique probability measure $W$ (called the ==**Wiener Measure**==) on $(W_d, \mathcal{W}_d)$ such that the coordinate process $(x_t)_{t\geq 0}$ is a Brownian motion starting from $x$.

If we have already constructed a [[Brownian Motion]], this is simple. We consider the mapping $\Omega\to C(\RR_+, \RR)$ via $\omega\mapsto (t\mapsto B_t(\omega))$, which is measurable. Then, the Wiener measure is the pushforward of $\PP(d\omega)$ under this mapping.

>[!proof] Proof ideas from 676
>You instead just observe that Brownian motion exists, and this is its pushforward. $W(B_{t_1}\in A_1,\dots)$ is some finite-dimensional marginal which was already specified for you; this means that you know the measure on a $\pi$-system, thus $W$ is unique.

With this in mind, if we pick $\Omega = C(\RR_+, \RR)$, $\FFF$ as described in [[Continuous Random Process Definitions]], and $\PP(dw) = W(dw)$, then the ==**canonical process**== $X_t(w) = w(t)$ yields a BM; this is the ==**canonical construction**==.

# Deprecated

>[!proof] Proof ideas
> Uniqueness is clear because of the definition of Brownian motion (we already have any finite distribution, and its continuous, shrug). The existence part starts with the dyadic construction to create your Brownian-distributed $(\xi_u)_{u\in \mathbb{D}}$ . You apply [[Kolmogorov's Criterion]] with any $\alpha > 2$ ($\alpha = 2$ doesn't work, because then $\beta = 0$) to find a continuous extension $X$. Then, the key idea to establish independence is that for any event $A\in \FFF_s^X$, one can find a $\tilde{A}\in \sigma(\xi_u : u\in \mathbb{D}, u \leq s)$ such that $\PP(A = \tilde{A}) = 1$.

**This theorem is really strong, because it sets down the mathematical formalism for the Path Integral!**

We can now do things in the PI picture, e.g. we can consider "functionals" (bounded measurable functions on $W_d$). Letting $f(x) = \int_{W_d} F(w) W(dw)$ be the expected value of $F$ given you started at $x$, $f$ is measurable and $\EE[F(X) | \FFF_0] = [f(X_0)]$.

> [!proof]- Why is this last statement true: lots of waffles
> This is intuitively obvious right. $\FFF_0$ will describe all the information you need to determine $X_0$, and $f$ is thus $\FFF_0$-measurable.
> 
> What exactly is happening here. $w$ is completely described by its starting point $X_0$ and its evolution, which is encapsulated in $W(dw)$. So we're just saying that if you condition on knowing what $X_0$ was, $\EE[F(x)]$ will just look like $f(X_0)$. And this should be clear, because $f(x) = \EE_{W}[F(w)]$ or something. Aiyah. $W$ is defined by $\mu(A) = \PP(X\in A)$, its the pushforward $\PP\circ X^{-1}$. What is happening now. $\EE[X^{-1}(F(w))]$ or something.
> 
> Ugh. Okay, here's exactly what I need to show. First, I need to show $f(X_0)$ is $\FFF_0$-measurable. Then, let $A\in \FFF_0$. I need to show that $\EE[F(x)\id_A] = \EE[f(X_0)\id_A]$.
> 
> Why is $\int_{W_d} F(w) W(dx)$ -- oh wait this is just a function from $\RR$ to $\RR$. The claim is that its measurable. $F$ is just any bounded measurable function $W_d\to \RR$. But $x$ parameterizes a distribution, that's annoying. But suppose I just take $\mu_0$ and  then use $F(w - x)$; surely that's completely fine. This is legal, because you can look at the definition of $W(dx)$. Then this should be measurable right. We have a function called $F(w - x): W_d\times \RR\to \RR$, which is bounded, and measurable (its measurable because its a measurable composition, and surely $w - x$ is measurable). The Fubini's theorem has got to apply; specifically the subset of Fubini that says the intermediate integral is measurable at all. Okay sure and then $X_0$ is clearly $\FFF_0$-measurable, thus the whole thing is. Great.
> 
> Now, claim:$$\EE[F(X)\id_A] = \EE[f(X_0)\id_A]$$come on are you serious, this has to be completely obvious. We also have the condition (remember) that $X_t - X_0$ is independent of $\FFF_s$. So we've got to use
> $$\EE[F((X - X_0) + X_0)\id_A].$$Uhhhh okay. And clearly $(X - X_0)$ is Brownian motion starting at $X_0$, independent of $X_0$. The fact that these are independent means what.$$\EE[\EE_{X - X_0}[F((X - X_0) + X_0)]\id_A]$$like surely right, why can't I just say something like this.
> 
> Anyways, moving on.
>