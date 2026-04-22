# Logic Neural Networks (LNN) & Differentiable Logic

## 🎯 Exam Importance

🔴 **必考 — LNN appears as Question 2 in EVERY test paper**

| Test Paper | Question | Marks | Topic |
|-----------|----------|-------|-------|
| Sample Test S1 2025 | Q2 (2 marks) | (a) 1 mark + (b) 1 mark | HeatingOn rule: natural language + compute soft AND |
| Actual Mid-Test S1 2025 | Q2 (3 marks) | (a) 1 mark + (b) 2 marks | Autonomous vehicle: LNN bounds with OR, safety-critical reasoning |
| Sample Test S1 2026 | Q2 (4 marks) | (a) 2 marks + (b) 2 marks | HeatingOn rule: natural language + compute soft AND |

**Pattern**: LNN is always Q2, worth 2-4 marks (13-20% of the test). Two sub-patterns repeat:
1. **Interpret an LNN rule in natural language and contrast with Boolean logic** (every test)
2. **Either compute a soft-logic value OR reason about truth bounds** (every test)

---

## 📖 Core Concepts

| English Term | 中文 | One-Sentence Definition |
|-------------|------|------------------------|
| Logic Neural Network / LNN | 逻辑神经网络 | A neural-symbolic system where the network structure mirrors a logical syntax tree, operating on continuous truth values [0,1] |
| Differentiable Logic / Soft Logic | 可微分逻辑 | Converting discrete Boolean operators into smooth continuous functions so gradient descent can be applied |
| Product-Sum T-norm | 积-和三角范数 | A specific soft logic: AND = $A \times B$, OR = $A + B - A \times B$, NOT = $1 - A$ |
| Lukasiewicz Logic | 卢卡西维茨逻辑 | A many-valued logic: AND = $\max(0, a+b-1)$, OR = $\min(1, a+b)$ |
| Truth Bounds [L, U] | 真值界 | Each proposition maintains a lower bound L and upper bound U, where $0 \le L \le U \le 1$ |
| Threshold $\alpha$ | 分类阈值 | The cutoff value used to classify truth bounds into TRUE / FALSE / UNCERTAIN |
| Upward Pass | 上行传播 | Information flows from leaf inputs up to the conclusion (like forward chaining) |
| Downward Pass | 下行传播 | Information flows from conclusion back to premises (like backward chaining) |
| Bidirectional Inference | 双向推理 | LNN runs both upward and downward passes until bounds converge |
| Three-Valued Logic | 三值逻辑 | Logic with three truth values: True (T), Unknown (U), False (F) |
| Neural-Symbolic AI | 神经符号AI | An approach that combines neural network learning with symbolic logical reasoning |

---

## 🧠 Feynman Draft -- From Zero to LNN

### Part 1: Why Do We Need Logic in Neural Networks?

Imagine a doctor looking at an X-ray. A neural network might say "85% chance of cancer" -- but the doctor asks *why*. The neural network shrugs. It is a **black box（黑盒）**: powerful at pattern recognition but terrible at explaining itself.

Now imagine a rule-based system: "IF the patient has a tumor larger than 2cm AND the margins are irregular THEN suspect malignancy." This is **transparent** -- you can see exactly why the decision was made. But writing thousands of such rules by hand is impractical, and rules cannot handle "maybe" situations.

**LNN is the marriage of both**: it keeps the logical structure (so you can read the rules) but makes the operators smooth and continuous (so gradient descent can learn the parameters from data).

### Part 2: From Light Switches to Dimmer Switches

Classical Boolean logic is like a light switch -- strictly ON (1) or OFF (0). But the real world is not binary. Is 12 degrees Celsius "cold"? It is *somewhat* cold -- maybe 0.6 out of 1.0.

**Soft logic replaces the light switch with a dimmer switch.** Instead of {0, 1}, truth values live in the continuous interval [0, 1]. Every logical operator (AND, OR, NOT) becomes a smooth function.

**Why does smoothness matter?** Because neural networks learn by computing gradients. Boolean AND has zero gradient almost everywhere (it is a step function), so backpropagation cannot adjust weights. But if AND = $A \times B$, the gradient $\frac{\partial}{\partial A} = B$ exists everywhere. Now we can learn!

### Part 3: The Dimmer Switch Operators (Product-Sum)

This is the specific soft logic system used in the exam. Memorize it.

| Operator | Boolean Version | Soft Logic (Product-Sum) |
|---------|----------------|------------------------|
| AND ($\wedge$) | Both must be 1 | $A \times B$ |
| OR ($\vee$) | At least one is 1 | $A + B - A \times B$ |
| NOT ($\neg$) | Flip 0/1 | $1 - A$ |

