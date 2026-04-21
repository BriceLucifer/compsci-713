# Mock Exam 4 — Answers & Explanations

> Attempt the exam first, then check answers. Award marks using the rubric below.

---

## Question 1 [4 marks] — Genetic Algorithms & NEAT

### (a) [1 mark]

In NEAT, the initial population consists of **minimal networks** where all 4 sensor inputs are directly connected to the 2 outputs, with **no hidden nodes**. Weights are assigned randomly. [0.5 mark]

NEAT starts this way because it searches through the **smallest possible space first**. Complexity is added only when needed through structural mutations, avoiding the problem of searching an unnecessarily large topology space from the beginning. [0.5 mark]

> 中文提示：NEAT 从最简结构开始，复杂度按需增长。这是和其他神经进化方法的关键区别。

### (b) [2 marks]

NEAT uses **speciation** to protect this individual. It groups similar individuals into species based on a compatibility distance measure: [0.5 mark]

$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$

Where $E$ = excess genes, $D$ = disjoint genes, $\overline{W}$ = average weight difference of matching genes, $N$ = larger genome size, and $c_1, c_2, c_3$ are configurable coefficients. [0.5 mark]

If $\delta < \delta_t$ (threshold), two individuals are in the same species. The new structural innovation would likely have high $\delta$ from existing networks, so it forms its own species (or joins a small one). [0.5 mark]

Within each species, **adjusted fitness** is calculated as $f'_i = f_i / |S|$ (individual fitness divided by species size). This prevents large established species from monopolizing breeding slots and gives the new structure time to optimize its weights before competing globally. [0.5 mark]

### (c) [1 mark]

**Matching genes** (both parents have): Inn# 1, 2, 3, 5 → randomly inherited from either parent [0.25 mark]

**Disjoint genes** (within range of both, but only in one):
- Parent 1: Inn# 6 (within Parent 2's range 1-7)
- Parent 2: Inn# 4, 7 (within Parent 1's range 1-8... but 4 is within 1-8, 7 is within 1-8) [0.25 mark]

Wait — let me re-analyze:
- Range of Parent 1: 1-8. Range of Parent 2: 1-7.
- Genes only in Parent 1: Inn# 6, 8. Inn# 6 is within Parent 2's max (7) → **disjoint**. Inn# 8 is beyond Parent 2's max (7) → **excess**.
- Genes only in Parent 2: Inn# 4, 7. Inn# 4 is within Parent 1's max (8) → **disjoint**. Inn# 7 is within Parent 1's max (8) → **disjoint**.

| Type | Parent 1 | Parent 2 |
|---|---|---|
| Matching | 1, 2, 3, 5 | 1, 2, 3, 5 |
| Disjoint | 6 | 4, 7 |
| Excess | 8 | — |

Since **Parent 1 is fitter** (85 > 72), all disjoint and excess genes come from **Parent 1**. [0.5 mark]

> ⚠️ 易错点：Disjoint 是在对方 Innovation Number 范围**之内**的不匹配基因，Excess 是**超出**对方范围的。

---

## Question 2 [3 marks] — NEAT Speciation Calculation

### (a) [1 mark]

Line up by Innovation Number:

