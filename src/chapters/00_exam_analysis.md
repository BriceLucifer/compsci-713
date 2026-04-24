# Exam Analysis Report — COMPSCI 713 Mid-Term Test

> This chapter analyses **4 past test papers** to identify patterns, predict high-priority topics, and guide your revision strategy.

## Papers Analysed

| # | Paper | Total Marks | Questions | Year |
|---|---|---|---|---|
| 1 | Sample Test S1 2025 | 15 marks | 6 | 2025 |
| 2 | Real Mid-Semester Test S1 2025 | 15 marks | 6 | 2025 |
| 3 | Sample Test S1 2026 | 20 marks | 6 | 2026 |
| 4 | Sample Test S1 2026 — Model Answers | (same as #3) | 6 | 2026 |

---

## Test Format（考试格式）

| Aspect | Detail |
|---|---|
| **Duration** | 60 minutes total (5 min reading + 55 min answering) |
| **Number of questions** | 6 short-answer questions — **attempt ALL** |
| **Total marks** | 15–20 marks |
| **Allowed materials** | Restricted book: **one double-sided page** of handwritten notes |
| **Marking philosophy** | Quality over quantity — concise, clear answers are rewarded |

### Time Budget Recommendation

With 55 minutes for answering and 15–20 marks, you have roughly **3–4 minutes per mark**. For a 3-mark question, aim for about 10 minutes. Do not over-write; the examiner values precision.

---

## Question-by-Question Breakdown（逐题分析）

### Q1 — Symbolic Logic: Propositional Logic + First-Order Logic（命题逻辑 + 一阶逻辑）

**Appears in: ALL 4 papers (100%) — 🔴 必考**

| Paper | Marks | Part (a) | Part (b) |
|---|---|---|---|
| 2025 Sample | 3 | Modus tollens with truth table (1 mk) | FOL: negate ∀x Fly(x) (1 mk) + give example (1 mk) |
| 2025 Real | 2 | Modus tollens with OR / De Morgan's Law (1 mk) | FOL modus tollens with universal instantiation (1 mk) |
| 2026 Sample | 5 | Truth table + modus tollens deduction (3 mk) | FOL: negate ∀x Fly(x) (1 mk) + give example (1 mk) |

**Key Observations:**

- **Modus tollens** is tested in every single paper — this is the most important inference rule to master.
- Part (a) always tests propositional logic manipulation: truth tables, applying inference rules, or simplifying with De Morgan's Law.
- Part (b) always involves First-Order Logic (FOL): translating English into formal notation, or applying quantifier negation (¬∀x P(x) ≡ ∃x ¬P(x)).
- Mark weight is increasing: 3 → 2 → 5 across the three distinct papers.

**What to prepare:**

1. Modus tollens: \\( P \rightarrow Q,\ \neg Q \vdash \neg P \\)
2. Truth table construction for compound propositions
3. De Morgan's Laws: \\( \neg(P \lor Q) \equiv \neg P \land \neg Q \\)
4. FOL quantifier negation: \\( \neg \forall x\, P(x) \equiv \exists x\, \neg P(x) \\)
5. Universal instantiation: from ∀x P(x) derive P(a) for a specific constant a

---

### Q2 — Logic Neural Networks / LNN（逻辑神经网络）

**Appears in: ALL 4 papers (100%) — 🔴 必考**

| Paper | Marks | Part (a) | Part (b) |
|---|---|---|---|
| 2025 Sample | 2 | Natural language interpretation + how LNN differs from Boolean logic (1 mk) | LNN computation with soft-logic AND (1 mk) |
| 2025 Real | 3 | LNN bounds computation for OR with threshold (1 mk) | Why bounds are beneficial in safety-critical applications (2 mk) |
| 2026 Sample | 4 | Natural language interpretation + Boolean difference (2 mk) | LNN numerical computation (2 mk) |

**Key Observations:**

- Two recurring sub-tasks: (1) explain what LNN does in natural language and contrast it with classical Boolean logic, and (2) perform a numerical LNN computation (bounds for AND or OR using soft-logic / t-norms).
- The 2025 Real paper added a deeper "why" question about safety-critical applications — be ready to justify why bounded truth values matter.
- Mark weight is trending upward (2 → 3 → 4).

**What to prepare:**

1. What LNN is and how it differs from Boolean logic (truth values are intervals/bounds, not binary 0/1)
2. Soft-logic AND (t-norm): \\( \text{AND}(a, b) = \max(0,\ a + b - 1) \\) using Lukasiewicz t-norm
3. Soft-logic OR (t-conorm): \\( \text{OR}(a, b) = \min(1,\ a + b) \\)
4. Computing upper and lower bounds given input intervals
5. Why bounded reasoning is useful in safety-critical systems (e.g., medical diagnosis, autonomous driving)

---

### Q3 — Knowledge Graphs / TransE（知识图谱 / TransE）

**Appears in: ALL 4 papers (100%) — 🔴 必考**

| Paper | Marks | Content |
|---|---|---|
| 2025 Sample | 2 | Role of embeddings in KG + inference task + example |
| 2025 Real | 2 | TransE explanation (1 mk) + scoring function (1 mk) |
| 2026 Sample | 2 | Role of embeddings in KG + inference task + example |

**Key Observations:**

- Always exactly 2 marks.
- Two flavours of question: (1) general — explain the role of embeddings in KG reasoning, or (2) specific — explain TransE and its scoring function.
- TransE is the only embedding method that has been tested.

**What to prepare:**

1. What a knowledge graph is: (head, relation, tail) triples
2. Why embeddings are used: map entities and relations to continuous vector space for inference
3. TransE principle: \\( \mathbf{h} + \mathbf{r} \approx \mathbf{t} \\)
4. Scoring function: \\( f(h, r, t) = -\| \mathbf{h} + \mathbf{r} - \mathbf{t} \| \\) (lower distance = more likely true)
5. Link prediction task: given (h, r, ?) predict the missing tail entity
6. A concrete example (e.g., (Auckland, locatedIn, ?) → New Zealand)

---

### Q4 — Variable Topic (2 marks each)

| Paper | Marks | Topic |
|---|---|---|
| 2025 Sample | 2 | Multi-agent: Robot soccer strategy |
| 2025 Real | 2 | Decision Trees: CART greedy algorithm |
| 2026 Sample | 2 | Multi-agent: Robot soccer strategy |

**Key Observations:**

- Robot soccer (multi-agent systems) appears in 3 of 4 papers — describe one strategy for team coordination.
- CART appeared once — explain why decision tree construction is greedy and what "greedy" means in this context.

---

### Q5 — Variable Topic (3 marks each)

| Paper | Marks | Topic |
|---|---|---|
| 2025 Sample | 3 | Random Forest: feature bagging — how it selects features (2 mk) + why this is beneficial (1 mk) |
| 2025 Real | 3 | Fuzzy Logic: contrast with traditional logic (3 mk) |
| 2026 Sample | 3 | Random Forest: feature bagging — how it selects features (2 mk) + why this is beneficial (1 mk) |

**Key Observations:**

- Random forest / bagging is the most common topic here (3 of 4 papers).
- Fuzzy logic appeared once but is closely related to Q6's vagueness vs uncertainty theme — study both together.

---

### Q6 — Variable Topic (3–4 marks)

| Paper | Marks | Topic |
|---|---|---|
| 2025 Sample | 4 | Vagueness vs Uncertainty: classify 4 scenarios (4 mk) |
| 2025 Real | 3 | Genetic Algorithm: design a fitness function (3 mk) |
| 2026 Sample | 4 | Vagueness vs Uncertainty: classify 4 scenarios (4 mk) |

**Key Observations:**

- Vagueness vs Uncertainty is the dominant question type (3 of 4 papers). The question format is always the same: given 4 real-world scenarios, classify each as vagueness or uncertainty and justify.
- GA fitness function design appeared once — given a problem, define what the fitness function should measure.

---

## Exam Topic Frequency Map（考点频率表）

| Topic | Appearances | Percentage | Priority |
|---|---|---|---|
| Symbolic Logic (Propositional + FOL) | 4 / 4 | 100% | 🔴 必考 |
| Logic Neural Networks (LNN) | 4 / 4 | 100% | 🔴 必考 |
| Knowledge Graphs / TransE | 4 / 4 | 100% | 🔴 必考 |
| Decision Trees / CART / Random Forest | 3 / 4 | 75% | 🔴 必考 |
| Bagging / Boosting / Ensemble Methods | 3 / 4 | 75% | 🔴 必考 |
| Vagueness vs Uncertainty | 3 / 4 | 75% | 🔴 必考 |
| Multi-Agent Systems (Robot Soccer) | 3 / 4 | 75% | 🟠 高频 |
| Fuzzy Logic | 2 / 4 | 50% | 🟠 高频 |
| Genetic Algorithms / NEAT | 1 / 4 | 25% | 🟡 中频 |
| MYCIN / Backward Chaining | 1 / 4 | 25% | 🟡 中频 |

### Priority Legend

- 🔴 **必考 (Must-know)** — Appeared in ≥ 75% of papers. Expect this on your test.
- 🟠 **高频 (High frequency)** — Appeared in 50–74% of papers. Very likely to appear.
- 🟡 **中频 (Medium frequency)** — Appeared in 25–49% of papers. May appear; do not skip entirely.
- 🟢 **低频 (Low frequency)** — Appeared in < 25% of papers. Lower priority but still possible.

---

## Teacher's Examination Style（命题风格分析）

### 1. Question Design Preferences

- **Scenario-based questions are dominant.** The teacher prefers "apply concept X to situation Y" over pure recall. For example, Q6 always presents real-world scenarios and asks you to classify them.
- **"Explain in natural language" is a signature prompt.** LNN questions frequently ask you to describe what a logical rule means in plain English, then contrast it with Boolean logic.
- **Multi-part questions** are the norm. Almost every question has sub-parts (a) and (b) that test different depths — typically (a) tests recall/computation and (b) tests understanding/justification.

### 2. Recurring Sentence Patterns in Questions

The teacher uses these question stems repeatedly:

| Pattern | Topic Area |
|---|---|
| *"What does this rule represent in natural language?"* | LNN, Symbolic Logic |
| *"Use propositional logic to deduce..."* | Symbolic Logic |
| *"Explain how [method] works"* | KG, Decision Trees, Random Forest |
| *"Describe one strategy for..."* | Multi-Agent Systems |
| *"Is this an example of vagueness or uncertainty? Justify."* | Vagueness vs Uncertainty |
| *"Why is this approach beneficial?"* | LNN, Random Forest |
| *"Design a fitness function for..."* | Genetic Algorithms |

### 3. What the Teacher Values

- **Conciseness.** The instructions explicitly state "quality over quantity." Write clear, direct answers — do not pad with filler.
- **Worked computation.** LNN questions always require you to show numerical steps. Write out intermediate values.
- **Correct formal notation.** FOL questions require proper use of ∀, ∃, ¬, →, and predicate syntax. Sloppy notation loses marks.
- **Justification over assertion.** When the question says "justify" or "explain why," a bare statement without reasoning will not earn full marks.

### 4. Common Traps（常见陷阱）

| Trap | How to Avoid |
|---|---|
| Confusing vagueness with uncertainty | Vagueness = the concept itself is inherently imprecise ("tall"). Uncertainty = the fact is precise but unknown ("Will it rain tomorrow?"). |
| Writing ¬∀x P(x) without converting it | Always push the negation inward: ¬∀x P(x) ≡ ∃x ¬P(x). Then give a concrete example. |
| Forgetting to show LNN computation steps | Even if you know the answer, write out the t-norm/t-conorm formula and substitute the numbers. |
| Confusing bagging with boosting | Bagging trains models in parallel on bootstrap samples. Boosting trains sequentially, weighting errors. Random forest uses bagging + feature subsampling. |
| Describing TransE without the scoring function | Always state h + r ≈ t **and** the distance-based scoring function. |

### 5. Co-occurrence Patterns（共现分析）

Some topics regularly appear together in the same exam:

- **Symbolic Logic + LNN** — always together (Q1 + Q2 in every paper). The teacher clearly treats these as a paired topic: classical logic → neural extension.
- **Random Forest + Vagueness vs Uncertainty** — appeared together in 3 of 4 papers. These are the teacher's preferred Q5–Q6 combination.
- **KG / TransE** is always standalone at Q3, never combined with other topics.

---

## Mark Distribution by Topic（分值分布）

Based on the 2026 Sample paper (20 marks total), marks are distributed as:

| Question | Topic | Marks | Percentage |
|---|---|---|---|
| Q1 | Symbolic Logic | 5 | 25% |
| Q2 | LNN | 4 | 20% |
| Q3 | Knowledge Graphs | 2 | 10% |
| Q4 | Multi-Agent | 2 | 10% |
| Q5 | Random Forest | 3 | 15% |
| Q6 | Vagueness vs Uncertainty | 4 | 20% |

> **Takeaway:** Symbolic Logic and LNN together account for 45% of the marks. These two topics alone can determine your grade. Prioritise them.

---

## Revision Priority Summary（复习优先级总结）

### Tier 1 — Master These First (45% of marks)

1. **Propositional Logic** — truth tables, modus tollens, De Morgan's Laws
2. **First-Order Logic** — predicates, quantifiers, negation of universal statements
3. **LNN** — natural language interpretation, soft-logic computation (AND/OR bounds), difference from Boolean logic

### Tier 2 — Secure These Next (30% of marks)

4. **Knowledge Graphs / TransE** — embedding concept, h + r ≈ t, scoring function, link prediction
5. **Random Forest / Bagging** — bootstrap sampling, feature subsampling, why it reduces variance
6. **Vagueness vs Uncertainty** — definitions, 4-scenario classification exercise

### Tier 3 — Cover These Last (25% of marks)

7. **Multi-Agent Systems** — robot soccer coordination strategies
8. **Fuzzy Logic** — contrast with crisp logic, membership functions
9. **Decision Trees / CART** — greedy splitting, information gain / Gini impurity
10. **Genetic Algorithms** — fitness function design, selection, crossover, mutation
