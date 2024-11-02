A ==**compact class**== is a family $C\subset 2^X$ such that all sequences in $C$ with the finite intersection property have a nonempty intersection. 

>[!idea] Contrapositive
>Every $C_1\cap C_2\cap\dots = \emptyset$ implies $\exists N < \infty$ with $C_1\cap\dots\cap C_N = \emptyset$.

The salient example, given that we will usually be working over [[Borel Measure|borel $\sigma$-algebras]] (and [[Compact Class Bootstrap]] will yield [[inner regular]] measures).

> [!example]- Compact sets in a Hausdorff Topological Space form a Compact Class
> We use the contrapositive. Let $D_i = C_1\cap\dots \cap C_i$ (these are closed sets) and $U_i = X\setminus D_i$. Then the $U_i$ form an open cover of $X$, and in particular $C_1$. Thus there is some finite subcover, which yields an $N$ such that $X\setminus D_N\supset C_1$ i.e. $D_N = \emptyset$.