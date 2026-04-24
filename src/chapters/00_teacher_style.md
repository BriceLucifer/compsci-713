# Teacher's Exam Style Analysis（命题风格分析）

## Instructor: Xinyu Zhang

Based on analysis of 4 past test papers and lecture materials.

## Question Design Philosophy

### 1. Scenario-Based Questions（场景应用题）
The teacher consistently wraps concepts in **real-world scenarios**:
- Secure facility (logic), smart home heating (LNN), robot soccer (multi-agent)
- Hospital medication, warehouse fire system, autonomous vehicles
- Stock prediction (random forest), hammer throwing (fuzzy logic), walking robot (GA)

**Implication**: Don't just memorize definitions — practice applying concepts to scenarios.

### 2. "Explain + Compute" Pattern
Most questions have two parts:
- **(a)** Explain in natural language / compare with another approach
- **(b)** Do a numerical computation or give a concrete example

**Implication**: Prepare both conceptual explanations AND worked numerical examples.

### 3. Quality Over Quantity（重质不重量）
Explicitly stated in every test: "We privilege quality over quantity, i.e., you do not need to write very long answers."

**Implication**: 
- 1-mark answers: 1–2 sentences
- 2-mark answers: 2–4 sentences
- 3-mark answers: 3–6 sentences or structured points
- Don't write essays — every extra sentence risks contradicting yourself

### 4. Consistent Sentence Patterns

The teacher uses a small set of recurring question templates:

| Pattern | Examples |
|---|---|
| "Use [logic type] to deduce what must be true about X" | Q1 in all tests |
| "What does this rule represent in natural language, and how is it different from..." | Q2 in 3/4 tests |
| "Explain how [system] would compute..." | Q2(b) in all tests |
| "What is the role of..." | Q3 in all tests |
| "Describe one strategy or collective behaviour..." | Q4 in 3/4 tests |
| "Describe how [algorithm] selects..." | Q5 in 3/4 tests |
| "Why is [technique] considered a good idea?" | Q5(b) in 3/4 tests |
| "State whether vagueness or uncertainty..." | Q6 in 3/4 tests |
| "Name the elements that should be part of..." | Q6 in 1/4 tests |
| "Contrast how [rule] works using [A] vs [B]" | Q5 in 1/4 tests |

### 5. Modus Tollens is the Favourite Inference Rule
Every single Q1 requires **Modus Tollens** (not Modus Ponens). The pattern is always:
- Given: a rule (P → Q or more complex)
- Given: the conclusion is FALSE (¬Q)
- Deduce: what about the premises

**Implication**: Practice Modus Tollens + De Morgan's Law until it's automatic.

### 6. FOL Questions Always Involve Negation of Universal
The FOL part of Q1 consistently asks to:
- Convert a negated universal statement to formal logic: ¬∀x P(x)
- OR apply universal instantiation + Modus Tollens to a specific individual

### 7. Marks for "No Look-Ahead" in CART
The answer key explicitly states that mentioning impurity reduction alone is NOT sufficient for full marks on the CART greedy question. You MUST mention **"without any look-ahead"** or **"no effort to craft an optimal tree overall"**.

## Common Traps

1. **The implication trap**: Students who confuse P → Q with Q → P lose marks in Q1
2. **The "just define it" trap**: Questions asking "what does it represent" want natural language, not just formulas
3. **The verbosity trap**: Writing too much wastes time and risks errors
4. **The probability/membership trap**: Confusing fuzzy membership (degree) with probability (likelihood) in vagueness vs uncertainty

## Recommended Answer Strategy

For each question type:

| Question Type | Strategy | Time |
|---|---|---|
| Q1 Logic | Write given → rule → Modus Tollens → De Morgan's → conclusion | 8 min |
| Q2 LNN | Part (a): natural language + Boolean contrast. Part (b): compute product, discuss threshold | 8 min |
| Q3 KG | Define KGE → name inference tasks → give Einstein/bornIn example | 5 min |
| Q4 Varies | Read carefully, give ONE well-explained answer | 5 min |
| Q5 Varies | Depends on topic; for feature bagging: √n, with replacement, reduces correlation | 8 min |
| Q6 Varies | For vagueness/uncertainty: classify each item + 1-sentence justification | 8 min |

**Total**: ~42 minutes for answers, leaving ~13 minutes for review.

## What the Teacher Values

Based on marking rubrics:
1. **Correct technical terminology** used precisely
2. **Step-by-step reasoning** shown (not just final answers)
3. **Concise natural language** explanations
4. **Specific examples** rather than generic statements
5. **Awareness of limitations** (e.g., "backward chaining identifies possible, not unique causes")
