# Real Exam Question Bank -- Sorted by Topic

> This chapter organizes **every question from all 4 past papers** by topic, so you can study all related questions together. Each entry includes the original question, step-by-step solution from official answer keys, mark allocation, and common pitfalls.
>
> **Papers covered:**
> | Code | Paper | Total | Year |
> |------|-------|-------|------|
> | P1 | Sample Test S1 2025 | 15 marks | 2025 |
> | P2 | Real Mid-Semester Test S1 2025 | 15 marks | 2025 |
> | P3 | Sample Test S1 2026 | 20 marks | 2026 |
> | P4 | (Answer keys for P1/P2/P3) | -- | -- |

---

## Topic A: Symbolic Logic -- Propositional Logic (Modus Tollens)

> Appears in: **ALL papers (100%)** -- the single most important topic.

---

### 真题 A.1 -- 2025 Sample Test Q1(a) [1 mark]

**原题：**
> In a secure facility, a person is granted entry only if they provide both a valid ID and a fingerprint match.
>
> Let the propositions be: I: The person has a valid ID. F: The fingerprint matches. E: The person is granted entry.
>
> The rule is logically expressed as: (I ∧ F) → E
>
> Today, we observed that the person was not granted entry.
>
> Use propositional logic to deduce what must be true about P and Q. Show your steps clearly. **[1 mark]**

**详细解析：**

Step 1: Identify the given information.
- Rule: (I ∧ F) → E
- Observation: ¬E (the person was NOT granted entry)

Step 2: Apply Modus Tollens.
- Modus Tollens states: if P → Q and ¬Q, then ¬P.
- Here P = (I ∧ F), Q = E.
- From (I ∧ F) → E and ¬E, we deduce ¬(I ∧ F).

Step 3: Apply De Morgan's Law.
- ¬(I ∧ F) = ¬I ∨ ¬F
- Meaning: the person either did not have a valid ID, or the fingerprint did not match, or both.

**标准答案：**
> Given: (I ∧ F) → E and ¬E.
> By Modus Tollens: ¬(I ∧ F).
> By De Morgan's Law: ¬I ∨ ¬F.
> Conclusion: The person either did not have a valid ID or the fingerprint did not match (or both).

**评分标准：**
- 1 mark: Correctly applying Modus Tollens and De Morgan's Law to reach ¬I ∨ ¬F.

**注意点 / 易错点：**
- ⚠️ This is worth only 1 mark in P1 but **3 marks in P3 (真题 A.3)** for the same scenario -- in P3 you must also draw the truth table.
- ⚠️ Do NOT just write the conclusion without showing the inference steps.
- ⚠️ De Morgan's for AND: ¬(A ∧ B) = ¬A ∨ ¬B. Do not confuse with OR version.

---

### 真题 A.2 -- 2025 Real Mid-Semester Q1(a) [1 mark]

**原题：**
> In a smart office, the alarm system is governed by the following rule: "If the door is open or the motion sensor is triggered, then the alarm will sound."
>
> Let the propositions be: P: The door is open. Q: The motion sensor is triggered. R: The alarm sounds.
>
> The rule is logically expressed as: **(P ∨ Q) → R**
>
> Today, you observed that the alarm did not sound.
>
> Use propositional logic to deduce what must be true about P and Q. Show your steps clearly. **[1 mark]**

**详细解析：**

Step 1: Identify the given information.
- Rule: (P ∨ Q) → R
- Observation: ¬R (the alarm did NOT sound)

Step 2: Apply Modus Tollens.
- From (P ∨ Q) → R and ¬R, we deduce ¬(P ∨ Q).

Step 3: Apply De Morgan's Law (for OR).
- ¬(P ∨ Q) = ¬P ∧ ¬Q
- Meaning: the door was NOT open AND the motion sensor was NOT triggered.

**标准答案：**
> Given: (P ∨ Q) → R and ¬R.
> By Modus Tollens: ¬(P ∨ Q).
> By De Morgan's Law: ¬P ∧ ¬Q.
> Therefore, the door was not open and the motion sensor was not triggered.

**评分标准：**
- 1 mark: Complete chain from Modus Tollens through De Morgan's to conclusion.

**注意点 / 易错点：**
- ⚠️ **Critical difference from 真题 A.1**: here the connective is OR (∨), so De Morgan's gives ¬P **∧** ¬Q (both must be false). In A.1 it was AND (∧), giving ¬I **∨** ¬F (at least one is false).
- ⚠️ Many students confuse the two De Morgan's Laws:
  - ¬(A ∧ B) = ¬A ∨ ¬B
  - ¬(A ∨ B) = ¬A ∧ ¬B
- ⚠️ The conclusion here is **stronger** (both definitely false) vs A.1 (at least one false).

---

### 真题 A.3 -- 2026 Sample Test Q1(a) [3 marks]

**原题：**
> (Same scenario as A.1) In a secure facility, a person is granted entry only if they provide both a valid ID and a fingerprint match. (I ∧ F) → E. Today, we observed that the person was not granted entry.
>
> Use propositional logic to deduce what must be true about P and Q. Show your steps (Truth Table) clearly. **[3 marks]**

**详细解析：**

Step 1: Since ¬E, and (I ∧ F) → E is true, construct a truth table for the implication.

| X (= I ∧ F) | E | X → E |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | **0** |
| 1 | 1 | 1 |

Step 2: Since the rule (I ∧ F) → E is true, and E = 0, the only valid row is X = 0, E = 0. Therefore I ∧ F = 0. [1 mark for truth table + identifying the valid row]

Step 3: Now construct the truth table for I ∧ F to see when it equals 0.

| I | F | I ∧ F |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Step 4: I ∧ F = 0 in three of four rows. So I or F (or both) must be 0. [1 mark for second truth table]

Step 5: Conclusion: The person either did not have a valid ID or the fingerprint did not match (or both). [1 mark]

**标准答案：**
> [Draw both truth tables as shown above]
>
> From truth table 1: since the rule is true and E = 0, then (I ∧ F) must be 0.
> From truth table 2: I ∧ F = 0 means I = 0 or F = 0 (or both).
> Conclusion: The person either did not have a valid ID or the fingerprint did not match (or both).

