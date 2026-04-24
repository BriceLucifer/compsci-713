# Genetic Algorithms & NEAT

## Exam Priority

**Medium frequency** | Appeared directly in 1/4 past tests (2025 Real Q6, 3 marks — fitness function design) | When it appears, it is a full question worth significant marks | The key exam skill is fitness function design

---

## Let's Start From Scratch

### Part 1: Genetic Algorithms — Like Breeding Racing Turtles

Imagine you want to breed the fastest racing turtle in the world. Here is your strategy:

1. You start with 100 random turtles. Some are fast, most are slow, a few are hilariously bad.
2. You race them all. You measure how fast each one runs. This measurement is the **fitness function**.
3. You pick the top 20 fastest turtles. This is **selection**.
4. You pair them up and let them breed. Each baby inherits some genes from Mom and some from Dad — maybe Mom's powerful legs and Dad's streamlined shell. This is **crossover**.
5. Occasionally, a random mutation occurs — maybe a baby is born with extra-long flippers. This is **mutation**. Most mutations are useless or harmful, but once in a while one is brilliant.
6. You now have a new generation of 100 turtles (babies + maybe a few elite parents who pass through directly).
7. Go back to step 2. Repeat for 1000 generations.

After 1000 generations, your turtles are blazingly fast — and you never designed a fast turtle yourself. You just defined what "fast" means (the fitness function) and let evolution do the engineering.

That is a genetic algorithm. Let me make it more precise.

### The Five Components of a GA

| Component | What It Does | Turtle Analogy |
|---|---|---|
| **1. Population** | N candidate solutions, each encoded as a "chromosome" (a string of values) | 100 turtles, each with a set of genes |
| **2. Fitness Function** | Evaluates how good each solution is — higher = better | The race timer |
| **3. Selection** | Picks the fittest individuals to reproduce | Top 20 turtles get to mate |
| **4. Crossover** | Combines genes from two parents to make offspring | Baby gets Mom's legs, Dad's shell |
| **5. Mutation** | Randomly changes a gene (low probability, ~0.01) | Random new trait appears |

### The GA Pipeline

```
Initialize random population (N individuals)
       ↓
  Evaluate fitness of each individual
       ↓
  Selection (pick fittest)
       ↓
  Crossover (combine parents → offspring)
       ↓
  Mutation (randomly alter some genes)
       ↓
  New generation formed
       ↓
  Termination condition met?
    NO  → go back to "Evaluate fitness"
    YES → return best individual
```

### Crossover — How Two Parents Make a Child

There are two main types you should know:

**Single-point crossover:** Pick a random position, swap everything after it.

```
Parent A:  [1  0  1  1 | 0  0  1]
Parent B:  [0  1  0  0 | 1  1  0]
                       ↓ cut here
Child 1:   [1  0  1  1 | 1  1  0]   ← A's head + B's tail
Child 2:   [0  1  0  0 | 0  0  1]   ← B's head + A's tail
```

**Uniform crossover:** For each gene position, flip a coin — take from Parent A or Parent B.

```
Parent A:  [1  0  1  1  0  0  1]
Parent B:  [0  1  0  0  1  1  0]
Coin flip: [A  B  A  B  B  A  A]
Child:     [1  1  1  0  1  0  1]
```

**Elitism:** A small number of the very best individuals pass directly to the next generation without crossover or mutation. This ensures you never lose your best solution.

### Mutation — Small Random Changes

Mutation rate is typically very low (0.01 or even 0.001). You do not want to randomly scramble good solutions. You just want to occasionally explore something new.

For a binary chromosome, mutation means flipping a random bit:

```
Before mutation: [1  0  1  1  0  0  1]
                              ↑ mutate this position
After mutation:  [1  0  1  1  1  0  1]
```

Why bother with mutation? Without it, the population can converge too early — everyone becomes too similar, and the algorithm gets stuck in a local optimum. Mutation maintains diversity.

### Selection Methods

**Tournament selection:** Pick k random individuals, the fittest one wins and gets to reproduce. Repeat.

