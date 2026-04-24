# Cheat Sheet — For Your Handwritten Notes Page

> Use this to prepare your **double-sided handwritten notes page** for the test.
> Prioritize formulas, key distinctions, and answer templates.

---

## Side 1: Core Formulas & Definitions

### 1. Propositional Logic — Truth Tables

| A | B | ¬A | A∧B | A∨B | A→B | A↔B |
|---|---|---|---|---|---|---|
| T | T | F | T | T | T | T |
| T | F | F | F | T | F | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

**Modus Tollens**: P → Q, ¬Q ⟹ ¬P

**De Morgan's**: ¬(A∧B) = ¬A∨¬B, ¬(A∨B) = ¬A∧¬B

### 2. First-Order Logic

- ∀x P(x): "for all x, P(x) holds"
- ∃x P(x): "there exists an x such that P(x)"
- **¬∀x P(x) = ∃x ¬P(x)**
- Universal instantiation: ∀x P(x) → P(a) for any specific a

### 3. LNN (Logic Neural Networks)

**Soft AND (⊗)**: Product t-norm: A ⊗ B = A × B

**Bounds for OR**: L = max(L_A, L_B), U = max(U_A, U_B)

**Bounds for AND**: L = max(0, L_A + L_B − 1), U = min(U_A, U_B)

**Threshold α classification**:
- L ≥ α → definitely true
- U < α → definitely false  
- L < α < U → uncertain

### 4. TransE

**h + r ≈ t**

Scoring: f(h,r,t) = ‖h + r − t‖

Smaller score = more likely true

### 5. Entropy & Information Gain

H(X) = −Σ p(x) log₂ p(x)

IG = H(parent) − Σ (|child|/|parent|) × H(child)

### 6. Bayes' Theorem

P(H|e) = P(e|H) × P(H) / P(e)

P(e) = P(e|H)P(H) + P(e|¬H)P(¬H)

### 7. Fuzzy Logic Operators

- AND: min(A, B) or A × B
- OR: max(A, B)
- NOT: 1 − A
- Implication: max(1−A, B)

### 8. MYCIN CF Formula

CF(conclusion) = CF(premise) × CF(rule)

CF(premise with AND) = min(CF(A), CF(B), CF(C))

---

## Side 2: Key Distinctions & Answer Templates

### 9. Vagueness vs Uncertainty (MEMORIZE THIS!)

| Vagueness | Uncertainty |
|---|---|
| Concept has **blurry boundaries** | **State of world is unknown** |
| Degree of membership | Belief under incomplete knowledge |
| "To what degree?" | "How likely?" |
| Tool: Fuzzy Logic | Tool: Bayesian Reasoning |
| "high risk", "almost excellent", "tall" | "is there a burglary?", "is it spam?" |

### 10. Forward vs Backward Chaining

| Forward | Backward |
|---|---|
| Data-driven | Goal-driven |
| Facts → Conclusions | Goal → Find support |
| Uses Modus Ponens | Tries to prove hypothesis |
| HOW queries | WHY queries |
| A is sufficient for B | B is necessary for A |

### 11. CART is "Greedy"

"At each node, selects the best split **WITHOUT ANY LOOK-AHEAD**. No effort to craft an optimal tree overall — only a locally optimal decision."

### 12. Feature Bagging

- Random subset of features per tree, size ≈ √(total)
- With replacement, size << total
- Why: reduces correlation between trees in the forest

### 13. GA Components

1. Population (chromosomes with genes)
2. Fitness function (evaluate solutions)
3. Selection (pick fittest)
4. Crossover (mix parents)
5. Mutation (random changes)

### 14. NEAT Key Ideas

- Start minimal (no hidden nodes)
- Add Connection mutation / Add Node mutation
- Innovation numbers for crossover alignment
- Speciation protects new structures
- Fitness sharing: adjusted fitness = fitness / species size

### 15. Robot Soccer Strategy (write ONE)

"Each robot independently assesses the game situation using shared overhead camera. A role-based strategy assigns each robot a role (attacker/defender/goalkeeper) based on current positions. Since all robots see the same information, they can coordinate implicitly without communication."

### 16. Answer Templates

**Explain concept**: "[X] refers to... The key idea is... For example..."

**Compare A vs B**: "While [A] focuses on..., [B] is designed to... The fundamental difference lies in..."

**Deduction**: "Given: [fact]. Rule: [rule]. By [inference rule]: [step]. Therefore: [conclusion]."
