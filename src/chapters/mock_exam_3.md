# Mock Exam 3 — Practice Test (Comprehensive)

> **Format:** 6 questions, 20 marks, 60 min
> **Focus:** Balanced mix of all topics; includes computation-heavy questions
> **Rules:** Double-sided handwritten A4 page only. No calculator.

---

## Question 1 [5 marks] — Symbolic Logic

**(a)** Consider the following rules in a security system: [3 marks]

> Rule 1: $(A \wedge B) \rightarrow C$
> Rule 2: $C \rightarrow D$
> Rule 3: $A$
> Rule 4: $B$

Using Modus Ponens, derive all possible conclusions. Show each inference step and name the rule used.

**(b)** A database administrator says: "No unauthorised user can access the server." [2 marks]

Predicates: Authorised(x), CanAccess(x), domain = all users.

(i) Write in FOL. [1 mark]

(ii) The negation of this statement would mean what? Write in FOL and in English. [1 mark]

---

## Question 2 [4 marks] — LNN

An LNN-based recommendation system uses this rule:

> Recommend $\leftarrow$ HighRating $\otimes$ RecentlyViewed

**(a)** Given:
- HighRating = 0.8, RecentlyViewed = 0.3

Compute Recommend using ALL THREE t-norms (product, Łukasiewicz, Gödel). Which t-norm gives the highest value? Which gives the lowest? [2 marks]

**(b)** The system also has a NOT operator. If HighRating = 0.8, what is $\neg$HighRating? 

Now compute: $\neg\text{HighRating} \vee \text{RecentlyViewed}$ using Łukasiewicz OR. 

Show that this equals the Łukasiewicz implication $\text{HighRating} \rightarrow \text{RecentlyViewed}$. [2 marks]

---

## Question 3 [2 marks] — TransE Computation

Given the following TransE embeddings:

| Entity/Relation | Vector |
|----------------|--------|
| Einstein | (0.3, 0.7, 0.5) |
| Germany | (0.8, 1.0, 0.9) |
| France | (0.6, 0.9, 0.8) |
| USA | (1.0, 0.5, 1.2) |
| born\_in | (0.5, 0.3, 0.4) |

**Query:** (Einstein, born\_in, ?)

Compute $h + r$ and find the closest entity using L1 distance. Show all calculations.

---

## Question 4 [2 marks] — Fuzzy Logic

A fuzzy control system for a washing machine has:
- $\mu_\text{dirty}(\text{clothes}) = 0.7$
- $\mu_\text{large}(\text{load}) = 0.4$

Rules:
- Rule A: IF dirty AND large THEN wash\_time = long
- Rule B: IF dirty THEN wash\_time = medium

**(a)** Using fuzzy AND = min, calculate the firing strength of each rule. [1 mark]

**(b)** Compute the fuzzy implication dirty $\rightarrow$ large using BOTH the standard formula ($\max(1-A, B)$) and the Gödel formula. Which is more intuitive and why? [1 mark]

---

## Question 5 [3 marks] — Ensembles & Bayesian

**(a)** In a Random Forest with 400 features, how many features would typically be considered at each split? Explain the formula and why this specific number is chosen. [1 mark]

**(b)** A Naïve Bayes classifier for medical diagnosis has:
- $P(\text{disease}) = 0.01$
- $P(\text{symptom}_1|\text{disease}) = 0.9$, $P(\text{symptom}_1|\text{no disease}) = 0.05$
- $P(\text{symptom}_2|\text{disease}) = 0.7$, $P(\text{symptom}_2|\text{no disease}) = 0.1$

A patient shows BOTH symptoms. Calculate $P(\text{disease}|\text{symptom}_1, \text{symptom}_2)$ up to proportionality. Which class (disease or no disease) has higher posterior? [2 marks]

---

## Question 6 [4 marks] — Mixed Short Answer

**(a)** Name ONE limitation of TransE and explain how TransH addresses it. [1 mark]

**(b)** In the context of RAG (Retrieval-Augmented Generation), explain the three main steps of the pipeline. [1 mark]

**(c)** What is the "knowledge acquisition bottleneck" in expert systems? [1 mark]

**(d)** Explain why AdaBoost's classifier weight $\alpha_t$ is larger when the error $\epsilon_t$ is smaller. What does this mean for the ensemble? [1 mark]
