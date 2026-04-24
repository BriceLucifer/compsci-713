# Logic Neural Networks (LNN)

## Exam Priority

**Must-know** | Appeared in **every single past test** (4/4) | Typically worth 2--4 marks

LNN is one of the most reliably examined topics in COMPSCI 713. The lecturer has asked about it in the 2025 Sample, 2025 Real, 2026 Sample tests, and the format is predictable. If you learn this chapter well, these are among the easiest marks on the paper.

---

## Part 1: Why Does LNN Even Exist?

Before we touch any formulas, let us understand the *problem* that LNN was invented to solve. This is the kind of thinking the lecturer rewards -- showing you understand the motivation, not just the mechanics.

### The Two Worlds That Could Not Talk to Each Other

Imagine two colleagues at a company. One is a brilliant detective (that is classical logic). The other is a talented artist who works by intuition (that is a neural network). They are both useful, but they cannot collaborate.

**The Detective (Classical Logic)** is rigorous and transparent. Given a set of rules, the detective can tell you *exactly* why a conclusion follows. "The suspect was at the scene AND had the weapon, THEREFORE the suspect is guilty." Every step is auditable. A judge can inspect the reasoning and trust it.

But the detective has a fatal flaw: everything must be perfectly black-and-white. The suspect was *either* at the scene or not. The weapon was *either* found or not. There is no room for "the witness is 90% sure she saw the suspect" or "the weapon was partially matching." If the evidence is ambiguous, the detective is paralysed.

**The Artist (Neural Network)** thrives on ambiguity. Feed a neural network a blurry photo, and it will tell you "I am 87% confident this is a cat." It learns patterns from data, handles noise gracefully, and can process messy real-world inputs. But ask the artist *why* it thinks it is a cat, and you get a shrug. The reasoning is locked inside millions of learned weights -- a black box.

**LNN is what happens when the detective and the artist learn to work together.** It keeps the detective's logical structure (rules you can read and inspect) but gives those rules the artist's ability to work with partial, uncertain information and to learn from data.

### Why This Matters for Exam Answers

The lecturer's exam questions consistently test whether you understand this gap. When a question asks "how is LNN different from standard Boolean logic?" -- the answer is rooted in this section. When a question asks about benefits of bounds in safety-critical applications -- the answer connects to why the detective alone is not enough.

> **Common Misconception:** Students often describe LNN as "just fuzzy logic." While LNN shares the idea of continuous truth values with fuzzy logic, LNN is specifically designed to be *differentiable* so it can be trained with gradient descent like a neural network. Fuzzy logic systems typically have fixed rules set by human experts. LNN *learns* its rules and parameters from data.

---

## Part 2: From Boolean AND to Soft AND -- The Heart of LNN

This is the single most tested concept. Let us build it from the ground up.

### Step 1: Remember What Boolean AND Does

You already know Boolean AND from programming. Here is the truth table:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Both inputs must be exactly 1 for the output to be 1. Simple. Clean. But real sensors do not give you clean 0s and 1s.

### Step 2: The Problem With Real-World Inputs

Now imagine a smart home system. You have a temperature sensor and an occupancy sensor. The temperature sensor says: "Cold = 0.9" (it is pretty cold -- not absolutely freezing, but quite cold). The occupancy sensor says: "AtHome = 0.4" (maybe someone is home? The motion detector triggered briefly, but it is not certain).

Your rule is: **"If it is cold AND someone is at home, turn on the heating."**

With Boolean logic, you have to pick a threshold and round:
- Is 0.9 "True"? Probably yes (above 0.5).
- Is 0.4 "True"? Hmm... below 0.5, so "False"?

So Boolean AND says: 1 AND 0 = 0. No heating. But that feels wrong -- it *is* cold, and there *might* be someone home. Maybe the heating should come on at a low level, not full blast but not completely off either.

This is the fundamental problem: **Boolean logic throws away the nuance in your sensor readings.**

### Step 3: Enter the Soft AND Operator

LNN replaces the strict Boolean AND with a **soft AND**, written as \\(\otimes\\) (the tensor product symbol). Instead of requiring both inputs to be exactly 1, the soft AND takes continuous values in [0, 1] and produces a continuous output in [0, 1].

The rule becomes:

\\[
\text{HeatingOn} \leftarrow \text{Cold} \otimes \text{AtHome}
\\]

But how exactly do you combine 0.9 and 0.4 into a single number? That is where **t-norms** come in.

### Step 4: Three Ways to Compute Soft AND (T-Norms)

A t-norm is simply a mathematical function that generalises Boolean AND to continuous values. There are three you need to know for the exam. Let us compute all three with Cold = 0.9 and AtHome = 0.4:

#### Product T-Norm: Multiply Them

\\[
A \otimes B = A \times B
\\]

\\[
0.9 \times 0.4 = 0.36
\\]

**Intuition:** Think of this as "the probability that both happen if they are independent." If you are 90% sure it is cold and 40% sure someone is home, and these are independent, then you are 36% sure both are true simultaneously. The product t-norm is the most commonly used in LNN exam questions.

#### Lukasiewicz T-Norm: Add Then Subtract

\\[
A \otimes B = \max(0,\; A + B - 1)
\\]

\\[
\max(0,\; 0.9 + 0.4 - 1) = \max(0,\; 0.3) = 0.3
\\]

**Intuition:** This is the most "pessimistic" of the three (well, almost). It says: "How much *overlap* is there in the truth of A and B?" If A = 0.9 covers 90% of the truth space and B = 0.4 covers 40%, their overlap is at most 30%. If the values are low enough that they do not overlap at all, you get 0.

#### Godel (Min) T-Norm: Take the Weakest Link

\\[
A \otimes B = \min(A, B)
\\]

