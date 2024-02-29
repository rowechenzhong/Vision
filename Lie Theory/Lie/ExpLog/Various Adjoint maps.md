Everything starts from the conjugation map
$$(g,h) \to ghg^{-1}$$

> [!idea]
> In Lie Algebra, we like to write $T_1G$ as $\fg$; this object will play an important role very soon.

For any particular $g$, this defines an diffeomorphism on $G$ which has [[Differential|differential]] $Ad(g) \in \GL(\fg)$. We can thus imagine that $Ad$ is a function $G\to \GL(\fg)$. Explicitly,
$$
	\Ad(g)(y) = \left.\frac{\der}{\der t}\right|_{t = 0} (g\exp(ty)g^{-1})
$$

This, too, has a differential, which is thus called $d(\Ad(g)) = \ad: \fg\to \GL(\fg)$. Explicitly, this is
$$
\ad(x)(y) = \left.\frac{\der}{\der s}\frac{\der}{\der t} \left(\exp(sx)\exp(ty)\exp(sx)^{-1}\right)\right|_{t=s=0}
$$
(which can be written nicely because these are linear maps).