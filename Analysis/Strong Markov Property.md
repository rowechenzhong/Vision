> [!idea] Informal
> Markov Properties take the form, "if after some (stopping) time $T$, we are at $X_T$, then $X_{T+s}$ forever looks like $X_s$." This is a statement about distributions on the space of (cadlag) processes. Hence, we will recall definitions, and then phrase our results in terms of expectations of test functions (measurable $\Phi: D(E)\to \RR_+$).

Let $(Q_t)_{t\geq 0}$ be a possibly non-Feller [[Definition and Existence of Markov Processes|transition semigroup]] on some metric space $E$. For each $x\in E$, suppose we can construct path-cadlag Markov processes $(X^x_t)_{t\geq 0}$; this follows immediately if $Q$ is Feller.

Now, the [[cadlag|space of all cadlag paths]] is called $D(E)$, and we can get pushforward laws $\PP_x$ for each $X^x$. (Note that even if multiple $X^x$ exist corresponding to some $Q$, the finite-dimensional marginals are completely determined by $Q$, so these laws $\PP_x$ are really a property of $Q$, not of $X^x$).

>[!claim]
>$\EE_x$ denotes expectation with respect to $\PP_x$. For any measurable $\Phi: D(E)\to \RR_+$, $x\mapsto \EE_x[\Phi]$ is measurable.

>[!proof]- Easy cylinder bootstrap
> It suffices to consider $\Phi = \id_A$ where $A\in D(E)$ is a cylinder set. In this case,$$\PP_x\left[\id_{X^x_{t_1}\in A_1}\dots \id_{X^x_{t_p}\in A_p}\right]$$has the un-enlightening explicit formula$$\int_E \id_{x_1\in A_1}Q_{t_1}(x,dx_1)\dots \int_E \id_{x_t\in A_t}Q_{t_p - t_{p-1}}(x_{p-1},dx_p)$$which is clearly $E$-measurable (by definition). The cylinder sets generate $D(E)$ and the indicators generate measurable $D(E)\to \RR_+$ so we conclude.

>[!theorem] Simple Markov Property
>Let $s\geq 0$ and $\Phi: D(E)\to \RR_+$ be measurable. Let $Y$ be a specific $Q$ $(\FFF_t)$ path-cadlag Markov process. Then,$$\EE\left[\Phi\left(\left(Y_{s+t}\right)_{t\geq 0}\right) | \FFF_s\right] = \EE_{Y_s}[\Phi].$$

Type-checking, both sides are $\FFF_s$-measurable. Actually, the full proof is also an easy cylinder bootstrap.

>[!proof]- Another easy cylinder boostrap
> For any $\phi_1,\dots, \phi_p\in B(E)$ (bounded measurable functions with $\infty$ norm), obviously$$\EE\left[\phi_1(Y_{s + t_1})\dots | \FFF_s\right] = \int Q_{t_1}(Y_s, dx_1) \phi_q(x_1)\dots \int Q_{t_p - t_{p-1}}(x_{p-1}, dx_p) \phi_p(x_p).$$So we can specialize to cylinders $\Phi = \id_A$ and win.

# Strong Markov Property

This time, make sure $(Q_t)_{t\geq 0}$ is a Feller subgroup.

> [!theorem] Strong Markov Property
> Let $T$ be a stopping time of $(\FFF_{t+})$ and $\Phi: D(E)\to \RR_+$ be measurable. Then,$$\EE\left[\id_{T < \infty} \Phi\left(\left(Y_{T+t}\right)_{t\geq 0}\right) | \FFF_T\right] = \id_{T < \infty} \EE_{Y_T}[\Phi].$$

Note that $T$ is a stopping time of $\FFF_{t+}$, which is extra sweet. Note that $\omega\mapsto Y_T(\omega)$ is $\FFF_T$-measurable because we are [[Index Progressive Process at Stopping Time|indexing a progressive process at a stopping time]].

Proof boring, details omitted, use dyadics to employ cadlag.