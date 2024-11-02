This is an [[interface]].

>[!example]
>Recall [[SL2 Worked example]].

$L$ is a nonzero semisimple Lie algebra; the words nilpotent and semisimple are in the $\ad$ sense. 

See:
- [[Toral Subalgebra]]

We can fix a ==**maximal**== toral subalgebra $H\subset L$. After diagonalizing everything, we find
$$
	L = \bigsqcup_{\alpha\in \Phi} L_\alpha
$$
where
$$L_\alpha = \{x\in L: [hx] = \alpha(h)x \quad \forall h\in H\}$$
are the eigenspaces. We single out $L_0 = C_L(H)$; clearly $H\subset C_L(H)$. Call $\Phi = \{\alpha: L_\alpha\neq 0, \alpha\neq 0\}$.

>[!theorem]
>  - Also, $[L_\alpha L_\beta] =  L_{\alpha + \beta}$
>  - For all $x\in L_\alpha$ with $\alpha\neq 0$, the previous shoots things through the roof. Thus $\ad_x$ is nilpotent.
>  - $\kappa(L_\alpha, L_\beta) = 0$ for $\alpha + \beta \neq 0$.
>  - Recall that the whole $\kappa$ was nondegenerate, but we now see $\kappa(L_0, L_\alpha)\equiv 0$. Thus the restriction of $\kappa$ to $L_0$ is nondegenerate. (Don't worry, $L_0$ isn't semisimple, because its not an ideal).
>  - $C_L(H) = H$ lol. Now, we can identify $H$ with $H^*$.

# Orthogonality properties

Basically uh, $\Phi$ is good. 
- It spans $H^*$.
- For $\alpha\in \Phi$, $-\alpha\in \Phi$ and no other multiples lie in $\Phi$.
- For all $\alpha\in \Phi$, $x\in L_\alpha$, and $y\in L_{-\alpha}$, $[xy] = \kappa(x,y)\alpha^*$. In particular, $[L_\alpha L_{-\alpha}]$ is one-dimensional with basis $\alpha^*$.
- $\alpha(\alpha^*) = \kappa(t_\alpha, t_\alpha)\neq 0$ for all $\alpha\in \Phi$.
- If $\alpha, \beta \in \Phi$ with $\alpha\neq \pm \beta$, and $r,q$ are the largest integers such that $\beta - r\alpha, \beta + q\alpha$ are roots, then all $\beta + i\alpha$ in between are roots; this is the ==**$\alpha$-string through $\beta$**==.

In fact, each $L_\alpha$ is one-dimensional.

>[!theorem] Everything is $\sl(2, \FF)$
>Let $\alpha \in \Phi$ and pick $x_\alpha\in L_\alpha$. Then, you can find a $y_\alpha\in L_{-\alpha}$ such that $x_\alpha, y_\alpha, h_\alpha = [x_\alpha, y_\alpha]$ spans a $3$-dimensional simple subalgebra of $L$ isomorphic to $\sl(2, \FF)$.
>
>This subalgebra turns out to be $L_\alpha + L_{-\alpha} + H_\alpha$ where $H_\alpha = [L_\alpha L_{-\alpha}]$.
>
>Actually, $h_\alpha = \frac{2\alpha^*}{\kappa(\alpha^*,\alpha^*)}$ and $h_\alpha = -h_{-\alpha}$.