**Why does OR = $A + B - AB$?** Think of probability. If you roll two dice, the chance of at least one six is $P(A) + P(B) - P(A \text{ and } B)$. The subtraction avoids double-counting the overlap. This is exactly the inclusion-exclusion principle.

### Part 4: What Makes LNN Different from Plain Fuzzy Logic?

> ⚠️ **Common Misconception**: Students think LNN is just "fuzzy logic with a neural network." This is WRONG. LNN has three features that fuzzy logic lacks:
> 1. **Learnable weights** -- the operator parameters are tuned by gradient descent
> 2. **Bidirectional inference** -- information flows both up (inputs to conclusion) AND down (conclusion to inputs), not just one direction
> 3. **Logical soundness guarantees** -- LNN is mathematically proven to maintain consistency

### Part 5: Truth Bounds -- The Safety Net

Instead of a single number, LNN gives you a **range** [L, U] for each proposition. Think of it as a confidence interval:

- **Cold = [0.8, 1.0]** means "we are fairly sure it is cold -- at least 0.8, possibly up to 1.0"
- **AtHome = [0.3, 0.5]** means "quite uncertain whether someone is home"

Given a threshold $\alpha$:
- If **both L and U are above $\alpha$** ($L \ge \alpha$) -- **Definitely TRUE**
- If **both L and U are below $\alpha$** ($U \le \alpha$) -- **Definitely FALSE**
- If **L < $\alpha$ < U** (bounds straddle the threshold) -- **UNCERTAIN**
- If **L > U** -- **CONTRADICTION** (should not happen in a well-formed LNN)

> 💡 **Core Intuition**: LNN replaces Boolean {0,1} switches with smooth [0,1] dimmers, adds confidence bounds [L,U], and uses bidirectional message passing -- giving you learnable, explainable, uncertainty-aware reasoning.

---

## 📐 Formal Definitions

### Soft Logic Operators (Product-Sum) -- THE EXAM DEFAULT

These are the operators used in all exam questions unless stated otherwise:

$$\text{AND}(A, B) = A \times B$$

$$\text{OR}(A, B) = A + B - A \times B$$

$$\text{NOT}(A) = 1 - A$$

### Three T-Norms You Must Know

| T-norm | AND formula | OR formula | NOT formula |
|--------|-----------|-----------|------------|
| **Product** (exam default) | $A \times B$ | $A + B - AB$ | $1 - A$ |
| **Lukasiewicz** | $\max(0, A + B - 1)$ | $\min(1, A + B)$ | $1 - A$ |
| **Godel (min/max)** | $\min(A, B)$ | $\max(A, B)$ | $1 - A$ |

### Lukasiewicz-like Logic in LNN (from Slide 40)

The lecture defines a **basis activation function（基础激活函数）**:

$$f(x) = \max(0, \min(1, x))$$

This clamps the output to [0, 1]. Then:

**Logical AND** for inputs $x_1, x_2, ..., x_n$:

$$\bigwedge_{i \in I} x_i = f\left(1 - \sum_i (1 - x_i)\right)$$

**Logical OR** for inputs $x_1, x_2, ..., x_n$:

$$\bigvee_{i \in I} x_i = f\left(\sum_i x_i\right)$$

### Truth Bounds Classification (from Slide 34)

Given bounds [L, U] and threshold $\alpha$:

| Lower Bound (L) | Upper Bound (U) | Classification |
|-----------------|-----------------|---------------|
| $L = 0$ | $U = 1$ | **Unknown** (no information) |
| $L \le \alpha$ | $U \le \alpha$ | **False** (both bounds below threshold) |
| $L \ge \alpha$ | $U \ge \alpha$ | **True** (both bounds above threshold) |
| $L > U$ | -- | **Contradiction** (inconsistent) |
| $L < \alpha$ | $U > \alpha$ | **Uncertain** (bounds straddle threshold) |

```
Truth Bounds Visualization:

0                   α                   1
|===================|===================|
        L_____U                           → FALSE (both below α)
                        L_____U           → TRUE (both above α)
              L___________U               → UNCERTAIN (spans α)
                  U___L                   → CONTRADICTION (L > U)
```

### Three-Valued Logic Truth Tables (from Slide 35)

**AND ($\wedge$):**

| A | B | A $\wedge$ B |
|---|---|-------------|
| T | T | **T** |
| T | U | **U** |
| T | F | **F** |
| U | U | **U** |
| U | F | **F** |
| F | F | **F** |

Key rule for AND: **Any F makes the result F. Both must be T for T. Otherwise U.**

