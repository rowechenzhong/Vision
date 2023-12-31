# Compact 
 
 Compactness is pretty important. Recall from point-set topology the following various equivalent definitions of a compact subset of a *metric space*: 
 
 
 
 -  Sequential compactness: every sequence has a convergent subsequence. 
 
 -  Completeness and total boundedness: for every $\eps > 0$, there exists a covering by finitely many $\eps$-balls. 
 
 -  Usual compactness: every open cover has a finite subcover. 
 
 Shrug! We'll present two ways to check something is compact on a Hilbert space. First, an elegant basis-free approach: 
> [!theorem] Finite Dimensional Approximations
 $K\subset \HH$ is compact iff: 
>  
>  
>  
>  -  $K$ is closed (which immediately implies $K$ is complete). 
>  
>  -  $K$ is bounded. 
>  
>  -  For all $\eps > 0$, there exists a finite-dimensional subspace $W\subset \HH$ such that for all $u\in K$, there exists a $w\in W$ such that $\norm{u - w} < \eps$. 
>  
>  

 Shrug! This actually isn't too difficult; its just a slight rewording of the standard total boundedness condition to be more amenable to vector spaces. 
> [!proof] Statement implies Compact
 Pick an $\eps$; we're going to fill up $K$ with $\eps$-balls. First off, use the statement to find a finite-dimensional subspace $W$ such that all points of $K$ are within $0.001\eps$ of $W$. I know that $K$ is bounded; $K\subset B_R(0)$. WLOG $R \gg \eps$. The set of $W\cap \overline{B_{2R}(0)}$ is closed and bounded, but it is also a subset of $W\equiv \CC^n$, thus by Heine-Borel it is compact. Thus, it can be covered by finitely many $0.001\eps$-balls. Finally, take all of those balls and increase their radius to $\eps$. We conclude. 

 
> [!proof] Compact implies Statement
 We show the contrapositive. Flipping all the quantifiers, suppose $$ \exists \eps \forall W \exists u\in K \forall w\in W,\qquad \norm{u - w}\geq \eps. $$ Well, fix that $\eps$. We'll create a sequence of $W$'s and $u$'s. Let $W_0 = \emptyset$. Then, given $W_i$, let $u_i \in K$ be such that for all $w\in W_i$, $\norm{u_i - w} \geq \eps$. Then, let $W_{i+1}$ be the span of $W_i$ and $u_i$. Then, each $W_i$ is finite dimensional, $W_i\subset W_{i+1}$, and we have found a sequence of $u_i$'s such that $\norm{u_i - u_j}\geq \eps$ for all $i\neq j$. This clearly has no converging subsequence, so $K$ is not compact. 

 Here is a second approach: 
> [!definition] Equi-Small Tails
 Let $\{e_k\}$ be a countable orthonormal subset. A subset $K\subset H$  is said to have ==**equi-small tails**== with respect to $\{e_k\}$ if for all $\eps > 0$, there is some $N$ such that for all $v\in K$ we have $$ \sum_{k > N} \abs{\braket{e_k | v}}^2 < \eps $$ Note that $\forall v \exists N$ is already guaranteed by Bessel's inequality; the strength here is that the convergence is uniform. 

 
> [!problem] Equi-Small Tails Characterization
 Let $\HH$ be a *separable* Hilbert space with orthonormal basis $\{e_k\}$. A subset $K\subset H$ is compact iff $K$ is closed, bounded, and has equi-small tails with respect to $\{e_k\}$. 

 \todo{Lol write the solution} ## Finite Rank Operators 
 
 
> [!definition] Finite Rank Operators
 \label{defn:finite-rank} An operator $T\in \BB(\HH, \HH)$ is said to have ==**finite rank**== if $T(\HH)$ is finite-dimensional. The set of finite rank operators is denoted $\mathcal{R}(\HH)$. 

 Finite-rank operators are very nice, because we can basically just write them down as a finite-dimensional matrix (or an \"infinite matrix with cofinitely many zeros\"). 
> [!problem] 
 An operator $T\in \BB(\HH, \HH)$ has finite rank iff there exists a finite orthonormal set $\{e_k\}_{k\leq L}$ and complex entries $c_{ij}$ such that $$ Tu = \sum_{i,j \leq L} c_{ij} \braket{e_j | u} e_i $$ for all $u\in \HH$. 

 
> [!problem] Properties of Finite Rank Operators
 Show that $\mathcal{R}(\HH)$ is a star-closed two-sided ideal in $\BB(\HH)$. This has three components: 
>  
>  
>  
>  -  **Star Closure** means that if $T\in \mathcal{R}(\HH)$, then $T^*\in \mathcal{R}(\HH)$. 
>  
>  -  **Two-Sided Ideal** means: 
>  
>  
>  
>  -  **Closure under Addition:** If $T, S\in \mathcal{R}(\HH)$, then $T + S\in \mathcal{R}(\HH)$. 
>  
>  -  **Closure under Multiplication:** If $T\in \mathcal{R}(\HH)$ and $S\in \BB(\HH)$, then $ST, TS\in \mathcal{R}(\HH)$. 
>  
>  
>  
>  

 \todo{Do it lol.} Although $\mathcal{R}(\HH)$ is a subspace, it isn't closed. 
> [!example] Finite Rank Operators are not Closed
 Consider the sequence of operators on $\mathcal{R}(\HH)$ called $$ T_n a = \left\{ \frac{a_1}{1}, \frac{a_2}{2}, \frac{a_3}{3}, \dots \frac{a_n}{n}, 0, \dots \right\} $$ The limit of this sequence is $$ T a = \left\{ \frac{a_1}{1}, \frac{a_2}{2}, \frac{a_3}{3}, \dots \right\} $$ The range contains all standard basis vectors, so this cannot be finite-dimensional. 

 So it makes sense to ask what this closure is. ## Compact Operators 
 
 
> [!definition] Compact Operators
 \label{defn:compact-operators} An operator $T\in \BB(\HH, \HH)$ is said to be ==**compact**== if $\overline{T(B_0(1))}$ is compact. The set of compact operators is denoted $\mathcal{K}(\HH)$. 

 The key ideas about compact operators are the following two problems: 
> [!problem] Closure of Finite Rank Operators
 Show that $\mathcal{K}(\HH)$ is the closure of $\mathcal{R}(\HH)$. 

 
> [!problem] Star-Closed Two-Sided Ideal
 Show that $\mathcal{K}(\HH)$ is a star-closed two-sided ideal in $\BB(\HH)$. 

























