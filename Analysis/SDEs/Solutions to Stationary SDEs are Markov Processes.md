We will assume Lipschitz-ness, so we can apply the expansive UE characterization written [[Lipschitz SDEs|here]].

Suppose now that $\sigma$ and $b$ do not change with time; this occurs in most simple physical problems as well as many interesting mathematical toys, all operating on a fixed background. One then expects that $X$ should evolve as a [[Markov Processes Homepage|markov process]]! This is true, and we can actually explicitly write down the kernels.

> [!theorem] Stationary SDEs are MPs
> Define semigroup $(Q_t)_{t\geq 0}$, where$$(Q_tf)(x) = \EE\left[f\left(X^x_t\right)\right] = \int f\left(F_x(w)_t\right) W(dw).$$Here, $X^x$ is an arbitrary solution of $E_x(\sigma, b)$.
> 
> Then, any solution $X$ to $E(\sigma, b)$ on some $(\FFF_t)$-filtered probability space is a $(\FFF_t)$-MP with TS $Q$.

(Finishing the proof is todo but it's trivial...)

>[!proof]- Show $Q$ satisfies MP relation
>We claim that
>$$\EE\left[f(X_{s+t}) | \FFF_s\right] = Q_tf(X_s).$$
>This is clear by truncating the integral
>$$
>	X_{s+t} = X_s + \int_s^{s+t} \sigma(X_r) dB_r + \int_s^{s+t} b(X_r)dr.
>$$

> [!proof]- Show $Q$ is a transition semigroup
> You should expect this. For every $f = \id_A$ for $\RR^d$-measurable $A$,
> $$
> Q_0(x, A) = (Q_0\id_A)(x) = \EE\left[\id_A(X^x_0)\right] = \id_A(x)
> $$
> thus $Q_0(x,dy) = \delta_x(dy)$ as desired.
> 
> For Chapman-Kolmogorov,$$
> Q_{t+s}f(x) = \EE\left[f\left(X^x_{s+t}\right)\right] = \EE\left[\EE\left[f\left(X^x_{s+t}\right)|\FFF_s\right]\right]= \EE\left[Q_t f\left(X^x_s\right)\right] = \int Q_s(x,dy)Q_tf(y)$$as desired.
> 
> $X^x_t$ depends continuously on $(x,t)$ by the Lipschitz SDE characterization. Hence,
> $$
> (t,x)\mapsto Q_t(x,A) = \EE\left[\id_A(X^x_t)\right]
> $$
> is measurable. Shrug. I think the mapping $X^x_t(w)\to \RR^d$ is supposed to be $(x,t,w)$-measurable.

And actually, we can do better.

>[!theorem] Stationary SDEs are Feller
>$Q$ is Feller, and the space of $C^2$ functions with compact support lie in the domain: $C^2_c(\RR^d)\subset D(L)$.
>
>For every $f\in C^2_c(\RR^d)$, we can actually compute $L$:
>$$
>Lf(x) = \frac12 \sigma_{ij}(x)\sigma_{kj}(x) \pa_i\pa_k f(x) + b_i(x)\pa_i f(x).
>$$

>[!proof]- Here's why this works intuitively.
> By Ito applied to $f$ on
> $$X^x_{t,i} = x_i + \int_0^t \sigma_{ij}(X^x_s)dB^j_s + \int_0^t b_i(X^x_s)ds,$$
> we get
> $$
> \begin{align*}
> df(X^x)_t &= \pa_i f(X^x_t) dX^x_t + \pa_i\pa_j f(X^x_t)d\braket{X^x_i, X^x_j}_t\\
> &=\pa_i f(X^x_t) \left(\sigma_{ij}(X^x_t) dB^i_t + b_i(X^x_s)dt\right)\\
> &\quad+ \pa_i\pa_j f(X^x_t)\sigma_{ik}(X^x_t)\sigma_{j\ell}(X^x_t)d\braket{B^k, B^l}_t\\
> &=\pa_i f(X^x_t) \left(\sigma_{ij}(X^x_t) dB^i_t + b_i(X^x_t)dt\right)\\
> &\quad+ \pa_i\pa_j f(X^x_t)\sigma_{ik}(X^x_t)\sigma_{jk}(X^x_t)dt
> \end{align*}
> $$
> Hence, extracting the FVP component
> $$
> 	g(x) = \sigma_{ij}(x)\sigma_{kj}(x) \pa_i\pa_k f(x) + b_i(x)\pa_i f(x),
> $$
> we see that $M_t = f\left(X^x_t\right) - f(x) - \int_0^t g\left(X^x_s\right)ds$ is a CLM. Hence, at least in the case where $f,g$ are bounded, $M$ is a true martingale. By [[Feller Semigroups|the theorem on how to identify L]], we obtain that $Lf = g$.

In particular, all solutions to $E(\sigma, b)$ satisfy the strong markov property.