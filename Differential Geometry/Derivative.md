Let $U\subset V$ be an open subset of a vector space. Let $f:U\to W$ be a continuous function, and $p\in U$. Suppose there exists a linear map $T:V\to W$ such that
$$
\lim_{\norm{v}_V\to 0} \frac{\norm{f(p + v) - f(p) - T(v)}}{\norm{v}_V} = 0
$$
Then, $T$ is the ==**total derivative**== of $f$ at $p$, we let $(Df)_p = T$, and we say $f$ is ==**differentiable at**== $p$. As usual, if $f$ is differentiable at all points, then $f$ is ==**differentiable**==. One can then discuss properties of $Df$, such as whether it is continuous; this leads to the notion of [[regularity class]].

Nobody actually cares about anything other than $W = \RR^1$ because you can project, so I'll do that from now on, such that $(Df)_p \in V^\vee$. It is a terrible accident that $V^\vee \cong V$, thus $Df$ can be interpreted as a vector in its own right called the *gradient*; this is morally reprehensible and we will never use this.

>[!problem] Chain Rule
>Show for any map $g:W\to X$ for which all quantities are defined, $D(g\circ f)_p = Dg_{f(p)}\cdot Df_p$.
>
>In particular if $A$ is linear, $D(A\circ f))_p = A\circ (Df)_p$ as expected.
>


# Partial derivative

Alternatively, you can pick a basis. Given $e_1,\dots, e_n$ and dual basis $e_1,\dots, e_n$ of $V$, the ==**$i$-th partial derivative**== of $f:U\to \RR$ is
$$
	\frac{\pa f}{\pa e_i}(p) = \lim_{t\to 0} \frac{f(p+te_i) - f(p)}{t}
$$
just as you expect. This reduces to what you learned in high school:

>[!problem] Components
>If $Df$ exists, then so do the partials, and
> $$
> 	Df = \sum_i \frac{\pa f}{\pa e_i}e_i^\vee
> $$

>[!solution]-
>If $Df_p$ exists, then we can take the limit along the $v = te_i$ as $t\to 0$, yielding
>$$
>	0 = \lim_{t\to 0} \frac{f(p + te_i) - f(p) - tT(e_i)}{t}\implies Df_p(e_i) = \frac{\pa f}{\pa e_i} e^\vee_i
>$$
>Thus all partials exist, and we can expand $Df$ in the $\{e_i^\vee\}$ basis.

In words, "the total derivative is a matrix full of partial derivatives." This yields the [[Jacobian matrix]] in the general case

>[!problem] Continuous Partials implies differentiable
>Let $f:U\to \RR$, and suppose that $\frac{\pa f}{\pa e_i}$ is both defined and continuous for each $i$. Then $f$ is differentiable.
>
>Show that $$f(x,y) = \begin{cases}\frac{xy}{x^2 + y^2} & (x,y)\neq (0,0)\\ 0 & (x,y) = (0,0)\end{cases}$$ is a counterexample if we drop the continuous condition.

>[!solution]-
>Walk along each component. It is important that $\frac{\pa f}{\pa e_i}$ is differentiable for each $i$, or the rate of change of each line might not be bounded.
>
>Specifically, let $w_i = v_1e_1+\dots+v_i e_i$. After walking along each component, it suffices to prove
>$$
>\lim_{\norm{v}_V \to 0} \frac{\norm{f(p + w_i + v_{i+1}e_{i+1}) - f(p + w_i) - \frac{\pa f}{\pa e_i}(p) v_i}}{\norm{v}} = 0
>$$
>Fix $\delta > 0$.
>
>There exists an $\eps_1$ such that for all $\norm{v_{i+1}} < \eps_1$,
>$$
> \norm{f(p + w_i + v_{i+1}e_{i+1}) - f(p + w_i) - \frac{\pa f}{\pa e_i}(p + w_i) v_i} < 0.001\delta v_i
>$$
>Thus, there also exists an $\eps_2$ such that for all $\norm{v} < \eps_2$ the above statement holds (as $C_1\norm{v}\leq \norm{v_2} \leq C_2\norm{v}$ for some constants $C_1, C_2$).
>
>There exists an $\eps_3$ such that for all $\norm{w} < \eps_3$,
>$$
>\norm{\frac{\pa f}{\pa e_i}(p + w_i) - \frac{\pa f}{\pa e_i}(p)} < 0.001\delta
>$$
>Combining everything, we get our result.