**OR ($\vee$):**

| A | B | A $\vee$ B |
|---|---|-----------|
| T | T | **T** |
| T | U | **T** |
| T | F | **T** |
| U | U | **U** |
| U | F | **U** |
| F | F | **F** |

Key rule for OR: **Any T makes the result T. Both must be F for F. Otherwise U.**

> ⚠️ **Common Misconception**: Students confuse which operator "dominates." For AND, **False dominates** (one False makes everything False). For OR, **True dominates** (one True makes everything True). This is the key to Exercise 8 and the 2025 actual test question.

### LNN Architecture -- Syntax Tree as Network

In LNN, every logical formula is compiled into a computation graph where:
- **Each node is a neuron** representing a logical operator or proposition
- **The structure follows the syntax tree** of the formula
- **Each edge passes truth bounds [L, U]** (not just single values)

```
Example: (Whiskers ⊗ Tail ⊗ (Laser pointer → Chases)) → Cat
         (Cat ⊕ Dog) → Pet

                              Pet
                               |
                          [⊕ (OR)]
                          /       \
                        Cat       Dog
                         |
                    [→ (IMPLIES)]
                    /            \
            [⊗ (AND)]        (this is Cat)
           /    |     \
     Whiskers  Tail  [→ (IMPLIES)]
                      /          \
               Laser pointer   Chases
```

- **$\otimes$ (circled multiply)** = AND-like operation (soft conjunction)
- **$\oplus$ (circled plus)** = OR-like operation (soft disjunction)
- **$\rightarrow$ (arrow)** = Implication (if...then)

### LNN Workflow (from Slides 33, 42)

```
Step 1: READ INPUTS
   - Known facts set bounds:
     e.g., cat is true → L_cat = 1, U_cat = 1
     e.g., ¬dog → L_dog = 0, U_dog = 0
   - Unknown propositions: L = 0, U = 1 (complete uncertainty)

Step 2: BIDIRECTIONAL MESSAGE PASSING (iterate until convergence)
   
   Upward Pass (children → parent):
   - "If dog and cat influence pet, compute pet's bounds from dog and cat"
   - Parent bounds are TIGHTENED based on children
   
   Downward Pass (parent → children):
   - "If pet is known to be true, what constraints does this put on dog and cat?"
   - Children bounds are TIGHTENED based on parent
   
   Repeat until bounds stop changing (convergence)

Step 3: READ FINAL BOUNDS
   - Inspect target neuron's [L, U]
   - Apply threshold α to classify as TRUE / FALSE / UNCERTAIN
```

---

## 🔄 Worked Examples -- Every Computation Step

### === EXAM QUESTION TYPE 1: Interpret LNN Rule + Compute Soft AND ===

This is the most frequently tested pattern. It appears in the Sample Test 2025, Sample Test 2026, and closely matches the lecture exercises.

---

### Worked Example 1: HeatingOn Rule (Sample Test 2025 Q2, Sample Test 2026 Q2)

**Question:**
A smart home system uses an LNN with the rule:

$$\text{HeatingOn} \leftarrow \text{Cold} \otimes \text{AtHome}$$

(a) What does this rule represent in natural language? How is it different from a standard Boolean rule?

(b) Given Cold = 0.9, AtHome = 0.4, compute HeatingOn. Would the system activate?

**Model Answer (a) -- 1-2 marks:**

> This rule reads: "If it is cold AND someone is at home, then the heating system should be turned on."
>
> In **standard Boolean logic**, both Cold and AtHome must be strictly True (= 1) for HeatingOn to fire. The output is binary: heating is either fully ON or fully OFF.
>
> In **LNN**, the $\otimes$ operator is a **differentiable soft conjunction** over continuous truth values in [0, 1]. It accepts partial inputs (like Cold = 0.9, AtHome = 0.4) and produces an intermediate activation (like 0.36), reflecting **degrees of truth**. This enables:
> - Gradient-based learning of operator weights
> - Nuanced outputs that reflect uncertainty
> - Threshold-dependent decisions

**Model Answer (b) -- 1-2 marks:**

> Using the **Product-Sum** soft AND:
>
> $$\text{HeatingOn} = \text{Cold} \times \text{AtHome} = 0.9 \times 0.4 = 0.36$$
>
> Whether heating activates depends on the **classification threshold**:
> - If threshold is **low** (e.g., $\alpha = 0.3$): HeatingOn = 0.36 > 0.3, so **heating turns ON**
> - If threshold is **high** (e.g., $\alpha = 0.7$): HeatingOn = 0.36 < 0.7, so **heating stays OFF**