**Roulette wheel selection:** Each individual gets a "slice" of a roulette wheel proportional to its fitness. Spin the wheel — fitter individuals have bigger slices so they are more likely to be selected.

### When Should You Use a GA?

GAs shine when:
- The search space is huge and you cannot try everything
- The fitness function is not differentiable (so gradient descent does not work)
- The problem has many local optima (GA's population-based search is better at escaping them)
- You have no good heuristic to guide the search

Examples: robot controller design, scheduling optimization, protein folding, game AI, evolving neural network architectures (which leads us to NEAT).

> **Common Misconception:** Many students write that GAs "find the optimal solution." They do not. GAs are heuristic methods that find *good* solutions, often very good, but there is absolutely no guarantee of optimality. Never use the word "optimal" in your answer unless you qualify it with "near-optimal" or "approximate."

---

## Part 2: Fitness Function Design — THE Exam Skill

This is the skill that was directly tested in the 2025 Real Q6 (3 marks). Let me teach you the general approach, then walk through the exam question.

### The General Approach

Designing a fitness function is like writing a job description. You need to answer: "What makes a good solution, and how do I measure it?"

**Step 1:** Identify all the things you want the solution to do well. These become your fitness **components**.

**Step 2:** For each component, define a **penalty** — the difference between what you want and what the solution actually does.

**Step 3:** Combine the penalties into a single number. Usually you add them up (possibly with weights). The best solution has the LOWEST total penalty (or equivalently, the HIGHEST fitness).

**Step 4:** Consider how to aggregate across time (if the problem involves a simulation). Usually you sum penalties over all timesteps.

### The Formula Template

For most controller/agent design problems, the fitness function follows this pattern:

\\[
F = -\sum_{t=1}^{T} \left[ w_1 \cdot \text{error}_1(t) + w_2 \cdot \text{error}_2(t) + \ldots + w_n \cdot \text{error}_n(t) \right]
\\]

The negative sign is because higher fitness = better, but higher error = worse. The weights \\(w_1, w_2, \ldots\\) let you emphasize certain objectives over others.

### 2025 Real Q6 (3 marks) — Complete Walkthrough

**The question:** Design a fitness function for a GA training a walking robot controller (like Big Dog). The controller receives: desired speed, desired direction, target height. The algorithm has access to: actual speed, actual direction, actual height, and attitude (pitch, yaw, roll) from the prior timestep.

**How to think about this:**

What makes a good walking robot? Four things:

1. **It goes the right speed.** If the target speed is 2 m/s and it is going 1.5 m/s, that is bad.
2. **It goes the right direction.** If it is supposed to go north but veers east, that is bad.
3. **It stays at the right height.** If it is supposed to stand 0.8m tall but is slouching at 0.5m (or about to fall over), that is bad.
4. **It stays balanced.** If it is wobbling wildly (extreme pitch, yaw, or roll), that is bad — even if speed, direction, and height are correct, an unstable robot is about to fall.

**The answer:**

\\[
F = -\sum_{t=1}^{T} \left[ \alpha(v_{\text{target}} - v_{\text{actual}})^2 + \beta(\theta_{\text{target}} - \theta_{\text{actual}})^2 + \gamma(h_{\text{target}} - h_{\text{actual}})^2 + \lambda \cdot P_{\text{attitude}}(t) \right]
\\]

Where:
- \\(v\\) is speed, \\(\theta\\) is direction, \\(h\\) is height
- \\(P_{\text{attitude}}(t)\\) penalizes excessive pitch, yaw, or roll (e.g., if pitch exceeds ±15 degrees, add a penalty proportional to how far it exceeds the threshold)
- \\(\alpha, \beta, \gamma, \lambda\\) are weights that control how much each term matters
- The sum is over all timesteps \\(t\\) in the simulation

**Fitness is highest when all error terms are zero across all timesteps** — meaning the robot perfectly tracks the target speed, direction, and height while staying balanced.

**Mark allocation (estimated):**

| What to Include | Marks |
|---|---|
| Identify the correct error terms (speed, direction, height differences) | 1 |
| Include attitude/stability as a fitness component | 1 |
| Explain aggregation: minimize differences, sum over all timesteps, higher fitness = better | 1 |

### Tips for Fitness Function Questions in General

1. **Read the problem carefully.** Every variable mentioned is probably a hint about what should be in your fitness function. Do not ignore any of them.
2. **Penalize DIFFERENCES** between target and actual. Do not reward absolute values — "going fast" is not good if the target is slow.
3. **Include stability/safety.** If the scenario involves a physical system, balance and safety matter.
4. **Aggregate over time.** If it is a simulation, sum or average over timesteps.
5. **Explain the sign convention.** Say "higher fitness = better" or "we negate the total error so that minimizing error maximizes fitness."

---

## Part 3: NEAT — Evolving Neural Networks

Now let's combine genetic algorithms with neural networks. Standard GAs evolve a fixed-length chromosome. But what if you want to evolve not just the weights of a neural network, but its **entire structure** — how many neurons, which ones are connected to which?

That is what NEAT does. NEAT stands for **NeuroEvolution of Augmenting Topologies**.

### The Key Idea

Traditional approach: "I'll design the network architecture (layers, neurons, connections), then train the weights using backpropagation."

NEAT approach: "I'll let evolution figure out BOTH the architecture AND the weights."

### Starting Minimal

NEAT starts with the **simplest possible network**: every input directly connected to every output. No hidden nodes. No hidden layers. Just wires from inputs to outputs.

```
Input 1 ──→ Output 1
Input 2 ──→ Output 1
Input 1 ──→ Output 2
Input 2 ──→ Output 2
```

Why start minimal? Because if you start with a big, complex network, you waste time optimizing connections that might not even be needed. Starting small and growing lets evolution add complexity only when it helps.

### Structural Mutation 1: Add Connection

A new connection is created between two nodes that were not previously connected.

```
Before:                       After:
  A ──→ C                      A ──→ C
  B ──→ C                      B ──→ C
                                A ──→ B  (new! innovation #7)
```

The new connection gets:
- A random initial weight
- A globally unique **innovation number** (more on this below)

### Structural Mutation 2: Add Node

An existing connection is **disabled**, and a new node is inserted in its place. Two new connections are created:

```
Before:
  A ─────(w=0.5)─────→ C

After:
  A ─────(w=0.5)─────→ C    [DISABLED, still in genome but inactive]
  A ──(w=1.0)──→ N ──(w=0.5)──→ C    [two new connections]
```

Why weight = 1.0 on the input side? So the new node initially behaves almost identically to the old direct connection. The signal passes through the new node with minimal disruption. Over subsequent generations, evolution can adjust these weights to take advantage of the new node.

### Innovation Numbers — Why They Matter

Here is a problem: if two networks have different structures, how do you do crossover? You cannot just swap genes at a random position because the genes represent different connections.

NEAT solves this with **innovation numbers**: every time a new structural mutation occurs anywhere in the population, it gets a globally unique ID number. When two parents have a connection with the same innovation number, it means that connection arose from the same structural mutation — so they are **homologous** (matching).

### Crossover with Innovation Numbers

This is the clever part. Let me walk through an example:

```
Parent 1 (higher fitness):
  Gene 1 (innov #1): A→C, weight=0.3
  Gene 2 (innov #2): B→C, weight=0.7
  Gene 3 (innov #3): A→B, weight=0.1    ← only in Parent 1 (disjoint)
  Gene 5 (innov #5): A→D, weight=0.5
  Gene 6 (innov #6): D→C, weight=0.9    ← only in Parent 1 (excess)

Parent 2 (lower fitness):
  Gene 1 (innov #1): A→C, weight=0.2
  Gene 2 (innov #2): B→C, weight=0.4
  Gene 4 (innov #4): B→D, weight=0.6    ← only in Parent 2 (disjoint)
  Gene 5 (innov #5): A→D, weight=0.8
```

Crossover rules:
- **Matching genes** (same innovation number, here: #1, #2, #5): randomly pick from either parent
- **Disjoint genes** (present in one but not the other, within the range, here: #3, #4): inherit from the **fitter** parent
- **Excess genes** (beyond the range of the other parent, here: #6): inherit from the **fitter** parent

```
Child:
  Gene 1 (innov #1): A→C, weight=0.2    ← randomly from Parent 2
  Gene 2 (innov #2): B→C, weight=0.7    ← randomly from Parent 1
  Gene 3 (innov #3): A→B, weight=0.1    ← from fitter parent (P1)
  Gene 5 (innov #5): A→D, weight=0.5    ← randomly from Parent 1
  Gene 6 (innov #6): D→C, weight=0.9    ← from fitter parent (P1)
```

Notice: Gene 4 from Parent 2 is NOT inherited because Parent 2 is the less fit parent. The child inherits the fitter parent's unique innovations.

### Speciation — Protecting Baby Ideas

This is one of the most important concepts in NEAT, and it solves a real problem.

**The problem:** When a network gets a brand new structural mutation (say, a new hidden node), it almost always performs WORSE initially. The new node has random weights — it has not been optimized yet. If this network competes directly against well-tuned simple networks, it gets eliminated immediately.

But that new structure might be brilliant if given time to optimize its weights over several generations. How do you protect it?

**The solution: speciation.** Group similar networks into "species." Networks within a species compete against each other, not against the entire population. This gives structurally novel networks time to mature.

**How similarity is measured:**

\\[
\delta = \frac{c_1 \cdot E}{N} + \frac{c_2 \cdot D}{N} + c_3 \cdot \bar{W}
\\]

Where:
- \\(E\\) = number of excess genes
- \\(D\\) = number of disjoint genes
- \\(\bar{W}\\) = average weight difference of matching genes
- \\(N\\) = number of genes in the larger genome
- \\(c_1, c_2, c_3\\) = tunable coefficients

If \\(\delta < \text{threshold}\\), the two networks belong to the same species.

### Fitness Sharing — Keeping It Fair

Within a species, fitness is adjusted:

\\[
F'_i = \frac{F_i}{|S|}
\\]

Where \\(|S|\\) is the number of individuals in the species.

Why? Without fitness sharing, a large species dominates the population simply because it has more members producing offspring. Fitness sharing ensures that a species' total offspring count is proportional to its total fitness, not its size. This prevents any single species from taking over and gives small, novel species room to grow.

### The NEAT Full Pipeline

```
Initialize population: simple networks (inputs → outputs, no hidden nodes)
       ↓
  Run simulation for each individual → measure fitness
       ↓
  Assign individuals to species (by compatibility distance)
       ↓
  Apply fitness sharing within each species
       ↓
  Selection: pick fittest within each species
       ↓
  Crossover: align by innovation number, inherit from fitter parent
       ↓
  Mutation:
    - Weight mutation (perturb existing weights)
    - Structural: add connection (probability ~0.05)
    - Structural: add node (probability ~0.03)
       ↓
  New generation formed → Repeat
```

---

## Part 4: Why NEAT Works — The Three Big Ideas

Let me summarize why NEAT is clever, because this is what makes a great exam answer:

**1. Start minimal and grow.** Instead of guessing the right architecture upfront, start with the simplest possible network. Complexity is added only when evolution discovers it helps. This avoids wasting computation on unnecessary structure.

**2. Innovation numbers enable meaningful crossover.** The historical marking system means you can cross two networks with completely different structures and produce a valid offspring. Without innovation numbers, crossover between different topologies would be meaningless.

**3. Speciation protects innovation.** New structural mutations get time to prove themselves within a sheltered group instead of being immediately crushed by well-optimized simpler networks. This is the key to allowing complexity to emerge.

> **Common Misconception:** Students sometimes say "NEAT starts with a large random network and simplifies it." This is completely backwards. NEAT starts MINIMAL and GROWS. Write this in your answer: "NEAT begins with the simplest possible topology — inputs directly connected to outputs, no hidden nodes — and incrementally adds structure through mutation."

> **Core Intuition:** NEAT evolves both the weights and architecture of neural networks, starting minimal and growing, using innovation numbers for crossover and speciation to protect new structures.

---

## Past Paper: 2025 Real Q6 (3 marks) — Complete Model Answer

**Question:** Design a fitness function for a GA training a walking robot (Big Dog) controller.

**A 3-mark answer looks like this:**

The fitness function should evaluate each candidate controller by running a simulation and measuring how well the robot tracks its targets. The function penalizes deviations from desired behavior:

1. **Speed error:** \\(|v_{\text{target}} - v_{\text{actual}}|\\) — penalize if the robot is too fast or too slow.
2. **Direction error:** \\(|\theta_{\text{target}} - \theta_{\text{actual}}|\\) — penalize if the robot veers off course.
3. **Height error:** \\(|h_{\text{target}} - h_{\text{actual}}|\\) — penalize if the robot is too high or too low (crouching, jumping, or falling).
4. **Attitude penalty:** penalize excessive pitch, yaw, or roll — a wobbling robot is unstable even if speed and direction are correct.

The fitness is the negative sum of all penalties across all timesteps:

\\[
F = -\sum_{t} \bigl[\text{speed error}(t) + \text{direction error}(t) + \text{height error}(t) + \text{attitude penalty}(t)\bigr]
\\]

Higher fitness means lower total error across the entire simulation run. The best controller minimizes all deviations simultaneously while maintaining stability.

---

## GA vs Gradient Descent — When to Use Which

| Aspect | Genetic Algorithm | Gradient Descent |
|---|---|---|
| Search strategy | Population-based, stochastic | Single-point, follows gradient |
| Requires differentiability? | No | Yes |
| Global vs local optima | Better at escaping local optima (diverse population) | Can get stuck |
| Speed | Slow — many fitness evaluations per generation | Fast when gradients are available |
| Search space | Handles discrete, mixed, enormous spaces | Best for continuous, smooth spaces |
| When to use | Non-differentiable objectives, huge search spaces, topology optimization | Differentiable loss function, standard neural network training |

### NEAT vs Fixed-Topology Neuroevolution

| Aspect | NEAT | Fixed Topology |
|---|---|---|
| What evolves | Weights AND structure | Weights only |
| Starting point | Minimal (no hidden nodes) | Pre-defined architecture |
| Crossover | Aligned by innovation numbers | Simple gene-by-gene |
| Speciation | Yes — protects new structures | Usually not needed |
| Complexity | Grows gradually as needed | Fixed from the start |
| Key advantage | Discovers architecture automatically | Simpler to implement |

---

## Practice Problems

### Problem 1 — Design a Fitness Function (Drone Path Following)

**Scenario:** You are using a GA to evolve a controller for a delivery drone that must follow a predefined path from warehouse to customer, maintain a safe altitude, and avoid obstacles detected by sensors.

The drone controller receives: target waypoint coordinates (x, y), target altitude, obstacle distance readings (front, left, right).

Design a fitness function. What are the components?

**Solution:**

Components:
1. **Path deviation:** distance between the drone's actual position and the target waypoint at each timestep
2. **Altitude error:** difference between target altitude and actual altitude
3. **Obstacle proximity penalty:** if the drone gets too close to an obstacle (below a safety threshold), add a large penalty
4. **Mission completion bonus:** add a positive reward for reaching the final destination
5. **Energy efficiency (optional):** penalize excessive throttle changes or aggressive maneuvers

\\[
F = -\sum_{t} \left[ w_1 \cdot d_{\text{path}}(t) + w_2 \cdot |h_{\text{target}} - h_{\text{actual}}(t)| + w_3 \cdot P_{\text{obstacle}}(t) \right] + B_{\text{completion}}
\\]

The key insight: you want the drone to follow the path accurately, stay at the right height, avoid crashing, and actually finish the delivery. Each of these becomes a term in the fitness function.

### Problem 2 — What If NEAT Started Large?

**Question:** What would happen if NEAT started with a large random network (many hidden nodes, many connections) instead of a minimal one?

**Answer:**

Several problems would arise:

1. **Wasted computation.** Most connections in a random large network are unnecessary. Evolution would spend many generations pruning useless connections instead of discovering useful ones.

2. **Harder to optimize.** A large network has a vast weight space. Finding good weights for a complex topology is much harder than optimizing a simple one.

3. **No gradual complexity growth.** One of NEAT's key advantages is that complexity is added only when it helps fitness. Starting large loses this — you cannot distinguish which structures are useful and which are noise.

4. **Crossover becomes chaotic.** With many excess and disjoint genes, crossover produces wildly different offspring, making it hard to preserve good partial solutions.

5. **The whole point of NEAT is lost.** The name says "Augmenting Topologies" — it GROWS structure. Starting large defeats the purpose.

### Problem 3 — Why Is Speciation Important? (2-mark answer)

**Question:** Explain why speciation is important in NEAT.

**Model answer (aim for this length for 2 marks):**

Speciation is important because structural mutations (adding a new node or connection) typically reduce fitness initially — the new structure has unoptimized weights. Without speciation, these novel networks would be outcompeted and eliminated by simpler, well-optimized networks before they have a chance to improve. Speciation groups structurally similar networks into species, forcing them to compete only within their group. This gives innovative topologies time to optimize their weights across several generations, potentially discovering superior architectures that would otherwise be lost.

### Problem 4 — Innovation Numbers in Crossover

**Question:** What is the role of innovation numbers in NEAT crossover? Why are they necessary?

**Model answer:**

Innovation numbers are globally unique IDs assigned to each new structural mutation. They serve as historical markers that track when and where each connection gene originated. During crossover, innovation numbers allow the algorithm to align genes from two parents with potentially different topologies. Matching innovation numbers indicate homologous genes (from the same ancestral mutation), which are randomly inherited from either parent. Disjoint and excess genes (present in one parent but not the other) are inherited from the fitter parent. Without innovation numbers, there would be no way to identify which connections in two different-topology networks correspond to each other, making meaningful crossover impossible.

### Problem 5 — Crossover Exercise

**Given two parent genomes, show the crossover result:**

```
Parent A (fitness = 85):
  Innov #1: In1→Out1, w=0.5, ENABLED
  Innov #2: In2→Out1, w=0.3, ENABLED
  Innov #3: In1→H1,   w=0.8, ENABLED
  Innov #4: H1→Out1,  w=0.2, ENABLED
  Innov #7: In2→H1,   w=0.6, ENABLED

Parent B (fitness = 72):
  Innov #1: In1→Out1, w=0.1, ENABLED
  Innov #2: In2→Out1, w=0.9, ENABLED
  Innov #5: In1→H2,   w=0.4, ENABLED
  Innov #6: H2→Out1,  w=0.7, ENABLED
```

**Solution:**

First, identify gene categories:
- **Matching** (same innov #): #1, #2 — present in both parents
- **Disjoint** (within range of the other parent): #3, #4 from A; #5, #6 from B — these are within each other's range (1-7 vs 1-6)
- **Excess** (beyond the other parent's range): #7 from A — beyond B's max innov #6

Crossover rules:
- Matching genes (#1, #2): randomly from either parent
- Disjoint genes: from fitter parent (A, fitness=85) → #3, #4 from A; #5, #6 from B are discarded
- Excess genes: from fitter parent → #7 from A

```
Child:
  Innov #1: In1→Out1, w=0.1  (randomly chose Parent B)
  Innov #2: In2→Out1, w=0.3  (randomly chose Parent A)
  Innov #3: In1→H1,   w=0.8  (from fitter Parent A)
  Innov #4: H1→Out1,  w=0.2  (from fitter Parent A)
  Innov #7: In2→H1,   w=0.6  (from fitter Parent A)
```

Notice: The child inherits Parent A's topology (with hidden node H1) because Parent A is fitter. Parent B's unique structure (hidden node H2, genes #5 and #6) is lost because Parent B is less fit.

### Problem 6 — Quick Conceptual Questions

**(a)** What is the purpose of elitism in a GA?

**Answer:** Elitism allows a small number of the very best individuals to pass directly to the next generation without modification. This ensures the best solution found so far is never lost to crossover or mutation.

**(b)** Why is the mutation rate kept low (typically 0.01)?

**Answer:** A high mutation rate would randomly destroy good solutions that took many generations to evolve. Low mutation provides just enough diversity to escape local optima without disrupting the population's accumulated improvements.

**(c)** Can a GA be used to train a standard neural network's weights? Why or why not?

**Answer:** Yes, it can. Each individual's chromosome encodes the network's weights as a list of numbers. The fitness function evaluates each network on the task. However, this is usually much slower than backpropagation because GAs do not exploit gradient information. GAs are preferred for weight optimization only when the fitness function is non-differentiable.

---

## Common Mistakes — Do Not Lose Easy Marks

1. **Do not forget ANY fitness function element.** Speed, direction, height, AND attitude all matter. Each omission can cost a mark. Read the question carefully — every variable mentioned is a hint.

2. **Fitness should penalize DIFFERENCES, not reward absolute values.** "Going fast" is not good if the target speed is slow. Always frame it as error between target and actual.

3. **Do not confuse crossover with mutation.** Crossover combines TWO parents. Mutation randomly changes ONE individual. These are different operations.

4. **NEAT starts MINIMAL.** Not large, not random, not complex. Minimal: inputs directly wired to outputs, no hidden nodes. Write this explicitly in your answer.

5. **Speciation PROTECTS innovation.** Without it, new structures are killed before they can optimize. If asked "why is speciation important," this is the answer.

6. **Do not say GAs guarantee optimality.** GAs are heuristic search methods. They find good solutions, not necessarily the best possible. Never write "GA finds the optimal solution."

7. **Innovation numbers are GLOBAL.** They track mutations across the entire population, not per individual. Two networks with the same innovation number for a connection means that connection came from the same evolutionary event.

8. **Disjoint and excess genes go to the fitter parent, not both parents.** In crossover, the less fit parent's unique genes are discarded.

---

## English Expression Guide

### Describing GA Components

- "The fitness function evaluates each individual based on how well it meets the desired criteria."
- "Selection ensures that fitter individuals are more likely to reproduce, driving the population toward better solutions."
- "Crossover combines genetic material from two parents to produce offspring that may inherit the best traits of both."
- "Mutation introduces small random changes to maintain genetic diversity and prevent premature convergence."

### Describing Fitness Function Design

- "The fitness function should penalize the difference between target and actual values for each objective."
- "Fitness is highest when all error terms are minimized across the entire simulation run."
- "Attitude (pitch, yaw, roll) should be maintained within acceptable bounds to ensure stability."
- "The total fitness is computed as the negative sum of all penalty terms over all timesteps."

### Describing NEAT

- "NEAT begins with minimal network topology and incrementally adds complexity through structural mutations."
- "Innovation numbers enable meaningful crossover between networks with different topologies by providing a historical record of structural changes."
- "Speciation protects novel structures by allowing them to compete only within their own group, preventing premature elimination of promising innovations."

---

## Self-Check Checklist

- [ ] Can you list the 5 components of a GA? (population, fitness function, selection, crossover, mutation)
- [ ] Can you draw the GA pipeline from initialization to termination?
- [ ] Can you explain single-point crossover and uniform crossover with examples?
- [ ] Can you design a fitness function for a given scenario — identifying components, penalties, and aggregation?
- [ ] Can you explain what NEAT's two structural mutations do? (add connection, add node)
- [ ] Can you explain why NEAT starts minimal instead of with a large random network?
- [ ] Can you explain the role of innovation numbers in crossover?
- [ ] Can you perform a NEAT crossover given two parent genomes with innovation numbers?
- [ ] Can you explain why speciation is important in NEAT in two sentences?
- [ ] Can you explain fitness sharing and why it prevents species domination?
- [ ] Can you explain the difference between GA and gradient descent and when to use each?
