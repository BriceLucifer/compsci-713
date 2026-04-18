# Exam Writing Training — For Non-Native English Speakers

> **目标 Goal:** Build the mental habit and sentence muscle memory so that under exam pressure, you think in English exam-logic, not in Chinese then translate.
>
> **Format:** COMPSCI 713 test = 6 short-answer questions · 20 marks · 55 min writing time · ~2.5 min per mark · quality over quantity.

---

## Part 1 — The Fundamental Problem for Non-Native Speakers

When a native speaker reads *"Explain how an LNN differs from Boolean logic"*, they immediately begin structuring a response. When a non-native speaker reads the same question, there is often an extra mental step:

> *understand question → think answer in Chinese → translate into English → write*

This extra step costs time and produces awkward phrasing. The goal of this chapter is to **short-circuit** that process so you think directly in **English exam patterns**.

### The Three Most Common NNS Mistakes in This Exam

| Mistake | Bad Example | Fix |
|---------|------------|-----|
| Over-long sentences | "The LNN is a system that uses the t-norm which is a function that computes AND in a way that is different from Boolean..." | Split into short sentences. One idea per sentence. |
| Translating Chinese structure | "Boolean logic it requires..." (topic-comment structure) | English: subject + verb. "Boolean logic **requires**..." |
| Missing the "so what" | "Entropy measures uncertainty." (stops too early) | Add consequence: "...therefore, a lower entropy after a split means the feature is more informative." |

---

## Part 2 — Answer Architecture by Question Type

Before writing a single word, **identify the question type**. Each type has a different architecture.

### Type 1 — "What does X mean / explain X" (definition questions)

```
ARCHITECTURE: Define → Mechanism → Significance
               (1 sentence)  (1-2 sentences)  (1 sentence)

SENTENCE 1:  "[X] refers to / is defined as ..."
SENTENCE 2:  "It works by ... / This is achieved by ..."
SENTENCE 3:  "This matters because ... / As a result, ..."
```

**Practice application (1 mark):**
> "What does the confidence factor (CF) represent in MYCIN?"

Draft using the architecture:
- Define: "The confidence factor (CF) is a numeric value in the range [−1, 1] that represents the degree of belief in a conclusion..."
- Mechanism: "A CF of +1 indicates certainty that the conclusion is true, −1 indicates certainty that it is false, and 0 indicates no information..."
- Significance: "This allows MYCIN to reason under uncertainty without requiring exact probabilities."

---

### Type 2 — "How does X differ from Y" (comparison questions)

```
ARCHITECTURE: One-sentence contrast → X approach → Y approach → (consequence)

SENTENCE 1:  "The key difference between [X] and [Y] is that ..."
SENTENCE 2:  "[X] ... whereas ..."
SENTENCE 3:  "[Y], by contrast, ..."
SENTENCE 4:  (optional) "This means that [X] is preferred when ..., while [Y] suits ..."
```

**Practice application (2 marks):**
> "How does bagging differ from boosting?"

Draft:
- "The key difference is that bagging trains learners **independently in parallel**, while boosting trains them **sequentially**, each correcting the errors of the previous."
- "In bagging, each model receives a random bootstrap sample and votes equally in the final prediction, which reduces **variance**."
- "In boosting (e.g., AdaBoost), misclassified samples are given higher weight in subsequent rounds, so the ensemble focuses on hard examples, reducing **bias**."

---

### Type 3 — "Compute / Show your working" (calculation questions)

```
ARCHITECTURE: State formula → Substitute → Compute → Interpret

LINE 1:  "Using [formula name]: [formula]"
LINE 2:  "= [substitute numbers]"
LINE 3:  "= [result]"
LINE 4:  "Therefore, [interpretation in one sentence]."
```

**Practice application (2 marks):**
> "Given Cold = 0.9, AtHome = 0.4, compute HeatingOn using the product t-norm."

