>[!idea]
>See [[Wong Zakai Paper]]



We have now defined SDEs and proven the relevant $\exists !$ results. How do such equations actually correspond to physical phenomena, such as diffusion?

Let me jump straight to the main conclusions:
- The Ito integral is powerful because the integral of an arbitrary process against a CLM noise remains a CLM. In particular, such integrals do not *look into the future.* Effectively,$$
  (H\cdot X)_t = \lim \sum H_{t_{i-1}} (X_{t_i} - X_{t_{i-1}})
  $$One imagines that $X$ represents some signal, like a stock price. Your profit is the integral of your decisions $H$, which must all be made on $\FFF_{t_{i-1}}$ information before the $X_{t_{i}}$ in $\FFF_{t_i}$ drops.
- However, real world processes *do* look into the future. Consider a colloid suspended in a fluid, whose position is the integral of its velocity term, which is itself stochastically altered by microscopic interactions with the fluid. There is a microscopic but finite delay between any two impacts, corresponding to a finite relaxation time; your noise is not truly white, but colored.
  
  These situations are naturally the limit of a series of random *ordinary* integrals as relaxation time is taken to zero. Such integrals converge to the **Stratonovich** integral, which differs from the Ito integral by a FVP correction factor.

Okay stop waffling lets cook. Today, we are considering stationary stochastic differential equations of the form$$dX_t = b(X_t)dt + \sigma(X_t)dW_t$$where $b,\sigma$ are $K$-Lipschitz and $X_0 = x_0$ is non-random.

Suppose we have a series of piecewise continuous (so as to automatically admit Reimann integrals) random functions which approximate white noise, $\xi^n_t$. "White noise" is not a function in the usual sense, so what we mean is that if we define $W^n_t = \int_0^t \xi^n_s ds$, there exists an $m$-dimensional Wiener process $W_t$ such that$$
\sup_{t\in [0,T]} \norm{W_t - W_t^n}\to 0
$$almost surely.

>[!example] Dumb example I conjured
>Write down any interpolating function (increasing, continuous) $\sigma:[0,1]\to [0,1]$ with $\sigma(0) = 0$ and $\sigma(1) = 1$ (these conditions are not all necessary). Then, let $[t] = 2^{-k}\floor{t 2^k}$ and $\{t\} = t - [t]$, and $W^n_t = W_{[t]} + \sigma(2^k\{t\})(W_{[t]+2^{-k}} - W_{[t]})$.

Then, we might hope that the usual solution to the differential equation, $\frac{d}{dt}X^n_t = b(X^n_t) + \sigma(X^n_t)\xi^n_t$, coincides with the solution obtained from $dX_t = b(X_t)dt + \sigma(X_t)dW_t$.

Here's the easiest case:

> [!claim] When $\sigma$ is $x$-independent
> If $\sigma(x) = \sigma$ is constant, $\sup_{t\in [0,T]}\norm{X^n_t - X_t} \to 0$ almost surely.

