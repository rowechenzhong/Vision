> [!definition] Simple Functions
> A function $f: \Omega \to \RR$ is ==**simple**== if it can be written
> $$ f = \sum_{i=1}^n c_i \id_{A_i} $$
> where $c_i \in \RR$ and $A_i$ are disjoint *measurable sets*.

Simple functions are obviously [[real-valued measurable functions]].

> [!problem] Verification
> Simple functions are closed under addition, products, and scalar multiplication.

> [!solution]-
> Let $f = \sum_{i=1}^n c_i \id_{A_i}$ and $g = \sum_{j=1}^m d_j \id_{B_j}$ be simple functions.
>
> - $$f+g = \sum_{i=1}^n \sum_{j=1}^m (c_i + d_j) \id_{A_i \cap B_j}.$$
> - $$fg = \sum_{i=1}^n \sum_{j=1}^m c_i d_j \id_{A_i \cap B_j}.$$
> - $$cf = \sum_{i=1}^n c c_i \id_{A_i}.$$
>
> These point to a common trick: when we a set is cut up into a finite/countable number of pieces in two different ways, one simply considers the finite/countable pieces of the form $A_i \cap B_j$.