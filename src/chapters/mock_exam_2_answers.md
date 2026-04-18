# Mock Exam 2 — Answers & Explanations

---

## Question 1 [5 marks]

### (a) [3 marks]

**Step 1:** From (3) $P$ and (1) $P \rightarrow Q$, by **Modus Ponens**: conclude $Q$. [1 mark]

**Step 2:** From $Q$ (just derived) and (2) $Q \rightarrow R$, by **Modus Ponens**: conclude $R$. [1 mark]

**All conclusions:** $Q$ and $R$.

> This also demonstrates **transitivity**: from $P \rightarrow Q$ and $Q \rightarrow R$, we get $P \rightarrow R$ (hypothetical syllogism). [1 mark]

### (b) [2 marks]

**(i):** $\exists x \, [\text{City}(x) \wedge \text{InNZ}(x) \wedge \text{MillionPlus}(x)]$ [1 mark]

**(ii):** Auckland has a population of ~1.7 million and is a city in New Zealand, so the statement is TRUE. [1 mark]

---

## Question 2 [4 marks]

### (a) [2 marks]

| Operator | Formula | Result |
|----------|---------|--------|
| Product AND | $0.6 \times 0.8$ | **0.48** |
| Łukasiewicz AND | $\max(0, 0.6 + 0.8 - 1)$ | **0.40** |
| Gödel AND | $\min(0.6, 0.8)$ | **0.60** |
| NOT(a) | $1 - 0.6$ | **0.40** |

[1 mark for table, 1 mark for all correct]

### (b) [2 marks]

Rule 1 firing strength: $\min(0.8, 0.6) = 0.6$ [0.5 mark]

Rule 2 firing strength: $0.8$ (only one condition) [0.5 mark]

Rule 2 fires more strongly (0.8 > 0.6). This makes sense — the single-condition rule isn't weakened by a second factor. [1 mark]

---

## Question 3 [2 marks]

### (a) [1 mark]

- Rule 1: $CF_1 = CF_\text{premise} \times CF_\text{rule} = 0.9 \times 0.6 = 0.54$
- Rule 2: $CF_2 = 0.7 \times 0.8 = 0.56$

### (b) [1 mark]

Both CFs are positive, so:

$$CF_{combined} = CF_1 + CF_2 - CF_1 \times CF_2 = 0.54 + 0.56 - 0.54 \times 0.56$$
$$= 1.10 - 0.3024 = 0.7976 \approx 0.80$$

> **Intuition**: Two independent pieces of evidence both supporting disease\_X boost the overall confidence to ~0.80, higher than either alone.

---

## Question 4 [2 marks]

| Aspect | Expert System | Ontology | Knowledge Graph |
|--------|--------------|----------|----------------|
| **Representation** | IF-THEN production rules in a knowledge base | Formal concepts, relationships, and constraints (OWL/RDF schema) | Entity-relation-entity triples (subject, predicate, object) |
| **Main strength** | Can simulate expert reasoning via rule chaining; provides explanations | Enables formal classification and constraint checking across domains | Scales to billions of facts; supports inference and embedding-based reasoning |

[1 mark per correct row]

---

## Question 5 [3 marks]

### (a) [1 mark]

$p_{\text{Yes}} = 4/7$, $p_{\text{No}} = 3/7$

$$H(\text{Play?}) = -\frac{4}{7}\log_2\frac{4}{7} - \frac{3}{7}\log_2\frac{3}{7}$$
$$= -\frac{4}{7}(-0.807) - \frac{3}{7}(-1.222)$$
$$= 0.461 + 0.524 = 0.985 \text{ bits}$$

### (b) [1 mark]

Split by Outlook:
- **Sunny** (3 examples): 1 Yes, 2 No → $H = -\frac{1}{3}\log_2\frac{1}{3} - \frac{2}{3}\log_2\frac{2}{3}$

  $= -\frac{1}{3}(-1.585) - \frac{2}{3}(-0.585) = 0.528 + 0.390 = 0.918$

- **Overcast** (2 examples): 2 Yes, 0 No → $H = 0$ (pure node)

- **Rain** (2 examples): 1 Yes, 1 No → $H = 1.0$ (maximum entropy)

$$H(\text{Play?}|\text{Outlook}) = \frac{3}{7}(0.918) + \frac{2}{7}(0) + \frac{2}{7}(1.0)$$
$$= 0.394 + 0 + 0.286 = 0.680 \text{ bits}$$

### (c) [1 mark]

$$IG(\text{Play?}|\text{Outlook}) = H(\text{Play?}) - H(\text{Play?}|\text{Outlook}) = 0.985 - 0.680 = 0.305 \text{ bits}$$

> Knowing the Outlook reduces uncertainty about Play? by 0.305 bits — a meaningful split.

---

## Question 6 [4 marks]

### (a) [1 mark]

$$P(\text{free}) = P(\text{free}|\text{spam})P(\text{spam}) + P(\text{free}|\neg\text{spam})P(\neg\text{spam})$$
$$= 0.8 \times 0.2 + 0.1 \times 0.8 = 0.16 + 0.08 = 0.24$$

### (b) [1 mark]

$$P(\text{spam}|\text{free}) = \frac{P(\text{free}|\text{spam})P(\text{spam})}{P(\text{free})} = \frac{0.8 \times 0.2}{0.24} = \frac{0.16}{0.24} \approx 0.667$$

### (c) [1 mark]

This makes sense because "free" is much more common in spam (80%) than in legitimate emails (10%). Seeing "free" should strongly shift our belief toward spam. The prior of 20% spam gets updated to 67% — the evidence more than triples the prior probability.

### (d) [1 mark]

**Uncertainty** — The system doesn't know whether the email IS spam; it's inferring an unknown class from observed evidence (the word "free"). This is a probabilistic reasoning problem, not a question of blurry concepts.
