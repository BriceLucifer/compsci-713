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

**🔴 FOL + Modus Tollens (2025真题Q1b考过!):**
Given: ∀x (Cheat(x) → Disqualified(x)), ¬Disqualified(Alice)
Step 1: Instantiate for Alice: Cheat(Alice) → Disqualified(Alice)
Step 2: Modus Tollens: ¬Disqualified(Alice) → **¬Cheat(Alice)**
Conclusion: Alice did not cheat.

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
- **AND bounds:** L_AND = **min**(L_P, L_Q), U_AND = **min**(U_P, U_Q) *(simplified; exact depends on t-norm)*
- **Example (2025 actual Q2):** P=[0.8,0.9], Q=[0.3,0.6], Alert ← P∨Q, α=0.7
  L_Alert = max(0.8, 0.3) = **0.8**, U_Alert = max(0.9, 0.6) = **0.9**
  L=0.8 ≥ α=0.7 → **Definitely True** ✅

**Why bounds matter in safety-critical apps (2025考过, 2分!):**
1. **Express uncertainty explicitly** — how confident the system is
2. **Conservative decision-making** — if L < threshold, wait/slow down rather than act on overconfident estimate
3. **Robustness to noisy/incomplete data** — bounds propagate uncertainty through the system
4. **Interpretability** — engineers can inspect confidence level, improving trust

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

**🔴 Boolean vs Fuzzy Logic 对比 (2025真题Q5, 3分!):**
Example rule: IF STRONG AND HEAVY THEN HAMMER_THROWER

| | Boolean Logic | Fuzzy Logic |
|---|---|---|
| Values | {True, False} only | [0, 1] continuous membership |
| STRONG | True or False (binary threshold) | μ_s ∈ [0,1] (degree of strongness) |
| AND | Both must be True, else False | min(μ_s, μ_h) or product |
| Output | Suitable or Not (binary) | Suitability score ∈ [0,1] |
| Advantage | Simple, clear-cut | Handles **gradual** concepts |

→ Fuzzy gives a **suitability score anywhere in [0,1]**, not just yes/no

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

**🔴 CART is "greedy" (2025真题考过, 2分!):**
At each node, CART evaluates ALL features and ALL split points, picks the **best-performing split** for impurity reduction **without any look-ahead**. There is no effort to find an optimal tree overall — just a **maximal local decision** at each step. Then it recurses on each sub-tree.
⚠️ 只说"maximize impurity reduction"不给满分! 必须提到 **no look-ahead / no global optimization**

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

### 15. EMBODIED AI (Lecture 12, Part 1)

**Core idea:** Intelligence = **acting robustly in the world**, not abstract reasoning.
Brooks (1990) "Elephants Don't Play Chess": build **upward from situated competence**, not down from symbolic AI.
Evolution: ~1B yrs simple life → Cambrian Explosion → human intelligence only ~1M yrs. Study cockroaches first!

**Polly (Horswill, 1993)** — 1st visually navigated robot at animal speed (~1m/s), MIT AI Lab tours:

| Simplifying Assumption | Shortcut Gained |
|---|---|
| Uniform un-patterned carpet | Non-carpet = obstacle (no object recognition) |
| Ground-plane constraint | Higher in image = farther away (no depth sensor) |
| Corridor geometry | Constrains landmark positions → smaller search space |

- **64×48** image / 66ms → Boolean precepts (`open-left?` `blocked?` `wall-ahead?` `vanishing-point`)
- Navigation: stored **landmark frames** + **rotational odometry** + **district recognition**
- Tour requested by **waving a foot** (camera at foot level, no speech)
- **Design principle: don't solve the hardest problem if the environment offers an easier one**

**Allen — Layered Control (Brooks, 1986):** sonar sensors, 3 concurrent layers:

| Layer | Behavior | Mechanism |
|---|---|---|
| L0 Avoid | Dodge obstacles | Repulsive force ∝ **1/d²** |
| L1 Wander | Random walk | Pick random direction ~10s |
| L2 Explore | Seek open space | Head toward widest opening |

All layers **run simultaneously**, forces **summed** → no master plan, no world model, robust behavior

