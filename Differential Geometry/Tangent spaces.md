The ==**tangent space**== at $P$ is the space of all [[Derivation|derivations at]] $P$, and is denoted $T_P X$. This is a $\RR/\CC$ vector space.

At first, this might seem really large, but it turns out that it's exactly what we think it is:

> [!claim] Basis
> Let $x_1,\cdots, x_n$ be local coordinates at $P$. Then $T_PX$ has basis
>
> $$
> 	D_i(f) = \frac{\pa f}{\pa x_i}(0)
> $$

> [!proof] Boring, Todo

> [!idea]
> The elements of $T_PX$ are functionals of functions. (Differentiable) functions are locally "linear maps". Thus, elements of $T_PX$ are comparable with elements of $X$, and should be thought of as literally a space "tangent" to $X$ at $P$.

> [!idea]
> The point of confusion comes from notation. Previously, $x_i$ was a local coordinate - a function from $U\subset X$ to $\RR$). We have now written $D_i\in T_PX = \frac{\pa}{\pa x_i}$. This object has different type from $x_i$; it can be imagined as "the point with coordinates $(0,\dots, 1,\dots, 0)$."
>
> So $\pa_{x_i} = D_i$, but you should never write $\pa_{x_i} = x_i$.
>
> $x_i$, as a function, is a ``covector," while objects like $\pa_{x_i} \in T_P X$ are vectors. To "contract" $\pa_{x_i}$ with a function $f$ is to evaluate $\pa_{x_i} f$, which is how much $f$ changes if you move by "$\eps x_i$", divided by $\eps$.
>
> For some reason, people write $v\in T_PX$ and then write $\pa_v : O(U)\to X$. I guess we're supposed to think $\pa_v\equiv v$. This is fine; just note that $\frac{\pa}{\pa x_i} \neq \pa_{x_i}$; we should write $\frac{\pa}{\pa x_i} \equiv \pa_{D_i} = D_i$.


> [!idea]
> You can extend derivations to algebras of regular functions, because the regular functions are elements of germs; you can write $\pa_v: O(U)\to \RR$.