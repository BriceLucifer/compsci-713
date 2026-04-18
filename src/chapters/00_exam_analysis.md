# Sample Test Detailed Analysis（真题逐题分析）

> **Source:** COMPSCI 713 Sample Test, Semester 1 2026, University of Auckland
> **Format:** 6 short-answer questions, 20 marks total, 60 minutes (5 min reading + 55 min answering)
> **Allowed aids:** One double-sided handwritten A4 page. No calculators.

---

## Question 1 — Symbolic Logic [5 marks]

### Question Summary

*Tests understanding of propositional logic and first-order logic (FOL).*

**(a) Propositional Logic — Deduction via Truth Table [3 marks]**

**Scenario:** A secure facility grants entry only if a person has a valid ID (I) AND fingerprint matches (F). Rule: $(I \wedge F) \rightarrow E$. Observed: the person was NOT granted entry ($\neg E$).

**Task:** Use propositional logic to deduce what must be true about I and F. Show truth table.

**(b) First-Order Logic — Formalisation + Example [2 marks]**

**Scenario:** A biologist claims "Not all birds in this region can fly." Domain = birds in this region. Fly(x) = bird x can fly.

- (i) Write the claim in formal FOL [1 mark]
- (ii) Provide a realistic example making the statement true [1 mark]

### Official Answer

**(a):**
1. Build truth table for $X \rightarrow E$ (where $X = I \wedge F$): when $E = 0$ and implication is true, $X$ must be 0 [1 mark]
2. Build truth table for $I \wedge F$: the only way $I \wedge F = 0$ is when at least one of $I$, $F$ is 0 [1 mark]
3. **Conclusion:** The person either did not have a valid ID, or the fingerprint did not match (or both) [1 mark]

**(b):**
- (i) $\neg \forall x \, \text{Fly}(x)$ [1 mark]
- (ii) Example: "There is a penguin in this region, and penguins cannot fly." [1 mark]

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Symbolic Logic（符号逻辑） |
| **Lecture** | W2L1 — Symbolic Logic |
| **Type** | 推理 + 形式化（Deduction + Formalisation） |
| **Difficulty** | ★★☆ |
| **Keywords** | propositional logic, truth table, modus tollens, FOL, quantifiers, negation |
| **Core skill** | Apply truth table reasoning; translate English to FOL with quantifiers |
| **Exam intent** | Tests if student can (1) apply logical inference mechanically, (2) translate natural language to formal logic, (3) give concrete examples for abstract statements |

### Learning Points（学习要点）

> **Why was this asked?** Symbolic logic is THE foundation of the course. The professor wants to verify you can do the "bread and butter": truth tables and FOL formalisation.

- **Modus Tollens pattern**: $(P \rightarrow Q)$ and $\neg Q$ implies $\neg P$. Q1(a) tests exactly this — recognize the pattern!
- **"Not all" in FOL** = $\neg \forall x$ which is equivalent to $\exists x \, \neg$. Know both forms.

> **Common mistake**: Writing $\forall x \, \neg \text{Fly}(x)$ instead of $\neg \forall x \, \text{Fly}(x)$. The first means "NO bird can fly" (too strong); the second means "not every bird can fly."

---

## Question 2 — Logic Neural Networks (LNN) [4 marks]

### Question Summary

*Tests understanding of LNN's soft conjunction operator and its difference from Boolean logic.*

**Scenario:** A smart home uses LNN to decide on heating. Rule: HeatingOn $\leftarrow$ Cold $\otimes$ AtHome, where $\otimes$ is the differentiable AND.

**(a)** What does this rule mean in natural language? How does it differ from standard Boolean? [2 marks]

**(b)** Given Cold = 0.9, AtHome = 0.4, compute HeatingOn and discuss whether heating activates. [2 marks]

### Official Answer

**(a):**
- Natural language: "If it is cold and someone is at home, then turn on the heating." [1 mark]
- Difference: Boolean requires both inputs to be strictly 1. LNN's $\otimes$ supports continuous truth values (0.4, 0.9), yielding intermediate activations that reflect uncertainty and enable gradient-based learning. [1 mark]

