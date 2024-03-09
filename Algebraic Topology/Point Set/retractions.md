Retractions are the topological analogues of projection operators in linear algebra. 

> [!definition] Retraction
> A ==**retraction**== of a space $X$ onto a subspace $A\subset X$ is a continuous map $r:X\to X$ such that $r(X) = A$ and $r|_A = \id_A$. Equivalently, $r^2 = r$.

> [!problem] Retractions are lame
 This is not a very strong condition; all spaces retract to points. 
 
> [!definition] Deformation Retraction
> Let $A\subset X$ be a subspace. If a retraction $r:X\to X$ is homotopic to the identity map $\id_X$, then we say $A$ is a ==**deformation retraction**== of $X$. 
 
> [!problem] Spinning Definitions
 Show that $X$ deformation retracts to $A$, then the inclusion $i: A\to X$ is a [[homotopy type|homotopy equivalence]].

> [!solution]-
 If $X$ deformation retracts to $A$, then the retraction $r:X\to X$ is a homotopic to $\id_X$. Let $r' : X\to A$ be $r$ but with the correct range. Then, $ir'\simeq \id_X$, and $r'i = \id_A$, as desired.