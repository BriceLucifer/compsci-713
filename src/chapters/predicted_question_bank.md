# Predicted Question Bank — COMPSCI 713 Mid-Term 2026

> This question bank is organized by topic and difficulty. Each question includes the full exam-style question text, a detailed model answer, mark allocation, prediction rationale, and key pitfalls.

## Prediction Methodology

Based on analysis of **4 past papers** (2025 Sample, 2025 Real, 2026 Sample, 2026 Sample Answers) and **all lecture content** (W2L1 through W6L1):

- **Q1--Q3 are FIXED topics** (Logic, LNN, KG) but difficulty is escalating (Q1 went from 2 to 5 marks)
- **Q4--Q6 ROTATE** — topics not tested recently have higher probability of appearing
- Topics covered extensively in lecture exercises but **never tested** are HIGH RISK for surprises
- The 2026 sample escalated difficulty (20 marks vs 15, Q1 from 2 to 5 marks)

**Priority levels:**
- HIGH RISK = covered in lectures with exercises, never tested on exam
- GUARANTEED = appears in every past paper, expect it again
- ROTATION CANDIDATE = has appeared before, may rotate back in

---

---

# Section 1: Guaranteed Topics — Harder Variants

These topics (Logic, LNN, KG) appear in **every** past paper. The 2026 trend shows marks increasing and questions becoming more complex. Prepare for harder versions.

---

## 1.1 Symbolic Logic — Multi-Step Modus Tollens Chain

### 题目

**Q1a [3 marks]:** Consider the following rules:

- Rule 1: SupportedByData(x) → AcceptedByCommunity(x)
- Rule 2: AcceptedByCommunity(x) → ReceivesFunding(x)
- Rule 3: ReceivesFunding(x) → RecognizedInAcademia(x)

Given: ¬RecognizedInAcademia(QuantumGravityTheory)

Using Modus Tollens, deduce what can be concluded about QuantumGravityTheory. Show each step of the deduction chain.

### 详细解答

**Step 1:** From Rule 3 and ¬RecognizedInAcademia(QGT):

Rule 3 says: ReceivesFunding(x) → RecognizedInAcademia(x)

By Modus Tollens (P → Q, ¬Q ⊢ ¬P):

¬RecognizedInAcademia(QGT) ⊢ **¬ReceivesFunding(QGT)**

**Step 2:** From Rule 2 and ¬ReceivesFunding(QGT):

Rule 2 says: AcceptedByCommunity(x) → ReceivesFunding(x)

By Modus Tollens:

¬ReceivesFunding(QGT) ⊢ **¬AcceptedByCommunity(QGT)**

**Step 3:** From Rule 1 and ¬AcceptedByCommunity(QGT):

Rule 1 says: SupportedByData(x) → AcceptedByCommunity(x)

By Modus Tollens:

¬AcceptedByCommunity(QGT) ⊢ **¬SupportedByData(QGT)**

**Conclusion:** QuantumGravityTheory is not supported by data, not accepted by the community, does not receive funding, and is not recognized in academia.

### 评分标准

| Component | Marks |
|---|---|
| Correctly apply MT once to get ¬ReceivesFunding | 1 |
| Chain MT to get ¬AcceptedByCommunity | 1 |
| Chain MT again to get ¬SupportedByData | 1 |

### 为什么可能考到

- Every past paper tests Modus Tollens, but only with a single rule application. The 2026 sample escalated Q1 from 2 to 5 marks, suggesting multi-step reasoning is now in scope.
- Exercise 4 from the lecture slides (W2L1) explicitly practices multi-step MT chains.
- The teacher values "reasoning ability" — chaining is a natural escalation.

### 注意点

- You must show EACH step explicitly. Do not jump from ¬Recognized to ¬Supported in one line.
- State "By Modus Tollens" at each step — the examiner wants to see you name the inference rule.
- Do not confuse Modus Tollens (backward: ¬Q ⊢ ¬P) with Modus Ponens (forward: P ⊢ Q).

---

## 1.2 Symbolic Logic — FOL with Negation of Existential

### 题目

**Q1b [2 marks]:** Express the following in First-Order Logic, then negate it and simplify:

"There exists a student who has failed every assignment."

### 详细解答

**Step 1 — Original statement in FOL:**

\\[
\exists x \bigl( \text{Student}(x) \land \forall y \bigl( \text{Assignment}(y) \to \text{Failed}(x, y) \bigr) \bigr)
\\]

**Step 2 — Negate:**

\\[
\neg \exists x \bigl( \text{Student}(x) \land \forall y \bigl( \text{Assignment}(y) \to \text{Failed}(x, y) \bigr) \bigr)
\\]

**Step 3 — Push negation inward:**

\\( \neg \exists x (\ldots) \equiv \forall x \neg (\ldots) \\)

\\[
\forall x \neg \bigl( \text{Student}(x) \land \forall y \bigl( \text{Assignment}(y) \to \text{Failed}(x, y) \bigr) \bigr)
\\]

Apply De Morgan's: \\( \neg(A \land B) \equiv \neg A \lor \neg B \\)

\\[
\forall x \bigl( \neg \text{Student}(x) \lor \neg \forall y \bigl( \text{Assignment}(y) \to \text{Failed}(x, y) \bigr) \bigr)
\\]

Push negation into \\( \neg \forall y \\): this becomes \\( \exists y \neg (\ldots) \\)

\\[
\forall x \bigl( \neg \text{Student}(x) \lor \exists y \neg \bigl( \text{Assignment}(y) \to \text{Failed}(x, y) \bigr) \bigr)
\\]

Since \\( \neg(P \to Q) \equiv P \land \neg Q \\):

\\[
\forall x \bigl( \neg \text{Student}(x) \lor \exists y \bigl( \text{Assignment}(y) \land \neg \text{Failed}(x, y) \bigr) \bigr)
\\]

**In English:** "For every student, there exists at least one assignment they did NOT fail." Equivalently: "There is no student who failed every assignment."

### 评分标准

| Component | Marks |
|---|---|
| Correct original FOL translation | 1 |
| Correct negation with proper simplification | 1 |

### 为什么可能考到

- Q1b in every past paper involves FOL quantifier manipulation. The 2025 and 2026 samples test \\( \neg \forall x \\) (negation of universal). Testing \\( \neg \exists x \\) (negation of existential) is the natural next step.
- Lecture slides explicitly cover both quantifier negation directions.

### 注意点

- Always push the negation ALL the way in. Stopping at \\( \forall x \neg(\ldots) \\) is incomplete.
- Remember: \\( \neg(P \to Q) \equiv P \land \neg Q \\), NOT \\( \neg P \to \neg Q \\).
- Provide the English translation — the teacher explicitly rewards this in marking rubrics.

---

## 1.3 Symbolic Logic — Modus Tollens with Biconditional

### 题目

**Q1a variant [2 marks]:** Given:
- Rule: P ↔ Q (P if and only if Q)
- Fact: ¬Q

What can you conclude about P? Justify your answer using a truth table or logical equivalences.

### 详细解答

P ↔ Q means \\( (P \to Q) \land (Q \to P) \\).

From the \\( P \to Q \\) component:

We have \\( P \to Q \\) and \\( \neg Q \\).

By Modus Tollens: \\( \neg P \\).

**Conclusion: ¬P** (P is false).

**Verification via truth table:**

| P | Q | P ↔ Q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| **F** | **F** | **T** |

Since Q is False, only rows 2 and 4 are candidates. P ↔ Q is True only in row 4, where P = False. Therefore ¬P.

### 评分标准

| Component | Marks |
|---|---|
| Correctly decompose ↔ into two implications and apply MT | 1 |
| Justify with truth table or logical reasoning | 1 |

### 为什么可能考到

- The biconditional (↔) is covered in lectures but has never appeared on a test. Every past paper uses →. Testing ↔ is a small twist that tests deeper understanding.
- The truth table for ↔ is on the lecture slides (W2L1).

### 注意点

- Do NOT assume ↔ works the same as →. With ↔, the reasoning works in BOTH directions, whereas → is one-way only.
- If the question says "if and only if," you MUST use ↔, not →.

---

## 1.4 LNN — Product-Sum OR Computation

### 题目

**Q2b [2 marks]:** Using Product-Sum operators, compute \\( F \lor C \\) where F = 0.9 and C = 0.7. Show your working.