**评分标准：**
- 1 mark: Truth table for implication X → E, identifying that X must be 0 when E = 0
- 1 mark: Truth table for I ∧ F, showing when it equals 0
- 1 mark: Correct natural-language conclusion

**注意点 / 易错点：**
- ⚠️ Compare with 真题 A.1: **same scenario, same answer**, but here you MUST show truth tables for full marks. In A.1 (1 mark) you could just write the Modus Tollens chain.
- ⚠️ The question says "Show your steps (Truth Table)" -- do NOT just use Modus Tollens without a table, or you will lose marks.
- ⚠️ You need TWO tables: one for the implication, one for the conjunction.

---

## Topic B: Symbolic Logic -- First-Order Logic (FOL)

> Appears in: **ALL papers (100%)** -- always paired with propositional logic in Q1.

---

### 真题 B.1 -- 2025 Sample Test Q1(b) [2 marks]

**原题：**
> A biologist claims: "Not all birds in this region can fly."
>
> Let the domain be all birds in this region, and Fly(x) means bird x can fly.
>
> (i) Write this claim in formal first-order logic. **[1 mark]**
> (ii) Provide a realistic example (in one sentence) that would make the statement true. **[1 mark]**

**详细解析：**

Step 1 (Part i): "Not all birds can fly" = it is NOT the case that for all x, Fly(x).
- In FOL: ¬∀x Fly(x)
- Equivalently (by quantifier negation): ∃x ¬Fly(x) -- "there exists a bird that cannot fly"

Step 2 (Part ii): Give a concrete counterexample.
- Penguins are birds but cannot fly.

**标准答案：**
> (i) ¬∀x Fly(x)
> (ii) "There is a penguin in this region, and penguins cannot fly."

**评分标准：**
- 1 mark: Correct FOL notation (either ¬∀x Fly(x) or ∃x ¬Fly(x))
- 1 mark: A valid real-world example

**注意点 / 易错点：**
- ⚠️ Both ¬∀x Fly(x) and ∃x ¬Fly(x) are accepted. They are logically equivalent.
- ⚠️ Do NOT write ∀x ¬Fly(x) -- that means "no birds can fly", which is too strong.
- ⚠️ The example must be realistic. "A penguin" or "an ostrich" or "a kiwi" are all fine.
- ⚠️ Compare with 真题 B.3 -- identical question, also worth 2 marks.

---

### 真题 B.2 -- 2025 Real Mid-Semester Q1(b) [1 mark]

**原题：**
> At a university, the disciplinary policy states: "Every student who cheats in the exam will be disqualified from the course."
>
> Let: Cheat(x): student x cheats. Disqualified(x): student x is disqualified.
>
> This rule is represented in first-order logic as: **∀x (Cheat(x) → Disqualified(x))**
>
> You are told: Student Alice is not disqualified.
>
> Based on the rule and the observed fact, use first-order logic to determine whether Alice cheated. Show your reasoning. **[1 mark]**

**详细解析：**

Step 1: Universal Instantiation.
- From ∀x (Cheat(x) → Disqualified(x)), instantiate for Alice:
- Cheat(Alice) → Disqualified(Alice)

Step 2: Apply Modus Tollens.
- Given: ¬Disqualified(Alice)
- From Cheat(Alice) → Disqualified(Alice) and ¬Disqualified(Alice):
- Conclude: ¬Cheat(Alice)

Step 3: Conclusion.
- Alice did not cheat.

**标准答案：**
> From the universal rule ∀x (Cheat(x) → Disqualified(x)), instantiate for Alice:
> Cheat(Alice) → Disqualified(Alice)
> Given: ¬Disqualified(Alice)
> Apply Modus Tollens: ¬Cheat(Alice)
> Conclusion: Alice did not cheat.

**评分标准：**
- 1 mark: Correct application of universal instantiation followed by Modus Tollens.

**注意点 / 易错点：**
- ⚠️ You MUST mention **universal instantiation** (going from ∀x to a specific constant Alice) -- this is a key FOL step that distinguishes it from propositional logic.
- ⚠️ This question combines FOL with Modus Tollens. It tests whether you know how to bridge the gap between quantified statements and inference rules.
- ⚠️ Do NOT say "Alice might or might not have cheated" -- the logic is definitive here.

---

### 真题 B.3 -- 2026 Sample Test Q1(b) [2 marks]

**原题：**
> (Same as 真题 B.1) A biologist claims: "Not all birds in this region can fly." Fly(x) means bird x can fly.
>
> (i) Write this claim in formal first-order logic. **[1 mark]**
> (ii) Provide a realistic example. **[1 mark]**

**详细解析：**
Identical to 真题 B.1. See above for full solution.

**标准答案：**
> (i) ¬∀x Fly(x)
> (ii) "There is a penguin in this region, and penguins cannot fly."

**评分标准：**
- 1 mark: Correct FOL
- 1 mark: Valid example

**注意点 / 易错点：**
- ⚠️ This is a **repeated question** from P1 -- the examiner clearly considers this a core competency.
- ⚠️ Same pitfalls as 真题 B.1: do NOT write ∀x ¬Fly(x).

---

## Topic C: Logic Neural Networks (LNN)

> Appears in: **ALL papers (100%)** -- mark weight trending upward (2 → 3 → 4).

---

### 真题 C.1 -- 2025 Sample Test Q2(a) [1 mark]

**原题：**
> A smart home system uses a Logic Neural Network (LNN) to determine whether to turn on the heating system. The decision rule is: "If it is cold and someone is at home, then the heating system should be turned on."
>
> This rule is encoded logically as: HeatingOn ← Cold ⊗ AtHome
>
> (a) What does this rule represent in natural language, and how is it different from a standard Boolean rule? **[1 mark]**

**详细解析：**

Step 1: Natural language interpretation.
- "If it is cold and someone is at home, then turn on the heating system."

Step 2: Difference from Boolean logic.
- In standard Boolean logic, both inputs must be strictly True (1) to activate the heating. There is no middle ground.
- In an LNN, the ⊗ operator allows soft conjunction over continuous truth values. It supports partial inputs (like 0.4 or 0.9), yielding an intermediate activation that reflects uncertainty and permits gradient-based learning.

