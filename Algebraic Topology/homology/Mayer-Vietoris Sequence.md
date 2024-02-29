This is the main computational tool in homology theory.

>[!theorem] Mayer-Vietoris Sequence
>Let $A,B\subset X$ be subsets such that
>$$\mathring{A} \cap \mathring{B} = X.$$
>Then, there is a long exact sequence
>![[Mayer-Vietoris.png]]

# Intuition

The map $H_n(A)\oplus H_n(B)\to H_n(X)$ is the sum of the maps induce by the inclusions $i:A\hookrightarrow X$ and $j: B\hookrightarrow X$, i.e. $$(x,y)\to i_*(x) + j_*(y).$$In words, take your holes and add them. It's not deep.

The map $H_n(A\cap B)\to H_n(A)\oplus H_n(B)$ is the **difference** between the maps induced by inclusions $k:A\cap B\hookrightarrow A$ and $\ell:A\cap B\hookrightarrow B$, i.e.
$$z\mapsto k_*(z), -\ell_*(z).$$This uh, takes your holes, and uh, places one copy in $A$ and a negative copy in $B$. Still not too deep. Note that this composes with the previous to $0$.

The third map, $\pa: H_n(X)\to H_{n-1}(A\cap B)$, is the $\pa$ operator we know and love, except that there's a slight technicality. Naively, $\pa H_n(X)$ maps straight into $H_{n-1}(X)$! It is certainly true that there are simplices in $H_n(X)$ that do not lie in $A\cap B$. The claim is that we don't care about any of those; this will be elaborated upon in the proof. Lol.