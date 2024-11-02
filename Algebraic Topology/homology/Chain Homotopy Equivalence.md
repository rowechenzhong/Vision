Under the homotopy category of chain complexes, $C$ and $D$ are ==**chain homotopy equivalent**== if there exist chain maps $\phi:C\to D$ and $\psi:D\to C$ such that $\psi\phi \sim \id_C$ and $\phi\psi \sim \id_D$. 

This implies $H(C) \cong H(D)$, because $H(\psi)H(\phi) = H(\id_C)$ and $H(\phi)H(\psi) = H(\id_D)$ implies $H(\psi)$ is a group isomorphism.

By arrow chasing,

>[!claim]
>$C$ is chain homotopy equivalent to the zero complex iff $\id_C\sim 0_C$ where $0_C$ is the zero map $C\to C$.

The homotopy category of chain complexes has strictly more information than the homology groups.

>[!example]
>$$\dots\ZZ/4\stackrel{2}{\to} \ZZ/4\stackrel{2}{\to} \ZZ/4\dots$$ has zero homology, but the identity map is not chain homotopic to $0$. Indeed, the kernels and images are both $\{0,2\}$, so the homology groups are $0$. However, the identity map is not chain homotopic to $0$, because $\pa h + h\pa$ is always a multiple of $2$ (because $\pa = 2$).

>[!example]
>The short exact sequence of abelian groups
>$$0 \to A \stackrel{\alpha}{\to} B \stackrel{\beta}{\to} C \to0$$
>is homotopy chain equivalent to $0$ iff it splits.