### 详细解答

Product-Sum OR formula:

\\[
F \lor C = F + C - F \times C
\\]

Substituting:

\\[
= 0.9 + 0.7 - (0.9 \times 0.7) = 1.6 - 0.63 = 0.97
\\]

**Answer: 0.97**

### 评分标准

| Component | Marks |
|---|---|
| Write the correct Product-Sum OR formula | 1 |
| Substitute and compute correctly | 1 |

### 为什么可能考到

- Exercise 5 on slide 25 of W2L2 is exactly this computation. Lecture exercises that align with exam-style questions are strong predictors.
- Past papers have tested AND computation (t-norms). Testing OR is the natural complement.

### 注意点

- Do NOT use max(F, C) = 0.9. That is the Godel/Zadeh OR, not Product-Sum OR.
- Product-Sum OR always gives a result \\(\geq\\) max(inputs). If your answer is lower than both inputs, you used the wrong formula.
- State which operator family you are using.

---

## 1.5 LNN — Nested Computation (AND then OR)

### 题目

**Q2b [2 marks]:** Using Product-Sum operators, compute \\( (C \land SOB) \lor F \\) where C = 0.7, SOB = 0.5, F = 0.9. Show each step.

### 详细解答

**Step 1 — Compute AND first:**

Product-Sum AND: \\( C \land SOB = C \times SOB \\)

\\[
C \land SOB = 0.7 \times 0.5 = 0.35
\\]

**Step 2 — Compute OR with F:**

Product-Sum OR: \\( X \lor Y = X + Y - X \times Y \\)

\\[
0.35 \lor 0.9 = 0.35 + 0.9 - (0.35 \times 0.9) = 1.25 - 0.315 = 0.935
\\]

**Answer: 0.935**

### 评分标准

| Component | Marks |
|---|---|
| Correctly compute AND first (order of operations) | 1 |
| Correctly compute OR second with the AND result | 1 |

### 为什么可能考到

- This is Exercise 6 from lecture slide 25 (W2L2). The exam has been testing single-operation LNN computations; a nested computation is the natural escalation given the trend toward harder questions.

### 注意点

- Order of operations matters: compute the inner expression (AND) FIRST, then use that result in the outer expression (OR).
- Do not confuse Product-Sum AND (multiplication) with Lukasiewicz AND (max(0, a+b-1)).

---

## 1.6 LNN — Lukasiewicz AND Bounds Computation

### 题目

**Q2b [2 marks]:** Using the Lukasiewicz t-norm, compute \\( P \land Q \\) where P has bounds [0.4, 0.7] and Q has bounds [0.3, 0.6]. Show the computation of both lower and upper bounds.

### 详细解答

Lukasiewicz AND formula: \\( A \otimes B = \max(0, A + B - 1) \\)

**Lower bound:**

\\[
L = \max(0, L_P + L_Q - 1) = \max(0, 0.4 + 0.3 - 1) = \max(0, -0.3) = 0
\\]

**Upper bound:**

\\[
U = \min(U_P, U_Q) = \min(0.7, 0.6) = 0.6
\\]

**Result: [0, 0.6]**

This means: the conjunction P AND Q has a truth value between 0 (could be completely false) and 0.6 (at most moderately true).

### 评分标准

| Component | Marks |
|---|---|
| Correctly compute lower bound using Lukasiewicz (note: result clips to 0) | 1 |
| Correctly compute upper bound | 1 |

### 为什么可能考到

- The 2025 Real paper Q2 tested OR bounds computation with a threshold. Testing AND bounds is the complement.
- The Lukasiewicz t-norm can produce a NEGATIVE intermediate value that clips to 0 — this is a natural trap question.
- Lecture slides (W2L2) explicitly teach bounds computation.

### 注意点

- The lower bound CAN be 0 even when both inputs are nonzero. This happens when the inputs do not "overlap" enough under Lukasiewicz. Do NOT write a negative number — always apply max(0, ...).
- Upper bound uses min(), NOT the Lukasiewicz formula. The upper bound formula is different from the lower bound formula.

---

## 1.7 KG — TransE Vector Computation

### 题目

**Q3 [2 marks]:** In a TransE knowledge graph embedding, the following vectors are learned:

- Paris = (0.5, 0.2, 0.7)
- located_in = (0.3, 0.2, 0.3)
- France = (0.8, 0.4, 1.0)
- Europe = (1.1, 0.6, 1.3)
- Germany = (0.9, 0.5, 0.8)

**(a)** Compute h + r for the triple (Paris, located_in, ?).

**(b)** Using L1 distance (Manhattan distance), determine which entity (France, Europe, or Germany) is the most likely tail. Show your computation.

### 详细解答

**(a)** h + r = Paris + located_in = (0.5+0.3, 0.2+0.2, 0.7+0.3) = **(0.8, 0.4, 1.0)**

**(b)** L1 distance = \\( \sum |h + r - t| \\)

**Distance to France (0.8, 0.4, 1.0):**

\\[
|0.8-0.8| + |0.4-0.4| + |1.0-1.0| = 0 + 0 + 0 = \mathbf{0.0}
\\]

**Distance to Europe (1.1, 0.6, 1.3):**

\\[
|0.8-1.1| + |0.4-0.6| + |1.0-1.3| = 0.3 + 0.2 + 0.3 = \mathbf{0.8}
\\]

**Distance to Germany (0.9, 0.5, 0.8):**

\\[
|0.8-0.9| + |0.4-0.5| + |1.0-0.8| = 0.1 + 0.1 + 0.2 = \mathbf{0.4}
\\]

**Conclusion:** France has the smallest distance (0.0), so the predicted tail is **France**. This makes sense: Paris is located in France.

### 评分标准

| Component | Marks |
|---|---|
| Correctly compute h + r | 0.5 |
| Correctly compute L1 distances and identify closest entity | 1.5 |

### 为什么可能考到

- Exercise 5 from lecture W3L1 is a TransE vector computation with actual numbers. Past papers have only asked for the formula (h + r ≈ t) without numerical computation. Given the escalation trend, a numerical question is plausible.
- The teacher values "show your working" — vector arithmetic is a natural way to test this.

### 注意点

- L1 (Manhattan) distance uses absolute values and sums. L2 (Euclidean) uses squares and square root. Check which one the question specifies.
- TransE scoring: LOWER distance = MORE likely to be true. Do not say "highest score."
- If the question asks for the scoring function, it is \\( f(h,r,t) = -\\|h+r-t\\| \\). The negative sign means higher score = better.

---

## 1.8 KG — TransE Limitations and TransH

### 题目

**Q3 variant [2 marks]:**

**(a)** Describe one fundamental limitation of TransE. [1 mark]

**(b)** How does TransH address this limitation? [1 mark]

### 详细解答

**(a)** TransE cannot handle **1-to-N, N-to-1, or N-to-N relations** properly. In TransE, h + r ≈ t. If one head maps to multiple tails via the same relation (e.g., "locatedIn" for a country containing many cities), then all those tail entities must have approximately the same embedding: t ≈ h + r. This forces different entities to collapse into the same point in vector space, which destroys their distinguishability.

Example: (France, contains, Paris), (France, contains, Lyon), (France, contains, Marseille). TransE would require Paris ≈ Lyon ≈ Marseille in embedding space, which is clearly wrong.

**(b)** TransH projects each entity onto a **relation-specific hyperplane** before computing the translation. Instead of h + r ≈ t directly, TransH computes:

\\[
h_\perp + d_r \approx t_\perp
\\]

where \\( h_\perp \\) and \\( t_\perp \\) are projections of h and t onto the hyperplane of relation r. This allows the same entity to have different representations for different relations, solving the 1-to-N collapse problem.

### 评分标准

| Component | Marks |
|---|---|
| Identify the 1-to-N / collapse problem with a clear example | 1 |
| Explain TransH's hyperplane projection mechanism | 1 |

### 为什么可能考到

- Lecture W3L2 covers TransE limitations and TransH as an improvement. Past papers have only tested TransE's basic formula. A "limitation + improvement" question tests deeper understanding and aligns with the teacher's preference for "why" questions.

### 注意点

