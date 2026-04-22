# COMPSCI 713 — A4 Cheatsheet (Double-Sided)

---

## ═══ SIDE 1: FORMULAS & COMPUTATIONS ═══

---

### 1. PROPOSITIONAL LOGIC

**Truth Table (必背):**

| P | Q | ~P | P∧Q | P∨Q | P→Q | P↔Q |
|---|---|----|-----|-----|------|-------|
| 0 | 0 | 1  | 0   | 0   | **1**| 1     |
| 0 | 1 | 1  | 0   | 1   | **1**| 0     |
| 1 | 0 | 0  | 0   | 1   | **0**| 0     |
| 1 | 1 | 0  | 1   | 1   | **1**| 1     |

- **P→Q = ~P ∨ Q** (P→Q is TRUE when P is FALSE! 易错: vacuous truth)
- **🔴 Modus Ponens:** P, P→Q ⊢ Q (已知前提,推结论)
- **🔴🔴 Modus Tollens:** P→Q, ~Q ⊢ ~P (#1 TESTED RULE — 否定后件→否定前件)
- **Hypothetical Syllogism:** P→Q, Q→R ⊢ P→R
- **Resolution:** (P∨Q), (~P∨R) ⊢ (Q∨R)
- **De Morgan:** ~(P∧Q) = ~P∨~Q | ~(P∨Q) = ~P∧~Q

**🔴 Exam Pattern (every year):**
```
Given: rule + negated conclusion
Step 1: Apply Modus Tollens → get negated premise
Step 2: Apply De Morgan's to expand → individual conclusions
Example: (I∧F)→E, ¬E → ¬(I∧F) → ¬I∨¬F
Example: (P∨Q)→R, ¬R → ¬(P∨Q) → ¬P∧¬Q
```
⚠️ Watch the connective! ¬(A∧B)=¬A**∨**¬B but ¬(A∨B)=¬A**∧**¬B — they FLIP!

---

### 2. FIRST-ORDER LOGIC (FOL)

- ~∀x P(x) = ∃x ~P(x) ("not all" = "some not")
- ~∃x P(x) = ∀x ~P(x) ("none" = "all not")
- "All A are B" = ∀x [A(x) → B(x)]
- Its negation = ∃x [A(x) ∧ ~B(x)] (注意: 否定后用 ∧, 不是 →!)

⚠️ 易错: ~∀x P(x) 是"并非所有"，不等于 ∀x ~P(x)"全都不是"

**🔴 FOL + Modus Tollens (2025真题Q1b考过!):**
```
Given: ∀x (Cheat(x) → Disqualified(x)), ¬Disqualified(Alice)
Step 1: Instantiate for Alice: Cheat(Alice) → Disqualified(Alice)
Step 2: Modus Tollens: ¬Disqualified(Alice) → ¬Cheat(Alice)
Conclusion: Alice did not cheat.
```

---

### 3. LNN — Soft Logic T-Norms (3 types)

| T-norm       | AND(a,b)         | OR(a,b)          | NOT(a) |
|-------------|------------------|------------------|--------|
| **Product**     | a × b            | a+b-ab           | 1-a    |
| **Łukasiewicz** | max(0, a+b-1)    | min(1, a+b)      | 1-a    |
| **Gödel**       | min(a, b)        | max(a, b)        | 1-a    |

**Example — AND(0.9, 0.4):**
Product: 0.36 | Łukasiewicz: 0.30 | Gödel: 0.40
→ Łukasiewicz最严格, Gödel最宽松

**Example — OR(0.9, 0.7) with Product:**
0.9 + 0.7 - 0.9×0.7 = 1.6 - 0.63 = **0.97**

**LNN Truth Bounds [L, U] (with threshold α):**
- L≥α, U≥α → **True** | U<α → **False**
- L<α<U → **Uncertain** | L>U → **Contradiction**

**🔴 LNN Bounds for compound formulas (2025真题考过!):**
- **OR bounds:** L_OR = **max**(L_P, L_Q), U_OR = **max**(U_P, U_Q)
- **AND bounds (Gödel/simplified):** L_AND = **min**(L_P, L_Q), U_AND = **min**(U_P, U_Q)
- **AND bounds (Łukasiewicz):** L_AND = **max**(0, L_P+L_Q-1), U_AND = **min**(U_P, U_Q)
- **AND bounds (Product):** L_AND = L_P×L_Q, U_AND = U_P×U_Q
- **Example (2025 actual Q2):** P=[0.8,0.9], Q=[0.3,0.6], Alert ← P∨Q, α=0.7
  L_Alert = max(0.8, 0.3) = **0.8**, U_Alert = max(0.9, 0.6) = **0.9**
  L=0.8 ≥ α=0.7 → **Definitely True** ✅

**Why bounds matter in safety-critical apps (2025考过, 2分!):**
1. Express uncertainty explicitly — confidence level
2. Conservative decision-making — if L < threshold, wait rather than act
3. Robustness to noisy/incomplete data — bounds propagate uncertainty
4. Interpretability — engineers can inspect confidence, improving trust

⚠️⚠️ 最易混淆: **Fuzzy AND = min(A,B)** vs **LNN AND = A×B (Product)**
这是两个不同的系统! Fuzzy用min/max, LNN用乘法/加法!

**LNN vs Boolean:** Boolean只有{0,1}; LNN用[0,1]连续值, 支持梯度学习, 双向推理(bidirectional inference)

---

### 4. FUZZY LOGIC (模糊逻辑)

**Operators (和LNN不同!):**
AND = **min**(A,B) | OR = **max**(A,B) | NOT = 1-A

**Fuzzy Implication:**
- Kleene-Dienes: A→B = max(1-A, B)
- Gödel: A→B = 1 if A≤B, else B

**Fuzzy Pipeline:** Fuzzification → Rule Evaluation → Aggregation → Defuzzification

**Firing strength** of multi-condition rule = min(all conditions)

⚠️ 模糊隶属度 ≠ 概率! μ=0.6 是"属于的程度", 不是"60%可能性"

**🔴 Boolean vs Fuzzy Logic 对比 (2025真题Q5, 3分!):**

| | Boolean Logic | Fuzzy Logic |
|---|---|---|
| Values | {True, False} only | [0, 1] continuous membership |
| AND | Both must be True, else False | min(μ_A, μ_B) |
| Output | Binary yes/no | Suitability score ∈ [0,1] |
| Advantage | Simple, clear-cut | Handles **gradual/vague** concepts |

---

### 5. BAYES' THEOREM & NAIVE BAYES

**Bayes:** P(H|e) = P(e|H) × P(H) / P(e)
where P(e) = P(e|H)P(H) + P(e|~H)P(~H)

**Naive Bayes:** Ĉ = argmax P(C) × ∏P(xᵢ|C)
**Log version (避免下溢):** argmax [log P(C) + Σ log P(xᵢ|C)]

**Naive assumption:** Features are conditionally independent given the class
(不是说features同等重要, 也不是说classes相互独立)

**Base rate fallacy:** 罕见事件 + 高灵敏度测试 = 大量假阳性. Prior很重要!

---

### 6. MYCIN — Confidence Factors (CF)

CF range: **[-1.0, +1.0]** | MYCIN uses **Backward Chaining**(目标驱动)

| Operation | Formula |
|-----------|---------|
| AND premises | CF = **min**(CF_A, CF_B) |
| OR premises  | CF = **max**(CF_A, CF_B) |
| Rule application (链式) | CF(conclusion) = CF(premise) **×** CF(rule) |
| Combine 2 positive rules (合并) | CF₁ + CF₂ × (1 - CF₁) |

**Example:** Rule A: fever(0.8)∧rash(0.6)→measles(CF_rule=0.7)
CF_premise = min(0.8,0.6) = 0.6 → CF_A = 0.6×0.7 = **0.42**
Rule B: contact(0.9)→measles(CF_rule=0.5) → CF_B = 0.9×0.5 = **0.45**
Combined = 0.42 + 0.45×(1-0.42) = 0.42+0.261 = **0.681**

⚠️ 易错: Combine(合并两规则)用加法公式, Chain(链式传递)用乘法. 不要搞混!

**Backward Chaining:** Goal → Find rules → MONITOR(查内存) → FINDOUT(问用户) → Fire rule → Compute CF
**WHY query:** reveals current reasoning goal (为什么问这个问题)
**HOW query:** shows rule chain used to reach conclusion (怎么得出结论)
**E-MYCIN:** domain-independent shell (换知识库就能用于其他领域)
**Knowledge Acquisition Bottleneck:** 专家难以清晰表达推理过程, 规则难以维护

**Forward vs Backward Chaining:**

| | Forward | Backward |
|---|---------|----------|
| Direction | Facts → conclusions | Hypothesis → evidence |
| Driven by | **Data-driven** | **Goal-driven** |
| Uses | Modus Ponens direction | Reverse direction |
| System | Monitoring, alerts | **MYCIN** diagnosis |
| Explains | **HOW** concluded | **WHY** asking |
| Sufficient/Necessary | A sufficient for B | B necessary for A |

---

### 7. DECISION TREES & ENSEMBLES

**Entropy:** H(Y) = -Σ p(y) log₂ p(y)
- Pure: H=0 | Fair coin(0.5,0.5): H=1.0 bit | (0.9,0.1): H=0.469

**Conditional Entropy:** H(Y|X) = Σ P(X=x) × H(Y|X=x)
**Information Gain:** IG(Y|X) = H(Y) - H(Y|X) ≥ 0
**Gini Impurity:** G(t) = 1 - Σ pᵢ²
**Gini of Split:** G_split = (n₁/n)G(D₁) + (n₂/n)G(D₂)

| Algorithm | Split Metric | Tree Type |
|-----------|-------------|-----------|
| **ID3**   | Entropy/IG  | Multi-way |
| **C4.5**  | Entropy/IG  | Multi-way, handles continuous |
| **CART**  | **Gini**    | **Binary** only |

**AdaBoost:**
- αₜ = ½ ln((1-εₜ)/εₜ) — low error → large α → more vote power
- wᵢ ← wᵢ × exp(2αₜ × I[wrong]) — misclassified get heavier weight
- H(x) = sign(Σ αₜhₜ(x)) — weighted majority vote

**Random Forest** = Bootstrap sampling + **Feature bagging**(每次只用 √p 个特征)
225 features → **15** per split | 400 features → **20** per split
Purpose: decorrelate trees → reduce **variance**

**🔴 CART is "greedy" (2025真题考过, 2分!):**
At each node, picks the **best-performing split** for impurity reduction **without any look-ahead**. No effort to find an optimal tree — just **maximal local decision** at each step.
⚠️ 必须提到 **no look-ahead / no global optimization**

**Bagging vs Boosting:**

| | Bagging | Boosting |
|---|---------|---------|
| Training | Independent, **parallel** | **Sequential** |
| Reduces | **Variance** | **Bias** |
| Base learner | Full trees | Weak learners (stumps) |
| Combination | Majority vote / average | **Weighted** vote |
| Errors | Equal weight | Upweight misclassified |
| Example | **Random Forest** | **AdaBoost**, XGBoost |

⚠️ Random Forest = Bagging + **Feature Bagging** (不只是bagging!)

---

### 8. KNOWLEDGE GRAPHS & TransE

**KG = (E, R, T):** Entities, Relations, Triples ⊂ E×R×E
**RDF triple:** (Subject, Predicate, Object) = (h, r, t)

**TransE:** h + r ≈ t → f(h,r,t) = ‖h+r-t‖ (越小越可能为真)
**L1 distance:** Σ|hᵢ + rᵢ - tᵢ|
**Link prediction:** (h, r, ?) → compute h+r, find closest entity

**Limitation:** 1-to-N relations fail (多个实体映射到同一点)
**TransH** = hyperplane projection | **TransR** = relation-specific space

**KG Inference 3 types:** Rule-based, Path-based, Embedding-based
**Ontology = schema** vs **KG = data** | **RDF = facts** vs **OWL = logic+ontology**

---

## ═══ SIDE 2: KEY DISTINCTIONS & CONCEPTS ═══

---

### 9. VAGUENESS vs UNCERTAINTY (考试最爱考!)

| | Vagueness(模糊性) | Uncertainty(不确定性) |
|---|-----------|------------|
| Question | "To what degree?" | "How likely?" |
| Nature | Concept boundaries blurry | Fact unknown but exists |
| Tool | **Fuzzy Logic** | **Bayesian/Probability** |
| Examples | "high risk", "almost excellent", "mildly obese" | alarm→burglary?, spam classification |

**判断方法:** 有一个确定但未知的事实? → Uncertainty. 概念本身边界模糊? → Vagueness.

---

### 10. BOOLEAN vs FUZZY vs LNN (三者区别!)

| | Boolean | Fuzzy Logic | LNN |
|---|---------|-------|-----|
| Values | {0, 1} | [0, 1] | [0, 1] with bounds [L,U] |
| AND | classical | **min**(A,B) | A×B **(Product)** |
| OR | classical | **max**(A,B) | A+B-AB **(Product)** |
| Learning | None | Manual rules | **Gradient-based** |
| Inference | — | Forward only | **Bidirectional** |
| Handles | Crisp facts | **Vagueness** | Vagueness + **learns** |

---

### 11. KNOWLEDGE REPRESENTATION METHODS

| | Expert System | Semantic Network | Frames | Ontology | Knowledge Graph |
|---|---|---|---|---|---|
| Core | IF-THEN rules | Node-edge graph | Slot-filler | Formal schema(OWL) | RDF triples |
| Strength | Explainable | IS-A inference | Inheritance | Classification | **Scalable** |
| Weakness | ~10K rules max | No standard | Rigid | NP-hard | Incomplete |

**DIKW:** Data → Information → Knowledge → Wisdom
**Expert System = 3 parts:** Knowledge Base + Inference Engine + User Interface
**RAG:** Response = LLM(Query + Retrieve(Q, KB)) — reduces hallucination

---

### 12. EMBODIED AI

**Core:** Intelligence = acting robustly in the world, not abstract reasoning.
Brooks (1990) "Elephants Don't Play Chess": build **upward from situated competence**.

**Polly (1993)** — 64×48 image, 15fps, MIT corridor tours:

| Simplifying Assumption | Shortcut |
|---|---|
| Uniform carpet | Non-carpet = obstacle |
| Ground-plane constraint | Higher in image = farther |
| Corridor geometry | Constrains landmark search |

→ Design principle: don't solve the hardest problem if environment offers easier one

**Allen — Layered Control (3 layers, run simultaneously, forces summed):**

| Layer | Behavior | Mechanism |
|---|---|---|
| L0 Avoid | Dodge obstacles | Repulsive force ∝ 1/d² |
| L1 Wander | Random walk | Random direction ~10s |
| L2 Explore | Seek open space | Head toward widest opening |

**BigDog:** 2-level control (low=joints, high=body+gait), 3 gaits (crawl/walk/trot)
Dynamic balancing = same class as NEAT's pole-balancing task!

---

### 13. AI TEAMS & SWARMS

**STEAM — Joint Persistent Goal (JPG):**
Team pursues JPG until: **A**chieved, **U**nachievable, or **I**rrelevant
If one agent concludes A/U/I → **must communicate** → create mutual belief
Core = **communicate**, not just act

**Flocking — Reynolds' 3 Rules (1987):**
R1: **Collision avoidance** — stay ≥ min distance
R2: **Flock centering** — stay close to group
R3: **Velocity matching** — align speed **and direction** with neighbors
→ Demonstrates **emergence**: complex global from simple local, **no central controller**

**Robot Soccer — 3 strategies:**
1. **Collective behaviours** — coordinated plays, passing risk assessment
2. **Positioning** — formation choice (e.g., 2-1-2)
3. **Role-based** — dynamic roles (goalie/attacker/defender)
⚠️ "They work together" = 0 marks. Must name **specific strategies**!

---

### 14. NEAT & GENETIC ALGORITHMS

**GA cycle:** Init → Evaluate → Select → Crossover → Mutate → Repeat

**NEAT = GA for evolving neural networks (structure + weights):**
- Starts **minimal** (inputs→outputs, NO hidden nodes)
- **Genome:** Node genes + Connection genes (In, Out, Weight, Enabled, **Innovation#**)

**2 structural mutations:**

| Mutation | How | Key Detail |
|---|---|---|
| **Add Connection** | New edge, gets **Innovation#** | Random weight, can be **recurrent** |
| **Add Node** | Disable A→B; insert C: A→C→B | Weight in = **1.0**, out = **old weight** → behavior unchanged |

**Crossover — aligned by Innovation#:**
- **Matching** genes → random parent
- **Disjoint** genes (within range) → from **fitter** parent
- **Excess** genes (beyond range) → from **fitter** parent

**Speciation formula:**
$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$
E=excess, D=disjoint, W̄=avg weight diff of **matching** genes, N=larger genome
δ < δₜ → same species | δ ≥ δₜ → different species

**Adjusted fitness:** f'ᵢ = fᵢ / |S| (fitness / species size)
→ Prevents large species monopolizing; small innovative species get fair quota

**🔴 GA Fitness Function Design (2025真题Q6, 3分!):**
Fitness = -Σ(|error_speed| + |error_direction| + |error_height|) over simulation time steps
+ Keep pitch, yaw, roll within bounds. Higher = better.

⚠️ NEAT does **NOT** use backpropagation — weights evolved via GA
⚠️ NEAT starts **MINIMAL** — complexity added only when needed

---

### 15. COMMON TRAPS SUMMARY (易错总结)

| Trap | Wrong ❌ | Correct ✅ |
|------|---------|-----------|
| FOL negation | ∀x ~P(x) | **∃x ~P(x)** |
| De Morgan ¬(A∧B) | ¬A∧¬B | **¬A∨¬B** (flip!) |
| Fuzzy AND | A×B | **min**(A,B) |
| LNN AND (Product) | min(A,B) | **A×B** |
| Bagging reduces | Bias | **Variance** |
| Boosting reduces | Variance | **Bias** |
| CF combine | CF₁ × CF₂ | **CF₁ + CF₂(1-CF₁)** |
| μ=0.6 means | 60% probability | **degree of membership** |
| RF = | just bagging | bagging + **feature bagging** |
| NEAT start | complex, prune down | **minimal**, grow up |
| NEAT uses | backpropagation | **GA** (crossover + mutation) |
| NEAT Add Node wt in | random | **1.0** (preserve behavior) |
| Disjoint vs Excess | same thing | Disjoint=**middle** gaps, Excess=**end** overhang |
| W̄ in speciation | total weight | avg wt diff of **matching** genes |
| Flocking | central controller | **no** central, **emergence** |
| Polly | full world model | **appearance-based**, simplifying assumptions |
| Sufficient/Necessary | interchangeable | A sufficient for B ≠ A necessary for B |

---

### 16. CROSS-TOPIC CONNECTIONS (考试加分!)

| Connection | Why |
|---|---|
| BigDog balancing ↔ NEAT pole balancing | Same control problem class |
| Fuzzy Logic ↔ Embodied AI | Soft computing for robot shortcuts |
| NEAT ↔ Reinforcement Learning | Fitness from simulation = RL reward |
| Flocking emergence ↔ GA population | Simple local → complex global |
| Expert Systems bottleneck ↔ NEAT | NEAT auto-discovers; expert systems need manual rules |
| Brooks layered ↔ MYCIN backward | Layered=parallel, MYCIN=sequential goal-driven |

---

### 17. EXAM STRATEGY (答题技巧)

**🔴 2025 vs 2026 Sample — 真题会变!**

| 2026 Sample | 2025 Actual | Change |
|---|---|---|
| Q1a: (I∧F)→E, ¬E | Q1a: (P∨Q)→R, ¬R | Swapped ∧→∨ |
| Q1b: ¬∀x Fly(x) | Q1b: FOL + Modus Tollens | Added reasoning |
| Q2: LNN AND | Q2: LNN OR + bounds [L,U] | Changed operator |
| Q4: Robot soccer | Q4: CART "greedy" | Changed topic! |
| Q5: Vagueness vs Uncertainty | Q5: Boolean vs Fuzzy | Changed comparison |
| Q6: Vagueness (4 items) | Q6: GA fitness for BigDog | Completely new! |

**Key strategies:**
- Don't just memorize sample answers — concepts will be tested differently
- Quality > Quantity: 2-4 precise sentences per mark
- "Explain then Compute" — concept first, calculation second
- Show ALL steps in calculations — partial credit for process
- CF: Combine(两规则→同一结论)=加法 vs Chain(链式传递)=乘法

**Topics not in sample but COULD appear (prepare!):**
MYCIN CF calculation | Entropy/IG calculation | Naive Bayes calculation | NEAT speciation formula | Ablation study | Backward chaining process | Embodied AI assumptions