**Other Brooks robots:** Squirt (seek dark corners, react to noise), Herbert (steal soda cans), Genghis (6-leg **loose control** — legs not coordinated, yet walks + follows IR)

**BigDog (Boston Dynamics, 2008):** rough-terrain quadruped, **109 kg**, hydraulic pump from 2-stroke engine

| Control Level | Manages |
|---|---|
| **Low-level** | Individual joint position & force |
| **High-level** | Body speed, attitude (pitch/yaw/roll), gait selection |

- **3 gaits:** crawl (steep/slippery) → walk → trot (speed)
- Dynamic balancing = same class as NEAT's **pole-balancing** task! (→ see §16)
- Prototype **very loud** → military lost interest. Still viable for **search-and-rescue, hazardous inspection, mine clearing**

**Mars Rovers:** autonomy needed because of **signal delay** (minutes to Earth)
- Stereo cameras (terrain map) + wheel odometers (slip on sand!) + inertial sensors + sun heading
- Can plan path, adapt dynamically, respect human-labeled no-go areas
- Conservative engineering: survive radiation, extreme temps, precious power, move very slowly
- **Ingenuity helicopter:** planned for 5 flights → completed **72**

**Conclusion (Part 1):** Embodied AI platforms support higher-level apps (CNN vision, speech, LLMs). But animals still dominate on agility, robustness, energy efficiency. Gap between demos and products remains large.

---

### 16. AI TEAMS & SWARMS (Lecture 12, Part 2)

**Joint Reasoning — Tambe (1997):** distributed team planning (attack helicopters).
Problem: brittle plans fail silently (scout destroyed → everyone waits forever)

**STEAM (Shell for TEAMwork) — Joint Persistent Goal (JPG):**
- Team pursues JPG until: **A**chieved, **U**nachievable, or **I**rrelevant
- If one agent concludes A/U/I → **must communicate** → create **mutual belief** for entire team
- Core commitment = **communicate**, not just act
- Example: detect SAM battery → mission unachievable → don't just fly home, **tell the team!**

**Flocking — Reynolds' 3 Rules (1987):**

| Rule | Name | Description |
|---|---|---|
| R1 | **Collision avoidance** | Stay ≥ min distance from nearby flockmates |
| R2 | **Flock centering** | Stay close to group, don't drift away |
| R3 | **Velocity matching** | Align speed **and direction** with neighbors |

- Demonstrates **emergence（涌现）**: complex global patterns from simple **local** rules, **no central controller**
- = **agent-based modelling** (also: epidemiology, social networks)
- Boids implementation (Hermellin & Michel 2017): **5 params** (FOV, separation dist, cohesion threshold, max speed, max rotation) + **3 agent attrs** (heading, speed, nearest-neighbor list)
- Small parameter changes → dramatically different emergent behavior

**Robot Soccer — 3 coordination strategies:**

| Strategy | What | Key Detail |
|---|---|---|
| **Collective behaviours** | Coordinated plays (passing) | Score passing points by interception risk + position value |
| **Positioning** | Formation choice | e.g., 2-1-2 for balanced attack/defense coverage |
| **Role-based** | Dynamic roles | Goalie/attacker/defender based on game state |

- Coordination depends on league rules: shared WiFi? Overhead camera? Direct signals or body language?
- Works best when teammates **perceive situation similarly**
- Each robot may only have rough **probabilistic model** (unstable walking platform, narrow FOV)

| Centralized | Decentralized |
|---|---|
| One controller, single point of failure | Each agent decides locally |
| All info flows to center | Only local info exchange |
| Limited scalability | Scales to thousands (flocking) |

⚠️ 答题要具体! "They work together" = 0 marks. Must name **specific strategies** (collective/positioning/role-based).

---

### 17. NEAT & GENETIC ALGORITHMS (Lecture 11)

**GA = evolutionary search** inspired by Darwin's natural selection:
```
Init random population → Evaluate fitness → Select → Crossover → Mutate → New generation → Repeat
```

