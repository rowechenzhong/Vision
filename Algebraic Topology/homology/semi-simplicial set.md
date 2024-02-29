We now consider a collection of [[Simplex|simplicies]] as a combinatorial object. A ==**semi-simplicial set**== is a collection of sets $K_0, K_1,\dots$, endowed with a collection of ==**face maps**==
$$\pa^i_n: K_n\to K_{n-1}, \qquad 0\leq i\leq n$$
such that $\pa^j\circ \pa^i = \pa^i\circ \pa^{j+1}$ from $K_n\to K_{n-2}$ for $i\leq j$.

$K_i$ is thought of as the set of all $i$-simplices.

Then, one can create an actual [[Delta Complex]] from this collection by writing
$$
	\abs{K} = \left(\bigsqcup_{n\geq 0} K_n\times \Delta_n\right)/ \sim
$$where$$(\pa_n^i(\sigma), x)\sim (\sigma, \epsilon^i_n(x)),$$as expected.