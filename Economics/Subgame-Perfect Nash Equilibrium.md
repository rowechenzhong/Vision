A ==**Nash equilibrium**== is ==**subgame-perfect**== if it remains an NE when restricted to any subgame. A subgame is the subtree of the extensive game tree upon reaching a node with trivial infoset.

In a ==**multi-stage game**==, the only non-trivial infosets contain the moves that other players are making concurrently. Another way to express this idea:
1. Give me a bunch of games, $G_1, G_2,\dots, G_n$.
2. Play game $G_1$ first (in normal-form; the moves are to select strategies), then reveal all hidden information (the entire strategies selected) to all players. Then play $G_2$, etc.

This is not the most general possible way to obtain subgames; more generally, construct a rooted tree of games, where each outcome of $G$ corresponds to a child of $G$. Reveal all hidden information at the conclusion of any game, and transition to a new node.

To check whether a strategy is an SPNE of a multi-stage game, just check whether you can unilaterally improve at any stage; this is the ==**one-shot deviation principle**== and is completely trivial.