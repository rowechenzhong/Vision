Note that if $L$ is nilpotent, then clearly all $x\in L$ are ==**ad-nilpotent**== (that is, $(\ad x)^n = 0$ for all $x$).

The strong claim is that the converse is true:

>[!theorem] Engel
>If all elements of $L$ are ad-nilpotent, then $L$ is nilpotent.

Well, $\ad L \subset \gl(L)$ consists of nilpotent endomorphisms, thus by the [[Nilpotent Representation Lemma]], there exists $x\in L$ such that $[Lx] = 0$. This means $Z(L) \neq 0$. $L / Z(L)$ consists of ad-nilpotent elements (of course) and has smaller dimension than $L$. Thus we can repeat this until eventually $L/Z(L) = 0$ which is nilpotent. Going back up, $L$ is nilpotent.