**标准答案：**
> This rule can be read as: "If it is cold and someone is at home, then turn on the heating system."
>
> In standard Boolean logic, this would require both inputs to be strictly True (1) to turn on the heating.
>
> In an LNN, the ⊗ operator allows soft conjunction over continuous truth values. It supports partial inputs (like 0.4 or 0.9), yielding an intermediate activation that reflects uncertainty and permits gradient-based learning.

**评分标准：**
- 1 mark: Natural language meaning + clear explanation of how LNN differs from Boolean (continuous vs binary).

**注意点 / 易错点：**
- ⚠️ You must mention BOTH the natural language meaning AND the difference. Just stating one is not enough.
- ⚠️ Key phrase to include: "continuous truth values" or "soft conjunction" or "partial inputs".
- ⚠️ Compare with 真题 C.3 -- same question but worth 2 marks (more detail expected).

---

### 真题 C.2 -- 2025 Sample Test Q2(b) [1 mark]

**原题：**
> Suppose the network receives the following inputs: Cold = 0.9, AtHome = 0.4.
>
> Explain how the LNN would likely compute the truth value of HeatingOn, and whether the system would activate heating or not. (You may answer qualitatively; exact numerical output is not required.) **[1 mark]**

**详细解析：**

Step 1: Apply soft-logic AND (product t-norm).
- HeatingOn = Cold ⊗ AtHome = 0.9 * 0.4 = 0.36

Step 2: Discuss threshold-based decision.
- Whether the heating is activated depends on the classification threshold.
- If the threshold is low (e.g., 0.3), heating will be turned on.
- If the threshold is high (e.g., 0.7), heating will stay off.

**标准答案：**
> Using soft-logic AND (e.g., Product-Sum), the output HeatingOn will reflect the multiplication of the two values, approx. 0.9 * 0.4 = 0.36.
>
> Depending on the classification threshold, the system may or may not trigger the heating. If the threshold is low (e.g., 0.3), heating will be turned on. If it's high (e.g., 0.7), it may stay off.

**评分标准：**
- 1 mark: Showing a reasonable computation (product or Lukasiewicz) + mentioning the role of the threshold.

**注意点 / 易错点：**
- ⚠️ The question says "qualitatively" -- you do not need exact numbers, but showing the calculation helps.
- ⚠️ Two t-norms are acceptable: Product (a * b = 0.36) or Lukasiewicz (max(0, a+b-1) = max(0, 0.3) = 0.3).
- ⚠️ You MUST mention the threshold. Just computing 0.36 without discussing activation is incomplete.
- ⚠️ Compare with 真题 C.4 -- same question but worth 2 marks.

---

### 真题 C.3 -- 2026 Sample Test Q2(a) [2 marks]

**原题：**
> (Same scenario as C.1) HeatingOn ← Cold ⊗ AtHome
>
> (a) What does this rule represent in natural language, and how is it different from a standard Boolean rule? **[2 marks]**

**详细解析：**
Same content as 真题 C.1, but with 2 marks you need more detail.

**标准答案：**
> This rule can be read as: "If it is cold and someone is at home, then turn on the heating system." [1 mark]
>
> In standard Boolean logic, this would require both inputs to be strictly True (1) to turn on the heating. In an LNN, the ⊗ operator allows soft conjunction over continuous truth values. It supports partial inputs (like 0.4 or 0.9), yielding an intermediate activation that reflects uncertainty and permits gradient-based learning. [1 mark]

**评分标准：**
- 1 mark: Correct natural language interpretation
- 1 mark: Clear explanation of difference (Boolean = binary; LNN = continuous, differentiable, supports partial truth values)

**注意点 / 易错点：**
- ⚠️ With 2 marks, write more than for C.1. Explicitly mention "gradient-based learning" or "differentiable" for full marks.
- ⚠️ Same core content as 真题 C.1 but examiner expects a more thorough comparison.

---

### 真题 C.4 -- 2026 Sample Test Q2(b) [2 marks]

**原题：**
> Suppose the network receives the following inputs: Cold = 0.9, AtHome = 0.4.
>
> Explain how the LNN would likely compute the truth value of HeatingOn, and whether the system would activate heating or not. **[2 marks]**

**详细解析：**
Same computation as 真题 C.2, but with 2 marks you need to be more explicit.

**标准答案：**
> Using soft-logic AND (e.g., Product-Sum), HeatingOn = 0.9 * 0.4 = 0.36. [1 mark]
>
> Depending on the classification threshold, the system may or may not trigger the heating. If the threshold is low (e.g., 0.3), heating will be turned on. If it's high (e.g., 0.7), it may stay off. [1 mark]

**评分标准：**
- 1 mark: Correct computation showing soft-AND result
- 1 mark: Discussion of threshold and its effect on the decision

**注意点 / 易错点：**
- ⚠️ Same as 真题 C.2 but write more. Show the actual multiplication and discuss both threshold scenarios.

---

### 真题 C.5 -- 2025 Real Mid-Semester Q2(a) [1 mark]

**原题：**
> In a Logic Neural Network (LNN), each logical formula is associated with a lower bound (L) and an upper bound (U), which indicate how confident the model is about the truth of the formula. Consider the example below:
>
> An autonomous vehicle is using an LNN to decide whether to trigger a collision alert based on two observed conditions:
> - P: "The object is very close" (L_P = 0.8, U_P = 0.9)
> - Q: "The object is moving fast" (L_Q = 0.3, U_Q = 0.6)
>
> The LNN rule for triggering an alert is: Alert ← P ∨ Q
>
> The system uses a classification threshold of α = 0.7:
> - If L ≥ α → definitely true
> - If U < α → definitely false
> - If L < α < U → uncertain
>
> (a) Based on the threshold α = 0.7, is the alert status: A. definitely true, B. definitely false, C. uncertain? (Choose one; no proof is required.) **[1 mark]**

**详细解析：**