**Scoring Notes from the official answer key:**
- (a): 1 mark for natural language, 1 mark for explaining the difference with Boolean (the $\otimes$ operator supports continuous values and gradient learning)
- (b): 1 mark for computing the product correctly, 1 mark for mentioning threshold-dependent activation

---

### === EXAM QUESTION TYPE 2: LNN Bounds with OR (Safety-Critical) ===

This appeared in the **Actual Mid-Semester Test S1 2025 Q2** (3 marks).

---

### Worked Example 2: Autonomous Vehicle Alert (Actual Test 2025 Q2)

**Question:**
An autonomous vehicle uses an LNN to decide whether to trigger a collision alert based on two conditions:
- P: "The object is very close" ($L_P = 0.8, U_P = 0.9$)
- Q: "The object is moving fast" ($L_Q = 0.3, U_Q = 0.6$)

Rule: Alert $\leftarrow$ P $\vee$ Q

Threshold $\alpha = 0.7$.

(a) Is the alert status: definitely true, definitely false, or uncertain? [1 mark]

(b) Why is using bounds (instead of a single probability) beneficial in safety-critical applications? [2 marks]

**Model Answer (a):**

For OR with truth bounds, we compute:

$$L_{\text{Alert}} = \max(L_P, L_Q) = \max(0.8, 0.3) = 0.8$$

$$U_{\text{Alert}} = \max(U_P, U_Q) = \max(0.9, 0.6) = 0.9$$

Now apply the threshold $\alpha = 0.7$:

$$L_{\text{Alert}} = 0.8 \ge 0.7 = \alpha$$

Since the **lower bound is already above** the threshold, the alert is **A. Definitely True**.

> **Why $\max$ for OR bounds?** In three-valued logic, OR only needs one True input to be True. If P's lower bound alone exceeds the threshold, then regardless of Q, the OR result must be at least that high.

**Model Answer (b) -- any two of the following earn full marks:**

1. **Expressing Uncertainty Explicitly**: Bounds allow the system to represent *how confident* it is about a truth value. A single probability of 0.85 hides whether the system is very sure (bounds [0.84, 0.86]) or deeply uncertain (bounds [0.3, 1.0]).

2. **Supporting Conservative Decision-Making**: In safety-critical applications like autonomous driving, the system should err on the side of caution. If the lower bound is below the threshold, the system can choose to slow down or stop rather than take a risky action based on an overconfident point estimate.

3. **Robustness to Noisy or Incomplete Data**: Sensors may fail or provide noisy signals. Bounds propagate this uncertainty from inputs to outputs, letting the system know how unreliable the final decision is.

4. **Better Interpretability**: Engineers and operators can inspect the bounds to understand how certain the model is about its decision. This improves debugging, transparency, and trust in the AI system.

---

### Worked Example 3: Lecture Exercise 5 -- Product-Sum OR

**Given:** Fever (F) = 0.9, Cough (C) = 0.7

**Compute:** $F \vee C$ using Product-Sum

$$F \vee C = F + C - F \times C$$

$$= 0.9 + 0.7 - (0.9 \times 0.7)$$

$$= 1.6 - 0.63$$

$$= 0.97$$

**Answer: A) 0.97**

---

### Worked Example 4: Lecture Exercise 6 -- Nested AND then OR

**Given:** F = 0.9, C = 0.7, SOB = 0.5

**Compute:** $(C \wedge \text{SOB}) \vee F$

**Step 1:** Compute $C \wedge \text{SOB}$ (AND = product):

$$C \wedge \text{SOB} = 0.7 \times 0.5 = 0.35$$

**Step 2:** Compute $(C \wedge \text{SOB}) \vee F$ (OR = A+B-AB):

$$0.35 + 0.9 - (0.35 \times 0.9)$$

$$= 1.25 - 0.315$$

$$= 0.935$$

**Answer: C) 0.935**

---

### Worked Example 5: Lecture Exercise 7 -- Truth Bounds Classification

**Given:** $L = 0.3$, $U = 0.7$, $\alpha = 0.5$

**Analysis:**
- Is $L \ge \alpha$? $0.3 \ge 0.5$? **No.**
- Is $U \le \alpha$? $0.7 \le 0.5$? **No.**
- So $L < \alpha < U$ (0.3 < 0.5 < 0.7)

**Answer: C) The neuron's truth value is uncertain.**

The bounds span both sides of the threshold, so we cannot classify it as definitely true or definitely false.

---

### Worked Example 6: Lecture Exercise 8 -- Three-Valued OR with Mixed Inputs

