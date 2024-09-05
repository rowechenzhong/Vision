---
aliases:
  - tower property
---
>[!definition] Conditional Expectation
>Let $X$ be an integrable or nonnegative random variable, and let $\GGG\subset \FFF$ be a $\sigma$-algebra. Then, there exists a unique random variable $[Y]$ such that
> - $Y$ is $\GGG$-measurable.
> - $Y$ is integrable.
> - $\EE[X\id_A] = \EE[Y\id_A]$ for all $A\in \GGG$.
>   
> We call $[Y] = \EE(X | \GGG)$ the ==**conditional expectation of $X$ given $\GGG$**==. In the case where $\GGG = \sigma(G)$ for some random variable $G$, we can also write $[Y] = \EE[X | G]$.

>[!idea]
>You can also just take a conditional expectation with respect to an event $A\in \FFF$: $\EE[X | A] = \EE[X\id_A] / \PP[A]$ if $\PP[A] > 0$ and undefined otherwise.

> [!proof]- Obviously Unique
> Suppose $Y, Y'$ are both $\GGG$-measurable, integrable, and $\EE[Y\id_A] = \EE[Y'\id_A]$ for all $A\in \GGG$. Then clearly $[Y] = [Y']$. Indeed, suppose for sake of contradiction that $Y > Y'$ on some positive-measure set $A\in \GGG$. Then, well, it's not that deep. (Details: $\PP(Y > Y') > 0\implies \exists k\in \NN : \PP\left(Y - Y' > \frac{1}{k}\right) > 0$ thus $\EE\left[(Y - Y')\id_{Y - Y' > \frac1k}\right] > 0$.

>[!proof] Existence follows by projection!
> Consider first the case where $X\in K = L^2(\Omega, \GGG, \PP)\subset H = L^2(\Omega, \FFF, \PP)$. Then, $\EE[\abs{X Z}]^2 \leq \EE[X^2]\EE[Z^2] < \infty$ for any $Z\in H$. Note that $\id_A$ span the elementary functions, which form a dense subset of $L^1(\Omega, \GGG, \PP)$. So the conditions are really just saying that $X - Y\perp H$! Let $Y$ be the projection of $X$ onto $K$ then, which exists by elementary Hilbert space theory; this $Y$ is in $L^2\subset L^1$.
> 
> Now we bootstrap, details omitted.

>[!idea]
>A conditional expectation interprets random variables as a partition of state space, then considers the expectation over each sector.

>[!idea]
>Conditional expectations are *only* defined in an almost-sure sense; thus instead of writing $[\EE[X | \GGG]]$ every single line, we interpret $\EE[X | \GGG]$ as a [[Canonical equivalence classes of Measurable functions|canonical equivalence class]] by definition.

# Properties

We will now show that middle-school mathematics works pretty well. I claim I can skip the proofs if I've been using the interface since mathcounts.

> [!theorem] Arithmetic Properties of Conditional Expectation
> Let $X$ and $Y$ be integrable random variables, and let $\GGG\subset \FFF$ be a $\sigma$-algebra. Let $\alpha,\beta \in \RR$.
> 
> 1. $\EE[\EE[X | \GGG]] = \EE[X]$.
> 2. If $X$ is actually $\GGG$-measurable, then $\EE[X | \GGG] = [X]$.
> 3. If $X$ is [[independence|independent of]] $\GGG$, then $\EE[X | \GGG] = [\EE[X]]$.
> 4. If $[X]\geq 0$, then $\EE[X |\GGG]\geq 0$.
> 5. $\EE[\alpha X + \beta Y | \GGG] = \alpha \EE[X | \GGG] + \beta \EE[X | \GGG]$
> 6. **(Jensen):** If $c: \RR \to (-\infty, \infty]$ is convex, $\EE[c(X) | \GGG] \geq c\left(\EE[X | \GGG]\right)$.

> [!theorem] Information Properties of Conditional Expectation
> Some "information" results:
> 1. **(Tower Property):** Suppose $\HHH\subset \GGG$. Then $\EE[\EE[X | \GGG] | \HHH] = \EE[X | \HHH]$.
> 2. If $Y$ is bounded and $\GGG$-measurable, then $\EE[YX | \GGG] = Y\EE[X | \GGG]$.
> 3. If $\sigma(X, \GGG)$ is independent of some other sigma algebra $\HHH$, then $\EE[X | \sigma(\GGG, \HHH)] = \EE[X | \GGG]$.

> [!idea] Intuition
> 1. $\HHH$ has less information than $\GGG$. Integrating over $\HHH$ at the end will wash out the integrals over $\GGG$.
> 2. $Y$ is known conditioned on $\GGG$. It is a constant on each partition.
> 3. $\HHH$ is like a required humanities class. Completely useless.

Please review the [[Convergence properties of Lebesgue Integral]].

> [!theorem] Convergence Theorems of Conditional Expectation
> Suppose $X_n$ are a sequence of random variables. Let $Y$ be some integrable random variable.
>  1. **Monotone Convergence Theorem:** If $0\leq [X_n]\uparrow [X]$, then $\EE[X_n | \GGG]\uparrow \EE[X | \GGG]$.
>  2. **Fatou's Lemma:** If $X_n\geq 0$ for all $n$, then $\EE[\lim \inf X_n | \GGG] \leq \lim \inf \EE[X_n | \GGG]$.
>  3. **Dominated Convergence Theorem:** If $X_n \to X$ and $\abs{X_n} \leq Y$

One more random claim: [[Conditional Expectations are UI]].

# Motivating Examples (Todo!)

This reduces to our mathcounts understanding in many cases of interest.

>[!example] Discrete

>[!example] Gaussian

>[!example] Conditional Density Functions