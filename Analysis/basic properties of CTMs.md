>[!claim] Boosting submartingales
>If $X_t$ is a submartingale and $f$ is a nondecreasing convex function, then $f(X_t)$ is also a submartingale (assuming $f(X_t)$ is in $L^1$).
>
>Alternatively, if $X_t$ is a martingale and $f$ is a nonnegative convex funnction, then $f(X_t)$ is automatically a submartingale.

>[!proof]- Jensen
>It is clearly adapted, and postulated to be integrable. The inequality follows from Jensen;
>$$
>\EE[f(X_t)|\FFF_s] \geq f\left(\EE[X_t | \FFF_s]\right)\geq f(X_s)
>$$

>[!claim] Bounding supermartingales
>If $X_t$ is a supermartingale, then $\sup\{\EE[\abs{X_s} : 0\leq s\leq t]\} < \infty$ for all $t < \infty$.