**Given:**
- Sharp: $L_{\text{sharp}} = 0.2$, $U_{\text{sharp}} = 0.8$
- Heavy: $L_{\text{heavy}} = 0.6$, $U_{\text{heavy}} = 1.0$
- $\alpha = 0.5$
- Rule: Dangerous $\leftarrow$ Sharp $\vee$ Heavy

**Step 1: Classify each input**

Heavy: $L = 0.6 \ge 0.5 = \alpha$ AND $U = 1.0 \ge 0.5 = \alpha$ $\Rightarrow$ **Heavy is TRUE**

Sharp: $L = 0.2 < 0.5 < 0.8 = U$ $\Rightarrow$ **Sharp is UNCERTAIN**

**Step 2: Apply three-valued OR**

From the truth table: $T \vee U = T$

Since Heavy is already TRUE, and OR only needs one True input, the result is:

**Answer: A) The object is definitely dangerous.**

> This is a critical reasoning pattern: in OR, one TRUE input is enough to guarantee TRUE output, regardless of the other input's uncertainty.

---

### Worked Example 7: Lukasiewicz AND (from Slide 40)

**Example 1:** $x_1 = 1$, $x_2 = 0.5$

$$\text{AND}(x_1, x_2) = f\left(1 - \sum_i(1-x_i)\right) = f(1 - (0 + 0.5)) = f(0.5) = 0.5$$

**Example 2:** $x_1 = 0$, $x_2 = 0$

$$\text{AND}(x_1, x_2) = f(1 - (1 + 1)) = f(-1) = \max(0, -1) = 0$$

**Example 3:** Lukasiewicz OR from Slide 41: $x_1 = 1$, $x_2 = 0.5$

$$\text{OR}(x_1, x_2) = f\left(\sum_i x_i\right) = f(1 + 0.5) = f(1.5) = \min(1, 1.5) = 1$$

**Example 4:** Lukasiewicz OR: $x_1 = 0$, $x_2 = 0$

$$\text{OR}(x_1, x_2) = f(0 + 0) = f(0) = 0$$

---

### Worked Example 8: Comparing All Three T-Norms

**Given:** $A = 0.9$, $B = 0.4$

| Operation | Product | Lukasiewicz | Godel |
|-----------|---------|-------------|-------|
| AND($A$,$B$) | $0.9 \times 0.4 = 0.36$ | $\max(0, 0.9+0.4-1) = 0.30$ | $\min(0.9, 0.4) = 0.40$ |
| OR($A$,$B$) | $0.9+0.4-0.36 = 0.94$ | $\min(1, 0.9+0.4) = 1.0$ | $\max(0.9, 0.4) = 0.90$ |
| NOT($A$) | $1-0.9 = 0.10$ | $1-0.9 = 0.10$ | $1-0.9 = 0.10$ |

Observations:
- Product AND gives the **lowest** value (multiplication shrinks things fast)
- Lukasiewicz AND can hit **exactly zero** even when inputs are positive (if $A + B < 1$)
- Godel AND is the **simplest** (just take the minimum) but is not fully smooth

---

## ⚖️ Trade-offs & Comparisons

### Boolean Logic vs Fuzzy Logic vs LNN

| Aspect | Boolean Logic | Fuzzy Logic | LNN |
|--------|-------------|-------------|-----|
| **Truth values** | {0, 1} | [0, 1] | [0, 1] with bounds [L, U] |
| **Operators** | Crisp AND/OR/NOT | min/max/complement | Differentiable t-norms |
| **Learning** | No learning | Manual rule design | **Gradient-based weight learning** |
| **Inference direction** | Forward OR backward | Forward only | **Bidirectional** (both) |
| **Soundness** | Proven sound | No formal guarantees | **Proven logically sound** |
| **Handles uncertainty?** | No | Partially (vagueness) | Yes (bounds quantify uncertainty) |
| **Explainability** | Full (rules visible) | Partial | Full (structure = syntax tree) |
| **Scalability** | Hard to write rules | Hard to write rules | Learns rules from data |
| **Use case** | Theorem proving | Control systems | Neural-symbolic AI |

### Why Not Just Use a Regular Neural Network?

| Aspect | Regular Neural Net | LNN |
|--------|-------------------|-----|
| **Interpretability** | Black box | Every neuron has logical meaning |
| **Structure** | Arbitrary architecture | Architecture follows logical formula |
| **Knowledge** | Learned from data only | Can encode known rules + learn from data |
| **Small data** | Needs lots of data | Works with rules + small data |
| **Consistency** | May produce contradictions | Logical constraints prevent contradictions |
| **Uncertainty** | Single probability output | Bounds [L,U] quantify confidence |

### Product vs Lukasiewicz vs Godel T-Norms

