# Soft Computing — Fuzzy Logic, Bayesian Reasoning & Naive Bayes (W5L1)

## 🎯 考试重要度

🔴 **必考** | **~20% of exam** | Appears in S1 2024, S1 2025, S1 2026 Sample

| Year | Question | Marks | Topic |
|---|---|---|---|
| S1 2026 Sample | Q6 | 4m | Classify 4 scenarios as vagueness vs uncertainty |
| S1 2025 Actual | Q5 | 3m | Contrast traditional logic vs fuzzy logic (hammer thrower) |
| S1 2024 Final | Q5 | ~3m | Naive Bayes assumptions (conditional independence + feature relevance) |

This chapter covers **three exam-critical skills**: (1) classifying vagueness vs uncertainty, (2) fuzzy logic computation, and (3) Bayesian / Naive Bayes calculation. All three have appeared in recent exams and are extremely likely to appear again.

---

## 📖 核心概念（Core Concepts）

| English Term | 中文 | One-line Definition |
|---|---|---|
| Hard Computing（硬计算） | 硬计算 | Computation using crisp symbols, exact values, binary true/false — compilers, arithmetic, classical logic |
| Soft Computing（软计算） | 软计算 | Computation tolerating imprecision, partial truth, and degrees — fuzzy logic, Bayes, neural nets |
| Vagueness（模糊性） | 模糊性（语义模糊） | The **concept itself** has blurry boundaries — "tall", "warm", "high risk" have no sharp cutoff |
| Uncertainty（不确定性） | 不确定性 | The **state of the world** is unknown — a definite fact exists but we lack evidence to know it |
| Fuzzy Set（模糊集合） | 模糊集合 | A set where membership is a degree in [0, 1], not binary {0, 1} |
| Membership Function $\mu_A(x)$（隶属度函数） | 隶属度函数 | Maps an element $x$ to its degree of belonging to fuzzy set $A$, valued in $[0, 1]$ |
| Fuzzy Connectives（模糊逻辑联结词） | 模糊算子 | AND = min, OR = max, NOT = 1 - $\mu$ |
| Fuzzy Implication（模糊蕴含） | 模糊蕴含 | Standard: $A \rightarrow B = \max(1-A, B)$; Godel: $1$ if $A \leq B$, else $B$ |
| Fuzzy Control（模糊控制） | 模糊控制 | Control system using fuzzy rules with error $e(t)$ and rate of change $\Delta e(t)$ as inputs |
| Defuzzification（去模糊化） | 去模糊化 | Converting a fuzzy output set back to a single crisp value (e.g., centre of gravity method) |
| Bayes' Theorem（贝叶斯定理） | 贝叶斯定理 | $P(H \mid e) = P(e \mid H) \cdot P(H) / P(e)$ — updating belief with evidence |
| Prior $P(H)$（先验概率） | 先验概率 | Probability of hypothesis before observing evidence |
| Likelihood $P(e \mid H)$（似然） | 似然 | Probability of observing evidence given the hypothesis is true |
| Posterior $P(H \mid e)$（后验概率） | 后验概率 | Updated probability of hypothesis after observing evidence |
| Base Rate Fallacy（基率谬误） | 基率谬误 | Ignoring the prior probability (base rate) when interpreting evidence |
| Naive Bayes Classifier（朴素贝叶斯分类器） | 朴素贝叶斯 | Classifier assuming conditional independence: $P(C \mid \mathbf{x}) \propto P(C) \prod P(x_i \mid C)$ |
| Conditional Independence（条件独立） | 条件独立 | Features are independent of each other *given* the class label |
| Log-score（对数得分） | 对数得分 | $\arg\max [\log P(C) + \sum \log P(x_i \mid C)]$ — avoids numerical underflow |

---

## 🧠 费曼草稿（Feynman Draft）

### Part 1: Why "Soft" Computing?

Imagine you are teaching a robot to drive. With **hard computing**, you would write rules like: "IF speed > 60 km/h THEN brake." But what if speed is 59.9 km/h? The rule says "don't brake," even though that is essentially the same as 60. Hard computing treats the world as black-and-white, but the real world is full of shades of grey.

**Soft computing** is the toolkit for handling this greyness. It has three main branches:
1. **Fuzzy Logic** — for concepts with blurry boundaries ("warm", "fast", "tall")
2. **Bayesian Reasoning** — for situations where we don't know the truth ("Is it spam?")
3. **Neural Networks** — for learning patterns from data (covered in other chapters)

"Soft" does NOT mean weak or inferior. It means **flexible enough to work when the world is messy** — noisy data, vague concepts, incomplete information. A spam filter that says "92% likely spam" is far more useful than one that crashes because it can't say "definitely spam" or "definitely not spam."

| Feature | Hard Computing | Soft Computing |
|---------|---------------|----------------|
| Representation | crisp symbols, exact values | approximate values, degrees, probabilities |
| Logic | true / false | partial truth or belief |
| Typical setting | well-defined rules, precise inputs | noisy, incomplete, vague, uncertain |
| Strength | exact answers when model is right | robust when world is messy |
| Examples | arithmetic, compilers, shortest path | fuzzy control, Bayes classifiers, neural nets |

### Part 2: The Two Faces of "Not Knowing" — Vagueness vs Uncertainty

This is the **single most important distinction** in this chapter. The exam tests it directly (Q6, 4 marks). Here is the clearest way to understand it:

**Uncertainty** is like a locked box. There is a definite object inside — a red ball or a blue ball. You just don't know which one. You can assign a *probability*: "70% chance it's red." The fact itself is crisp; your *knowledge* is incomplete.

**Vagueness** is like asking "Is this colour red?" while looking at an orange-red sunset. There is no hidden truth to discover. The concept "red" itself has blurry boundaries. You assign a *degree*: "This is red to degree 0.6." There is no randomness — you can see the colour perfectly. The blurriness is in the *word*, not in the world.

**Decision procedure for the exam:**

```
Step 1: Is there a DEFINITE FACT about the world that we simply don't know?
   → YES → UNCERTAINTY (Bayesian reasoning)
   → NO  → Go to Step 2

Step 2: Does the concept have BLURRY BOUNDARIES / admit degrees?
   → YES → VAGUENESS (Fuzzy logic)
   → NO  → Standard hard computing
```

**Worked examples (exam-style):**

| Scenario | Hidden fact? | Blurry concept? | Answer |
|---|---|---|---|
| "This patient is high risk" | No — "high risk" is not a fact to discover | Yes — no sharp cutoff for "high risk" | **VAGUENESS** |
| Alarm went off — burglary? | Yes — burglar either came or didn't | N/A | **UNCERTAINTY** |
| "Student 74 is almost excellent" | No — the grade 74 is known | Yes — "almost excellent" is graded | **VAGUENESS** |
| Spam filter classifying an email | Yes — email is either spam or not | N/A | **UNCERTAINTY** |

⚠️ **Common Misconception**: Many students confuse fuzzy membership with probability. When we say $\mu_{\text{Tall}}(183\text{cm}) = 0.6$, we are **not** saying "60% chance this person is tall." The person IS 183cm — there's no randomness. The 0.6 is a **degree of truth** about how well the concept "tall" applies. Fuzzy logic handles **vagueness** (blurry concepts); probability handles **uncertainty** (unknown facts).

### Part 3: Building Intuition for Fuzzy Logic

Think of a dimmer switch for lights. A classical light switch is either ON or OFF — that is a classical (crisp) set. A dimmer switch lets you set any brightness from 0% to 100% — that is a fuzzy set.

When we say $\mu_{\text{Tall}}(183\text{cm}) = 0.6$, we mean: "183cm belongs to the set 'Tall' with degree 0.6." No randomness, no probability. Just a graded concept.

**Toy example with numbers:**

Let $\mu_{\text{hot}} = 0.8$ and $\mu_{\text{humid}} = 0.7$. Then:

- Fuzzy AND: $\min(0.8, 0.7) = 0.7$ (the weakest link determines the conjunction)
- Fuzzy OR: $\max(0.8, 0.7) = 0.8$ (the strongest component determines the disjunction)
- Fuzzy NOT hot: $1 - 0.8 = 0.2$

**Why min for AND?** You are only as "both tall and heavy" as the lesser degree. If someone is tall (degree 0.9) but light (degree 0.2), they are "tall AND heavy" only to degree 0.2.

**Why max for OR?** "Tall OR heavy" is satisfied by the stronger of the two. If someone is tall (0.9) but not heavy (0.2), they are "tall OR heavy" to degree 0.9.

### Part 4: Building Intuition for Bayesian Reasoning

Imagine a doctor diagnosing a rare disease. Before any test, the doctor knows: "This disease occurs in 1 out of 10,000 people" — that is the **prior** ($P(H) = 0.0001$). A test comes back positive, and the test catches 95% of true cases (sensitivity = 0.95). Many students instantly say "95% chance the patient has it!" But that is **dead wrong**.

Here is why: Out of 10,000 people, about 1 truly has the disease and tests positive. But about 100 healthy people also test positive (1% false positive rate of 9,999 people). So roughly 1 out of 101 positive tests is a true positive — about 1%, not 95%.

This is exactly what Bayes' theorem captures: **posterior $\propto$ prior $\times$ likelihood**. A strong test on a rare event still produces mostly false positives. This is the **base rate fallacy**.

### Part 5: Naive Bayes — Why "Naive" Works

Imagine you are sorting mail into "spam" and "not spam." You look at each word independently: "FREE" suggests spam, "meeting" suggests not-spam. The "naive" part is assuming that seeing "FREE" tells you nothing about whether you will also see "WINNER" — each word is treated as an independent piece of evidence.

This assumption is obviously wrong (spam emails often contain both "FREE" and "WINNER" together). But Naive Bayes works anyway because:
1. We only need the **ranking** of classes to be correct, not exact probabilities
2. Many weak signals **combine effectively** even with independence errors
3. Estimation is **easy** even with limited training data — no need to estimate complex joint distributions

💡 **Core Intuition**: Fuzzy asks "to what degree?" about blurry concepts; Bayes asks "how likely?" about unknown facts. Both tolerate imprecision — that is what makes them "soft."

---

## 📐 正式定义（Formal Definition）

### 1. Hard Computing vs Soft Computing

| Feature | Hard Computing（硬计算） | Soft Computing（软计算） |
|---|---|---|
| Values | Crisp symbols, exact numbers | Approximate, degrees, partial truth |
| Truth model | Binary: True or False | Continuous: degrees in [0, 1], probabilities |
| Reasoning | Deductive, deterministic | Inductive, probabilistic, heuristic |
| Tolerance | No tolerance for imprecision | Tolerates and exploits imprecision |
| Examples | Classical logic, arithmetic, compilers, SQL | Fuzzy logic, Bayesian networks, neural networks |
| Strengths | Precision, provable correctness | Handling real-world ambiguity, noise, complexity |
| Limitations | Brittle with noisy/vague inputs | May sacrifice exactness for tractability |

### 2. Vagueness vs Uncertainty — Formal Distinction

| Dimension | Vagueness（模糊性） | Uncertainty（不确定性） |
|---|---|---|
| What is blurry? | The **concept** itself | Our **knowledge** of the world |
| The world | Fully observable — no hidden state | Has hidden state we cannot observe |
| The right question | "To what **degree** is this true?" | "How **likely** is this true?" |
| Output | Membership degree $\mu \in [0,1]$ | Probability $P \in [0,1]$ |
| Tool | Fuzzy Logic | Bayesian Reasoning |
| Sum constraint | Degrees do NOT need to sum to 1 | Probabilities MUST sum to 1 |

**Critical point**: $\mu_{\text{Tall}}(x) + \mu_{\text{Short}}(x)$ does NOT need to equal 1. A person can be "tall to degree 0.6" and "short to degree 0.2" simultaneously. But $P(\text{spam}) + P(\neg\text{spam})$ MUST equal 1.

### 3. Fuzzy Set Theory

**Classical (crisp) set:**

$$\mu_A(x) \in \{0, 1\}$$

An element either belongs ($1$) or does not ($0$). Sharp boundary.

**Fuzzy set:**

$$\mu_A: X \rightarrow [0, 1]$$

An element belongs with a **degree** between 0 and 1. No sharp boundary.

**Example — fuzzy set "Tall":**

| Height (cm) | $\mu_{\text{Tall}}$ | Interpretation |
|---|---|---|
| 160 | 0.0 | Not tall at all |
| 170 | 0.2 | Barely tall |
| 175 | 0.4 | Somewhat tall |
| 180 | 0.6 | Moderately tall |
| 183 | 0.7 | Fairly tall |
| 190 | 0.9 | Very tall |
| 200 | 1.0 | Fully tall |

### 4. Fuzzy Logic Connectives

Given fuzzy truth values $A, B \in [0, 1]$:

**Fuzzy AND (conjunction / 模糊合取):**

$$A \wedge B = \min(A, B)$$

**Fuzzy OR (disjunction / 模糊析取):**

$$A \vee B = \max(A, B)$$

**Fuzzy NOT (negation / 模糊否定):**

$$\neg A = 1 - A$$

**Properties preserved from classical logic:**

| Property | Classical | Fuzzy |
|---|---|---|
| Commutativity | $A \wedge B = B \wedge A$ | $\min(A,B) = \min(B,A)$ ✓ |
| Associativity | $(A \wedge B) \wedge C = A \wedge (B \wedge C)$ | ✓ |
| De Morgan's | $\neg(A \wedge B) = \neg A \vee \neg B$ | $1 - \min(A,B) = \max(1-A, 1-B)$ ✓ |
| Law of Excluded Middle | $A \vee \neg A = 1$ | $\max(A, 1-A) \neq 1$ in general ✗ |
| Law of Contradiction | $A \wedge \neg A = 0$ | $\min(A, 1-A) \neq 0$ in general ✗ |

⚠️ **Important**: Fuzzy logic violates the Law of Excluded Middle and Law of Contradiction. If $A = 0.5$, then $A \vee \neg A = \max(0.5, 0.5) = 0.5 \neq 1$ and $A \wedge \neg A = \min(0.5, 0.5) = 0.5 \neq 0$.

### 5. Fuzzy Implication

Two common definitions of $A \rightarrow B$:

**Standard (Kleene-Dienes) implication:**

$$A \rightarrow B = \max(1 - A, B)$$

This is the fuzzy analogue of the classical equivalence $A \rightarrow B \equiv \neg A \vee B$.

**Godel implication:**

$$A \rightarrow B = \begin{cases} 1 & \text{if } A \leq B \\ B & \text{if } A > B \end{cases}$$

**Complete comparison table:**

| $A$ | $B$ | Standard: $\max(1-A, B)$ | Godel | More intuitive? |
|---|---|---|---|---|
| 0.5 | 0 | $\max(0.5, 0) = 0.5$ | $0$ (since $0.5 > 0$) | Godel — antecedent holds but consequent fails, so implication should fail |
| 0.8 | 0.3 | $\max(0.2, 0.3) = 0.3$ | $0.3$ (since $0.8 > 0.3$) | Same result |
| 0.6 | 0.9 | $\max(0.4, 0.9) = 0.9$ | $1$ (since $0.6 \leq 0.9$) | Godel — antecedent partially holds, consequent holds more, implication fully satisfied |
| 0.7 | 0.3 | $\max(0.3, 0.3) = 0.3$ | $0.3$ (since $0.7 > 0.3$) | Same result |
| 1.0 | 0.0 | $\max(0, 0) = 0$ | $0$ (since $1 > 0$) | Same — both give 0 for fully true antecedent, fully false consequent |
| 0.0 | 0.0 | $\max(1, 0) = 1$ | $1$ (since $0 \leq 0$) | Same — false antecedent makes implication vacuously true |

