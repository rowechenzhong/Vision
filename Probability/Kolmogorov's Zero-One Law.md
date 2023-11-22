This elementary theorem has a very [[Ergodic Theory|ergodic]] flavor.

Let $(X_n: n\in \NN)$ be a sequence of random variables, and
$$\mathfrak{T}_n = \sigma(X_{n+1},\dots), \qquad \mathfrak{T} = \bigcap_n \mathfrak{T}_n$$
Then, $\mathfrak{T}$ is the ==**tail $\sigma$-algebra**==, characterizing events which depend solely on the limiting behavior of the sequence.

>[!idea]
>This is the infinite hat-guessing equivalence class idea!

> [!theorem] K$01$
> If $X_n$ are [[independence|independent]], then $\mathfrak{T}$ contains only events of measure $0$ or $1$. In particular, any $\mathfrak{T}$-measurable RV is constant AS.

If $\FFF_n = \sigma(X_1,\dots X_n)$ as usual, $\FFF_n \pperp \mathfrak{T}_n$, thus $\FFF_\infty \pperp \mathfrak{T}$ are independent too. But this means if $A\in \mathfrak{T}$, $\PP(A) = \PP(A \cap A) = \PP(A)^2$ as desired.

A very funny proof, huh?