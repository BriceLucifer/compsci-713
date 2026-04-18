# COMPSCI 713 — A4 Cheatsheet (Double-Sided)

---

## ═══ SIDE 1: FORMULAS & COMPUTATIONS ═══

---

### 1. PROPOSITIONAL LOGIC

**Truth Table (必背):**

| P | Q | ~P | P^Q | PvQ | P->Q | P<->Q |
|---|---|----|-----|-----|------|-------|
| 0 | 0 | 1  | 0   | 0   | **1**| 1     |
| 0 | 1 | 1  | 0   | 1   | **1**| 0     |
| 1 | 0 | 0  | 0   | 1   | **0**| 0     |
| 1 | 1 | 0  | 1   | 1   | **1**| 1     |

- **P->Q = ~P v Q**  (P->Q is TRUE when P is FALSE! 易错: 虚真/vacuous truth)
- **Modus Ponens:** P, P->Q ⊢ Q  (已知前提,推结论)
- **Modus Tollens:** P->Q, ~Q ⊢ ~P  (否定后件,推否定前件)
- **Hypothetical Syllogism:** P->Q, Q->R ⊢ P->R
- **Resolution:** (PvQ), (~PvR) ⊢ (QvR)
- **De Morgan:** ~(P^Q)= ~Pv~Q | ~(PvQ)= ~P^~Q

---

### 2. FIRST-ORDER LOGIC (FOL)

- ~∀x P(x) = ∃x ~P(x)  ("not all" = "some not")
- ~∃x P(x) = ∀x ~P(x)  ("none" = "all not")
- "All A are B" = ∀x [A(x) -> B(x)]
- 其否定(negation) = ∃x [A(x) ^ ~B(x)]  (注意: 否定后用 ^, 不是 ->!)

⚠️ 易错: ~∀x P(x) 是"并非所有"，不等于 ∀x ~P(x)"全都不是"

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
- L≥α, U≥α → **True** | L≤α, U≤α → **False**
- L<α<U → **Uncertain** | L>U → **Contradiction**

⚠️⚠️ 最易混淆: **Fuzzy AND = min(A,B)** vs **LNN AND = A×B (Product)**
这是两个不同的系统! Fuzzy用min/max, LNN用乘法/加法!

**LNN vs Boolean:** Boolean只有{0,1}; LNN用[0,1]连续值, 支持梯度学习, 双向推理(bidirectional inference)

---

### 4. FUZZY LOGIC (模糊逻辑)

**Operators (和LNN不同!):**
AND = **min**(A,B) | OR = **max**(A,B) | NOT = 1-A

**Fuzzy Implication:**
- Kleene-Dienes: A->B = max(1-A, B)
- Gödel: A->B = 1 if A≤B, else B

**Fuzzy Pipeline:** Fuzzification(输入转模糊) → Rule Evaluation(规则评估) → Aggregation(聚合) → Defuzzification(输出转精确值)

**Firing strength**(触发强度) of multi-condition rule = min(all conditions)

⚠️ 模糊隶属度 ≠ 概率! μ=0.6 是"属于的程度", 不是"60%可能性"

---

### 5. BAYES' THEOREM & NAIVE BAYES

**Bayes:** P(H|e) = P(e|H) × P(H) / P(e)
where P(e) = P(e|H)P(H) + P(e|~H)P(~H)

**Naive Bayes:** Ĉ = argmax P(C) × ∏P(xᵢ|C)
**Log version (避免下溢):** argmax [log P(C) + Σ log P(xᵢ|C)]

**Naive assumption:** Features are conditionally independent given the class
(不是说features同等重要, 也不是说classes相互独立)

**Base rate fallacy(基率谬误):** 罕见事件 + 高灵敏度测试 = 大量假阳性. Prior很重要!

---

### 6. MYCIN — Confidence Factors (CF)

CF range: **[-1.0, +1.0]** | MYCIN uses **Backward Chaining**(目标驱动)

| Operation | Formula |
|-----------|---------|
| AND premises | CF = **min**(CF_A, CF_B) |
| OR premises  | CF = **max**(CF_A, CF_B) |
| Rule application (链式) | CF(conclusion) = CF(premise) **×** CF(rule) |
| Combine 2 positive rules (合并) | CF₁ + CF₂ × (1 - CF₁) |

