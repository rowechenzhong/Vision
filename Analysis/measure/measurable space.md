---
aliases:
  - sigma algebra
---
> [!definition] Measurable Space and $\sigma$-algebra
> A ==**measurable space**== is a set $\Omega$ together with a non-empty collection $\AAA$ of subsets of $\Omega$.
> 
>$\AAA$ is a ==**$\sigma$-algebra**==, and the elements of $\AAA$ are called ==**measurable sets**==. The set $\AAA$ is required to be closed under complements and *countable* unions. If we replace \"countable\" with \"finite,\" we get an ==**algebra**== instead. 
>People sometimes also use the word "field" instead of "algebra."
>^algebra

> [!problem] Countable Intersections
 Show that $\sigma$-algebras are closed under countable intersections, and contain $\Omega$ and $\emptyset$. 
 
> [!solution]- 
 Let $\Omega$ be a set, and $\AAA$ a $\sigma$-algebra of subsets of $\Omega$. Let $A_1, A_2, \dots \in \AAA$. Then, $\conj{A}_1, \conj{A}_2, \dots \in \AAA$, so $\bigcup \conj{A}_i \in \AAA$. Thus, $\conj{\bigcup \conj{A}_i} \in \AAA$, so $\bigcap A_i \in \AAA$. Since $\AAA$ is closed under countable unions, $\emptyset = \bigcup_{A\in \emptyset} \in \AAA$. (Alternatively, use the nonempty condition.) Since $\AAA$ is closed under complements, $\Omega = \conj{\emptyset} \in \AAA$. 

 It is quite hard to write down measurable sets explicitly, so for any set $\Omega$ and family of subsets $\FFF$, the ==**$\sigma$-algebra generated by $\FFF$**== is the smallest $\sigma$-algebra containing $\FFF$. 
 
> [!idea]- Details
Specifically, take the intersection of all $\sigma$-algebras containing $\FFF$; this is guaranteed to be a $\sigma$-algebra containing $\FFF$.
To prove that $\mathcal{A}$ is a $\sigma$-algebra, we need to show three things:
>1. $\Omega \in \mathcal{A}$: Since each of the $\sigma$-algebras containing $\FFF$ must contain the sample space $\Omega$, it follows that the intersection of all such $\sigma$-algebras also contains $\Omega$. Therefore, $\Omega \in \mathcal{A}$.
>2. If $A \in \mathcal{A}$, then $A^c \in \mathcal{A}$: Let $A \in \mathcal{A}$. This means that $A$ is in every $\sigma$-algebra containing $\FFF$. Since each of these $\sigma$-algebras also contains the complements of their elements, it follows that $A^c$ is in every such $\sigma$-algebra. Therefore, $A^c \in \mathcal{A}$.
>3. If $A_1, A_2, A_3, ... \in \mathcal{A}$, then their union $B = A_1\cup A_2\cup A_3\cup ...  \in \mathcal{A}$: Let $B = A_1\cup A_2\cup A_3\cup ...$ . For each $i$, we know that $B$ must be in every $\sigma$-algebra containing $\FFF$, and since each of these algebras are closed under countable unions, it follows that $B \in \mathcal{A}$.
>
>Therefore, we have shown that $\mathcal{A}$ is a $\sigma$-algebra.
>
>To show that $\mathcal{A}$ contains $\FFF$, note that each of the $\sigma$-algebras containing $\FFF$ must contain all the sets in $\FFF$. Therefore, the intersection of all such $\sigma$-algebras will also contain all the sets in $\FFF$. Hence, $\mathcal{A}$ contains $\FFF$.

 The most important $\sigma$-algebra is the ==**Borel $\sigma$-algebra**==. If $\Omega$ is a topological space, then the Borel $\sigma$-algebra $\BBB(\Omega)$ is the $\sigma$-algebra generated by the open sets of $\Omega$.