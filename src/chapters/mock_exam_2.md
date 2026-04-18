# Mock Exam 2 — Practice Test (Harder Variant)

> **Format:** 6 questions, 20 marks, 60 min
> **Focus:** Tests topics NOT in the sample test (MYCIN CF, entropy, fuzzy logic computation)
> **Rules:** Double-sided handwritten A4 page only. No calculator.

---

## Question 1 [5 marks] — Symbolic Logic + Inference

**(a)** Given the following knowledge base: [3 marks]

> 1. $P \rightarrow Q$
> 2. $Q \rightarrow R$
> 3. $P$

Using Modus Ponens, derive all conclusions that follow. Show each step clearly, naming the inference rule used.

**(b)** Translate the following into first-order logic: [2 marks]

> "There exists a city in New Zealand that has more than one million people."
>
> Predicates: City(x), InNZ(x), MillionPlus(x)

(i) Write in FOL. [1 mark]

(ii) Is the statement true in reality? Give a counterexample or confirming example. [1 mark]

---

## Question 2 [4 marks] — LNN + Fuzzy Logic

**(a)** An LNN system uses the following operators. For each, compute the result with inputs $a = 0.6$ and $b = 0.8$: [2 marks]

| Operator | Formula | Result |
|----------|---------|--------|
| Product AND | $a \times b$ | ? |
| Łukasiewicz AND | $\max(0, a+b-1)$ | ? |
| Gödel AND (min) | $\min(a, b)$ | ? |
| Standard NOT | $1 - a$ | ? |

**(b)** A fuzzy control system for an air conditioner has:
- $\mu_\text{hot}(\text{temperature}) = 0.8$
- $\mu_\text{humid}(\text{humidity}) = 0.6$

Rule: IF hot AND humid THEN fan\_speed = high.

Using fuzzy AND = min, what is the firing strength of this rule? If a second rule says "IF hot THEN fan\_speed = medium" with $\mu_\text{hot} = 0.8$, which rule fires more strongly? [2 marks]

---

## Question 3 [2 marks] — MYCIN Confidence Factors

A MYCIN knowledge base contains two rules that both conclude the same diagnosis:

- **Rule 1:** IF symptom\_A (CF=0.9) THEN disease\_X (rule CF=0.6)
- **Rule 2:** IF symptom\_B (CF=0.7) THEN disease\_X (rule CF=0.8)

**(a)** Calculate the CF of disease\_X from each rule separately. [1 mark]

**(b)** Combine the two CFs into a single confidence factor for disease\_X using the combination formula: $CF_{combined} = CF_1 + CF_2 - CF_1 \times CF_2$ (for both positive). [1 mark]

---

## Question 4 [2 marks] — Knowledge Representation

Compare **Expert Systems**, **Ontologies**, and **Knowledge Graphs** by filling in this table (give one key point per cell):

| Aspect | Expert System | Ontology | Knowledge Graph |
|--------|--------------|----------|----------------|
| **Representation** | ? | ? | ? |
| **Main strength** | ? | ? | ? |

---

## Question 5 [3 marks] — Entropy & Information Gain

Consider a dataset for predicting whether to play tennis:

| Outlook | Play? |
|---------|-------|
| Sunny | No |
| Sunny | No |
| Sunny | Yes |
| Overcast | Yes |
| Overcast | Yes |
| Rain | Yes |
| Rain | No |

**(a)** Calculate the entropy of the target variable (Play?). There are 4 Yes and 3 No out of 7.
(Given: $\log_2(4/7) \approx -0.807$, $\log_2(3/7) \approx -1.222$) [1 mark]

**(b)** Calculate the conditional entropy $H(\text{Play?} | \text{Outlook})$. [1 mark]

**(c)** Calculate the Information Gain of splitting on Outlook. [1 mark]

---

## Question 6 [4 marks] — Bayesian Reasoning

A university uses a spam filter for student emails. Statistics show:
- 20% of emails are spam: $P(\text{spam}) = 0.2$
- The word "free" appears in 80% of spam: $P(\text{free}|\text{spam}) = 0.8$
- The word "free" appears in 10% of non-spam: $P(\text{free}|\text{not spam}) = 0.1$

**(a)** Calculate $P(\text{free})$, the overall probability of seeing "free" in an email. [1 mark]

**(b)** Using Bayes' theorem, calculate $P(\text{spam}|\text{free})$. [1 mark]

**(c)** Explain why the result makes intuitive sense. [1 mark]

**(d)** Is this scenario an example of vagueness or uncertainty? Justify. [1 mark]
