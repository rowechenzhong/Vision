Following the notation of $18.615$, measures are ==**covectors**==, transition matrices are ==**operators**== (such that $\mu P^t$ represents evolution), and functions are ==**vectors**==. This is good, because e.g. it reminds us that the natural operation on functions is $Pf\implies \sum_{y\in E} p_{xy} f$ not the other way around. In this context, an object like $x\in E$ is a unit covector --  a point distribution; thus evaluation is extracting a coordinate. This presents a slight challenge, because evaluation is written to the right; thus parenthesis like $(Pf)(x)$ are useful for clarification (However, I suppose $Pf(x)$ presents no ambiguity because there is only one logical contraction order). A random variable like $X:\Omega\to E$ is a function from $\Omega$ to the unit vectors.

Also, note that all our covectors are implicitly $L^1$ with norm $1$. This is why we always consider bounded $L^\infty$ functions; they're the correct dual space.

The probability part and the linear algebra part talk to each other, if somewhat awkwardly.