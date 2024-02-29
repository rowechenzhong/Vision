Fix some group $G$. Let $EG$ be the semi-simplicial set $EG_n = G^{n+1} = \{(g_0,\dots g_n)\}$. Face maps work via deleting coordinates. Observe that $G\curvearrowright EG_n$ via$$g\cdot (g_0,\dots, g_n) = (gg_0,\dots, gg_n).$$letting us define the semi-simplicial set $BG$ via $BG_n = (EG_n) / G$. This is still a semi-simplicial set because this is a completely combinatorial object and our face maps didn't change. This is sort of equivalent to setting $g_0\equiv 1$, but for some reason we're supposed to imagine $BG_n$ as displacements or paths$$
(g_1|\dots|g_n) \equiv [1, g_1, g_1g_2,\dots, g_1g_2\dots g_n]\in BG_n.
$$In this way, $\pa_0(g_1|\dots|g_n) = (g_2|\dots|g_n)$, $\pa_i(g_1|\dots|g_n) = (g_1|\dots|g_ig_{i+1}|\dots|g_n)$, and $\pa_n(g_1|\dots|g_n) = (g_1|\dots|g_{n-1})$.

Somehow, this chain complex is so important that $H_*(G) \equiv H_*(BG)$ is called the ==**homology**== of group $G$.

I'll evaluate some low dimensions as an exercise.

Observe that $\pa_1 = 0$ and $\pa_2:(g_1|g_2) \to (g_2) - (g_1|g_2) + (g_1)$. Thus $H_1 = \bigoplus (g)\ZZ$ modulo $(g_1)+(g_2) \sim (g_1g2)$, which means as abelian groups, $H_1\cong G / [G,G]$. This is pretty cracked, and shows that $BG$ is really good.

Onwards!