| Aspect | Product | Lukasiewicz | Godel (min/max) |
|--------|---------|-------------|-----------------|
| **Smoothness** | Fully smooth, good gradients | Piecewise linear, has kinks | Not differentiable at min/max points |
| **AND behavior** | Multiplicative (shrinks fast with many inputs) | Additive penalties (can hit zero) | Takes minimum only |
| **Gradient issues** | Can vanish with many small inputs | Flat regions where gradient = 0 | Gradient is 0 for non-minimum inputs |
| **Exam default** | **YES** (used in all exam questions) | Used in LNN paper | Used in classical fuzzy logic |

---

## 🏗️ Design Question Framework

If the exam asks "Design an LNN-based system for [scenario]":

### WHAT
Define propositions and their meanings. Example:
- P: "The road is wet" (truth value from rain sensor)
- Q: "Visibility is low" (truth value from camera)
- Conclusion: SlowDown $\leftarrow$ P $\vee$ Q

### WHY LNN?
- Inputs are uncertain/partial (sensor readings, not binary)
- Need explainability (safety-critical application)
- Want gradient-based learning to tune operator weights
- Bounds [L,U] allow conservative decision-making

### HOW
1. Assign truth values or bounds to input propositions
2. Choose a t-norm (Product-Sum for exam purposes)
3. Build the syntax tree as a computation graph
4. Run bidirectional message passing
5. Read output bounds, apply threshold

### TRADE-OFF
- Product t-norm: smooth but shrinks fast with many inputs
- Higher threshold $\alpha$ = more conservative (fewer false positives, more false negatives)
- Lower threshold $\alpha$ = more aggressive (fewer false negatives, more false positives)
- Bounds give safety guarantees but add computational cost

### EXAMPLE
Plug in specific numbers and compute step-by-step.

---

## 📝 All Exam Questions with Full Model Answers

### --- Sample Test S1 2025, Question 2 [2 marks] ---

**(a)** What does HeatingOn $\leftarrow$ Cold $\otimes$ AtHome represent in natural language, and how is it different from a standard Boolean rule? **[1 mark]**

**Model Answer:**

This rule reads: "If it is cold and someone is at home, then turn on the heating system."

In standard Boolean logic, this would require both inputs to be strictly True (1) to turn on the heating. In an LNN, the $\otimes$ operator allows soft conjunction over continuous truth values. It supports partial inputs (like 0.4 or 0.9), yielding an intermediate activation that reflects uncertainty and permits gradient-based learning.

**(b)** Given Cold = 0.9, AtHome = 0.4, compute HeatingOn and discuss activation. **[1 mark]**

**Model Answer:**

Using soft-logic AND (Product-Sum), HeatingOn = Cold $\times$ AtHome = $0.9 \times 0.4 = 0.36$.

Depending on the classification threshold, the system may or may not trigger the heating. If the threshold is low (e.g., 0.3), heating will be turned on. If it is high (e.g., 0.7), it may stay off.

---

### --- Actual Mid-Semester Test S1 2025, Question 2 [3 marks] ---

**(a)** P: $L_P = 0.8$, $U_P = 0.9$; Q: $L_Q = 0.3$, $U_Q = 0.6$. Alert $\leftarrow$ P $\vee$ Q. With $\alpha = 0.7$, is alert definitely true, definitely false, or uncertain? **[1 mark]**

**Model Answer:**

Lower Bound: $L_{\text{Alert}} = \max(L_P, L_Q) = \max(0.8, 0.3) = 0.8$

Upper Bound: $U_{\text{Alert}} = \max(U_P, U_Q) = \max(0.9, 0.6) = 0.9$

Since $\alpha = 0.7 < 0.8 = L_{\text{Alert}}$, both bounds are above the threshold.

Classification: **A. Definitely true.**

**(b)** Why are bounds beneficial in safety-critical applications? **[2 marks]**

**Model Answer (any two for full marks):**

1. **Expressing Uncertainty Explicitly**: Bounds represent how confident the system is in a truth value, unlike a single probability that hides uncertainty.

2. **Supporting Conservative Decision-Making**: In autonomous driving, if the lower bound is below the threshold, the system can slow down or stop rather than take risky action based on overconfident estimates.

3. **Robustness to Noisy/Incomplete Data**: Sensors may fail or provide noisy signals. Bounds propagate uncertainty from inputs to outputs, tracking how unreliable the final decision is.

4. **Better Interpretability**: Engineers can inspect bounds to understand model certainty, improving debugging, transparency, and trust.

---

### --- Sample Test S1 2026, Question 2 [4 marks] ---

