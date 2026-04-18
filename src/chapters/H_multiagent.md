# Multi-Agent Systems — Robot Soccer & Collective Behaviour

## 🎯 Exam Importance
🟠 **高频** | Sample Test Q4: **2 marks = 10%**

> **Note:** The lecture slides for this topic were not in the provided input files. Content is reconstructed from the sample test Q4 and its official answer.

---

## 📖 Core Concepts

| Term | 中文 | Definition |
|------|------|-----------|
| Multi-Agent System / MAS（多智能体系统） | 多智能体系统 | A system of multiple autonomous agents interacting to achieve individual or shared goals |
| Collective Behaviour（集体行为） | 集体行为 | Coordinated actions among agents, e.g., passing strategies in robot soccer |
| Positioning Strategy（位置策略） | 位置策略 | Choosing formations for optimal attack/defense coverage |
| Role-Based Strategy（角色分配策略） | 角色分配策略 | Dynamically assigning roles to agents based on the current situation |

---

## 🧠 Feynman Draft

Imagine a football team where every player can see the entire field from an overhead camera. They all have the same information, but they need to coordinate — who attacks, who defends, who passes to whom?

That's exactly what **multi-agent robot soccer** is about. Each robot is an **agent** — an autonomous decision-maker. The challenge isn't just making one robot smart; it's making them work **together** without a central controller.

There are three levels of strategy discussed in this course:

**Level 1 — Collective Behaviours (集体行为)**
Like a passing play in real football: one robot calculates where to pass, another predicts interception points, and they coordinate a play. Each potential passing point gets a **value score** based on its position — is it closer to the goal? Is there an opponent nearby?

**Level 2 — Positioning Strategies (位置策略)**
Think of formation: 2-1-2 vs 1-3-1. The team chooses a formation that gives good coverage for both attack and defense opportunities.

**Level 3 — Role-Based Strategies (角色策略)**
Instead of fixed positions, each robot dynamically picks a **role** (goalkeeper, attacker, midfielder) based on the current game situation. If the ball is near the opponent's goal, more robots switch to attacker roles.

> ⚠️ **Common Misconception**: Students think multi-agent = each agent acts independently. Actually, the key challenge is **coordination** — agents must share information and align their actions.

> 💡 **Core Intuition**: Multi-agent systems coordinate autonomous agents through shared information and strategic role assignment.

---

## 🔄 How It Works

### The Robot Soccer Setup (from exam)

- **Overhead camera** provides a global view of the field
- Each frame has **225 features** (positions, velocities, etc.)
- **5 robots** per team
- All robots share the same camera view → same information

### Three Strategy Types

```
Multi-Agent Strategies
├── Collective Behaviours
│   ├── Passing strategy
│   │   ├── Identify suitable passing points
│   │   ├── Predict interception by opponents
│   │   └── Assign value to each passing point
│   └── Coordinated attack/defense transitions
├── Positioning Strategies
│   ├── Choose formation (e.g., 2-1-2)
│   └── Optimize field coverage for attack + defense
└── Role-Based Strategies
    ├── Assign roles dynamically (goalie, attacker, defender)
    └── Adapt to game situation (score, time, ball position)
```

---

## ⚖️ Trade-offs

| Strategy Type | Advantage | Disadvantage |
|--------------|-----------|-------------|
| **Collective** | Sophisticated coordinated plays | Complex to compute in real-time |
| **Positioning** | Simple to implement; good coverage | Static; doesn't adapt to opponent behaviour |
| **Role-Based** | Flexible; adapts to situation | Roles may conflict; needs coordination protocol |

---

## 📝 Exam Practice

### Practice: Q4-Style Question

**Question:** In a multi-agent robot soccer system with shared vision, name TWO strategies that a team of 5 robots could use and briefly explain each. [2 marks]

<details>
<summary>Model Answer</summary>

1. **Passing strategy (collective behaviour)**: Each robot evaluates potential passing points by predicting interception probabilities and assigning values based on field position. The robot with the ball passes to the highest-value point. [1 mark]

2. **Role-based strategy**: Each robot dynamically selects a role (attacker, defender, goalkeeper) based on the current game state — for example, when the ball is in the opponent's half, more robots adopt attacker roles. [1 mark]

</details>

---

## 🌐 English Expression Tips

- "In a multi-agent system, each agent operates autonomously but coordinates with others to achieve a shared objective."
- "The team employs a role-based strategy where each robot dynamically assumes a role based on the current game situation."
- "Collective behaviours enable coordinated actions such as passing strategies, where passing points are evaluated based on interception risk and positional advantage."

---

## ✅ Self-Test Checklist

- [ ] Can I name and explain three types of multi-agent strategies?
- [ ] Can I explain why shared information (overhead camera) enables coordination?
- [ ] Can I give a concrete example of a passing strategy with value assessment?
- [ ] Do I understand the difference between positioning vs role-based strategies?
