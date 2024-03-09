Van Kampen's theorem computes the [[fundamental group|fundamental group]] of the union of two spaces.
 
  Let's set up the notation. \todo{draw a diagram lol} 
 -  $X$ is a union of path-connected open subsets $A_\alpha$ for $\alpha \in \mathcal{A}$, such that each $A_\alpha$ contains basepoint $x_0$. We drop references to this basepoint from now on. 
 -  Let $$ F = \underset{\alpha\in\mathcal{A}}\ast \pi_1(A_\alpha) $$ be the free group. 
 For every $U, V, W \in \mathcal{A}$: 
 -  $U\cap V\cap W$ is path-connected. 
 -  There exists natural homomorphisms $$ i_U: \pi_1(U\cap V) \stackrel{i_U}{\to} \pi_1(U) \stackrel{k_U}{\to} \pi_1(X) $$ via topological inclusion. 
 -  There exists natural inclusion homomorphism $$ j_U: \pi_1(U)\to F. $$
 By the universal property of the free group, there exists a natural homomorphism $$ \Phi:F\to \pi_1(X) $$ compatible with each $k_U$. 
 
> [!theorem] Van Kampen's Theorem
> $\Phi$ is surjective. Let $N$ be the smallest normal subgroup containing $$ \left(j_U\circ i_U(\gamma)\right) \left( j_V \circ i_V(\gamma) \right)^{-1} $$ for all $\gamma\in \pi_1(U\cap V)$ for all $U,V \in \mathcal{A}$. Then $\ker \Phi = N$. 

 In a sense, this should be obscenely obvious. If I start from $x_0$, what can I do? I can walk around inside $U$ until I get back to $U\cap V$, or walk around inside $V$ until I get back to $U\cap V$, and eventually I execute some arbitrary string of elements in $U$ and $V$ and wind up back at $x_0$. Obviously I shouldn't double-count nontrivial loops inside $U\cap V$, so I need to mod out by all of those. 
 
> [!proof]- Proof $\Phi$ is surjective
 You literally do what I just said. Pick any loop $\gamma:I\to X$. Then, the preimage of $U$ on $I$ is a collection of open sets. By the definition of a basis, we can split each open set into a union of open intervals. The interval is compact, thus we can extract a finite subcover $(a_i, b_i)$ ordered by increasing $a_i$. WLOG no interval contains another, and WLOG no two adjacent intervals are members of the same open set $U$ or $V$. Let $s_0 = [0, \frac{a}]$, $s_i = \frac{a_i + b_{i-1}}{2}$ for $i = 1, 2, \cdots, n$, and $s_{n+1} = 1$. By construction, each $\gamma([s_i, s_{i+1}])$ lies entirely inside either $U$ or $V$, and each $\gamma(s_i)$ lies inside $U\cap V$. By hypothesis, we can also connect each $\gamma(s_i)$ to $x_0$ by a path in $U\cap V$, $\beta_i$. Thus, the entire $\gamma$ is a concatenation of loops inside $U$ or $V$: $$ \gamma = \gamma([s_0, s_1])\beta_1^{-1}\quad \beta_1^1 \gamma([s_1, s_2])\beta_2^{-1}\quad \cdots \quad \beta_n^1 \gamma([s_n, s_{n+1}]) $$ 
  
> [!proof]- Proof $N\subset \ker \Phi$
 This is basically tautological. For any path $\gamma$ inside $U\cap V$, the inclusions $j_U\cap i_U$ and $j_V\cap i_V$ map $\gamma$ to the exact same loop inside $X$. So of course this is an element of the kernel. 

 I will return to show the hard part of this proof someday, maybe, if I ever have the time.