**Key insight**: The Godel version is generally more intuitive because when $A$ partially holds but $B$ does not hold at all, Godel correctly gives 0 (implication fails completely), while Standard gives a positive value.

### 6. Fuzzy Rules and Fuzzy Control

**Fuzzy Rule format:**

$$\text{IF } x \text{ is } A \text{ AND } y \text{ is } B \text{ THEN } z \text{ is } C$$

**Fuzzy Control System Architecture:**

```
                    ┌──────────────┐
  Crisp Input  ──→  │ Fuzzification │  ──→  Fuzzy Input
                    └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
  Rule Base   ──→  │  Inference    │  ──→  Fuzzy Output
                    │  Engine       │
                    └──────────────┘
                           │
                           ▼
                    ┌────────────────┐
                    │ Defuzzification │  ──→  Crisp Output
                    └────────────────┘
```

**Fuzzy Control uses two key inputs:**
- **Error** $e(t)$: difference between desired state and actual state
- **Rate of change** $\Delta e(t)$: how fast the error is changing

Example for temperature control:
- $e(t) = T_{\text{desired}} - T_{\text{actual}}$ (e.g., 22 - 25 = -3, meaning too hot)
- $\Delta e(t)$: is the temperature rising or falling?
- Rules like: IF $e(t)$ is negative-big AND $\Delta e(t)$ is positive THEN cooling is medium (it is too hot but getting better, so moderate cooling)

**Applications (from lecture):**
- Autopilot systems
- Anti-lock braking systems (ABS)
- Washing machines (adjust cycle based on "somewhat dirty")
- Consumer devices
- Decision support systems

### 7. Bayes' Theorem

$$P(H \mid e) = \frac{P(e \mid H) \cdot P(H)}{P(e)}$$

Where:
- $P(H)$ = **prior**（先验概率）: belief in hypothesis before evidence
- $P(e \mid H)$ = **likelihood**（似然）: probability of evidence given hypothesis is true
- $P(e)$ = **evidence/marginal**（边际概率）: total probability of evidence under all hypotheses
- $P(H \mid e)$ = **posterior**（后验概率）: updated belief after evidence

**Expanding the denominator** via the law of total probability:

$$P(e) = P(e \mid H) \cdot P(H) + P(e \mid \neg H) \cdot P(\neg H)$$

**Core relationship:**

$$\boxed{\text{posterior} \propto \text{prior} \times \text{likelihood}}$$

### 8. Naive Bayes Classifier

For classification with class $C$ and feature vector $\mathbf{x} = (x_1, x_2, \ldots, x_n)$:

**Full Bayes:**

$$P(C = c \mid \mathbf{x}) = \frac{P(C = c) \cdot P(\mathbf{x} \mid C = c)}{P(\mathbf{x})}$$

**Naive assumption**（朴素假设）— features are **conditionally independent** given the class:

$$P(x_1, x_2, \ldots, x_n \mid C) = \prod_{i=1}^{n} P(x_i \mid C)$$

This simplifies the classifier to:

$$P(C = c \mid \mathbf{x}) \propto P(C = c) \cdot \prod_{i=1}^{n} P(x_i \mid C = c)$$

**Classification rule:**

$$\hat{C} = \underset{c}{\arg\max} \; P(C = c) \cdot \prod_{i=1}^{n} P(x_i \mid C = c)$$

**Log-score version** (prevents numerical underflow from multiplying many small probabilities):

$$\hat{C} = \underset{c}{\arg\max} \left[ \log P(C = c) + \sum_{i=1}^{n} \log P(x_i \mid C = c) \right]$$

**Why log-score?** When you multiply many probabilities like $0.01 \times 0.005 \times 0.001 \times \ldots$, the product quickly becomes too small for floating-point representation. In log-space, multiplication becomes addition, which is numerically stable. Each feature contributes **additively** in log-space.

**Why Naive Bayes works despite the unrealistic independence assumption:**

1. **Only ranking matters** — for classification, we only need $P(C_1 \mid \mathbf{x}) > P(C_2 \mid \mathbf{x})$, not exact values. Even if individual probabilities are wrong, the relative ordering is often preserved.
2. **Many weak signals combine effectively** — errors from different features tend to cancel out.
3. **Easy parameter estimation** — only need to estimate $P(x_i \mid C)$ for each feature individually, not the full joint $P(x_1, x_2, \ldots \mid C)$. Works with limited training data.
4. **Avoids overfitting** in high-dimensional spaces — more complex models that model feature dependencies may overfit when data is scarce.

---

## 🔄 机制与推导（How It Works）

### Procedure 1: Classifying Vagueness vs Uncertainty (Exam Algorithm)

```
INPUT: A scenario description.
OUTPUT: "Vagueness" or "Uncertainty" with justification.

Step 1: Ask — "Is there a DEFINITE FACT about the world that we simply don't know?"
   → YES → This is UNCERTAINTY → Bayesian reasoning
   → NO  → Go to Step 2

Step 2: Ask — "Does the concept used have BLURRY BOUNDARIES / admit degrees?"
   → YES → This is VAGUENESS → Fuzzy logic
   → NO  → This is standard logic (hard computing)
```

**Worked examples from all exam years:**

| # | Scenario | Step 1: Hidden fact? | Step 2: Blurry concept? | Answer | Tool |
|---|---|---|---|---|---|
| 1 | "This patient is high risk" | No — "high risk" is not a fact to discover | Yes — no sharp cutoff | **Vagueness** | Fuzzy Logic |
| 2 | Alarm went off — is it burglary? | Yes — burglar either came or didn't | N/A | **Uncertainty** | Bayesian Reasoning |
| 3 | "Student 74 is almost excellent" | No — grade 74 is known precisely | Yes — "almost excellent" is graded | **Vagueness** | Fuzzy Logic |
| 4 | Spam filter with incomplete evidence | Yes — email is either spam or not | N/A | **Uncertainty** | Naive Bayes |

**Pattern**: If the scenario contains a **linguistic/graded adjective** ("high risk", "almost excellent", "warm", "fast"), it is almost always **vagueness**. If it contains a **binary outcome** that we need to infer ("Is it X?", "Did Y happen?"), it is almost always **uncertainty**.

### Procedure 2: Fuzzy Rule Evaluation — Step by Step

**Scenario**: A fuzzy controller for air conditioning.

- $\mu_{\text{hot}}(\text{temp}) = 0.8$ (temperature is "hot" to degree 0.8)
- $\mu_{\text{humid}}(\text{humidity}) = 0.7$ (humidity is "humid" to degree 0.7)

**Rule**: IF temperature is hot AND humidity is humid THEN fan speed is high.

**Step 1 — Fuzzification** (already done — inputs mapped to membership degrees):
- $\mu_{\text{hot}} = 0.8$, $\mu_{\text{humid}} = 0.7$

**Step 2 — Evaluate antecedent (fuzzy AND):**

$$\text{Rule strength} = \min(\mu_{\text{hot}}, \mu_{\text{humid}}) = \min(0.8, 0.7) = 0.7$$

**Step 3 — Apply to consequent:**

The rule fires with strength 0.7. The output fuzzy set "high fan speed" is **clipped** (truncated) at 0.7.

**Step 4 — Defuzzification** (if multiple rules):

Combine all fired rules' output fuzzy sets and compute a single crisp output, e.g., using **centre of gravity** (centroid) method:

$$\text{Crisp output} = \frac{\int \mu_{\text{output}}(z) \cdot z \, dz}{\int \mu_{\text{output}}(z) \, dz}$$

### Procedure 3: Traditional Logic vs Fuzzy Logic — Hammer Thrower Example (2025 Q5)

**Scenario**: Evaluating whether an athlete is suited to be a hammer thrower using the rule:

> IF STRONG AND HEAVY THEN HAMMER_THROWER

**Traditional (crisp) logic approach:**