| Inn# | A | B | Status |
|---|---|---|---|
| 1 | 0.5 | 0.7 | **Matching** |
| 2 | -0.3 | -0.1 | **Matching** |
| 3 | 0.8 | — | **Disjoint** (within B's range 1-8) |
| 4 | — | 0.6 | **Disjoint** (within A's range 1-6) |
| 5 | 0.2 | 0.5 | **Matching** |
| 6 | 0.4 | — | **Disjoint** (within B's range 1-8) |
| 7 | — | -0.2 | **Excess** (beyond A's max = 6) |
| 8 | — | 0.3 | **Excess** (beyond A's max = 6) |

- **Matching:** Inn# 1, 2, 5 → 3 matching genes
- **Disjoint:** Inn# 3 (A), 4 (B), 6 (A) → D = 3
- **Excess:** Inn# 7, 8 (B) → E = 2

### (b) [1 mark]

$N = \max(5, 6) = 6$

Matching gene weight differences:
- Inn# 1: $|0.5 - 0.7| = 0.2$
- Inn# 2: $|-0.3 - (-0.1)| = 0.2$
- Inn# 5: $|0.2 - 0.5| = 0.3$

$\overline{W} = (0.2 + 0.2 + 0.3) / 3 = 0.233$

$$\delta = \frac{1.0 \times 2}{6} + \frac{1.0 \times 3}{6} + 0.4 \times 0.233 = 0.333 + 0.500 + 0.093 = 0.927$$

$\delta = 0.927 < \delta_t = 3.0$ → **Yes, A and B are in the same species.** [1 mark]

> 中文提示：δ 远小于阈值，说明这两个个体的拓扑结构和权重差异不大，属于同一物种。

### (c) [1 mark]

**Species X** (4 individuals): fitness 12, 8, 6, 10
- Adjusted: $12/4=3$, $8/4=2$, $6/4=1.5$, $10/4=2.5$
- Sum of adjusted fitness = $3 + 2 + 1.5 + 2.5 = 9.0$

**Species Y** (2 individuals): fitness 14, 10
- Adjusted: $14/2=7$, $10/2=5$
- Sum of adjusted fitness = $7 + 5 = 12.0$

**Breeding quota ratio:** X : Y = 9.0 : 12.0 = **3 : 4**

> 注意：虽然 Species X 有更多个体，但 Species Y 每个个体更强，且不被大物种大小稀释，所以反而获得更多繁殖名额。这就是 adjusted fitness 的作用——防止大物种垄断。

---

## Question 3 [4 marks] — Embodied AI

### (a) [2 marks]

Polly exploited three simplifying assumptions about its indoor environment: [1.5 marks, 0.5 each]

1. **Carpet detection:** The floor was uniform un-patterned carpet. Anything with visual patterns was classified as an obstacle. This eliminated the need for complex object recognition.

2. **Ground-plane constraint:** Objects rest on a flat floor, so objects appearing higher in the image are farther away. This provided depth information from a single camera without needing stereo vision or a depth sensor.

3. **Corridor geometry:** Narrow corridors constrained where in the visual field distant landmarks could appear, reducing the search space for navigation landmarks.

**Design principle:** "Do not solve the hardest possible vision problem if the environment lets you solve an easier one." — exploit environmental structure for computational shortcuts. [0.5 mark]

> 中文提示：Polly 的关键在于**利用环境的特殊性**来简化计算。不是通用的 CV，而是针对特定场景的巧妙 shortcut。

### (b) [2 marks]

Allen's three layers: [1 mark, ~0.33 each]

| Layer | Behavior | Mechanism |
|---|---|---|
| **Level 0 — Avoid** | Obstacle avoidance | Generates a repulsive force inversely proportional to distance ($\propto 1/d^2$) |
| **Level 1 — Wander** | Random exploration | Chooses a random direction and follows it for about 10 seconds |
| **Level 2 — Explore** | Directed movement | Steers toward wide-open space |

**Combination:** All three layers run **simultaneously** (in parallel), and their forces are **summed/combined** to determine the robot's final direction. [0.5 mark]

**Difference from hierarchical control:** In a traditional hierarchical system, a top-level planner issues commands that are executed by lower levels (top-down command). In Brooks' layered control, there is **no master plan** — each layer runs independently and contributes its own "vote." The robot exhibits robust behavior through the **emergent interaction** of simple concurrent layers, not through centralized planning. [0.5 mark]

> 中文提示：关键区别 — Brooks 的层是**并行运行、力叠加**的，不是传统的"上级命令下级执行"。

---

## Question 4 [3 marks] — Multi-Agent Systems & Flocking

### (a) [1.5 marks]

Reynolds' three flocking rules (1987): [1 mark, ~0.33 each]

1. **R1 — Collision Avoidance:** Do not come within a minimum distance of nearby flockmates.
2. **R2 — Flock Centering:** Stay close to flockmates rather than drifting away from the group.
3. **R3 — Velocity Matching:** Align your motion (both speed and direction) with nearby agents.

This demonstrates **emergence** — complex, realistic global patterns (flocking behavior) arise from simple **local** rules followed by individual agents, without any central controller. This is a form of **agent-based modelling**. [0.5 mark]

> 中文提示：Reynolds 的三条规则是考试高频点。velocity 是**矢量**（包含 speed + direction），不要只说 speed。

### (b) [1.5 marks]

A **Joint Persistent Goal (JPG)** is a shared goal that all team members commit to pursuing. They continue working toward it until they determine it is **Achieved (A)**, **Unachievable (U)**, or **Irrelevant (I)**. [0.5 mark]

Communication is fundamental because when one agent privately concludes A/U/I, it must not simply act on this knowledge alone. Instead, it must **inform the entire team** so they can form a **new mutual belief** about the goal's status. STEAM is a commitment to **communicate**, not just to act. [0.5 mark]

**Example:** In a squadron of attack helicopters, if one helicopter detects a surface-to-air missile battery (making the mission unachievable), it must tell the rest of the team. Without this communication commitment, the detecting helicopter might simply fly home while the others continue the now-impossible mission, unaware of the danger. [0.5 mark]

---

## Question 5 [3 marks] — Cross-Topic Integration

### (a) [1.5 marks]

The **double pole balancing** task requires a cart moving on a limited track to balance two poles of **different lengths** simultaneously. [0.25 mark]

The **fitness function** measures the **number of time steps survived** — how long the cart can keep both poles upright while staying on the track. An additional fitness criterion penalizes oscillation (minimizing sum of velocity, angular velocity, and angle). [0.5 mark]

In the **harder version**, angular velocities and cart velocity are **not given as inputs**. The network must infer angular velocity by detecting **change in angle over time** ($\Delta\theta / \Delta t$). This requires a **recurrent connection** — a feedback loop where the network's previous output becomes part of its current input, giving it **memory** of past states. Without recurrence, the network has no way to compute time derivatives. [0.75 mark]

> 中文提示：BigDog 的动态平衡和这个问题本质相同——都是实时控制问题。NEAT 已证明可以学习此类控制器。

### (b) [1.5 marks]

| Aspect | NEAT Approach | Expert System Approach |
|---|---|---|
| **Knowledge acquisition** | Automatically discovered through evolution (fitness-driven) | Manually elicited from human experts (knowledge engineering) |
| **Controller representation** | Neural network (evolved topology + weights) | IF-THEN rules in a knowledge base |
| **Main advantage** | No need to articulate rules; can discover non-obvious strategies | Explainable; human-readable reasoning chain |

[1 mark for correct table]

For a task like pole balancing where the rules are **difficult to articulate**, NEAT is clearly better suited. A human expert would struggle to write IF-THEN rules for "when the pole is at 3.2 degrees with angular velocity -0.5 rad/s, apply force 2.1N to the left." NEAT **evolves** this knowledge automatically through simulation, bypassing the **knowledge acquisition bottleneck** that plagues expert systems. Furthermore, NEAT generates small, interpretable networks, partially retaining the explainability advantage. [0.5 mark]

---

## Question 6 [3 marks] — Mixed Short Answer

### (a) [1 mark]

Brooks argued that traditional AI focused too heavily on high-level symbolic reasoning (chess, theorem proving), but this was the **wrong starting point**. He noted that evolution spent **billions of years** on simple organisms before complex intelligence appeared, and human-level intelligence has only existed for ~1 million years. [0.5 mark]

Therefore, AI should study **simple intelligent behavior** — locomotion, obstacle avoidance, and social coordination — and build **upward from situated competence** rather than downward from symbolic performance. This is the foundation of embodied AI: intelligence arises from **interaction with the physical world**, not from abstract reasoning alone. [0.5 mark]

### (b) [1 mark]

Two coordination strategies in robot soccer:

1. **Collective behaviours (e.g., passing strategy):** Robots evaluate candidate passing points based on **interception prediction** (can an opponent reach the ball?) and assign **tactical value** based on field position (closer to goal = higher value). [0.25 mark]

2. **Role-based strategies:** Each robot dynamically assigns itself a **role** (goalkeeper, attacker, defender) based on the current game state — for example, when the ball is near the opponent's goal, more robots switch to attacker roles. [0.25 mark]

These strategies work best when teammates **perceive the situation similarly** because: if one robot thinks the ball is in the attacking zone (and adopts an attacker role) while another robot thinks the ball is in the defending zone (and adopts a defender role), their strategies will conflict. Shared perception (e.g., an overhead camera) enables consistent decision-making. [0.5 mark]

> ⚠️ 答题切忌笼统！"They cooperate" or "They work together" = 0 marks. 必须写出具体的策略名称和机制。

### (c) [1 mark]

An **ablation study** removes individual components of a system one at a time and measures the impact on performance, to verify that each component contributes meaningfully. [0.25 mark]

Two of NEAT's ablation experiments:

1. **Disabling speciation:** Without speciation, new structural innovations were eliminated too early before their weights could be optimized. Result: slower learning or failure to master the task. This demonstrates that speciation is essential for **protecting innovation**. [0.375 mark]

2. **Starting from a larger-than-minimal network:** Instead of NEAT's minimal initialization, networks started with more nodes and connections. Result: slower convergence. This demonstrates the importance of NEAT's **minimal initialization** principle — searching small spaces first and adding complexity only when needed. [0.375 mark]

> 中文提示：四个消融实验——固定全连接、大网络开始、去掉物种形成、去掉交叉——**任选两个**作答即可。关键是说出"去掉了什么→结果→说明了什么"。

---

## 评分标准 & 自评指南

| 分数段 | 对应水平 |
|---|---|
| 18-20 | A+ 水平：概念精准，公式正确，解释清晰，有跨主题联系 |
| 15-17 | A/A- 水平：主要概念正确，少数细节遗漏 |
| 12-14 | B+ 水平：理解大方向，但公式或细节有错 |
| < 12 | 需要回到章节复习 |

### 自查重点

- [ ] Q1(c): 能正确区分 disjoint 和 excess 吗？（最易错）
- [ ] Q2(b): speciation 公式计算步骤完整吗？
- [ ] Q2(c): adjusted fitness 的除法有没有搞对？
- [ ] Q3(a): 三个 simplifying assumptions 能不能完整说出来？
- [ ] Q4(a): velocity matching 有没有说是"速度+方向"的矢量？
- [ ] Q5(a): 为什么需要 recurrent connection？逻辑链完整吗？
- [ ] Q6(c): 消融实验有没有说出"去掉什么→结果→证明了什么"？