**Example:** Rule A: fever(0.8)^rash(0.6)->measles(CF_rule=0.7)
CF_premise = min(0.8,0.6) = 0.6 → CF_A = 0.6×0.7 = **0.42**
Rule B: contact(0.9)->measles(CF_rule=0.5) → CF_B = 0.9×0.5 = **0.45**
Combined = 0.42 + 0.45×(1-0.42) = 0.42+0.261 = **0.681**

⚠️ 易错: Combine(合并两条规则)用加法公式, Chain(链式传递)用乘法. 不要搞混!

**Backward Chaining Process:** Goal → Find rules → MONITOR(查内存) → FINDOUT(问用户) → Fire rule → Compute CF
**WHY query:** reveals current reasoning goal (为什么问这个问题)
**HOW query:** shows rule chain used to reach conclusion (怎么得出结论)
**E-MYCIN:** domain-independent shell (空壳, 换知识库就能用于其他领域)
**Knowledge Acquisition Bottleneck(知识获取瓶颈):** 专家难以清晰表达推理过程, 规则难以维护

---

### 7. DECISION TREES & ENSEMBLES

**Entropy(信息熵):** H(Y) = -Σ p(y) log₂ p(y)
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
- αₜ = ½ ln((1-εₜ)/εₜ)  — low error → large α → more vote power
- wᵢ ← wᵢ × exp(2αₜ × I[wrong])  — misclassified get heavier weight
- H(x) = sign(Σ αₜhₜ(x))  — weighted majority vote

**Random Forest** = Bootstrap sampling + **Feature bagging**(每次只用 sqrt(p) 个特征)
225 features → **15** per split | 400 features → **20** per split
Purpose: decorrelate trees → reduce **variance**

**Bias(偏差):** 模型过于简单, 系统性偏离真实值 (underfitting)
**Variance(方差):** 模型对数据过于敏感, 不同数据集结果差异大 (overfitting)

---

### 8. KNOWLEDGE GRAPHS & TransE

**KG = (E, R, T):** Entities, Relations, Triples ⊂ E×R×E
**RDF triple:** (Subject, Predicate, Object) = (h, r, t)

**TransE:** h + r ≈ t → f(h,r,t) = ‖h+r-t‖ (越小越可能为真)
**L1 distance:** Σ|hᵢ + rᵢ - tᵢ|
**Link prediction:** (h, r, ?) → compute h+r, find closest entity

**Limitation:** 1-to-N relations fail (多个实体被迫映射到同一点)
**TransH** = hyperplane projection | **TransR** = relation-specific space

**KG Inference 3 types:** Rule-based(规则), Path-based(路径遍历), Embedding-based(向量)

---

## ═══ SIDE 2: KEY DISTINCTIONS & CONCEPTS ═══

---

### 9. VAGUENESS vs UNCERTAINTY (考试最爱考!)

| | Vagueness(模糊性) | Uncertainty(不确定性) |
|---|-----------|------------|
| 问题 | "To what degree?"(程度多少) | "How likely?"(可能性多大) |
| 本质 | 概念边界模糊 | 事实未知但确定存在 |
| 工具 | Fuzzy Logic | Bayesian/Probability |
| 例子 | "high risk", "almost excellent", "mildly obese" | alarm→burglary?, spam classification |

**判断方法:** 有一个确定但未知的事实? → Uncertainty. 概念本身边界模糊? → Vagueness.

---

### 10. BAGGING vs BOOSTING (必考对比!)

| | Bagging | Boosting |
|---|---------|---------|
| 训练方式 | Independent, **parallel** | **Sequential** |
| 降低 | **Variance**(方差) | **Bias**(偏差) |
| Base learner | Full trees | Weak learner (stumps) |
| 组合方式 | Majority vote / average | **Weighted** vote |
| 错误处理 | Equal weight | Upweight misclassified |
| Example | **Random Forest** | **AdaBoost**, XGBoost, Gradient Boosting |

⚠️ Random Forest = Bagging + **Feature Bagging** (不只是bagging!)
⚠️ AdaBoost adds stumps; **Gradient Boosting** adds full trees fitting **residuals**(残差)

---

### 11. FORWARD vs BACKWARD CHAINING

| | Forward Chaining | Backward Chaining |
|---|---------|----------|
| 方向 | Facts → conclusions | Hypothesis → evidence |
| 驱动 | **Data-driven**(数据驱动) | **Goal-driven**(目标驱动) |
| 推理 | Modus Ponens direction | Reverse direction |
| 用途 | Monitoring, alerts | **MYCIN** diagnosis |
| 解释 | **HOW** query | **WHY** query |

