>[!idea]
> WOAH I did not realize that Obsidian had native support for Mermaid diagrams! ...I might have to do all my Syntax homework in Obsidian from now on.

Here is the ==**X' Schema**==:

```mermaid
graph TD;
id1[XP] --> id2[Specifier];
id1 --> id3[X'];
id3 --> id4[X];
id3 --> id5[Complement];
id4 --> id6[Head];
```

The ==**Head**== is the (required) nucleus of the phrase, in $\{N, V, A, P\}$. If the type of the head is a noun (N), then the diagram might look like this:

```mermaid
graph TD;
id1[NP] --> id2[Specifier];
id1 --> id3[N'];
id3 --> id4[N];
id3 --> id5[Complement];
id4 --> id6[Head];
```
Here, "NP" means "Noun Phrase."

The ==**Specifier**== always occurs at the edge of a phrase, and is (optional for now). In English, it is always at the beginning of the phrase.
- For Nouns, the specifier is either a determiner (e.g. "the", "a", "this", "that", "some", "any") or a possessive (see below).
- For Verbs, the specifier is almost always a (preverbal) adverb (e.g. "quickly", "happily", "very", "too", "again").
- For Adjectives or Prepositions, the specifier is a degree word (e.g. "very", "too", "extremely", "quite").

The ==**Complement**== is an (optional for now) phrase providing information about entities or locations implied by the meaning of the head.

Finally, if the Specifer or Complement are omitted, then we can compress the tree structure.

Hence, here are some examples of valid trees:

```mermaid
graph TD;
%% "a cat"
id1[NP] --> id2[Det];
id2 --> id3[a];
id1 --> id4[N];
id4 --> id5[cat];

%% "a cat with a hat"
id6[NP] --> id7[Det];
id7 --> id8[a];
id6 --> id9[N'];
id9 --> id10[N];
id10 --> id11[cat];
id9 --> id12[PP];
id12 --> id13[P];
id13 --> id14[with];
id12 --> id15[NP];
id15 --> id16[Det];
id16 --> id17[a];
id15 --> id18[N];
id18 --> id19[hat];

%% "eat candy"
id20[VP] --> id21[V];
id21 --> id22[eat];
id20 --> id23[NP];
id23 --> id24[N];
id24 --> id25[candy];
```

Some more cases:
- We treat pronouns as N's.
- We treat possessives as NP's which can fill the roll of a specifier.

```mermaid
graph TD;
%% "Mary"
id1[NP] --> id2[N];
id2 --> id3[Mary];
%% "the child's dog"
id4[NP] --> id5[NP];
id5 --> id6[Det];
id6 --> id7[the];
id5 --> id8[N];
id8 --> id9[child's];
id4 --> id10[N];
id10 --> id11[dog];
```
