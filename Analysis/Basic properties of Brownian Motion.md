Consider a [[Brownian Motion with Filtration]].

>[!claim] Simple Markov Property
>If $X_t$ is standard BM, for all $s\geq 0$, $(B_{s+t} - B_s)_{t\geq 0}$ is a standard BM independent of $\FFF_s$.

This is obvious.

>[!claim] Less simple Markov Property
>Actually, $(B_{s+t} - B_s)_{t\geq 0}$ is a standard BM independent of $\FFF_{s+}$.

This is because $B_{s+t} - B_s = \lim_{\eps\to 0} B_{s+t+\eps} - B_{s+\eps}$ by continuity, and limits preserve independence (which is obvious by considering the sigma algebras or something).

> [!theorem] Blumenthal
> Suppose $A\in \FFF^X_{0+}$. Then $\PP(A)\in \{0,1\}$.

Indeed, $A\in \sigma(B_t: t\geq 0)\pperp \FFF_{0+}$, thus just like [[Kolmogorov's Zero-One Law]] you win.

>[!claim] Strong Markov Property
>For any [[Stopping Time]] $T$ with $\PP(t < \infty) > 0$, set $B_t^{(T)} = \id_{T < \infty}(B_{T+t} - B_T)_{t\geq 0}$. Under the probability measure $\PP(\bullet | T < \infty)$, $B_t^{(T)}$ is a standard Brownian motion $\pperp \FFF_T$.

> [!proof] Dyadic on $T$ to make it countable, then remember definitions.

# Example Applications

>[!example] Brownian motion crosses $0$ i.o. near $0$.
>Almost surely:
> - For all $\eps > 0$, $\sup(B_s: s\in [0,\eps) > 0$ and $\inf(B_s: s\in [0,\eps) < 0$.
> - $\forall a\in \RR$, $T_a = \inf_{t\in \RR} B_t = a$ is finite (i.e. $\lim\sup B_t = +\infty$ and $\lim\inf B_t = -\infty$).

The first one is trivial. The second one observes that$$1 = \lim_{\delta\to 0} \PP\left(\sup\left\{B_s:s\in [0,1]\right\}\right)\geq \delta) = \lim_{\delta\to 0} \PP\left(\sup\left\{B_s:s\leq \left(\frac{a}{\delta}\right)^2\right\}\right)\geq a = \PP(T_a < \infty).$$Very cool!

An application of the strong markov property:

>[!example] Reflection Principle
>Let $S_t = \sup\{B_s: s\leq t\}$. Then, for all $0\leq a$ and $b\leq a$, $\PP(S_t \geq a, B_t\leq b) = \PP(B_t \geq 2a - b)$.

This is trivial, cool though.