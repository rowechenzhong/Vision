Let $F:X\to Y$ be a regular map. Now that we have [[Differential|differentials]] which are linear maps $dF_P: T_PX\to T_{F(P)} Y$, we can talk about basic properties of linear maps.

>[!definition] Submersion and Immersion
> -  If $d F$ is surjective for all $P\in X$, then we call $F$ a ==**submersion**==. Intuitively, $F$ locally fills $Y$.
> - If $dF$ is injective for all $P\in X$, then we call $F$ an ==**immersion**==. Intuitively, $F$ does not have a local kernel; it is locally homeomorphic to its image.
>   ^submersion-immersion

>[!problem]  Implicit Function Theorem
> In full generality-- if $F$ is a submersion then for any $Q\in Y$, $F^{-1}(Q)$ is a manifold of dimension $\dim X - \dim Y$.

>[!solution]
>This is a local question. For any $P\in F^{-1}(Q)$, we wish to exhibit a local homeomorphism to $\RR^{n-m}$. Looking at local charts $\phi: U\to \RR^n$. and $\psi: V\to \RR^m$ with $P\in U$ and $Q\in V$, we observe that $\psi \circ F\circ \phi^{-1}$ is also a submersion.
>
 Thus, we must show $\phi\circ F^{-1} Q$ is locally homeomorphic to $\RR^{n-m}$ inside $\RR^n$. This is just the [[Basic Manifold Exercises#^1292a3|Implicit Function Theorem]].

Note that we only care about local properties here! Globally, when given the topology of $Y$, neither submersions nor immersions are necessarily manifolds!

For immersions, this leads to the notion of an [[Immersed Submanifold]] and an [[Embedding]].