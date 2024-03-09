We will now compute the irreps of $\GL_n(\CC)$ through [[Representations of SL|representations of $\SL_n(\CC)$]]. We observe that $\GL_n(\CC) = (\CC^\times\times \SL_n(\CC))/\mu_n$ where $\mu_n$ consists of terms $(\omega^{-1},\omega \id)\in \CC^\times\times\SL_n$; the covering homomorphism is via $\CC^\times \times \SL_n(\CC)\to \GL_n(\CC): (z,A)\mapsto zA$, and turn our attention to $\CC^\times \times \SL_n(\CC)$.

If $n = 1$, representation of $\CC^\times$ are completely reducible, with irreps $\chi_N$ all one-dimensional via $\chi_N(z) = z^N$. (Obviously, the corresponding Lie algebra representation is $z\mapsto Nz$).

In general, $\CC^\times \times \SL_n$ representations are still completely reducible, and all of the form $L_{\lambda, N} = \chi_N\otimes L_\lambda$ (this is clear). In order to factor through $\GL_n$, they need to annihilate $(\omega^{-1}, \omega \id)$. The $\CC^\times$ part acts as $\omega^{-N}$ on $L_{\lambda, N}$, while $\omega \id$ acts as $\omega^\abs{\lambda}$.

>[!proof]- Short calculation
>In the lie algebra with $\omega = e^{\frac{2\pi ik}{n}}$, this maps to e.g.$$\left(-\frac{2\pi i k N}{n}, +\frac{2\pi i k}{n} \underbrace{\begin{pmatrix}1&&&\\&1&&\\&&\ddots&\\&&&-n+1\end{pmatrix}}_h\right).$$$h$ is in the CSA of $\sl_n$, and thus acts by a dot product against the weight. This dot product is $\lambda(h) = \frac{2\pi i k}{n} \abs{\lambda}$ ($\lambda_n = 0$ for $\SL_n$-reps). 

Thus a representation factors iff $N = nm_n + \sum_{i}^{n-1} \lambda_i$ for some $m_n$, and we restrict to this case from now on.

# Results

Working in reductive $\gl_n$ now, $\hh = \CC^n$ has an additional axis (which we append to the back). Highest weights now take the form$$(m_1+\dots+m_n,\dots,m_n)$$n.b. the last term is no longer $0$. We rename $\lambda$ to this. Observe now that $N = \abs{\lambda}$, i.e. the $\CC^\times$ component acts as $z\mapsto z^{\abs{\lambda}}$; this is not surprising, because $\id\in \gl_n$ lives in root space $(1,\dots,1)$. The fundamental representations are $\wedge^mV$. $\wedge^nV$ is no longer trivial, but the ==**determinant character**== with highest weight $\omega_n = (1,\dots,1)$. The highest weight of a finite-dimensional representation is $\lambda = \sum_{i = 1}^n m_i \omega_i$ where $m_i\geq 0$ for $i < n$ and $m_n\in \ZZ$, and $L_\lambda$ is found inside $\bigotimes_i (\wedge^i V)^{\otimes m_i}$.


>[!idea] One-dimensional determinant character admits "negative tensor powers"
>Allow $\chi^{\otimes k} = (\chi^*)^{\otimes -k}$ if $k < 0$.

When $m_n\geq 0$, the $\lambda$ lives naturally inside some $V^{\otimes N}$, while if $m_n\leq 0$, it does not (the action of $\omega \id$ on some subrep of $V^{\otimes N}$ should always have positive determinant).

>[!idea] Polynomial representations
>These representations are called ==**polynomial**== because their matrix coefficients are polynomial functions of the entries in $\GL_n(\CC)$; consequently they extend by continuity to representations of $\End_n(\CC)$. Note that any irrep is a polynomial rep tensored with a non-positive power of $\wedge^nV$.