Draft:
- "Using the product t-norm: HeatingOn = Cold × AtHome"
- "= 0.9 × 0.4"
- "= 0.36"
- "Therefore, the output truth value is 0.36. Whether heating activates depends on the system threshold: if the threshold is 0.3, heating turns on; if it is 0.7, it remains off."

> ⚠️ Never just write the number. Always add the interpretation sentence — that is often where the second mark is awarded.

---

### Type 4 — "Build a truth table" (formal logic)

```
ARCHITECTURE: Table → mark relevant row → state conclusion

STEP 1:  Draw the table with all column headers first.
STEP 2:  Fill columns LEFT to RIGHT (don't skip to the result).
STEP 3:  Circle or underline the row where E = 0 (the given condition).
STEP 4:  Write a one-sentence conclusion starting with "Therefore, ..."
```

**Practice application (3 marks):**
> Q1(a) style — construct the truth table for (I ∧ F) → E, given ¬E.

Correct conclusion sentence:
- "Therefore, since ¬E is true and the implication must hold, I ∧ F must be 0, which means at least one of I or F is false — either the ID was invalid, the fingerprint did not match, or both."

---

### Type 5 — "Translate to FOL" (formalisation)

```
ARCHITECTURE: Define predicate(s) → identify quantifier → write formula → sanity check

STEP 1:  "Let [Pred(x)] mean '[English meaning].'"
STEP 2:  Identify the quantifier: "all" → ∀,  "some/exists" → ∃,  "not all" → ¬∀
STEP 3:  Write the formula.
STEP 4:  Read it back in English to verify it matches the original statement.
```

**Exam trap drill — translate these correctly:**

| English Statement | Correct FOL | Common Wrong Answer |
|------------------|-------------|---------------------|
| Not all birds can fly | ¬∀x Fly(x) | ∀x ¬Fly(x) ← means "no bird can fly"! |
| Some students passed | ∃x Passed(x) | ∀x Passed(x) ← too strong |
| No dog can speak | ∀x ¬Speak(x) | ¬∀x Speak(x) ← means "not all dogs speak" |
| There is a perfect score | ∃x Perfect(x) | ∀x Perfect(x) ← wrong |

---

### Type 6 — "Classify these scenarios" (Q6-style classification)

```
ARCHITECTURE: Label → One-sentence justification

FORMAT:  "[Scenario N]: [Vagueness / Uncertainty] — [one-sentence reason]."
```

**Decision tree for classification:**

```
Is the concept itself blurry (no sharp cutoff)?
    YES → VAGUENESS  → use fuzzy logic
    NO  → Is a definite fact unknown / are we inferring something?
              YES → UNCERTAINTY → use Bayesian reasoning
```

**Key signal words:**
- Vagueness cues: *"high risk", "warm", "tall", "almost", "nearly", "somewhat"*
- Uncertainty cues: *"classifying", "inferring", "predicting whether", "did X happen", "unknown diagnosis"*

---

## Part 3 — Sentence Starters by Function

Learn these as **fixed phrases**. Under exam pressure, having the first 4 words ready lets you write without hesitation.

### Starting an explanation
- "X refers to the process of..."
- "In essence, X is a mechanism that..."
- "The key idea behind X is that..."
- "X enables a model to..."
- "Put simply, X allows..."

### Showing mechanism
- "This works by..."
- "The process involves..."
- "Specifically, at each [step/node/round], ..."
- "To compute this, we..."

### Making a contrast
- "Unlike X, which [does A], Y [does B] instead."
- "The fundamental difference lies in..."
- "While X focuses on..., Y is designed to..."
- "X tends to excel when..., whereas Y is preferred when..."

### Showing consequence / so-what
- "This means that..."
- "As a result, the model..."
- "This is significant because..."
- "The practical implication is that..."
- "Therefore, we conclude that..."

### Hedging (when you are not 100% certain)
- "Depending on the threshold, the system may..."
- "This assumes that..."
- "In practice, this is typically..."

