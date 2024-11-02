# Constructing some Manifolds

> [!problem] Grassmanian
> Let $Gr_k(\KK^n)$ be the space of $k$-dimensional subspaces of $\KK^n$. Show that $Gr_k(\RR^n)$ is a topological manifold, and write out $\binom{n}{k}$ charts. Show that $Gr_k(\CC^n)$ is a complex manifold (i.e., analytic).

>[!idea] Blunder
>Here's a misconception I had: the standard basis for [[k-blades]] consists of subspaces with magnitude, but the ray space of $\Lambda^k V$ is too large. $\Lambda^k V$ contains objects that are "sums of subspaces" which cannot be cleanly mapped to a single subspace. 
>
>>[!idea]- Excuses
>>If so, you would expect that the dimension of $Gr_n(\KK^n)$ is $\binom{n}{k} - 1$, but the dimension is really $k(n-k)$.
>>I was confused by my low-dimensional intuition, because if $k\in \{0,1,n-1, n\}$ this just holds. The smallest nontrivial example is $2$-planes in $4$-space, where the space of rays of $2$-blades is $\binom{4}{2} - 1 = 5$ but there are only $2(4 - 2)$ subspaces.

> [!solution]- 
> Write down an $n\times k$ matrix, then use reduced column echelon form smh.


# Deeper Questions

> [!problem] Products of Manifolds
> Suppose $X$ is an $m$-dimensional manifold, and $Y$ is an $n$-dimensional manifold. Show that:
> - $X\times Y$ is an $m + n$-dimensional manifold.
> - If $X$ and $Y$ are ($C^k$/real analytic/complex analytic) then $X\times Y$ is as well.

>[!solution]- $X\times Y$ is a manifold
>$X\times Y$ is:
>- Hausdorff, obviously.
>- Has countable basis, obviously.
>- For any $(x,y)\in X\times Y$, pick the desired atlases $(U, \phi)$ and $(V, \psi)$, then $(U\times V, \phi \times \psi)$ is an atals from $U\times V$ to $\RR^m\times \RR^n \cong \RR^{m + n}$.

>[!solution] Regularity
>A multivariable function satisfies any of the above regularity conditions iff it does componentwise.

>[!problem] Continuous functions yield manifolds
>Given a continuous function $f: \RR^m\to \RR^n$, the graph of all points $(x, f(x))\subset \RR^{m + n}$ with the induced topology is a smooth $m$-manifold.

>[!proof]
>The conjectured atlas is simply $f$. We need to show this is a homeomorphism. This is actually just true in general; for any continuous $f:X\to Y$, it is true that $\{(x, f(x))\}\subset X\times Y$ is homeomorphic to $X$.
>
>

>[!problem]
>Show that any holomorphic function on a connected compact complex Lie group $f:G\to \CC$ is constant.
>^holomorphic-constant

Suppose otherwise; $G$ is non-constant on some open set $U$. Call a point $x$ locally-constant if there exists an open set containing $x$ on which $f$ is constant; otherwise call it a potato. Now:
- The set of all LC points is an open set, because if $x$ is LC, then it admits a chart $(U,\phi)$, and then $f$ is forced to be constant on $U\subset \CC^n$ by complex analysis.
- The set of all potatoes is an open set, because if $x$ is a potato, then it admits a chart $(U,\phi)$, and then $f$ is forced to be non-locally-constant on $U\subset \CC^n$.

It's not that deep. Assuming $f$ is never locally constant, it is potato everywhere. Thus, by complex analysis again, non-constant holomorphic functions are open maps, thus the image of $G$ must be an open set in $\CC$.

The image of $G$ is compact just because continuous maps preserve compact sets. But there are no compact open sets of $\CC$! So $f$ must be constant.