**(a)** What does HeatingOn $\leftarrow$ Cold $\otimes$ AtHome represent in natural language? How is it different from a standard Boolean rule? **[2 marks]**

**Model Answer:**

This rule reads: "If it is cold and someone is at home, then turn on the heating system." [1 mark]

In standard Boolean logic, this would require both inputs to be strictly True (1) to turn on the heating. In an LNN, the $\otimes$ operator allows soft conjunction over continuous truth values. It supports partial inputs (like 0.4 or 0.9), yielding an intermediate activation that reflects uncertainty and permits gradient-based learning. [1 mark]

**(b)** Given Cold = 0.9, AtHome = 0.4, compute HeatingOn. Would the system activate heating? **[2 marks]**

**Model Answer:**

Using soft-logic AND (e.g., Product-Sum), the output HeatingOn will reflect the multiplication of the two values: $0.9 \times 0.4 = 0.36$. [1 mark]

Depending on the classification threshold, the system may or may not trigger the heating. If the threshold is low (e.g., 0.3), heating will be turned on. If it is high (e.g., 0.7), it may stay off. [1 mark]

---

### --- Actual Mid-Semester Test S1 2025, Question 5 [3 marks] ---

**(This tests fuzzy/soft logic, closely related to LNN)**

**Question:** Consider the rule: IF STRONG AND HEAVY THEN HAMMER_THROWER. Contrast traditional logic vs fuzzy logic.

**Model Answer:**

