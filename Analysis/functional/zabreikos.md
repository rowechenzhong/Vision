# Foundational Theorems 

We will now prove $4$ foundational theorems of functional analysis. As suggested by [this blog post](https://math.blogoverflow.com/2014/06/25/zabreikos-lemma-and-four-fundamental-theorems-of-functional-analysis/), all of these four theorems follow from an overarching main lemma. The main lemma itself follows from the Baire category theorem.
## An obvious but crucial lemma

> [!theorem] Zabreikos Lemma
 Let $p: X\to [0,\infty)$ be a [[seminorm]] on a Banach space. Suppose that, for all *absolutely convergent* sequences $\sum_{n=1}^\infty \norm{x_n} < \infty$, $$ p\left(\sum_{n=1}^\infty x_n\right) \leq \sum_{n=1}^\infty p(x_n) $$ Then, $p$ is continuous on $X$. 

>[!example]
>If $p$ is continuous on $X$, then the theorem trivially holds (prove it!)
>
>It is surprising and non-trivial that a generic seminorm need not be continuous on $X$; such seminorms are [pathological and non-constructive](https://math.stackexchange.com/questions/907560/discontinuous-seminorm-on-banach-space). So in a sense, this lemma is really silly. It's a river to cross in all of our major theorems, but the river is highly pathological.

> [!proof]- Baire go brr
>  The standard way to begin all of these proofs is to let $A_n = p^{-1}([0,n))$ for all $n > 0$, and let $F_n = \overline{A_n}$. Observe that $A_n$ and $F_n$ are both [[seminorm|convex]].
> 
> The $F_n$ form a closed cover of $X$, thus by Baire's theorem (which is the only usage of completeness of $X$), $$ \exists N, R, x_0 \qquad B_R(x_0)\subset F_N $$ Then, WLOG $x_0 = 0$, because $B_R(-x_0)\subset F_N$, and by convexity $B_R(0)\subset F_N$. Also, WLOG $R = 1$ by scaling. The result is that $B_1(0)\subset F_N$.

>[!idea] This theorem is really weak but important.
> We haven't used the problem condition yet, and we already know that for some $n > 0$, $B_1(0)\subset \overline{p^{-1}([0,n))}$!

>[!proof]- Finishing it
Pick any $x$ and $r$ such that $\norm{x} < r < 1$. Let $0 < \eps < 1 - r$. Then, $y = \frac{x}{r}$ is inside $F_N$. Pick a $y_0\in A_N$ such that $\norm{y - y_0} < \eps$. Then, $\frac{1}{\eps}(y - y_0) \in B_1(0)$, so we can repeat; choose a $y_1\in A_N$ such that $\norm{\frac{1}{\eps}(y - y_0) - y_1} < \eps$. Then, $\frac{1}{\eps^2}(y - y_0 - \eps y_1) \in B_1(0)$, ad infinitum. Thus, $y = \sum_{k = 0}^\infty \eps^k y_k$. Each $\norm{y_k}\leq 1 + \eps$, thus this series is absolutely convergent. Thus, by the hypothesis, $$ p(y) \leq \sum_{k=0}^\infty p(\eps^k y_k) \leq \sum_{k=0}^\infty \eps^kN = \frac{N}{1-\eps} $$ Thus $p(x) = rp(y) < \frac{N}{1-\eps}r < N$, so $x\in A_N$. 

# The four major theorems
 
> [!problem] Open Mapping Theorem
 Let $X, Y$ be Banach spaces, and $T\in \BB(X, Y)$ be surjective. Then, $T$ is an open map. 

>[!solution]- Could be phrased better, todo
>Let $p:W\to \RR$ be the seminorm sending
> $$
> 	p(w) = \inf_{v\in T^{-1}(w)}\norm{v}
> $$
> Then, ummmm, why's this a seminorm? Well, for any $u,w\in W$, 
> $$\inf_{v\in T^{-1}(u + w)} \norm{v} \leq \inf_{v \in T^{-1}(u)} \norm{v} + \inf_{v'\in T^{-1}(w)} \norm{v'}$$
> right? why? because for all $v,v'$, um, $\norm{v} + \norm{v'}\geq \norm{v + v'}$, sure.
> 
> So now um $p$ is a seminorm and it satisfies the conditions because it just does.
> 
> And the theorem says that there exists an open ball inside $\{w: \inf_{v\in T^{-1}(w)}\norm{v} < 1\} = T(B_0(1))$, as desired.
> 


> [!problem] Bounded Inverse Theorem
 If $T\in \BB(X, Y)$ is a bijective map, then $T^{-1}$ is bounded. 

>[!solution]-
>By the previous solution, $T$ is an open map, thus $T^{-1}$ is a homeomorphism.
> 
> Alternatively, we can let $p(w) = \norm{T^{-1}(w)}$. Then, $p$ is a seminorm because $$\norm{T^{-1}(u + v)} = \norm{T^{-1}(u)} + \norm{T^{-1}(v)} \leq \norm{T^{-1}(u)} + \norm{T^{-1}(u + v)}$$
> Then uh, there exists a ball inside $\{w: \norm{T^{-1}(w)} < 1\} = T(B_1(0,1))$, i.e. $T^{-1}$ is continuous gg.


> [!problem] Uniform Boundedness Theorem
 Let $\{T_n\}$ be a sequence in $\BB(B, V)$. Suppose for all $b\in B$, we have $\sup_n \norm{T_n b} < \infty$. Then, $\sup_n \norm{T_n} < \infty$. In other words, pointwise boundedness implies uniform boundedness. 

> [!solution]-
> Just let $p(x) = \sup_{n\in \NN} \norm{T_n(x)}$ which is finite by assumption; this is obviously a seminorm.
> $$
> \sup_n \norm{T_n\left(\sum_i x_i\right)} = \sup_n \norm{\sum_i T_nx_i}\leq \sup_n \sum_i \norm{T_nx_i}\leq \sum_i \sup_n \norm{T_nx_i}
> $$
> Thus $$p^{-1}([0,1)) = \{x: \sup_{n\in N} \norm{T_n(x)} < 1\}$$contains a ball $\norm{x} < \eps$; but then $\sup_n \norm{T_n} \leq \frac{1}{\eps}$, win.


> [!definition] Graph
 Let $f:X\to Y$ be a function. The ==**graph**== of $f$ is the set $$ \Gamma_f = \{(x, f(x)) : x\in X\}\subset X\times Y $$ 


> [!problem] Closed Graph Theorem
 Let $X$ and $Y$ be Banach spaces, and $T:X\to Y$ be an *arbitrary* linear operator. Then, $T$ is bounded iff $\Gamma_T$ is closed. 

> [!solution]-
> For any Cauchy sequence $(x_i, y_i)\subset \Gamma_T$ your $x_i$'s must be Cauchy; then they admit a limit $x$. Suppose $T$ is bounded; then $x_i\to x$ implies $T(x_i)\to T(x)$. Thus the limit point is in the set, and $\Gamma_T$ is closed.
> 
> Let $p(x) = \norm{T(x)}$; this is clearly a seminorm.
> $$
> 	\sum_n \norm{T(x_n)}\leq \norm{\sum_n T(x_n)}
> $$
> because stare at tails or something lol (this doesn't really require the lemma; its a composition of continuous functions).
> 
> Then, $T^{-1}\left(B_0(1)\right)$ contains a ball.

# Deprecated

Here are direct proofs of the four major theorems; the Zabriekos approach is more unified, and these are included for completeness.
 
### Uniform Boundedness Theorem 
 
 
> [!theorem] Uniform Boundedness Theorem
 Let $\{T_n\}$ be a sequence in $\BB(B, V)$. Suppose for all $b\in B$, we have $\sup_n \norm{T_n b} < \infty$. Then, $\sup_n \norm{T_n} < \infty$. In other words, pointwise boundedness implies uniform boundedness. 

 
> [!proof] 
 Consider the following closed cover of $B$: $$ C_k = \{b\in B : \norm{b} \leq 1, \sup_n \norm{T_n b}\leq k\} $$ Each $C_k$ is closed because it is the intersection of a bunch of preimages of closed sets under continuous functions. (Specifically, $\norm{b} \leq 1$, and $\norm{T_n b}\leq k$.) Thus, by Baire's theorem, one of the $C_k$ has nonempty interior, containing some open ball $B(b_0, \delta)$. Thus, for any $b \in B(0,\delta)$, $$ \sup_n \norm{T_n b} \leq \sup_n \norm{T_n(b_0 + b)} + \sup_n \norm{T_n b_0} \leq 2k $$ By rescaling, we conclude. 

 ### Main Lemma 
 
 
> [!theorem] Open Mapping Theorem
 Let $X, Y$ be Banach spaces, and $T\in \BB(X, Y)$ be surjective. Then, $T$ is an open map. 

 First, let's prove a lemma. \begin{claim*} The closure of the image of the open ball $B_X(0,1)$ is a neighborhood of the origin. \end{claim*} 
> [!proof] 
 $T$ is surjective, thus we can write down the closed cover $$ V_2 = \bigcup_{n\in \NN} \overline{T(B_X(0, n))} $$ where the line means closure. **$Y$ is Banach**, so by Baire's theorem, one of the $\overline{T(B_X(0, n))}$ has nonempty interior, containing some open ball $B_Y(b_0, \delta)$. Well, suppose $B_Y(b_0, \delta) \subset \overline{T(B_X(0, k))}$. Then, for all $v\in B_Y(0,1)$, we have $b_0 + \delta v \in B_Y(b_0, \delta)$, thus $b_0 + \delta v \in \overline{T(B_X(0, k))}$. Subtracting, we find that $$ \delta v \in \overline{T(B_X(0, k))} - \overline{T(B_X(0, k))} \subset \overline{T(B_X(0, 2k))} $$ Allowing $L = \frac{\delta}{2k}$, we see that for all $v\in B_Y(0,L)$, $$ v\in \overline{T(B_X(0, 1))} $$ 

 We're almost there! This is literally what we want, except for the stupid closure. You'll notice we haven't used the Banach property of $X$ yet. \begin{claim*} The image of the open ball $B_X(0,1)$ is a neighborhood of the origin. \end{claim*} 
> [!proof] 
 Now, by definition of closure on a metric space (sequential, i.e. limit points, i.e. things grow arbitrarily close), our current progress reads: \begin{center} For all $v\in Y$ such that $\norm{v} < L$, and for any $\eps > 0$, there exists $x\in X$ such that $\norm{x} < 1$ and $\norm{v - Tx} < \eps$. \end{center} By scaling $v$ such that $\norm{v}$ is arbitrarily close to $L$, we find: \begin{center} For all $y\in Y$, and for any $\eps > 0$, there exists $x\in X$ such that $L\norm{x} \leq \norm{y}$ and $\norm{y - Tx} < \eps$. \end{center} 
> > [!idea] 
> Observe that $L\norm{x}\leq \norm{y}$! I'm emphasizing and being precise here because, in some sense, this entire problem is about the difference between $<$ and $\leq$.
> 
>  Okay great. Pick any $v\in B_Y(0,L)$, and pick some $0 < \eps$. We can find a $x_0\in X$ such that $\norm{x_0} < 1$ and $\norm{v - Tx_0} < \eps L$. Then, we can pick some $x_1\in X$ such that $\norm{x_1} < \eps$ and $\norm{v - Tx_0 - Tx_1} < \eps^2 L$. And so on. Observe that $x_0, x_1,\cdots$ converges absolutely. Thus, the partial sums $\sum_{i=0}^n x_i$ are Cauchy. **$X$ is banach**, therefore the partial sums converge to some $x\in X$. Next up, $Tx_0 + Tx_1 + \cdots = Tx$ (these two quantities are equal by definition of limit) converges to $v$, by construction. The norm of $x$ is bounded above by $1 + \eps + \cdots$; pick $\eps = 0.0001$ and we discover that $\norm{x} < 2$. Thus, the image of $B_X(0,2)$ contains $B_Y(0, L)$. By scaling, we conclude. 

 
> [!problem] 
 Conclude the proof of the open mapping theorem, by scaling and moving the ball around. 

 
> [!solution] 
 Any open set in $X$ is a union of a bunch of balls. Each ball is of the form $aB_x(0,1) + b$. These get mapped to $aT(B_X(0,1)) + T(b)$, which is open by the previous claim. 

 ### Immediate Corrolaries 
 
 
> [!problem] 
 If $T\in \BB(X, Y)$ is a bijective map, then $T^{-1}$ is bounded. 

 ### Application: Closed Graph Theorem 
 
 
> [!definition] Graph
 Let $f:X\to Y$ be a function. The ==**graph**== of $f$ is the set $$ \Gamma_f = \{(x, f(x)) : x\in X\}\subset X\times Y $$ 

 
> [!theorem] Closed Graph Theorem
 Let $X$ and $Y$ be Banach spaces, and $T:X\to Y$ be an *arbitrary* linear operator. Then, $T$ is bounded iff $\Gamma_T$ is closed. 

 Let's explain why this is useful. Suppose I wanted to prove that $T:X\to Y$ was bounded. Then, I need to show that it is continuous. Thus, give me any sequence in $X$, $\{u_n\}$, which converges to a point $u\in X$. It need to show that $T(u_n)$ converges to $T(u)$. Sure. Using this theorem, I am given a sequence $\{u_n\}$ which converges to $u$. However, I am *also* guaranteed that $T(u_n)$ converges to some point $v\in Y$. All I need to do is show that $v = T(u)$, and I'm done. 
> [!proof] 
 The forward direction is trivial. Otherwise, suppose the backwards direction. We have projections $\pi_x: \Gamma(T)\to X$ and $\pi_y: \Gamma(T)\to Y$. These are continuous, and thus bounded. Observe that $\pi_x$ is actually bijective; thus, $\pi_x^{-1}$ is *also* continuous. Thus, $\pi_y\circ \pi_x^{-1}$ is continuous. But this is just $T$!