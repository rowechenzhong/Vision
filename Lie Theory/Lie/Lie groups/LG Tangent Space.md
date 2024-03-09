This set of ideas comes before we create the bridge, but it will be an essential stepping stone.

When working with differentials in $\RR^n$, we don't distinguish between "infinitesimal movement by $(0,1)$ at $(0,0)$" versus "infinitesimal movement by $(0,1)$ at $(2,3)$," because the tangent space at $(0,0,0)$ is naturally identified with that at $(2,3)$. In vanilla differential geometry, $T_xM$ and $T_yM$ cannot be canonically identified, so one must make this distinction.

Recall that [[LG + Tensor Fields#^b9afb7|we can create a natural tangent bundle on $G$]]. The reason this is important is that $(1,x)\in T_1G$ and $d_1L_g(1,x)\in T_gG$ ***can now be canonically identified;*** they are both "infinitesimal left movement by $x$." Similarly, $d_1R_gx\in T_gG$ can also be identified with $x$; it is "infinitesimal right movement by $x$."

To this end, let's let $\fg = T_1G$, and pick some $x\in \fg$. We will abbreviate $T_1L_gx$ to $gx$ in the future, and $T_1R_gx$ to $xg$.

The question now is how to do calculations. We've [[Differential|defined the differential]], but the equation there is hopelessly ugly. As you might hope, in Lie, because of the above principles, one can think about vectors in $\fg$ simply as vectors, without referencing all of the germ garbage. We will never explicitly write a vector in $T_gG$ for $g\neq 1$ again; we will perform all computations with things like $gx$, $x\in \fg$, and replace all computations involving $d_g\phi$ with $d_1\phi$.

Here's the main computational claim, which is not deep and codifies this:

>[!claim] Shift differentials of homomorphisms
>Let $\phi:G\to H$ be a homomorphism of Lie groups sending $g\to h$. For any $x\in \fg$,
>$$(d_g\phi)(gx) = h(d_1\phi(x))$$
>

Recall that we're supposed to think $gx \equiv x$, $hx\equiv x$. In that case, this is just saying "$d_g\phi \equiv d_1\phi$," which is completely expected; a group homomorphism is basically linear.

>[!proof]-
> Indeed, observe
> $$\begin{align*}
> (d_g\phi)(gx) &= \left((d_g\phi)\circ (d_1 L_g)\right)x\\
> &= d[\phi\circ L_g]x\\
> &= d[L_h\circ \phi] x\\
> &= \left((d_1L_h)\circ (d\phi_1)\right)x\\
> &= h\left(d\phi_1(x)\right)
> \end{align*}$$
>