\\[
\min(0.9, 0.4) = 0.4
\\]

**Intuition:** A chain is only as strong as its weakest link. The AND is only as true as the least-true input. This is the most "generous" t-norm -- it gives the highest result.

### Comparison Table: All Three at a Glance

| T-Norm | Formula | Cold=0.9, AtHome=0.4 | Character |
|--------|---------|---------------------|-----------|
| Product | \\(A \times B\\) | **0.36** | Moderate -- penalises both low inputs |
| Lukasiewicz | \\(\max(0, A+B-1)\\) | **0.30** | Pessimistic -- requires significant overlap |
| Godel (min) | \\(\min(A, B)\\) | **0.40** | Generous -- only as bad as the weakest |

All three agree on Boolean inputs (when A, B are exactly 0 or 1, they produce the same result as classical AND). They diverge when inputs are partial -- and that divergence is precisely what the lecturer likes to test.

> **Exam Tip:** The 2025 and 2026 sample tests both use the **product t-norm** for computation questions. Unless the question specifies otherwise, use product. But always *state which t-norm you are using* in your answer.

### Step 5: Does the Heating Turn On?

We computed HeatingOn = 0.36 (product t-norm). But 0.36 is just a number -- we need a decision. This is where the **threshold** comes in.

- If the activation threshold is 0.5: HeatingOn = 0.36 < 0.5, so **heating stays OFF**.
- If the activation threshold is 0.3: HeatingOn = 0.36 > 0.3, so **heating turns ON**.

The threshold is a design choice. In a safety-critical system, you might set it low (better to heat an empty house than freeze a person). In an energy-saving system, you might set it high.

**Core Intuition:** LNN replaces the hard yes/no of Boolean logic with a sliding scale, letting the system make *graded* decisions that reflect the confidence of its inputs.

---

## Part 2B: Product-Sum Soft Logic Operators (W2L2, slide 25)

The t-norms above (Product, Lukasiewicz, Godel) are one family of soft operators. The lecture also introduces a **different** set called **Product-Sum** operators. You need to know both -- the exam may use either.

### Product-Sum Operator Definitions

| Operation | Boolean | Product-Sum Soft Version |
|-----------|---------|--------------------------|
| AND | A ∧ B | \\(A \times B\\) (same as product t-norm) |
| OR | A ∨ B | \\(A + B - A \times B\\) |
| NOT | ¬A | \\(1 - A\\) |

> **Key difference:** The Product-Sum OR is **not** the same as the Godel (max) OR. Product-Sum OR uses \\(A + B - A \times B\\), which accounts for overlap. Think of it like the probability union formula \\(P(A \cup B) = P(A) + P(B) - P(A \cap B)\\) -- but applied to truth values, not probabilities.

### Worked Example: Exercise 5 (slide 25)

**Question:** F = 0.9, C = 0.7. Compute \\(F \lor C\\) using Product-Sum.

**Solution:**

\\[
F \lor C = F + C - F \times C = 0.9 + 0.7 - (0.9 \times 0.7) = 1.6 - 0.63 = 0.97
\\]

**Answer: A (0.97)**

Notice how this is different from the Godel OR: \\(\max(0.9, 0.7) = 0.9\\). The Product-Sum OR gives a **higher** result (0.97 vs 0.9) because it "boosts" the output when both inputs contribute some truth.

### Worked Example: Exercise 6 (slide 25)

**Question:** Compute \\((C \land SOB) \lor F\\) where C = 0.7, SOB = 0.5, F = 0.9 using Product-Sum.

**Solution (step by step):**

Step 1 -- Compute the AND first:
\\[
C \land SOB = C \times SOB = 0.7 \times 0.5 = 0.35
\\]

Step 2 -- Now compute the OR with F:
\\[
0.35 \lor F = 0.35 + 0.9 - (0.35 \times 0.9) = 1.25 - 0.315 = 0.935
\\]

**Answer: C (0.935)**

> **Exam Tip:** When a question says "Product-Sum" or uses the formula \\(A + B - AB\\) for OR, use these operators. When a question says "t-norm" or uses min/max, use the Godel family. Always check which operator family the question specifies.

---

## Part 2C: LNN Architecture -- The Syntax Tree as a Neural Network (W2L2, slides 30--33)

This section explains *how* an LNN is actually structured as a network. It is not just a collection of formulas -- it is a neural network whose architecture mirrors the logical structure.

### The Core Idea: One Neuron Per Logical Node

In a standard neural network, the architecture (number of layers, connections) is a design choice. In an LNN, **the architecture is determined by the logical formula itself**.

Every logical formula can be written as a **syntax tree** -- a tree where:
- **Leaf nodes** are the input propositions (e.g., Whiskers, Tail, Laser pointer)
- **Internal nodes** are logical connectives (AND, OR, IMPLIES)
- **The root** is the final conclusion

In an LNN, each node of this syntax tree becomes a **neuron**. Different connectives use different activation functions:
- AND nodes use a t-norm activation (e.g., product)
- OR nodes use a t-conorm activation (e.g., sum-product)
- IMPLIES nodes use an implication activation

### Example From Lecture (slides 31--32)

Consider these two rules:

- **Rule 1:** Whiskers \\(\otimes\\) Tail \\(\otimes\\) (Laser\_pointer \\(\rightarrow\\) Chases) \\(\rightarrow\\) Cat
- **Rule 2:** Cat \\(\oplus\\) Dog \\(\rightarrow\\) Pet

Where \\(\otimes\\) = AND (multiplication), \\(\oplus\\) = OR (addition), \\(\rightarrow\\) = implication.

The syntax tree (and therefore the network) looks like:

