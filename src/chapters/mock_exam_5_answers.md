# Mock Exam 5 — Answers & Explanations

> Attempt the exam first, then check answers. Award marks using the rubric below.

---

## Question 1 [5 marks] — Symbolic Logic

### (a) [3 marks]

**Given:** $(I \wedge G) \rightarrow L$ and $\neg L$

**Step 1 — Apply Modus Tollens:** [1 mark]

The rule has the form $P \rightarrow Q$, and we know $\neg Q$.

By Modus Tollens: $(P \rightarrow Q), \neg Q \vdash \neg P$

Therefore: $\neg(I \wedge G)$

**Step 2 — Apply De Morgan's Law:** [1 mark]

$\neg(I \wedge G) = \neg I \vee \neg G$

**Step 3 — Interpret the conclusion:** [1 mark]

$\neg I \vee \neg G$ means: "Either the intrusion sensor did NOT trigger, OR the guard did NOT confirm the alert (or both)."

We **cannot** conclude that both are false — only that **at least one** of the two conditions was not met. This is because the negation of a conjunction (AND) becomes a disjunction (OR) under De Morgan's law.

> ⚠️ 易错点: 学生常错误得出 ¬I ∧ ¬G (both false)。注意 ¬(A∧B) = ¬A**∨**¬B，是"至少一个为假"，不是"两个都假"。
>
> 对比: 如果原规则是 (I∨G)→L, ¬L, 那么 ¬(I∨G) = ¬I∧¬G, 此时才是"两个都假"。

### (b) [2 marks]

**(i)** [0.5 mark]

$$\forall x \, [\text{PaidFees}(x) \rightarrow \text{CanEnroll}(x)]$$

**(ii)** [1.5 marks]

**Step 1 — Instantiate the universal statement for Charlie:** [0.5 mark]

From the universal rule, we can derive for any specific individual:

$\text{PaidFees}(\text{Charlie}) \rightarrow \text{CanEnroll}(\text{Charlie})$

**Step 2 — Apply Modus Tollens:** [0.5 mark]

We know: $\neg\text{CanEnroll}(\text{Charlie})$

By Modus Tollens: $(\text{PaidFees}(\text{Charlie}) \rightarrow \text{CanEnroll}(\text{Charlie})), \neg\text{CanEnroll}(\text{Charlie}) \vdash \neg\text{PaidFees}(\text{Charlie})$

**Conclusion:** Charlie has **not** paid their fees. [0.5 mark]

> 中文提示: 这是 FOL + Modus Tollens 的经典模式——先实例化 (instantiate)，再用逆否推理。和 2025 真题 Q1b (Cheat/Disqualified) 是完全相同的模式。

---

## Question 2 [4 marks] — Logic Neural Networks (LNN)

### (a) [2 marks]

**Product t-norm AND bounds:** $L_{AND} = L_P \times L_Q$, $U_{AND} = U_P \times U_Q$ [0.5 mark]

Given: ObstacleDetected = [0.6, 0.9], PathBlocked = [0.5, 0.8]

$$L_{\text{MustStop}} = 0.6 \times 0.5 = 0.30$$
$$U_{\text{MustStop}} = 0.9 \times 0.8 = 0.72$$

MustStop = **[0.30, 0.72]** [0.5 mark]

**With threshold α = 0.5:** [0.5 mark]

$L = 0.30 < \alpha = 0.5 < U = 0.72$

Since L < α < U → **Uncertain**

The system cannot definitively say MustStop is true or false. In a safety-critical context, the robot should adopt a **conservative** response (e.g., slow down and gather more sensor data).

**With threshold α = 0.7:** [0.5 mark]

$L = 0.30 < U = 0.72 > \alpha = 0.7$

Since L < α and U > α → still **Uncertain** (but just barely — upper bound exceeds threshold)

However, note that U = 0.72 is only marginally above 0.7. The system is still uncertain, and should still act conservatively.

> 中文提示: Product t-norm 的 AND bounds 就是直接相乘。注意 α=0.5 和 α=0.7 都落在 [L,U] 区间内，所以都是 Uncertain。