Step 1: Compute bounds for OR.
- For OR (disjunction), the bounds are:
  - L_Alert = max(L_P, L_Q) = max(0.8, 0.3) = 0.8
  - U_Alert = max(U_P, U_Q) = max(0.9, 0.6) = 0.9

Step 2: Compare with threshold α = 0.7.
- L_Alert = 0.8 ≥ α = 0.7
- Therefore: **A. Definitely true**

**标准答案：**
> L_Alert = max(L_P, L_Q) = max(0.8, 0.3) = 0.8
> U_Alert = max(U_P, U_Q) = max(0.9, 0.6) = 0.9
> Since 0.7 = α < 0.8 = L_Alert, the classification is: **A. Definitely true**

**评分标准：**
- 1 mark: Correct answer (A. Definitely true).

**注意点 / 易错点：**
- ⚠️ OR bounds use **max** for both lower and upper bounds. This is different from AND bounds.
- ⚠️ The question says "no proof is required" but showing the computation is good practice.
- ⚠️ Do NOT confuse the threshold comparison: it is L ≥ α that gives "definitely true", not U ≥ α.
- ⚠️ This is a **different type of LNN question** compared to C.1-C.4 (bounds-based vs product t-norm). Be prepared for both.

---

### 真题 C.6 -- 2025 Real Mid-Semester Q2(b) [2 marks]

**原题：**
> Why is using bounds (instead of just a single probability) beneficial in safety-critical applications such as autonomous driving? **[2 marks]**

**详细解析：**

The official answer accepts ANY TWO of the following four reasons:

1. **Expressing Uncertainty Explicitly**: Bounds allow the system to represent how confident it is in a truth value.

2. **Supporting Conservative Decision-Making**: In safety-critical tasks (like autonomous driving), erring on the side of caution is crucial. If the lower bound is below the threshold, the system might wait or slow down rather than take action. This avoids risky decisions based on overconfident estimates.

3. **Robustness to Noisy or Incomplete Data**: Sensors may fail or provide noisy signals. Bounds propagate uncertainty from inputs to outputs, allowing the system to track how uncertain the final decision is.

4. **Better Interpretability**: Engineers and operators can inspect bounds to understand how certain the model is about a decision. This improves debugging, transparency, and trust in the AI system.

**标准答案：**
> (Any two of the following for full marks)
> 1. Bounds express uncertainty explicitly, showing how confident the system is.
> 2. They support conservative decision-making -- if the lower bound is below the threshold, the system can err on the side of caution rather than making overconfident decisions.
> 3. They provide robustness to noisy or incomplete data by propagating uncertainty through the reasoning chain.
> 4. They improve interpretability -- engineers can inspect bounds to understand model confidence.

**评分标准：**
- 1 mark per valid reason, maximum 2 marks.

**注意点 / 易错点：**
- ⚠️ You need **two distinct reasons**, not just one reason explained at length.
- ⚠️ Always tie your answer back to "safety-critical" -- generic answers about bounds are weaker.
- ⚠️ Good keywords: "conservative", "overconfident", "noisy sensors", "interpretability", "transparency".

---

## Topic D: Knowledge Graphs / TransE

> Appears in: **ALL papers (100%)** -- always exactly 2 marks.

---

### 真题 D.1 -- 2025 Sample Test Q3 [2 marks]

**原题：**
> What is the role of entity and relation embeddings in knowledge graph completion? Introduce a common Knowledge Graph Inference task and provide one example of how such embeddings help in a typical KG task. **[2 marks]**

**详细解析：**

Step 1: Role of embeddings.
- Knowledge Graph Embeddings (KGE) represent entities and relations as dense vectors in a continuous space. Instead of treating each symbol independently, embedding methods map them into a continuous, low-dimensional space where semantic relationships can be captured numerically.

Step 2: Common inference tasks.
- Link prediction: Predicting missing links such as (h, r, ?) or (?, r, t)
- Relation prediction: Predicting missing relations such as (h, ?, t)

Step 3: Example.
- Given embeddings of entities and relations, the model might discover that: (Einstein, bornIn, ?) → Germany, even if this triple was not originally present in the KG.

**标准答案：**
> Knowledge Graph Embeddings (KGE) represent entities and relations as dense vectors in a continuous space. These embeddings allow models to predict missing links, validate facts, and reason over structured knowledge. [1 mark]
>
> Common inference tasks: Link prediction (h, r, ?) or (?, r, t), and Relation prediction (h, ?, r). Example: the model might discover (Einstein, bornIn, ?) → Germany even if this triple was not in the KG. [1 mark]

**评分标准：**
- 1 mark: Explaining what embeddings are and their role (dense vectors, continuous space)
- 1 mark: Naming an inference task + giving a concrete example

**注意点 / 易错点：**
- ⚠️ You must give a **concrete example** (with actual entities), not just describe the task abstractly.
- ⚠️ This is the "general" version of the KG question. Compare with 真题 D.2 which asks specifically about TransE.
- ⚠️ Same question appears in 真题 D.3 (P3).

---

### 真题 D.2 -- 2025 Real Mid-Semester Q3 [2 marks]

**原题：**
> (a) Briefly explain how a translation-based embedding model such as TransE learns representations for entities and relations in a knowledge graph. **[1 mark]**
>
> (b) What is the basic idea behind TransE's scoring function? **[1 mark]**

**详细解析：**

Part (a): TransE explanation.
- TransE is a translation-based embedding model that represents **entities and relations as vectors in the same space**.
- It assumes that for a valid triple (h, r, t), the embedding of the tail entity t should be **close to** the embedding of the head entity h plus the relation vector r.
- i.e., h + r ≈ t

Part (b): Scoring function.
- TransE defines a distance-based score: f(h, r, t) = ||h + r - t||_{L1/L2}
- The **smaller** the score, the **more likely** the triple is true.

**标准答案：**
> (a) TransE is a translation-based embedding model that represents entities and relations as vectors in the same space. For a valid triple (h, r, t), it assumes h + r ≈ t. [1 mark]
>
> (b) Scoring function: f(h, r, t) = ||h + r - t||. The smaller the score, the more likely the triple is true. [1 mark]

**评分标准：**
- 1 mark (a): Explain TransE as translation-based, entities/relations as vectors, h + r ≈ t
- 1 mark (b): Write the scoring function and state "smaller = more likely"

