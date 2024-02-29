---
aliases:
  - simplicies
  - simplex
---
>[!idea]- Ignore
>
> > [!definition] The $n$-simplex
> > An ==**$n$-simplex**== $[v_0,\dots, v_n]$ is the convex hull of $n+1$ points $v_0, \dots, v_n$ where $\{v_i - v_0\}$ are independent.
> In this definition, the order of the vertices $(v_0,\dots, v_n)$ is important; an $n$-simplex is a tuple of vertices, not a set.

> [!example] Standard $n$-simplex
> The ==**standard**== $n$-simplex is $\Delta^n = \{(t_0,\dots, t_n)\in \RR^{n+1} : \sum t_i = 1, t_i\geq 0\}$.

There is a canonical linear homeomorphism from $\Delta^n$ to any $n$-simplex via barycentric coordinates.

>[!definition] Faces and boundary
> If one deletes a vertex of $[v_0,\dots, v_n]$, one obtains an $n-1$ simplex $[v_0,\dots, \hat{v_i}, \dots, v_n]$; this is called a ==**face**==. When we describe a face of an $n$-simplex, the coordinates will always be their order in the larger subsimplex. You can delete more vertices too.
> 
> The ==**boundary**== $\pa \Delta^n$ of a simplex is the union of all of its faces; the ==**open simplex**== $\mathring{\Delta}^n = \Delta^n - \pa \Delta^n$.

Obviously, there is a canonical linear inclusion $\epsilon^i_n: \Delta^{n-1}\to \Delta^n$ if $\Delta^{n-1}$ is a face of $\Delta^n$. To write it out:
$$
	\epsilon^i_n: (x_1,\dots, x_i, \dots, x_n) \to(x_1,\dots, 0, \dots, x_n)
$$

>[!problem]
>Show $\epsilon^i_n\circ \epsilon^j_{n-1} = \epsilon^{j+1}_n\circ \epsilon^i_{n-1}$ for $i\leq j$.