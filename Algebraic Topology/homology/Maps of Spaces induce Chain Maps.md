---
aliases:
  - induced map
  - induced maps
---
A map $\phi:X\to Y$ induces a [[Chain Map]] on their corresponding [[Chain Complexes]] via $f_n:C_n\to D_n$ sending $\sigma\to \phi\circ \sigma$.

This is a chain map, because$$
\begin{align*}
\pa_n(D)\circ f_n(\sigma)
&=\pa_n(D)(\phi \circ \sigma)\\
&=\phi \circ (\pa_n(C)\sigma)\\
&=\phi \circ (\pa_n(C)\sigma)\\
&=(f_{n-1}\circ \pa_n(C))(\sigma)\\
\end{align*}$$for each $n$.