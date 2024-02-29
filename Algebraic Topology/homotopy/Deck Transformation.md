---
aliases:
  - Covering group
  - covering group
---
> [!definition] Deck Transformation
A ==**deck transformation**== is a homeomorphism $\phi: \tilde{X}\to \tilde{X}$ such that $p\circ \phi = p$. 

These are automorphisms (in the covering space sense) from $\tilde{X}$ to itself. The word "deck" is pretty good; I visualize $\tilde{X}$ as a deck of cards, and $\phi$ as a shuffling of the deck. Look at the pancake picture; its a permutation on every fiber. The set of all deck transformations is a group denoted $G(\tilde{X})$, and is sometimes called the ==**covering group**==. As is thematic, we observe that such deck transformations encode discrete information in their action on fibers.

In fact, a deck transformation is precisely a **lift of the covering map**, and these maps behave really well:
-  For ==*pc spaces*==, by the [[unique lifting]] property, a deck transformation $\phi$ is uniquely determined by where it sends a single point. For instance, $\phi$ has a fixed point iff it is the identity. 

-  Let $\{\tilde{x}_0, \tilde{x}_1\} \in p^{-1}(x)$. For ==*pc lpc spaces*==, by the [[lifting criterion]], a deck transformation sending $\tilde{x}_0$ to $\tilde{x}_1$ exists if and only if $$ p_*(\pi_1(\tilde{X}, \tilde{x}_0)) = p_*(\pi_1(\tilde{X}, \tilde{x}_1)).$$ This [[Regular Covering Spaces|normally]] works (pun intended).