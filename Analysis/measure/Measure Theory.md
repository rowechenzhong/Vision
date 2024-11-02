This is the [[homepage|home page]] for measure theory.

# Introduction

In mathematics, the concept of a measure is a generalization and formalization of geometrical measures (length, area, volume) and other common notions, such as magnitude, mass, and probability of events. These seemingly distinct concepts have many similarities and can often be treated together in a single mathematical context.

Let's try to motivate measures with some simple examples from probability.

> [!example] Uniform Distribution
> Let $X$ be a random variable ``uniformly distributed" on the interval $[0,1]$. Then, for instance, we might say that the probability that $X$ takes on a value in the interval $[a,b]$ is $b-a$.

> [!example] Dice Roll
> Let $X$ be a random variable representing the outcome of a roll of a fair six-sided die. Then, for instance, we might say that the probability that $X = 3$ is $1/6$, and the probability that $X\in \{1,2,3\}$ is $1/2$. This is easily generalized to the "counting measure" on any finite set.

Both of these examples are instances of a more general concept: a measure. You will immediately notice that there are two essential components to a measure:

-   A set of objects, $S$. In the uniform distribution example, the objects are the real numbers in $[0,1]$, and in the dice roll example, the objects are the integers $\{1,2,3,4,5,6\}$.
-   A function $\mu$ that assigns a "size" to _subsets_ of $S$. In the uniform distribution example, the size of $[a,b]\subset S$ is $\mu([a,b]) = b-a$. In the dice roll example a is its length, and in the dice roll example, the size of an object is its probability.

There is a much less obvious third component to measures. It turns out that for $S$ that are larger than a finite set, [[vitali|it is impossible]] to assign a measure to _all_ subsets of $S$ without violating some basic assumptions about how measures should behave. However, one very rarely needs to be able to measure all sets; it is usually sufficient to be able to measure a large collection of so-called "measurable" sets.

# Main Sequence

If you would like, you can check out an [[measure prologue|extended prologue]].

First, the formal definition of a measure space.

1. [[measurable space]]
2. [[measure space]]

Next, we will _construct_ the most important measure spaces, starting with the real numbers.

3. [[Lebesgue Measure]] (More advanced alternative: [[Compact Class Bootstrap]])
4. [[Caratheodory Extension Theorem]]
5. [[More examples of measures]]

From here, one can study integration over measures, which is a large subject.

6. [[Integration]]

There is also more to be discussed in "point-set measure theory"

7.  [[box product measure]]
8.  [[product measure]]