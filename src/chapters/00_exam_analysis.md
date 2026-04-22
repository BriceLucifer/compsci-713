# 真题逐题分析 — Complete Exam Analysis

> **Course:** COMPSCI 713: AI Fundamentals, University of Auckland
> **Instructor:** Xinyu Zhang (mid-semester) / Thomas (final exam, partial)
> **Scope:** ALL available exam papers — S1 2025 Sample, S1 2025 Actual, S1 2026 Sample, S1 2024 Final
> **Purpose:** Question-by-question breakdown for exam preparation

---

## How to Use This Document（使用指南）

1. **First pass**: Skim the tables at the end of each exam section to see topic/mark distribution
2. **Second pass**: Read the Learning Points for your weakest topics
3. **Third pass**: Use the Common Mistakes as a self-check before the exam
4. **Final review**: Jump to [Cross-Exam Patterns](#cross-exam-patterns-跨卷规律总结) at the bottom

> 💡 **核心发现**: 每一份试卷都考了 Symbolic Logic, LNN, Knowledge Graphs, 和 Decision Trees/Ensembles。这四个是绝对必考项。

---

# Exam Paper 1: S1 2025 Sample Test

> **Format:** 15 marks, 6 questions, 60 minutes (5 reading + 55 answering)
> **Allowed aids:** One double-sided handwritten A4 page

---

## Q1 — Symbolic Logic [3 marks]

### Question Summary

**(a) Propositional Logic — Modus Tollens [~1.5m]**

**Scenario:** A secure facility grants entry only if a person has a valid ID ($I$) AND fingerprint matches ($F$). Rule: $(I \wedge F) \rightarrow E$. Observed: person was NOT granted entry ($\neg E$).

**Task:** Deduce what must be true about $I$ and $F$.

**(b) First-Order Logic [~1.5m]**

**Task:** Write "Not all birds can fly" in FOL using $\text{Fly}(x)$. Give a realistic example.

### Expected Answer

**(a):**
- By Modus Tollens: $(I \wedge F) \rightarrow E$ and $\neg E$ implies $\neg(I \wedge F)$
- By De Morgan: $\neg I \vee \neg F$
- **Conclusion:** Either the person lacked a valid ID, or the fingerprint didn't match (or both)

**(b):**
- FOL: $\neg \forall x \, \text{Fly}(x)$, equivalently $\exists x \, \neg \text{Fly}(x)$
- Example: "Penguins are birds but cannot fly"

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Symbolic Logic（符号逻辑） |
| **Lecture** | W2L1 |
| **Type** | 推理 + 形式化 (Deduction + Formalisation) |
| **Difficulty** | ★★☆ |
| **Keywords** | propositional logic, modus tollens, FOL, universal quantifier, negation |
| **Exam intent** | Can student apply basic inference rules AND translate English → FOL? |

### Learning Points（学习要点）

- **Modus Tollens 是本课程考试的第一推理模式**: $(P \rightarrow Q), \neg Q \vdash \neg P$。务必熟练到条件反射
- **"Not all" = $\neg \forall x$**: 注意不是 $\forall x \, \neg$（后者意为"所有都不"，语义完全不同）
- **De Morgan 定律**: $\neg(A \wedge B) = \neg A \vee \neg B$，推导结论时经常用到

> ⚠️ **Common Mistake**: Writing $\forall x \, \neg \text{Fly}(x)$ which means "NO bird can fly" — much stronger than "not all birds can fly."

---

## Q2 — Logic Neural Networks (LNN) [2 marks]

### Question Summary

**Scenario:** Smart home LNN rule: HeatingOn $\leftarrow$ Cold $\otimes$ AtHome (differentiable AND).

**(a)** Interpret in natural language. How does it differ from Boolean? [1m]

**(b)** Compute with Cold = 0.9, AtHome = 0.4. Discuss whether heating activates. [1m]

### Expected Answer

**(a):**
- Natural language: "If it is cold AND someone is at home, turn on the heating."
- Difference: Boolean AND requires both inputs strictly TRUE (1). LNN's $\otimes$ works with continuous truth values in $[0, 1]$, producing intermediate results that capture partial truth and enable gradient-based learning.

**(b):**
- Product t-norm: $0.9 \times 0.4 = 0.36$
- Lukasiewicz: $\max(0, 0.9 + 0.4 - 1) = 0.3$
- Whether heating activates depends on threshold: if $\alpha = 0.3$, yes; if $\alpha = 0.7$, no.

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Logic Neural Networks（逻辑神经网络） |
| **Lecture** | W2L2 |
| **Type** | 概念解释 + 计算 (Explain + Compute) |
| **Difficulty** | ★★☆ |
| **Keywords** | LNN, soft conjunction, t-norm, product, Lukasiewicz, threshold |
| **Exam intent** | Why do we need differentiable logic? Can student compute with t-norms? |

### Learning Points

- **必背三个 t-norm**:
  - Product: $a \times b$
  - Lukasiewicz: $\max(0, a + b - 1)$
  - Godel/min: $\min(a, b)$
- **Boolean vs LNN 的关键差异**: Boolean 是离散的 {0,1}；LNN 是连续的 [0,1]，支持梯度下降

> ⚠️ **Common Mistake**: Forgetting to discuss the **threshold**. Computing 0.36 is not enough — you must state what activation decision follows.

---

## Q3 — Knowledge Graph Embeddings [2 marks]

### Question Summary

Explain the role of entity/relation embeddings in KG completion. Introduce a common KG inference task with an example.

### Expected Answer

- **Embeddings**: Map entities and relations to dense vectors in continuous space, enabling mathematical operations for reasoning
- **Inference task**: Link prediction — given $(h, r, ?)$, predict tail entity
- **Example**: $(Einstein, bornIn, ?) \rightarrow Germany$

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Knowledge Graphs（知识图谱） |
| **Lecture** | W3L2 |
| **Type** | 概念解释 + 举例 (Explain + Example) |
| **Difficulty** | ★☆☆ |
| **Keywords** | KG embedding, TransE, link prediction, knowledge completion |

### Learning Points

- **TransE 核心公式**: $h + r \approx t$（头实体向量 + 关系向量 ≈ 尾实体向量）
- **三种推理任务**: tail prediction $(h, r, ?)$, head prediction $(?, r, t)$, relation prediction $(h, ?, t)$

> ⚠️ **Common Mistake**: Confusing "embedding" with "one-hot encoding." Embeddings are **dense, low-dimensional, learned** vectors — not sparse indicator vectors.

> **Exam tip（答题技巧）**: 永远给具体例子。"(Einstein, bornIn, ?) → Germany" 远比 "it predicts missing links" 好。

---

## Q4 — Embodied AI / Robot Soccer [2 marks]

### Question Summary

Robot soccer league: overhead camera, 225 features per frame, team of 5 robots, no inter-robot communication. Describe strategies/collective behaviours.

### Expected Answer

Any of (1 mark each, max 2):
- **Collective behaviours**: passing strategy, interception prediction, passing point value assessment
- **Positioning strategies**: formations for attack/defense
- **Role-based strategies**: dynamic role assignment based on game situation
- **Centralized control**: overhead camera acts as single controller for all 5 robots

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Embodied AI / Multi-Agent Systems（具身AI/多智能体） |
| **Lecture** | Multi-Agent lecture |
| **Type** | 知识回忆 (Recall) |
| **Difficulty** | ★☆☆ |
| **Exam intent** | Tests lecture attendance — can you name concrete strategies? |

### Learning Points

- **三大策略类别**: (1) 集体行为 — passing, (2) 位置策略 — formation, (3) 角色分配 — dynamic assignment
- **关键细节**: No communication → centralized control via overhead camera → single decision-maker

> ⚠️ **Common Mistake**: Being too vague. "They work together" = 0 marks. Name **specific** strategies.

---

## Q5 — Random Forest / Bagging [3 marks]

### Question Summary

Dataset with 225 features.

**(a)** How are features selected per tree? How many? [2m]

**(b)** Why is feature bagging a good idea? [1m]

### Expected Answer

**(a):**
- Random subset of features sampled per tree (not all 225)
- Typical: $\sqrt{p} = \sqrt{225} = 15$ features per tree
- Different trees see different feature subsets

**(b):**
- Prevents trees from being highly **correlated** (e.g., same dominant feature always at root)
- Decorrelated trees → ensemble averaging reduces **variance** more effectively

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Decision Trees & Ensembles（决策树与集成方法） |
| **Lecture** | W4L2 |
| **Type** | 解释 + 计算 (Explain + Calculate) |
| **Difficulty** | ★★☆ |
| **Exam intent** | Tests "why" not just "what" — understanding the **purpose** of feature bagging |

### Learning Points

- **$\sqrt{p}$ rule**: For $p$ features, sample $\sqrt{p}$ per tree. For 225 features → 15.
- **Bagging vs Boosting**:
  - Bagging → parallel trees → reduces **variance**
  - Boosting → sequential trees → reduces **bias**
- **两层随机化**: (1) Bootstrap sampling of data rows, (2) Random sampling of features. Both reduce correlation.

> ⚠️ **Common Mistake**: Confusing bootstrap sampling (random **data points**) with feature bagging (random **features**). Both happen in Random Forest; they serve different purposes.

---

## Q6 — MYCIN / Expert Systems [3 marks]

### Question Summary

Medical diagnosis scenario using backward chaining. Patient has a runny nose. Possible diagnoses: common cold, allergies, measles. Demonstrate backward chaining reasoning.

### Expected Answer

- **Backward chaining**: Start from hypothesis, work backward to check conditions
  1. Hypothesis: Common Cold → needs runny nose ✓, fever ?, cough ?
  2. Hypothesis: Allergies → needs runny nose ✓, sneezing ?, itchy eyes ?
  3. Hypothesis: Measles → needs runny nose ✓, rash ?, high fever ?
- Ask additional questions to discriminate between hypotheses
- Contrast with **forward chaining**: start from facts, derive conclusions

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Expert Systems / MYCIN（专家系统） |
| **Lecture** | W3L1 (Knowledge Representation) |
| **Type** | 推理过程演示 (Demonstrate reasoning process) |
| **Difficulty** | ★★☆ |
| **Keywords** | backward chaining, hypothesis, rule-based reasoning, MYCIN |
| **Exam intent** | Can student trace backward chaining step by step? |

### Learning Points

- **Backward chaining 三步法**: (1) Start with hypothesis, (2) Check conditions, (3) Ask for missing info
- **Forward vs Backward**: Forward = data-driven (fact → conclusion); Backward = goal-driven (hypothesis → verify)
- **MYCIN 特色**: Uses **certainty factors** (CF) instead of probabilities; backward chaining for diagnosis

> ⚠️ **Common Mistake**: Describing forward chaining when asked for backward chaining. Direction matters!

---

### S1 2025 Sample Test — Summary Table

| Q | Topic | Marks | % | Cognitive Level |
|---|-------|-------|---|----------------|
| Q1 | Symbolic Logic | 3 | 20% | Apply + Formalise |
| Q2 | LNN | 2 | 13% | Explain + Compute |
| Q3 | KG Embeddings | 2 | 13% | Explain + Exemplify |
| Q4 | Robot Soccer | 2 | 13% | Recall |
| Q5 | Random Forest | 3 | 20% | Explain + Calculate |
| Q6 | MYCIN / Expert Systems | 3 | 20% | Demonstrate reasoning |
| **Total** | | **15** | **100%** | |

---

# Exam Paper 2: S1 2025 Actual Test

> **Format:** 15 marks, 6 questions, 60 minutes
> **This is the REAL exam that was sat**

---

## Q1 — Symbolic Logic [2 marks]

### Question Summary

**(a)** Given $(P \vee Q) \rightarrow R$ and $\neg R$. Apply Modus Tollens. [1m]

**(b)** Given $\forall x(\text{Cheat}(x) \rightarrow \text{Disqualified}(x))$ and Alice is not disqualified. Conclude about Alice. [1m]

### Expected Answer

**(a):**
- Modus Tollens: $(P \vee Q) \rightarrow R$ and $\neg R$ implies $\neg(P \vee Q)$
- By De Morgan: $\neg P \wedge \neg Q$
- **Both P and Q must be false**

**(b):**
- Universal instantiation: $\text{Cheat}(\text{Alice}) \rightarrow \text{Disqualified}(\text{Alice})$
- Given $\neg \text{Disqualified}(\text{Alice})$, by Modus Tollens: $\neg \text{Cheat}(\text{Alice})$
- **Conclusion: Alice did not cheat**

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Symbolic Logic（符号逻辑） |
| **Lecture** | W2L1 |
| **Type** | 推理 (Pure deduction) |
| **Difficulty** | ★★☆ |
| **Keywords** | modus tollens, disjunction, De Morgan, universal instantiation, FOL |
| **Exam intent** | Modus Tollens again! Plus combining FOL with propositional reasoning |

### Learning Points

- **这道题和 Sample 的区别**: Sample 用 $(I \wedge F) \rightarrow E$，Actual 用 $(P \vee Q) \rightarrow R$。结论不同！
  - $\neg(A \wedge B) = \neg A \vee \neg B$（至少一个为假）
  - $\neg(A \vee B) = \neg A \wedge \neg B$（两个都假）
- **FOL + Modus Tollens 组合拳**: Universal instantiation 先把 $\forall x$ 具体化为 Alice，再用 Modus Tollens

> ⚠️ **Common Mistake**: For $\neg(P \vee Q)$, some students write "$P$ or $Q$ is false" — this is WRONG. **BOTH** must be false. De Morgan on disjunction gives conjunction of negations.

> 🔑 **关键对比**: AND 的否定 → 至少一个假 (disjunction); OR 的否定 → 全部假 (conjunction). 这是必须刻在脑子里的。

---

## Q2 — LNN with Truth Bounds [3 marks]

### Question Summary

**Scenario:** Autonomous vehicle collision alert system. Two sensors:
- Pedestrian detector: $P$ with bounds $[L_P, U_P] = [0.8, 0.9]$
- Obstacle detector: $Q$ with bounds $[L_Q, U_Q] = [0.3, 0.6]$

Rule: Alert $\leftarrow P \vee Q$ (disjunction, not conjunction!)

Alert threshold: $\alpha = 0.7$

**(a)** Determine alert status [2m]

**(b)** Why are bounds (instead of point estimates) useful in safety-critical applications? [1m]

### Expected Answer

**(a):**
- Co-norm for OR (using Lukasiewicz):
  - Lower bound: $\min(1, L_P + L_Q) = \min(1, 0.8 + 0.3) = 1.0$
  - Upper bound: $\min(1, U_P + U_Q) = \min(1, 0.9 + 0.6) = 1.0$
- OR result bounds: $[1.0, 1.0]$
- Since lower bound $1.0 \geq \alpha = 0.7$: **Alert ACTIVATES**

  Alternative (product-based co-norm):
  - $P \vee Q = P + Q - P \cdot Q$
  - Lower: $0.8 + 0.3 - 0.8 \times 0.3 = 0.86$
  - Upper: $0.9 + 0.6 - 0.9 \times 0.6 = 0.96$
  - Bounds: $[0.86, 0.96]$, both $\geq 0.7$: **Alert ACTIVATES**

**(b):**
- Bounds capture **epistemic uncertainty** — we know the truth value lies somewhere in the interval
- In safety-critical systems, we can make **conservative decisions**: if even the lower bound exceeds threshold, we act
- Point estimates hide uncertainty; bounds let us reason about worst-case scenarios

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | LNN with Truth Bounds（带真值边界的 LNN） |
| **Lecture** | W2L2 |
| **Type** | 计算 + 论述 (Compute + Argue) |
| **Difficulty** | ★★★ |
| **Keywords** | LNN, truth bounds, co-norm, disjunction, safety-critical, epistemic uncertainty |
| **Exam intent** | Can student compute with bounds (not just point values)? Understands safety implications? |

### Learning Points

- **这是 LNN 的升级版考法**: Sample 考 AND 的点值计算，Actual 考 OR 的区间计算
- **AND vs OR t-norm/co-norm**:
  - AND (t-norm): Product → $a \times b$; Lukasiewicz → $\max(0, a + b - 1)$
  - OR (co-norm): Product → $a + b - a \times b$; Lukasiewicz → $\min(1, a + b)$
- **Safety-critical reasoning**: 用 lower bound 做决策 = 最保守策略

> ⚠️ **Common Mistake**: Using AND formula when the question says OR! Read the operator carefully: $\otimes$ = AND, $\oplus$ = OR, $\vee$ = OR.

> ⚠️ **另一个常见错误**: 忘记 bounds 是区间运算。不能只算一个值，要算 [lower, upper]。

---

## Q3 — Knowledge Graphs / TransE [2 marks]

### Question Summary

**(a)** Explain the TransE embedding model [1m]

**(b)** Write the TransE scoring function [1m]

### Expected Answer

**(a):**
- TransE represents entities and relations as vectors in the same space
- Core idea: for a true triple $(h, r, t)$, the head plus relation should approximate the tail: $h + r \approx t$

**(b):**
- Scoring function: $f(h, r, t) = \|h + r - t\|$ (L1 or L2 norm)
- Lower score = more likely to be true
- Training: minimize score for true triples, maximize for false (negative sampling)

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Knowledge Graphs / TransE |
| **Lecture** | W3L2 |
| **Type** | 概念 + 公式 (Concept + Formula) |
| **Difficulty** | ★☆☆ |
| **Exam intent** | TransE is the simplest and most testable KG model — can you state the formula? |

### Learning Points

- **TransE 必背**: $f(h,r,t) = \|h + r - t\|$，越小越可能是真三元组
- **与 Sample 的区别**: Sample 考概念层面（什么是 embedding），Actual 考公式层面（TransE 具体怎么算）
- **局限性**: TransE 无法建模 1-to-N 关系（如一个国家有多个城市）

> ⚠️ **Common Mistake**: Writing $h + r = t$ (equality) instead of $h + r \approx t$ (approximation). The model **learns** to minimize the distance, not enforce exact equality.

---

## Q4 — Decision Trees / CART [2 marks]

### Question Summary

What does "greedy" mean in the context of CART (Classification and Regression Trees)?

### Expected Answer

- **Greedy** = at each node, CART picks the **locally optimal split** (maximum information gain or minimum Gini impurity) without considering future splits
- It does **not** evaluate all possible tree structures to find the global optimum
- This makes it computationally efficient but potentially suboptimal
- Why greedy? Finding the optimal tree is NP-hard

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Decision Trees（决策树） |
| **Lecture** | W4L1-L2 |
| **Type** | 概念解释 (Concept explanation) |
| **Difficulty** | ★☆☆ |
| **Keywords** | CART, greedy algorithm, local optimum, information gain, Gini impurity |
| **Exam intent** | Tests understanding of algorithm design philosophy, not just mechanics |

### Learning Points

- **"Greedy"三要素**: (1) 每步选当前最优 (2) 不回溯 (3) 不保证全局最优
- **为什么接受 greedy?**: 找最优树是 NP-hard；greedy 在实践中效果够好
- **Ensemble 弥补 greedy**: Random Forest 通过多棵 greedy tree 的聚合来逼近更好的解

> ⚠️ **Common Mistake**: Saying greedy means "fast." Greedy is about the **optimization strategy** (local vs global), not speed.

---

## Q5 — Fuzzy Logic [3 marks]

### Question Summary

Contrast traditional (Boolean) logic vs fuzzy logic for the rule:
**IF** athlete is STRONG **AND** athlete is HEAVY **THEN** athlete is HAMMER_THROWER

### Expected Answer

**Traditional Logic:**
- STRONG = {yes, no}, HEAVY = {yes, no} → HAMMER_THROWER = {yes, no}
- Sharp boundaries: an athlete is either strong or not
- AND = Boolean AND: both must be true for conclusion to hold

**Fuzzy Logic:**
- STRONG(x) ∈ [0, 1], HEAVY(x) ∈ [0, 1] → HAMMER_THROWER(x) ∈ [0, 1]
- Gradual membership: "somewhat strong" = 0.6, "very heavy" = 0.9
- AND = t-norm (e.g., min): HAMMER_THROWER ≥ min(0.6, 0.9) = 0.6
- Captures **vagueness** — no sharp cutoff between "strong" and "not strong"

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Fuzzy Logic / Soft Computing |
| **Lecture** | W5L1 |
| **Type** | 对比分析 (Compare & Contrast) |
| **Difficulty** | ★★☆ |
| **Exam intent** | Core theme: why do we need fuzzy logic? What problem does it solve? |

### Learning Points

- **对比答题模板**: 分三行写 — (1) Traditional: binary, (2) Fuzzy: continuous, (3) WHY fuzzy is better for this case
- **Fuzzy logic 解决 vagueness**: "Strong" 没有明确边界 → 需要 membership function
- **给具体数字**: 说 "STRONG(athlete) = 0.6" 比抽象描述好得多

> ⚠️ **Common Mistake**: Confusing fuzzy logic with probability. Fuzzy = degree of **membership** (to what extent is this athlete "strong"?). Probability = **likelihood** of an event (what's the chance this athlete wins?).

---

## Q6 — GA / Embodied AI [3 marks]

### Question Summary

Design a fitness function for a BigDog walking robot using Genetic Algorithm optimization.

### Expected Answer

Fitness function components:
1. **Distance traveled** (primary): $f_1 = d / d_{max}$ — further is better
2. **Stability** (constraint): $f_2 = 1 - \text{angular\_deviation} / \text{max\_deviation}$ — less wobble is better
3. **Energy efficiency** (secondary): $f_3 = 1 - E_{used} / E_{max}$ — less energy is better
4. **Penalty**: $f_{penalty} = -C$ if robot falls

**Combined**: $F = w_1 f_1 + w_2 f_2 + w_3 f_3 + f_{penalty}$

Key design considerations:
- Must balance **multiple objectives**
- Weights reflect priority (distance > stability > efficiency typically)
- Penalties for catastrophic failure (falling) should be large

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Genetic Algorithms / Fitness Function Design（遗传算法/适应度函数设计） |
| **Lecture** | GA/NEAT lectures |
| **Type** | 设计题 (Design) |
| **Difficulty** | ★★★ |
| **Keywords** | fitness function, multi-objective, GA, embodied AI, BigDog |
| **Exam intent** | Can student translate a real-world goal into a mathematical optimization objective? |

### Learning Points

- **Fitness function 设计万能框架**: (1) 定义主目标, (2) 加约束, (3) 加惩罚项, (4) 用加权求和合并
- **开放题没有唯一答案**: 关键是逻辑自洽 + 覆盖关键方面
- **必须提到权衡**: 速度 vs 稳定性 vs 能耗

> ⚠️ **Common Mistake**: Only considering one objective (e.g., just distance). Real fitness functions must balance multiple competing goals.

---

### S1 2025 Actual Test — Summary Table

| Q | Topic | Marks | % | Cognitive Level |
|---|-------|-------|---|----------------|
| Q1 | Symbolic Logic (Modus Tollens + FOL) | 2 | 13% | Apply + Deduce |
| Q2 | LNN (Truth Bounds + OR) | 3 | 20% | Compute + Argue |
| Q3 | KG / TransE | 2 | 13% | Explain + Formula |
| Q4 | Decision Trees (CART greedy) | 2 | 13% | Explain concept |
| Q5 | Fuzzy Logic | 3 | 20% | Compare & Contrast |
| Q6 | GA / Fitness Function Design | 3 | 20% | Design |
| **Total** | | **15** | **100%** | |

---

# Exam Paper 3: S1 2026 Sample Test

> **Format:** 20 marks, 6 questions, 60 minutes (5 reading + 55 answering)
> **Note:** Marks increased from 15 → 20. Same topics, more depth required.

---

## Q1 — Symbolic Logic [5 marks]

### Question Summary

**(a) Propositional Logic — with Truth Table [3m]**

Same scenario as S1 2025 Sample: $(I \wedge F) \rightarrow E$, given $\neg E$. But now **explicitly requires a truth table** for full marks.

**(b) FOL — Birds [2m]**

Same "not all birds can fly" question.

### Expected Answer

**(a):**

Step 1: Truth table for $X \rightarrow E$ where $X = I \wedge F$:

| $X$ | $E$ | $X \rightarrow E$ |
|-----|-----|:--:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

When $E = 0$ and implication is TRUE: $X$ must be 0. [1 mark]

Step 2: Truth table for $I \wedge F$:

| $I$ | $F$ | $I \wedge F$ |
|-----|-----|:--:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

$I \wedge F = 0$ when at least one is 0. [1 mark]

Step 3: Conclusion — person either lacked valid ID, or fingerprint didn't match, or both. [1 mark]

**(b):**
- $\neg \forall x \, \text{Fly}(x)$ [1 mark]
- Example: penguins, ostriches, kiwi (kiwi 特别适合 UoA 的语境!) [1 mark]

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Symbolic Logic |
| **Lecture** | W2L1 |
| **Difficulty** | ★★☆ |
| **Compared to 2025** | Same scenario, more marks → must show truth table explicitly |

### Learning Points

- **2026 版本更重视过程**: 3 marks for truth table vs 2025's ~1.5 marks. Show ALL steps.
- **真值表是得分保障**: 即使你能直接用 Modus Tollens 推出结论，画真值表拿更稳的分

> 💡 **策略提示**: 5 marks = 25% of total. Spend proportional time (~14 minutes). Don't rush the truth table.

---

## Q2 — LNN [4 marks]

### Question Summary

Same HeatingOn scenario as S1 2025 Sample, but 4 marks (was 2).

**(a)** Interpret rule + compare with Boolean [2m]

**(b)** Compute with Cold = 0.9, AtHome = 0.4 [2m]

### Expected Answer

Same as S1 2025 Sample Q2 but **more detail expected** for the extra marks:
- **(a)**: Need deeper comparison — mention gradient-based learning, continuous optimization, partial truth
- **(b)**: Show at least two t-norms, discuss threshold selection, explain practical implications

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | LNN |
| **Compared to 2025** | Same question, doubled marks → expects more thorough answer |
| **Difficulty** | ★★☆ |

### Learning Points

- **More marks = more depth expected**:
  - 2m version: basic computation + brief threshold mention
  - 4m version: multiple t-norms + threshold discussion + why LNN matters for AI
- **安全策略**: 写出所有你知道的 t-norm 计算结果，对比它们

---

## Q3 — Knowledge Graph Embeddings [2 marks]

### Question Summary

Same as S1 2025 Sample Q3: explain entity/relation embeddings + KG inference task + example.

### Expected Answer

Identical to S1 2025 Sample Q3. (See above.)

### Learning Points

- **三年不变**: 这道题完全一样。说明 KG embedding 是必考的固定题型。

---

## Q4 — Robot Soccer [2 marks]

### Question Summary

Same as S1 2025 Sample Q4: overhead camera, 225 features, describe strategies.

### Expected Answer

Identical to S1 2025 Sample Q4. (See above.)

### Learning Points

- **同样三年不变**: Robot Soccer 策略也是固定考点。

---

## Q5 — Random Forest [3 marks]

### Question Summary

Same as S1 2025 Sample Q5: feature selection + why feature bagging.

### Expected Answer

Identical to S1 2025 Sample Q5. (See above.)

---

## Q6 — Vagueness vs Uncertainty [4 marks]

### Question Summary

**New question type** (not in S1 2025 Sample):

Classify 4 scenarios:
1. Patient described as "high risk" → **Vagueness**
2. Security system estimates burglary → **Uncertainty**
3. Student rated "almost excellent" → **Vagueness**
4. Spam filter classifies email → **Uncertainty**

### Expected Answer

| Scenario | Classification | Reasoning |
|----------|---------------|-----------|
| "high risk" patient | **Vagueness** | Blurry boundary — what counts as "high"? Degree, not yes/no |
| Alarm/burglary estimate | **Uncertainty** | Unknown ground truth — did burglary actually happen? |
| "almost excellent" student | **Vagueness** | Gradual concept — no sharp boundary between "good" and "excellent" |
| Spam filter | **Uncertainty** | Probabilistic inference — inferring unknown class from features |

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Soft Computing — Vagueness vs Uncertainty |
| **Lecture** | W5L1 |
| **Difficulty** | ★☆☆ (if you know the distinction) |
| **Exam intent** | THE central philosophical distinction of soft computing |

### Learning Points

- **万能判断法则**:
  - **Vagueness** → "To what **degree**?" → Fuzzy Logic (membership functions)
  - **Uncertainty** → "How **likely**?" → Bayesian Reasoning (probabilities)
- **快速测试**: 概念边界模糊 → vagueness; 世界状态未知 → uncertainty
- **语言线索**: "high", "almost", "kind of" → vagueness; "estimate", "predict", "classify" → uncertainty

> ⚠️ **Common Mistake**: Thinking fuzzy logic handles uncertainty. NO — fuzzy handles **vagueness**; Bayes handles **uncertainty**. This is THE most important distinction in W5.

---

### S1 2026 Sample Test — Summary Table

| Q | Topic | Marks | % | Cognitive Level |
|---|-------|-------|---|----------------|
| Q1 | Symbolic Logic (truth table + FOL) | 5 | 25% | Apply + Formalise |
| Q2 | LNN (soft AND computation) | 4 | 20% | Explain + Compute |
| Q3 | KG Embeddings | 2 | 10% | Explain + Exemplify |
| Q4 | Robot Soccer | 2 | 10% | Recall |
| Q5 | Random Forest / Bagging | 3 | 15% | Explain + Calculate |
| Q6 | Vagueness vs Uncertainty | 4 | 20% | Classify scenarios |
| **Total** | | **20** | **100%** | |

---

# Exam Paper 4: S1 2024 Final Exam (Thomas's Section)

> **Note:** This is the final exam (not mid-semester), with questions from a different instructor (Thomas). These topics may or may not appear in 2026's mid-semester, but they are useful for final exam preparation and general knowledge.

---

## Q1 — Continual Learning [4 marks]

### Question Summary

Concept drift, replay methods, Gaussian Mixture Models in continual learning.

### Expected Answer

- **Concept drift**: Data distribution changes over time; model must adapt
- **Replay methods**: Store subset of old data; replay during training on new data to prevent catastrophic forgetting
- **GMM**: Can be used to model data distributions; detect drift by comparing distributions
- **Stability-plasticity tradeoff**: Too much stability → can't learn new; too much plasticity → forgets old

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Continual Learning（持续学习） |
| **Difficulty** | ★★☆ |
| **Priority for 2026 mid-sem** | 🟢 LOW — Thomas's topic, unlikely in mid-semester |

---

## Q2 — BFS vs UCS [3 marks]

### Question Summary

Compare Breadth-First Search and Uniform-Cost Search.

### Expected Answer

- **BFS**: Expands shallowest node first; optimal when all edge costs equal; uses FIFO queue
- **UCS**: Expands lowest-cost node first; optimal for any non-negative costs; uses priority queue
- **Key difference**: BFS = optimal for unweighted; UCS = optimal for weighted graphs

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Search Algorithms |
| **Priority for 2026 mid-sem** | 🟢 LOW — not in Xinyu's question pattern |

---

## Q3 — MCTS / UCB1 [3 marks]

### Question Summary

Explain the components of the UCB1 formula used in Monte Carlo Tree Search.

### Expected Answer

$$UCB1 = \bar{X}_j + C \sqrt{\frac{\ln N}{n_j}}$$

- $\bar{X}_j$: average reward of node $j$ (exploitation term)
- $N$: total visits to parent
- $n_j$: visits to node $j$
- $C$: exploration constant
- $\sqrt{\ln N / n_j}$: exploration term — favors less-visited nodes
- **Balances exploration vs exploitation**

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | MCTS / UCB1 |
| **Priority for 2026 mid-sem** | 🟡 MEDIUM — exploration-exploitation could appear in GA context |

---

## Q4 — RL for Pac-Man [1 mark]

### Question Summary

Define state, action, policy, reward for RL applied to Pac-Man.

### Expected Answer

- **State**: Current game board configuration (ghost positions, pellet locations, Pac-Man position)
- **Action**: Move direction (up, down, left, right)
- **Policy**: Mapping from state to action (which direction to move in each situation)
- **Reward**: +10 eating pellet, +200 eating ghost, -500 dying, -1 per time step

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Reinforcement Learning（强化学习） |
| **Priority for 2026 mid-sem** | 🟢 LOW |

---

## Q5 — GNN [2 marks]

### Question Summary

Explain permutation invariance and permutation equivariance in Graph Neural Networks.

### Expected Answer

- **Permutation invariance**: Output doesn't change when node ordering changes (graph-level prediction)
- **Permutation equivariance**: Output permutes consistently with input permutation (node-level embeddings)

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Graph Neural Networks |
| **Priority for 2026 mid-sem** | 🟢 LOW — not in Xinyu's observed pattern |

---

## Q6 — Self-Supervised Learning [2 marks]

### Question Summary

Distinguish pretext tasks from downstream tasks in self-supervised learning.

### Expected Answer

- **Pretext task**: Artificial task designed to learn representations without labels (e.g., predict rotation, fill masked words)
- **Downstream task**: Actual target task the representations are used for (e.g., classification, NER)
- **Relationship**: Pretext → learn general features; fine-tune on downstream task with few labels

### Analysis

| Item | Detail |
|------|--------|
| **Topic** | Self-Supervised Learning |
| **Priority for 2026 mid-sem** | 🟢 LOW |

---

## Additional Topics from S1 2024 Final (Answer Key)

The following topics appeared in the S1 2024 final exam answer key:

| Topic | Content | Priority for Mid-Sem |
|-------|---------|---------------------|
| **DQN** | Online vs target network, bootstrapping | 🟢 LOW |
| **Self-Attention** | Q/K/V vectors, advantage over traditional attention | 🟡 MEDIUM |
| **LLM System Design** | Technical route for LLM-based system | 🟡 MEDIUM |
| **Decision Tree vs Forest** | Interpretability/efficiency trade-off | 🟠 HIGH (DT is core) |
| **Naive Bayes** | Conditional independence, feature relevance assumptions | 🟡 MEDIUM |
| **NEAT** | Mobile robot application, fitness function design | 🟠 HIGH (GA/NEAT is core) |
| **Self-Supervised Learning** | Pretext/downstream tasks | 🟢 LOW |
| **Replay in Continual Learning** | Stability-plasticity tradeoff | 🟢 LOW |
| **CNN in Self-Driving** | CNN application in autonomous vehicles | 🟡 MEDIUM |

---

# Cross-Exam Patterns（跨卷规律总结）

## Pattern 1: Repeated Questions（原题重复出现）

以下题目在多份试卷中几乎一模一样地出现：

| Question | S1 2025 Sample | S1 2025 Actual | S1 2026 Sample |
|----------|:-:|:-:|:-:|
| $(I \wedge F) \rightarrow E$, $\neg E$ → Modus Tollens | ✅ | variant: $(P \vee Q) \rightarrow R$ | ✅ (with truth table) |
| FOL: "Not all birds can fly" | ✅ | variant: Cheat/Disqualified | ✅ |
| LNN HeatingOn ← Cold ⊗ AtHome | ✅ | variant: Bounds + OR | ✅ |
| KG embeddings + inference task | ✅ | variant: TransE formula | ✅ |
| Robot Soccer strategies | ✅ | — | ✅ |
| Random Forest feature bagging | ✅ | variant: CART greedy | ✅ |
| MYCIN backward chaining | ✅ | — | — |
| Fuzzy logic contrast | — | ✅ | — |
| Vagueness vs Uncertainty | — | — | ✅ |
| GA fitness function | — | ✅ | — |

> 💡 **核心发现**: Xinyu 喜欢在 Sample Test 和 Actual Test 之间做微调而非大改。Sample 就是 Actual 的预告片！

## Pattern 2: Question Evolution（题目进化路径）

每个核心考点在不同年份有"升级版":

**Symbolic Logic 进化链:**
```
S1 2025 Sample: (I∧F)→E, ¬E → 推理（无真值表要求）
S1 2025 Actual: (P∨Q)→R, ¬R → 推理 + FOL 组合
S1 2026 Sample: 同 2025 Sample 但要求画真值表，5 marks
```
→ **趋势**: 从 "能推理" → "能推理 + 证明过程" → "能推理 + 证明 + 变体"

**LNN 进化链:**
```
S1 2025 Sample: 点值计算 (AND), 2 marks
S1 2025 Actual: 区间计算 (OR) + safety reasoning, 3 marks
S1 2026 Sample: 点值计算 (AND), 4 marks (deeper explanation)
```
→ **趋势**: AND 和 OR 交替考，区间 vs 点值交替考

**KG 进化链:**
```
S1 2025 Sample: "Explain embeddings" (概念)
S1 2025 Actual: "Write TransE formula" (公式)
S1 2026 Sample: "Explain embeddings" (概念, 同2025 Sample)
```
→ **趋势**: 概念和公式交替考。两手都要准备。

## Pattern 3: Mark Allocation Trends

| Topic | 2025 Sample (15m) | 2025 Actual (15m) | 2026 Sample (20m) |
|-------|:-:|:-:|:-:|
| Symbolic Logic | 3m (20%) | 2m (13%) | 5m (25%) |
| LNN | 2m (13%) | 3m (20%) | 4m (20%) |
| KG | 2m (13%) | 2m (13%) | 2m (10%) |
| Decision Trees/RF | 3m (20%) | 2m (13%) | 3m (15%) |
| Soft Computing/Fuzzy | — | 3m (20%) | 4m (20%) |
| Embodied AI/GA | 2m (13%) | 3m (20%) | 2m (10%) |
| Expert Systems | 3m (20%) | — | — |

> **Key insight**: Symbolic Logic + LNN consistently take 35-45% of total marks. These two topics alone are worth nearly half the exam.

## Pattern 4: Cognitive Level Distribution

| Level | Description | Typical % |
|-------|-------------|-----------|
| **Recall** | Name strategies, list features | ~15% |
| **Explain** | Describe how/why something works | ~30% |
| **Compute** | Calculate t-norm, truth table, $\sqrt{p}$ | ~25% |
| **Compare** | Fuzzy vs Boolean, vagueness vs uncertainty | ~15% |
| **Design** | Fitness function, system strategy | ~15% |

---

# Topic Priority Matrix for 2026 Mid-Semester（2026 期中复习优先级）

Based on cross-exam analysis, here is the definitive priority ranking:

| Priority | Topic | Expected Marks | Study Time |
|----------|-------|:-:|:-:|
| 🔴 **MUST** | Symbolic Logic (Modus Tollens + truth table + FOL) | 4-5m | 20% |
| 🔴 **MUST** | LNN (AND/OR, point/bounds, t-norm/co-norm) | 3-4m | 20% |
| 🔴 **MUST** | Knowledge Graphs (TransE, embeddings, inference) | 2m | 10% |
| 🔴 **MUST** | Decision Trees & Random Forest (greedy, bagging, $\sqrt{p}$) | 2-3m | 10% |
| 🔴 **MUST** | Soft Computing (vagueness vs uncertainty, fuzzy vs Boolean) | 3-4m | 15% |
| 🟠 **HIGH** | Embodied AI / Robot Soccer (strategies, centralized control) | 2m | 8% |
| 🟠 **HIGH** | GA / NEAT (fitness function design) | 2-3m | 10% |
| 🟠 **HIGH** | Expert Systems / MYCIN (backward chaining) | 0-3m | 5% |
| 🟡 **MEDIUM** | Naive Bayes (conditional independence) | 0-2m | 2% |

---

# Exam Strategy Recommendations（应试策略建议）

## Time Management（时间分配）

For a 20-mark, 55-minute exam:
- **~2.75 minutes per mark**
- Q1 (5m): ~14 minutes
- Q2 (4m): ~11 minutes
- Q3 (2m): ~5.5 minutes
- Q4 (2m): ~5.5 minutes
- Q5 (3m): ~8 minutes
- Q6 (4m): ~11 minutes

## Cheatsheet Priorities（A4 速查表优先写什么）

Your double-sided A4 page should include (in order of priority):

1. **Truth table templates** — implication, AND, OR truth tables pre-drawn
2. **Modus Tollens + De Morgan** — write the formulas
3. **T-norm / Co-norm formulas** — all 3 variants for AND and OR
4. **LNN bounds computation** — interval arithmetic rules
5. **TransE formula** — $f(h,r,t) = \|h + r - t\|$
6. **$\sqrt{p}$ formula** — for Random Forest feature bagging
7. **Vagueness vs Uncertainty** — decision table with examples
8. **Backward vs Forward chaining** — one-line definitions
9. **Fitness function template** — multi-objective weighted sum
10. **Key FOL patterns** — $\neg \forall x = \exists x \neg$

## Answer Writing Tips（答题技巧）

1. **Show your work**: 2026 version gives more marks for process (truth tables, step-by-step computation)
2. **Give concrete examples**: "(Einstein, bornIn, ?) → Germany" > "it predicts missing links"
3. **Use the scenario**: Refer back to the specific context (smart home, autonomous vehicle, etc.)
4. **Label your steps**: "Step 1: ... Step 2: ... Therefore: ..."
5. **Quality over quantity**: The exam explicitly states this. Be **concise and precise**.
6. **When asked "why"**: Give the **mechanism**, not just the outcome. "Feature bagging decorrelates trees, making ensemble averaging more effective at reducing variance."

---

# Appendix: Complete Question Index（完整题目索引）

For quick reference, every question across all papers:

| Paper | Q# | Marks | Topic | Key Task |
|-------|----|:-----:|-------|----------|
| 2025 Sample | Q1 | 3 | Symbolic Logic | Modus Tollens + FOL |
| 2025 Sample | Q2 | 2 | LNN | AND computation |
| 2025 Sample | Q3 | 2 | KG | Embeddings + inference |
| 2025 Sample | Q4 | 2 | Robot Soccer | List strategies |
| 2025 Sample | Q5 | 3 | Random Forest | Feature bagging |
| 2025 Sample | Q6 | 3 | MYCIN | Backward chaining |
| 2025 Actual | Q1 | 2 | Symbolic Logic | Modus Tollens (OR variant) + FOL |
| 2025 Actual | Q2 | 3 | LNN | Bounds + OR + safety |
| 2025 Actual | Q3 | 2 | KG / TransE | TransE formula |
| 2025 Actual | Q4 | 2 | Decision Trees | CART greedy |
| 2025 Actual | Q5 | 3 | Fuzzy Logic | Boolean vs Fuzzy |
| 2025 Actual | Q6 | 3 | GA / BigDog | Fitness function design |
| 2026 Sample | Q1 | 5 | Symbolic Logic | Truth table + FOL |
| 2026 Sample | Q2 | 4 | LNN | AND computation (deeper) |
| 2026 Sample | Q3 | 2 | KG | Embeddings + inference |
| 2026 Sample | Q4 | 2 | Robot Soccer | List strategies |
| 2026 Sample | Q5 | 3 | Random Forest | Feature bagging |
| 2026 Sample | Q6 | 4 | Vagueness vs Uncertainty | Classify 4 scenarios |
| 2024 Final | Q1 | 4 | Continual Learning | Concept drift + replay |
| 2024 Final | Q2 | 3 | Search | BFS vs UCS |
| 2024 Final | Q3 | 3 | MCTS | UCB1 formula |
| 2024 Final | Q4 | 1 | RL | State/action/policy/reward |
| 2024 Final | Q5 | 2 | GNN | Permutation invariance |
| 2024 Final | Q6 | 2 | Self-Supervised | Pretext vs downstream |
