A bounded function $f$ on $E$ is ==**harmonic**== if $Pf = f$. Then $f(X_n)$ is a bounded martingale; by [[Martingale Convergence Theorems|MCT]] it admits an AS-$L^p$ limit for all $p < \infty$.

More generally, for $D\subset E$ a bounded function $f$ is ==**harmonic on $D$**== if $Pf\big\vert_D = f\big\vert_D$.

Harmonic functions are pretty tight. If $\pa D = E\setminus D$ and we fix a bounded $f$ on $\pa D$, it turns out that there is essentially one way to make a bounded harmonic function on $D$ which agrees with this (observe that the harmonic condition extends to edges depth-$1$ outside of $D$).

>[!theorem] Harmonic Extension
> Let $T = \inf \{n\geq 0: X_n\in \pa D\}$ and $u(x) = \EE_x\left(f\left(X_t\right)\id_{T\leq \infty}\right)$. Then, $u$ is bounded and harmonic in $D$, while $u = f$ on $\pa D$.
> 
> If $\PP_x(T < \infty) = 1$ for all $x\in D$, then $u$ is the unique bound extension of $f$ which harmonic in $D$.