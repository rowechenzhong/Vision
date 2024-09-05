# On the Convergence of Ordinary Integrals to Stochastic Integrals

### Setup
The following types of approximations to BM will be considered. Each includes the conditions of the previous.
1. For almost all $\omega$, $y_n(t,\omega)\to y(t,\omega)$ for all $t\in [a,b]$. $y_n(t,\omega)$ are path-continuous and of bounded variation, which I take to mean they are FVPs.
2. For almost all $\omega$, there exist **finite real numbers** $n_0(\omega)$ and $k(\omega)$ such that for all $n > n_0$ and all $t\in [a,b]$, $\abs{y_n(t,\omega)}\leq k(\omega)$. Note that $n_0(\omega)$ doesn't have to be constant on $\omega$, so this is an interesting assumption.
3. For (almost?) all $\omega$, $y_n(t,\omega)$ has piecewise continuous derivative in $t$.
4. For (almost?) all $\omega$, $y_n(t,\omega)\to y(t,\omega)$ uniformly on $[a,b]$.

### Stochastic Integrals

> [!theorem] Integrals against brown noise $\to$ Stratonovich against BM
> Let $\psi(\eta, t)$ have continuous partial derivatives on $\RR\times [a,b]$. Let $y_n(t)$ be an approximation of a BM satisfying $A_2$. Then, almost surely,
> $$
> \lim_{n\to \infty} \int_a^b \psi(y_n(t), t)dy_n(t) = \int_a^b \psi(y(t), t)\circ dy(t)
> $$
> 
> If $\psi(\eta, t) = \psi(\eta)$ is independent of $t$, then this holds with $A_1$.

As a reminder, this Stratonovich integral is
$$
\int_a^b \psi(y(t), t)dy(t) + \braket{\psi(y(t),t), y(t)}_a^b = \int_a^b\psi(y(t), t)dy(t) + \frac12 \int_a^b\frac{\pa\psi}{\pa \eta}(y(t),t) dt$$

To prove this, we allow $F(\lambda, t) = \int_a^\lambda \psi(\eta, t)d\eta$. This is a $C^2$ function in $\lambda$ which we can hopefully apply Ito's formula to. Then,$$F(y_n(b), b) - F(y_n(a),a) = \int_a^b \psi\left(y_n(t), t\right) dy_n(t) + \int_a^b \left(\frac{\pa F}{\pa t}\right)(y_n(t), t)dt.$$This is simply true for almost all $\omega$, by the Fundamental theorem of calculus, as $(y_n(t), t)$ is continuous.

>[!idea]- Irrelevant Waffles
> Now, $\int_a^b \psi\left(y_n(t), t\right) dy_n(t)$ is the function of $\omega$ of interest. We would like to apply dominated convergence theorem to it, $\omega$-pointwise.
> - First off, why is it measurable? Well, $(\omega,t)\mapsto (y_n(t),t)\mapsto \psi(y_n(t), t)$ is measurable. It's clearly adapted. It's path-continuous, and thus progressive. Thus the integral is another finite variation process. Those are just some thoughts.
> - Notably, $t\mapsto \psi(y_n(t), t)$ is measurable because its actually continuous. Fine.
> - What the heck are we dominated convergence theorem-ing. Do the measures associated with $y_n(t)$, which we'll call $\mu_n$, converge set-wise or something. They definitely convergence for all sets $[0,t]$ $\omega$-almost surely; $\mu_n([0,t]) = y_n(t)\to y(t) = \mu([0,t])$. Do they thus converge on all Borel sets? This is an algebra. Why is it a monotone class?

Now, the main reason we did all of this was because it is very hard to compute $\lim_{n\to \infty} \int_a^b \psi\left(y_n(t), t\right) dy_n(t)$ in any sense. Your finite variation process is supposed to converge to a CLM, and Portmanteau / Dominated convergence theorem / etc don't cut it. The above $\omega$-pointwise equality lets us rewrite this integral in terms of three very smooth well-understood objects.

First off, $F(y_n(b), b) - F(y_n(a), a)\to F(y(b), b) - F(y(a), a)$ everywhere, because $y_n\to y$ and $F$ is continuous.

