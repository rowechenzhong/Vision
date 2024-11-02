A ==**$\ZZ[G]$-module**== is an abelian group $A$ endowed with a left group action $x\to gx$ which is distributive on the right (in other words... it is a module in the usual sense).

A module is called ==**free over $\ZZ[G]$**== if one can find a $\ZZ$-basis on $\ZZ[G]$, indexed $e_{g, \lambda}$, such that $ge_{h,\lambda} = e_{gh, \lambda}$ (in other words, you are of the form $\ZZ[G]^{\otimes \Lambda}$).

See: [[Coinvariants of a ZG module]]

# Building $\ZZ[G]$-modules from $G$-sets

For any set $X$, the ==**free abelian group on $X$**== is $\ZZ[X]$, the free abelian group with basis $(e_x)_{x\in X}$. If $G$ is a group, then $\ZZ[G]$ also has a ring structure via $e_g\cdot e_h = e_{gh}$.

If $X$ happens to be a $G$-set (a set endowed with a left group action) then the action of $G$ on $X$ induces a $\ZZ[G]$-module structure on $\ZZ[X]$. Indeed, elements $g$ act on $e_x$ via $ge_x = e_{gx}$. It's not that deep.

>[!idea]
>In the case that $X = G$, note that $\ZZ[X] = \ZZ[G]$ is exactly the ring $\ZZ[G]$... as a left module over itself. Nothing surprising.

For any family $(X_\lambda)_{\lambda\in \Lambda}$ of sets,$$\ZZ\left[\bigsqcup_{\lambda\in \Lambda} X_\lambda\right] \cong \bigoplus_{\lambda\in \Lambda} \ZZ[X_\lambda].$$In the case that $(X_\lambda)$ is actually a bunch of $G$-sets, then this also induces an isomorphism of $\ZZ[G]$-modules. This is pretty stupid; they're both direct sums.

# Free $G$-sets

Suppose now that $X$ is a free $G$-set, meaning $X\cong \bigsqcup_{\lambda \in \Lambda} G$ as $G$-sets for some index set $\Lambda$. (In other words, you have a bunch of $(g, \lambda)$ which get rotated within themselves by $G$). The resulting $\ZZ[G]$ module, $\ZZ[X]$, is just$$\ZZ[X] \cong \ZZ[G]^{\oplus \Lambda}.$$In other words, we can find a basis $e_{h,\lambda}$ such that the action of $g$ is just $e_{h,\lambda}\to e_{gh,\lambda}$.