1. Set crisp thresholds: e.g., STRONG = bench press > 100kg, HEAVY = weight > 90kg
2. Evaluate: If athlete benches 105kg and weighs 95kg → STRONG = True, HEAVY = True
3. AND = True AND True = True
4. Result: HAMMER_THROWER = True (binary yes/no)
5. **Problem**: An athlete who benches 99kg and weighs 89kg gets HAMMER_THROWER = False, even though they are very close to the thresholds. Sharp cutoff is unrealistic.

**Fuzzy logic approach:**

1. Define membership functions:
   - $\mu_{\text{Strong}}$: maps bench press to degree in [0, 1]
   - $\mu_{\text{Heavy}}$: maps weight to degree in [0, 1]
2. Compute membership degrees: e.g., $\mu_{\text{Strong}}(\text{bench} = 95\text{kg}) = 0.7$, $\mu_{\text{Heavy}}(\text{weight} = 88\text{kg}) = 0.6$
3. Fuzzy AND: $\min(0.7, 0.6) = 0.6$
4. Result: HAMMER_THROWER suitability = 0.6 (a graded score, not binary)
5. **Advantage**: No sharp cutoff. Athletes near the boundary get intermediate scores. The system degrades gracefully.

**Key contrasts for the exam answer:**

| Aspect | Traditional Logic | Fuzzy Logic |
|---|---|---|
| STRONG and HEAVY | Binary: True or False (by threshold) | Graded: degree in [0, 1] via membership function |
| AND operation | Boolean AND (both must be True) | $\min(\mu_{\text{Strong}}, \mu_{\text{Heavy}})$ |
| Output | Binary: is/isn't a hammer thrower | Suitability score in [0, 1] |
| Boundary cases | Sharp cutoff — small difference → opposite conclusion | Smooth transition — similar inputs → similar outputs |
| Realism | Unrealistic for human attributes | More realistic — strength and heaviness are graded concepts |

### Procedure 4: Bayesian Reasoning — Burglar Alarm (Lecture Example)

**Setup:**
- $P(\text{burglary}) = 0.0001$ (1 in 10,000)
- $P(\text{alarm} \mid \text{burglary}) = 0.95$ (alarm detects 95% of burglaries)
- $P(\text{alarm} \mid \neg\text{burglary}) = 0.01$ (1% false alarm rate)

**Question**: Alarm goes off. What is $P(\text{burglary} \mid \text{alarm})$?

**Step 1 — Compute $P(\text{alarm})$ via law of total probability:**

$$P(\text{alarm}) = P(\text{alarm} \mid \text{burglary}) \cdot P(\text{burglary}) + P(\text{alarm} \mid \neg\text{burglary}) \cdot P(\neg\text{burglary})$$

$$= 0.95 \times 0.0001 + 0.01 \times 0.9999$$

$$= 0.000095 + 0.009999 = 0.010094$$

**Step 2 — Apply Bayes' theorem:**

$$P(\text{burglary} \mid \text{alarm}) = \frac{P(\text{alarm} \mid \text{burglary}) \cdot P(\text{burglary})}{P(\text{alarm})}$$

$$= \frac{0.95 \times 0.0001}{0.010094} = \frac{0.000095}{0.010094} \approx 0.0094$$

**Step 3 — Interpret:**

Still less than 1%! The alarm increased belief from 0.01% to ~0.94% — roughly a **100-fold increase** — but the base rate (prior) is so low that even strong evidence doesn't make burglary likely.

**Why?** Out of every 10,000 households:
- ~1 has a burglary, and the alarm goes off (true positive)
- ~100 have false alarms (0.01 × 9,999 ≈ 100)
- So out of ~101 alarm events, only 1 is a real burglary → about 1%

**Key insight**: The prior matters enormously. A highly sensitive test applied to a rare event will still produce mostly false positives. This is the **base rate fallacy**（基率谬误）.

### Procedure 5: Naive Bayes — Spam Detection Walkthrough

**Setup:**
- Classes: Spam ($S$) and Not-Spam ($\neg S$)
- $P(S) = 0.3$, $P(\neg S) = 0.7$
- Email contains words: "FREE" and "WINNER"
- $P(\text{"FREE"} \mid S) = 0.8$, $P(\text{"FREE"} \mid \neg S) = 0.05$
- $P(\text{"WINNER"} \mid S) = 0.6$, $P(\text{"WINNER"} \mid \neg S) = 0.02$

**Step 1 — Compute unnormalized posteriors (using naive independence):**

$$P(S \mid \text{email}) \propto P(S) \cdot P(\text{"FREE"} \mid S) \cdot P(\text{"WINNER"} \mid S)$$
$$= 0.3 \times 0.8 \times 0.6 = 0.144$$

$$P(\neg S \mid \text{email}) \propto P(\neg S) \cdot P(\text{"FREE"} \mid \neg S) \cdot P(\text{"WINNER"} \mid \neg S)$$
$$= 0.7 \times 0.05 \times 0.02 = 0.0007$$

**Step 2 — Normalize:**

$$P(S \mid \text{email}) = \frac{0.144}{0.144 + 0.0007} = \frac{0.144}{0.1447} \approx 0.995$$

**Step 3 — Classify:** 99.5% probability of spam. Classify as **Spam**.

**Step 4 — Verify with log-score version:**

$$\text{Score}(S) = \log(0.3) + \log(0.8) + \log(0.6) = -1.204 + (-0.223) + (-0.511) = -1.938$$

$$\text{Score}(\neg S) = \log(0.7) + \log(0.05) + \log(0.02) = -0.357 + (-2.996) + (-3.912) = -7.265$$

Since $-1.938 > -7.265$, classify as **Spam**. Same result, but numerically stable.

---

## ⚖️ 权衡分析（Trade-offs & Comparisons）

### Fuzzy Logic vs Naive Bayes — The Master Comparison (from lecture slide 26)

| Dimension | Fuzzy Logic（模糊逻辑） | Naive Bayes（朴素贝叶斯） |
|---|---|---|
| **Core idea** | Degree of membership / partial truth | Probability of class given evidence |
| **Handles** | Vagueness（模糊性） | Uncertainty（不确定性） |
| **Core question** | "To what degree is this true?" | "How likely is this class?" |
| **Values represent** | Degree of membership (NOT probability) | Probability |
| **Sum constraint** | Degrees need NOT sum to 1 | Probabilities MUST sum to 1 |
| **Input** | Expert-defined rules, linguistic variables | Labelled training data, feature counts |
| **Output** | Control action, recommendation strength | Class label with posterior score |
| **Knowledge source** | Domain expert encodes rules | Learned from data |
| **Key assumption** | Rules correctly capture expert knowledge | Conditional independence of features |
| **Best suited for** | Smooth rule-based control (AC, ABS, washing machine) | Lightweight probabilistic classification (spam, text) |
| **Handles continuous input** | Naturally via membership functions | Requires discretization or Gaussian assumption |
| **Interpretability** | High — rules are human-readable | Moderate — probabilities are interpretable |
| **Training** | No training needed — rules from expert | Learns from labelled data |

### When to Use Which

| Scenario | Best Approach | Why |
|---|---|---|
| Controlling room temperature | Fuzzy Logic | "Warm" / "cool" are vague; expert rules map naturally |
| Classifying emails as spam | Naive Bayes | Unknown class with probabilistic evidence from word features |
| Medical diagnosis from symptoms | Bayesian Reasoning | Unknown disease state; update belief with test results |
| Autopilot adjusting altitude | Fuzzy Logic | "Too high" / "descending fast" are graded, rule-based |
| Predicting customer churn | Naive Bayes | Binary outcome with multiple feature evidence |
| Washing machine cycle | Fuzzy Logic | "Somewhat dirty" → fuzzy rule → appropriate wash cycle |
| Sentiment analysis of reviews | Naive Bayes | Text classification with word-frequency features |

### Strengths and Weaknesses