Next, we claim that for almost all $\omega$,$$\int_a^b \left(\frac{\pa F}{\pa t}\right)(y_n(t), t)dt\to \int_a^b \left(\frac{\pa F}{\pa t}\right)(y(t), t)dt. \tag{$\star$}$$
> [!proof]- Boring
> $F$ is $C^1$, thus
> $$\frac{\pa F}{\pa t}(\lambda, t) = \int_a^\lambda \frac{\pa \psi(\eta, t)}{\pa t} d\eta$$
> 
> Note that if $\psi$ is independent of $t$, we immediately conclude.
> 
> So, fix an $\omega$. Observe that $\frac{\pa \psi(\eta, s)}{\pa s}$ is continuous everywhere, and thus bounded by say $K$ on $[-k(\omega), k(\omega)]\times [a,b]$.
> 
> Fix a $a\leq t\leq b$. We'll show that $\left(\frac{\pa F}{\pa t}\right)(y_n(t), t)$ converges. Look at
> $$
> \int_a^{y_n(t)} \frac{\pa \psi(\eta, t)}{\pa t}d\eta = \int_a^{k(\omega)} \id_{\eta \leq y_n(t)} \frac{\pa \psi(\eta, t)}{\pa t}d\eta 
> $$
> 
>  Thus, for these clearly converge almost surely to $\left(\frac{\pa F}{\pa t}\right)\left(y(t), t\right)$. This is true for each fixed $t$. Hence, because $\frac{\pa F}{\pa t}(y_n(t), t)$ and $\frac{\pa F}{\pa t}(y(t), t)$ are each continuous functions, they converge pointwise on $[a,b]$ almost surely. Now, for each $t$, $\frac{\pa F}{\pa t}(y_n(t), t)$ is dominated by
> $$
> \int_a^{k(\omega)} K d\eta  = k(\omega - a)K < \infty.
> $$
> Hence we conclude.

Now, by Ito's formula, we know that $F(y_n(b), b) - F(y_n(a), a)$ converges to$$
\int_a^b \psi(y(t), t)dy(t) + \int_a^b \left(\frac{\pa F}{\pa t}\right)(y(t), t)dt + \frac12 \int_a^b \frac{\pa \psi}{\pa \eta}(y(t),t)dt
$$
Plugging in $\star$, we conclude.

Awesome. Let's repeat this proof for a more general setup.

### More General Integrals

This time, let $x(t)$ be a CSM. $\psi$ still has continuous partial derivatives on $\RR\times [a,b]$. Construct FVPs $x_n(t)$ such that for almost all $\omega$:
1. $x_n(t,\omega)\to x(t,\omega)$ for all $t\in [a,b]$.
2. There exist **finite real numbers** $n_0(\omega)$ and $k(\omega)$ such that for all $n > n_0$ and all $t\in [a,b]$, $\abs{x_n(t,\omega)}\leq k(\omega)$.

> [!theorem] Integrals against FVP approximations $\to$ Stratonovich against CSM
> Almost surely,
> $$
> \lim_{n\to \infty} \int_a^b \psi(x_n(t), t)dx_n(t) = \int_a^b \psi(x(t), t)\circ dx(t).
> $$
 
As a reminder, this Stratonovich integral is
$$
\int_a^b\psi(y(t), t)dy(t) + \frac12 \int_a^b\frac{\pa\psi}{\pa \eta} d\braket{\psi(x(t), t), x(t)}$$

>[!proof]- The proof is identical to last time
> Write $F(\lambda, t) = \int_a^\lambda \psi(\eta, t)d\eta$ again. Then,$$F(x_n(b), b) - F(x_n(a),a) = \int_a^b \psi\left(x_n(t), t\right) dx_n(t) + \int_a^b \left(\frac{\pa F}{\pa t}\right)(y_n(t), t)dt.$$
> Identically to last time, $F(x_n(b), b) - F(x_n(a), a)\to F(x(b), b) - F(x(a), a)$ everywhere, and for all $\omega$, $$\int_a^b \left(\frac{\pa F}{\pa t}\right)(x_n(t), t)dt\to \int_a^b \left(\frac{\pa F}{\pa t}\right)(x(t), t)dt. \tag{$\star$}$$
> Now, by Ito's formula, we know that $F(x_n(b), b) - F(x_n(a), a)$ converges to$$
> \int_a^b \psi(x(t), t)dx(t) + \int_a^b \left(\frac{\pa F}{\pa t}\right)(x(t), t)dt + \frac12 \int_a^b \frac{\pa \psi}{\pa \eta}d\braket{\psi(x(t), t), x(t)}
> $$
> Plugging in $\star$, we conclude.