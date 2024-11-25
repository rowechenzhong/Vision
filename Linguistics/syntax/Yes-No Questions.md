Consider the following two sentences:

1. Those guys should leave.
2. Should those guys leave?

The first sentence is a statement, while the second sentence is a question.

The tree diagram for the first sentence is:

```mermaid
graph TD
those_guys_should_leave[TP] --> those_guys[NP];
those_guys --> det_those[Det];
det_those --> those;
those_guys --> n_guys[N];
n_guys --> guys;
those_guys_should_leave --> tense_should_leave[T'];
tense_should_leave --> t_should[T];
t_should --> should;
tense_should_leave --> vp_should_leave[VP];
vp_should_leave --> v_should_leave[V];
v_should_leave --> leave;
```

We make two claims about this tree: there is a hidden external CP shell wrapping the entire tree, whose C position encodes that the sentence is a statement, possessing a -Q feature (non-question).

```mermaid
graph TD
cp_shell[CP] --> C;
C --> -Q;
cp_shell --> those_guys_should_leave[TP];
those_guys_should_leave --> those_guys[NP];
those_guys --> det_those[Det];
det_those --> those;
those_guys --> n_guys[N];
n_guys --> guys;
those_guys_should_leave --> tense_should_leave[T'];
tense_should_leave --> t_should[T];
t_should --> should;
tense_should_leave --> vp_should_leave[VP];
vp_should_leave --> v_should_leave[V];
v_should_leave --> leave;
```

To transform this into a question, we turn the -Q feature into a +Q feature.

```mermaid
graph TD
cp_shell[CP] --> C;
C --> +Q;
cp_shell --> those_guys_should_leave[TP];
those_guys_should_leave --> those_guys[NP];
those_guys --> det_those[Det];
det_those --> those;
those_guys --> n_guys[N];
n_guys --> guys;
those_guys_should_leave --> tense_should_leave[T'];
tense_should_leave --> t_should[T];
t_should --> should;
tense_should_leave --> vp_should_leave[VP];
vp_should_leave --> v_should_leave[V];
v_should_leave --> leave;
```

The problem is, +Q and -Q currently are indistinguishable. To solve this, we introduce the ==**move operation**==, which claims that the internal T element of the TP should move to the external C position.

```mermaid
graph TD
cp_shell[CP] --> C;
C --> +Q;
C --> tense_should[T];
tense_should --> should;
cp_shell --> tense_those_guys_should_leave[TP];
tense_those_guys_should_leave --> those_guys[NP];
those_guys --> det_those[Det];
det_those --> those;
those_guys --> n_guys[N];
n_guys --> guys;
tense_those_guys_should_leave --> tense_should_leave[T'];
tense_should_leave --> t_should[T];
t_should --> t;
tense_should_leave --> vp_should_leave[VP];
vp_should_leave --> v_should_leave[V];
v_should_leave --> leave;
```

In the location where the "should" was, we insert a "t" element, which is a "trace" of the original T element. We can indicate the specific movement with an additional arrow:

```mermaid
graph TD
cp_shell[CP] --> C;
C --> +Q;
C --> tense_should[T];
tense_should --> should;
cp_shell --> tense_those_guys_should_leave[TP];
tense_those_guys_should_leave --> those_guys[NP];
those_guys --> det_those[Det];
det_those --> those;
those_guys --> n_guys[N];
n_guys --> guys;
tense_those_guys_should_leave --> tense_should_leave[T'];
tense_should_leave --> t_should[T];
t_should --> t;
tense_should_leave --> vp_should_leave[VP];
vp_should_leave --> v_should_leave[V];
v_should_leave --> leave;
t --> should;
```