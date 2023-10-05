We now know what kind of object the [[Tangent spaces|tangent space]] $TX$ is! The ==**tangent bundle**== is the vector bundle $p:TX\to X$, where we take the atlas of charts $(U_\alpha, \phi_\alpha)$ with transition maps
$$
	\theta_{\alpha\beta}:\phi_\alpha\circ \phi_\beta^{-1}: \phi_\beta(U_\alpha \cap U_\beta) \to\phi_\alpha(U_\alpha \cap U_\beta)
$$
and set the clutching functions to be
$$
h_{\alpha\beta} = d_{\phi_\beta(x)} \theta_{\alpha\beta}
$$
This formalizes the idea that the tangent space $T_xX$ varies smoothly with $x\in X$; this is all part of a larger tangent bundle structure.