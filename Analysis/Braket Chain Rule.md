>[!idea] $\lim \sum \Delta X \Delta F(Y) = \lim \sum F'(Y) \Delta X \Delta Y$.

It turns out that this piece of intuition (like all of the others) is correct, by a quick application of Ito's formula.

>[!claim]
>Given CSMs $X, Y$ and a $C^2$ function $f$, $d\braket{X,F(Y)}_t = F'(Y_t) d\braket{X,Y}_t$.

Indeed, by Ito's formula, $F(Y) = \int_0^t F'(Y_t) d Y_t + \int_0^t \frac{F''(Y_t)}{2} d\braket{Y,Y}_t$. Thus the braket against $X$ is just $$\braket{X,F(Y)} = \braket{X, F'(Y)\cdot Y} = F'(Y) \braket{X,Y}$$ as desired.