```
                        Pet
                         |
                    [OR / ⊕]
                   /         \
                Cat           Dog
                 |
          [IMPLIES →]
         /           \
    [AND / ⊗]        Cat
    /    |    \
Whiskers Tail [IMPLIES →]
              /          \
        Laser_pointer   Chases
```

Each box is a neuron. The leaf nodes (Whiskers, Tail, Laser\_pointer, Chases, Dog) receive input truth values. The internal nodes compute their logical operations and pass results upward.

### Bidirectional Message Passing

This is what makes LNN special compared to a standard feedforward network. Messages flow in **both directions**:

1. **Upward Pass (bottom-up):** Starting from the leaf nodes, truth values propagate upward through the tree. Each node computes its output from its children's values. This is like *evaluating* the logical expression -- "given these inputs, what is the conclusion?"

2. **Downward Pass (top-down):** Starting from higher-level conclusions, constraints propagate *downward*. If we know the conclusion should be TRUE, the downward pass tightens the bounds on the inputs to ensure logical consistency. This is like *inference* -- "given this conclusion, what must be true about the inputs?"

3. **Iterate Until Convergence:** The upward and downward passes alternate until the bounds stabilise. This ensures global logical consistency across all rules simultaneously.

> **Why this matters:** Bidirectional inference is what allows LNN to do things standard neural networks cannot -- like deducing that if "Pet is TRUE" and "Dog is FALSE," then "Cat must be TRUE" (by the downward pass through Rule 2). A standard feedforward network can only compute in one direction.

> **Common Misconception:** Students sometimes think LNN is just a neural network with logical loss functions. It is more than that -- the *architecture itself* encodes the logical structure, and the bidirectional message passing enforces logical consistency in a way that standard backpropagation does not.

---

## Part 2D: Łukasiewicz-like Logic Formulas (W2L2, slides 40--41)

The lecture presents a specific set of formulas that LNN uses internally, based on **Łukasiewicz logic** with a clamping function.

### The Basis Activation Function

All LNN operations are wrapped in a clamping function:

\\[
f(x) = \max(0, \min(1, x))
\\]

This ensures outputs always stay in [0, 1]. If the raw computation gives something negative, it clamps to 0. If it gives something above 1, it clamps to 1.

### Logical AND (Łukasiewicz-style)

\\[
\bigwedge x_i = f\left(1 - \sum(1 - x_i)\right)
\\]

**How to read this:** For each input, compute "how far from 1 it is" (that is \\(1 - x_i\\)). Sum those gaps. Subtract from 1. Clamp.

**Example 1:** \\(x_1 = 1, x_2 = 0.5\\)
\\[
\bigwedge = f(1 - (1-1) - (1-0.5)) = f(1 - 0 - 0.5) = f(0.5) = 0.5
\\]

**Example 2:** \\(x_1 = 0, x_2 = 0\\)
\\[
\bigwedge = f(1 - (1-0) - (1-0)) = f(1 - 1 - 1) = f(-1) = 0
\\]

The clamping function catches the negative value and floors it to 0.

### Logical OR (Łukasiewicz-style)

\\[
\bigvee x_i = f\left(\sum x_i\right)
\\]

**Example 1:** \\(x_1 = 1, x_2 = 0.5\\)
\\[
\bigvee = f(1 + 0.5) = f(1.5) = 1
\\]

The clamping function catches the value above 1 and caps it to 1.

**Example 2:** \\(x_1 = 0, x_2 = 0\\)
\\[
\bigvee = f(0 + 0) = f(0) = 0
\\]

> **Exam Tip:** Notice that the Łukasiewicz AND formula \\(f(1 - \sum(1 - x_i))\\) for two inputs simplifies to \\(\max(0, x_1 + x_2 - 1)\\), which is exactly the Lukasiewicz t-norm from Part 2. The formula here is just the generalised version for any number of inputs.

---

## Part 3: Truth Value Bounds [L, U] -- Reasoning Under Uncertainty

This section covers the most *advanced* LNN concept tested in COMPSCI 713. It appeared in the 2025 real test for 3 marks. Understanding it deeply will set you apart.

### The Analogy: A Thermometer With a Range

Imagine you have a cheap thermometer. It does not tell you "the temperature is exactly 30.0 degrees." Instead, it tells you "the temperature is somewhere between 28 and 32 degrees." That range [28, 32] is its **bound**.

In LNN, every proposition has a truth value that is not a single number but a **range** [L, U]:
- **L (lower bound):** At minimum, the proposition is *this* true. Even in the worst-case interpretation of the evidence, the truth is at least L.
- **U (upper bound):** At most, the proposition is *this* true. Even in the best-case interpretation, the truth is no more than U.

### What Do the Bounds Tell You?

**Narrow bounds = high confidence.** If a proposition has bounds [0.85, 0.90], you are quite sure its truth is around 0.87 or so. The system is confident.

**Wide bounds = high uncertainty.** If a proposition has bounds [0.2, 0.8], the system is saying "I really do not know -- the truth could be anywhere from slightly true to quite true." This is valuable information! A single-point estimate like 0.5 would hide this uncertainty.

### Classifying With a Threshold

Given a threshold \\(\alpha\\), you classify a proposition based on where its bounds sit relative to \\(\alpha\\):

```
             0                    alpha                   1
             |----------------------|---------------------|
                                   
Case 1:  [=====L==========U====]
                              ^--- both above alpha
         L >= alpha  -->  DEFINITELY TRUE

Case 2:             [===L==========U===]
                    ^--- both below alpha  
         U < alpha  -->  DEFINITELY FALSE

Case 3:       [===L========|==========U===]
                           ^alpha in the middle
         L < alpha <= U  -->  UNCERTAIN
```

More precisely:

| Condition | Classification |
|---|---|
| \\(L \geq \alpha\\) | **Definitely true** -- even the worst case clears the bar |
| \\(U < \alpha\\) | **Definitely false** -- even the best case falls short |
| \\(L < \alpha \leq U\\) | **Uncertain** -- could go either way |

