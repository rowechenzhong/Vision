---
aliases:
  - chain homotopic
  - chain homotopy
---
A chain homotopy $\phi\stackrel{h}{\to} \psi$ between two [[Chain Map|chain maps]] $\phi$ and $\psi$ is a collection of maps $(h_n: C_n\to D_{n+1})_n$ such that$$\phi_n - \psi_n = \pa_{n+1}(D) h_n + h_{n-1}\pa_n(C).$$For short, we write $\phi - \psi = \pa_D h + h\pa_C$. Then, $C$ and $D$ are said to be ==**chain homotopic**==.

>[!idea] Ultimate GPU exercise
>See why homotopic maps induce chain homotopies.

![[Chain Homotopy.png]]