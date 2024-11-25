There are two chains of ideals that are interesting to us:
- The ==**derived series**==, $L^{(k)} = [L^{(k-1)}, L^{(k-1)}]$. $L$ is ==**solvable**== if this vanishes.
- The ==**descending central series**== or ==**lower central series**== is $L^k = [L, L^{k-1}]$. $L$ is ==**nilpotent**== if this vanishes.

# Solvability + Nilpotency

>[!problem] Properties
> - If $L$ is solvable, then so are all subalgebras and homomorphic images.
>   Note that $(L/I)^{(k)} \subseteq L^{(k)} / I$ and $(L/I)^k \subseteq L^k / I$.
> - If $I, J$ are solvable ideals in $L$, then $I + J$ is solvable.
> 
> Ditto for nilpotency.

> [!solution]-
> Subalgebras are obviously solvable/nilpotent. Homomorphic images satisfy $\phi(I)^{(k)} = \phi(I^{(k)})$, so we're fine (ditto for nilpotence).
> 
> If $I,J$ are solvable/nilpotent, then clearly so is $[IJ]\subset I\cap J$ (because $I$ and $J$ are ideals). Thus, you can do combo lol. The slick solution: $(I+J)/J \sim I/(I\cap J)$ naturally, and clearly both $I/(I\cap J)$ and $J$ are solvable.
> 
> I'm not sure about the slick solution for nilpotence, but $(I + J)^{2n}\subset (I^{2n}+J^0) + \cdots + (I^0 + J^{2n}) = 0$.

(The second condition implies there exists a [[radical|maximal solvable ideal]]).

>[!problem] Solvability bootstrapping
> If $I$ is a solvable ideal of $L$ such that $L / I$ is solvable, then $L$ is solvable too.

>[!solution]-
> - If $L/I$ is solvable, then $L^{(k)}$ is eventually inside $I$; this is solvable, thus we conclude.

# Nilpotency

>[!problem] Properties
> - If $L/Z(L)$ is nilpotent, then so is $L$.
> - If $L$ is nilpotent and nonzero, $Z(L)\neq 0$.

> [!solution]-
> - $L^k$ is eventually inside $Z(L)$, which vanishes on the next step.
> - We look at the last term of the sequence.

The correct characterization here is [[Engel's Theorem]].

>[!problem]
>Suppose $K$ is a [[subalgebra]] (not necessarily and [[Lie ideal|ideal]]) of nilpotent $L$. Then,
>$$
>	N_L(K) = \{x: [x,K] \subset K\}
>$$
>strictly contains $K$.
>
>Thus, any nilpotent $L$ 
>- has an ideal of codimension $1$ (easy)
>- admits an outer derivation (less easy, but not hard).

>[!solution]-
> Clearly $K\subset N_L(K)$. Note that $L/K$ is a homomorphic image of $L$ and thus nilpotent. Thus, $Z(L/K)\neq 0$; there exists some $0\neq x+K\in L/K$ such that $[x+K, L/K] = 0$. Then, $[x, K] \subset K$. Win.
> 
> Now, take any proper subalgebra $L$. We know that $N_L(K)$ strictly contains $K$, and in fact by the construction above we can add in an $x$ such that $K + \FF x$ is still a valid ideal. Do this until $K$ has codimension $1$. By the claim, $K + \FF x = L$ for some $x$ such that $[x,K] = K$. Thus $[L, K] = K$, and $K$ is in fact an ideal.

>[!solution]- Last part
> Here's a way to generate outer derivations. $\delta$ is going to send $K$ to $0$. We want to pick a smart place to send $x$; we choose it to lie in $C_L(k)$, which is nonzero because $0\neq Z(k)\subset C_L(k)$. In this case, Leibniz works automatically.
> 
> The problem is that $\delta$ might be secretly an inner derivation $[\gamma, \bullet]$. $[\gamma, K] = 0$, thus $\gamma$ must be in $C_L(K)$. We also have $[\gamma, x] = \delta(x)$; we want to make sure this is impossible.
> 
> The way to fix this is to find an $n$ such that $C_L(k)\subseteq L^n$ but $C_L(k)\nsubseteq L^{n+1}$. Then, pick $\delta(x)$ in $C_L(k) \setminus $L^{n+1}$. This way $[\gamma,x]\in L^{n+1}$, yet $\delta(x)$ is not.

>[!problem] Nilpotent boostrapping (This has nothing to do with Engel)
> Let $L$ be a Lie algebra and $K$ be an ideal. $L/K$ is nilpotent, and for all $x\in L$, $\ad x|_K$ is nilpotent.
> 
> Show $L$ is nilpotent.

> [!solution]-
> This is just completely clear; $L^n\subset K$ eventually, and $\ad$ nilpotency finishes.