# Mock Exam 4 — NEAT, Embodied AI & Comprehensive Review

> **Format:** 6 questions, 20 marks, 60 min (5 reading + 55 answering)
> **Focus:** Covers NEAT/GA and Embodied AI/Multi-Agent — topics NOT tested in Mock 1-3. Also integrates other topics.
> **Rules:** Double-sided handwritten A4 page only. No calculator.

---

## Question 1 [4 marks] — Genetic Algorithms & NEAT

A researcher wants to use NEAT to evolve a neural network that controls a robot arm to sort objects on a conveyor belt. The arm has 4 sensor inputs (object position x, y, object size, conveyor speed) and 2 outputs (arm angle, grip force).

**(a)** Describe how the initial population of neural networks would look in NEAT. Why does NEAT start this way rather than with complex networks? [1 mark]

**(b)** The researcher observes that after 50 generations, a new structural mutation adds a hidden node, but this individual's fitness drops compared to the simpler networks. Explain the mechanism NEAT uses to prevent this individual from being eliminated immediately, and write the formula it uses. [2 marks]

**(c)** After 200 generations, two parent networks have the following connection genes (shown by Innovation Number):

```
Parent 1 (fitness = 85): Inn# [1, 2, 3, 5, 6, 8]
Parent 2 (fitness = 72): Inn# [1, 2, 3, 4, 5, 7]
```

Identify the **matching**, **disjoint**, and **excess** genes for each parent. Which parent's disjoint and excess genes will appear in the offspring? [1 mark]

---

## Question 2 [3 marks] — NEAT Speciation Calculation

Two NEAT individuals have the following genomes:

| Individual A | Inn# 1 | Inn# 2 | Inn# 3 | Inn# 5 | Inn# 6 |
|---|---|---|---|---|---|
| Weight | 0.5 | -0.3 | 0.8 | 0.2 | 0.4 |

| Individual B | Inn# 1 | Inn# 2 | Inn# 4 | Inn# 5 | Inn# 7 | Inn# 8 |
|---|---|---|---|---|---|---|
| Weight | 0.7 | -0.1 | 0.6 | 0.5 | -0.2 | 0.3 |

Given: $c_1 = 1.0$, $c_2 = 1.0$, $c_3 = 0.4$, species threshold $\delta_t = 3.0$, $N = \max(\text{genome lengths})$.

**(a)** Identify the matching, disjoint, and excess genes. [1 mark]

**(b)** Calculate the compatibility distance $\delta$. Are A and B in the same species? [1 mark]

**(c)** Species X has 4 individuals with fitness values 12, 8, 6, 10. Species Y has 2 individuals with fitness values 14, 10. Calculate the adjusted fitness for each individual and the breeding quota ratio between Species X and Species Y. [1 mark]

---

## Question 3 [4 marks] — Embodied AI

**(a)** Polly (1993) was able to navigate corridors using only a 64×48 pixel camera at 15 frames per second. Explain THREE simplifying assumptions Polly exploited and the design principle this demonstrates. [2 marks]

**(b)** Brooks' robot Allen (1986) used a layered control architecture with three levels. Name each level, describe its behavior, and explain how the levels are combined. Why is this considered different from a traditional hierarchical control system? [2 marks]

---

## Question 4 [3 marks] — Multi-Agent Systems & Flocking

**(a)** Reynolds (1987) proposed three rules for simulating flocking behavior. State all three rules. What important concept in AI does this demonstrate? [1.5 marks]

**(b)** In STEAM (Tambe, 1997), explain what a Joint Persistent Goal (JPG) is and why communication is a fundamental commitment in this framework. Give a concrete example of what could go wrong without this commitment. [1.5 marks]

---

## Question 5 [3 marks] — Cross-Topic Integration

**(a)** BigDog's dynamic balancing problem is related to NEAT's double pole balancing evaluation task. Explain what the double pole balancing task is, what the fitness function measures, and why the harder version of this task requires a recurrent connection in the neural network. [1.5 marks]

**(b)** Compare the following two approaches to creating an AI controller for a robot:

| Aspect | NEAT Approach | Expert System Approach |
|---|---|---|
| How knowledge is acquired | ? | ? |
| How the controller is represented | ? | ? |
| Main advantage | ? | ? |

Fill in the table and explain which approach is better suited for a task where the rules are difficult to articulate (e.g., balancing a pole). [1.5 marks]

---

## Question 6 [3 marks] — Mixed Short Answer

**(a)** Brooks' (1990) paper is titled "Elephants Don't Play Chess." What is the core argument of this paper and how does it relate to embodied AI? [1 mark]

**(b)** In robot soccer, name and briefly explain TWO of the three coordination strategies discussed in the course. Why do these strategies work best when teammates perceive the situation similarly? [1 mark]

**(c)** What is an ablation study? The NEAT paper performed four ablation experiments. Name TWO of them and state what each result demonstrated about NEAT's design. [1 mark]