- Do not say "TransE is inaccurate." Be specific: the problem is with 1-to-N relations.
- TransH still uses translation (d_r), but in a projected space. It is NOT a completely different approach.

---

---

# Section 2: Never-Tested, High-Risk Topics

These topics are covered extensively in lectures (often with exercises) but have **never appeared on a past exam**. They are the most likely source of surprises on Q4--Q6.

---

## 2.1 Entropy and Information Gain Calculation

### 题目

**[3 marks]:** A dataset contains 10 emails: 6 Spam and 4 Not Spam. A feature "ContainsLink" splits the data as follows:

- ContainsLink = Yes: 5 Spam, 1 Not Spam (6 total)
- ContainsLink = No: 1 Spam, 3 Not Spam (4 total)

**(a)** Compute the entropy of the root node (before splitting). [1 mark]

**(b)** Compute the Information Gain from splitting on "ContainsLink." [2 marks]

### 详细解答

**(a) Root entropy:**

\\[
H(\text{root}) = -\left(\frac{6}{10}\log_2\frac{6}{10} + \frac{4}{10}\log_2\frac{4}{10}\right)
\\]

Computing each term:
- \\( 0.6 \times \log_2(0.6) = 0.6 \times (-0.737) = -0.442 \\)
- \\( 0.4 \times \log_2(0.4) = 0.4 \times (-1.322) = -0.529 \\)

\\[
H(\text{root}) = 0.442 + 0.529 = \mathbf{0.971 \text{ bits}}
\\]

**(b) Information Gain:**

**Left child (ContainsLink = Yes): 5S, 1NS (6 total)**

\\[
H(\text{left}) = -\left(\frac{5}{6}\log_2\frac{5}{6} + \frac{1}{6}\log_2\frac{1}{6}\right)
\\]

- \\( 0.833 \times \log_2(0.833) = 0.833 \times (-0.263) = -0.219 \\)
- \\( 0.167 \times \log_2(0.167) = 0.167 \times (-2.585) = -0.431 \\)

\\[
H(\text{left}) = 0.219 + 0.431 = 0.650 \text{ bits}
\\]

**Right child (ContainsLink = No): 1S, 3NS (4 total)**

\\[
H(\text{right}) = -\left(\frac{1}{4}\log_2\frac{1}{4} + \frac{3}{4}\log_2\frac{3}{4}\right)
\\]

- \\( 0.25 \times \log_2(0.25) = 0.25 \times (-2.0) = -0.5 \\)
- \\( 0.75 \times \log_2(0.75) = 0.75 \times (-0.415) = -0.311 \\)

\\[
H(\text{right}) = 0.5 + 0.311 = 0.811 \text{ bits}
\\]

**Weighted average entropy after split:**

\\[
H(\text{after}) = \frac{6}{10} \times 0.650 + \frac{4}{10} \times 0.811 = 0.390 + 0.324 = 0.714 \text{ bits}
\\]

**Information Gain:**

\\[
\text{IG} = H(\text{root}) - H(\text{after}) = 0.971 - 0.714 = \mathbf{0.257 \text{ bits}}
\\]

### 评分标准

| Component | Marks |
|---|---|
| Correct root entropy computation with formula shown | 1 |
| Correct child entropies (both) | 1 |
| Correct weighted average and final IG | 1 |

### 为什么可能考到

- Entropy and Information Gain occupy 10+ slides in W4L2 (slides 15--26) with worked examples. This is one of the most heavily taught topics that has NEVER been tested.
- The teacher tests decision tree topics frequently (CART greedy, feature bagging). Entropy/IG is the mathematical foundation — testing it is natural.
- The lecture includes Exercise problems on entropy computation.
- Numerical "show your working" computations align with the teacher's style.

### 注意点

- Use \\(\log_2\\), NOT natural log (ln). The unit is "bits" with \\(\log_2\\).
- The convention \\(0 \log 0 = 0\\). If a child is pure (only one class), its entropy is 0 — do not divide by zero.
- The weighted average uses \\(|S_v|/|S|\\) as weights — the PROPORTION of data in each child, not equal weights.
- Higher IG = better split. The feature with the highest IG should be chosen at the root.

---

## 2.2 Naive Bayes Classification

### 题目

**[3 marks]:** An email classifier uses Naive Bayes. From the training data:

- P(Spam) = 0.4, P(Not Spam) = 0.6
- P("free" | Spam) = 0.8, P("free" | Not Spam) = 0.1
- P("meeting" | Spam) = 0.1, P("meeting" | Not Spam) = 0.7

A new email contains the words "free" and "meeting." Classify it as Spam or Not Spam. Show your computation.

### 详细解答

By Bayes' theorem and the Naive Bayes independence assumption:

\\[
P(\text{Spam} | \text{free}, \text{meeting}) \propto P(\text{Spam}) \times P(\text{free}|\text{Spam}) \times P(\text{meeting}|\text{Spam})
\\]

**Compute numerator for Spam:**

\\[
0.4 \times 0.8 \times 0.1 = 0.032
\\]

**Compute numerator for Not Spam:**

\\[
P(\text{NS}) \times P(\text{free}|\text{NS}) \times P(\text{meeting}|\text{NS}) = 0.6 \times 0.1 \times 0.7 = 0.042
\\]

**Normalize:**

\\[
P(\text{Spam}|\text{evidence}) = \frac{0.032}{0.032 + 0.042} = \frac{0.032}{0.074} \approx 0.432
\\]

\\[
P(\text{NS}|\text{evidence}) = \frac{0.042}{0.074} \approx 0.568
\\]

**Classification: Not Spam** (0.568 > 0.432)

Despite the word "free" strongly suggesting spam, the word "meeting" strongly suggests not-spam, and the prior favors not-spam. The combination tips the balance toward Not Spam.

### 评分标准

| Component | Marks |
|---|---|
| Correct formula (Bayes with Naive independence assumption) | 1 |
| Correct computation of both numerators | 1 |
| Correct normalization and final classification | 1 |

### 为什么可能考到

- Bayesian reasoning is covered in W5L1 (Soft Computing) with the Naive Bayes email classifier as a running example.
- The Spam classifier is the canonical Naive Bayes example from lectures.
- Decision trees and Bayes are the two main "learning from data" approaches taught in this course. Decision trees have been tested repeatedly; Naive Bayes has never been tested.
- The computation is mechanical and suits the "show your working" exam style.

### 注意点

- "Naive" means features are assumed INDEPENDENT given the class. You multiply the likelihoods. Do not add them.
- You do NOT need to compute the denominator P(evidence) for classification — just compare the numerators. But normalizing gives a cleaner answer.
- If the question asks for "probability," you MUST normalize. If it just says "classify," comparing unnormalized scores is sufficient.

---

## 2.3 Bayes' Theorem — The False Positive Trap

### 题目

**[2 marks]:** A rare disease affects 0.1% of the population (prevalence = 0.001). A diagnostic test has:
- Sensitivity (true positive rate) = 0.99
- False positive rate = 0.05

A person tests positive. What is the probability they actually have the disease?

### 详细解答

Using Bayes' theorem:

\\[
P(\text{Disease}|\text{Positive}) = \frac{P(\text{Pos}|\text{Disease}) \times P(\text{Disease})}{P(\text{Positive})}
\\]

**Compute P(Positive) using total probability:**

\\[
P(\text{Pos}) = P(\text{Pos}|\text{D}) \times P(\text{D}) + P(\text{Pos}|\neg\text{D}) \times P(\neg\text{D})
\\]

\\[
= 0.99 \times 0.001 + 0.05 \times 0.999 = 0.00099 + 0.04995 = 0.05094
\\]

**Apply Bayes:**

\\[
P(\text{D}|\text{Pos}) = \frac{0.00099}{0.05094} \approx \mathbf{0.019} \approx 1.9\%
\\]

**Key insight:** Even with a positive test result, the probability of actually having the disease is only about 2%. This is because the disease is so rare (low prior) that the false positives from healthy people vastly outnumber the true positives from sick people.

### 评分标准

| Component | Marks |
|---|---|
| Correct application of Bayes' theorem with total probability | 1 |
| Correct numerical answer and interpretation of the result | 1 |

### 为什么可能考到

- Bayes' theorem is taught in W5L1 with the base-rate fallacy as a key concept. It demonstrates why probabilistic reasoning is counterintuitive.
- This is a classic exam question in any AI course that covers Bayesian reasoning.
- It tests whether students understand the role of the prior P(Disease) — a concept the teacher emphasizes.

