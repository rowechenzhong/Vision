Lean is all about functions and types.
```lean
variable (a: ℝ)
#check a
-- a : ℝ
```

Here, the colon means that `a` is of type `ℝ`. This is actually what the colon means in lean as well; you have to write code in a way that this type-checking is valid.

`f x` means `f(x)`. A function which outputs functions is the same thing as a two-input function, because `f x y` .

When I write
```lean
theorem abc (a b c : ℝ) : a * b * c = b * (a * c) := by
  rw [mul_comm a b]
  rw [mul_assoc b a c]
```
what happens?

Recall that `#check` checks the *type* of an object.

```lean
#check abc
-- abc (a b c : ℝ) : a * b * c = b * (a * c)

#check abc 1
-- abc 1 : ∀ (b c : ℝ), 1 * b * c = b * (1 * c)

#check abc 1 2
-- abc 1 2 : ∀ (c : ℝ), 1 * 2 * c = 2 * (1 * c)

#check abc 1 2 3
-- abc 1 2 3 : 1 * 2 * 3 = 2 * (1 * 3)
```

>[!idea]
>In lean, **a theorem is a function** mapping universally quantified inputs to a *proof* of a proposition.

So yeah, here `abc` is a function which maps any `a b c : ℝ` to an element of type `a * b * c = b * (a * c)`, that is, proofs of `a * b * c = b * (a * c)`. In order to write down this function (which isn't a variable; we're writing something that in cpp looks like `int a = 2` and we need to write the `2`...) we write `:=` and include the actual element afterwards, which in this case is an entire proof.

By the way, these things are propositions.
```lean
#check 1 = 2
-- 1 = 2 : Prop

#check ∀ x: ℝ, x = x
-- ∀ (x : ℝ), x = x : Prop
```

When I write `∀ (c : ℝ), p(c)` where `p(c)` is some proposition involving `c`, then this is actually a function which maps `c` to `p(c)`. TODO: is this true?

When I write down a variable which is a real number, I'm not writing down an actual number (which would be an element with type `ℝ`). Instead, I'm saying "let x be a real number." Not that deep.
```lean4
variable (x: ℝ)
#check x
-- x : ℝ
```

When I write down a variable which is a Proposition, I'm not providing a proof for it (which would be an element with type whatever the proposition is). Instead, I'm essentially saying "let h be some proof of this proposition."

```lean
variable (h: ∀ x: ℝ, x = x)

#check h
-- h : ∀ (x : ℝ), x = x

#check h 2
-- h 2 : 2 = 2
```

Meanwhile, when you write a `def`, you're doing something different. Here, `foo` maps `x` to proofs that `x = x`. `x = x` is the type here, and I think that this elements of this type are proofs that `x = x`. So `foo` has type (function mapping real numbers to proofs). This is identified with the type (for all real numbers, this proof).

```lean
def foo : ∀ (x: ℝ), x = x := by
  intro h
  rfl

#check foo
-- foo (x : ℝ) : x = x

#check foo 3
-- foo 3 : 3 = 3
```

To actually prove a statement like `foo` which takes as input, we use the `intro` command as shown.

Moving on, here are some more examples.

```lean
def FnUb (f : ℝ → ℝ) (a : ℝ) : Prop :=
  ∀ x, f x ≤ a

#check FnUb
-- FnUb (f : ℝ → ℝ) (a : ℝ) : Prop
```

So `FnUb` is a function which takes in functions `(f : ℝ → ℝ)` and real numbers `(a : ℝ)` and outputs propositions. This is not a variable, so we actually write out exactly what this function outputs.

Now,
```lean
example (hfa : FnUb f a) (hgb : FnUb g b) : FnUb (fun x ↦ f x + g x) (a + b) := by
  intro x
  dsimp
  apply @_root_.add_le_add
  apply hfa
  apply hgb
```

Recall that example is just an anonymous theorem. This is a function that maps inputs `hfa` and `hgb` to objects of *type* `FnUb (fun x ↦ f x + g x) (a + b)`, not an object of *type* Prop!! This is super important. If `FnUb` mapped (stuff) to `a: ℝ`, then the above example would have to map (stuff) to objects of type `a`! This is really quite cool. Just to check that I understand what's going on, observe that this also works:

```lean
example (hfa : FnUb f a) : ((hgb : FnUb g b) → (FnUb (fun x ↦ f x + g x) (a + b))) := by
  intro hgb
  intro x
  dsimp
  apply @_root_.add_le_add
  apply hfa
  apply hgb
```

And just to go full-circle, here's a completely identical (I think the words are "definitionally equivalent") rewriting of the `h` above:
```lean
variable (h1: (x: ℝ) → (x =x))
#check h1
-- h1 : ∀ (x : ℝ), x = x
```

>[!idea]- GPT Summary
>In this exploration of Lean 4, we've learned several key concepts:
> 1. **Functions and Types**: Lean revolves around functions and types. The colon `:` in Lean signifies that something is of a particular type (e.g., `a : ℝ` means `a` is of type `ℝ`). Functions in Lean are denoted as `f x`, which is equivalent to `f(x)` in other languages. A function that outputs another function is conceptually the same as a multi-input function.
> 
> 2. **Theorems as Functions**: Theorems in Lean are functions that map inputs to proofs of propositions. For example, a theorem `abc` takes inputs `a, b, c : ℝ` and produces a proof of `a * b * c = b * (a * c)`. Lean treats this as a function from variables to a proposition.
> 
> 3. **Checking Types with `#check`**: The `#check` command checks the type of an expression. For example, `#check abc` shows that `abc` is a function from real numbers to a proposition. Type-checking is central to Lean’s logic system.
> 
> 4. **Variables as Assumptions**: When declaring a variable in Lean (e.g., `variable (x: ℝ)`), you're stating an assumption that `x` is a real number. Similarly, a variable representing a proposition (e.g., `variable (h: ∀ x: ℝ, x = x)`) indicates that `h` is a proof of that proposition.
> 
> 5. **Defining Functions with `def`**: Defining a function in Lean involves specifying the inputs and the output. For example, `def foo : ∀ (x: ℝ), x = x` defines a function `foo` that proves `x = x` for any real number `x`. The proof is constructed using tactics like `intro` and `rfl` (reflexivity).
> 
> 6. **Anonymous Theorems (`example`)**: Using `example` allows you to write anonymous theorems. This is equivalent to a function mapping inputs (assumptions) to a proof of a proposition. An `example` can be rewritten in multiple ways, showing the flexibility of Lean’s logic system.
> 
> This exploration has revealed Lean’s deep integration of functions, types, and propositions, with proofs being treated as objects of certain types.