### (b) [2 marks]

Two reasons LNN with truth bounds is better for safety-critical applications: [1 mark each]

1. **Explicit uncertainty quantification:** Boolean logic outputs only TRUE or FALSE, with no indication of confidence. LNN's bounds [L, U] explicitly represent *how confident* the system is. When the gap between L and U is large, the system knows its information is unreliable and can act cautiously (e.g., stop the robot) rather than making a potentially dangerous binary decision.

2. **Graceful handling of noisy/incomplete sensor data:** Real sensors produce imperfect readings — a camera might partially detect an obstacle (confidence 0.7, not 1.0). Boolean logic must force this into TRUE or FALSE using an arbitrary threshold, losing information. LNN propagates the sensor uncertainty through the entire reasoning chain as bounds, ensuring the final decision reflects the true quality of the input data.

> 其他可接受答案: interpretability for engineers, supports gradient-based learning for adaptation, bidirectional inference.

---

## Question 3 [2 marks] — Knowledge Graphs & TransE

### (a) [0.5 mark]

TransE principle: **h + r ≈ t**, score = ||h + r - t||₁ (L1 distance, smaller = better)

Mozart + composed = (0.3+0.4, 0.8+0.4, 0.2+0.4) = **(0.7, 1.2, 0.6)**

Symphony_No_40 = (0.7, 1.2, 0.6)

L1 distance = |0.7-0.7| + |1.2-1.2| + |0.6-0.6| = 0 + 0 + 0 = **0.0**

Score = 0.0 → perfect fit, valid fact. ✅

### (b) [1 mark]

Beethoven + composed = (0.5+0.4, 0.9+0.4, 0.3+0.4) = **(0.9, 1.3, 0.7)**

**Distance to Moonlight_Sonata** (0.9, 1.3, 0.7):
|0.9-0.9| + |1.3-1.3| + |0.7-0.7| = **0.0** [0.25 mark]

**Distance to Piano_Concerto_21** (0.8, 1.1, 0.5):
|0.9-0.8| + |1.3-1.1| + |0.7-0.5| = 0.1 + 0.2 + 0.2 = **0.5** [0.25 mark]

TransE predicts **Moonlight_Sonata** (distance 0.0 < 0.5). [0.5 mark]

> 中文提示: TransE 的核心就是 h+r≈t，L1 距离越小越好。计算不难但要细心，逐维度算。

### (c) [0.5 mark]

**Limitation: TransE cannot handle 1-to-N (one-to-many) relations.** For example, if a composer "composed" many pieces, TransE requires h + r ≈ t for each, meaning all tail entities would need to have nearly identical embeddings. This forces distinct entities (like different symphonies) into the same point in embedding space, which is incorrect.

> 其他可接受答案: cannot handle N-to-1 or N-to-N relations; symmetric relations are problematic (h+r=t and t+r=h requires r≈0).

---

## Question 4 [2 marks] — Multi-Agent & Embodied AI

### (a) [1 mark]

In STEAM's framework, the drone team shares a **Joint Persistent Goal (JPG)** — to search the disaster zone for survivors. The team pursues this goal until it is **Achieved**, **Unachievable**, or **Irrelevant**. [0.25 mark]

When one drone discovers the area is completely flooded and inaccessible, it privately concludes the goal is **Unachievable (U)**. [0.25 mark]

The **critical commitment** in STEAM is **communication**: the discovering drone must **not** simply return to base on its own. Instead, it must **broadcast this information to all other team members** so the entire team can form a **mutual belief** that the goal is unachievable. [0.25 mark]

Without this commitment, the other drones would continue searching a dangerous, flooded area indefinitely, wasting resources and potentially being damaged — they would never learn the mission is impossible. [0.25 mark]

### (b) [1 mark]

In Allen's architecture, all three layers run **simultaneously** and their output forces are **summed**. [0.25 mark]

