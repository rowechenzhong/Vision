# Hahn-Banach Theorem 
 
 
> [!definition] Functional
 $V' = \BB(V, F)$ is the ==**dual space**== of $V$, containing ==**functionals**== on $V$. 

 Of course, if $F$ is complete (e.g. $\RR, \CC$) then $V'$ is a Banach space. This dual *sort of* works like you would expect. Let's prove a main theorem on this dual space. Here's the objective: 
 
> [!theorem] Han-Banach Theorem
 Let $M\subset V$ be a subspace. If $u:M\to \CC$ is a bounded linear functional, then there exists a bounded linear functional $U:V\to \CC$ such that $U(t) = u(t)$ for all $t\in M$ and $\norm{U} = \norm{u}$. 

## Simplified Problem 
 
 First, we should demonstrate that we can extend a bounded linear functional by just one element, in the real case. 
 
 >[!claim]
 >Let $V$ be a normed $\RR$ vector space, and let $M$ be a subspace. Let $u:M\to \RR$ be a bounded linear functional. Then, if $x\notin M$, let $M' = M + \RR x$. Then, there exists a function $u': M'\to \RR$ such that $u'(t) = u(t)$ for all $t\in M$ and $\norm{u'} = \norm{u}$. 

 
> [!proof] 
 If your bounding constant is $0$, then $u' = 0$ works. Otherwise, divide by that constant such that $\norm{u} = 1$. Now, any extension is uniquely determined by $\lambda = u(x)$; we simply require that for all $t\in M$, $$ \abs{u(t) - \lambda} \leq \norm{t - x} $$ This is now incredibly straightforward; we're solving for $\lambda \in \RR$, and we can break the absolute value into two cases. For all $t_1, t_2$ in $M$, we require that $$ u(t_1) - \norm{t_1 - x}\leq \lambda \leq u(t_2) + \norm{t_2 - x} $$ Taking the supremum of the lower bound and the infimum of the upper bound, we just have to show $$ u(t_1) - \norm{t_1 - x} \leq u(t_2) + \norm{t_2 - x} $$ for all $t_1, t_2\in M$. But this is just triangle inequality: $$ u(t_1) - u(t_2) = u(t_1 - t_2) \leq \norm{t_1 - t_2} \leq \norm{t_1 - x} + \norm{t_2 - x} $$ 

 
> [!idea] 
 If you attempt to repeat this proof directly in the complex setting, the problem is there are \"a lot of ways for $\abs{u(t) + \lambda}$ to be large.\" In retrospect, looking at the complex case now appears *more* not less daunting; the space of acceptable $u(t)$ is some convex region in $\CC$, bounded by lines. Perhaps Helly's theorem yields a direct proof?

## Successor Case 
 
 >[!claim]
 >Let $V$ be a normed $\CC$ vector space, and let $M$ be a subspace. Let $u:M\to \CC$ be a bounded linear functional. Then, if $x\notin M$, let $M' = M + \CC x$. Then, there exists a function $u': M'\to \CC$ such that $u'(t) = u(t)$ for all $t\in M$ and $\norm{u'} = \norm{u}$. 
 
>[!proof] 
>  The basic claim is that **any complex vector space can be regarded as a real vector space.** First, let $w(t) = \frac{1}{2}(u(t) + \conj{u(t)})$; use the real case to find a real functional $w'(t) : M + \RR x \to \RR$ such that $w'(t + ax) \leq \norm{t + ax}_V$ for all $a\in \RR$. Repeat this computation to find a real functional $w\": M + \RR x + \RR (ix)\to \RR$ such that $w\"(t + ax + b(ix)) \leq \norm{t + ax + b(ix)}_V$ for all $a, b\in \RR$. We're not quite done-- $w\"$ is some properly bounded continuous extension, but it might not even be linear in the complex sense! The fix: $$ u'(t + (a + bi) x) = w\"(t + ax + b(ix)) - iw\"(it - bx + a(ix))\forall a, b\in \RR $$ To check that this is linear in the complex sense, it suffices to check scaling by $i$, which can be done manually. Then, we have to check that $u'$ is bounded properly. This is true; there is some argument $\theta$ such that $$ \norm{u'(t + cx)} = \Re e^{i\theta} u'(t + cx) = w\"(e^{i\theta}t + e^{i\theta}cx)\leq \norm{t + cx}_V $$ 

## General Case 
 
It's Zorn time. Let $E$ be the poset containing *all* extensions of $u$, which are ordered pairs $(v,N)$ containing a function $v$ and a subspace $N$, ordered such that $(v_1, N_1) \leq (v_2, N_2)$ if $v_1 = v_2$ on $N_1$ and $N_1\subset N_2$. For any chain $C = \{v_i, N_i\}_{i\in I}$ in this poset, the maximal element is $(v, N)$, where: 
 -  $N = \bigcup_{i\in I} N_i$. 
 -  $v$ is a function defined on $N$; pick any $x\in N_i\subset N$. Then, $v(x) = v_i(x)$. This is well-defined because for all $N_i, N_j\subset M$ such that $x\in N_i$ and $x\in N_j$, $v_i(x) = v_j(x)$. 
 
 Yay, take a maximal element $(v,M)$ of the whole thing. If $M\neq V$, use the successor case to kill.

## Corollaries 
 
> [!problem] 
 For any normed space $V$ and element $\norm{v} = 1$, there is a continuous linear functional $f:V\to \CC$ sch that $f(v) = 1$ and $\norm{f} = 1$. 
 
> [!solution] 
 Well, I can certainly define this on $\CC v$; Hahn-Banach rips this functional through the whole space. 

 Alright, we're now going to check whether or not duality is an involution, like its supposed to be. The ==**double dual**== is $V\"$. 
 
> [!theorem] Duality
 Let $v\in V$, and let $T_v: V'\to \CC$ via $T_v(v') = v'(v)$. Then, the map $T: V\to V\"$ via $v\to T_v$ is isometric (and thus injective). 

> [!proof] 
 This is clearly linear; its just a contraction. It's also bounded because $$ \sup_{\norm{v} = 1} \norm{T(v)} = \sup_{\norm{v} = 1} \norm{T_v} = \sup_{\norm{v} = 1}\sup_{\norm{v'} = 1} \norm{T_v(v')} \leq \sup_{\norm{v} = 1}\sup_{\norm{v'} = 1} \norm{v'}\norm{v} = 1 $$ (lol). Okay, but we want this to be equality, not just bounded. We need to show that for all $\norm{v} = 1$ there actually exists a $\norm{v'} = 1$ such $v'(v) = 1$. This was precisely the above corollary. 

 Okay, so we know that the double-dual has an isomorphic copy of $V$ living inside it. But is $T$ surjective? Here's a partial result: 
