Consider a [[Brownian Motion with Filtration]].

>[!claim] Simple Markov Property
>If $X_t$ is standard BM, for all $s\geq 0$, $(B_{s+t} - B_s)_{t\geq 0}$ is a standard BM independent of $\FFF_s$.

This is obvious.

>[!claim] Less simple Markov Property
>Actually, $(B_{s+t} - B_s)_{t\geq 0}$ is a standard BM independent of $\FFF_{s+}$.

>[!proof]- By continuity, plus details.
> By continuity, $B_{s+t} - B_s = \lim_{\eps\to 0} B_{s+t+\eps} - B_{s+\eps}$ pointwise. The claim is thus that limits preserve independence. This is basically true, but you have to be careful to talk about the measure-$0$ events. Observe that$$
> \{B_{s+t} - B_s \in (a,b)\}\subset \lim_{\eps\to 0} \{B_{s+t+\eps} - B_{s+\eps} \in (a,b)\}\subset \lim_{\eps\to 0} \{B_{s+t+\eps} - B_{s+\eps} \in [a,b]\}\subset \{B_{s+t} - B_s\in [a,b]\}.
> $$But the LHS and the RHS have the same measure. Thus, for any $A\in \FFF_{s+}$,$$\PP(B_{s+t} - B_s\in (a,b), A) = \lim_{\eps\to 0} \PP\left(B_{s+t+\eps} - B_{s+\eps}\in (a,b), A\right) = \lim_{\eps\to 0} \PP\left(B_{s+t+\eps} - B_{s+\eps}\right)\PP(A) = \PP\left(B_{s+t} - B_s\in (a,b)\right)\PP(A).$$This concludes.

> [!theorem] Blumenthal
> Suppose $A\in \FFF^X_{0+}$. Then $\PP(A)\in \{0,1\}$.

We just showed $\FFF_{0+}\pperp \sigma(B_t: t>0)$. By continuity, this $\sigma$-algebra is the same as $\sigma(B_t: t\geq 0)$.

> [!proof]- Really?
> The functions $f_n = B_{\frac1n}$ are $\FFF_{0+}$-measurable. Thus their limit is as well. But by path-continuity, this limit is just $B_0$. Thus $\{B_0\in A\}$ is $\FFF_{0+}$-measurable for all $A$.

But $\FFF_{0+} = \bigcap_\eps \FFF_{\eps}\subset \sigma(B_t: t \geq 0)$, so $\FFF_{0+} \pperp \FFF_{0+}$, thus just like [[Kolmogorov's Zero-One Law]] you win.

>[!claim] Strong Markov Property
>For any [[Stopping Time]] $T$ with $\PP(T < \infty) > 0$, set $B_t^{(T)} = \id_{T < \infty}(B_{T+t} - B_T)_{t\geq 0}$. Under the probability measure $\PP(\bullet | T < \infty)$, $B_t^{(T)}$ is a standard Brownian motion $\pperp \FFF_T$.

> [!proof]- Dyadic on $T$ to make it countable. (Sketch)
> First take $T < \infty$ everywhere. Take $T^k = 2^{-k}\ceil{2^k T}\geq T$ and $B^{(T,k)}_t = B_{T^k+t} - B_{T^k}$. It is immediate that $B^{(T,k)}_t$ are BM $\pperp \FFF_T$. They converge path-wise pointwise to $B^{(T)}_t$, and arguments similar to the less simple MP above conclude.
> 
> The $0 < \PP(T < \infty) < 1$ modification is harmless.

These are generalized to arbitrary Markov processes [[Strong Markov Property|here]].

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