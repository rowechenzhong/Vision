### `import`
- **Definition**: This keyword is used to include external libraries or modules into your Lean file. It allows you to access definitions, theorems, and tactics from these imported files.
- **Usage**: Typically, you import libraries such as Mathlib (Mathematical Components Library) to use its pre-defined mathematical objects, tactics, and theorems.
- **Syntax**:
  ```lean
  import Mathlib.Data.Real.Basic  -- Imports real number definitions and tactics
  import Mathlib.Tactic           -- Imports useful tactics like `ring` and `linarith`
  ```

- **Example**:
  ```lean
  import Mathlib.Data.Nat.Prime

  #check nat.prime -- Now you can access `nat.prime` and its properties
  ```

### `open`
- **Definition**: This keyword opens a **namespace**, making all the definitions, theorems, and lemmas in that namespace available without having to use the full name (i.e., it avoids the need for qualified names). It simplifies the use of libraries by allowing shorter names in the code.
- **Usage**: Instead of referring to an object with its fully qualified name (e.g., `Nat.add`), you can just use `add` if the `Nat` namespace is opened.
- **Syntax**:
  ```lean
  open Nat  -- Opens the Nat namespace so you can use its functions without prefixing
  ```

- **Example**:
  ```lean
  import Mathlib.Data.Nat.Basic

  open Nat  -- Opens the Nat namespace, allowing you to use functions from it directly
  #check add -- This refers to Nat.add
  ```