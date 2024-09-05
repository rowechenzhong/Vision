Let $F\subset\CC$ contain $\zeta = e^{2\pi i / p}$. A ==**Kummer Extension**== is a Galois extension $K/F$ of degree $p$; the Galois group is of course $\ZZ/p$.

>[!theorem]
>There exists some $\beta \in K$ such that $\beta^p\in F$ and $K = F[\beta]$.

The content is that there exists any $\beta\in K\setminus F$ such that $\beta^p \in F$, because by Galois correspondence there are no proper intermediate fields.

By JCF (over $\CC$, but if you repeat the proof you get that you can do this on $K$!) we observe that $\sigma\in \End_F K$ is diagonalizable, hence its eigenvalues are of the form $\zeta^k$. It isn't the identity, hence it has a nontrivial eigenvector $\beta$ which is not in $F$. Then, $\sigma(\beta) = \zeta\beta$, thus $\sigma(\beta^p) = \beta^p\in F$ gg.


>[!idea]- Figuring it out.
>>[!idea]
>>Does a Galois representation theory exist?
>
> This is really cool, because it uses the "field extensions are vector spaces" idea for real. There are two salient operators on this space: some primitive $\alpha$ and the generator of the cyclic Galois group $\sigma$. Any eigenvector of this operator must have eigenvalue $\zeta^k$. Using $\sigma$, we can feel free to change basis from whatever naive $(1,\alpha,\dots, \alpha^{p-1})$ basis we use to perform the embedding, because $\ker (\sigma - 1)$ is exactly $F$. Cool.
> 
>>[!idea]- Waffles about what $\alpha$ looks like.
>>By say, Jordan canonical form, we note that $\alpha$ is actually diagonalizable (over $K$, rip) with eigenvalues exactly $\alpha_i$. Sure, whatever; I can represent this in whatever basis I want I guess; I can consider like a $F$-subalgebra of $K\otimes_F \End_F(K)$. Uh okay let's be way more explicit.
>> $$
>> \rho(\alpha) = \begin{pmatrix}
>> 0 & 0 & 0 & \dots & -a_0\\
>> 1 & 0 & 0 & \dots & -a_1\\
>> 0 & 1 & 0 & \dots & -a_2\\
>> \vdots & \vdots & \vdots & \ddots & \vdots\\
>> 0 & 0 & 0 & \dots & -a_{p-1}
>> \end{pmatrix},\qquad \sum_{i = 0}^p a_i \alpha^i = 0
>> $$
>> 
>> This has eigenvalues $\alpha_i$, but I can't see the eigenvectors immediately. Think. Fields are commutative, does it help to transpose?
>> $$
>> \rho^\top(\alpha) = \begin{pmatrix}
>> 0 & 1 & 0 & \dots & 0\\
>> 0 & 0 & 1 & \dots & 0\\
>> 0 & 0 & 0 & \dots & 0\\
>> \vdots & \vdots & \vdots & \ddots & \vdots\\
>> -a_0 & -a_1 & -a_2 & \dots & -a_{p-1}
>> \end{pmatrix}
>> $$
>> Then it's like, $\left(1, \alpha,\dots, \alpha^{p-2}, \alpha^{p-1}\right)^\top$ gets mapped to $(\alpha,\alpha^2,\dots, \alpha^p)^\top$ as desired lol. Okay, this is how you diagonalize it over $K$ and it works for any $\alpha_i$.
>> 
>> Fine! In this basis my guy just looks like $\diag(\alpha_1,\alpha_2,\dots)$. $\sigma$ looks like some garbage (but it already looked like garbage), and has eigenvalues $\zeta^k$. Pause.
> 
> $\sigma$ is cyclic thus must send $\alpha_1\to \alpha_2\to \dots \to \alpha_p\to \alpha_1$, awesome, so its eigenvalues are exactly $\{\zeta^k\}$ (this is actually wrong!! it is possible that the $\alpha_i$ are not linearly $F$-independent). Then, pick some nonzero $k$, and consider the $\zeta^k$-eigenvector $\sum_i \zeta^{-ik} \alpha_i$. This guy is not an element of $F$, lol. $\sigma$ sends your $\beta = \sum_i \zeta^{-i}\alpha_i$ to $\zeta \beta$, but that already wins because $\sigma(\beta^p) = \zeta^p \beta^p = \beta^p$ by the field property.
> 
>>[!idea]- Bash confirmation
>But its $p$-th power is...? Do I agree with this nonsense LOL. $\sum_{\text{tuple}} \zeta^{-k\sum} \alpha_{i_1}\dots \alpha_{i_p}$. Oh, I might agree with this? Gets sent to $\sum_{\text{tuple}} \zeta^{-k \sum} \alpha_{i_1 + 1}\dots \alpha_{i_p + 1}$... which is yeah the same thing XD okay what a legend.
> 
>