When Level 2 (Explore) wants to head toward a wide opening but Level 0 (Avoid) detects an obstacle in that path, Level 0 generates a **repulsive force** (proportional to 1/d²) pushing the robot away from the obstacle, while Level 2 generates an attractive force toward the opening. These forces are **combined/summed**, and the robot would likely veer around the obstacle while still trending toward the open space. [0.5 mark]

This differs from a traditional planning system because there is **no central planner** that decides "first avoid obstacle, then proceed to opening." Instead, robust behavior **emerges** from the parallel interaction of simple, independent layers — no master plan, no world model. [0.25 mark]

> 中文提示: Allen 的关键在于"并行+力叠加"，不是"上层规划、下层执行"。obstacle avoidance 的力会自然和 explore 的力合成，让机器人绕过障碍。

---

## Question 5 [3 marks] — Decision Trees & Random Forest

### (a) [2 marks]

**Parent node entropy:** [0.5 mark]

Distribution: 12/20 = 0.6 positive, 8/20 = 0.4 negative

$H(\text{parent}) = -0.6 \log_2 0.6 - 0.4 \log_2 0.4 = 0.442 + 0.529 = 0.971$ bits

**Left branch entropy (9+, 1−):** [0.5 mark]

$H(\text{left}) = -0.9 \log_2 0.9 - 0.1 \log_2 0.1 = 0.137 + 0.332 = 0.469$ bits

**Right branch entropy (3+, 7−):** [0.5 mark]

$H(\text{right}) = -0.3 \log_2 0.3 - 0.7 \log_2 0.7 = 0.521 + 0.360 = 0.881$ bits

**Conditional entropy (weighted average):** [0.25 mark]

$H(Y|X) = \frac{10}{20} \times 0.469 + \frac{10}{20} \times 0.881 = 0.5 \times 0.469 + 0.5 \times 0.881 = 0.2345 + 0.4405 = 0.675$ bits

**Information Gain:** [0.25 mark]

$IG = H(\text{parent}) - H(Y|X) = 0.971 - 0.675 = \mathbf{0.296}$ bits

> 中文提示: IG = 分裂前的熵 - 分裂后的加权平均熵。IG > 0 说明这个特征提供了信息量。0.296 是一个不错的 gain。

### (b) [1 mark]

With 100 features, Random Forest considers $\sqrt{100} = \mathbf{10}$ features at each split. [0.25 mark]

Random Forest uses feature bagging (randomly selecting a subset of features at each split) **in addition to** bootstrap sampling because: [0.75 mark]

Bootstrap sampling alone (bagging) creates trees trained on different data subsets, but if one feature is strongly predictive, **all trees would still split on that feature first**, making the trees highly **correlated**. Averaging correlated trees provides limited variance reduction.

Feature bagging **forces each tree to consider different features**, producing **decorrelated** trees. When these diverse trees are averaged, variance is reduced much more effectively. This is why Random Forest = bagging + **feature bagging**, not just bagging alone.

> ⚠️ 必须解释 decorrelation！只说"uses random features" 不给满分。要说明为什么 correlated trees 的 averaging 效果差。

---

## Question 6 [4 marks] — Soft Computing: Vagueness vs Uncertainty

### (a) [2 marks — 0.5 each]

1. **"Moderately high fever" → VAGUENESS.**
The concept "moderately high" has blurry boundaries — at what exact temperature does a fever become "moderately high"? There is no sharp cutoff. The question is "to what degree is this fever moderately high?" → Fuzzy Logic.

2. **"80% chance the flight will be delayed" → UNCERTAINTY.**
The flight will either be delayed or not — this is a definite fact that is currently unknown. The 80% represents a probability of an event occurring, not a degree of membership in a vague category. → Bayesian/Probability.

3. **"Roughly average in quality" → VAGUENESS.**
"Average" and "roughly" both have fuzzy boundaries — the concept of "average quality" is inherently imprecise. An essay could be 0.7 "average" — a degree of membership, not a probability. → Fuzzy Logic.