With **classic logic**, both STRONG and HEAVY would be either True or False (by some criteria, like how much they can benchpress, or the athlete's weight in kg). If, and only if, both criteria are true, then the individual is judged suitable for hammer throwing; else, not.

With **Fuzzy Logic**, membership functions map both STRONG and HEAVY to values in [0,1]. Some level of strength maps to $\mu_s$, and some bodyweight maps to $\mu_h$. The AND function might be implemented as $\min(\mu_s, \mu_h)$, or as the product $\mu_s \times \mu_h$. The THEN might have strength 1.0 or something less as a further multiplier. The final result is a suitability score anywhere in [0,1].

---

## 🔄 OR Bounds Computation -- Deep Dive

This is the most likely new question type for the 2026 actual test, since it appeared in the 2025 actual test. Here is a complete reference.

### Computing OR Bounds

For $C \leftarrow A \vee B$ with bounds $A = [L_A, U_A]$ and $B = [L_B, U_B]$:

$$L_C = \max(L_A, L_B)$$
$$U_C = \max(U_A, U_B)$$

**Intuition:** OR only needs ONE input to be true. The lower bound of the OR output is at least as high as the highest lower bound of any input.

### Computing AND Bounds

For $C \leftarrow A \wedge B$ with bounds $A = [L_A, U_A]$ and $B = [L_B, U_B]$:

$$L_C = \max(0, L_A + L_B - 1) \quad \text{(Lukasiewicz)}$$
$$U_C = \min(U_A, U_B) \quad \text{(Godel)}$$

**Intuition:** AND needs ALL inputs to be true. The upper bound of the AND output cannot exceed the smallest upper bound of any input.

### Practice: Multiple OR-Bound Scenarios

| Scenario | $L_A$ | $U_A$ | $L_B$ | $U_B$ | $\alpha$ | $L_{OR}$ | $U_{OR}$ | Classification |
|----------|-------|-------|-------|-------|---------|----------|----------|---------------|
| 1 | 0.8 | 0.9 | 0.3 | 0.6 | 0.7 | 0.8 | 0.9 | **TRUE** |
| 2 | 0.4 | 0.6 | 0.3 | 0.5 | 0.5 | 0.4 | 0.6 | **UNCERTAIN** |
| 3 | 0.1 | 0.3 | 0.2 | 0.4 | 0.5 | 0.2 | 0.4 | **FALSE** |
| 4 | 0.9 | 1.0 | 0.9 | 1.0 | 0.5 | 0.9 | 1.0 | **TRUE** |

---

## 🌐 English Expression Tips

### Key Phrases for LNN Questions

**Explaining what LNN is:**
- "A Logic Neural Network is a neural-symbolic approach where the network structure mirrors a logical syntax tree, with each neuron representing a logical connective."
- "LNN combines the interpretability of symbolic logic with the learning capability of neural networks."

**Explaining the difference from Boolean:**
- "Unlike Boolean logic, which requires inputs to be strictly 0 or 1, LNN operates over continuous truth values in the interval [0, 1]."
- "The $\otimes$ operator is a differentiable soft conjunction that supports partial truth values, enabling gradient-based learning."

**Explaining truth bounds:**
- "Each proposition maintains a lower bound L and upper bound U, expressing the system's confidence interval for that proposition's truth value."
- "Bounds allow the system to distinguish between 'probably true' and 'definitely true,' which is critical in safety-sensitive applications."

**Explaining why bounds matter in safety-critical systems:**
- "In autonomous driving, an overconfident single-point estimate could lead to dangerous decisions; bounds explicitly quantify the system's uncertainty."
- "If the lower bound falls below the decision threshold, the system can choose a conservative action rather than risking an unsafe response."

### Commonly Confused Terms

| Pair | Clarification |
|------|-------------|
| LNN vs Fuzzy Logic | LNN has learnable weights, bidirectional inference, and soundness guarantees. Fuzzy logic is manually designed with no learning. |
| T-norm vs activation function | T-norm generalizes AND to [0,1]; activation function (ReLU, sigmoid) is a general nonlinearity in standard neural nets. |
| "Differentiable" vs "continuous" | Differentiable means we can compute gradients for backpropagation. Continuous just means no jumps. |
| $\otimes$ vs $\times$ | $\otimes$ is the LNN conjunction operator (may include learned weights); $\times$ is plain multiplication. |
| $\oplus$ vs $+$ | $\oplus$ is the LNN disjunction operator; $+$ is plain addition. |
| Vagueness vs Uncertainty | Vagueness = blurry boundaries ("is 12C cold?"). Uncertainty = unknown truth ("will it rain?"). LNN handles both. |
| Product t-norm vs Lukasiewicz | Product = $A \times B$; Lukasiewicz = $\max(0, A+B-1)$. They give different results! |

---

## ✅ Self-Test Checklist

### Computation Skills
- [ ] Can I compute Product-Sum AND for any two values? (e.g., $0.9 \times 0.4 = 0.36$)
- [ ] Can I compute Product-Sum OR for any two values? (e.g., $0.9 + 0.7 - 0.63 = 0.97$)
- [ ] Can I compute nested operations? (e.g., $(C \wedge \text{SOB}) \vee F$)
- [ ] Can I compute Lukasiewicz AND and OR? (e.g., $\max(0, 0.9+0.4-1) = 0.3$)
- [ ] Can I compute OR bounds from two [L,U] pairs? (e.g., $\max(L_P, L_Q)$)
- [ ] Can I classify truth bounds as TRUE/FALSE/UNCERTAIN given $\alpha$?

### Conceptual Understanding
- [ ] Can I explain in 2 sentences why LNN uses differentiable operators instead of Boolean AND?
- [ ] Can I explain the difference between LNN and standard Boolean logic?
- [ ] Can I explain why truth bounds [L,U] are useful in safety-critical applications? (Name at least 2 reasons)
- [ ] Do I know the three-valued logic truth tables for AND and OR?
- [ ] Can I explain upward pass vs downward pass?
- [ ] Can I draw the LNN computation graph for a simple rule?
- [ ] Do I understand the difference between LNN and fuzzy logic? (Name 3 differences)

### Exam Readiness
- [ ] Can I write a full answer for "interpret this LNN rule in natural language"?
- [ ] Can I write a full answer for "compute HeatingOn = Cold $\otimes$ AtHome with values"?
- [ ] Can I write a full answer for "compute OR bounds for autonomous vehicle alert"?
- [ ] Can I write a full answer for "why are bounds useful in safety-critical systems"?
- [ ] Have I memorized the Product-Sum formulas: AND = $A \times B$, OR = $A + B - AB$, NOT = $1 - A$?

---

## 🎯 Exam Strategy -- Quick Reference Card

### If the question asks "What does this LNN rule mean in natural language?":
1. Translate the formula into an English sentence
2. State that Boolean requires strictly True/False inputs
3. State that LNN's $\otimes$ operator uses differentiable soft conjunction over [0,1]
4. Mention that this enables gradient-based learning and handles uncertainty

### If the question asks "Compute the truth value":
1. Identify which t-norm to use (Product-Sum unless stated otherwise)
2. Show the formula: AND = $A \times B$ or OR = $A + B - AB$
3. Plug in numbers and compute step by step
4. Discuss how the threshold determines the final decision

### If the question asks about truth bounds:
1. State the bounds for each input
2. Compute the output bounds using the appropriate rule (max for OR, min for AND upper)
3. Compare with threshold $\alpha$
4. Classify as TRUE ($L \ge \alpha$), FALSE ($U \le \alpha$), or UNCERTAIN ($L < \alpha < U$)

### If the question asks "Why are bounds useful in safety-critical applications?":
Pick two from: (1) express uncertainty explicitly, (2) support conservative decisions, (3) robust to noisy sensors, (4) better interpretability for engineers