**注意点 / 易错点：**
- ⚠️ You MUST write the formula h + r ≈ t for part (a).
- ⚠️ You MUST write the scoring function f(h,r,t) = ||h + r - t|| for part (b).
- ⚠️ You MUST state "smaller score = more likely true" -- this is the key insight.
- ⚠️ This is the "specific" version. If the question asks about TransE, you need the formula. If it asks about "embeddings in general" (like D.1), you can be more general.

---

### 真题 D.3 -- 2026 Sample Test Q3 [2 marks]

**原题：**
> What is the role of entity and relation embeddings in knowledge graph completion? Introduce a common Knowledge Graph Inference task and provide one example of how such embeddings help in a typical KG task. **[2 marks]**

**详细解析：**
Identical to 真题 D.1. See above for full solution.

**标准答案：**
> (Same as D.1)

**评分标准：**
- 1 mark: Role of embeddings
- 1 mark: Inference task + example

**注意点 / 易错点：**
- ⚠️ **Exact repeat** of 真题 D.1. This question is clearly a template the examiner re-uses.
- ⚠️ Be prepared for BOTH versions: general (D.1/D.3) and TransE-specific (D.2).

---

## Topic E: Decision Trees & Random Forests (Feature Bagging)

> Feature bagging appears in: **3 of 3 distinct papers (100%)**. CART greedy appears in: **1 paper (P2)**.

---

### 真题 E.1 -- 2025 Sample Test Q5(a) [2 marks]

**原题：**
> You're trying to predict the 1-month change in value for a stock based on a set of 225 different features (aspects of the company, its products and market conditions). You're going to use a random forest with feature bagging to make the estimate.
>
> (a) Describe how the bagging algorithm selects features for any given tree. **[2 marks]**

**详细解析：**

Step 1: Explain feature sampling.
- A random subset of the features would be sampled for any given tree in the random forest.
- The typical sample size is the square root of the total features: sqrt(225) = 15 features per tree.
- Anything substantially less than 225 could be OK.

Step 2: Explain sampling method.
- Typically, a large number of trees are produced (e.g., 2048).
- Features would be selected as a **random sample, with replacement**, of size much less than 225.

**标准答案：**
> A random subset of features would be sampled for any given tree in the random forest. Square-root of the total features was given as an example sample size, so sampling 15 features (sqrt(225)) per tree would be a great choice; but anything substantially less than 225 could be OK. Typically, a large number of trees are produced (e.g., 2048), so we'd need to sample with replacement. So, features would be selected as a random sample, with replacement, of size << 225.

**评分标准：**
- 1 mark: Random subset of features per tree, mentioning sqrt(n) as a guideline
- 1 mark: Sampling with replacement, size much less than total features

**注意点 / 易错点：**
- ⚠️ You MUST mention **sqrt(n)** or give the specific number 15 = sqrt(225).
- ⚠️ You MUST mention **with replacement**.
- ⚠️ Do NOT confuse feature bagging with data bagging (bootstrap aggregating of samples).
- ⚠️ Same question appears in 真题 E.3 (P3) -- identical.

---

### 真题 E.2 -- 2025 Sample Test Q5(b) [1 mark]

**原题：**
> (b) Why is feature bagging considered a good idea? **[1 mark]**

**详细解析：**

The core reason: Without feature bagging, a single strong feature tends to be selected as the root of most trees (even on random subsets of the data), making the trees **highly correlated**. Feature bagging makes the trees in the forest **less correlated** and more able to complement one another as an ensemble.

**标准答案：**
> Feature bagging is a solution to trees being highly-correlated, for instance due to a single strong feature being selected as the root of most trees (even on random subsets of the data). So, feature bagging is considered to be a good idea because it makes the trees in the forest less correlated and more able to complement one another as an ensemble.

**评分标准：**
- 1 mark: Explaining that it reduces correlation between trees / increases diversity.

**注意点 / 易错点：**
- ⚠️ The key phrase is **"less correlated"** or **"decorrelates the trees"**. This is what the examiner wants.
- ⚠️ Do NOT just say "it improves accuracy" -- you must explain the mechanism (reducing correlation).
- ⚠️ Mentioning that a dominant feature would otherwise always be chosen as root is a strong answer.
- ⚠️ Same question appears in 真题 E.4 (P3) -- identical.

---

### 真题 E.3 -- 2026 Sample Test Q5(a) [2 marks]

**原题：**
> (Same as E.1) Describe how the bagging algorithm selects features for any given tree. **[2 marks]**

**详细解析：**
Identical to 真题 E.1. See above.

**标准答案：**
> (Same as E.1)

---

### 真题 E.4 -- 2026 Sample Test Q5(b) [1 mark]

**原题：**
> (Same as E.2) Why is feature bagging considered a good idea? **[1 mark]**

**详细解析：**
Identical to 真题 E.2. See above.

---

### 真题 E.5 -- 2025 Real Mid-Semester Q4 [2 marks]

**原题：**
> CART is a recursive algorithm for decision tree induction driven by impurity reduction.
>
> What exactly is meant by saying CART is 'greedy'? **[2 marks]**

**详细解析：**

The answer must emphasize the concept of **no look-ahead**.

Step 1: At each node, starting from the root, the algorithm assesses the potential impurity reduction for splitting the training data on each available feature (and for every possible split point for numeric features).

Step 2: The best-performing split is selected **without any look-ahead**. That is the greedy part -- there is no effort to craft an optimal tree overall, just a maximal local decision regarding the current split.

Step 3: The algorithm is then recursively invoked on each resulting sub-tree.

**标准答案：**
> At each node, starting from the root, the algorithm assesses the potential impurity reduction for splitting the training data on each available feature (and for every possible split point for numeric features). The best-performing split is selected **without any look-ahead** -- that's the greedy part -- there is no effort to craft an optimal tree overall, just a maximal local decision regarding the current split. The algorithm is then recursively invoked on each resulting sub-tree.

