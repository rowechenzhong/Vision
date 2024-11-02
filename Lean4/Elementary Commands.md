These commands are "elementary" from a pedagogical standpoint, not from any "fundamental" perspective. They can be used to let you hit the ground running in Lean 4 and prove basic statements.

This should be read in parallel with [[Basic Syntax]], which will help you understand from a more "fundamental" level why the syntax looks the way it does.

### 0. Boilerplate

Type this in and forget about it for now.

```lean
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

open Real Nat
```

See [[Import and Open]] for details.

### 1. `example`
- **Definition**: Used to create a simple, unnamed proof of a proposition.
- **Syntax**: 
```lean
  example (a b c : ℝ) : a * b * c = b * (a * c) := by
    rw [mul_comm a b]
    rw [mul_assoc b a c]
```

### 2. `variable`
- **Definition**: Declares variables or assumptions that apply to multiple examples or theorems.
- **Syntax**: 
```lean
  variable (a b c : ℝ)
```

### 3. `theorem`, `lemma`
- **Definition**: Used to define a named theorem, which can be referenced later.
- **Syntax**: 
```lean
  theorem add_comm (a b : ℝ) : a + b = b + a := by
    apply add_comm
```

A `lemma` is the same thing as a `theorem`.

### 5. `by`
- **Definition**: Introduces the tactic mode, which allows step-by-step interactive proving of goals.
- **Syntax**: 
```lean
  by
    rw [mul_assoc]
```

### 6. `rw` (rewrite)
- **Definition**: Used to replace a part of an expression with another part based on an identity or theorem.
- **Syntax**: 
```lean
  rw [mul_comm a b]
```

### 7. `apply`
- **Definition**: Applies a theorem or lemma to the current goal.
- **Syntax**: 
```lean
  apply add_comm
```

### 8. `exact`
- **Definition**: Provides an explicit proof term that solves the goal exactly.
- **Syntax**: 
```lean
  exact h
```

### 9. `calc`
- **Definition**: Used to build structured, step-by-step calculations for proofs.
- **Syntax**: 
```lean
  calc
    (a + b) * (a + b) = a * a + b * a + (a * b + b * b) := by
      rw [mul_add, add_mul, add_mul]
    _ = a * a + (b * a + a * b) + b * b := by
      rw [← add_assoc, add_assoc (a * a)]
```

### 10. `section` / `end`
- **Definition**: Groups related definitions, variables, and theorems into a logical section.
- **Syntax**: 
```lean
  section
    variable (a b c : ℝ)
    theorem mul_comm : a * b = b * a := by
      apply mul_comm
  end
```

### 11. `#check`
- **Definition**: Used to check the type of an expression or proof term.
- **Syntax**: 
```lean
  #check mul_comm
```

### 12. `have`
- **Definition**: Introduces an intermediate result while in tactic mode, allowing you to name it for later use.
- **Syntax**: 
```lean
  have h : a * 0 + a * 0 = a * 0 + 0 := by
    rw [← mul_add, add_zero]
```

### 13. `ring`
- **Definition**: A tactic that automatically simplifies expressions in commutative rings (e.g., integers, real numbers) based on ring axioms.
- **Syntax**: 
```lean
  ring
```

### 14. `linarith`
- **Definition**: A tactic designed for solving goals involving linear inequalities and equalities.
- **Syntax**: 
```lean
  linarith
```

### 15. `norm_num`
- **Definition**: A tactic that simplifies numeric expressions and proves simple arithmetic equalities or inequalities.
- **Syntax**: 
```lean
  norm_num
```

### 16. `nth_rw`
- **Definition**: A variant of the `rw` tactic that applies the rewrite to only a specific occurrence of an expression.
- **Syntax**: 
```lean
  nth_rw 2 [h]
```

### 17. `intro`
- **Definition**: Introduces a variable or hypothesis into the context.
- **Syntax**: 
```lean
  intro x
```

### 18. `apply?`
- **Definition**: Attempts to apply a relevant lemma or theorem from Lean's library to solve a goal.
- **Syntax**: 
```lean
  apply?
```

### 20. `sorry`
- **Definition**: A placeholder for incomplete proofs. It leaves a goal unproven.
- **Syntax**: 
```lean
  sorry
```

### 21. `repeat`
- **Definition**: Repeats a tactic or block of tactics until it can no longer be applied.
- **Syntax**: 
```lean
  repeat
    apply le_min
    apply min_le_right
    apply min_le_left
```

### 22. `ring`
- **Definition**: Automatically proves equalities in commutative rings (like real numbers, integers).
- **Syntax**: 
```lean
  ring
```

These keywords form the essential building blocks of formal proofs and theorem proving in Lean. They help structure logical arguments, manipulate expressions, and automate common proof steps.