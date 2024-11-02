An ==**automorphism**== of $L$ is an isomorphism $L\to L$. The group of all automorphisms is called $\Aut L$. 

> [!example] Automorphisms of Linear Lie groups are basis changes
> If $L\subset \gl(V)$, then for any $g\in \gl(V)$, if $gLg^{-1} = L$, $x\to gxg^{-1}$ is an automorphism.

If a derivation $\delta$ is nilpotent, $\delta^k = 0$ for sufficiently large $k$, then $\exp(\delta)$ makes sense as a power series. In this case,
$$\exp \delta(x) \exp \delta(y) = \exp \delta(xy)$$
Thus $\exp \delta$ is an automorphism.

If $\delta = \ad x$ such that $(\ad x)^n = 0$, then $x$ is called ==**ad-nilpotent**==. Then, $\exp \delta$ is called an ==**inner automorphism**==; the normal subgroup of all such is called $\Int L \trianglelefteq \Aut L$.