# Mock Exam 1 — Answers & Explanations

> Attempt the exam first, then check answers. Award marks using the rubric below.

---

## Question 1 [5 marks]

### (a) [3 marks]

**Given:** $(S \vee T) \rightarrow A$ and $\neg A$.

**Step 1:** Modus Tollens: $\neg A$ and $(S \vee T) \rightarrow A$ → $\neg(S \vee T)$ [1 mark]

**Step 2:** Truth table for the implication:

| $S \vee T$ | $A$ | $(S \vee T) \rightarrow A$ |
|---|---|---|
| 0 | 0 | 1 ✓ |
| 0 | 1 | 1 |
| 1 | 0 | 0 ✗ |
| 1 | 1 | 1 |

Since $A = 0$ and the implication holds, $S \vee T = 0$. [1 mark]

**Step 3:** De Morgan's: $\neg(S \vee T) = \neg S \wedge \neg T$

| $S$ | $T$ | $S \vee T$ |
|---|---|---|
| 0 | 0 | 0 ✓ |
| 0 | 1 | 1 ✗ |
| 1 | 0 | 1 ✗ |
| 1 | 1 | 1 ✗ |

**Conclusion:** Both S and T must be FALSE — no smoke AND no high temperature. [1 mark]

> **Compare with sample test:** There, $(I \wedge F) \rightarrow E$ and $\neg E$ → at least one is false. Here, $(S \vee T) \rightarrow A$ and $\neg A$ → BOTH must be false. The connective (∧ vs ∨) changes the conclusion.

### (b) [2 marks]

**(i):** $\forall x \, [\text{StudyHard}(x) \rightarrow \text{Pass}(x)]$ [1 mark]

**(ii):** $\exists x \, [\text{StudyHard}(x) \wedge \neg \text{Pass}(x)]$

"There exists a student who studies hard but does NOT pass." [1 mark]

> Key: $\neg(P \rightarrow Q) \equiv P \wedge \neg Q$

---

## Question 2 [4 marks]

### (a) [2 marks]

"If a patient has a high fever AND has had contact with an infected patient, recommend testing." [1 mark]

Boolean requires both = 1. LNN accepts continuous values (0.7, 0.5) and produces an intermediate result, enabling gradient-based learning while preserving logical structure. [1 mark]

### (b) [2 marks]

Łukasiewicz: $\max(0, a + b - 1) = \max(0, 0.7 + 0.5 - 1) = \max(0, 0.2) = 0.2$ [1 mark]

- Threshold 0.3: $0.2 < 0.3$ → NOT recommend
- Threshold 0.5: $0.2 < 0.5$ → NOT recommend [1 mark]

> Note: Product t-norm gives $0.7 \times 0.5 = 0.35$, which would pass the 0.3 threshold. T-norm choice matters!

---

## Question 3 [2 marks]

**TransE:** $h + r \approx t$

Infer Sydney: from (Sydney, located\_in, Australia): Sydney ≈ Australia - located\_in = $(0.7-0.4, 0.9-0.3, 0.8-0.4) = (0.3, 0.6, 0.4)$

Predicted tail: $h + r = (0.3+0.4, 0.6+0.3, 0.4+0.4) = (0.7, 0.9, 0.8)$ [1 mark]

L1 distances:
- Australia (0.7, 0.9, 0.8): $|0|+|0|+|0| = 0$ ✓
- NewZealand (0.6, 0.8, 0.7): $0.1+0.1+0.1 = 0.3$
- Oceania (0.9, 1.0, 1.1): $0.2+0.1+0.3 = 0.6$

**Answer: Australia** (distance = 0). [1 mark]

---

## Question 4 [2 marks]

### (a) [1 mark]

**Forward chaining**: data-driven — starts with known facts, fires applicable rules to derive new conclusions.

**Backward chaining**: goal-driven — starts with a hypothesis, finds supporting rules, checks premises recursively.

MYCIN uses backward chaining because it starts with a diagnostic goal (identify the organism) and works backward, asking the doctor for evidence as needed.

### (b) [1 mark]

CF(premise) = min(0.8, 0.5) = 0.5 (AND → take minimum)

CF(measles) = CF(premise) × CF(rule) = 0.5 × 0.7 = **0.35**

---

## Question 5 [3 marks]

### (a) [1 mark]

$p_+ = 0.6, \quad p_- = 0.4$

$H = -(0.6 \times (-0.737)) - (0.4 \times (-1.322)) = 0.442 + 0.529 = **0.971** \text{ bits}$

### (b) [1 mark]

**Bagging**: trains multiple models **independently** on bootstrap samples, combines by majority vote. Reduces **variance**.

**Boosting**: trains models **sequentially**, each focusing on previous errors via sample re-weighting. Reduces **bias**.

### (c) [1 mark]

$\alpha = \frac{1}{2} \ln \frac{1-\epsilon}{\epsilon} = \frac{1}{2} \ln \frac{0.7}{0.3} = \frac{1}{2} \times 0.847 \approx **0.42**$

---

## Question 6 [4 marks]

1. **Uncertainty** — 60% chance of rain is a probability about an unknown future state. [1 mark]
2. **Vagueness** — "reasonably good" is a graded concept with blurry boundaries. [1 mark]
3. **Vagueness** — "mildly obese" has no sharp boundary; it's a degree of a graded concept. [1 mark]
4. **Uncertainty** — The model doesn't know the true class; 85% is a probability over an unknown fact. [1 mark]