### Complete Bounds Interpretation Table (W2L2, slide 34)

The full set of cases, including the edge case of contradiction:

| L | U | Meaning |
|---|---|---|
| 0.0 | 1.0 | **Uncertain:** no information at all -- truth could be anything |
| \\(L \leq \alpha\\) | \\(U \leq \alpha\\) | **False:** both bounds below threshold |
| \\(L \geq \alpha\\) | \\(U \geq \alpha\\) | **True:** both bounds above threshold |
| \\(L > U\\) | — | **Contradiction:** inconsistent logic (should not happen in a well-formed system) |

The contradiction case is important conceptually: if during bidirectional inference the bounds cross (lower exceeds upper), it signals that the rules in the system are logically inconsistent.

### Three-Valued Logic Table (W2L2, slide 35)

Before we get to continuous bounds, it helps to understand the **three-valued** logic that sits between Boolean (two values) and full continuous LNN. Here, each proposition can be **True (T)**, **False (F)**, or **Uncertain (U)**.

| A | B | A ∧ B | A ∨ B |
|---|---|-------|-------|
| T | T | T | T |
| T | U | U | T |
| T | F | F | T |
| U | U | U | U |
| U | F | F | U |
| F | F | F | F |

**Key observations to memorise:**

- **AND rule of thumb:** If *either* input is False → result is False. If *both* are True → True. If one is Uncertain and the other is not False → stays Uncertain.
- **OR rule of thumb:** If *either* input is True → result is True. If *both* are False → False. If one is Uncertain and the other is not True → stays Uncertain.

Think of Uncertain as a "weak" value: AND cannot promote it (only False dominates it), and OR cannot demote it (only True dominates it).

> **Why this matters for the exam:** The three-valued table is the conceptual foundation for bounds-based classification. When you have bounds [L, U] that span the threshold \\(\alpha\\), you are essentially in the "Uncertain" row of this table. Understanding how AND and OR interact with Uncertain values helps you quickly reason about compound formulas without doing full bound arithmetic.

### Worked Example: Exercise 7 (W2L2, slides 36--37)

**Question:** Given L = 0.3, U = 0.7, threshold \\(\alpha = 0.5\\). Classify the proposition.

**Solution:**

- \\(L = 0.3 < \alpha = 0.5\\) → not definitely true
- \\(U = 0.7 > \alpha = 0.5\\) → not definitely false
- Therefore: \\(L < \alpha \leq U\\)

**Answer: C (Uncertain)** -- the bounds span both sides of the threshold. We cannot determine truth or falsity from the available information.

### Worked Example: Exercise 8 (W2L2, slides 38--39)

**Question:** Given:
- Sharp = [0.2, 0.8]
- Heavy = [0.6, 1.0]
- Threshold \\(\alpha = 0.5\\)
- Rule: Dangerous \\(\leftarrow\\) Sharp \\(\lor\\) Heavy

Classify Dangerous.

**Solution (using three-valued reasoning):**

Step 1 -- Classify each input individually:
- **Heavy:** \\(L = 0.6 \geq \alpha = 0.5\\) → Heavy is **TRUE**
- **Sharp:** \\(L = 0.2 < \alpha = 0.5\\), \\(U = 0.8 > \alpha = 0.5\\) → Sharp is **UNCERTAIN**

Step 2 -- Apply the three-valued OR table:
- TRUE ∨ UNCERTAIN = **TRUE** (from the table above: if either input is True, OR is True)

**Answer: A (Definitely True)**

The key insight: because Dangerous uses OR, and Heavy is already TRUE on its own, it does not matter that Sharp is uncertain. One true input is enough for OR. If the rule had been AND instead, the uncertainty in Sharp would have made the result UNCERTAIN.

> **Exam Tip:** This exercise tests whether you can shortcut the computation using three-valued logic. You do not need to compute full bound arithmetic here -- just classify each input, look up the three-valued table, and read off the answer. This saves time under exam pressure.

---

### Why This Matters: The Self-Driving Car Example

This is the exact scenario from the 2025 real test. An autonomous vehicle has two sensors:
- P: "The object is very close" with bounds [0.8, 0.9]
- Q: "The object is moving fast" with bounds [0.3, 0.6]

The vehicle should trigger a collision alert if P OR Q is true (either condition is dangerous). The threshold is \\(\alpha = 0.7\\).

If we only had single-point estimates (say P = 0.85, Q = 0.45), we might compute OR and get a single number. But with bounds, we can determine whether the conclusion is *guaranteed* to be true even in the worst case -- which is exactly what you want before slamming the brakes at highway speed.

---

## Part 4: Computing Bounds for OR and AND

### OR Bounds: \\(P \lor Q\\)

\\[
L_{P \lor Q} = \max(L_P,\; L_Q)
\\]
\\[
U_{P \lor Q} = \max(U_P,\; U_Q)
\\]

**Intuition:** OR is satisfied if *either* input is true. So:
- The lower bound of OR = the best (highest) lower bound among the inputs. If at least one input is guaranteed to be at least 0.8, then the OR is guaranteed to be at least 0.8.
- The upper bound of OR = the best (highest) upper bound among the inputs. The OR could be as high as the most optimistic individual input.

**Worked example (2025 real test):**

Given:
- P = [0.8, 0.9]
- Q = [0.3, 0.6]

\\[
L_{\text{Alert}} = \max(0.8,\; 0.3) = 0.8
\\]
\\[
U_{\text{Alert}} = \max(0.9,\; 0.6) = 0.9
\\]

Alert has bounds **[0.8, 0.9]**.

