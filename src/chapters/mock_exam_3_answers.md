# Mock Exam 3 — Answers & Explanations

---

## Question 1 [5 marks]

### (a) [3 marks]

**Step 1:** From Rule 3 ($A$) and Rule 4 ($B$), combine: we know $A$ and $B$. [0.5 mark]

**Step 2:** From $A$ and $B$, we get $A \wedge B$ (conjunction introduction). From $(A \wedge B)$ and Rule 1 $(A \wedge B) \rightarrow C$, by **Modus Ponens**: conclude $C$. [1 mark]

**Step 3:** From $C$ and Rule 2 $C \rightarrow D$, by **Modus Ponens**: conclude $D$. [1 mark]

**All conclusions:** $C$ and $D$. [0.5 mark]

### (b) [2 marks]

**(i):** "No unauthorised user can access" = "For all users, if not authorised, then cannot access"

$$\forall x \, [\neg \text{Authorised}(x) \rightarrow \neg \text{CanAccess}(x)]$$

Equivalently (contrapositive): $\forall x \, [\text{CanAccess}(x) \rightarrow \text{Authorised}(x)]$ [1 mark]

**(ii):** Negation: $\exists x \, [\neg \text{Authorised}(x) \wedge \text{CanAccess}(x)]$

English: "There exists an unauthorised user who CAN access the server." [1 mark]

---

## Question 2 [4 marks]

### (a) [2 marks]

With HighRating = 0.8, RecentlyViewed = 0.3:

| T-norm | Formula | Result |
|--------|---------|--------|
| Product | $0.8 \times 0.3$ | **0.24** |
| Łukasiewicz | $\max(0, 0.8 + 0.3 - 1)$ | **0.10** |
| Gödel | $\min(0.8, 0.3)$ | **0.30** |

Highest: **Gödel (0.30)**. Lowest: **Łukasiewicz (0.10)**. [2 marks]

> Note: Łukasiewicz is the strictest — it requires both values to be high. Gödel is the most lenient.

### (b) [2 marks]

$\neg \text{HighRating} = 1 - 0.8 = 0.2$ [0.5 mark]

Łukasiewicz OR: $\min(1, a + b)$

$\neg \text{HighRating} \vee \text{RecentlyViewed} = \min(1, 0.2 + 0.3) = \min(1, 0.5) = 0.5$ [0.5 mark]

Łukasiewicz implication: $A \rightarrow B = \min(1, 1 - A + B)$

$\text{HighRating} \rightarrow \text{RecentlyViewed} = \min(1, 1 - 0.8 + 0.3) = \min(1, 0.5) = 0.5$ ✓ [1 mark]

They are equal because in Łukasiewicz logic, $A \rightarrow B \equiv \neg A \vee B$, just like in classical logic.

---

## Question 3 [2 marks]

$h + r = (0.3 + 0.5, 0.7 + 0.3, 0.5 + 0.4) = (0.8, 1.0, 0.9)$ [1 mark]

L1 distances:
- **Germany (0.8, 1.0, 0.9):** $|0|+|0|+|0| = **0**$ ✓
- France (0.6, 0.9, 0.8): $0.2 + 0.1 + 0.1 = 0.4$
- USA (1.0, 0.5, 1.2): $0.2 + 0.5 + 0.3 = 1.0$

**Answer: Germany** (distance = 0). Einstein was born in Germany. [1 mark]

---

## Question 4 [2 marks]

### (a) [1 mark]

- Rule A: AND(dirty, large) = min(0.7, 0.4) = **0.4**
- Rule B: dirty = **0.7**

Rule B fires more strongly (0.7 > 0.4).

### (b) [1 mark]

Standard: $\text{dirty} \rightarrow \text{large} = \max(1 - 0.7, 0.4) = \max(0.3, 0.4) = 0.4$

Gödel: Since $0.7 > 0.4$ (A > B), result = $B = 0.4$

Both give 0.4 in this case. But consider dirty = 0.7, large = 0: Standard gives $\max(0.3, 0) = 0.3$ (implication partially holds?), while Gödel gives 0 (implication fails). **Gödel is more intuitive** because if the premise holds but the conclusion doesn't, the implication should be false (0), not partially true (0.3).

---

## Question 5 [3 marks]

### (a) [1 mark]

$\sqrt{400} = 20$ features per split.

This is chosen because using all features would cause every tree to split on the same dominant feature → highly correlated trees → averaging doesn't help. $\sqrt{p}$ forces diversity, making trees less correlated and the ensemble more effective.

### (b) [2 marks]

**Naïve Bayes assumes features are conditionally independent given the class.**

$P(\text{disease} | s_1, s_2) \propto P(\text{disease}) \times P(s_1|\text{disease}) \times P(s_2|\text{disease})$
$= 0.01 \times 0.9 \times 0.7 = 0.0063$ [1 mark]

$P(\text{no disease} | s_1, s_2) \propto P(\text{no disease}) \times P(s_1|\text{no disease}) \times P(s_2|\text{no disease})$
$= 0.99 \times 0.05 \times 0.1 = 0.00495$

Since $0.0063 > 0.00495$, **disease has higher posterior**. The classifier would predict disease. [1 mark]

> Despite only a 1% base rate, both symptoms together make disease MORE likely than no disease.

---

## Question 6 [4 marks]

### (a) [1 mark]

**TransE limitation:** It struggles with **N-to-1 relations** (many heads, same relation, same tail). For example, (Paris, located\_in, France) and (Lyon, located\_in, France) would force Paris and Lyon to have the same embedding, losing distinctiveness.

**TransH** fixes this by projecting entities onto a **relation-specific hyperplane** before applying the translation. Different entities can be distinguished even when they share a relation and tail.

### (b) [1 mark]

RAG pipeline:
1. **User submits a query** (e.g., "Who won the Turing Award in 2023?")
2. **Knowledge retrieval**: search structured (KGs, databases) and unstructured (documents) sources using BM25, DPR, or FAISS for relevant information
3. **Contextual integration**: retrieved documents are passed to the LLM as additional context, and the LLM generates a factually grounded response

### (c) [1 mark]

The **knowledge acquisition bottleneck** refers to the difficulty and expense of extracting expert knowledge and encoding it as formal rules. Human experts often find it hard to articulate their reasoning explicitly, and the process of interviewing experts, formalising their knowledge, and validating the rules is extremely time-consuming and doesn't scale.

### (d) [1 mark]

$\alpha_t = \frac{1}{2}\ln\frac{1-\epsilon_t}{\epsilon_t}$

When $\epsilon_t$ is small (low error), $(1-\epsilon_t)/\epsilon_t$ is large, making $\ln$ and thus $\alpha_t$ large. This means **more accurate classifiers get higher weight** in the final ensemble vote. The ensemble trusts accurate models more and inaccurate ones less — this is the key mechanism behind AdaBoost's ability to combine weak learners into a strong classifier.