**Fuzzy Logic:**
- ✅ Interpretable — rules are human-readable
- ✅ No training data needed — expert knowledge suffices
- ✅ Smooth, gradual response — no sharp cutoffs
- ✅ Handles linguistic variables naturally
- ❌ Requires domain expert to define rules and membership functions
- ❌ Difficult to scale to high-dimensional problems
- ❌ Rules may be subjective — different experts give different rules

**Naive Bayes:**
- ✅ Simple, fast, scalable to large datasets
- ✅ Strong baseline for text classification
- ✅ Works well with limited training data
- ✅ Probabilistic output allows confidence-based decisions
- ❌ Independence assumption is often violated in practice
- ❌ Estimated probabilities can be poorly calibrated (too extreme)
- ❌ Cannot model feature interactions (e.g., "FREE" + "WINNER" together is more spammy than each alone)

---

## 🏗️ 设计题答题框架

### Framework 1: Classifying Vagueness vs Uncertainty (Q6 pattern — 4 marks)

When given a scenario to classify, use this template for **each sub-question (1 mark each)**:

> **Template** (write this for each scenario):
>
> "This is **[vagueness / uncertainty]** because [justification]. The appropriate tool is **[Fuzzy Logic / Bayesian reasoning]** because [link to tool]."

**For vagueness:**
> "This is **vagueness** because the concept '[X]' has no sharp boundary — it is a matter of degree, and different observers might draw the boundary in different places. Fuzzy Logic is the appropriate tool, as it models graded membership through $\mu(x) \in [0,1]$."

**For uncertainty:**
> "This is **uncertainty** because there is a definite state of the world (it either is [X] or it isn't), but we lack sufficient evidence to determine which state is true. Bayesian reasoning is the appropriate tool, as it updates probability estimates over possible states using Bayes' theorem."

### Framework 2: Contrasting Traditional vs Fuzzy Logic (Q5 2025 pattern — 3 marks)

Structure your answer in three parts:

**Part A — Traditional logic approach (1 mark):**
> "In traditional logic, [concept] is evaluated with a crisp threshold (e.g., [value]). The attribute is either True or False. The AND operation is Boolean — both conditions must be True for the rule to fire. The output is binary."

**Part B — Fuzzy logic approach (1 mark):**
> "In fuzzy logic, [concept] is modelled with a membership function $\mu(x) \in [0,1]$. Each attribute has a graded degree. The AND operation uses $\min(\mu_A, \mu_B)$. The output is a continuous score representing the degree to which the conclusion holds."

**Part C — Why fuzzy is better for this case (1 mark):**
> "Fuzzy logic is more appropriate because [concept] is inherently a matter of degree — there is no natural sharp boundary. Fuzzy logic avoids the arbitrary threshold problem and provides a smooth, graded output that better reflects reality."

### Framework 3: Naive Bayes Assumptions (Q5 2024 pattern — 3 marks)

**Two key assumptions:**

1. **Conditional independence** (the "naive" part): Features $x_1, x_2, \ldots, x_n$ are independent of each other given the class label. Formally: $P(x_1, x_2, \ldots, x_n \mid C) = \prod_{i} P(x_i \mid C)$.

2. **Feature relevance**: All features contribute information about the class. (If a feature is completely irrelevant, it adds noise rather than signal.)

**Why it works despite violations:**
> "Although the independence assumption is rarely true in practice, Naive Bayes still performs well because classification only requires the correct ranking of classes, not calibrated probabilities. Many weak, correlated signals can still combine effectively to produce correct class orderings."

### Framework 4: Designing a Soft Computing System (General)

**WHAT**: State the problem and why hard computing is insufficient.
> "The problem requires handling [vagueness / uncertainty / both], which classical binary logic cannot capture."

**WHY**: Justify the choice of approach.
> "I choose [Fuzzy Logic / Bayesian / Hybrid] because [inputs are linguistically vague / we need probabilistic inference / both aspects are present]."

**HOW**: Describe the architecture.
> - For Fuzzy: Define membership functions → Write fuzzy rules → Evaluate rules (min/max) → Defuzzify output
> - For Bayesian: Define prior probabilities → Specify likelihoods → Apply Bayes' theorem → Output posterior
> - For Naive Bayes: Collect labelled training data → Estimate priors and likelihoods → Classify via argmax of posterior

**TRADE-OFF**: Acknowledge limitations.
> "One limitation is [fuzzy rules require expert knowledge / Naive Bayes assumes independence]. This can be mitigated by [learning rules from data / using full Bayesian networks that model dependencies]."

**EXAMPLE**: Give a concrete computation.
> "For example, with input temperature = 28°C, $\mu_{\text{warm}} = 0.7$, applying the rule 'IF warm THEN medium fan' gives output strength 0.7."

---

## 📝 历年真题与标准答案（Past Exam Questions — Full Model Answers）

### Q5 — S1 2025 Actual Exam [3 marks]

> **Contrast traditional logic vs fuzzy logic** for the rule:
> IF STRONG AND HEAVY THEN HAMMER_THROWER.
> Give a concrete example of how each approach would evaluate an athlete.

<details>
<summary><strong>Click to reveal model answer</strong></summary>

**Traditional logic approach:**

In traditional (crisp) logic, STRONG and HEAVY are defined by sharp thresholds — for example, STRONG = (bench press > 100kg) and HEAVY = (weight > 90kg). For an athlete who benches 95kg and weighs 88kg, both conditions evaluate to **False**, so:

$$\text{STRONG} \wedge \text{HEAVY} = \text{False} \wedge \text{False} = \text{False}$$

Result: HAMMER_THROWER = **False** (not recommended at all).

For an athlete who benches 105kg and weighs 95kg, both are **True**, so HAMMER_THROWER = **True**.

The problem: an athlete at 99kg bench press gets a completely different result from one at 101kg, despite being almost identical.

**Fuzzy logic approach:**

In fuzzy logic, STRONG and HEAVY are modelled with membership functions $\mu_{\text{Strong}}$ and $\mu_{\text{Heavy}}$, each mapping to $[0, 1]$. For the same athlete (bench 95kg, weight 88kg):

$$\mu_{\text{Strong}}(95\text{kg}) = 0.7, \quad \mu_{\text{Heavy}}(88\text{kg}) = 0.6$$

$$\text{Fuzzy AND} = \min(0.7, 0.6) = 0.6$$

Result: HAMMER_THROWER suitability = **0.6** — a graded recommendation rather than a binary yes/no.

**Key contrast:** Traditional logic produces a binary classification with sharp, arbitrary cutoffs. Fuzzy logic produces a graded suitability score that transitions smoothly, better reflecting that strength and heaviness are inherently graded concepts with no natural sharp boundary.

</details>

---

### Q6 — S1 2026 Sample Test [4 marks]

> For each of the following, classify as **vagueness** or **uncertainty** and briefly justify:
> 1. "This patient is high risk."
> 2. An alarm went off — was it a burglar?
> 3. "Student 74 is almost excellent."
> 4. Email spam filter with incomplete evidence.

<details>
<summary><strong>Click to reveal model answer</strong></summary>

1. **Vagueness** — "High risk" is a concept with no sharp boundary. At what exact point does a patient become "high risk"? 50% risk? 60%? Different clinicians might disagree. The concept itself admits of degrees. The appropriate tool is **Fuzzy Logic**, which models the degree to which a patient is "high risk" via a membership function $\mu_{\text{high\_risk}} \in [0, 1]$.

2. **Uncertainty** — Either a burglary occurred or it did not — there is a definite fact about the world. We have evidence (the alarm) but do not know the true state with certainty. The appropriate tool is **Bayesian reasoning**, which computes $P(\text{burglary} \mid \text{alarm})$ using Bayes' theorem.

3. **Vagueness** — The grade 74 is known precisely; there is no hidden fact. The concept "almost excellent" is a graded, linguistic term with blurry boundaries — where exactly does "almost excellent" begin? 70? 72? 75? The appropriate tool is **Fuzzy Logic**, with a membership function for "almost excellent" (e.g., $\mu_{\text{almost\_excellent}}(74) = 0.7$).

