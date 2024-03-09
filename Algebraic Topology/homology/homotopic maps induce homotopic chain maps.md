>[!theorem] Homology is a functor from hTop to homotopy category of chain complexes
>If $f_0$ and $f_1$ are homotopic, the maps $(f_0)_*, (f_1)_*: C_*(X)\to C_*(Y)$ are chain homotopic.

Thus $(f_0)_* = (f_1)_*: H_*(X)\to H_*(Y)$ for instance; **homotopic maps induce the same maps on homology groups**. This immediately implies **homotopic spaces have the same homology groups**.

# The Ultimate GPU exercise
If $f_0, f_1: X\to Y$, there exists a map $F: X\times I\to Y$ such that $F(\bullet,0) = f_0$ and $F(\bullet, 1) = f_1$. This $F$ induces a chain map from $C(X\times I)$ to $C(Y)$; by inclusion map $\sigma \to (\sigma\times I)\subset (X\times I)$, this induces a chain map $h:C_*(X)\to C_{*+1}(Y)$. Then stare at the definition of [[Chain Homotopy|chain homotopy]].

It's too beautiful, I'm so happy. It's important that you see how this will work before we start bashing.

# Algebraic bash, for fun

>[!idea] Hint
>I rendered $n = 2$ first. Do that, then come back. Otherwise don't read this section.

>[!proof]- Defining $h$
> Let me describe $h$ more carefully. Start with some $\sigma: \Delta^n\to X$. Accordingly, $F\circ \sigma: \Delta^n\times I\to Y$. From this prism, we can extract $n + 1$ different $(n+1)$-simplices. Indeed, describing $\Delta^n$ by barycentric $x_0,\dots x_n$ coordinates, I can partition $\Delta^n\times I$ by whether the last coordinate $w$ lies in relation to
> $$0,\quad x_0,\quad x_0 + x_1,\quad\dots,\quad x_1+\dots + x_{n-1},\quad x_1+\dots+x_n = 1.$$Now, denote the image of $\sigma = [a_0a_1\dots a_n]$ under $f_0$ and $f_1$ by $[01\dots n]$ and $[\bar{0}\bar{1}\dots\bar{n}]$ (these are tuples of points in $Y$). I wish for
> $$h(\sigma) = \sum_{0\leq i\leq n} (-1)^{n(i+1)} [i(i+1)\dots n\bar{0}\dots\bar{i}]$$
> where the under-specified simplices are defined through the partition above.

>[!proof]- Computing $\pa h$
> We claim that these $h$ form the necessary [[Chain Homotopy|chain homotopy]]. First we compute $\pa h(\sigma)$.
> $$\begin{align*}
> \pa h(\sigma)
> &=\sum_{0\leq i\leq n} (-1)^{n(i+1)} \pa [i(i+1)\dots n\bar{0}\dots\bar{i}]\\
> &=\sum_{0\leq i\leq n} (-1)^{n(i+1)} \left(\sum_{i\leq j\leq n} (-1)^{j - i} [i(i+1)\dots \hat{j}\dots n\bar{0}\dots\bar{i}]\right)\\
> &+(-1)^{ni + 1}\left(\sum_{0\leq j\leq i}(-1)^{j - i}[i(i+1)\dots n\bar{0}\dots\hat{\bar{j}}\dots\bar{i}]\right)\\
> \end{align*}$$
> The $(i,j) = (k,k)$ term of the top series cancels with the $(i,j) = (k + 1, k + 1)$ term of the bottom series; the sign of the top thing is $(-1)^{n(k+1)}$ and the sign of the bottom thing is $(-1)^{n(k+1) + 1}$.
> $$\begin{align*}
> &=[\bar{0}\dots\bar{n}] - [0\dots n] + \sum_{0\leq i\leq n} (-1)^{ni + n} \left(\sum_{i < j\leq n} (-1)^{j - i} [i(i+1)\dots \hat{j}\dots n\bar{0}\dots\bar{i}]\right)\\
> &+(-1)^{ni + 1}\left(\sum_{0\leq j < i}(-1)^{j - i}[i(i+1)\dots n\bar{0}\dots\hat{\bar{j}}\dots\bar{i}]\right)\\
> \end{align*}$$

>[!proof]- Computing $h \pa$
> okay, we're halfway there. This time, we compute $h\pa(\sigma)$.
> $$
> \begin{align*}
> h\pa(\sigma)
> &= h\left(\sum_{0\leq j\leq n} (-1)^j [a_0\dots\hat{a_j}\dots a_n]\right)\\
> &= \sum_{0\leq j\leq n} (-1)^j \left(\sum_{0\leq i < j} (-1)^{(n-1)(i+1)}[i\dots\hat{j}\dots n\bar{0}\dots\bar{i}]\right)\\
> &+ (-1)^j \left(\sum_{j < i \leq n} (-1)^{(n-1)i}[i\dots n\bar{0}\dots \hat{\bar{j}}\dots\bar{n}]\right)\\
> &= \sum_{0\leq i\leq n} \left(\sum_{i < j\leq n} (-1)^{(n-1)(i+1) + j}[i\dots\hat{j}\dots n\bar{0}\dots\bar{i}]\right)\\
> &+ \left(\sum_{0 \leq j < i} (-1)^{(n-1)i + j}[i\dots n\bar{0}\dots \hat{\bar{j}}\dots\bar{n}]\right)\\
> \end{align*}
> $$
> Fucking legendary.
> $$\pa h(\sigma) + h\pa(\sigma) = [\bar{0}\dots\bar{n}] - [0\dots n] = f_1 \sigma - f_0 \sigma.$$