**(b):**
- Using product t-norm: HeatingOn $\approx 0.4 \times 0.9 = 0.36$ [1 mark]
- Whether heating activates depends on the threshold. Low threshold (0.3) → heating on. High threshold (0.7) → heating off. [1 mark]

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Logic Neural Networks（逻辑神经网络） |
| **Lecture** | W2L2 — Logic Neural Networks |
| **Type** | 概念解释 + 计算（Explain + Compute） |
| **Difficulty** | ★★☆ |
| **Keywords** | LNN, soft conjunction, Lukasiewicz logic, truth value, differentiable logic, threshold |
| **Core skill** | Explain crisp vs soft logic difference; compute with real-valued operators |
| **Exam intent** | Tests if student understands WHY we need differentiable logic |

### Learning Points（学习要点）

> **Why was this asked?** LNN bridges symbolic AI and neural networks — the signature theme of this course.

- **Key insight**: Boolean AND(0.9, 0.4) would round to AND(1, 0) = 0. LNN gives 0.36 — a nuanced answer reflecting partial truth.
- **Know multiple t-norms**:
  - Product: $0.9 \times 0.4 = 0.36$
  - Lukasiewicz: $\max(0, 0.9 + 0.4 - 1) = 0.3$
  - Godel (min): $\min(0.9, 0.4) = 0.4$

> **Common mistake**: Forgetting to discuss the **threshold**. A truth value alone doesn't determine activation — you need a decision boundary.

---

## Question 3 — Knowledge Graph Embeddings [2 marks]

### Question Summary

*Tests understanding of entity/relation embeddings and KG inference tasks.*

**Task:** Explain the role of entity and relation embeddings in knowledge graph completion. Introduce a common KG inference task and provide one example.

### Official Answer

- KGE represent entities and relations as dense vectors in continuous space, allowing models to predict missing links, validate facts, and reason over structured knowledge. [1 mark]
- Common inference tasks: Link prediction (h, r, ?) or (?, r, t); Relation prediction (h, ?, r). Example: the model discovers (Einstein, bornIn, ?) -> Germany, even if not originally in the KG. [1 mark]

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Knowledge Graph Embeddings（知识图谱嵌入） |
| **Lecture** | W3L2 — Knowledge Graphs for AI |
| **Type** | 概念解释 + 举例（Explain + Example） |
| **Difficulty** | ★☆☆ |
| **Keywords** | KG embedding, TransE, link prediction, knowledge completion |
| **Core skill** | Explain why we embed KG entities; name inference tasks |

### Learning Points（学习要点）

- **TransE core idea**: $h + r \approx t$. If head embedding + relation vector is close to tail, the triple is likely true.
- **Three inference tasks**: tail prediction (h, r, ?), head prediction (?, r, t), relation prediction (h, ?, t)

> **Common mistake**: Confusing "embedding" with "one-hot encoding." Embeddings are *dense, low-dimensional, learned* vectors.

> **Exam tip**: Give a concrete example. "(Einstein, bornIn, ?) -> Germany" is much better than "it predicts missing links."

---

## Question 4 — Multi-Agent Systems [2 marks]

### Question Summary

*Tests knowledge of collective strategies in multi-agent robot soccer.*

**Scenario:** Robot soccer league with overhead camera, 225 features per frame, team of 5 robots.

**Task:** List strategies/collective behaviours discussed in class. [2 marks]

### Official Answer

Any of the following (1 mark each, max 2):
- **Collective behaviours**: passing strategy, interception prediction, passing point value assessment
- **Positioning strategies**: choosing formations for attack/defense
- **Role-based strategies**: assigning roles to each player based on game situation

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Multi-Agent Systems（多智能体系统） |
| **Lecture** | Likely from a session not in provided input files |
| **Type** | 知识回忆（Recall） |
| **Difficulty** | ★☆☆ |
| **Exam intent** | Tests lecture attendance — can you name concrete strategies? |

### Learning Points

- **Three categories**: (1) Collective behaviours (passing), (2) Positioning (formation), (3) Role-based (dynamic assignment)

