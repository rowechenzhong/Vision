Let $F:X\to Y$ be a regular map. Now that we have [[Differential|differentials]] which are linear maps $dF_P: T_PX\to T_{F(P)} Y$, we can talk about basic properties of linear maps.

>[!definition] Submersion and Immersion
> -  If $d F$ is surjective for all $P\in X$, then we call $F$ a [[Submersion]]. 
> - If $dF$ is injective for all $P\in X$, then we call $F$ an ==**immersion**==. Intuitively, $F$ does not have a local kernel; it is locally homeomorphic to its image.
>   ^submersion-immersion

> [!example] Stupid Examples
> Let $m < n$ be positive integers. Consider:
> $$i(x_1,\dots x_m)\to (x_1,\dots, x_m, 0,\dots, 0),\qquad s(x_1,\dots, x_n)\to (x_1,\dots x_m)$$
> 
> Then $i$ is an immersion while $s$ is a submersion. This ends up being almost completely general.

Note that we only care about local properties here! Globally, when given the topology of $Y$, immersions are not necessarily manifolds! This leads to the notion of an [[Immersed Submanifold]] and [[Embedding]].