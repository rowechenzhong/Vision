We now have had several instances where an object of the form $d\bullet$ has been defined:
- $dt$ represents infinitesimal Lebesgue measure, and satisfies $t = \int_0^t ds$.
- $dA$ for a [[Finite Variation Processes|FVP]] represents an infinitesimal step of a FVP, and satisfies $A_t - A_0 = \int_0^t 1dA_s$.
- $dM$ for a [[Continuous Local Martingales|CLM]] represents an infinitesimal step of a CLM, and satisfies $M_t - M_0 = \int_0^t 1dM_s$.
- $dX$ for a [[Continuous Semimartingale|CSM]].

Note the integrals on the RHS all have slightly different meanings, but the [[Construction of Stochastic Integral|stochastic integral]] subsumes all definitions. In particular, for all of the above, for any LBPP $H$, $\int_0^t H_s dX_s = \lim\sum H \Delta X$ in probability.

Thus, we write $dX = dX'$ if $\int_0^t dX = \int_0^t dX'$, i.e. $X_t - X_0 = X'_t - X'_0$ for all $t$; in this case, we are guaranteed that $dX$ and $dX'$ behave the same IP as infinitesimals within the stochastic integral.

# CLM Intuition

We would like to say that $M$ is a CLM iff $\EE[dM] = 0$. Let's