Today I decided to write a brief set of notes on information theory. I want it to be a bigger note that most of the other pages, like a latex pdf handout. 

Where to begin -- 
# Entropy

Attempt to solve the following problem before moving on.

>[!problem] Game 1
>Alice and Bob play the following game.
>1. It is publicly known that there is a weighted coin landing heads $\frac23$ of the time, and tails $\frac13$ of the time. There is a publicly known positive integer $n$.
>2. She secretly records $n$ i.i.d. samples from the coin, which Bob cannot see.
>3. She may send Bob a message, which is a sequence of bits of finite length.
>4. Then, Bob is required to report what Alice's samples were!
>
>Alice and Bob can strategize beforehand. Alice and Bob lose the game outright if Bob does not report Alice's sample correctly; the strategy must work with probability one. Their score is otherwise the number of bits that Alice communicated to Bob; Alice and Bob attempt to *minimize* the expected value of this score!
>
>Solve this game asymptotically. Specifically, demonstrate that there exists a constant $H$ such that:
>1. For any $H' > H$, there exists some $n_0$ such that for all $n \geq n_0$, there exists a strategy with expected score $\leq H'n$.
>2. For any $H' < H$, there exists some $n_0$ such that for all $n \geq n_0$, there exists no strategy with expected score $\leq H'n$.


>[!hint]-
>Suppose instead of the coin, it is a dice with $d = 2^k$ sides. Solve the same problem; $H = k$.
>
>Then solve the problem for arbitrary $d$. $H = \log_2 d$.

>[!hint]-
>$H = -\frac13 \log_2 \frac13 - \frac23 \log_2 \frac23$. The construction is much easier than the impossibility proof.

We will solve the problem in the following generality:

>[!theorem] Entropy
>Alice and Bob play the following game.
>1. Alice and Bob are publicly told a probability distribution $p$ over $[N]$ (where $[N] = \{1,\dots, N\}$ is a finite set) and a finite integer $n$.
>2. Alice secretly receives $n$ i.i.d. samples from $p$, which Bob cannot see.
>3. She may send Bob a message, which is a sequence of bits of finite length.
>4. Then, Bob is required to report what Alice's samples were!
>
>Alice and Bob can strategize beforehand, where $p, N, n$ are known. Alice and Bob lose the game outright if Bob does not report Alice's sample correctly; the strategy must work with probability one. Their score is otherwise the number of bits that Alice communicated to Bob; Alice and Bob attempt to *minimize* the expected value of this score!
>
>There exists a constant $H(p)$ such that:
>1. For all $H' > H(p)$, there exists some $n_0$ such that for all $n \geq n_0$, there exists a strategy with expected score $\leq H'n$.
>2. For any $H' < H(p)$, there exists some $n_0$ such that for all $n \geq n_0$, there exists no strategy with expected score $\leq H'n$.
>   
> $H(p) = -\sum_{i = 1}^N p(i)\log_2 p(i)$, and is called the ==**entropy**== of $p$.

First, let $H = H(p)$ for brevity. For any $\eps > 0$, we exhibit a strategy which achieves a score of $nH(1 + 3\eps)$.

Define the ==**surprisal**== of a sequence $x^n = (x_1,\dots, x_n)$ as $\sigma(x^n) = -\log p(x^n) = -\sum_{i\leq n} \log p(x_i)$. There are two key ideas:
1. Almost all sequences have surprisal in $\leq n(H+ \eps)$. Indeed, this surprisal is a sum of i.i.d. random variables, hence we expect concentration in $nH(p)\pm \Theta(\sqrt{n})$.
2. We can get away with ignoring everything but these ==**typical**== sequences.

To formalize the first idea, simply note that by *Hoeffding's inequality*, there exists some constant $C(p)$ such that $\PP_{x_i\sim p}(\sigma(x^n) - H(p) \geq \eps n) \leq \exp\left( - C(p) n \eps^2\right)$. 

To complete the construction, we *enumerate* all typical sequences. As the probability of any such sequence is at least $2^{-(H + \eps)n}$, there are at most $2^{(H + \eps)n}$ such sequences, which we can order arbitrarily. Hence, we can ==**encode**== these sequences in the following manner:
1. Send a single $0$ to indicate that we are sending a ==**typical**== sequence.
2. Send $\ceil{(H + \eps)n}$-length bitstring which is the index of the typical sequence.

This successfully encodes the *vast majority* of messages in $(H + \eps)n + 2$ bits! We send each of the remaining messages in this brutal way:
1. Send a single $1$ to indicate that we are sending an atypical sequence.
2. There are $N^n$ messages *total*, including typical sequences. Hence we can send a length-$\ceil{n\log_2 N}$ message which reports the index of the message.