**评分标准：**
- 2 marks: Full explanation with "no look-ahead" / "no effort to craft optimal tree overall"
- 1 mark: Answers that mentioned maximizing impurity reduction but did NOT mention the lack of looking ahead (with 1/2 point variance depending on what else was said)

**注意点 / 易错点：**
- ⚠️ **CRITICAL**: You MUST say "no look-ahead" or "no effort to craft an optimal tree overall" for full marks. The official answer key explicitly states that answers missing this received only 1/2 marks.
- ⚠️ "Greedy" does NOT just mean "picks the best split" -- it means picks the best split **locally, without considering future consequences**.
- ⚠️ This is a conceptual understanding question. The examiner wants to see that you understand the difference between greedy and globally optimal approaches.

---

## Topic F: Multi-Agent Systems (Robot Soccer)

> Appears in: **3 of 3 distinct papers (100%)** -- always exactly 2 marks.

---

### 真题 F.1 -- 2025 Sample Test Q4 [2 marks]

**原题：**
> Consider a robot soccer league where the rules allow all robots to access an overhead camera view of the field (so, they know the position of all teammates, opponents and the ball), but they cannot send signals (other than visual signals) to teammates.
>
> Describe one strategy or collective behaviour that can be effective under these conditions. **[2 marks]**

**详细解析：**

The official answer accepts any of the following strategies (1 mark each, max 2):

1. **Collective behaviours** (e.g., a passing strategy):
   - Suitable passing points extracted from interception prediction
   - Each passing point assigned a value based on its position
   - Plenty of room for optimization of such value assessment

2. **Positioning strategies**:
   - Choosing a formation on the field that yields good attack and defense opportunities

3. **Role-based strategies**:
   - Choose a role for each player based on game situation

The key justification: Since all robots can access an overhead camera view in this league, they could all assess the game situation, attack/defense opportunities and suitable passing points on the **same information**. So, any of these behaviours/strategies appear feasible and useful.

**标准答案：**
> (Any of the following, with justification)
>
> **Passing strategy**: All robots share the overhead camera view, so they can independently calculate suitable passing points by predicting interception paths. Each passing point can be assigned a value based on field position. Since all robots compute on the same information, they can coordinate without explicit communication.
>
> OR: **Formation/positioning**: Robots can adopt formations (e.g., attack vs defense) based on the shared game state.
>
> OR: **Role assignment**: Each robot assigns itself a role (attacker, defender, goalkeeper) based on its position relative to the ball and teammates.

**评分标准：**
- 1 mark per valid strategy described, maximum 2 marks.
- Must explain WHY it works given the constraints (shared perception, no signals).

**注意点 / 易错点：**
- ⚠️ You MUST justify why the strategy works **under these specific conditions** (overhead camera = shared perception).
- ⚠️ The key insight: since all robots see the same information, they can independently reach the same conclusions about what to do -- no explicit communication needed.
- ⚠️ Do NOT describe strategies that require sending signals to teammates.
- ⚠️ Same question in 真题 F.2 (P2) and F.3 (P3) -- identical.

---

### 真题 F.2 -- 2025 Real Mid-Semester (Not present -- Q4 was CART greedy in P2)

> Note: Robot soccer did NOT appear in the 2025 Real Mid-Semester Test. Q4 in P2 was about CART greedy (see 真题 E.5). This means robot soccer appeared in 2/3 papers (P1 and P3).

---

### 真题 F.3 -- 2026 Sample Test Q4 [2 marks]

**原题：**
> (Same as F.1) Consider a robot soccer league... Describe one strategy or collective behaviour. **[2 marks]**

**详细解析：**
Identical to 真题 F.1. See above.

---

## Topic G: Soft Computing -- Vagueness vs Uncertainty

> Appears in: **1 paper (P3, 2026 Sample)** -- 4 marks. A unique question type.

---

### 真题 G.1 -- 2026 Sample Test Q6 [4 marks]

**原题：**
> For each of the following situations, state whether it is mainly an example of **vagueness or uncertainty**. Then, briefly justify your answer in 1-2 sentences.
>
> 1. A doctor says: "This patient is high risk."
> 2. A security system reports that an alarm has gone off, and we want to know whether there is actually a burglary.
> 3. A teacher says: "A student with a mark of 74 is almost excellent."
> 4. An email filter must decide whether a new email is spam, based on incomplete evidence such as suspicious words and many links.

**详细解析：**

The distinction:
- **Vagueness**: The concept itself has blurry/graded boundaries. There is no sharp cutoff. The real state is known, but the label is inherently fuzzy.
- **Uncertainty**: The real state of the world is unknown. We are trying to infer a definite fact from incomplete evidence.

1. **Vagueness** -- "high risk" has blurry boundaries; it is a matter of degree rather than a yes/no fact.
2. **Uncertainty** -- the real state of the world is unknown; we are uncertain whether a burglary actually happened.
3. **Vagueness** -- "almost excellent" is a graded concept with no sharp boundary.
4. **Uncertainty** -- the system is inferring an unknown class from evidence, which is a probabilistic reasoning problem.

**标准答案：**
> 1. **Vagueness** -- "high risk" has blurry boundaries; it is a matter of degree rather than a yes/no fact. [1 mark]
> 2. **Uncertainty** -- the real state of the world is unknown; we are uncertain whether a burglary actually happened. [1 mark]
> 3. **Vagueness** -- "almost excellent" is a graded concept with no sharp boundary. [1 mark]
> 4. **Uncertainty** -- the system is inferring an unknown class from evidence, which is a probabilistic reasoning problem. [1 mark]

**评分标准：**
- 1 mark per scenario: correct label + brief justification.

**注意点 / 易错点：**
- ⚠️ **The most common mistake**: confusing scenarios 1 and 2, or 3 and 4.
- ⚠️ Rule of thumb: if the problem is about a **graded/fuzzy label** (high risk, almost excellent), it is **vagueness**. If the problem is about **inferring an unknown fact** (was there a burglary? is it spam?), it is **uncertainty**.
- ⚠️ Vagueness is about the **definition** being fuzzy. Uncertainty is about the **world state** being unknown.
- ⚠️ Scenario 4 is tricky: "suspicious words" might seem vague, but the core question is "is this email spam?" which is a binary fact we are uncertain about.