### 注意点

- The most common mistake is computing \\( P(\text{D}|\text{Pos}) = 0.99 \\) (confusing sensitivity with posterior). Sensitivity is P(Pos|D), NOT P(D|Pos).
- Always compute P(Positive) using the law of total probability. Do not skip this step.
- The counterintuitive result (only ~2%) is the POINT of the question. State the insight.

---

## 2.4 Gini Impurity Computation

### 题目

**[2 marks]:** A decision tree node contains 8 examples: 5 Class A and 3 Class B. After splitting on a feature, the left child has {4A, 1B} and the right child has {1A, 2B}.

Compute the Gini impurity of the root node and the weighted Gini after splitting. Does the split reduce impurity?

### 详细解答

**Gini impurity formula:**

\\[
\text{Gini}(S) = 1 - \sum_{i} p_i^2
\\]

**Root node:** 5A, 3B out of 8

\\[
\text{Gini}(\text{root}) = 1 - \left(\frac{5}{8}\right)^2 - \left(\frac{3}{8}\right)^2 = 1 - 0.391 - 0.141 = \mathbf{0.469}
\\]

**Left child:** 4A, 1B out of 5

\\[
\text{Gini}(\text{left}) = 1 - \left(\frac{4}{5}\right)^2 - \left(\frac{1}{5}\right)^2 = 1 - 0.64 - 0.04 = 0.32
\\]

**Right child:** 1A, 2B out of 3

\\[
\text{Gini}(\text{right}) = 1 - \left(\frac{1}{3}\right)^2 - \left(\frac{2}{3}\right)^2 = 1 - 0.111 - 0.444 = 0.444
\\]

**Weighted Gini after split:**

\\[
\text{Gini}(\text{after}) = \frac{5}{8} \times 0.32 + \frac{3}{8} \times 0.444 = 0.200 + 0.167 = \mathbf{0.367}
\\]

**Gini reduction:** \\( \Delta \text{Gini} = 0.469 - 0.367 = 0.102 \\)

**Yes, the split reduces impurity** by 0.102.

### 评分标准

| Component | Marks |
|---|---|
| Correct root Gini computation | 0.5 |
| Correct child Gini values and weighted average | 1 |
| Correct conclusion about impurity reduction | 0.5 |

### 为什么可能考到

- CART uses Gini impurity as its splitting criterion (lecture W4L2, slide 28). Past papers tested "what does greedy mean" but never the actual impurity computation.
- Entropy computation (tested above) and Gini are the two measures from the lecture. If one appears, the other is also fair game.

### 注意点

- Gini impurity ranges from 0 (pure) to 0.5 (for two classes, maximum impurity). If you get a value > 0.5 for binary classification, you made an arithmetic error.
- Gini is NOT entropy. They are different measures that serve the same purpose. Do not use log in Gini.
- Use the proportion of samples in each child as weights (|child|/|parent|).

---

## 2.5 Reynolds' Flocking Rules

### 题目

**[2 marks]:** Craig Reynolds' Boids model uses three simple rules to produce realistic flocking behavior.

**(a)** List and briefly explain each rule. [1.5 marks]

**(b)** What broader AI principle does this demonstrate? [0.5 marks]

### 详细解答

**(a)** The three rules, applied to each individual "boid":

1. **Collision Avoidance (Separation):** Each boid steers away from any neighbor that is within a minimum separation distance. This prevents boids from crowding together or colliding.

2. **Flock Centering (Cohesion):** Each boid steers toward the average position of its nearby neighbors. This pulls the flock together and prevents individuals from drifting away.

3. **Velocity Matching (Alignment):** Each boid adjusts its velocity (speed and direction) to match the average velocity of its nearby neighbors. This makes the flock move as a coordinated unit.

**(b)** This demonstrates **emergence**: complex, coordinated global behavior arising from simple local rules followed by individual agents. No boid knows about the flock as a whole; each only observes its nearest neighbors. Yet the collective behavior — a realistic murmuration — appears spontaneously.

### 评分标准

| Component | Marks |
|---|---|
| Correctly name and explain all 3 rules (0.5 each) | 1.5 |
| Identify emergence as the key principle | 0.5 |

### 为什么可能考到

- Reynolds' Boids are taught in W6L1 with substantial lecture time. The three rules are a clean, memorizable fact — perfect for a 2-mark question.
- Multi-agent systems (robot soccer) appears frequently. Boids/flocking is the OTHER multi-agent topic from the same lecture and has never been tested.
- "Emergence" is a key course theme that connects to several topics.

### 注意点

- The rules are LOCAL — each boid only looks at NEARBY neighbors, not the entire flock. Emphasize this.
- Do not confuse the rules: Separation pushes AWAY, Cohesion pulls TOWARD, Alignment matches VELOCITY.
- There is no leader and no global plan. If you mention a "lead bird," you are wrong.

---

## 2.6 Forward Chaining (Never Tested — Only Backward Has Been Tested)

### 题目

**[3 marks]:** Given the following rules and facts:

**Rules:**
- R1: IF HasFever(x) AND HasCough(x) THEN MayHaveFlu(x)
- R2: IF MayHaveFlu(x) AND NotVaccinated(x) THEN PrescribeAntiviral(x)
- R3: IF HasRash(x) THEN MayHaveAllergy(x)

**Facts:**
- HasFever(Alice)
- HasCough(Alice)
- NotVaccinated(Alice)

**(a)** Show the forward chaining process step by step. [2 marks]

**(b)** How does forward chaining differ from backward chaining? [1 mark]

### 详细解答

**(a) Forward chaining (data-driven):**

**Iteration 1:** Start with known facts: {HasFever(Alice), HasCough(Alice), NotVaccinated(Alice)}

Check all rules:
- R1: HasFever(Alice) AND HasCough(Alice) — both satisfied → **FIRE R1**
- New fact derived: **MayHaveFlu(Alice)**
- R2: MayHaveFlu(Alice)? Not yet known at start of this iteration. (In some implementations, newly derived facts trigger re-evaluation.)
- R3: HasRash(Alice)? Not in facts. R3 does not fire.

Updated facts: {HasFever(Alice), HasCough(Alice), NotVaccinated(Alice), MayHaveFlu(Alice)}

**Iteration 2:** Check all rules against updated facts:
- R1: Already fired, no new conclusions.
- R2: MayHaveFlu(Alice) AND NotVaccinated(Alice) — both satisfied → **FIRE R2**
- New fact derived: **PrescribeAntiviral(Alice)**
- R3: Still does not fire.

Updated facts: {HasFever, HasCough, NotVaccinated, MayHaveFlu, **PrescribeAntiviral**(Alice)}

**Iteration 3:** No new rules fire. **Halt.**

Final conclusion: Alice should be prescribed an antiviral.

**(b) Difference:**

| | Forward Chaining | Backward Chaining |
|---|---|---|
| **Direction** | From known facts → derive conclusions | From a goal → find supporting evidence |
| **Trigger** | Data-driven: "what can I conclude from what I know?" | Goal-driven: "what do I need to prove this?" |
| **Inference rule** | Modus Ponens (P, P→Q ⊢ Q) — P is sufficient for Q | Modus Tollens direction — Q is necessary, check if P holds |
| **MYCIN connection** | HOW queries ("How did you conclude X?") | WHY queries ("Why do you need to know X?") |

### 评分标准

| Component | Marks |
|---|---|
| Correct step-by-step forward chaining (show each iteration) | 1.5 |
| Show that new facts enable subsequent rules to fire | 0.5 |
| Clear contrast with backward chaining | 1 |

### 为什么可能考到

- Backward chaining was tested in 2025 Sample. Forward chaining is the complementary reasoning direction and has NEVER been tested.
- The teacher pairs complementary concepts: logic + LNN, vagueness + uncertainty. Forward + backward chaining is a natural pair.
- Lecture W4L1 (MYCIN) teaches both forward and backward chaining with examples and exercises.

### 注意点

- Forward chaining fires ALL rules whose conditions are met at each iteration, then repeats. It does NOT stop after one rule fires.
- New facts derived in one iteration can enable NEW rules in the next iteration. Show this cascading effect.
- Do NOT say forward chaining uses Modus Tollens. It uses Modus Ponens.

