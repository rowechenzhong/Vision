---
aliases:
  - Dynkin's Theorem
---
> [!definition] Pi system
> A ==**pi system**== on $\Omega$ is a collection of subsets that is closed under finite intersections.

^5c9b44

> [!definition] Lambda system
> A ==**lambda system**== on $\Omega$ is a collection of subsets such that:
>
> 1. $\Omega \in \Lambda$.
> 2. If $A,B \in \Lambda$ and $A \subseteq B$, then $B \setminus A \in \Lambda$.
> 3. If $A_1, A_2, \dots \in \Lambda$ and $A_i \uparrow A$, then $A \in \Lambda$.
>    
>    (This is sometimes called a ==**d-system**==).

The main idea is that these two definitions neatly partition the definition of a $\sigma$-algebra:

> [!theorem] $\pi + \lambda = \sigma$
>
> $\LL$ is a $\sigma$-algebra iff it is both a $\pi$-system and a $\lambda$-system.

> [!proof]
> First off, all $\sigma$-algebras are clearly $\pi$ systems, and satisfy the first two properties of $\lambda$-systems. The third property is simply a special case of countable unions.
>
> If you are a $\lambda$ system, then you have $\Omega$. Thus by the second condition you have complements. If you also a $\pi$ system, then finite intersections give you finite unions. Finally, given any collection $A_1, A_2,\cdots \in \LL$, their prefix unions $A_1\cup \cdots A_n$ are all in $\LL$, and thus by the third condition of $\lambda$-systems, their union is also in $\LL$.

> [!theorem] Dynkin's $\pi$-$\lambda$ Theorem
> Let $\mathcal{P}$ be a $\pi$-system, and $\LL$ be a $\lambda$-system. If $\mathcal{P} \subseteq \LL$, then $\sigma(\mathcal{P}) \subseteq \LL$.

> [!proof]-
>
> > [!claim]
> > The intersection of two $\lambda$-systems is a $\lambda$-system:
> >
> > 1. $\Omega$ lies in both.
> > 2. If $A \subset B$ lie in both, then $B\setminus A$ lies in both.
> > 3. If $A_1, A_2, \dots$ lie in both, then $A_1 \cup A_2 \cup \dots$ lie in both.
> 
> To prove the theorem, let $\LL$ be the smallest $\lambda$-system containing $\mathcal{P}$, which can be obtained as the intersection of all $\lambda$-systems containing $\mathcal{P}$ (via Zorn's Lemma for instance). We will show that $\LL$ is a $\pi$-system, as this would show it is a $\sigma$-field.
>
> The trick is to let
> $$
>   \LL' = \{ B\in \LL | A\cap B \in \LL \text{ for all $A\in \mathcal{P}$}\}
> $$
> It is clear that $\LL'$ is a $\lambda$-algebra. It is also clear that $\LL\subset \mathcal{P}$. Thus $\LL' = \LL$! Then, let
> $$
>   \LL'' = \{ B\in \LL | A\cap B \in \LL \text{ for all $A\in \LL$}\}
> $$
> Then, $\mathcal{P}\subset \LL''$ because $\LL = \LL'$. Thus $\LL'' = \LL$ as desired.

> [!idea]
> Measure-theoretic proofs are difficult because we don’t have a closed form for all measurable subsets. Instead, we must first verify that a certain subset $\mathcal{P}$ has a property $\LL$ that we want. Then, Dynkin booststraps the results from $\mathcal{P}$ to its $\sigma$-algebra.

A related theorem: [[Monotone Class Theorem]] (for sets).