---

### 12. BOOLEAN vs FUZZY vs LNN (三者区别!)

| | Boolean | Fuzzy Logic | LNN |
|---|---------|-------|-----|
| Values | {0, 1} | [0, 1] | [0, 1] with bounds [L,U] |
| AND | classical AND | **min**(A,B) | A×B **(Product)** |
| OR | classical OR | **max**(A,B) | A+B-AB **(Product)** |
| Learning | None | Manual rules | **Gradient-based** |
| Inference | — | Forward only | **Bidirectional** |
| Handles | Crisp facts | **Vagueness** | Vagueness + **learns** |

---

### 13. KNOWLEDGE REPRESENTATION METHODS

| | Expert System | Semantic Network | Frames | Ontology | Knowledge Graph |
|---|---|---|---|---|---|
| 核心 | IF-THEN rules | Node-edge graph | Slot-filler | Formal schema(OWL) | RDF triples |
| 优势 | Explainable | IS-A inference | Inheritance, defaults | Classification | **Scalable**(billions) |
| 劣势 | 难扩展(~10K rules) | No standardization | Rigid structure | NP-hard reasoning | Incomplete data |
| Example | MYCIN | — | — | Gene Ontology | Wikidata |

**Ontology = schema**(什么类型的事实是合法的) vs **KG = data**(具体有哪些事实)
**RDF = facts**(三元组数据) vs **OWL = logic + ontology**(在RDF上加逻辑推理)
**SPARQL** = query language for RDF | **Cypher** = query language for Neo4j

---

### 14. KNOWLEDGE FUNDAMENTALS

**DIKW:** Data → Information → Knowledge → Wisdom
**5 KR Requirements:** Expressiveness, Computational Efficiency, Scalability, Interpretability, Modifiability
**Expert System = 3 parts:** Knowledge Base(知识库) + Inference Engine(推理引擎) + User Interface(用户界面)
**RAG:** Response = LLM(Query + Retrieve(Q, KB)) — 减少幻觉(hallucination), 无需更新权重

**KG Construction Pipeline:**
Entity Extraction(NER) → Relation Extraction(RE) → Knowledge Integration(实体对齐) → Storage & Query

---

### 15. MULTI-AGENT (Robot Soccer)

All robots share overhead camera view, **no direct communication**.
3 strategy levels:
1. **Collective behaviour(集体行为):** Passing strategy — evaluate passing points by interception risk & position value
2. **Positioning(阵型):** Choose formation (e.g., 2-1-2) for attack/defense
3. **Role-based(角色分配):** Dynamic roles (goalie/attacker/defender) based on game state

⚠️ 答题要具体! "They work together" = 0 marks. 写出具体策略名称.

---

### 16. EXAM STRATEGY (答题技巧)

- **Quality > Quantity:** 每分写2-4句精练句子, 不要长篇大论
- **"Explain then Compute":** 先解释概念, 再计算. 不要只算不解释
- **Scenario-based:** 所有题目都包装在场景中, 要在场景中应用方法
- **Distinguish concepts:** 老师爱考"X和Y有什么区别?" — 准备对比表
- **Show all steps:** 计算题展示每一步, 算错也有过程分
- **Sample test以外的内容也会考:** MYCIN CF, Entropy/IG, Fuzzy computation
- **FOL negation:** ∀x[A(x)->B(x)] 的否定是 ∃x[A(x) ^ ~B(x)], 用^不用->!
- **CF combine vs chain:** Combine(两规则指向同一结论)用加法公式; Chain(链式传递)用乘法

### COMMON TRAPS SUMMARY (易错总结)

| Trap | Wrong ❌ | Correct ✅ |
|------|---------|-----------|
| FOL negation | ∀x ~P(x) | ∃x ~P(x) |
| Fuzzy AND | A×B | **min**(A,B) |
| LNN AND | min(A,B) | **A×B** (Product) |
| Bagging reduces | Bias | **Variance** |
| Boosting reduces | Variance | **Bias** |
| CF combine | CF₁ × CF₂ | CF₁ + CF₂(1-CF₁) |
| μ=0.6 means | 60% probability | degree of membership |
| RF = | just bagging | bagging + **feature bagging** |
