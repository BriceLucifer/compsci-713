# Instructor Style Analysis（命题风格分析）

> **Instructor:** Xinyu Zhang | **Course:** COMPSCI 713 AI Fundamentals | **S1 2026**
> Based on: Sample Test + 7 lecture slide decks (W2L1 through W5L1)

---

## Overall Teaching Philosophy

The course traces the **evolution of AI reasoning**: crisp symbolic logic → neural-symbolic hybrids (LNN) → knowledge structures (KG, ontologies) → practical ML (decision trees, ensembles) → soft/approximate reasoning (fuzzy, Bayesian).

The exam mirrors this narrative — questions progress from foundational logic to increasingly "softer" methods for handling real-world imperfection.

---

## Exam Design Patterns（出题模式）

### Pattern 1: "Explain, Then Compute"

Most questions have two parts:
- Part (a): Explain a concept or distinguish two ideas → tests **understanding**
- Part (b): Apply a formula to specific numbers → tests **skill**

**Examples:**
- Q2: (a) Explain LNN rule + difference from Boolean → (b) Compute with Cold=0.9, AtHome=0.4
- Q5: (a) Describe feature selection → (b) Explain why it helps

> **Strategy**: Never just compute without explaining. Never just explain without showing you can apply it.

### Pattern 2: "Scenario-Based, Not Abstract"

Every question is wrapped in a **real-world scenario**:
- Q1: Secure facility (fingerprint + ID)
- Q2: Smart home heating
- Q3: Knowledge graph completion
- Q4: Robot soccer
- Q5: Dataset with 225 features
- Q6: Patient risk, security, student rating, spam

> **Strategy**: Practice translating between real-world descriptions and formal concepts. The exam never asks "define modus tollens" — it asks you to USE it in a story.

### Pattern 3: "Quality Over Quantity"

The exam explicitly states: *"We privilege quality over quantity."*

- Concise, clear answers score higher than long rambling ones
- Show reasoning steps but don't pad with filler
- A correct 3-sentence answer beats an incorrect 10-sentence one

> **Strategy**: Practice writing answers in 2-4 sentences per mark.

### Pattern 4: "Distinguish Similar Concepts"

The professor loves "what's the difference between X and Y":
- Q2a: Boolean vs LNN soft logic
- Q6: Vagueness vs Uncertainty (entire question)

Other likely comparison questions:
- Expert Systems vs Ontologies vs Knowledge Graphs
- Bagging vs Boosting
- Forward vs Backward Chaining
- Fuzzy Logic vs Bayesian Reasoning
- TransE vs TransH

> **Strategy**: Prepare comparison tables for every pair of related concepts.

---

## Common Question Sentence Patterns

| Pattern | Example | What It Tests |
|---------|---------|--------------|
| "What does this rule represent in natural language?" | Q2a | Formal → informal translation |
| "How is it different from [X]?" | Q2a (vs Boolean) | Compare and contrast |
| "Use [method] to deduce..." | Q1a | Apply a procedure |
| "Write this in formal [X]" | Q1b (FOL) | Informal → formal translation |
| "Explain how [system] would compute..." | Q2b | Step-by-step calculation |
| "What is the role of [X] in [Y]?" | Q3 | Explain purpose |
| "Describe how [mechanism] works" | Q5a | Explain a procedure |
| "Explain why [X] is a good idea" | Q5b | Justify a design choice |
| "Identify whether this involves [A] or [B]" | Q6 | Classification / judgement |

---

## Concept Co-occurrence（概念共现分析）

Concepts frequently paired together:

```
Propositional Logic  <-->  First-Order Logic       (Q1: both in one question)
Truth Tables         <-->  Modus Tollens            (Q1a: implicit pattern)
LNN                  <-->  Boolean Logic            (Q2a: explicit comparison)
Soft Conjunction     <-->  Threshold Decision        (Q2b: compute + decide)
KG Embeddings        <-->  Link Prediction           (Q3: purpose + task)
Random Forest        <-->  Feature Bagging            (Q5: mechanism + why)
Vagueness            <-->  Uncertainty               (Q6: core distinction)
Fuzzy Logic          <-->  Bayesian Reasoning        (W5L1: twin pillars)
Bagging              <-->  Boosting                  (W4L2: contrast)
Forward Chaining     <-->  Backward Chaining         (W4L1: MYCIN uses backward)
Expert Systems       <-->  Knowledge Graphs          (W3: KR evolution)
TransE               <-->  TransH / TransR           (W3L2: limitations + fixes)
```

---

## Predicted Questions for Actual Test（真题预测）

### Very Likely（极大概率出现）:

1. **MYCIN confidence factor calculation** — Full lecture (W4L1), not in sample → almost certainly in actual test
2. **Entropy / Information Gain calculation** — W4L2 has worked examples; classic exam question
3. **TransE distance calculation** — W3L2 slide 45-46 has a full exercise with vectors
4. **Bagging vs Boosting comparison** — Core W4L2 distinction, not in sample

### Likely（较大概率）:

5. **Ontology vs KG comparison** — W3L1 teaches both; fits the professor's style
6. **Fuzzy logic rule computation** — W5L1 fuzzy AND/OR with specific membership values
7. **Naive Bayes classification** — W5L1 burglar alarm example
8. **Forward vs Backward chaining explanation** — W4L1

### Possible（有可能）:

9. **RAG pipeline description** — W3L1/W3L2 both cover it
10. **LNN truth bound propagation** — Advanced LNN computation with [L, U] bounds

---

## Key Takeaways for Exam Prep

1. **Practice computation by hand** — truth tables, LNN operators, TransE distances, entropy, MYCIN CF
2. **Prepare comparison tables** — for every pair of related concepts
3. **Write concise** — 2-4 sentences per mark, quality over quantity
4. **Know the "why"** — for every method, know why it exists and what problem it solves
5. **Use concrete examples** — the professor values vivid illustrations over abstract definitions
6. **Cover ALL lectures** — the sample test samples broadly; the actual test may shift emphasis to untested topics