Classification with \\(\alpha = 0.7\\):
- \\(L = 0.8 \geq 0.7 = \alpha\\)
- Therefore: **Definitely true**

The alert should trigger. Even in the worst-case interpretation of the sensor data, the danger level exceeds our threshold.

### AND Bounds (Lukasiewicz): \\(P \land Q\\)

\\[
L_{P \land Q} = \max(0,\; L_P + L_Q - 1)
\\]
\\[
U_{P \land Q} = \min(U_P,\; U_Q)
\\]

**Intuition:** AND requires *both* inputs to be true. So:
- The lower bound uses the Lukasiewicz formula -- the overlap. Both inputs need to contribute, and the overlap shrinks as either input gets less certain.
- The upper bound is the *minimum* of the individual upper bounds. AND can never be more true than its weakest input (in the best case).

**Worked example:**

Given P = [0.8, 0.9], Q = [0.3, 0.6]:

\\[
L_{P \land Q} = \max(0,\; 0.8 + 0.3 - 1) = \max(0,\; 0.1) = 0.1
\\]
\\[
U_{P \land Q} = \min(0.9,\; 0.6) = 0.6
\\]

Result: [0.1, 0.6]. With \\(\alpha = 0.7\\), since \\(U = 0.6 < 0.7\\), this is **definitely false**.

Notice the contrast: OR gave [0.8, 0.9] (definitely true), AND gave [0.1, 0.6] (definitely false). Makes sense -- the "object is moving fast" input is too uncertain to pass AND, but the "object is close" input is strong enough to trigger OR alone.

> **Warning:** A very common mistake is using \\(\min\\) for the upper bound of OR. The upper bound of OR uses **max**, not min. Think about it: if one input could be as high as 0.9, then the OR could also be as high as 0.9 -- you take the best case, not the worst.

---

## Part 5: Every Past Paper LNN Question -- Fully Worked

### 2026 Sample Test, Question 2 [4 marks]

This is the *highest-value* LNN question across all tests. Let us nail every mark.

**The setup:**

> A smart home system uses an LNN with the rule:
> HeatingOn \\(\leftarrow\\) Cold \\(\otimes\\) AtHome
>
> (a) What does this rule represent in natural language, and how is it different from a standard Boolean rule? [2 marks]
>
> (b) Cold = 0.9, AtHome = 0.4. Compute HeatingOn. Should heating activate? [2 marks]

**Model answer for (a) -- targeting 2 marks:**

"If it is cold and someone is at home, then turn on the heating system." [1 mark for correct natural-language reading]

In standard Boolean logic, both Cold and AtHome must be strictly True (1) or False (0), and AND requires both to be exactly 1 for HeatingOn to be True. In an LNN, the \\(\otimes\\) operator is a soft conjunction that operates over continuous truth values in [0, 1]. It accepts partial inputs such as 0.9 or 0.4, producing an intermediate activation that reflects the degree of confidence. This makes the logic differentiable and suitable for gradient-based learning. [1 mark for explaining continuous values / differentiability vs. strict binary]

**Mark allocation:**
- 1 mark: correct natural-language reading of the rule
- 1 mark: explaining that LNN uses continuous [0,1] values and/or is differentiable, versus Boolean's strict {0, 1}

**Model answer for (b) -- targeting 2 marks:**

Using the product t-norm for the soft AND:

\\[
\text{HeatingOn} = \text{Cold} \times \text{AtHome} = 0.9 \times 0.4 = 0.36
\\]

[1 mark for correct computation]

Whether the heating activates depends on the classification threshold. Since 0.36 is relatively low, it would not activate at a typical threshold (e.g., 0.5 or 0.7). If the threshold were set lower (e.g., 0.3), the heating would activate. The low value reflects that while it is quite cold (0.9), there is low confidence that someone is at home (0.4), and the product t-norm penalises this weak input. [1 mark for discussing threshold and activation decision]

**Mark allocation:**
- 1 mark: correct numerical computation (0.36)
- 1 mark: discussing whether the system activates based on threshold

---

### 2025 Sample Test, Question 2 [2 marks]

Same scenario as above but with **fewer marks**, so shorter answers are expected.

**The setup:**

> (a) Natural language + Boolean difference. [1 mark]
> (b) Cold = 0.9, AtHome = 0.4. Qualitative answer OK. [1 mark]

**Model answer for (a) -- targeting 1 mark:**

"If it is cold and someone is at home, then turn on the heating." In Boolean logic, both must be strictly 1; in LNN, the \\(\otimes\\) operator works over continuous values in [0, 1], allowing partial truth.

**Model answer for (b) -- targeting 1 mark:**

Using soft-AND (e.g., product t-norm), HeatingOn \\(\approx\\) 0.9 \\(\times\\) 0.4 = 0.36. This is relatively low, so the system likely would not activate the heating unless the threshold is set very low.

> **Exam Strategy:** Notice the 2025 sample awards 1 mark for part (b) and says "qualitative OK." This means you do not strictly need to compute 0.36 -- you could say "the result would be low because the AND operator is dragged down by the weak AtHome input." But computing the number takes 5 seconds and makes your answer stronger. Always compute if you can.

---

### 2025 Real Test, Question 2 [3 marks]

This is the bounds question. The highest-difficulty LNN question seen so far.

**The setup:**

> An autonomous vehicle uses an LNN to decide whether to trigger a collision alert.
> - P: "The object is very close" (\\(L_P = 0.8, U_P = 0.9\\))
> - Q: "The object is moving fast" (\\(L_Q = 0.3, U_Q = 0.6\\))
>
> Alert \\(\leftarrow\\) P \\(\lor\\) Q, threshold \\(\alpha = 0.7\\)
>
> (a) Is the alert status: A. definitely true, B. definitely false, C. uncertain? [1 mark]
> (b) Why is using bounds beneficial in safety-critical applications? [2 marks]