---

## Topic H: Soft Computing -- Fuzzy Logic vs Traditional Logic

> Appears in: **1 paper (P2, 2025 Real)** -- 3 marks.

---

### 真题 H.1 -- 2025 Real Mid-Semester Q5 [3 marks]

**原题：**
> Consider a rule that uses the attributes STRONG and HEAVY that assesses suitability of an individual for the Olympic sport of hammer throwing:
>
> IF STRONG AND HEAVY THEN HAMMER_THROWER
>
> Contrast how the above rule might work using traditional logic as compared to Fuzzy Logic. **[3 marks]**

**详细解析：**

**Traditional Logic approach:**
- Both STRONG and HEAVY would be either True or False (by some criteria, like how much they can benchpress, or the athlete's weight in kg).
- If, and only if, both criteria are true, then the individual is judged to be suitable for hammer throwing; else, not.
- Binary outcome: suitable or not suitable.

**Fuzzy Logic approach:**
- Fuzzy Set Theory can be applied to both STRONG and HEAVY.
- Some level of strength performance will map to a membership value μ_s in [0,1].
- Some bodyweight will map to a membership value μ_h in [0,1].
- The AND function might be implemented as min(μ_s, μ_h) or the product μ_s * μ_h (there are other options, such as the Yager operator).
- The THEN might have a strength of 1.0, or something less as a further multiplier.
- The final result is a **suitability score for hammer throwing anywhere in the range [0,1]**.

**标准答案：**
> **Traditional Logic**: Both STRONG and HEAVY are binary True/False. If and only if both are true, the individual is suitable. Otherwise not. Binary decision.
>
> **Fuzzy Logic**: STRONG and HEAVY each get a membership value in [0,1]. The AND is computed as min(μ_s, μ_h) or product. The result is a graded suitability score in [0,1], not a binary yes/no.

**评分标准：**
- 1 mark: Correct description of traditional logic (binary True/False, both must be true)
- 1 mark: Correct description of fuzzy logic (membership values in [0,1], graded output)
- 1 mark: Clear contrast / AND function explanation (min or product)

**注意点 / 易错点：**
- ⚠️ You MUST describe BOTH approaches, not just one.
- ⚠️ Mention specific AND operators: min(μ_s, μ_h) or product. Just saying "fuzzy uses degrees" is not enough for full marks.
- ⚠️ Emphasize the key contrast: binary output vs continuous output in [0,1].
- ⚠️ The Yager operator is a bonus mention but not required.

---

## Topic I: MYCIN / Backward Chaining

> Appears in: **1 paper (P1, 2025 Sample)** -- 3 marks.

---

### 真题 I.1 -- 2025 Sample Test Q6 [3 marks]

**原题：**
> Both forward and backward chaining are useful in medical diagnosis, where a doctor decides what is likely to be wrong with a patient based on symptoms and observations. A patient might initially volunteer to the doctor one symptom, e.g. a runny nose, which could be due to the common cold. But runny nose can also be due to allergies (in which case the patient may have a history of allergies) or measles (where the patient develops a distinctive rash).
>
> In the context of these six concepts (runny nose, history of allergies, rash, common cold, allergies and measles) describe an instance of backward chaining reasoning for a patient with a runny nose. **[3 marks]**

**详细解析：**

Step 1: Understand backward chaining.
- Backward chaining starts with a **goal** (a hypothesis/diagnosis) and then works backward to find supporting evidence in terms of symptoms.
- This is different from forward chaining, which starts with observations and derives conclusions.

Step 2: Apply to the scenario.
- The goal is to decide what is wrong with the patient.
- We start with one of the possible diagnoses and find support for it in terms of symptoms.

Three valid backward chaining paths:

**Path 1 -- Support 'common cold':**
- Start with hypothesis: the patient has a common cold.
- Check: does the patient have a runny nose? Yes.
- Conclusion: common cold is supported. (We've got all we need.)

**Path 2 -- Support 'measles':**
- Start with hypothesis: the patient has measles.
- Check: does the patient have a runny nose? Yes.
- But we also need: does the patient have a distinctive rash?
- We'd need to find out if they have a rash.

**Path 3 -- Support 'allergies':**
- Start with hypothesis: the patient has allergies.
- Check: does the patient have a runny nose? Yes.
- But we also need: does the patient have a history of allergies?
- We'd need to find out if they have such a history.

**标准答案：**
> Backward chaining starts with a goal (diagnosis) and finds support for it in terms of symptoms. We have three valid options:
>
> 1. Support 'common cold' -- we've got all we need, as the patient has said they have a runny nose.
> 2. Support 'measles' -- we have runny nose, but we'd also have to find out if they have a distinctive rash.
> 3. Support 'allergies' -- we have runny nose, but we'd also have to find out if they have a history of allergies.
>
> None of these rules would have 100% confidence. The doctor would need to consider the risk of being wrong and the prevalence of each condition.

**评分标准：**
- 1 mark: Explaining that backward chaining starts with a goal/hypothesis
- 1 mark: Showing at least one valid backward chaining path
- 1 mark: Showing awareness that additional evidence may be needed (e.g., rash for measles)

**注意点 / 易错点：**
- ⚠️ Do NOT describe forward chaining (starting from symptoms and concluding). The question specifically asks for **backward** chaining.
- ⚠️ You must use the six concepts given: runny nose, history of allergies, rash, common cold, allergies, measles.
- ⚠️ Mentioning that confidence is not 100% shows deeper understanding (MYCIN-style reasoning).
- ⚠️ The key phrase: "start with one of the problems and find support for it in terms of symptoms."

---

## Topic J: Genetic Algorithms (Fitness Function Design)

> Appears in: **1 paper (P2, 2025 Real)** -- 3 marks.

---

### 真题 J.1 -- 2025 Real Mid-Semester Q6 [3 marks]

**原题：**
> You've been asked to program a genetic algorithm (GA) to train the controller for the legs of a walking robot like Big Dog.
>
> Your inputs will include the desired speed and direction of the robot, as well as the target height (e.g., standing tall, or crouched low). The algorithm will have access to the speed, direction, height and angle (i.e., 'attitude' -- pitch, yaw and roll) of the robot's body from the prior time step.
>
> Name the elements that should be part of the fitness function for the GA. You don't need to write a complete equation; just describe the key terms that would contribute to the sum of the fitness score. **[3 marks]**

**详细解析：**

Step 1: Understand the goal.
- A fitness function in a GA dictates the suitability of an individual to pass their genome onto the next generation.
- The fitness should measure how well the robot achieves the desired movement.

Step 2: Identify key elements.
- Difference of target speed to actual speed: |target_speed - actual_speed|
- Difference of target direction to actual direction: |target_direction - actual_direction|
- Difference of target height to actual height: |target_height - actual_height|
- Maintaining pitch, yaw and roll within acceptable bounds (stability penalties)

Step 3: Combine.
- The highest fitness score would be attained where all the above differences are low.
- The fitness function might put a minus sign in front of each absolute value (or square) summed over observations during a simulation run.
- Fitness = -(|speed_error| + |direction_error| + |height_error| + stability_penalties)

**标准答案：**
> Elements of the fitness function:
> 1. Difference of target speed to actual speed
> 2. Difference of target direction to actual direction
> 3. Difference of target height to actual height
> 4. Maintaining pitch, yaw and roll within acceptable bounds
>
> The highest fitness score would be attained where all the above differences are low across a simulation run. So, the fitness function might put a minus sign in front of absolute value (or square) of each, summed over observations during the simulation run.

**评分标准：**
- 1 mark per relevant fitness element mentioned (up to 3 marks)
- Mentioning the negative/minimization aspect is a bonus but not strictly required

**注意点 / 易错点：**
- ⚠️ You do NOT need to write a formal equation -- just describe the elements.
- ⚠️ Do NOT forget the **stability terms** (pitch, yaw, roll). The question specifically mentions "attitude" -- referring to it earns an easy mark.
- ⚠️ The fitness is a **negative sum** (lower error = higher fitness). Explain this relationship.
- ⚠️ Think about what the robot is TRYING TO DO: match target speed, direction, and height while staying stable.

---

## Cross-Reference Summary Table

| Topic | P1 (2025 Sample) | P2 (2025 Real) | P3 (2026 Sample) |
|---|---|---|---|
| **A. Propositional Logic** | Q1a [1mk] AND→MT | Q1a [1mk] OR→MT | Q1a [3mk] AND→TruthTable |
| **B. First-Order Logic** | Q1b [2mk] ¬∀xFly(x) | Q1b [1mk] ∀x→UI+MT | Q1b [2mk] ¬∀xFly(x) |
| **C. LNN (explain+compute)** | Q2 [2mk] HeatingOn | Q2 [3mk] Alert OR bounds | Q2 [4mk] HeatingOn |
| **D. Knowledge Graphs** | Q3 [2mk] KGE general | Q3 [2mk] TransE specific | Q3 [2mk] KGE general |
| **E. Decision Trees/RF** | Q5 [3mk] Feature bagging | Q4 [2mk] CART greedy | Q5 [3mk] Feature bagging |
| **F. Multi-Agent (Robot Soccer)** | Q4 [2mk] Strategy | -- | Q4 [2mk] Strategy |
| **G. Vagueness vs Uncertainty** | -- | -- | Q6 [4mk] 4 scenarios |
| **H. Fuzzy vs Traditional** | -- | Q5 [3mk] Hammer thrower | -- |
| **I. MYCIN/Backward Chaining** | Q6 [3mk] Runny nose | -- | -- |
| **J. GA Fitness Function** | -- | Q6 [3mk] Big Dog | -- |

---

## Study Priority Based on Frequency

| Priority | Topic | Times Appeared | Study Time |
|---|---|---|---|
| **MUST KNOW** | Propositional Logic (Modus Tollens + De Morgan's) | 3/3 papers | High |
| **MUST KNOW** | First-Order Logic (quantifiers, negation, universal instantiation) | 3/3 papers | High |
| **MUST KNOW** | LNN (explain + compute soft-AND/OR + bounds) | 3/3 papers | High |
| **MUST KNOW** | Knowledge Graphs (general KGE + TransE) | 3/3 papers | Medium |
| **MUST KNOW** | Feature Bagging (how + why) | 3/3 papers | Medium |
| **HIGH** | Multi-Agent (Robot Soccer strategies) | 2/3 papers | Medium |
| **HIGH** | CART Greedy (no look-ahead) | 1/3 papers | Low-Medium |
| **MEDIUM** | Vagueness vs Uncertainty | 1/3 papers | Medium |
| **MEDIUM** | Fuzzy Logic vs Traditional Logic | 1/3 papers | Medium |
| **MEDIUM** | MYCIN / Backward Chaining | 1/3 papers | Medium |
| **MEDIUM** | GA Fitness Function Design | 1/3 papers | Medium |

---

## Key Formulas Cheat Sheet (for handwritten notes page)

```
PROPOSITIONAL LOGIC
  Modus Tollens: P->Q, ¬Q ⊢ ¬P
  De Morgan (AND): ¬(A∧B) = ¬A∨¬B
  De Morgan (OR):  ¬(A∨B) = ¬A∧¬B

FIRST-ORDER LOGIC
  Quantifier negation: ¬∀x P(x) ≡ ∃x ¬P(x)
  Universal instantiation: ∀x P(x) ⊢ P(a)

LNN - Soft Logic Operators
  Product t-norm (AND): a * b
  Lukasiewicz t-norm (AND): max(0, a+b-1)
  OR bounds: L = max(L1, L2), U = max(U1, U2)
  Threshold: L>=a -> definitely true
             U<a  -> definitely false
             else -> uncertain

TRANSE
  h + r ≈ t
  f(h,r,t) = ||h + r - t||    (smaller = more likely)

FEATURE BAGGING
  Sample sqrt(n) features per tree, with replacement
  Why: reduces tree correlation -> better ensemble

CART GREEDY
  Best local split, NO LOOK-AHEAD

VAGUENESS vs UNCERTAINTY
  Vagueness = fuzzy boundary (degree)
  Uncertainty = unknown state (probability)
```
