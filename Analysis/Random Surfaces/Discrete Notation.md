When $f: \ZZ^d\to \RR$, we define $\bar{f}(x) = \frac1{2d} \sum_{y\sim x} f(y)$. The ==**discrete Laplacian**== is $\Delta f(x) = \bar{f}(x) - f(x)$.

The ==**discrete boundary**== of $D\subset \ZZ^d$ is $\{\pa D = \{x\in \ZZ^d: d(x,D) = 1\}$. The ==**discrete closure**== is $\bar{D} = D\cup \pa D$. $\Ff_{(D)}$ is the set of functions from $\ZZ^d\to \RR$ equal to $0$ outside $D$.

$E_{\bar{D}}$ is the set of edges with at least one endpoint in $D$. We define $\abs{\nabla F(e)} = \abs{F(x) - F(y)}$, where $e = (x,y)$. The signage would depend on an orientation, but we are ignoring this. The product $\nabla F_1(e) \nabla F_2(e)$ has no orientation issues.

We introduce the ==**Dirichlet energy**== of $F$ over a finite $D$,
$$\mathcal{E}_D(F) = \sum_{e\in E_{\bar{D}}} \abs{\nabla F(e)}^2.$$

We introduce the ==**Dirichlet form**== $$(f,g)_\nabla = \sum_{\braket{x,y}} ((f(x)-f(y))(g(x) - g(y))$$under which the above energy is $(f,f)_\nabla$.