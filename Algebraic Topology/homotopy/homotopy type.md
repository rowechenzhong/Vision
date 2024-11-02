By replacing homomorphisms with [[homotopic maps|homotopies]], one can greatly generalize the notion of a space.

The identity function $X\to X$ is now expanded to an entire homotopy class. In this sense, the notion of an inverse must be broadened. We say that $f:X\to Y$ is a ==**homotopy equivalence**== (read: \"invertible in the homotopic sense\") if there exists $g:Y\to X$ such that $g\circ f\simeq \id_X$ and $f\circ g\simeq \id_Y$. 

If any such homotopic equivalence exist between two spaces $f:X\to Y$, then we say that $X$ and $Y$ have the same ==**homotopy type**==, and write $X\simeq Y$. 
 
> [!idea] 
Homotopy Theory cannot discern between spaces that are homotopy equivalent.
 
> [!idea] 
 As is standard in these category-theoretic type situations, the objects are second-class citizens, with their properties governed by the morphisms between them. 

> [!problem] 
 Show that $gf \simeq \id_X$ and $fh \simeq \id_Y$ implies $g\simeq h$; this is pure symbol-pushing.
 >
 Thus $f$ is a homotopy equivalence if and only if there exist $g,h$ such that $g\circ f\simeq \id_X$ and $f\circ h\simeq \id_Y$.
 >
 >One last exercise: $f:X\to Y$ is a homotopy equivalence iff there exist $g:W\to X$, $h:Y\to Z$ such that $gf$ and $fh$ are homotopy equivalences. 
 >
 >Push the symbols around until you're comfortable with them; they're literally just arrows.
 
> [!problem] 
 Show that homotopy type is an equivalence relation. 

> [!idea] 
Homotopy equivalence of spaces is a much coarser classification than homeomorphism of spaces (clearly homeomorphisms are homotopy equivalences).

> [!example] Contractible
 Spaces that are homotopy equivalent to a point are called ==**contractible**==. This occurs iff, for some point $*\in X$, there exists a map $f:[0,1]\times X\to X$ such that $f(0,x) = x$ and $f(1,x) = *$ for all $x\in X$.

>[!example] Examples of Contractible Spaces
>Examples include: 
> -  $\RR^n$ for any $n$. 
> -  Any convex subset $X\subset \RR^n$. 
> - Any [[topological cone]]

> [!example] Circle
 The Mobius band and cylinder are homotopy equivalent to a circle. We show this for a cylinder $[0,1]\times \CC^1$; the Mobius band is similar. Indeed, let $f: [0,1]\times S^1\to S^1$ via $(r,\theta)\to \theta$, and let $g$ send $\theta \to (0, \theta)$. Then, $f\circ g$ sends $(r,\theta)\to (0,\theta)$, which is homotopy equivalent to the identity via $\gamma_t(r,\theta) = (rt,\theta)$ and $g\circ f$ is literally the identity. 

> [!example] Punctured Torus
 The once-punctured surface of genus $g$ is homotopy equivalent to a wedge of $2g$ circles.