# Graph Theory

>[!definition] Graph
>An ==**undirected graph**== $G$ consists of a set of **vertices** $V$ and a set of **edges** $E$. Each edge is an unordered pair of distinct vertices. We write $G = (V, E)$. 
> - The vertices represent points, and the edges represent connections between these points.
> - If two vertices are connected by an edge, they are called **adjacent**.
> - The **degree** of a vertex is the number of edges connected to it.
> - A graph can be **finite** or **infinite**, depending on whether $V$ and $E$ are finite or infinite sets.

>[!example] A Square
>Consider a simple undirected graph $G$ where $V = \{A, B, C, D\}$ and $E = \{(A, B), (B, C), (C, D), (A, C)\}$. 
>- Here, the vertices $A, B, C,$ and $D$ can represent cities, and the edges represent direct roads between them.
>- The degree of vertex $A$ is $2$ because it is connected to both $B$ and $C$.


>[!definition] Bipartite Graph
>An ==**undirected bipartite graph**== $G = (V, E)$ is a graph where the vertex set $V$ can be divided into two **disjoint** sets $U$ and $W$ such that every edge connects a vertex in $U$ to a vertex in $W$. No edges exist between vertices within the same set.
> - **Complete Bipartite Graph**: If every vertex in $U$ is connected to every vertex in $W$, the graph is called a **complete bipartite graph** and is denoted as $K_{m,n}$ where $m = |U|$ and $n = |W|$.

>[!example]
>Consider a bipartite graph $G$ where $U = \{1, 2\}$ and $W = \{A, B, C\}$, and $E = \{(1, A), (1, B), (2, B), (2, C)\}$.
>- Here, the vertices $1$ and $2$ could represent different types of workers, while $A, B,$ and $C$ represent tasks. 
>- The edges show which workers can perform which tasks. For example, worker $1$ can do tasks $A$ and $B$, while worker $2$ can do tasks $B$ and $C$.