---

## 2.7 MYCIN CF Computation

### 题目

**[2 marks]:** A MYCIN rule states:

IF Stain = gram-positive (CF = 0.9) AND Shape = coccus (CF = 0.6) THEN Identity = Staphylococcus (CF_rule = 0.7)

Compute the CF of the conclusion. Show each step.

### 详细解答

**Step 1 — Compute the CF of the conjunctive premise using min():**

\\[
\text{CF}(\text{premise}) = \min(\text{CF}(\text{Stain}), \text{CF}(\text{Shape})) = \min(0.9, 0.6) = 0.6
\\]

The weakest link principle: the premise is only as confident as the least certain condition.

**Step 2 — Multiply by the rule CF:**

\\[
\text{CF}(\text{conclusion}) = \text{CF}(\text{premise}) \times \text{CF}(\text{rule}) = 0.6 \times 0.7 = \mathbf{0.42}
\\]

**Interpretation:** The system is 42% confident that the bacterium is Staphylococcus. The low confidence results from moderate evidence for Shape (only 0.6) combined with a rule that is itself only 70% reliable.

### 评分标准

| Component | Marks |
|---|---|
| Correctly apply min() for AND premises | 1 |
| Correctly multiply premise CF by rule CF | 1 |

### 为什么可能考到

- MYCIN CF computation is taught in W4L1 with worked examples. It has never been directly tested as a computation question.
- The CF computation parallels LNN computation (which IS tested every time). The teacher may want to test a different numerical reasoning framework.
- The min() vs multiplication distinction is a classic pitfall that tests understanding.

### 注意点

- For AND conditions: use min(), NOT multiplication. CF(A AND B) = min(CF(A), CF(B)).
- Then multiply the min result by CF(rule). These are TWO DIFFERENT operations — do not mix them up.
- CF is NOT a probability. It ranges from -1 to 1. Do not call it "probability" in your answer.
- Common wrong approach: multiplying all CFs together (0.9 x 0.6 x 0.7 = 0.378). This is WRONG.

---

## 2.8 NEAT Speciation

### 题目

**[2 marks]:**

**(a)** Why does NEAT use speciation? What problem does it solve? [1 mark]

**(b)** Write the formula NEAT uses to measure the distance between two genomes. [1 mark]

### 详细解答

**(a)** When a network receives a new structural mutation (e.g., a new hidden node is added), it almost always performs **worse initially** because the new node has random, unoptimized weights. If this network must compete directly against well-tuned simpler networks in the general population, it will be eliminated immediately — before its new structure has time to prove its worth.

**Speciation solves this by grouping structurally similar networks into "species."** Networks compete primarily within their own species, not against the entire population. This gives structurally novel networks time to optimize their weights over several generations before facing broader competition. It **protects innovation**.

**(b)** The compatibility distance between two genomes:

\\[
\delta = \frac{c_1 \cdot E}{N} + \frac{c_2 \cdot D}{N} + c_3 \cdot \bar{W}
\\]

Where:
- E = number of **excess genes** (beyond the range of the other genome)
- D = number of **disjoint genes** (within range but not matching)
- \\(\bar{W}\\) = average **weight difference** of matching genes
- N = number of genes in the larger genome
- \\(c_1, c_2, c_3\\) = coefficients that tune relative importance

Two genomes belong to the same species if \\(\delta < \delta_t\\) (a threshold).

### 评分标准

| Component | Marks |
|---|---|
| Explain the problem (novel structures eliminated prematurely) and the solution (intra-species competition) | 1 |
| Write the correct compatibility distance formula with all terms defined | 1 |

### 为什么可能考到

- NEAT is covered in W6L1 with speciation as a major concept. GA appeared on the 2025 Real test (fitness function), so the evolutionary computation topic is fair game.
- Speciation is a distinctive, memorable concept — perfect for a "why" question.
- The formula is precise and testable.

### 注意点

- The key word is "protect innovation." Use this phrase.
- E (excess) and D (disjoint) are different: excess genes are beyond the maximum innovation number of the other genome; disjoint genes are within range but unmatched.
- Do not confuse speciation with selection. Speciation groups organisms; selection chooses who reproduces.

---

## 2.9 AdaBoost Mechanism

### 题目

**[2 marks]:** Explain how AdaBoost works. In particular, explain:

**(a)** How does AdaBoost adjust training data between iterations? [1 mark]

**(b)** How does AdaBoost determine the weight of each weak learner in the final ensemble? [1 mark]

### 详细解答

**(a)** AdaBoost trains a sequence of **weak learners** (classifiers slightly better than random guessing). After each weak learner is trained, the algorithm **increases the weight of misclassified examples** and decreases the weight of correctly classified examples. This forces the next weak learner to focus on the "hard" examples that previous learners got wrong.

The effect is that each successive weak learner specializes in correcting the mistakes of its predecessors.

**(b)** The weight (vote) of each weak learner in the final ensemble is determined by its accuracy:

\\[
\alpha_t = \frac{1}{2} \ln \frac{1 - \varepsilon_t}{\varepsilon_t}
\\]

where \\(\varepsilon_t\\) is the weighted error rate of weak learner \\(t\\).

- If \\(\varepsilon_t\\) is small (high accuracy), \\(\alpha_t\\) is large → this learner gets a strong vote.
- If \\(\varepsilon_t\\) is close to 0.5 (barely better than random), \\(\alpha_t\\) is close to 0 → this learner gets almost no vote.
- If \\(\varepsilon_t > 0.5\\) (worse than random), \\(\alpha_t\\) is negative → this learner's predictions are inverted.

The final prediction is a **weighted vote** of all weak learners.

### 评分标准

| Component | Marks |
|---|---|
| Explain re-weighting of misclassified examples | 1 |
| Explain learner weighting formula and its meaning | 1 |

### 为什么可能考到

- Boosting is covered in W4L2 alongside bagging. Bagging/Random Forest has been tested in 3 of 4 papers. Boosting is the complementary ensemble method and has never been tested.
- The teacher likes contrast questions. Bagging vs Boosting is a natural comparison.

### 注意点

- Bagging trains models in **parallel** on independent bootstrap samples. Boosting trains models **sequentially**, each one focusing on previous errors. Do not confuse them.
- AdaBoost weak learners must be better than random (error < 0.5). If error ≥ 0.5, the algorithm stops.
- The final prediction is a WEIGHTED vote, not a simple majority vote.

---

## 2.10 RAG (Retrieval-Augmented Generation)

### 题目

**[2 marks]:** Explain what Retrieval-Augmented Generation (RAG) is and how it relates to Knowledge Graphs.

### 详细解答

**RAG** is a technique that combines information retrieval with large language model (LLM) generation to produce more accurate, grounded responses.

**The pipeline:**

1. **Query:** The user asks a question.
2. **Retrieve:** The system searches a knowledge base (such as a Knowledge Graph, document collection, or vector database) to find relevant facts and passages.
3. **Augment:** The retrieved information is included as context in the LLM's input prompt.
4. **Generate:** The LLM generates a response that is grounded in the retrieved evidence, not just its parametric memory.

**Connection to Knowledge Graphs:** A KG can serve as the retrieval source in RAG. When a user asks a factual question, the system retrieves relevant triples from the KG (e.g., (Einstein, bornIn, Germany)), feeds them to the LLM as context, and the LLM produces a fluent, factually grounded answer.

**Key benefit:** RAG reduces **hallucination** — the LLM is less likely to make up facts because it has access to verified external knowledge at inference time.

**Critical distinction:** RAG does NOT train or fine-tune the model. It operates at **inference time** only, providing context to an already-trained model.

### 评分标准

| Component | Marks |
|---|---|
| Explain the RAG pipeline (retrieve then generate) | 1 |
| Connect to KG and explain the benefit (reduces hallucination, grounded responses) | 1 |

### 为什么可能考到

- RAG is mentioned in the KG lectures (W3L2) as a modern application of Knowledge Graphs.
- It connects two course topics (KG + AI systems) and is highly topical in 2026.
- The teacher might test whether students understand the difference between training and inference-time augmentation.

### 注意点