4. **Uncertainty** — The email is either spam or not spam (a definite class). We have incomplete evidence (word frequencies, sender info) and need to infer which class is true. The appropriate tool is **Naive Bayes**, which computes $P(\text{spam} \mid \text{features})$ via Bayes' theorem with conditional independence assumption.

</details>

---

### Q5 — S1 2024 Final [~3 marks]

> State the key assumptions of the Naive Bayes classifier and explain why it works well in practice despite these assumptions being violated.

<details>
<summary><strong>Click to reveal model answer</strong></summary>

**Key assumptions:**

1. **Conditional independence**: Given the class label $C$, all features $x_1, x_2, \ldots, x_n$ are independent of each other. Formally:
$$P(x_1, x_2, \ldots, x_n \mid C) = \prod_{i=1}^{n} P(x_i \mid C)$$
This means knowing the value of one feature provides no information about any other feature, once we know the class. In practice, this is almost always violated — for example, in spam detection, the words "FREE" and "WINNER" are correlated (they tend to co-occur in spam).

2. **Feature relevance**: All features are assumed to carry some discriminative information about the class. Irrelevant features can degrade performance by adding noise.

**Why it works despite violations:**

- **Only ranking matters**: For classification, we only need $P(C_1 \mid \mathbf{x}) > P(C_2 \mid \mathbf{x})$, not exact probability values. Even when individual probability estimates are biased due to violated independence, the relative ordering of classes is often preserved.
- **Many weak signals combine effectively**: In high-dimensional problems like text classification, each word provides a small signal. The product of many such signals (even if correlated) still tends to point toward the correct class.
- **Easy parameter estimation**: We only need to estimate univariate distributions $P(x_i \mid C)$, not the full joint distribution. This requires far less training data and avoids overfitting in high-dimensional feature spaces.
- **Errors cancel out**: Positive and negative correlations among features tend to partially cancel each other, making the overall prediction more robust than the individual estimates might suggest.

</details>

---

## 📝 Additional Practice Questions

### Practice Q1: New Vagueness vs Uncertainty Scenarios [4 marks]

> Classify each scenario as **vagueness** or **uncertainty**. Justify your answer and name the appropriate reasoning tool.
>
> (a) "This coffee is too hot to drink."
> (b) A pregnancy test shows positive — is the person actually pregnant?
> (c) "The traffic is heavy on the motorway."
> (d) Based on satellite imagery, did deforestation occur in this region last year?

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a) Vagueness** — "Too hot" has no sharp boundary. At what exact temperature does coffee become "too hot"? 60°C? 65°C? 70°C? The concept admits degrees. Tool: **Fuzzy Logic** ($\mu_{\text{too\_hot}}(65°\text{C}) = 0.6$).

**(b) Uncertainty** — The person either is pregnant or is not — a definite biological fact. The test provides probabilistic evidence, but we don't know the true state with certainty. Tool: **Bayesian Reasoning** (update prior with test sensitivity/specificity).

**(c) Vagueness** — "Heavy traffic" is a graded concept. Is 50 cars/minute heavy? 80? 120? There is no universally agreed crisp boundary. Tool: **Fuzzy Logic**.

**(d) Uncertainty** — Either deforestation occurred or it didn't — a definite historical fact. We have incomplete evidence (satellite images may be cloudy or ambiguous). Tool: **Bayesian Reasoning** (probability of deforestation given observed image features).

</details>

---

### Practice Q2: Fuzzy Logic Computation [3 marks]

> Given:
> - $\mu_A = 0.6$ (degree to which temperature is "warm")
> - $\mu_B = 0.9$ (degree to which humidity is "high")
>
> Compute:
> (a) $A \wedge B$ (Fuzzy AND)
> (b) $A \vee B$ (Fuzzy OR)
> (c) $\neg A$ (Fuzzy NOT)
> (d) $A \rightarrow B$ using Godel implication
> (e) $A \rightarrow B$ using standard implication

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a)** $A \wedge B = \min(0.6, 0.9) = 0.6$

**(b)** $A \vee B = \max(0.6, 0.9) = 0.9$

**(c)** $\neg A = 1 - 0.6 = 0.4$

**(d)** Godel: Since $A = 0.6 \leq B = 0.9$, we get $A \rightarrow B = 1$.
(If the antecedent holds to degree 0.6 and the consequent holds to degree 0.9, the implication is fully satisfied — the consequent "more than covers" the antecedent.)

**(e)** Standard: $A \rightarrow B = \max(1 - 0.6, 0.9) = \max(0.4, 0.9) = 0.9$

</details>

---

### Practice Q3: Fuzzy Implication Edge Case [2 marks]

> Given $\mu_A = 0.7$ and $\mu_B = 0.3$:
>
> (a) Compute $A \rightarrow B$ using Godel implication.
> (b) Compute $A \rightarrow B$ using standard implication.
> (c) Now compute for $A = 0.5, B = 0$ using both. Which is more intuitive?

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a)** Godel: Since $A = 0.7 > B = 0.3$, return $B = 0.3$.

**(b)** Standard: $\max(1 - 0.7, 0.3) = \max(0.3, 0.3) = 0.3$. (Same result here.)

**(c)** For $A = 0.5, B = 0$:
- Standard: $\max(1 - 0.5, 0) = \max(0.5, 0) = 0.5$
- Godel: Since $0.5 > 0$, return $B = 0$

The **Godel version is more intuitive** here. If the antecedent holds to degree 0.5 but the consequent is completely false (0), it makes sense that the implication should fail entirely (= 0). The standard version giving 0.5 is counterintuitive — it suggests the implication is "half true" even though the consequent is completely false.

</details>

---

### Practice Q4: Bayesian Reasoning Calculation [4 marks]

> A medical test for a rare disease:
> - $P(\text{disease}) = 0.002$ (prevalence: 2 in 1,000)
> - $P(\text{positive} \mid \text{disease}) = 0.98$ (sensitivity)
> - $P(\text{positive} \mid \neg\text{disease}) = 0.03$ (false positive rate)
>
> (a) Compute $P(\text{positive})$.
> (b) Compute $P(\text{disease} \mid \text{positive})$.
> (c) Interpret the result.

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a)**

$$P(\text{positive}) = P(\text{pos} \mid \text{disease}) \cdot P(\text{disease}) + P(\text{pos} \mid \neg\text{disease}) \cdot P(\neg\text{disease})$$

$$= 0.98 \times 0.002 + 0.03 \times 0.998$$

$$= 0.00196 + 0.02994 = 0.0319$$

**(b)**

$$P(\text{disease} \mid \text{positive}) = \frac{P(\text{pos} \mid \text{disease}) \cdot P(\text{disease})}{P(\text{positive})} = \frac{0.98 \times 0.002}{0.0319} = \frac{0.00196}{0.0319} \approx 0.0614$$

**(c)** Only about **6.1%** chance of having the disease despite a positive test. The test increased belief from 0.2% to 6.1% (a ~30x increase), but because the disease is rare (low prior), most positive tests are still false positives. The patient should get a confirmatory second test rather than panicking. This illustrates the **base rate fallacy** — a sensitive test on a rare condition still produces many false positives because the low base rate dominates.

</details>

---

### Practice Q5: Naive Bayes Classification [3 marks]

> You are building a fruit classifier. Given:
>
> | Feature | P(feature \| Apple) | P(feature \| Orange) |
> |---|---|---|
> | Red | 0.7 | 0.1 |
> | Round | 0.8 | 0.9 |
> | Smooth skin | 0.3 | 0.8 |
>
> $P(\text{Apple}) = 0.5$, $P(\text{Orange}) = 0.5$
>
> A fruit is Red, Round, and has Smooth skin. Classify it.

<details>
<summary><strong>Click to reveal answers</strong></summary>

**Apple score:**

$$P(\text{Apple}) \times P(\text{Red} \mid \text{Apple}) \times P(\text{Round} \mid \text{Apple}) \times P(\text{Smooth} \mid \text{Apple})$$