In expectation, we send at most $(H + \eps)n + 2 + \exp\left(-C(p) n\eps^2\right)(n\log_2 N + 1)$ bits. Set $n_0$ sufficiently large such that $\exp\left(-C(p) n_0\eps^2\right) < \frac1{\log_2 N} \eps$, yielding an upper bound of $(H + 2\eps)n + 3$. We conclude.

>[!idea]
>The main technique used here is called the ==**Asymptotic Equipartition Principle**==.
>It's a nontrivial leap to consider applying the CLT to *statistical properties of realizations* as in the definition of a typical sequence.

Conversely, we will use much the same ideas to demonstrate that no strategy can achieve an expected asymptotic score of $(H - 2\eps)n$ with $\eps > 0$.

The key idea is once again the AEP. Roughly:
- Considering *only* typical sequences, there are still $2^{(H - \eps)n}$ sequences, each of which has small probability.
- By pigeonhole, we require around $(H - \eps)n$ bits to send just these sequences!

Call a sequence ==**typical**== if it has surprise at least $n(H - \eps)$. By Hoeffding once more, there exists some constant $C(p)$ such that $\PP_{x_i\sim p}(\sigma(x^n) - H(p) \leq - \eps n) \leq \exp\left( - C(p) n \eps^2\right) = \delta(n)$. Hence, are at least $\left(1 - \delta(n)\right)2^{(H - \eps)n}$ such typical sequences. Increase $n$ such that there are at least $2^{(H - \eps)n - 1}$ typical sequences.

The probability that Alice's encoding scheme sends at most $d$ bits, conditioned on receiving a typical sequence, is at most $2^{d + 1 - (H - \eps)n}$, as this can only be reliably done for $2^{d+1} - 1$ distinct messages. Hence, the expected score conditioned on receiving a typical sequence is at least$$
\EE[\text{score}] = \sum_{d = 0}^{(H - \eps)n} \PP\left(\text{score} > d\right)\geq \sum_{d = 0}^{(H - \eps)n} 1 - 2^{d + 1 - (H - \eps)n}\geq (H - \eps)n - 2
$$Now, if your expected score is $(H- 2\eps)n$, then your expected score conditioned on receiving a typical sequence must be at most $\frac{H - 2\eps}{1 - \delta(n)}n$. Increase $n$ such that this is at most $(H - 2\eps)n + 1$, and we see that this is incompatible with the bound!

# Entropy II

Continuing, the thesis is to convince you that entropy and surprisal are real (as in, tangible and important, non-arbitrary), extrinsic (in the physicist's sense; roughly, additive) quantities associated with probability distributions.

>[!problem] Game 2
>Alice and Bob play the following game.
>1. It is publicly known that there is a fair coin. There is a publicly known positive integer $n$.
>2. She secretly records $n$ i.i.d. samples from the coin, which Bob cannot see.
>3. She may send Bob a message, which is a sequence of characters in $\{A, B, C\}$.
>4. Then, Bob is required to report what Alice's samples were!
>
>The game is the same, except for scoring. Suppose $a, b, c$ usages of $A, B, C$ occurred. The score is $a + 2b + 2c$.
>
>There exists a value of $S$ such that the asymptotically optimal score is $(S + o(1))n$. Find $S$.

>[!hint]- Big hint
>Imagine that $A, B, C$ are exactly the strings "0", "10", and "11".

>[!theorem]
>Alice and Bob play the following game.
>1. Alice and Bob are publicly told a probability distribution $p$ over $[N]$, a probability distribution $q$ over $[M]$, and an integer $n$.
>3. Alice secretly receives $n$ i.i.d. samples from $p$, which Bob cannot see.
>4. She may send Bob a message, which is a sequence of elements of $[M]$ of finite length.
>5. Then, Bob is required to report what Alice's samples were!
>
>The score is $\sum_{i\in [M]} -\log q(i) m_i$, where there are $m_i$ usages of $i$; this is exactly the surprise of the message sent under $[M]$.
>
>The asymptotically optimal expected score is $\left(H(p) + o(1)\right)n$.

This tells us that all probability distributions are perfect substitutes (in the economics sense) at encoding information, with numeraire the entropy.

> [!claim]
> The above theorem holds when $p$ is restricted to be uniform over $[N]$.

[!proof] Proof of Claim
One can guess the key idea this time around:
- By the AEP, for all $d$, there are roughly $2^{dH(q)}$ messages of length $d$ we can send which each have surprise roughly $dH(q)$.
- This actually suffices; we can elect to *only* use such messages. It's *incredibly* powerful that $1 - \exp(\dots)$ of the messages have equal surprise.

Details are omitted.

Conversely, suppose there exists $\eps$ such that we can send a uniformly random integer $1\dots N^n$ with $(1 - \eps)n\log_2 N$ surprise in expectation for sufficiently large $n$.


To prove the main theorem, we chain the claim together with our previous theorem!