- Do NOT say RAG "trains" or "fine-tunes" the model. RAG retrieves information and provides it as context at inference time.
- RAG is not specific to KGs — it can retrieve from any knowledge source. But in this course, the KG connection is the relevant angle.

---

## 2.11 Brooks' "Elephants Don't Play Chess"

### 题目

**[2 marks]:** Explain Rodney Brooks' argument in "Elephants Don't Play Chess" (1990). What was his criticism of mainstream AI, and what alternative did he propose?

### 详细解答

Brooks argued that mainstream AI had its priorities **backwards**. The AI community was building chess players, theorem provers, and expert systems — focusing on "elite" intellectual tasks. Brooks pointed out that evolution tells a different story:

- Evolution spent **billions of years** producing organisms that could move, sense obstacles, avoid predators, find food, and survive in dynamic physical environments.
- Only in the last **tiny fraction** of evolutionary time did abstract reasoning appear.
- Yet AI researchers started with abstract reasoning and assumed that perception and locomotion would be "easy add-ons."

**Brooks' alternative:** Build AI **upward from situated competence**, not downward from symbolic reasoning. Study how a cockroach navigates a kitchen floor before studying how a professor plays chess. The cockroach's problem — real-time sensor processing, robust motor control, instant adaptation to a changing world — is arguably the harder and more fundamental problem.

**Design implication:** This led to the **layered control (subsumption) architecture** — simple behavior layers stacked on top of each other, no central planner, no symbolic world model.

### 评分标准

| Component | Marks |
|---|---|
| Explain the criticism (AI focused on elite tasks, not basic competence) with the evolutionary argument | 1 |
| Explain the alternative (build upward from situated competence, layered control) | 1 |

### 为什么可能考到

- This is a foundational philosophical position from W6L1. It motivates every robot example in the lecture.
- The teacher may want to test whether students understand the "why" behind embodied AI, not just the robots.
- A 2-mark "explain the philosophy" question is simple to write and grade.

### 注意点

- The argument is about PRIORITIES, not about chess being unimportant. Brooks is saying: solve basic competence FIRST.
- The key word is "situated" — intelligence that is grounded in physical interaction with the environment.
- Do not describe specific robots here unless the question asks. Focus on the argument.

---

## 2.12 Decision Tree vs Random Forest Trade-off

### 题目

**[2 marks]:** Compare a single decision tree with a Random Forest. Under what circumstances would you prefer each?

### 详细解答

| Aspect | Single Decision Tree | Random Forest |
|---|---|---|
| **Interpretability** | High — you can read the tree and trace every decision. Can be converted to IF-THEN rules. | Low — hundreds of trees combined into a black box. No single readable explanation. |
| **Accuracy** | Lower — prone to overfitting, high variance | Higher — ensemble averaging reduces variance significantly |
| **Speed (training)** | Fast | Slower (must train many trees) |
| **Speed (inference)** | Fast (single tree traversal) | Slower (traverse all trees, aggregate) |
| **Overfitting risk** | High (especially deep trees) | Low (bagging + feature subsampling reduce variance) |

**When to prefer a single decision tree:**
- When **explainability is legally or ethically required** (e.g., medical diagnosis, loan approval — you must explain WHY a decision was made)
- When the dataset is small and a complex ensemble would overfit
- When inference speed is critical (real-time systems)

**When to prefer Random Forest:**
- When **accuracy is the primary goal** and you can tolerate a black-box model
- When the dataset is large enough that overfitting is a real risk for single trees
- When you want robustness to noisy or missing features

### 评分标准

| Component | Marks |
|---|---|
| Identify key differences (interpretability, accuracy, overfitting) | 1 |
| Give appropriate scenarios for when to use each | 1 |

### 为什么可能考到

- Feature bagging has been tested 3 times. CART greedy has been tested once. A higher-level "compare" question is a natural escalation.
- The teacher likes contrast/trade-off questions ("while A focuses on..., B is designed to...").

### 注意点

- Do NOT say Random Forest is "always better." The trade-off with interpretability is real and important.
- Random Forest uses BAGGING (parallel, independent trees) not boosting (sequential).
- Each tree in a Random Forest sees a random subset of FEATURES at each split, not just a random subset of data.

---

---

# Section 3: Cross-Topic Combination Questions

These questions combine concepts from different lectures. The teacher has not done this yet, but as the exam matures and difficulty increases, cross-topic questions become likely.

---

## 3.1 Backward Chaining (MYCIN) vs Bayesian Reasoning (Naive Bayes) for Medical Diagnosis

### 题目

**[3 marks]:** Compare how MYCIN (using backward chaining with confidence factors) and a Naive Bayes classifier would approach diagnosing a patient. Discuss at least two differences in their reasoning approach.

### 详细解答

| Aspect | MYCIN (Backward Chaining + CF) | Naive Bayes |
|---|---|---|
| **Knowledge source** | Hand-crafted IF-THEN rules from human experts. Rules like: "IF gram-negative AND rod-shaped AND anaerobic THEN Bacteroides (CF=0.6)" | Learned from data. The model computes P(Disease\|Symptoms) from a training set of patient records |
| **Reasoning direction** | **Goal-driven (backward)**: starts with a hypothesis ("Is it Bacteroides?") and works backward to check if the evidence supports it | **Data-driven**: takes all observed symptoms as input and computes posterior probability for each disease simultaneously |
| **Uncertainty handling** | Uses **Confidence Factors** (CF): CF(conclusion) = min(CF(premises)) x CF(rule). CFs are NOT probabilities — they range from -1 to 1 and represent expert belief | Uses **probabilities** grounded in Bayes' theorem: P(D\|S) = P(S\|D)P(D)/P(S). Probabilities must be consistent (sum to 1) |
| **Explainability** | Highly explainable: the system can trace its reasoning chain and answer "WHY did you ask me about the stain?" or "HOW did you conclude Bacteroides?" | Less explainable: the model outputs a probability but the reasoning is purely mathematical (multiply priors and likelihoods) |
| **Scalability** | Does not scale well: requires a human expert to hand-craft every rule. MYCIN had ~200 rules and took years to build | Scales with data: give it more patient records and it learns better, no expert needed |

### 评分标准

| Component | Marks |
|---|---|
| Correctly describe MYCIN's reasoning approach (backward chaining, CF, expert rules) | 1 |
| Correctly describe Naive Bayes approach (data-driven, probabilistic) | 1 |
| Identify at least 2 meaningful differences | 1 |

### 为什么可能考到

- MYCIN and Bayesian reasoning are both taught as approaches to medical diagnosis (W4L1, W5L1). Comparing them tests synthesis across lectures.
- The teacher rewards "contrast" answers that show understanding of trade-offs.

### 注意点

- Do NOT say CFs and probabilities are the same thing. The teacher explicitly distinguishes them.
- MYCIN uses BACKWARD chaining (goal-driven), not forward chaining. Get the direction right.
- Naive Bayes assumes feature INDEPENDENCE. MYCIN rules can capture dependencies through rule structure.

---

## 3.2 LNN and Fuzzy Logic — How Are They Related?

### 题目

**[2 marks]:** An LNN uses fuzzy membership values as inputs to its logical neurons. How does this combine ideas from both Logic Neural Networks and Fuzzy Logic? What are the differences?

### 详细解答

**Similarities:**
- Both use **continuous truth values** in [0, 1] rather than binary True/False.
- Both define **soft operators** for AND, OR, NOT that generalize Boolean operators to continuous inputs.
- Both can represent concepts with "degrees of truth" — e.g., "this patient is 0.7 high-risk."

**Key differences:**

| Aspect | Fuzzy Logic | LNN |
|---|---|---|
| **Rule creation** | Rules and membership functions are **designed by human experts** | Rules and weights can be **learned from data** via gradient descent |
| **Differentiability** | Typically NOT differentiable. Membership functions are fixed. | Specifically designed to be **differentiable** so backpropagation works |
| **Architecture** | Standalone rule system with membership functions | A **neural network** whose architecture mirrors the logical formula — each logical operation is a neuron |
| **Bounds** | Produces single truth values | Can compute **upper and lower bounds** on truth values, expressing the range of possible truth |

**How they combine:** An LNN can take fuzzy membership values as inputs (from fuzzy sensors or fuzzy preprocessing) and then perform differentiable logical reasoning on those values. The fuzzy stage handles "how much does x belong to category C?" and the LNN stage handles "given these degrees of membership, what can we logically conclude?" The LNN adds the ability to learn and to express bounded uncertainty on top of the fuzzy inputs.

