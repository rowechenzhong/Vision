---
aliases:
  - CLM
---
>[!definition] Continuous Local Martingale
>An adapted path-continuous process $M$ such that $M_0 = 0$ a.s. is a ==**Continuous Local Martingale**== if there exists a nondecreasing sequence of stopping times $T_n\uparrow \infty$ such that for every $n$, $M^{T_n}$ is a UI martingale.

If $M_0$ is not zero, we can still say $M$ is a CLM if $M_t - M_0$ is. These $T_n$ are called a ==**reduction**==, and are said to ==**reduce**== $M$.

>[!idea]- Note immediately
> - Continuous martingales $\subset$ CLMs via e.g. $T_n = n$.
> - By replacing $T_n$ with $T_n\wedge n$, we can replace "UI martingale" with "martingale"
> - If $M$ is a CLM, then for all stopping times $T$, $M^T$ is also a CLM. After all, $M^{T_n\land T}$ is a martingale.
> - If $T_n$ reduces $M$ and $S_n\uparrow \infty$, then $T_n\land S_n$ also reduces $M$. 
> - The space of CLMs is a vector space; simply use $T_n\land T'_n$ to reduce $M + M'$.

> [!example] The gambler is sentenced to the death penalty. They will be ruined at some point before time $1$, but they don't know when.
> Let $\tau = \inf\{t: B_t = -1\}$; note $\tau < \infty$ a.s. Consider the process
> $$
> X_t = \begin{cases}
> B^\tau_{t/(1-t)}: t < 1\\
> -1: t \geq 1
> \end{cases}
> $$
> under its natural filtration. The stopping times which reduce this local martingale are $T_k = \inf\{t: X_t \geq k\}$.
> 
> >[!proof]- Details
>> If the Brownian motion's filtration is $\GGG$, then $\FFF_t = \GGG_{t / (1-t)}$ for $t < 1$. $T_k$ are stopping times, because they're [[Elementary Stopping Time Constructions|collision times]] of a continuous adapted process. Then, $X^{T_k}$ is clearly a martingale on $s < t < 1$. The only other case is $s < t = 1$, because any $t\geq 1$ is equivalent to $t = 1$. In this case, if we let $\tau_k = \frac{T_k}{1 - T_k}$ be $\inf\{t: B_t \geq k\}$, we wish to show $\EE\left[B_{\tau \land \tau_k} | \FFF_t\right] = B_{t/(1-t)\land \tau \land \tau_k}$, but this is clear by OST.

>[!idea] Intuition
>Observe that the failing of the martingale a la OST was amplified by the time rescaling. The reduction rectifies this failure. This is the intuition behind the space-bound below.

>[!claim] Positive CLMs are supermartingales
>If $M\geq 0$ is a CLM with $M_0\in L^1$ then $M$ is a supermartingale.

>[!claim] Dominated CLMs are UI martingales
>If $M$ is a CLM and $Z\in L^1$ such that $\abs{M_t}\leq Z$ for all $t$, then $M$ is a UI martingale.

>[!claim] Bounded space reduction to shield a la OST
>If $M$ is a CLM and $M_0\in L^1$, then $T_n = \inf\{t\geq 0: \abs{M_t} \geq n\}$ reduces $M$.