> [!problem] 
 $\BB(V,B)$ is a Banach space. 

 
> [!solution] 
 Fine. Give me an absolutely summable sequence $\{T_n\}$. We'll show $\sum_n T_n$ is summable. The target $T$ is defined pointwise; this is well-defined because $$ \norm{\sum_n (T_n v)} \leq \sum_n \norm{T_n} \norm{v} = \abs{C}\norm{v}< \infty $$ (we used norm-limit interchange) and $B$ is Banach. $T$ is linear because $$ T(av + w) = \lim_{m\to \infty} \sum_{n = 1}^m T_n(av + w) = \lim_{m\to \infty} \sum_{n = 1}^m aT_nv + T_nw = aTv + Tw $$ $T$ is bounded because $$ \sup\norm{\lim_{m\to\infty} \sum_{n=1}^m T_n v} = \sup\lim_{m\to\infty} \norm{\sum_{n=1}^m T_n v} $$ by interchange and the interior is bounded $\abs{C}\norm{v}$. Finally, $\{T_n\}$ converges to $T$ in the operator norm because $$ \sup \norm{\sum_{n = 1}^m T_n - T}v = \sup \norm{\sum_{n > m} T_n} v \leq \sup \sum_{n > m} \norm{T_n} \norm{v} = \sum_{n > m} \norm{T_n} \to 0 $$ Lol. 

 In particular, $(V')'$ is Banach, so if $T$ is surjective, $V$ has to be Banach too. If you are Banach and have the property that $V = V\"$, i.e. $T$ is surjective, then $V$ is called ==**reflexive**==. ## Functionals on sequences 
 
 
> [!example] Functionals on sequences
 Let $V = \ell^p$ for $1 \leq p \leq \infty$. We will show the correspondence between $(\ell^p)'$ and $\ell^q$ for $1/p + 1/q = 1$. Specifically, for $p < \infty$, there is a bijective isometry between $(\ell^p)'$ and $\ell^q$, while if $p = \infty$, there is merely an injection. For any $b\in \ell^q$, define $T_b: \ell^p\to \CC$ via $T_b(a) = \sum a_n b_n$. This is an element of $\ell^q$, and $\norm{T_b} = \norm{b}$. Thus the map $T:b\to T_b$ is an injective isometry. Conversely, for any $T\in (\ell^p)'$, define $b(T)$ via $b(T)_n = T(e_n)$. This is an element of $\ell^q$. If $p < \infty$, then actually these two operations are inverses; $$ T(a) = \sum a_n b(T)_n $$ $p = \infty$ fails to be true in this regard. 

 
> [!proof] Forward Direction
 $T_b$ is clearly linear. For any $a\in \ell^p$, we have $$ \abs{\sum a_k b_k }\leq \norm{a}_p\norm{b}_q $$ by Holder's inequality. Observe that Holder's inequality is perfectly valid for $1\leq p\leq \infty$. Thus, $T_b$ is bounded by $\norm{b}$. To saturate the inequality: 
>  
>  
>  
>  -  **If $1 < p < \infty$:** Let $a_k = \frac{\abs{b_k}^q}{b_k}$, with $a_k = 0$ if $b_k = 0$. Then: $$ \norm{a} = \left(\sum \abs{a_k}^p\right)^{1/p} = \left(\sum \abs{b_k}^q\right)^{1/p} = \norm{b}_q^{q/p} < \infty $$ and $$ \abs{\sum a_k b_k} = \sum \abs{b_k}^q = \norm{b}_q^q = \norm{a}_p \norm{b}_q $$ 
>  
>  -  **If $p = \infty$:** If $b = 0$ we're done. Else let $a_k = \frac{\abs{b_k}}{b_k}$, with $a_k = 0$ if $b_k = 0$. Then: $$ \norm{a} = \sup_k \abs{a_k} = 1 $$ and $$ \abs{\sum a_k b_k} = 1\cdot (\sum \abs{b_k}) $$ 
>  
>  -  **If $p = 1$:** We need to actually use the supremum definition of the norm here. Let $a_k$ be the indicator function at $N$; then $\norm{a_k} = 1$ and $\abs{\sum a_k b_k} = \abs{b_N}$, so $\norm{T_b} \geq \abs{b_N}$ for all $N$. 
>  
>  

 
> [!proof] Backwards Direction, showing $b_k\in \ell^q$
 This direction is slightly harder. We already know that $T$ is bounded. In particular, there exists some $c$ such that for all *finite* sequences $a = (a_1,\cdots, a_n, 0, \cdots)$, $$ \sum_{k\leq n} a_k b_k \leq c\norm{a}_p $$ 
>  
>  
>  
>  -  **If $1 < p < \infty$:** Let $a_k = \abs{b_k}^q/b_k$. Then, the equation reads $$ \sum_{k\leq n} \abs{b_k}^q \leq c \left(\sum_{k\leq n} \abs{b_k}^q\right)^{1/p} $$ $p > 1$ strictly, so this shows that $\sum_{k\leq n} \abs{b_k}^q$ is uniformly bounded by $c$; thus $b_k\in \ell^q$. 
>  
>  -  **If $p = 1$:** $\abs{b_k} = \abs{f(e_k)} \leq \norm{f}$, so $b \in \ell^\infty$. 
>  
>  -  **If $p = \infty$:** Let $a_k = \abs{b_k} / b_k$ (this just aligns all the $b_k$'s). Then $\sum_{k\leq n} \abs{b_k} \leq c$, and $b\in \ell^1$. 
>  
>  

 
> [!proof] Backwards direction, Verifying Inverse
 For $1\leq p < \infty$, I already know that $$ f((a_1,\cdots, a_n, 0,\cdots)) - \sum_{k\geq 1} a_k b_k = 0 $$ The first term is continuous by assumption, the second term is continuous by the forward direction. Thus, this whole thing is one continuous function. **Only if $p < \infty$, the sequence of prefixes converges to the whole sequence.** If $p = \infty$, then the prefixes of $(1,1,1\cdots)$ do not converge to $(1,1,1,\cdots)$. 

 
> [!proof] Counterexample for $p = \infty$
 Consider $c_0 \subset \ell^\infty$ containing sequences which converge to $0$. Let $u$ be the functional on $c_0$ mapping $a$ to $\lim_{k\to \infty} a_k$. This is linear and bounded by $1$. By Hahn-Banach, we can extend $u$ to a functional $f$ on $\ell^\infty$ with $\norm{f} = 1$. By passing in indicator functions, if any $b_k$ exists such that $$ f(a_k) = \sum a_k b_k $$ then $b_k$ must be identically $0$. This clearly fails, because $f$ is nonzero. 

 ## Transposes 
 
 Do mathematicians actually call these things adjoints??? Ouch lmao. 
 
> [!definition] Transpose
 Let $T: V\to W$ be a bounded linear map. Then, the ==**transpose**== of $T$ is the map $T^\top: W'\to V'$ defined via $$ T^\top(f) = f\circ T $$ We claim $\norm{T^\top} = \norm{T}$, and in particular $T^\top$ is bounded. 

 
> [!proof] 
 This is definition chasing. $T^\top$ is linear because $$ T^\top(f + g) = (f + g)\circ T = f\circ T + g\circ T = T^\top(f) + T^\top(g) $$ and $$ T^\top(\lambda f) = (\lambda f)\circ T = \lambda (f\circ T) = \lambda T^\top(f) $$ $T^\top$ is bounded because $$ \norm{T^\top f} = \norm{f\circ T} \leq \sup_{\norm{v} = 1} \norm{f(Tv)} \leq \sup_{norm{w} \leq \norm{T}} \norm{f(w)} = \norm{f}\norm{T} $$ On the other hand, for all $\eps > 0$, by definition, there exists a $\norm{v} = 1$ such that $$ \norm{T(v)} + \eps \geq \norm{T} $$ By Hahn, we pick the functional $f$ such that $f(T(v)) = \norm{T(v)}$ and $\norm{f} = 1$. Then, $$ \eps + \sup_{\norm{v} = 1} \norm{f(T(v))} \geq \norm{T} $$ We conclude.