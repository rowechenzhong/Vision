Let's drop some intuition about why a Clifford algebra is constructed the way it is. (WIP?)

Suppose I have a finite-dimensional $V$ with inner product, and consider the space of tensors on $V$. I will perform a long computation inside $T V$, which might involve lots of tensor products (no contractions though!), but at the end of the day, all I want to know is what the ==**full trace**== of my object is.

The full trace of some generic element $e_{i_1}\otimes \dots \otimes e_{i_k}$ written in terms of an orthonormal basis is:
- $0$ if there there is any $e_j$ which appears an odd number of times.
- Otherwise, there is some permutation $\sigma$ of $[k]$ such that $e_{i_{\sigma_{2n}}} = e_{i_{\sigma_{2n + 1}}}$, i.e., there is a way to rearrange the $e_i$'s into pairs which are valid contractions. The full trace of this term is then $(-1)^\sigma$.

This is a natural thing to do on any vector space with an inner product.

The question is, how much information do I have to keep track of at all times in order to be able to compute this full trace at the end.

This didn't turn out to be as cool as I thought it would. Hmmm.