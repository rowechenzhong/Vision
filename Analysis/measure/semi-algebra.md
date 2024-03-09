A ==**semi-algebra**== $S\subset 2^\Omega$, in the context of [[Measure Theory]], is a set of subsets
1. Containing $\emptyset$.
2. which is a [[pi lambda system#^5c9b44|Pi system]]; it is closed under finite intersection.
3. **Semiclosed under complementation:** if $E\in S$, then $\Omega \setminus E$ is a finite **disjoint** union of elements of $S$.

>[!idea]
>It is not equivalent to replace condition (3) with the statement "if $E\in S$, then $\Omega \ E$ is a finit union of elements of $S$."
>>[!idea]- Copied from https://math.stackexchange.com/a/719191/1200236:
>> Let $X$ be the nodes of an infinite complete binary tree. Then for $x\in X$, let $L(x)$ denote all nodes in the left subtree from $x$, and similarly let $R(x)$ denote all nodes in the right subtree from $x$. Then let$$S = \{\{x\}| x\in X\} \cup \{\{x\}\cup L(x)| x\in X\} \cup \{\{x\}\cup R(x)| x\in X\} \cup \{\{\} \}$$In other words, $S$ is comprised of all singletons, all singletons with their left subtrees, and all singletons with their right subtrees. One can check that this is a semi-algebra in the sense of 1,2,and 3. But we will never be able to write $X$ (the complement of the empty set) as a finite disjoint union of elements of $S$.


> [!example] Half-open intervals
> The collection of intervals $[a,b)$ (and $(a,\infty)$) is a semialgebra.