>[!proof]- Gronwall smash
> Indeed,$$X^n_t - X_t = \int_0^t \left(b(X^n_s) - b(X_s)\right)ds + \sigma(W^n_t - W_t)$$thus by triangle inequality and Lipschitz,$$\norm{X^n_t - X_t}\leq K\int_0^t \norm{X^n_s - X_s}ds + \norm{\sigma} \sup_{t\in [0,T]}\left(W^n_t - W_t\right).$$The supremum goes to $0$ AS. Then, [[Gronwall's Lemma]] wins.

We expect this to be the case; your randomness is agnostic to $X$, so you simply don't look at the future despite having access.

# Wong-Zakai Theorem

In the case where $\sigma$ is a function of $X$, computations are joever very quickly. So let's make everything as simple as possible immediately.
- $X,W, X^n, \xi^n$ are scalars, $d = 1$.
- $b,\sigma$ are Lipschitz continuous as usual, but they're also *bounded* now $b,\sigma \leq L$.
- $\sigma$ is $C^1$ and $\sigma(x) \frac{d\sigma(x)}{dx}$ is Lipschitz continuous.
- There is some $\beta > 0$ such that $\sigma(x)\geq\beta > 0$ for all $x$.

In this case, we claim that the answer coincides with the Stratonovich SDE
$$\begin{align*}
dX_t &= b(X_t)dt + \sigma(X_t)\circ dW_t\\
&= b(X_t)dt + \sigma(X_t)dW_t + \frac12d\braket{\sigma(X_t), W_t}\\
&= b(X_t)dt + \sigma(X_t)dW_t + \frac12\sigma'(X_t)d\braket{X_t, W_t}\\
&= b(X_t)dt + \sigma(X_t)dW_t + \frac12\sigma'(X_t)\sigma(X_t)dt.
\end{align*}$$where $\sigma'(X_t)\sigma(X_t)$ is called the ==**Ito Correction Term**==, and is Lipschitz continuous so that we can use the above results. As before, $\frac{d}{dt}X^n_t = b(X^n_t) + \sigma(X^n_t)\xi^n_t$.

Then,

> [!claim] Nerfed Wong-Zakai
> $\sup_{t\in [0,T]} \abs{X^n_t - X_t}\to 0$ almost surely.

> [!proof]-
> We consider the function $\Phi(x) = \int_0^x \left(\sigma(y)\right)^{-1} dy$, which is well-defined and $C^2$, because $\sigma(y)$ is $C(1)$ and $\sigma(y) \geq \beta > 0$. Then,
> $$
> \frac{d}{dt} \Phi\left(X^n_t\right) = \left(\sigma(X^n_t)\right)^{-1} \left(b(X^n_t) + \sigma(X^n_t)\xi^n_t\right) = \frac{b(X^n_t)}{\sigma(X^n_t)}+\xi^n_t.
> $$
> 
> Meanwhile,$$
> \begin{align*}
> d\Phi(X_t)&=\sigma^{-1}(X_t)\left\{b(X_t)dt + \sigma(X_t)dW_t + \frac12\sigma'(X_t)\sigma(X_t)dt\right\} -\frac12\frac{\sigma'}{\sigma^2}\sigma(X_t)^2dt\\
> &= \sigma^{-1}\left(X_t\right)\left(b\left(X_t\right)dt + \sigma(X_t)dW_t\right)\\
> &= \frac{b(X_t)}{\sigma(X_t)}dt + dW
> \end{align*}
> $$because the Stratonovich integral obeys the chain rule. We now want to smash with Gronwall.$$
> \norm{\Phi\left(X^n_t\right) - \Phi(X_t)} \leq \int_0^t \abs{\frac{b(X^n_s)}{\sigma(X^n_s)} - \frac{b(X_s)}{\sigma(X_s)}}ds + \sup_{t\in [0,T]} \abs{W^n_t - W_t}.
> $$Now, because $\sigma$ is bounded by $L$, $\sigma^{-1}$ is bounded by $\frac1L$ from below, hence $\abs{\Phi(x) - \Phi(z)}\geq \frac1L\abs{x-z}$. Meanwhile,$$\abs{\frac{b(x)}{\sigma(x)} - \frac{b(z)}{\sigma(z)}} \leq \frac{1}{\sigma(x)}\abs{b(x) - b(z)} + \frac{b(z)}{\sigma(x)\sigma(z)} \abs{\sigma(x) - \sigma(z)}\leq \frac{K}{\beta}\abs{x - z} + \frac{LK}{\beta^2}\abs{x-z}.$$Gronwall kills now.

> [!idea]- What if I consider just applying Gronwall immediately
> $$
> X^n_t - X_t =  \int_0^t \abs{b(X^n_t) - b(X_t) - \sigma'(X_t)\sigma(X_t)} + \int_0^t \sigma(X^n_t)\xi^n_tdt - \int_0^t \sigma(X_t)dW_t
> $$
> You're dead; you needed to kill off the $\sigma$'s.

# Multidimensional Wong-Zakai Theorem

For entertainment (and my 676 final project) let me un-nerf this to the $d$-dimensional case. We use Einstein summation notation.
- $b: \RR^d\to B_0(L)$ is $K$-Lipschitz continuous and bounded by $L$.
- $\sigma: B_0(L)\setminus B_0(\beta)$ is $K$-Lipschitz continuous, bounded by $L$ and $\beta$.
- $b,\sigma$ are Lipschitz continuous as usual, but they're also *bounded* now $b,\sigma \leq L$.
- $\sigma$ is $C^1$ and $\sigma(x) \frac{d\sigma(x)}{dx}$ is Lipschitz continuous.
- There is some $\beta > 0$ such that $\sigma(x)\geq\beta > 0$ for all $x$.

In this case, we claim that the answer coincides with the Stratonovich SDE
$$\begin{align*}
dX^i_t &= b(X_t)^idt + \sigma(X_t)^i_\alpha\circ dW^\alpha_t\\
&= b(X_t)^idt + \sigma(X_t)^i_\alpha dW^\alpha_t + \frac12d\braket{\sigma(X_t)^i_\alpha, W^\alpha_t}\\
&= b(X_t)^idt + \sigma(X_t)^i_\alpha dW^\alpha_t + \frac12(D\sigma(X_t))^i_{\alpha j} d\braket{X_t^j, W^\alpha_t}\\
&= b(X_t)^idt + \sigma(X_t)^i_\alpha dW^\alpha_t + \frac12(D\sigma(X_t))^i_{\alpha j} d\braket{\sigma(X_t)^j_\beta dW^\beta_t, W^\alpha_t}\\
&= b(X_t)^idt + \sigma(X_t)^i_\alpha dW^\alpha_t + \frac12(D\sigma(X_t))^i_{\alpha j} \sigma(X_t)^j_\beta  \eta^{\beta \alpha}\\
&= b(X_t)^idt + \sigma(X_t)^i_\alpha dW^\alpha_t + \frac12(D\sigma(X_t))^i_{\alpha j} \sigma(X_t)^j_\alpha
\end{align*}$$where $\sigma'(X_t)\sigma(X_t)$ is called the ==**Ito Correction Term**==, and is Lipschitz continuous so that we can use the above results.

As before, $\frac{d}{dt}X^n_t = b(X^n_t) + \sigma(X^n_t)\xi^n_t$.

Then,

> [!claim] Nerfed ND Wong-Zakai
> $\sup_{t\in [0,T]} \norm{X^n_t - X_t}_2\to 0$ almost surely.

[!proof]-
We consider the function $\Phi(x) = \int_0^{x_i} \frac{\sigma(y)_i}{\sigma(y)^j\sigma(y)_j}dy$, which is well-defined and $C^2$, because $\sigma(y)$ is $C(1)$ and bounded. This function is designed solely such that $\frac{\pa \Phi}{\pa x_i} = \frac{\sigma(x)_i}{\sigma(x)_i\sigma(x)^i}$. Then,
$$
\frac{d}{dt} \Phi\left(X^n_t\right) = \frac{\sigma\left(X^n_t\right)^i}{\sigma\left(X^n_t\right)^j\sigma\left(X^n_t\right)_j} \left(b_i(X^n_t) + \sigma_i(X^n_t)\xi^n_t\right) = \frac{(\sigma\cdot b)(X^n_t)}{(\sigma\cdot \sigma)(X^n_t)}+\xi^n_t.
$$

Meanwhile,
$$
\frac{d}{dt} \Phi\left(X_t\right) = \frac{\sigma\left(X_t\right)^i}{\sigma\left(X_t\right)^j\sigma\left(X_t\right)_j} \left(b_i(X_t) + \sigma_i(X_t)dW_t + \frac12 (D\sigma)(X_t)_{ij}\sigma(X_t)^jdt\right) - \frac{\pa_k \sigma^i\left(\eta^{ij} \sigma^2 - 2\sigma^i\sigma^j\right)}{2\sigma^4}
$$


Meanwhile,$$
\begin{align*}
d\Phi(X_t)&=\sigma^{-1}(X_t)\left\{b(X_t)dt + \sigma(X_t)dW_t + \sigma'(X_t)\sigma(X_t)dt\right\} -\frac{\sigma'}{\sigma^2}\sigma(X_t)^2dt\\
&= \sigma^{-1}\left(X_t\right)\left(b\left(X_t\right)dt + \sigma(X_t)dW_t\right)\\
&= \frac{b(X_t)}{\sigma(X_t)}dt + dW
\end{align*}
$$because the Stratonovich integral obeys the chain rule. We now want to smash with Gronwall.$$
\norm{\Phi\left(X^n_t\right) - \Phi(X_t)} \leq \int_0^t \abs{\frac{b(X^n_s)}{\sigma(X^n_s)} - \frac{b(X_s)}{\sigma(X_s)}}ds + \sup_{t\in [0,T]} \abs{W^n_t - W_t}.
$$Now, because $\sigma$ is bounded by $L$, $\sigma^{-1}$ is bounded by $\frac1L$ from below, hence $\abs{\Phi(x) - \Phi(z)}\geq \frac1L\abs{x-z}$. Meanwhile,$$\abs{\frac{b(x)}{\sigma(x)} - \frac{b(z)}{\sigma(z)}} \leq \frac{1}{\sigma(x)}\abs{b(x) - b(z)} + \frac{b(z)}{\sigma(x)\sigma(z)} \abs{\sigma(x) - \sigma(z)}\leq \frac{K}{\beta}\abs{x - z} + \frac{LK}{\beta^2}\abs{x-z}.$$Gronwall kills now.