> **Common mistake**: Being too vague. "They work together" gets 0 marks. Name specific strategies.

---

## Question 5 — Random Forest [3 marks]

### Question Summary

*Tests understanding of random forest's feature bagging mechanism.*

**Scenario:** Dataset with 225 features.

**(a)** How are features selected per tree? How many features per tree? [2 marks]

**(b)** Why is feature bagging a good idea? [1 mark]

### Official Answer

**(a):** Random subset of features sampled per tree. Typical: $\sqrt{225} = 15$ features. Features sampled with replacement, size $\ll 225$. [2 marks]

**(b):** Prevents trees from being highly correlated (e.g., same strong feature always at root). Makes trees less correlated and more complementary as an ensemble. [1 mark]

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Decision Trees & Ensembles（决策树与集成方法） |
| **Lecture** | W4L2 |
| **Type** | 解释 + 计算（Explain + Calculate） |
| **Difficulty** | ★★☆ |
| **Exam intent** | Tests deeper understanding — not just "what" but "why" feature bagging helps |

### Learning Points

- **$\sqrt{p}$ rule**: For 225 features, sample $\sqrt{225} = 15$ features per tree.
- **Bagging vs Boosting**: Bagging reduces **variance** (averaging). Boosting reduces **bias** (sequential correction).

> **Common mistake**: Confusing "random data points" (bootstrap sampling) with "random features" (feature bagging). Both happen in Random Forest, but they're different mechanisms.

---

## Question 6 — Vagueness vs Uncertainty [4 marks]

### Question Summary

Classify 4 scenarios as either vagueness or uncertainty:

1. Patient condition described as "high risk"
2. Security system estimates whether burglary occurred
3. Student performance rated "almost excellent"
4. Spam filter classifies email

### Official Answer

1. **Vagueness** — "high risk" has blurry boundaries; degree, not yes/no [1 mark]
2. **Uncertainty** — real state unknown; uncertain whether burglary happened [1 mark]
3. **Vagueness** — "almost excellent" is graded concept, no sharp boundary [1 mark]
4. **Uncertainty** — inferring unknown class from evidence; probabilistic reasoning [1 mark]

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Soft Computing（软计算） |
| **Lecture** | W5L1 |
| **Type** | 分类判断（Classification） |
| **Difficulty** | ★☆☆ |
| **Exam intent** | Tests the philosophical distinction — the central theme of W5L1 |

### Learning Points

- **The key question**:
  - **Vagueness** → "To what degree?" → Tool: **Fuzzy Logic** (membership functions)
  - **Uncertainty** → "How likely?" → Tool: **Bayesian Reasoning** (probabilities)
- **Quick test**: Blurry concept boundary → vagueness. Unknown world state → uncertainty.

> **Common mistake**: Thinking fuzzy logic models uncertainty. Fuzzy logic models **vagueness** (degree of membership). Bayesian reasoning models **uncertainty** (belief given evidence).

---

## Overall Summary

| Q | Topic | Marks | % | Cognitive Level |
|---|-------|-------|---|----------------|
| Q1 | Symbolic Logic | 5 | 25% | Apply (truth table) + Formalise (FOL) |
| Q2 | LNN | 4 | 20% | Explain (concept) + Compute (t-norm) |
| Q3 | KG Embeddings | 2 | 10% | Explain + Exemplify |
| Q4 | Multi-Agent | 2 | 10% | Recall |
| Q5 | Random Forest | 3 | 15% | Explain mechanism + Justify design |
| Q6 | Vagueness vs Uncertainty | 4 | 20% | Classify scenarios |
| **Total** | | **20** | **100%** | |

### Mark Distribution by Cognitive Level

| Level | Marks | Questions |
|-------|-------|-----------|
| **Recall / Define** | 6 | Q3, Q4, parts of Q1b, Q6 |
| **Apply / Compute** | 8 | Q1a, Q2b, Q5a |
| **Analyze / Explain** | 6 | Q2a, Q5b, Q6 |

> **Takeaway**: The exam balances recall, computation, and explanation roughly equally. You must be able to DO logic (not just describe it) and EXPLAIN reasoning (not just give answers).
