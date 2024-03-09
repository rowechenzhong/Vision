>[!definition] DGFF
>The ==**discrete GFF on $D$ with Dirichlet boundary conditions**== is the centered Gaussian vector $(\Gamma(x))_{x\in D}$ whose density function is
$$p(\gamma) \sim \exp\left( -\frac12 \frac{\mathcal{E}_D(\gamma)}{2d}\right),\qquad \gamma \in \RR^D,$$
where $\mathcal{E}_{D}$ is the ==**energy function**==$$\mathcal{E}_D(F) = \sum_{e\in E_{\bar{D}}} \abs{\nabla F(e)}^2.$$

>[!idea]
>We can add a $\sigma$ to the denominator of the expression; this amounts to scaling $\gamma$.

### Resampling Procedure
If we condition on $(\Gamma(y))_{y\in D\setminus\{x\}}$, $\Gamma(x)$ is distributed as
$$\sim \exp\left( - \frac{1}{4d} \sum_{y: y\sim x} \abs{\gamma_x - h(y)}\right) = \exp\left( - \frac12 (\gamma_x - \bar{h}(x))^2\right)$$
This immediately implies $\Gamma(x) - \overline{\Gamma(x)}\sim N(0,1)$ for all $x$. Consider the Markov Chain on $\Ff_{(D)}$, where on each step we choose a point $x\in D$ uniformly at random (any distribution supported on $D$ works) and replace $h(x)$ with $\bar{h}(x) + N(0,1)$. This is the ==**resampling procedure**== under which the GFF is the stationary distribution. 

### Covariance Function
Denote the ==**covariance function**== $\Sigma(x,y) = \Sigma_x(y) = \EE[\Gamma(x)\Gamma(y)]$. Observe that$$
\begin{align*}
	\Sigma_x(y) &= \EE[\Gamma(x)\Gamma(y)]\\
	&= \EE[\Gamma(x)\bar{\Gamma}(y)] + \underbrace{\EE[\bar\Gamma(x)(\Gamma(y) - \bar{\Gamma}(y))]}_0\\
	&+ \EE[(\Gamma(x) - \bar{\Gamma}(x))(\Gamma(y) - \bar{\Gamma}(y))]\\
	&= \overline{\Sigma_x}(y) + \id_{x=y}\\
	\implies \Delta \Sigma_x(y) &= -\id_{x = y}
\end{align*}
$$where the underbraced expression is $0$ by the resampling procedure.