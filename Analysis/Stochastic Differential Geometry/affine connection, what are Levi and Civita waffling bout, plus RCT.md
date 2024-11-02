An ==**affine connection**== is just a bilinear map $\Gamma(TM)\times \Gamma(TM)\to \Gamma(TM)$ called $(X,Y)\mapsto \nabla_X Y$. It's defined on arbitrary manifolds. For all smooth $f$ on $M$ and all vector fields $X,Y$:
- $\nabla_{fX} Y = f\nabla_X Y$, which is a locality thing (you expect this).
- $\nabla_X(fY) = X(f)Y + f \nabla_X Y$, which is a Leibniz rule.

Notably, $\nabla_XY(x)$ is a function of $X(x)$ and the germ of of $Y(x)$. It tells you how much $Y$ is supposed to change if you push it along $X$. There's no a priori good way to pick this connection; it's additional data that specifies how $TM$ glues together.

>[!idea]
>This is also called the ==**covariant derivative**==, which makes sense because it already looks like a derivative. Given a specific $X_p\in T_pM$, $\nabla_{X_p}Y$ makes sense.
>
>Extend in the usual Leibniz sense to tensors.

Except, like, bro we're working on a Riemannian manifold. Fundamental theorem of Riemannian geometry: there's only one way to write a "torsion-free" affine connection compatible with $g$, and it's called the ==**Levi-Civita Connection**==. We want the contraction $\nabla g = 0$, which just means that orthonormal bases are preserved; this means we can raise and lower indices through the derivative.

The torsion-free part is $\nabla_X Y - \nabla_Y X = [X,Y]$. Shrug, sounds valid.

Hey, the Riemann curvature tensor, you know this stuff right. $R^d_{cab}Z^c = \nabla_a \nabla_b Z^d - \nabla_b \nabla_a Z^d$ is the commutator of $\nabla_a$ and $\nabla_b$, and this second-order information literally encodes curvature of your space.

Move.