**Model answer for (a) -- targeting 1 mark:**

Using OR bound rules:
- \\(L_{\text{Alert}} = \max(L_P, L_Q) = \max(0.8, 0.3) = 0.8\\)
- \\(U_{\text{Alert}} = \max(U_P, U_Q) = \max(0.9, 0.6) = 0.9\\)

Since \\(L_{\text{Alert}} = 0.8 \geq \alpha = 0.7\\), the classification is: **A. Definitely true**.

> **Exam Tip:** Even though the question says "no proof required," showing the computation takes 10 seconds and protects you if you circle the wrong letter by accident. The marker can still see you understood the method.

**Model answer for (b) -- targeting 2 marks:**

Any two of these four points earn full marks (from the 2025 marking rubric):

1. **Expressing uncertainty explicitly.** Bounds directly represent the confidence level. A single probability of 0.85 hides the fact that the truth could be anywhere from 0.8 to 0.9 -- which is very different from 0.5 to 1.0 (same average but much more uncertain).

2. **Supporting conservative decision-making.** In safety-critical domains like autonomous driving, the system can treat the "uncertain" zone as a reason to act cautiously. If the lower bound is below the threshold, the vehicle might slow down and gather more sensor data rather than take irreversible action.

3. **Robustness to noisy or incomplete data.** Sensors may fail or provide noisy readings. Bounds propagate this uncertainty through the logical reasoning chain, so the system knows *how uncertain* its final decision is, rather than presenting a false sense of precision.

4. **Better interpretability.** Engineers and operators can inspect the bounds to understand how certain the model is about each conclusion. A decision with bounds [0.85, 0.90] is far more trustworthy than one with bounds [0.3, 0.9], and the system can flag the latter for human review.

---

## Part 6: Practice Problems With Full Solutions

### Problem 1: Lukasiewicz T-Norm Computation

**Question:** A fire alarm system uses the rule: Alarm \\(\leftarrow\\) Smoke \\(\otimes\\) Heat. Given Smoke = 0.7 and Heat = 0.6, compute the Alarm activation using the Lukasiewicz t-norm. Should the alarm sound if the threshold is 0.5?

**Solution:**

\\[
\text{Alarm} = \max(0,\; 0.7 + 0.6 - 1) = \max(0,\; 0.3) = 0.3
\\]

Since 0.3 < 0.5, the alarm does **not** sound.

Notice: with the product t-norm, we would get 0.7 \\(\times\\) 0.6 = 0.42, still below 0.5. With the Godel t-norm, we would get min(0.7, 0.6) = 0.6, which *would* trigger the alarm. The choice of t-norm matters!

---

### Problem 2: OR Bounds With Classification

**Question:** A hospital monitoring system uses: CriticalAlert \\(\leftarrow\\) HighFever \\(\lor\\) LowOxygen. Given:
- HighFever = [0.6, 0.8]
- LowOxygen = [0.5, 0.7]

Classify the alert with threshold \\(\alpha = 0.65\\).

**Solution:**

\\[
L_{\text{Alert}} = \max(0.6, 0.5) = 0.6
\\]
\\[
U_{\text{Alert}} = \max(0.8, 0.7) = 0.8
\\]

Bounds: [0.6, 0.8].

Since \\(L = 0.6 < \alpha = 0.65 \leq U = 0.8\\), the classification is: **C. Uncertain**.

The system cannot confidently say the patient is critical, but it cannot rule it out either. In a hospital, this would trigger a "monitor closely" status rather than a full emergency or an all-clear.

---

### Problem 3: Natural Language Interpretation

**Question:** Given the LNN rule: Irrigate \\(\leftarrow\\) DrySoil \\(\otimes\\) CropGrowing, explain in natural language what this rule means and how it differs from a standard Boolean rule.

**Solution:**

"If the soil is dry and a crop is currently growing, then the irrigation system should activate."

In Boolean logic, both DrySoil and CropGrowing must be strictly True (1) for irrigation to occur. In LNN, the \\(\otimes\\) operator allows continuous truth values. For example, if DrySoil = 0.7 (moderately dry) and CropGrowing = 0.9 (crop is almost certainly growing), the product t-norm gives 0.63 -- moderate confidence that irrigation is needed. This continuous output enables proportional responses (e.g., watering at 63% capacity rather than full blast or nothing).

---

### Problem 4: AND Bounds With Lukasiewicz

**Question:** Given P = [0.7, 0.9] and Q = [0.5, 0.8], compute the bounds for R \\(\leftarrow\\) P \\(\land\\) Q using Lukasiewicz AND bounds. Classify with \\(\alpha = 0.5\\).

**Solution:**

\\[
L_R = \max(0,\; L_P + L_Q - 1) = \max(0,\; 0.7 + 0.5 - 1) = \max(0,\; 0.2) = 0.2
\\]
\\[
U_R = \min(U_P,\; U_Q) = \min(0.9,\; 0.8) = 0.8
\\]

Bounds: [0.2, 0.8].

Since \\(L = 0.2 < \alpha = 0.5 \leq U = 0.8\\), the classification is: **Uncertain**.

---

### Problem 5: Why Not Just a Single Probability?

**Question:** "An LNN system reports that a proposition has bounds [0.4, 0.9]. A simpler system reports the same proposition with a single probability of 0.65. Why is the LNN representation more useful?"

**Solution:**

The single probability of 0.65 suggests moderate confidence, but it hides crucial information about how *uncertain* that estimate is. The bounds [0.4, 0.9] reveal that the truth could be anywhere from "probably false" (0.4) to "very likely true" (0.9) -- a massive range.

