Sentences introduce a new variable to our CFL: tense categories (T, T') and "Tense Phrases" (TP) which are entire sentences. TP's are also called ==**sentential phrases**== or ==**clauses**==.

```mermaid
graph TD;
%% "The hikers found the shortcut"
the_hikers_found_the_shortcut[TP] --> the_hikers[NP];
the_hikers --> det_the[Det];
det_the --> the;
the_hikers --> n_hikers[N'];
n_hikers --> hikers;
the_hikers_found_the_shortcut --> tense_found_the_shortcut[T'];
tense_found_the_shortcut --> past_tense[+Pst];
tense_found_the_shortcut --> vp_found_the_shortcut[VP];
vp_found_the_shortcut --> v_found_the_shortcut[V];
v_found_the_shortcut --> found;
vp_found_the_shortcut --> np_the_shortcut[NP];
np_the_shortcut --> det_the_2[Det];
det_the_2 --> the_2[the];
np_the_shortcut --> n_shortcut[N'];
n_shortcut --> shortcut;
```

A ==**modal auxilliary**== (historically, "auxilliary verbs") such as "can", "could", "may", "might", "must", "shall", "should", "will", "would" have T inherent tense, and hence are T's.

```mermaid
graph TD;
%% "The hikers will find the shortcut"
the_hikers_will_find_the_shortcut[TP] --> the_hikers[NP];
the_hikers --> det_the[Det];
det_the --> the;
the_hikers --> n_hikers[N'];
n_hikers --> hikers;
the_hikers_will_find_the_shortcut --> tense_will_find_the_shortcut[T'];
tense_will_find_the_shortcut --> future_tense[will];
tense_will_find_the_shortcut --> vp_find_the_shortcut[VP];
vp_find_the_shortcut --> v_find_the_shortcut[V];
v_find_the_shortcut --> find;
vp_find_the_shortcut --> np_the_shortcut[NP];
np_the_shortcut --> det_the_2[Det];
det_the_2 --> the_2[the];
np_the_shortcut --> n_shortcut[N'];
n_shortcut --> shortcut;
```