### 评分标准

| Component | Marks |
|---|---|
| Identify shared features (continuous truth values, soft operators) | 1 |
| Identify key differences (learning vs fixed, differentiable, bounds) | 1 |

### 为什么可能考到

- Both LNN and Fuzzy Logic use continuous truth values, and students frequently confuse them (the teacher notes this as a common misconception in lecture materials).
- Testing the distinction forces students to understand each concept at a deeper level.

### 注意点

- Do NOT say "LNN is just fuzzy logic in a neural network." The bounds and differentiability are fundamental differences.
- LNN has a specific neural architecture derived from logical structure. Fuzzy logic does not have this.
- Fuzzy membership values are not probabilities, and they are not LNN truth value bounds. All three are different concepts.

---

## 3.3 GA-Evolved Robot Soccer Strategy

### 题目

**[3 marks]:** A robot soccer team wants to use a Genetic Algorithm to evolve its team strategy. Describe:

**(a)** What would the chromosome represent? [1 mark]

**(b)** What would the fitness function measure? [1 mark]

**(c)** Describe a suitable selection and crossover method. [1 mark]

### 详细解答

**(a) Chromosome representation:**

Each chromosome encodes a set of **strategy parameters** for the entire team. For example:

- Aggression level (0.0 to 1.0): how far forward the team plays
- Passing threshold: minimum open-field distance before attempting a pass
- Defensive formation width: how spread out defenders are
- Shot distance threshold: maximum distance from goal at which a player attempts a shot
- Role assignment weights: probability of each player being attacker/midfielder/defender

The chromosome could be a vector of real numbers: [0.7, 15.0, 3.5, 20.0, 0.3, 0.5, 0.2], where each position corresponds to one parameter.

**(b) Fitness function:**

\\[
F = w_1 \cdot \text{GoalsScored} - w_2 \cdot \text{GoalsConceded} + w_3 \cdot \text{PossessionTime} + w_4 \cdot \text{ShotsOnTarget}
\\]

The fitness function aggregates over a simulated match (or series of matches). Higher fitness = better team performance. Key components:
- Goals scored (most important — this is the objective)
- Goals conceded (penalty — a good defense matters)
- Possession time and shots on target (secondary indicators of quality play)

Fitness should be evaluated over **multiple matches** against different opponents to avoid overfitting to one opponent's style.

**(c) Selection and crossover:**

**Selection — Tournament selection (k=3):** Randomly pick 3 chromosomes, the one with the highest fitness wins and enters the mating pool. Repeat until the mating pool is full. Tournament selection is simple and provides good selection pressure.

**Crossover — Uniform crossover:** For each gene (strategy parameter), flip a coin to decide whether to take from Parent A or Parent B. This allows mixing of individual strategy components from both parents, which is more flexible than single-point crossover for real-valued chromosomes.

### 评分标准

| Component | Marks |
|---|---|
| Reasonable chromosome representation with specific parameters | 1 |
| Fitness function that measures match performance with multiple components | 1 |
| Appropriate selection method and crossover method with brief justification | 1 |

### 为什么可能考到

- Robot soccer appears in 3 of 4 past papers (Q4, 2-mark descriptive question). A harder, design-oriented version combining GA + robot soccer tests both topics simultaneously.
- GA fitness function design was tested in 2025 Real. Combining it with the robot soccer scenario is natural.
- The teacher likes "design" questions — "Design a fitness function for..." is a signature prompt.

### 注意点

- The chromosome encodes STRATEGY PARAMETERS, not individual moves. A chromosome is a complete strategy that governs behavior throughout a match.
- The fitness function should be evaluated over MULTIPLE matches to be robust. State this.
- Do NOT say the GA finds the "optimal" strategy. Say "good" or "high-performing."

---

## 3.4 Knowledge Graph vs Decision Tree for Car Diagnosis

### 题目

**[3 marks]:** Compare how a Knowledge Graph and a Decision Tree might be used to diagnose car problems. What are the trade-offs?

### 详细解答

**Knowledge Graph approach:**

Build a KG with triples representing car domain knowledge:
- (Engine, hasPart, SparkPlug)
- (SparkPlug, canCause, MisfireSound)
- (MisfireSound, symptomOf, IgnitionProblem)
- (LowOilPressure, leadTo, EngineKnocking)

**Diagnosis process:** Given symptoms, traverse the graph backward from symptom nodes to find possible causes. Use reasoning/inference rules or graph embedding (TransE) to predict missing links.

**Decision Tree approach:**

Build a tree from historical repair data:
- Root: "Is the engine making unusual noise?" (Yes/No)
- If Yes: "Is the oil light on?" (Yes/No)
- And so on until a diagnosis leaf is reached.

**Trade-offs:**

| Aspect | Knowledge Graph | Decision Tree |
|---|---|---|
| **Knowledge source** | Expert-curated relationships + ontology | Learned from historical repair data |
| **Explainability** | Can trace reasoning path through relationships | Can trace decision path through tree |
| **Handling new problems** | Can reason about new entity combinations (compositional reasoning) | Cannot diagnose problems not represented in training data |
| **Data requirement** | Needs domain expert to build the graph | Needs labeled training data (symptom to diagnosis pairs) |
| **Multiple diagnoses** | Naturally supports multiple possible causes (multiple paths) | Each input reaches exactly one leaf (single diagnosis) |
| **Maintenance** | Easy to update (add new triples) | Must retrain entire tree when new data arrives |

**When to use KG:** When domain expertise is available, when the system must explain its reasoning in terms of causal relationships, and when the problem space is complex with many interacting components.

**When to use Decision Tree:** When abundant historical data exists, when fast inference is needed, and when the diagnostic process follows a clear sequential questioning pattern.

### 评分标准

| Component | Marks |
|---|---|
| Describe KG-based diagnosis approach | 1 |
| Describe Decision Tree-based diagnosis approach | 1 |
| Identify meaningful trade-offs (at least 2) | 1 |

### 为什么可能考到

- KG (Q3) and Decision Trees (Q4/Q5) are both guaranteed topics. Comparing them in an applied scenario tests synthesis.
- The teacher values "trade-off" analysis — this is a signature question style.

### 注意点

- KG approach is based on structured RELATIONSHIPS. Decision tree approach is based on DATA-DRIVEN SPLITS.
- Both are explainable, but in different ways: KG explains via relationships, DT explains via decision path.
- Do not claim one is universally better. State the scenarios where each excels.

---

---

# Section 4: Vagueness vs Uncertainty — Extended Scenarios

This topic appears in 3 of 4 papers and the format is always the same. Here are additional practice scenarios beyond the 4 that have been tested.

---

## 4.1 Extended Classification Practice

### 题目

**[4 marks]:** For each scenario, state whether it is an example of vagueness or uncertainty. Justify your answer in one sentence.

**(a)** A self-driving car's sensor detects an object ahead and needs to determine whether it is a pedestrian or a trash can.

**(b)** A wine critic describes a bottle as "an almost outstanding vintage."

**(c)** An earthquake early warning system has detected seismic waves and must predict whether a major earthquake will follow within the next 30 seconds.

**(d)** A university describes a student's performance as "satisfactory."

### 详细解答

**(a) Uncertainty.** The object either IS a pedestrian or it IS NOT — there is a definite fact about the world. The sensor has incomplete information (limited resolution, partial occlusion), so the system must infer the true state from noisy evidence. An all-knowing oracle could immediately tell you what the object is.

**(b) Vagueness.** "Almost outstanding" is a graded concept with no sharp boundary. Even if you know everything about the wine (every chemical compound, every flavor note), the label "almost outstanding" remains inherently blurry — it is a matter of degree, not a factual question. An all-knowing oracle would say "it depends on where you draw the line between outstanding and not."

**(c) Uncertainty.** Either a major earthquake will occur in the next 30 seconds or it will not — this is a factual event with a definite (but currently unknown) outcome. The system uses incomplete seismic data to estimate the probability. Once the 30 seconds pass, the uncertainty resolves.

