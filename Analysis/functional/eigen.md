# Eigenanalysis 
 
 We finally have the tools necessary to study eigenvalues, culminating in the spectral theorem. 
> [!problem] Inverses
 If $\norm{T} < 1$ is bounded, then $1 - T$ is invertible, and its inverse is the absolutely convergent series $$ (1 - T)^{-1} = \sum_{n=0}^\infty T^n. $$ 

 
> [!solution] 
 The series is clearly absolutely convergent, because the $k$-th term has norm $\norm{T^k} \leq \norm{T}^k$, We have $$ (1 - T)\sum_{n=0}^\infty T^n = \sum_{n=0}^\infty T^n - \sum_{n=0}^\infty T^{n+1} = I - T^{n+1} = I. $$ Similarly, $\sum_{n=0}^\infty T^n(1 - T) = I$. 

 Thus, 
> [!problem] 
 $\GL(\HH)$ is open. 

 Now, here are several closely related notions. 
> [!definition] Resolvent Set, Spectrum
 Let $T \in \BB(\HH)$. The ==**resolvent set**== of $T$ is $$ \Res(T) = \{ \lambda \in \CC : T - \lambda\in \GL(\HH)\}. $$ The ==**spectrum**== of $T$ is $$ \Spec(T) = \CC \setminus \Res(T) $$ 

 
> [!definition] Eigenthings
 Let $T \in \BB(\HH)$. If $T - \lambda$ is not injective, then there exists some nonzero $v \in \HH$ such that $Tv = \lambda v$. Then, $v$ is an ==**eigenvector**== of $T$, and $\lambda$ is an ==**eigenvalue**== of $T$. We let $E_\lambda$ denote the set of all eigenvectors with eigenvalue $\lambda$. 

 Unfortunately, injectivity, surjectivity, and invertibility do not coincide for infinite-dimensional linear maps. So while all eigenvalues are in the spectrum, the converse is not true. 
 
> [!theorem] 
 Let $A\in \BB(\HH)$. Then $\Spec(A)$ is a closed subset of $B_{\norm{A}}(0)$ in $\CC$. 

 Btw, by Liouville's theorem, $\Spec(A)\neq \emptyset$.
 
## Self-Adjoint 
 
 
> [!definition] Self-Adjoint
 A linear operator $T \in \BB(\HH)$ is ==**self-adjoint**== if $T = T^\dagger$. 

 Preliminary property: 
 
> [!problem] Trivial
 Show that $\braket{u | Tu}\in \RR$ for all $u$. 

> [!solution] 
 Take the adjoint. 

 Next, we will make steps towards the spectral theorem. 
 
> [!problem] 
 $\Spec(T)\subset [ - \norm{T}, \norm{T}]$. 

 
> [!problem] Tedious
 Show that $\norm{T} = \sup_{\norm{u} = 1} \abs{\braket{u | Tu}}$. 

 
> [!problem] 
 At least one of $\pm \norm{T}$ is in $\Spec(T)$. 

 
> [!problem] 
 Actually, let $a_- = \inf_{\norm{u} = 1} \braket{u | Tu}$ and $a_+ = \sup_{\norm{u} = 1} \braket{u | Tu}$. Then $a_-, a_+ \in \Spec(T)$, and $\Spec(T) \subset [a_-, a_+]$. 

 
> [!problem] Positive Operators
 A ==**positive operator**== is a self-adjoint operator such that $\braket{u | Tu} \geq 0$ for all $u$. Show $T$ is positive iff $\Spec(T) \subset [0, \infty)$. 

## Spectral Theory 
 
 We now restrict our attention to $T$ a *compact* self-adjoint operator. We basically know the entire roadmap towards the spectral theorem, because we've done this whole thing before in the finite-dimensional case; all we need to do is repeat everything with higher power. 
> [!problem] Finite Sanity Check
 If $\lambda \neq 0$ is an eigenvalue of $T$, then $E_\lambda$ is finite-dimensional. 

 
> [!problem] Orthogonality Result
 Distinct eigenspaces are orthogonal. 

 
> [!problem] Number of Eigenvalues
 The set of nonzero eigenvalues of $T$ is countable. If it is a countably infinite sequence $\lambda_1, \lambda_2, \dots$, then $\lambda_n \to 0$. 

 
> [!theorem] Fredholm Alternative
 Let $A$ be a compact operator (dropping self-adjointness for the time being), and let $\lambda \neq 0$ be real. Then the range of $A - \lambda$ is closed. 

 In particular, if $A$ is self-adjoint, then $(A-\lambda)(\HH) = \ker(A-\lambda)^\perp$. Thus, ether $A-\lambda$ is bijective, or $E-\lambda$ is nontrivial and finite-dimensional. In particular, 
 
> [!problem] Largest Eigenvalue
 Let $T$ be nonzero. Then, there is some nonzero eigenvalue $\lambda_1$ with $\lambda_1 = \sup_{\norm{u} = 1} \abs{\braket{u | Tu}}$. 

 By subtracting these off one at a time, 
> [!problem] Maximum Principle
 The nonzero eigenvalues of $T$ can be ordered $\abs{\lambda_1} \geq \abs{\lambda_2} \geq \dots$ including multiplicity such that we have pairwise orthonormal eigenvectors $\{u_k\}$ for $\lambda_k$ satisfying $$ \abs{\lambda_j} = \sup_{\norm{u} = 1, u\perp u_i \forall i < j} \abs{\braket{u | Tu}}. $$ 

 At last: 
 
> [!theorem] Spectral Theorem
 Suppose $\HH$ is separable. If $\abs{\lambda_1} \geq \abs{\lambda_2}\geq \dots$ are the nonzero eigenvalues of $T$ counted with multiplicity and with corresponding orthonormal eigenvectors $\{u_k\}$, then $\{u_k\}_k$ is an orthonormal basis for $\overline{T(\HH)}$. This basis can be completed by an orthonormal basis $\{f_j\}$ of $\ker T$ such that $\{u_k\}\cup \{f_j\}$ forms an orthonormal basis for $\HH$.

See [[Direct Proof of Spectral Theorem]]