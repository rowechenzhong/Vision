A la Etingof.

>[!theorem] Hilbert-Schmidt
>Let $A:H\to H$ be a compact self-adjoint operator. Then, there exists an orthogonal decomposition$$H = \Ker A \oplus \widehat{\bigoplus}_\lambda H_\lambda$$such that each $H_\lambda$ is a $\lambda$-eigenspace. Furthermore, $H_\lambda$ are each finite-dimensional, and the eigenvalues $\lambda$ are real numbers which either form a finite set or a sequence going to $0$.

This is trivial for finite-rank operators. The fact that eigenvalues are real numbers and that each $H_\lambda$ is finite-dimensional are trivial.

We begin by proving this for $A^2$, which is also compact and self-adjoint. Let $\beta = \norm{A}^2 = \sup_{\norm{v} = 1} \braket{A^2v | v}\geq 0$. Assume $\beta > 0$ else $A = 0$. Let $A_n$ be a sequence of self-adjoint finite-rank operators converging to $A$, which exists because one can take any convergent sequence of finite-rank operators $A_n$ and consider $\frac12\left(A_n + A^\dagger_n\right)$. Let $\beta_n = \norm{A_n}$ which is also the supremum eigenvalue of $A_n^2$. Clearly $\beta_n\to \beta$ (norm continuity). Ensure $\norm{\beta_n - \beta} \leq \norm{A_n - A}\leq \frac{1}{n}$.

Let $v_n$ be a sequence of unit vectors in $H$ such that $A^2_nv_n = \gamma_nv_n$ and $\gamma_n\geq \beta_n - 1/n$. $A^2$ is compact thus $A^2v_n$ admits a convergent subsequence; extract this subsequence from $(A_n)$ such that WLOG this sequence converges to some limit $w\in H$. Ensure $\norm{A^2 v_n - w} \leq 1/n$.

Alright, bet. Then, everything is just exact in the limit:
- $\norm{A^2v_n - A^2_nv_n}\leq \frac1n$.
- $\norm{A_n^2v_n - \gamma_nv_n} \leq \frac1n$.
- $\abs{\gamma_n - \beta}\leq \frac{2}{n}$.
Thus $\norm{w - \beta v_n}\leq \frac{4}{n}$. Notably, $v_n$ converge to $w / \beta$, thus $A^2w = \beta w$. Draw the whole finite-dimensional $\beta$ eigenspace, $W$.

Then $Aw = \pm \sqrt{\beta}w$; pick the correct signs for $W_+\oplus W_- = W$ and replace $A$ with $A - \sqrt{\beta}P_{W_+} + \sqrt{\beta}P_{W_-}$. $w$ is in the kernel of this guy, and $\braket{A - \sqrt{\beta})v | w} = 0$ thus its image lies in the orthogonal subspace to $w$. Thus we can replace $H$ with the orthogonal complement of $w$ and repeat. This either yields a sequence of $\beta$ which tend to $0$ or yields a finite sequence.

$\bigoplus_n H_{\beta_n}$ is dense, because if you are orthogonal to all $\beta_k$ then $\norm{Av}\leq \beta_k\norm{v}$ for all $k$ and $Av = 0$ as desired. In the case where the sequence is finite it's even easier because at that stage $\norm{A} =0 \implies A = 0$.