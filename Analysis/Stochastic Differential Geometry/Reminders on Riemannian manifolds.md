$M$ is a $d$-dimensional complete Riemannian manifold. What does this mean?
- $M$ is a smooth manifold.
- $M$ has a positive-definite inner product $g_p$ assigned to $T_pM$ at each point $p$; $g_p\in T^*_pM^{\otimes 2}$. This is taken to be smooth unless you're doing crazy things.

Let's remind ourselves of the major objects.
- The ==**Lie derivative**== evaluates the change in a tensor field with respect to some vector field. It is denoted $\LL_X T$, and is a derivation. The Lie derivatives are actually good derivations, because $\LL_{[X,Y]} = \LL_X\LL_Y - \LL_Y\LL_X$.
	- Algebraic definition:
		- $\LL_Y f = Y(f)$ for scalar $f$; the Lie derivative of ahm function is just the directional derivative.
		- Leibniz' rule with respect to tensors: $\LL_Y(S\otimes T) = (\LL_Y S)\otimes T + S\otimes (\LL_Y T)$.
		- Leibniz' rule with respect to contraction: $\LL_X S^{\alpha\dots}_{\dots} T^{\dots}_{\alpha\dots} = \left(\LL_X S^{\alpha\dots}_{\dots}\right)T^{\dots}_{\alpha\dots} + S^{\alpha\dots}_{\dots}\left(\LL_X T^{\dots}_{\beta\dots}\right)$.
		- The Lie derivative commutes with the exterior derivative on functions.
	- The correct way to think of this: you have a vector field on your *entire manifold*, which is really strong; it induces a local flow $\Phi^t_X$. Drop a leaf in the flow at $p$, and after time $t$ it's at $\Phi^t_X(p)$. The flow gives you a local diffeomorphism (it might have global problems, but this really doesn't matter) from $T_pM$ to $T_{\Phi^t_X(p)}M$, which lets you pullback your leaf. Then $$\lim_{t\to 0} \frac{\left(\Phi^t_X\right)^* T_{\Phi^t_X(p)} - T_p}{t}$$ is actually facts. For bigger leaves, add tensor products.
- The ==**gradient**== is the "wrong" scalar derivative; the tangent vector is a co-vector, and the gradient is what you get when you raise the index with the metric. $g(\nabla f, X) = \pa_X f$.
- The ==**divergence**== is also a subtlely wrong thing I think, but let's carry on. $\nabla\cdot X = \frac{1}{\sqrt{\abs{g}}} \pa_i\left(\sqrt{\abs{g}} X^i\right)$.
- The ==**Laplace-Beltrami**== operator $\Delta$ is supposed to generalize $\pa_i\pa^i$. It's $\nabla(\nabla\cdot X)$.