In practice, a decision-maker would treat these very differently:
- A proposition with bounds [0.6, 0.7] and average 0.65 is fairly reliable -- act on it.
- A proposition with bounds [0.4, 0.9] and average 0.65 is highly uncertain -- gather more evidence before acting.

A single probability collapses these two very different situations into the same number.

---

### Problem 6: Compare All Three T-Norms

**Question:** Given A = 0.8 and B = 0.5, compute the soft AND using all three t-norms and rank the results.

**Solution:**

| T-Norm | Computation | Result |
|--------|-------------|--------|
| Product | 0.8 \\(\times\\) 0.5 | **0.40** |
| Lukasiewicz | \\(\max(0, 0.8 + 0.5 - 1) = \max(0, 0.3)\\) | **0.30** |
| Godel (min) | \\(\min(0.8, 0.5)\\) | **0.50** |

Ranking from highest to lowest: Godel (0.50) > Product (0.40) > Lukasiewicz (0.30).

This ordering is always the same: **Godel \\(\geq\\) Product \\(\geq\\) Lukasiewicz** for any inputs in [0, 1]. Godel is the most generous (only limited by the weakest input), Lukasiewicz is the most demanding (requires significant overlap).

> **Exam Tip:** This ordering relationship is useful to remember. If a question gives you a result and asks which t-norm could have produced it, the ordering helps you narrow it down.

---

## Part 7: How to Write the Perfect Exam Answer

The lecturer emphasises "quality over quantity" and "concise and clear." Here is exactly what to write for each mark level.

### 1-Mark LNN Question (Qualitative)

**Example:** "Explain how the LNN computes HeatingOn given Cold = 0.9 and AtHome = 0.4."

**Write this:**

> "The LNN applies a soft AND (e.g., product t-norm) to the continuous inputs: 0.9 \\(\times\\) 0.4 = 0.36. Since this is relatively low, the system would likely not activate the heating unless the threshold is set below 0.36."

That is two sentences. Done. Do not write a paragraph about what LNN is -- the question assumes you know.

### 2-Mark LNN Question (Natural Language + Boolean Contrast)

**Example:** "What does HeatingOn \\(\leftarrow\\) Cold \\(\otimes\\) AtHome mean in natural language? How is it different from Boolean AND?"

**Write this:**

> "In natural language: 'If it is cold and someone is at home, turn on the heating.' In Boolean logic, both inputs must be strictly True (1) to produce True. In LNN, the \\(\otimes\\) operator performs a soft AND over continuous truth values in [0, 1], allowing partial inputs like 0.4 or 0.9 to produce an intermediate output. This makes the logic differentiable and trainable via gradient descent."

Four sentences. Covers both marks cleanly.

### 3-Mark LNN Question (Bounds + Benefits)

**Example:** "Compute OR bounds for Alert \\(\leftarrow\\) P \\(\lor\\) Q given P=[0.8,0.9], Q=[0.3,0.6], \\(\alpha\\)=0.7. Then explain why bounds are beneficial."

**Write this:**

> "\\(L_{\text{Alert}} = \max(0.8, 0.3) = 0.8\\). \\(U_{\text{Alert}} = \max(0.9, 0.6) = 0.9\\). Since \\(L = 0.8 \geq \alpha = 0.7\\), the alert is definitely true.
>
> Bounds are beneficial because they explicitly represent uncertainty: the system knows *how confident* it is, not just a point estimate. In safety-critical applications like autonomous driving, this allows conservative decision-making -- the system can act cautiously when the lower bound is below the threshold, rather than relying on an overconfident single value."

Six sentences total. Computation + two clear reasons.

---

## Part 8: Common Traps -- Explained in Depth

### Trap 1: Truth Values Are NOT Probabilities

This is the most common mistake in student answers, and it costs marks.

| Aspect | LNN Truth Value | Probability |
|---|---|---|
| What it measures | Degree of truth / membership | Likelihood of an event |
| Range | [0, 1] | [0, 1] |
| Interpretation of 0.6 | "This is 0.6 true" (like fuzzy membership) | "There is a 60% chance this happens" |
| Can you add them? | No -- they do not sum to 1 | Yes -- complementary events sum to 1 |
| Framework | Fuzzy logic / t-norms | Bayesian / frequentist statistics |

**Why students confuse them:** Both use numbers between 0 and 1. But the operations are completely different. For probabilities, P(A AND B) = P(A) \\(\times\\) P(B) *only if A and B are independent*. For LNN truth values, the t-norm is always applied regardless of independence -- it is a matter of logical structure, not statistical independence.

**How to avoid losing marks:** Never write "there is a 36% probability the heating should turn on." Write "the truth value of HeatingOn is 0.36" or "the degree of truth is 0.36."

### Trap 2: Different T-Norms Give Different Results

Some students assume all t-norms are interchangeable. They are not. For Cold = 0.9, AtHome = 0.4:

- Product: 0.36
- Lukasiewicz: 0.30
- Godel: 0.40

A threshold of 0.35 would give different decisions depending on the t-norm:
- Product (0.36 > 0.35): Heating ON
- Lukasiewicz (0.30 < 0.35): Heating OFF
- Godel (0.40 > 0.35): Heating ON

**How to avoid losing marks:** Always state which t-norm you are using. If the question does not specify, say "Using the product t-norm (the most common choice)..." and then compute.

### Trap 3: OR Bounds Use MAX for Both L and U

Many students incorrectly use min for the upper bound of OR. Let us see why max is correct.

Think about it concretely: P has upper bound 0.9, Q has upper bound 0.6.

The OR of P and Q asks: "Is at least one of them true?" In the best case, P could be as high as 0.9. Since OR only needs *one* input to be true, the best case for OR is the best case among the inputs: max(0.9, 0.6) = 0.9.