### Giving examples
- "For instance, consider..."
- "A concrete example: given [numbers], the output is..."
- "In the context of the smart home scenario, ..."

---

## Part 4 — Timed Writing Drills (based on real exam questions)

Work through these in exam conditions: **no notes, time yourself, write in English directly.**

---

### Drill Set A — 5-minute drills (2-mark questions)

**A1 — LNN (2 min per part = 4 min total)**

> Q: A smart home LNN uses the rule: `HeatingOn ← Cold ⊗ AtHome`.
>
> (a) What does this rule mean in natural language, and how does it differ from a standard Boolean rule? [2 marks]
>
> (b) Cold = 0.9, AtHome = 0.4. Compute HeatingOn and state whether heating activates. [2 marks]

*Self-check for (a):* Did you mention (1) the natural-language meaning AND (2) the specific difference — continuous vs crisp, gradient vs threshold?

*Self-check for (b):* Did you (1) state the formula, (2) substitute numbers, (3) give the result, (4) interpret with a threshold discussion?

---

**A2 — Vagueness vs Uncertainty (1 min per scenario)**

> Classify each as Vagueness or Uncertainty and give a one-sentence justification:
>
> 1. A medical system labels a patient as "high risk."
> 2. A detective infers whether a burglary occurred based on evidence.
> 3. A professor says a student's work is "almost excellent."
> 4. A spam classifier predicts whether an email is spam.

*Self-check:* Answers are V, U, V, U. For each, can you write one crisp justification sentence?

---

**A3 — Information Gain (5 min)**

> A dataset has 10 samples: 5 positive, 5 negative. Feature X splits them into:
> - Left branch: 4 positive, 0 negative
> - Right branch: 1 positive, 5 negative
>
> (a) Compute H(parent). [1 mark]
> (b) Compute weighted H after split. [1 mark]
> (c) Compute IG and state whether X is a useful split. [1 mark]

*Working (write this format):*
```
H(parent) = −0.5·log₂(0.5) − 0.5·log₂(0.5) = 1.0 bit
H(left)   = 0  (pure)
H(right)  = −(1/6)·log₂(1/6) − (5/6)·log₂(5/6) ≈ 0.650
H(after)  = (4/10)·0 + (6/10)·0.650 = 0.390
IG        = 1.0 − 0.390 = 0.610 bits
∴ X is an informative split (IG = 0.610 > 0).
```

---

### Drill Set B — 8-minute drills (3-4 mark questions)

**B1 — Random Forest feature bagging (3 marks)**

> You have a dataset with 225 features. You are building a Random Forest with 2048 trees.
>
> (a) How many features would you sample at each split? Justify. [2 marks]
> (b) Why is feature bagging considered beneficial even when a random subset of features is used? [1 mark]

*Answer framework for (a):*
- State the rule: "The standard heuristic is to sample √p features per split."
- Apply it: "With 225 features, √225 = 15 features per split."
- Justify: "This is sampled **with replacement** from all 225 features; any number substantially less than 225 is acceptable."

*Answer framework for (b):*
- Start with the problem feature bagging solves: "Without feature bagging, a single strong predictor tends to be selected as the root of most trees..."
- State the consequence: "...making the trees highly correlated, so averaging them provides little variance reduction."
- State the fix: "Feature bagging ensures each tree uses a different random subset, **decorrelating** the trees so they make complementary errors and improve ensemble performance."

---

**B2 — MYCIN backward chaining (3 marks)**

> Describe how MYCIN uses backward chaining to diagnose a patient. Include in your answer: (a) the direction of reasoning, (b) how it handles uncertainty, and (c) what the explanation facility provides. [3 marks]

