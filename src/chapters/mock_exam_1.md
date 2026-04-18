# Mock Exam 1 — Practice Test

> **Format:** 6 questions, 20 marks, 60 min (5 reading + 55 answering)
> **Rules:** Double-sided handwritten A4 page only. No calculator.
> **Tip:** Do this under timed conditions. Check answers AFTER.

---

## Question 1 [5 marks] — Symbolic Logic

**(a)** Consider the following scenario: [3 marks]

> A fire alarm activates if it detects smoke (S) or high temperature (T):
>
> $(S \vee T) \rightarrow A$
>
> Today, the alarm did NOT activate ($\neg A$).

Use propositional logic to deduce what must be true about S and T. Show your steps with a truth table.

**(b)** Consider the statement: [2 marks]

> "Every student who studies hard passes the exam."
>
> Domain: all students. StudyHard(x) = x studies hard. Pass(x) = x passes.

(i) Write this in formal first-order logic. [1 mark]

(ii) Write the **negation** of this statement in FOL and explain what it means in English. [1 mark]

---

## Question 2 [4 marks] — Logic Neural Networks

A medical triage system uses LNN. The rule is:

> ShouldTest $\leftarrow$ HighFever $\otimes$ ContactWithPatient

**(a)** What does this rule mean in natural language? How does LNN's treatment differ from classical Boolean logic? [2 marks]

**(b)** Given HighFever = 0.7, ContactWithPatient = 0.5:

Compute ShouldTest using the **Łukasiewicz t-norm**. Would the system recommend testing at threshold 0.3? At threshold 0.5? [2 marks]

---

## Question 3 [2 marks] — Knowledge Graphs

A TransE model is trained on these facts with embeddings:
- Auckland → (0.2, 0.5, 0.3), NewZealand → (0.6, 0.8, 0.7)
- Australia → (0.7, 0.9, 0.8), Oceania → (0.9, 1.0, 1.1)
- located\_in → (0.4, 0.3, 0.4)

The model correctly represents (Auckland, located\_in, NewZealand).

**Query:** (Sydney, located\_in, ?). Given that Sydney's embedding can be inferred from (Sydney, located\_in, Australia), which entity would TransE predict? Show your L1 distance calculations.

---

## Question 4 [2 marks] — MYCIN / Expert Systems

**(a)** Explain the difference between forward chaining and backward chaining. Which does MYCIN use and why? [1 mark]

**(b)** A MYCIN rule states: "IF fever (CF = 0.8) AND rash (CF = 0.5), THEN measles (rule CF = 0.7)." Calculate the confidence factor for measles. [1 mark]

---

## Question 5 [3 marks] — Decision Trees & Ensembles

A node in a decision tree has 6 positive and 4 negative examples.

**(a)** Calculate the entropy. (Given: $\log_2(0.6) \approx -0.737$, $\log_2(0.4) \approx -1.322$) [1 mark]

**(b)** Explain the difference between **bagging** and **boosting** — specifically, how each builds and combines models. [1 mark]

**(c)** In AdaBoost, a weak classifier has weighted error $\epsilon = 0.3$. Calculate $\alpha$. (Given: $\ln(7/3) \approx 0.847$) [1 mark]

---

## Question 6 [4 marks] — Soft Computing

For each scenario, state whether it involves **vagueness** or **uncertainty**. Justify in one sentence.

1. A weather app says "60% chance of rain tomorrow."
2. A review describes food as "reasonably good."
3. A doctor says the patient is "mildly obese."
4. An ML model predicts an image is a cat with 85% confidence.