If you used min, you would get 0.6 -- which would say "the OR can be at most 0.6." But that is wrong! P alone could be 0.9, which would make the OR at least 0.9.

**Memory aid:** OR is the "optimistic" connective -- it takes the best from each input for both bounds. AND is the "pessimistic" connective -- it takes the worst upper bound and an even lower lower bound.

### Trap 4: Checking the Wrong Value Against the Threshold

For classification:
- Check **L** against \\(\alpha\\) for "definitely true" (L \\(\geq\\) \\(\alpha\\))
- Check **U** against \\(\alpha\\) for "definitely false" (U < \\(\alpha\\))
- If neither, it is "uncertain"

Students sometimes check only the midpoint of [L, U] or check U for "definitely true." Remember: "definitely true" means *even in the worst case (the lower bound) you clear the threshold.*

### Trap 5: Forgetting That LNN Extends Classical Logic (Not Replaces It)

LNN does not throw away classical logic. When truth values are exactly 0 or 1, all t-norms produce the same result as Boolean AND. Classical logic is a *special case* of LNN -- the case where there is no uncertainty.

This matters for exam framing. Never write "LNN replaces Boolean logic." Write "LNN *extends* Boolean logic to handle continuous truth values."

---

## Part 9: The Big Picture -- Classical Logic vs LNN

| Aspect | Classical Logic | LNN |
|---|---|---|
| Truth values | {0, 1} only | [0, 1] continuous |
| AND operator | Both must be exactly 1 | Soft \\(\otimes\\): product, Lukasiewicz, or Godel |
| OR operator | At least one must be 1 | Soft disjunction with bounds |
| Uncertainty handling | Not representable | Bounds [L, U] capture confidence range |
| Trainable? | No -- rules are fixed by humans | Yes -- differentiable, uses gradient descent |
| Interpretability | Full -- every step is transparent | High -- logical structure is preserved |
| Real-world inputs | Must round to 0 or 1 (lossy) | Uses raw sensor values (no rounding) |
| When to use | Rules are known and inputs are certain | Rules may be uncertain, inputs are noisy |
| Exam tip | Always describe as the baseline to contrast against | Always contrast with this column |

---

## Part 10: Useful Exam Phrases

### Explaining the \\(\otimes\\) Operator

- "The \\(\otimes\\) operator is a soft conjunction that generalises Boolean AND to continuous truth values in [0, 1]."
- "Unlike Boolean AND, which requires both inputs to be strictly 1, the soft AND accepts partial truth values and produces an intermediate output reflecting the combined confidence."
- "This makes the logical operation differentiable, enabling gradient-based learning while preserving the logical structure."

### Explaining Bounds

- "The bounds [L, U] capture the range of possible truth values, explicitly representing the system's uncertainty about a proposition."
- "A narrow bound (e.g., [0.85, 0.90]) indicates high confidence, while a wide bound (e.g., [0.3, 0.8]) indicates significant uncertainty."
- "When the lower bound exceeds the threshold, the formula is classified as definitely true -- even in the worst-case interpretation of the evidence."

### Explaining Benefits in Safety-Critical Applications

- "Bounds allow the system to distinguish between confident and uncertain conclusions, which is essential in safety-critical domains where overconfident decisions can be fatal."
- "Rather than collapsing all information into a single point estimate, bounds preserve the uncertainty from noisy or incomplete sensor data throughout the reasoning chain."

---

## Part 11: Quick-Reference Formula Card

Copy this to your handwritten notes sheet for the exam:

```
SOFT AND (t-norms):
  Product:      A x B
  Lukasiewicz:  max(0, A + B - 1)
  Godel (min):  min(A, B)

PRODUCT-SUM OPERATORS:
  AND:  A x B
  OR:   A + B - A x B
  NOT:  1 - A

ŁUKASIEWICZ-LIKE (clamped):
  AND:  f(1 - Σ(1 - x_i))     where f(x) = max(0, min(1, x))
  OR:   f(Σ x_i)

OR BOUNDS:
  L_OR = max(L_P, L_Q)
  U_OR = max(U_P, U_Q)

AND BOUNDS (Lukasiewicz):
  L_AND = max(0, L_P + L_Q - 1)
  U_AND = min(U_P, U_Q)

CLASSIFICATION with threshold alpha:
  L >= alpha        -->  Definitely true
  U < alpha         -->  Definitely false
  L < alpha <= U    -->  Uncertain

KEY EXAMPLE:
  Cold=0.9, AtHome=0.4
  Product: 0.9 x 0.4 = 0.36
```

---

## Self-Check

Before you move on, make sure you can confidently do all of these:

- [ ] Explain in one sentence what the \\(\otimes\\) operator does compared to Boolean AND
- [ ] Compute a soft-AND result using *any* of the three t-norms
- [ ] Compute OR using Product-Sum (\\(A + B - AB\\)) and explain how it differs from Godel max
- [ ] Explain why LNN exists (the gap between classical logic and neural networks)
- [ ] Describe how an LNN uses a syntax tree as its network architecture
- [ ] Explain bidirectional message passing (upward pass vs downward pass)
- [ ] Compute OR bounds given [L, U] for each input proposition
- [ ] Compute AND bounds (Lukasiewicz) given [L, U] for each input proposition
- [ ] Classify a result as definitely true / definitely false / uncertain given a threshold
- [ ] Use the three-valued logic table to shortcut compound formula classification
- [ ] Identify a contradiction case (L > U) and explain what it means
- [ ] Apply the Łukasiewicz clamped formulas for AND and OR with more than two inputs
- [ ] List at least two reasons why bounds help in safety-critical applications
- [ ] Explain why truth values are not probabilities
- [ ] State which t-norm is most commonly expected in exam questions (product)
- [ ] Write a 1-mark, 2-mark, or 3-mark answer in the correct length and structure