*Answer framework:*
- "(a) MYCIN uses **backward chaining**: it begins with a diagnostic hypothesis (e.g., 'Does the patient have bacteraemia?') and works backwards, identifying which rules could prove this hypothesis, then asking the clinician for the evidence those rules require."
- "(b) Uncertainty is handled via **confidence factors (CFs)**: each rule has a CF encoding expert confidence, and the CF of the evidence is multiplied by the CF of the rule. Multiple rules pointing to the same conclusion are combined using CF_combined = CF_a + CF_b(1 − CF_a)."
- "(c) The explanation facility allows the clinician to ask 'Why?' (to see the current goal) or 'How?' (to see the chain of rules that produced a conclusion), making the system transparent and trustworthy in a clinical setting."

---

**B3 — Knowledge Graph Embeddings (2 marks)**

> Explain what Knowledge Graph Embeddings (KGE) are and describe one inference task they enable. [2 marks]

*Answer framework:*
- "KGE represents entities and relations in a knowledge graph as dense vectors in a continuous space. This allows models to generalise over observed facts and perform reasoning tasks algebraically."
- "One key task is **link prediction**: given an incomplete triple (h, r, ?), the model finds the entity t that minimises the scoring distance — for example, TransE computes t* = argmin ||h + r − t||. This enables discovery of missing facts, such as inferring (Einstein, bornIn, Germany) even if that triple was not explicitly stored."

---

### Drill Set C — Full exam simulation (55 minutes)

Set a timer for 55 minutes. Use your handwritten A4 notes page. Attempt all 6 questions.

**Full Mock Exam — Writing Practice Version**

---

**Question 1 [5 marks] — Symbolic Logic**

(a) Consider the rule: "A package is delivered only if it is paid AND the address is verified."
Let P = paid, A = address verified, D = delivered.
The rule is: (P ∧ A) → D.
Today, the package was NOT delivered.
Use a truth table to deduce what must be true about P and A. [3 marks]

(b) A logistics manager says: "Not every shipment in this batch arrived on time."
Let domain = all shipments in the batch. Let OnTime(x) mean "shipment x arrived on time."
(i) Write this claim in FOL. [1 mark]
(ii) Give a realistic example that makes the statement true. [1 mark]

---

**Question 2 [4 marks] — Logic Neural Networks**

A medical AI uses: `Diagnosis ← Fever ⊗ Rash`, where ⊗ is the LNN soft conjunction.

(a) What does this rule mean, and how does the ⊗ operator differ from Boolean AND? [2 marks]

(b) Fever = 0.75, Rash = 0.5. Compute Diagnosis using the Lukasiewicz t-norm. State whether the system should flag a diagnosis given threshold = 0.4. [2 marks]

---

**Question 3 [2 marks] — Knowledge Graphs**

Explain what KGE enables that a traditional symbolic KG cannot do, and give one concrete example of a link prediction task. [2 marks]

---

**Question 4 [2 marks] — Multi-Agent Systems**

Name and briefly describe **two** collective strategies that a team of robots could use in the robot soccer context discussed in this course. [2 marks]

---

**Question 5 [3 marks] — Decision Trees & Ensembles**

(a) A Random Forest is trained on data with 100 features. How many features would be sampled at each split, and why? [2 marks]

(b) Explain, in one paragraph, why feature bagging is beneficial and what problem it solves. [1 mark]

---

**Question 6 [4 marks] — Soft Computing**

Classify each scenario below as **Vagueness** or **Uncertainty** and justify your answer in one sentence each.

1. A credit scoring system assigns a customer to the "somewhat risky" category.
2. A geologist infers whether an earthquake occurred at a specific location based on seismic readings.
3. A sentiment classifier labels a review as "almost positive."
4. A doctor predicts the probability of a patient developing diabetes based on biomarkers.

---

### Self-Scoring Rubric for Mock Exam

After writing, compare against these markers:

