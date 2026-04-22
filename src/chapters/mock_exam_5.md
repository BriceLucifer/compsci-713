# Mock Exam 5 — Comprehensive Review (2026 Format)

> **Format:** 6 questions, 20 marks, 60 min (5 reading + 55 answering)
> **Rules:** Double-sided handwritten A4 page only. No calculator.
> **Note:** This exam uses DIFFERENT scenarios from previous mocks and actual tests, but tests the SAME core concepts.

---

## Question 1 [5 marks] — Symbolic Logic

**(a)** Consider the following security system rule: [3 marks]

> A building enters lockdown (L) if both the intrusion sensor triggers (I) AND the guard confirms the alert (G):
>
> $(I \wedge G) \rightarrow L$
>
> It is known that the building did NOT enter lockdown: $\neg L$.

Using propositional logic, determine what can be concluded about I and G. Show all reasoning steps clearly, naming the inference rules you use.

**(b)** Consider the following statements about a university's enrollment system: [2 marks]

> "Every student who has paid their fees is allowed to enroll in courses."
>
> Domain: all students. PaidFees(x) = x has paid fees. CanEnroll(x) = x can enroll.

(i) Write this in first-order logic (FOL). [0.5 mark]

(ii) It is known that Charlie **cannot** enroll in courses. Using FOL and an appropriate inference rule, determine what must be true about Charlie. Show your reasoning steps. [1.5 marks]

---

## Question 2 [4 marks] — Logic Neural Networks (LNN)

A warehouse robot uses an LNN-based safety system. The rule is:

> MustStop ← ObstacleDetected $\otimes$ PathBlocked

The system uses the **Product t-norm** for AND operations.

**(a)** Given the following truth bounds: [2 marks]

- ObstacleDetected: [0.6, 0.9]
- PathBlocked: [0.5, 0.8]

Compute the truth bounds [L, U] for MustStop using Product t-norm AND bounds.

If the safety threshold is α = 0.5, what is the truth status of MustStop? What if α = 0.7?

**(b)** A colleague suggests replacing the LNN system with classical Boolean logic (where obstacle detected is simply TRUE or FALSE). Give TWO reasons why LNN with truth bounds is more appropriate for this safety-critical application. [2 marks]

---

## Question 3 [2 marks] — Knowledge Graphs & TransE

A TransE model has been trained with the following entity and relation embeddings (3-dimensional):

| Entity/Relation | Embedding |
|---|---|
| Mozart | (0.3, 0.8, 0.2) |
| Symphony_No_40 | (0.7, 1.2, 0.6) |
| composed | (0.4, 0.4, 0.4) |
| Beethoven | (0.5, 0.9, 0.3) |
| Moonlight_Sonata | (0.9, 1.3, 0.7) |
| Piano_Concerto_21 | (0.8, 1.1, 0.5) |

**(a)** Verify that (Mozart, composed, Symphony_No_40) is a valid fact by computing the L1 distance score. [0.5 mark]

**(b)** For the query (Beethoven, composed, ?), compute the L1 distance to both Moonlight_Sonata and Piano_Concerto_21. Which entity does TransE predict? [1 mark]

**(c)** Name ONE limitation of TransE and briefly explain how it manifests. [0.5 mark]

---

## Question 4 [2 marks] — Multi-Agent & Embodied AI

**(a)** A team of autonomous drones is deployed to search a disaster zone for survivors. Using Tambe's STEAM framework, explain what happens when one drone discovers that the entire search area has been flooded and is inaccessible. What is the critical commitment in STEAM and why? [1 mark]

**(b)** Brooks' robot Allen (1986) used a layered control architecture. Explain how Allen would behave if its Level 2 (Explore) layer wanted to head toward a wide opening, but its Level 0 (Avoid) layer detected an obstacle in that direction. What makes this different from a traditional planning system? [1 mark]

---

## Question 5 [3 marks] — Decision Trees & Random Forest

**(a)** A dataset has 20 samples: 12 positive (+) and 8 negative (−). A candidate feature splits the data into: [2 marks]

- Left branch: 10 samples (9+, 1−)
- Right branch: 10 samples (3+, 7−)

Calculate the **Information Gain** of this split. Show the entropy calculations for the parent node and both child nodes.

(Hint: -0.9 log₂ 0.9 ≈ 0.137, -0.1 log₂ 0.1 ≈ 0.332, -0.3 log₂ 0.3 ≈ 0.521, -0.7 log₂ 0.7 ≈ 0.360, -0.6 log₂ 0.6 ≈ 0.442, -0.4 log₂ 0.4 ≈ 0.529)

**(b)** If this dataset has 100 features, how many features would a Random Forest consider at each split? Explain WHY Random Forest uses feature bagging (not just bootstrap sampling). [1 mark]

---

## Question 6 [4 marks] — Soft Computing: Vagueness vs Uncertainty

**(a)** Classify each of the following as involving **vagueness** or **uncertainty**, and justify your answer in one sentence each: [2 marks]

1. "The patient has a **moderately high** fever."
2. "There is an 80% chance the flight will be delayed due to weather."
3. "This essay is **roughly average** in quality."
4. "Given the lab results, the patient **probably** has diabetes."

**(b)** For scenario 1 above, explain how **Fuzzy Logic** would handle the concept of "moderately high fever." Describe the membership function and how a specific temperature (e.g., 38.5°C) would be processed. [1 mark]

**(c)** For scenario 4 above, explain how **Bayesian reasoning** would compute the probability of diabetes given the lab results. Write Bayes' theorem applied to this case and explain what each term represents. [1 mark]