| GA Term | Meaning |
|---|---|
| **Population** | Set of N candidate solutions (individuals) |
| **Chromosome** | One individual = string of genes |
| **Gene** | Smallest encoding unit (bit, weight, etc.) |
| **Fitness function** | Evaluates how good an individual is |
| **Selection** | Fittest survive to reproduce |
| **Crossover** | Mix 2 parents' genes → offspring |
| **Mutation** | Random gene change (rate ~0.01-0.001) |
| **Elitism** | Best individuals pass to next gen unchanged |

**Crossover types:** Single-point (split at one point, swap halves) | Uniform (each gene randomly from either parent)
Not all individuals undergo crossover. GA has MANY tunable params (operators, rates, pop size, fitness design).
**GA applications:** scheduling, portfolio optimization, vehicle routing, protein folding — vast search spaces where BFS/DFS impractical

**NEAT (Stanley & Miikkulainen, 2002) = GA for evolving neural networks (structure + weights):**
- **Genome** encodes: **Node genes** (ID, type: Sensor/Output/Hidden) + **Connection genes** (In, Out, Weight, Enabled, **Innovation#**)
- Starts from **minimal network** (inputs → outputs, NO hidden nodes)
- Complexity grows **incrementally** through structural mutation

**NEAT's 2 structural mutations:**

| Mutation | How | Key Detail |
|---|---|---|
| **Add Connection** | New edge between existing nodes | Gets **Innovation Number** + random weight. Can be **recurrent** (→ memory!) |
| **Add Node** | Disable A→B; insert C: A→C→B | Weight into C = **1.0**, out of C = **original weight** → behavior **unchanged** |

**NEAT Crossover — aligned by Innovation Number:**
- **Matching** genes (both parents have same Inn#) → random parent
- **Disjoint** genes (non-matching, within range) → from **fitter** parent
- **Excess** genes (beyond shorter genome) → from **fitter** parent
- Equal fitness → random. Disabled genes: small chance re-enable

**Speciation — protect structural innovation from premature elimination:**

$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$

| Symbol | Meaning |
|---|---|
| E | # excess genes |
| D | # disjoint genes |
| $\overline{W}$ | Avg weight diff of **matching** genes |
| N | Larger genome size |
| $c_1, c_2, c_3$ | Configurable coefficients |

$\delta < \delta_t$ → same species | $\delta \geq \delta_t$ → different species

**Adjusted fitness:** $f'_i = f_i / |S|$ (individual fitness / species size)
→ Large species don't monopolize; small innovative species get fair quota
→ Breeding quota per species ∝ **sum of adjusted fitness**
→ Example: Species A (5 members, fitness 10,8,6,12,9 → adj sum=9) vs Species B (2 members, 10,8 → adj sum=9) → **equal quota 1:1**

**Double Pole Balancing (evaluation task):**
- Cart on limited track balances 2 poles of different lengths
- **Fitness = time steps survived** (+ penalty for oscillation)
- Hard version: no velocity/angular-velocity inputs → needs **recurrent node** to compute $\Delta\theta/\Delta t$
- Connects to BigDog's dynamic balancing (→ see §15)!

**Ablation study** (remove component, compare to full system):

| Ablated | Result | Shows importance of... |
|---|---|---|
| Fixed fully-connected network | Slower/failed | Topology evolution |
| Start from larger network | Slower | Minimal initialization |
| Disable speciation | Slower/failed | Protecting innovation |
| Disable crossover (mutation only) | Slower | Recombination |

**NEAT applications:** game AI (Flappy Bird, Pac-Man, Monopoly), robot control, scheduling
→ Generates **small, interpretable** networks (useful for explainability)

**🔴 GA Fitness Function Design (2025真题Q6, 3分! BigDog walking robot):**
Q: Design fitness for GA that trains BigDog's leg controller.
Inputs: desired speed, direction, target height. Available: actual speed, direction, height, attitude (pitch/yaw/roll).
**Key fitness elements:**
1. |target speed - actual speed| → minimize
2. |target direction - actual direction| → minimize
3. |target height - actual height| → minimize
4. Keep pitch, yaw, roll within acceptable bounds
5. Sum over time steps across simulation run

**Fitness = -Σ(|error_speed| + |error_direction| + |error_height|)** (negated so higher = better)
→ Highest fitness when all errors are low across the simulation (reinforcement learning style)

⚠️ NEAT does **NOT** use backpropagation — weights evolved via GA crossover + mutation
⚠️ NEAT starts **MINIMAL** — complexity added only when needed (not pruned from large)

---

### 18. EXAM STRATEGY (答题技巧)

**🔴🔴 2025真题 vs 2026 Sample 对比 — 实际考试会变题!**

| 2026 Sample | 2025 Actual | 变化模式 |
|---|---|---|
| Q1a: (I∧F)→E, ¬E | Q1a: **(P∨Q)→R, ¬R** | 换连词(∧→∨), 结论不同! |
| Q1b: ¬∀x Fly(x) | Q1b: **FOL + Modus Tollens** | 加推理步骤 |
| Q2: LNN AND computation | Q2: **LNN OR + bounds [L,U]** | 换运算符, 加bounds判断! |
| Q4: Robot soccer | Q4: **CART "greedy"** | 完全换topic! |
| Q5: Vagueness vs Uncertainty | Q5: **Boolean vs Fuzzy** | 换对比对象 |
| Q6: Vagueness (4 items) | Q6: **GA fitness for BigDog** | 完全新题! |

**应对策略:**
- **不要只背 sample test 答案!** 真题会换连词、换运算符、换 topic
- **Quality > Quantity:** 每分写2-4句精练句子, 不要长篇大论
- **"Explain then Compute":** 先解释概念, 再计算. 不要只算不解释
- **CART "greedy"必须说 no look-ahead**, 不要只说 maximize impurity reduction
- **LNN bounds: 要会算 OR 和 AND 的 bounds**, 不只是单个值的 t-norm 计算
- **GA fitness function 设计题**: 列出要 minimize 的差异项, 说明 sum over simulation time steps
- **FOL: 准备好 instantiation + Modus Tollens** 推理链, 不只是 negation
- **Boolean vs Fuzzy 对比**: 要给出具体例子, 写清楚从 binary → [0,1] continuous 的变化
- **Show all steps:** 计算题展示每一步, 算错也有过程分
- **CF combine vs chain:** Combine(两规则指向同一结论)用加法公式; Chain(链式传递)用乘法

**可能出现但 sample 未考的 topic (🔴 必须准备):**
MYCIN CF 计算 | Entropy/IG 计算 | Naive Bayes 计算 | NEAT speciation 公式 | 消融实验 | Backward chaining 过程 | Embodied AI simplifying assumptions

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
| NEAT start | complex network, prune down | **minimal** network, grow up |
| NEAT uses | backpropagation | **GA** (crossover + mutation) |
| NEAT Add Node weight in | random | **1.0** (preserve behavior) |
| Disjoint vs Excess | same thing | Disjoint=**middle** gaps, Excess=**end** overhang |
| $\overline{W}$ in speciation | total weight | avg weight diff of **matching** genes |
| Multi-agent answer | "they work together" | Name **specific** strategy (collective/positioning/role-based) |
| Flocking | needs central controller | **no** central control, **emergence** from local rules |
| Polly navigation | full world model | **appearance-based**, simplifying assumptions |

---

### CROSS-TOPIC CONNECTIONS (跨主题联系, 考试加分!)

| Connection | Why It Matters |
|---|---|
| BigDog dynamic balancing ↔ NEAT pole balancing | Same class of control problem; NEAT can learn such controllers |
| Fuzzy Logic ↔ Embodied AI | Soft computing enables task-specific shortcuts for robot control |
| NEAT ↔ Reinforcement Learning | NEAT fitness from simulation = RL-style reward (no labeled data) |
| Flocking (emergence) ↔ GA (population) | Both: simple local rules/operators → complex global behavior |
| Expert Systems bottleneck ↔ NEAT | NEAT auto-discovers structure; expert systems need manual rules |
| Naive Bayes ↔ Robot Soccer | Robot may use probabilistic model of game state (limited perception) |
| Brooks layered control ↔ MYCIN backward chaining | Both: structured architecture, but layered=parallel, MYCIN=sequential goal-driven |
