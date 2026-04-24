# Exam Topic Frequency Map（考点频率分布）

## Overview

Based on analysis of **4 past test papers** (2025 Sample, 2025 Real, 2026 Sample, 2026 Sample Answers), this chapter maps which topics appear and how often.

## Frequency Table

| Topic | 2025 Sample | 2025 Real | 2026 Sample | Count | Percentage | Priority |
|---|---|---|---|---|---|---|
| Symbolic Logic (Prop + FOL) | Q1 (3mk) | Q1 (2mk) | Q1 (5mk) | 4/4 | 100% | 🔴 必考 |
| Logic Neural Networks (LNN) | Q2 (2mk) | Q2 (3mk) | Q2 (4mk) | 4/4 | 100% | 🔴 必考 |
| Knowledge Graphs / TransE | Q3 (2mk) | Q3 (2mk) | Q3 (2mk) | 4/4 | 100% | 🔴 必考 |
| Random Forest / Feature Bagging | Q5 (3mk) | — | Q5 (3mk) | 3/4 | 75% | 🔴 必考 |
| Vagueness vs Uncertainty | Q6 (4mk) | — | Q6 (4mk) | 3/4 | 75% | 🔴 必考 |
| Multi-agent (Robot Soccer) | Q4 (2mk) | — | Q4 (2mk) | 3/4 | 75% | 🟠 高频 |
| CART Greedy | — | Q4 (2mk) | — | 1/4 | 25% | 🟡 中频 |
| Fuzzy Logic vs Traditional | — | Q5 (3mk) | — | 1/4 | 25% | 🟡 中频 |
| Backward Chaining / MYCIN | Q6 (3mk) | — | — | 1/4 | 25% | 🟡 中频 |
| GA / NEAT / Fitness Function | — | Q6 (3mk) | — | 1/4 | 25% | 🟡 中频 |

## Question Slot Patterns

The test has 6 questions that follow a consistent pattern:

| Slot | Topic | Stability | Notes |
|---|---|---|---|
| Q1 | Symbolic Logic | **Fixed** | Always propositional + FOL, always Modus Tollens |
| Q2 | LNN | **Fixed** | Always involves computation with soft operators |
| Q3 | Knowledge Graphs | **Fixed** | Always about embeddings / TransE |
| Q4 | Varies | **Rotates** | Robot soccer OR CART greedy |
| Q5 | Varies | **Rotates** | Feature bagging OR Fuzzy logic |
| Q6 | Varies | **Rotates** | Vagueness/Uncertainty OR Backward chaining OR GA fitness |

## Mark Distribution by Topic Area

```
Symbolic Logic:     ████████████████████  15-25%
LNN:                ████████████████      13-20%
Knowledge Graphs:   ██████████            10-13%
Decision Trees:     ██████████            10-15%
Soft Computing:     ████████████████████  15-20%
Multi-agent:        ██████████            10-13%
GA/NEAT:            ██████████            10-20%
```

## Key Insight: The "Safe Three"

Q1 (Logic), Q2 (LNN), and Q3 (KG) have appeared in **every single test** with virtually identical question formats. Mastering these three topics guarantees at least **6-11 marks** (40-55% of the test).

## Priority Ranking for Study

1. **First priority** (study these until perfect): Symbolic Logic, LNN, Knowledge Graphs
2. **Second priority** (high-return topics): Vagueness vs Uncertainty, Feature Bagging, CART Greedy
3. **Third priority** (prepare model answers): Robot Soccer, Fuzzy Logic, Backward Chaining, GA Fitness Function

> Every "third priority" topic has appeared at least once. The teacher rotates Q4-Q6 to test different soft computing and applied AI topics. Prepare a model answer for each.
