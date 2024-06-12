# Lean Formalization and Human-Style Proofs

## Overview

In mathematical logic and proof verification, two main approaches are Lean formalization and human-style proofs. Here’s a brief overview:

## Lean Formalization

**What is Lean?**
Lean is an open-source theorem prover and programming language used to formalize mathematical proofs, ensuring they are precise and verifiable by a computer.

**Process:**
- **Logical Foundations:** Based on dependent type theory.
- **Lean Language:** Combines logical statements with functional programming constructs.
- **Tactics:** Tools to automate the proof process.

**Advantages:**
- **Verification:** Proofs are mechanically verified, eliminating logical errors.
- **Reusability:** Formalized proofs can be reused and built upon.
- **Precision:** Ensures precise and unambiguous proofs.

**Example:**
```lean
theorem add_comm (a b : nat) : a + b = b + a :=
begin
  exact nat.add_comm a b,
end
```

$let A := {(a,b) : ℕ | a+b = b+a}$


# Combining Lean and Human-Style Proofs

Formalization of Human Proofs: Human-style proofs can be formalized in Lean to ensure correctness.
Explanations for Formal Proofs: Formal proofs can be accompanied by human-readable explanations for better understanding.

## Project Structure
Your project includes directories for different types of files:

- input/ and output/: Directories for input and output files, including markdown files.
- lean/: Contains .lean files for Lean formalizations and .human files for human-readable proofs.
- website/: Hosts the static files for the web interface to display the proofs.

```node index.js```
OR
```npm start```
