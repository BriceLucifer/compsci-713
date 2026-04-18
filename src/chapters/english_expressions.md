# English Expression Templates for Exam Writing

> 考试英语句型模板 — 直接套用，提升表达质量。
> All templates are derived from the sample test answer style and lecture language.

---

## 1. Explaining a Concept（解释类）

Use when the question says "Explain...", "What is...", "Describe..."

| Pattern | Example |
|---------|---------|
| "[X] refers to the process of..." | "Entropy refers to the measure of impurity or uncertainty in a dataset." |
| "In essence, [X] is a mechanism that enables..." | "In essence, TransE is a mechanism that enables knowledge graph completion by modelling relations as translations in vector space." |
| "The key idea behind [X] is that..." | "The key idea behind feature bagging is that decorrelating trees improves the ensemble's predictive power." |
| "To put it simply, [X] allows a model to..." | "To put it simply, backward chaining allows a system to reason from a goal back to supporting evidence." |

### Defining a Term (1-2 sentence pattern)

> "[Term] is a [category] that [function]. It works by [mechanism]."

**Example:**
> "A Random Forest is an ensemble learning method that combines multiple decision trees to reduce prediction variance. It works by training each tree on a bootstrap sample with a random subset of features."

---

## 2. Comparing Two Concepts（对比类）

Use when the question says "How is [X] different from [Y]?", "Compare..."

| Pattern | Example |
|---------|---------|
| "While [A] focuses on..., [B] is designed to..." | "While bagging focuses on reducing variance by averaging independent models, boosting is designed to reduce bias by sequentially correcting errors." |
| "The fundamental difference between [A] and [B] lies in..." | "The fundamental difference between vagueness and uncertainty lies in what is imprecise: vagueness concerns blurry concept boundaries, while uncertainty concerns unknown world states." |
| "Unlike [A], which requires..., [B] operates by..." | "Unlike Boolean logic, which requires inputs to be strictly 0 or 1, LNN operates over continuous truth values in [0, 1]." |
| "[A] is best suited for..., whereas [B] is preferred when..." | "Fuzzy logic is best suited for graded concepts like 'tall', whereas Bayesian reasoning is preferred for updating beliefs given evidence." |

---

## 3. Describing a Procedure（步骤类）

Use when the question says "Describe how...", "Explain the process..."

> "The process consists of [N] main steps. First, [step 1]. Then, [step 2]. Finally, [step 3]."

**Example (MYCIN backward chaining):**
> "MYCIN uses backward chaining in three steps. First, the system identifies the goal (e.g., determining the organism). Then, it searches for rules whose conclusion matches the goal. Finally, unknown premises become sub-goals, and the process recurses until all premises are resolved."

---

## 4. Justifying a Design Choice（论证类）

Use when the question says "Explain why...", "Why is [X] a good idea?"

| Pattern | Example |
|---------|---------|
| "The rationale for choosing [X] is..." | "The rationale for choosing feature bagging is that it decorrelates trees, making the ensemble more effective." |
| "This approach is advantageous because..." | "This approach is advantageous because continuous truth values enable gradient-based optimization." |
| "A key trade-off to consider is..." | "A key trade-off is that deeper trees have lower bias but higher variance." |
| "One limitation is..., which can be mitigated by..." | "One limitation is TransE's inability to handle 1-to-N relations, mitigated by TransH." |

---

## 5. Computation Answers（计算类）

Template:
> "Given [inputs], we apply [formula]:
> [formula with numbers] = [result].
> Therefore, [interpretation]."

**Example (LNN):**
> "Given Cold = 0.9, AtHome = 0.4, using the product t-norm:
> HeatingOn = 0.9 × 0.4 = 0.36.
> Since 0.36 < 0.5 (threshold), the heating would not activate."

**Example (TransE):**
> "Given h = (0.5, 0.2, 0.7), r = (0.3, 0.2, 0.3):
> h + r = (0.8, 0.4, 1.0).
> L1 distance to France (0.8, 0.4, 1.0) = 0. France is the predicted entity."

---

## 6. Classifying Scenarios（分类判断类）

Template per scenario:
> "[Label]: This involves [A/B] because [reason]."

**Example:**
> "**Vagueness**: 'High risk' involves vagueness because it is a graded concept with no sharp boundary."

---

## 7. Causal Reasoning（因果类）

| Pattern | Example |
|---------|---------|
| "This leads to [X] because..." | "This leads to overfitting because a deep tree memorises noise." |
| "As a result of [X], we observe..." | "As a result of feature bagging, trees become less correlated." |
| "The reason [X] outperforms [Y] is..." | "The reason RF outperforms a single tree is that averaging decorrelated trees reduces variance." |

---

## 8. Linking Phrases

| Purpose | Phrases |
|---------|---------|
| **Adding** | Furthermore, Moreover, Additionally |
| **Contrasting** | However, In contrast, On the other hand |
| **Cause-effect** | Therefore, Consequently, As a result |
| **Example** | For instance, For example, Consider the case where |
| **Summary** | In summary, The key takeaway is |
