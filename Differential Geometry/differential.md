Let $F:X\to Y$ be a regular map and $P\in X$. The ==**differential**== of $F$ at $P$ is exactly what you expect: a linear map $d_PF: T_PX\to T_{F(P)}Y$ sending any $v\in T_P(X)$, $f\in O_{F(P)}$ to
$$
(d_PF\cdot v)(f) = v(f\circ F)
$$
We also write $dF_P\cdot v = F_*v$.

To unpack what this is doing: $v$ is an infinitesimal change at $P$. If we pass this through a locally linear function called $F$ at $P$ (which is precisely $d_PF$), we should get a corresponding vector "$F(P+v) = F(P) + F_*(v)$." How should $F_*(v)$ behave? Well, if you move along $F_*(v)$ at $F(P)$, then any function $f:V \to \RR$ should change by the same amount as $f\circ F:U\to V\to \RR$-- which is simply $v(f\circ F)$.

This is *exactly* what you think it is.

>[!problem] Chain Rule
>Show that if $F: X\to Y$ and $G:Y\to Z$ are regular maps,
>$$
>	d(G\circ F)_P = dG_{F(P)}\circ dF_P
>$$

>[!solution]
>This is completely stupid; let $f:Z\to \RR$ be regular and $v\in T_PX$; then
>$$
>	(d(G\circ F)_P \cdot v)(f) = v(f\circ G\circ F) = dF_PV(f\circ G) = ((dG_{F(P)}\circ dF_P)\cdot v)(f)
>$$