| Q | Key marks to check |
|---|-------------------|
| Q1(a) | Two truth tables drawn, conclusion sentence present |
| Q1(b) | Formula uses ¬∀ not ∀¬; example is specific |
| Q2(a) | Natural language + specific difference (continuous vs crisp) |
| Q2(b) | Formula stated, numbers substituted, threshold discussed |
| Q3 | Specific task named (link prediction) + concrete triple |
| Q4 | Two named strategies with at least one sentence each |
| Q5(a) | √100 = 10, with-replacement, justification |
| Q5(b) | Correlation problem identified + decorrelation benefit |
| Q6 | Correct V/U classification + one-sentence justification (not just "it's vague") |

---

## Part 5 — Common Language Mistakes in This Exam

### Vocabulary precision

| Loose (avoid) | Precise (use) |
|---------------|--------------|
| "kind of true" | "partial truth value / membership degree" |
| "guess the answer" | "infer / predict / classify" |
| "make it more accurate" | "reduce variance / reduce bias" |
| "the formula is changed" | "the weights are updated / re-weighted" |
| "LNN is better" | "LNN supports continuous truth values, enabling gradient-based learning" |
| "the tree is cut" | "the tree is pruned" |
| "shows the result" | "outputs / computes / yields" |

### Article rules (a / an / the)

- Use **the** when referring to a specific thing already introduced: "the truth table", "the threshold we defined"
- Use **a** / **an** for first mention: "a confidence factor", "an entity embedding"
- Zero article for abstract concepts: "entropy measures uncertainty" (not "the entropy")

### Connective words for exam flow

| Purpose | Words to use |
|---------|-------------|
| Adding a point | "Furthermore, ...", "In addition, ..." |
| Contrasting | "However, ...", "By contrast, ...", "Unlike X, Y..." |
| Giving result | "As a result, ...", "Therefore, ...", "Consequently, ..." |
| Explaining why | "This is because ...", "The reason is that ..." |
| Giving example | "For instance, ...", "Concretely, ...", "Consider the case where ..." |
| Concluding | "In summary, ...", "To conclude, ..." |

---

## Part 6 — 5-Minute Verbal Rehearsal Protocol

Do this the morning before the exam:

1. **Pick a random topic** from the list (A–H).
2. **Say out loud** — in English — a 3-sentence explanation as if talking to a classmate.
3. **Check:** Did you use a definition sentence? A mechanism sentence? A significance sentence?
4. Repeat 5 times with different topics.

This trains your mouth and working memory to produce English exam sentences under zero processing load, so when you sit down to write, the words come automatically.

---

## Part 7 — Cheat Sheet for the Handwritten A4 Note Page

When preparing your handwritten note page, structure it like this:

**Side 1 — Formulas & Computation (the "calculator")**

```
TRUTH TABLE: → is FALSE only when P=T, Q=F
FOL: ¬∀x P(x) ≡ ∃x ¬P(x)   ¬∃x P(x) ≡ ∀x ¬P(x)
LNN t-norms: Product = a×b | Lukasiewicz = max(0,a+b−1) | Gödel = min(a,b)
TransE: score = ||h+r−t||₁  (lower = more likely)
Entropy: H = −Σ p·log₂(p)    IG = H(parent) − H(weighted after)
AdaBoost: α = ½·ln((1−ε)/ε)   CF chain: CF_a + CF_b(1−CF_a)
Bayes: P(H|e) = P(e|H)P(H)/P(e)   Fuzzy: AND=min OR=max NOT=1−μ
```

**Side 2 — Key Distinctions (the "judge")**

```
Vagueness (to what DEGREE?) vs Uncertainty (how LIKELY?) 
Bagging: parallel, variance↓  vs  Boosting: sequential, bias↓
Forward chaining: data→goal   vs  Backward chaining: goal←ask (MYCIN)
Boolean AND: crisp {0,1}       vs  LNN ⊗: continuous, differentiable
∀x ¬P(x) = "no x"            vs  ¬∀x P(x) = "not all x" — NOT the same!
TransE limit: 1-to-N fails → TransH uses hyperplane projection
Random Forest: bootstrap + √p feature bagging → decorrelated trees
MYCIN CF: expert knowledge in rules, backward chaining, explanation facility
```