$$= 0.5 \times 0.7 \times 0.8 \times 0.3 = 0.084$$

**Orange score:**

$$P(\text{Orange}) \times P(\text{Red} \mid \text{Orange}) \times P(\text{Round} \mid \text{Orange}) \times P(\text{Smooth} \mid \text{Orange})$$

$$= 0.5 \times 0.1 \times 0.9 \times 0.8 = 0.036$$

**Comparison:** $0.084 > 0.036$, so classify as **Apple**.

**Normalized posterior:** $P(\text{Apple} \mid \text{features}) = 0.084 / (0.084 + 0.036) = 0.084 / 0.120 = 0.70 = 70\%$

The "Red" feature strongly favours Apple ($0.7$ vs $0.1$), which outweighs the "Smooth skin" evidence favouring Orange ($0.3$ vs $0.8$). This shows how Naive Bayes weighs each feature's contribution independently.

</details>

---

### Practice Q6: Naive Bayes with Log-Score [3 marks]

> Using the same fruit example above, compute the log-scores and verify the classification.

<details>
<summary><strong>Click to reveal answers</strong></summary>

**Apple log-score:**

$$\log(0.5) + \log(0.7) + \log(0.8) + \log(0.3)$$
$$= -0.693 + (-0.357) + (-0.223) + (-1.204) = -2.477$$

**Orange log-score:**

$$\log(0.5) + \log(0.1) + \log(0.9) + \log(0.8)$$
$$= -0.693 + (-2.303) + (-0.105) + (-0.223) = -3.324$$

Since $-2.477 > -3.324$, classify as **Apple**. Same result as the product version, but using addition in log-space avoids the risk of numerical underflow when there are many features.

Note how each feature's contribution is additive in log-space:
- Prior: same ($-0.693$)
- Red: Apple gets $-0.357$ vs Orange gets $-2.303$ → Red strongly favours Apple (difference of $+1.946$)
- Round: Apple gets $-0.223$ vs Orange gets $-0.105$ → Round slightly favours Orange
- Smooth: Apple gets $-1.204$ vs Orange gets $-0.223$ → Smooth favours Orange (difference of $-0.981$)

Net effect: Red's contribution ($+1.946$) outweighs Smooth's ($-0.981$), so Apple wins.

</details>

---

### Practice Q7: Fuzzy Control System [3 marks]

> A fuzzy controller for a car's ABS (Anti-lock Braking System) uses two inputs:
> - Speed: $\mu_{\text{fast}}(v) = 0.9$
> - Road condition: $\mu_{\text{slippery}}(\text{road}) = 0.5$
>
> Rule 1: IF speed is fast AND road is slippery THEN brake pressure is low.
> Rule 2: IF speed is fast AND road is NOT slippery THEN brake pressure is high.
>
> (a) Compute the firing strength of Rule 1.
> (b) Compute the firing strength of Rule 2.
> (c) Which rule fires more strongly? What does this mean for the braking?

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a)** Rule 1: $\min(\mu_{\text{fast}}, \mu_{\text{slippery}}) = \min(0.9, 0.5) = 0.5$

**(b)** Rule 2: $\min(\mu_{\text{fast}}, \neg\mu_{\text{slippery}}) = \min(0.9, 1 - 0.5) = \min(0.9, 0.5) = 0.5$

**(c)** Both rules fire with equal strength (0.5). This makes sense — the road is exactly at the boundary between slippery and not slippery ($\mu = 0.5$). The defuzzification step would combine both rules' outputs, producing a **moderate** brake pressure — a compromise between "low" and "high." This is precisely the advantage of fuzzy control: instead of an abrupt switch between strategies, it produces a smooth blend.

</details>

---

### Practice Q8: Conceptual Short Answer [2 marks each]

> (a) A fuzzy set assigns $\mu_{\text{Tall}}(175\text{cm}) = 0.4$. A student says: "This means there is a 40% probability the person is tall." Is this correct? Explain.
>
> (b) Why does Naive Bayes work well in practice despite its unrealistic independence assumption?
>
> (c) In the burglar alarm example, $P(\text{burglary} \mid \text{alarm}) \approx 0.94\%$. Why so low despite 95% alarm reliability?
>
> (d) What is the difference between $P(e \mid H)$ and $P(H \mid e)$? Why do people often confuse them?

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a)** Incorrect. The value 0.4 is a **degree of membership**, not a probability. There is no randomness — the person is definitely 175cm. The 0.4 expresses how much the vague concept "Tall" applies to this height. Fuzzy membership handles **vagueness** (blurry concepts); probability handles **uncertainty** (unknown states). They are fundamentally different: $\mu_{\text{Tall}} + \mu_{\text{Short}}$ does NOT need to equal 1, but $P(\text{tall}) + P(\neg\text{tall})$ MUST equal 1.

**(b)** For classification, we only need the correct **ranking** of classes, not exact posterior probabilities. Even when features are correlated (violating independence), the class with the highest true posterior typically still receives the highest Naive Bayes score. Additionally, in high-dimensional data (like text), more complex models that model feature dependencies may overfit, while Naive Bayes remains stable due to its simplicity.

**(c)** Because the **prior probability** of burglary is extremely low ($P = 0.0001$). Although the alarm is 95% sensitive, false alarms ($P(\text{alarm} \mid \neg\text{burglary}) = 0.01$) applied to the ~10,000 non-burglary events produce ~100 false alarms. So out of ~101 total alarms, only ~1 is a true burglary. This is the **base rate fallacy** — ignoring how rare the event is leads to overestimating the posterior.

**(d)** $P(e \mid H)$ is the **likelihood** — "If the hypothesis is true, how likely is the evidence?" $P(H \mid e)$ is the **posterior** — "Given the evidence, how likely is the hypothesis?" People confuse them because intuitively, "the alarm is 95% reliable" ($P(\text{alarm} \mid \text{burglary}) = 0.95$) *feels* like it should mean "if the alarm goes off, there's a 95% chance of burglary" ($P(\text{burglary} \mid \text{alarm}) = 0.95$). But these are NOT the same — the posterior also depends on the prior. This confusion is called the **prosecutor's fallacy** or **confusion of the inverse**.

</details>

---

### Practice Q9: Contrast Traditional vs Fuzzy for a New Scenario [3 marks]

> Compare how traditional logic and fuzzy logic would evaluate the rule:
> IF EXPERIENCED AND CREATIVE THEN GOOD_DESIGNER
>
> Use a concrete example of a candidate.

<details>
<summary><strong>Click to reveal answers</strong></summary>

**Traditional logic:**

Set crisp thresholds — e.g., EXPERIENCED = (years > 5), CREATIVE = (portfolio score > 80/100).

For a candidate with 4 years experience and portfolio score 78:
- EXPERIENCED = False (4 < 5)
- CREATIVE = False (78 < 80)
- GOOD_DESIGNER = False AND False = **False**

This candidate is rejected entirely, despite being very close to both thresholds.

**Fuzzy logic:**

Define membership functions for EXPERIENCED and CREATIVE, each mapping to [0, 1].

For the same candidate:
- $\mu_{\text{Experienced}}(4 \text{ years}) = 0.7$ (fairly experienced)
- $\mu_{\text{Creative}}(78) = 0.8$ (quite creative)
- Fuzzy AND: $\min(0.7, 0.8) = 0.7$
- GOOD_DESIGNER suitability = **0.7** (a strong recommendation)

**Key contrast:** Traditional logic gives a binary rejection despite the candidate being close to thresholds. Fuzzy logic gives a graded score (0.7) reflecting that this candidate is a fairly good designer. For concepts like "experienced" and "creative" that inherently admit degrees, fuzzy logic provides a more realistic and nuanced evaluation.

</details>

---

### Practice Q10: Quick Quiz (from Lecture) [3 marks]

