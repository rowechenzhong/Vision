You know what a spanning tree is. A ==**uniform spanning tree**== is a ST which is chosen uniformly at random from the set of STs.

Observe that there is some constant $c$ such that for some family of graphs e.g. grids on $\sqrt{n}\times \sqrt{n}$ vertices, the number of STs scales as $c^n$.

Anyways, how does one generate a UST quickly?

**Wilson's algorithm:** Iteratively begin at some vertex (chosen arbitrarily; any choice works). Traverse at random, deleting any loop when it is created. When this path reaches part of the tree which has already been generated, it is locked and becomes part of the tree again.

This is called a ==**loop-erased random walk**== (LERW).

Wilson's algorithm can be rewritten as a card-popping algorithm; essentially if place a sequence of possible out-connections at every vertex and pop off the top, you will obtain a randomly sampled tree. This is pretty strong, I'll write the proof down later but it's very cool.

Now, consider such a randomly generated UST, pick a vertex in the center, and consider its path to the edge of the square (the edges of the square are all identified as a single vertex). The trajectory agrees in law with the LERW.