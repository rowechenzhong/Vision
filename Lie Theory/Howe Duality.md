>[!theorem] Howe Duality
>$$S^n(V\otimes W) = \bigoplus_{\abs{\lambda} = n} S^\lambda V \otimes S^\lambda W.$$

Note that if $\lambda$ doesn't fit in $V$ or $W$ then the corresponding summand is $0$.

>[!proof]-
> Observe that this is (basically by definition) $(V^{\otimes n}\otimes W^{\otimes n})^{S_n}$. By Schur-Weyl duality,$$\bigoplus_{\abs{\lambda} = \abs{\mu} = n} S^\lambda V \otimes S^\mu W \otimes (\pi_\lambda \otimes \pi_\mu)^{S_n}.$$Now, there's a trick. The character $\pi_\lambda$ is integer valued (TODO: why?) thus $\pi^*_\lambda = \pi_\lambda$. By Schur's lemma, $(\pi_\lambda \otimes \pi_\mu)^{S_n} = \CC^{\delta_{\lambda \mu}}$ and we obtain the desired.

Corollaries:

TODO: Cauchy identity, Molien Formula