> (a) What does fuzzy logic primarily model?
> A. Uncertainty in data   B. Probability of events   C. Vagueness in concepts   D. Statistical correlation
>
> (b) If fuzzy membership $\mu_A = 0.6$ and $\mu_B = 0.8$, what is $A \wedge B$?
> A. 0.6   B. 0.8   C. 0.7   D. 1.0
>
> (c) What is the key assumption of Naive Bayes?
> A. Features are independent of the class   B. Features are conditionally independent given the class   C. All features have equal weight   D. The prior is uniform

<details>
<summary><strong>Click to reveal answers</strong></summary>

**(a) C** — Fuzzy logic models **vagueness** in concepts (blurry boundaries), not uncertainty (which is handled by Bayesian reasoning).

**(b) A** — Fuzzy AND = $\min(0.6, 0.8) = 0.6$. The conjunction is limited by the weaker component.

**(c) B** — Features are **conditionally independent given the class**. Note: NOT "independent of the class" (that would mean features carry no information). The "naive" assumption is that features are independent of *each other* once we know the class.

</details>

---

## 🌐 英语表达要点（English Expression）

### Describing Vagueness vs Uncertainty

```
"This is an example of vagueness because the concept '[X]' admits of degrees
 and has no sharp boundary — it is not a yes/no matter."

"This is an example of uncertainty because there is a definite state of the
 world, but we lack sufficient evidence to determine which state is true."

"Vagueness concerns the definition of a concept; uncertainty concerns
 our knowledge of a fact."
```

### Describing Fuzzy Logic

```
"Fuzzy Logic models graded concepts through membership functions
 μ(x) ∈ [0, 1], where 0 means complete non-membership and 1 means
 full membership."

"The fuzzy AND of two values is computed as their minimum:
 min(μ_A, μ_B). This captures the idea that a conjunction is only
 as strong as its weakest component."

"A membership value of 0.7 indicates that the element belongs to
 the fuzzy set to degree 0.7 — this is NOT a probability."

"Fuzzy logic is particularly suited to control systems because
 concepts like 'warm', 'fast', and 'heavy' are inherently graded."
```

### Describing Bayesian Reasoning

```
"By Bayes' theorem, the posterior probability P(H|e) is proportional
 to the prior P(H) multiplied by the likelihood P(e|H)."

"The prior represents our initial belief before observing evidence,
 while the posterior represents our updated belief after evidence."

"The base rate fallacy occurs when we ignore the prior probability
 and overweight the evidence, leading to incorrect conclusions."
```

### Describing Naive Bayes

```
"Naive Bayes assumes conditional independence of features given the
 class, which simplifies the joint likelihood to a product of
 individual feature likelihoods."

"Despite its 'naive' assumption, Naive Bayes works well in practice
 because classification only requires correct ranking of classes,
 not calibrated probability estimates."

"The log-score version converts multiplication to addition,
 preventing numerical underflow when many features are involved."
```

### Contrasting Traditional vs Fuzzy Logic (for Q5-type questions)

```
"In traditional logic, [attribute] is evaluated against a crisp
 threshold, producing a binary True/False result."

"In fuzzy logic, [attribute] is modelled with a membership function
 that maps to a continuous degree in [0, 1]."

"The key advantage of fuzzy logic is that it avoids arbitrary
 threshold effects and produces smooth, graded outputs."

"Fuzzy logic is more appropriate here because [concept] is
 inherently a matter of degree with no natural sharp boundary."
```

### 易错表达 / Common Expression Mistakes

| Incorrect Expression | Correct Expression | Why |
|---|---|---|
| "Fuzzy Logic handles uncertainty" | "Fuzzy Logic handles **vagueness**" | Uncertainty → Bayes; Vagueness → Fuzzy |
| "μ = 0.6 means 60% probability" | "μ = 0.6 means **degree of membership** 0.6" | Membership ≠ probability |
| "Soft computing is imprecise, so it's worse" | "Soft computing **tolerates** imprecision to solve harder problems" | Tolerance of imprecision is a strength |
| "Naive Bayes requires independent features" | "Naive Bayes **assumes conditional** independence" | The assumption may be violated but NB still works |
| "The posterior is the prior times the likelihood" | "The posterior is **proportional to** prior times likelihood" | Must normalise by $P(e)$ for exact values |
| "P(e\|H) = P(H\|e)" | "P(e\|H) is the likelihood; P(H\|e) is the posterior — they are different" | Confusion of the inverse / prosecutor's fallacy |
| "Fuzzy degrees must sum to 1" | "Fuzzy membership degrees do **NOT** need to sum to 1" | Only probabilities must sum to 1 |

### 高频考试用词

- **admits of degrees** — 承认程度差异（describes vagueness）
- **base rate** — 基率（prior probability of a rare event）
- **base rate fallacy** — 基率谬误（ignoring the prior when interpreting evidence）
- **conditionally independent** — 条件独立（the "naive" assumption in Naive Bayes）
- **crisp boundary** — 清晰边界（classical sets have it; fuzzy sets don't）
- **degrades gracefully** — 优雅降级（soft computing's advantage over hard computing）
- **defuzzification** — 去模糊化（converting fuzzy output to a crisp value）
- **degree of membership** — 隶属度（NOT probability）
- **false positive rate** — 假阳性率 ($P(\text{positive} \mid \neg\text{disease})$)
- **firing strength** — 规则触发强度（the result of evaluating a fuzzy rule's antecedent）
- **linguistic variable** — 语言变量（e.g., "temperature" with values "cold", "warm", "hot"）
- **likelihood** — 似然 ($P(e \mid H)$, not to be confused with posterior)
- **posterior** — 后验概率 ($P(H \mid e)$)
- **prior** — 先验概率 ($P(H)$)
- **sensitivity** — 灵敏度 ($P(\text{positive} \mid \text{disease})$)

---

## ✅ 自测检查清单

### Concepts — Vagueness vs Uncertainty
- [ ] Can I define vagueness and uncertainty in one sentence each in English?
- [ ] Can I correctly classify 4+ new scenarios as vagueness or uncertainty?
- [ ] Can I explain why "soft" does not mean "weak"?
- [ ] Do I know the two-step decision procedure for classifying vagueness vs uncertainty?

### Fuzzy Logic
- [ ] Can I compute fuzzy AND ($\min$), OR ($\max$), and NOT ($1 - \mu$)?
- [ ] Can I compute both standard and Godel fuzzy implication?
- [ ] Can I explain why $\mu = 0.6$ is NOT a probability?
- [ ] Can I explain why fuzzy degrees do NOT need to sum to 1?
- [ ] Can I describe the fuzzy control pipeline (fuzzification → inference → defuzzification)?
- [ ] Can I contrast traditional logic vs fuzzy logic for a given rule (like hammer thrower)?
- [ ] Can I name 3+ real-world fuzzy logic applications?

### Bayesian Reasoning
- [ ] Can I write Bayes' theorem from memory and explain each term?
- [ ] Can I expand $P(e)$ using the law of total probability?
- [ ] Can I work through the burglar alarm example step by step?
- [ ] Can I explain the base rate fallacy in my own words?
- [ ] Do I know the difference between $P(e \mid H)$ and $P(H \mid e)$?

### Naive Bayes
- [ ] Can I state the conditional independence assumption precisely?
- [ ] Can I compute a Naive Bayes classification by hand (multiply priors and likelihoods)?
- [ ] Can I normalize to get actual posterior probabilities?
- [ ] Can I write the log-score version and explain why it prevents underflow?
- [ ] Can I explain why Naive Bayes works despite unrealistic assumptions (3 reasons)?

### Exam Readiness
- [ ] Can I answer a Q6-style question (4 scenarios, vagueness vs uncertainty) in under 5 minutes?
- [ ] Can I write a full contrast answer for traditional vs fuzzy logic in under 8 minutes?
- [ ] Can I state and justify Naive Bayes assumptions in a short answer?
- [ ] Do I know the Fuzzy Logic vs Naive Bayes comparison table from memory?
- [ ] Can I do a full Bayes' theorem calculation without referring to notes?