> [!proof]- Proofs (Boring, use Fatou and Dominated Convergence)
> WLOG $M_0 = 0$ in the above (note in the second case, $M_0\in L^1$ as well). Then, for every $n$ and $s\leq t \leq \infty$,
> $$
> M_{s\land T_n} = \EE[M_{t\land T_n} | \FFF_s].
> $$
> (Small technicality: we know that $M^{T_n}$ is UI and admits an AS $L^1$ limit $M^{T_n}_\infty = M_{T_n}$. For all $\omega\in \{T_n = \infty\}$ minus a negligible set, this means that $M_t(\omega)$ has a $t\to\infty$ limit which we call $M_\infty(\omega)$. To avoid confusion, you can take $T_n\land n$ to all be finite).
> 
> - If $M\geq 0$, then by [[Convergence properties of Lebesgue Integral|Fatou]] for conditional expectations, for all $s \leq t < \infty$, $$M_s = \lim\inf_n M_{s\land T_n} = \liminf_n \EE[M_{t\land T_n} | \FFF_s] \geq  \EE[\liminf_n  M_{t\land T_n} | \FFF_s] = \EE[M_t | \FFF_s].$$
>   (This does not work for $t = \infty$, because $M_\infty$ has not been defined, so it doesn't make sense to ask if $\liminf_n M_{t\land T_n} = M_\infty$!)
> 
> - If $M$ is dominated, then for all $s \leq t < \infty$, $$M_s = \lim_{n} M_{s\land T_n} = \lim_n \EE[M_{t\land T_n} | \FFF_s] = \EE[\lim_n  M_{t\land T_n} | \FFF_s] =\EE[M_t | \FFF_s].$$ Hence $M$ is a martingale, hence $M$ is an $L^1$-bounded martingale, hence $M$ admits an almost-sure limit, hence the same equation with $t = \infty$ is completely valid and says $M$ is a UI martingale, as desired.
> 
> All the technical details about $\infty$ are important to keep track of!

For the shield, note that $M^{T_n}$ are CLMs (obvious) which are bounded by $n + \abs{M_0}\in L^1$, thus they are UI martingales as desired.

>[!idea]- Loosen the requirements
>These requirements are unnecessarily strong, of course. By identical logic:
>- In the first case, just make sure $M_t > N_t$ for all $t$, where $N$ is some path-wise decreasing function with $N_t\in L^1$.
>- In the second case, just make sure $\abs{M_t} \leq Z_t$ where $Z_t$ is some path-wise increasing function with $Z_t\in L^1$. Then we won't be UI, but we still have a martingale.
>  
> Also, the second case has an equivalent (advanced) reformulation via the [[The BDG Inequalities|BDG inequalities]].

# CLMs are disjoint from FVPs

>[!claim] CLMs are disjoint from FVPs
>If $M$ is a CLM and a FVP (so $M_0 = 0$) then $M_t \equiv 0$ a.s.

> [!proof]- Variances Add
> The main idea is that [[Square Integrable Martingale|Variances Add]], and we want to coerce $M$ to be in $L^2$ such that we can exploit these growth rates.
> 
>  The easiest way is to shield by its total variation. Let $$\tau_n = \inf\left\{t\geq 0: \int_0^t \abs{dM_s} \geq n\right\}.$$These are stopping times because they're the [[Elementary Stopping Time Constructions|collision times]] of the adapted (in fact, increasing) process $\int_0^t \abs{dM_s}$. Then, the process $N = M^{\tau_n}$ is bounded by $n$ and thus a martingale. Picking meshes and using additivity of variance,$$\begin{align*}
> \EE[N_t^2] &= \sum_{1\leq i\leq p} \EE\left[\left(N_{t_i} - N_{t_{i-1}}\right)^2\right]\\
> &\leq \EE\left[\left(\sup_{1\leq i\leq p} \abs{N_{t_i} - N_{t_{i-1}}}\right) \underbrace{\sum_{1\leq i\leq p} \abs{N_{t_i} - N_{t_{i-1}}}}_{\leq n}\right]\\
> & \leq n \EE\left[\sup_{1\leq i\leq p} \abs{N_{t_i} - N_{t_{i-1}}}\right]
> \end{align*}$$ By continuity of sample paths, we know that the inner function should vanish along any decreasing mesh; $N$ is bounded, thus it is dominated and $\lim_{k\to \infty} \EE\left[\dots\right] = 0$. Thus $\EE[N_t^2] = 0$ and $M_{t\land \tau_n} \equiv 0$ AS. This is true for all $n$, and $\tau_n\uparrow \infty$, thus $M_t\equiv 0$ a.s.