4. **"Probably has diabetes" → UNCERTAINTY.**
The patient either has diabetes or does not — there is a definite but unknown ground truth. "Probably" expresses our belief about an unknown fact based on evidence. → Bayesian/Probability.

> 中文提示: 判断标准很简单 — 有没有一个确定的事实？"delayed or not" "has diabetes or not" 是确定事实，只是不知道 → Uncertainty。"moderately high" "roughly average" 没有明确边界 → Vagueness。

### (b) [1 mark]

Fuzzy Logic handles "moderately high fever" by defining a **membership function** $\mu_{\text{moderately\_high}}(T)$ that maps temperature to a degree of membership in [0, 1]: [0.5 mark]

For example:
- Below 37.5°C: μ = 0 (not moderately high at all)
- 37.5°C to 38.0°C: μ increases gradually from 0 toward 0.5
- 38.0°C to 39.0°C: μ ranges from 0.5 to 1.0
- Above 39.0°C: μ may decrease (transitioning to "very high")

For **38.5°C**, the membership function might yield $\mu_{\text{moderately\_high}}(38.5) = 0.75$, meaning this temperature belongs to the "moderately high" category to degree 0.75. [0.25 mark]

This value (0.75) is **not** a probability — it represents the *degree to which* 38.5°C fits the vague concept of "moderately high." The patient's temperature is a known fact; the fuzziness is in the concept itself. [0.25 mark]

### (c) [1 mark]

Bayesian reasoning computes the probability of diabetes given lab results using Bayes' theorem: [0.5 mark]

$$P(\text{Diabetes} | \text{LabResults}) = \frac{P(\text{LabResults} | \text{Diabetes}) \times P(\text{Diabetes})}{P(\text{LabResults})}$$

Where: [0.5 mark]
- $P(\text{Diabetes})$ = **prior probability** — how common diabetes is in the population before seeing any test results (e.g., 0.08 for 8% prevalence)
- $P(\text{LabResults} | \text{Diabetes})$ = **likelihood** — probability of observing these specific lab results if the patient does have diabetes (e.g., elevated blood sugar is common in diabetics)
- $P(\text{LabResults})$ = **evidence** — overall probability of seeing these lab results across all patients, computed as: $P(\text{LR}|\text{D})P(\text{D}) + P(\text{LR}|\neg\text{D})P(\neg\text{D})$
- $P(\text{Diabetes} | \text{LabResults})$ = **posterior probability** — our updated belief about diabetes after incorporating the evidence

> 中文提示: Bayes 定理的核心是"用证据更新先验信念"。Prior × Likelihood / Evidence = Posterior。注意分母 P(LabResults) 需要用全概率公式展开。

---

## 评分标准 & 自评指南

| 分数段 | 对应水平 |
|---|---|
| 18-20 | A+ 水平：概念精准，公式正确，解释清晰，有跨主题联系 |
| 15-17 | A/A- 水平：主要概念正确，少数细节遗漏 |
| 12-14 | B+ 水平：理解大方向，但公式或细节有错 |
| < 12 | 需要回到章节复习 |

### 自查重点

- [ ] Q1(a): De Morgan 有没有搞对？¬(A∧B) = ¬A**∨**¬B，不是 ¬A∧¬B！
- [ ] Q1(b): FOL + Modus Tollens 三步骤完整？(写FOL → 实例化 → 逆否推理)
- [ ] Q2(a): Product AND bounds 用乘法了吗？(不是 min/max！)
- [ ] Q2(a): 两个 threshold 的判断都对吗？
- [ ] Q3(b): L1 距离是逐维度取绝对值再求和，有没有算错？
- [ ] Q5(a): Entropy 计算有没有用 hints 提供的近似值？
- [ ] Q5(b): 有没有解释 **decorrelation**？(只说"random features"不给满分)
- [ ] Q6(a): Vagueness vs Uncertainty 判断依据写清楚了吗？
- [ ] Q6(b): 有没有强调 μ 不是概率？
- [ ] Q6(c): Bayes 四个术语 (prior/likelihood/evidence/posterior) 都解释了吗？
