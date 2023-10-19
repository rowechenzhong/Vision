Okay.

This motherfucker is defined by
$$
	\sl_2 = \braket{e, h, f | [h, e] = 2e, [h,f] = -2f, [e,f] = h}
$$

This guy acts on the uh what the fuck

The algebra of polynomials $\CC[x,y]$ via
$$
	e\to x\pa_y,\qquad  f\to y\pa_x, \qquad h\to x\pa_x - y\pa_y
$$
Okay motherfucker what's happening. We can write
$$
	V_n = \spn\braket{x^iy^j | i + j = n}
$$
And then $hx^iy^j = (i-j)x^iy^j$ for instance. The full vector space is
$$
	V = \bigoplus_n V_n
$$

Last time, we showed that $V_n$ were [[irreducible]] under $\sl_2$.
Let $V_n(k)$ is the $k$-eigenspace of $h$ inside $V_n$; this is one polynomial.
$$
	V_n = V_n(-n) + V_n(-n+2) + \dots\oplus V_n(n)
$$

The set of $h$-weights in $V_n$ is $h$.

So it's pretty clear that
- $\dim V_n = n+1$
- $\dim V_n(k) \in \{0,1\}$.

Okay!

The objective is to show that:
- $\{V_n\}_{n\geq 0}$ are all irreps of $\sl_2$. Why is this useful?
- And then any finite dim representation of $\sl_2$ is a direct sum of $V_n$. Why the fuck is this useful?