**(d) Vagueness.** "Satisfactory" is a graded label with no precise boundary. Is a C+ satisfactory? What about a C? What about a B-? Even knowing the exact GPA, the concept "satisfactory" remains fuzzy. The tool to handle this is fuzzy logic (degree of membership in the set "satisfactory").

### 评分标准

| Component | Marks |
|---|---|
| (a) Correct classification + justification | 1 |
| (b) Correct classification + justification | 1 |
| (c) Correct classification + justification | 1 |
| (d) Correct classification + justification | 1 |

### 为什么可能考到

- This exact format (4 scenarios, 1 mark each) appears in 3 of 4 past papers. The scenarios change but the format is constant.
- Having practiced more scenarios beyond the 4 tested ones gives you pattern recognition for any new scenario.

### 注意点

- Use the **Oracle Test**: If an all-knowing oracle could give a definitive yes/no answer, it is uncertainty. If even an oracle would say "depends on your definition," it is vagueness.
- Adjectives without precise definitions (tall, fast, satisfactory, almost excellent) are almost always vagueness.
- Questions about factual states (is it X? will Y happen? what is it?) are almost always uncertainty.
- A scenario can involve a NUMBER and still be vagueness (e.g., "74 is almost excellent" — the number is precise, but the label is vague).

---

---

# Section 5: Quick-Fire Recall Questions (1--2 Mark Style)

These are high-probability short-answer questions that could appear as sub-parts of larger questions.

---

## 5.1 Polly's Design Principle

### 题目

**[1 mark]:** What was the key design principle behind Polly the robot?

### 详细解答

"Do not solve the hardest possible vision problem if the environment lets you solve an easier one." Polly exploited environment-specific constraints (uniform carpet, predictable corridor geometry, fixed camera height) to avoid general-purpose computer vision. Instead of recognizing objects, it detected carpet — anything that was NOT carpet was an obstacle.

### 为什么可能考到

- Polly is a specific, memorable example from W6L1. The design principle encapsulates the entire embodied AI philosophy in one sentence.

---

## 5.2 Allen's Layered Control

### 题目

**[1 mark]:** Name the three behavior layers in Allen (Brooks, 1986) from lowest to highest.

### 详细解答

- **Level 0: Avoid** — obstacle avoidance using distance sensors (repulsive force inversely proportional to distance)
- **Level 1: Wander** — pick a random heading, follow it for ~10 seconds
- **Level 2: Explore** — steer toward the most wide-open space

Key insight: All layers run **simultaneously** and their forces **combine**. Higher layers do not replace lower layers.

### 为什么可能考到

- Allen is the canonical example of subsumption architecture from the lectures. The three layers are clean, memorizable facts.

---

## 5.3 Joint Persistent Goal (STEAM)

### 题目

**[2 marks]:** What is a Joint Persistent Goal (JPG) in the STEAM framework? What is the critical communication requirement?

### 详细解答

A JPG is a shared commitment by a team to pursue a goal until one of three conditions is met:

1. **Achieved** — the goal has been accomplished
2. **Unachievable** — the goal is now impossible
3. **Irrelevant** — the goal no longer matters

**Critical communication requirement:** If any agent determines that one of these three conditions holds, it must **communicate this to the entire team** before withdrawing. The agent does NOT simply act alone — it shares its knowledge so the team can coordinate.

This solves the "brittle team plan" problem (Tambe, 1997): without STEAM, if a scout helicopter is destroyed, the rest of the team waits forever for data that will never come. With STEAM, any agent that recognizes the goal is unachievable broadcasts this information.

### 为什么可能考到

- STEAM/JPG is a specific, testable concept from W6L1 multi-agent systems. The three exit conditions (A, U, I) and the communication rule are precise, exam-friendly facts.
- Multi-agent systems appear in 3 of 4 papers. Expanding beyond "robot soccer strategies" to STEAM is a natural progression.

---

## 5.4 Why is CART Greedy? (Refined Full-Marks Answer)

### 题目

**[2 marks]:** What exactly is meant by saying CART is "greedy"?

### 详细解答

At each node of the decision tree, starting from the root, the algorithm assesses the potential impurity reduction for splitting the training data on each available feature (and for every possible split point for numeric features). The best-performing split is selected **without any look-ahead**. That is the greedy part — there is no effort to craft an optimal tree overall, just a locally optimal decision regarding the current split. The algorithm is then recursively invoked on each resulting sub-tree.

*(Source: 2025 Real Test official answer)*

### 为什么可能考到

- Tested on 2025 Real (2 marks). Could appear again since the marking rubric is very specific.
- Key phrases the examiner wants: (1) evaluates all possible splits, picks maximum impurity reduction (2) **without any look-ahead**.

### 注意点

- Saying only "picks the best split" = 1 mark. You MUST add "without look-ahead" for full marks.

---

## 5.5 Feature Bagging in Random Forest (Refined Full-Marks Answer)

### 题目

**[3 marks]:**

**(a)** In a Random Forest, how does each tree select features for splitting? [2 marks]

**(b)** Why is this beneficial? [1 mark]

### 详细解答

**(a)** At each split point in each tree, the algorithm randomly selects a **subset** of the available features (typically \\(\sqrt{p}\\) features for classification, where p is the total number of features). It then evaluates only these selected features and picks the best split among them. This random feature selection is done **independently at every split** in every tree — so different trees see different features at different nodes.

Additionally, each tree is trained on a **bootstrap sample** (random sample with replacement) of the training data. This is the "bagging" part.

**(b)** This is beneficial because it **reduces correlation between trees** in the ensemble. If all trees see all features, they would all tend to pick the same best feature at the root, making them highly correlated. Averaging correlated predictions does not reduce variance much. By forcing each tree to consider only a random subset of features, the trees make different splits, become diverse, and their averaged prediction has **lower variance** (less overfitting) than any individual tree.

### 为什么可能考到

- This exact question appeared in 3 of 4 past papers (2025 Sample Q5, 2026 Sample Q5). It is the most likely repeat question.

### 注意点

- Feature selection happens at EVERY SPLIT, not just once at the beginning.
- The key benefit is DECORRELATION of trees leading to variance reduction. Not just "each tree is different."
- Random Forest = Bagging + Feature subsampling. Both components matter.

---

---

# Summary: Top 15 Predictions Ranked by Likelihood

| Rank | Question | Topic | Risk Level | Rationale |
|---|---|---|---|---|
| 1 | Feature bagging (how + why) | Random Forest | GUARANTEED | Appeared 3/4 papers, same format |
| 2 | Vagueness vs Uncertainty (4 scenarios) | Soft Computing | GUARANTEED | Appeared 3/4 papers, same format |
| 3 | Modus Tollens deduction | Symbolic Logic | GUARANTEED | Appeared 4/4 papers |
| 4 | LNN numerical computation | LNN | GUARANTEED | Appeared 4/4 papers |
| 5 | FOL quantifier negation | Symbolic Logic | GUARANTEED | Appeared 4/4 papers |
| 6 | TransE principle + scoring function | KG | GUARANTEED | Appeared 4/4 papers |
| 7 | Entropy / Information Gain computation | Decision Trees | HIGH RISK | Heavily taught, never tested |
| 8 | Naive Bayes classification | Soft Computing | HIGH RISK | Canonical example in lectures, never tested |
| 9 | Forward chaining | MYCIN | HIGH RISK | Only backward tested; forward is complement |
| 10 | MYCIN CF computation | Expert Systems | HIGH RISK | Taught with exercises, never tested |
| 11 | Reynolds' 3 flocking rules | Multi-Agent | HIGH RISK | Same lecture as robot soccer, never tested |
| 12 | AdaBoost mechanism | Ensemble Methods | MEDIUM RISK | Complement to bagging (which IS tested) |
| 13 | NEAT speciation | Evolutionary Comp. | MEDIUM RISK | GA tested once; speciation is key NEAT concept |
| 14 | TransE limitations / TransH | KG | MEDIUM RISK | Deeper KG question beyond basic formula |
| 15 | Brooks' philosophy | Embodied AI | MEDIUM RISK | Motivational lecture content, clean 2-mark question |

---

> **Final note:** Prioritize guaranteed topics first (items 1--6). Once those are solid, study high-risk items 7--11 — these are the most likely source of surprise questions. Items 12--15 are lower priority but still possible. Do not walk into the exam having studied ONLY the guaranteed topics.
