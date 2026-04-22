# NEAT & Genetic Algorithms — NeuroEvolution of Augmenting Topologies

## 🎯 考试重要度

🟠 **高频** | Week 6 Lecture 11 (24 slides) | 属于 Soft Computing 大类，与 GA 强关联

> **Exam track record:**
> - S1 2024 Final Q6: NEAT for mobile robot — design fitness function + time-consuming aspect of tuning
> - S1 2025 Actual Q6 (3m): Design fitness function for BigDog walking robot using GA
> - S1 2025/2026 Sample Q4 (2m): Robot soccer strategies (cross-topic with H_multiagent)
>
> The professor consistently tests **fitness function design** — this is the single most exam-critical skill for this chapter.

---

## 📖 核心概念速查（Core Concepts）

| English Term | 中文 | 一句话定义 |
|---|---|---|
| Genetic Algorithm (GA)（遗传算法） | 遗传算法 | An optimization algorithm inspired by Darwin's evolution: population → fitness → selection → crossover → mutation → repeat |
| Population（种群） | 种群 | A set of N candidate solutions (individuals/chromosomes) |
| Chromosome（染色体） | 染色体 | One individual's complete encoding — a sequence of genes |
| Gene（基因） | 基因 | The smallest unit of encoding within a chromosome |
| Phenotype（表现型） | 表现型 | The problem-specific expression of genes (weights, features, behaviors) |
| Genotype（基因型） | 基因型 | The internal encoding (the chromosome itself) |
| Fitness Function（适应度函数） | 适应度函数 | Evaluates how close an individual is to the ideal solution |
| Selection（选择） | 选择 | Picking the fittest individuals for reproduction |
| Crossover（交叉） | 交叉 | Combining genes from two parents to produce offspring |
| Single-point Crossover（单点交叉） | 单点交叉 | Choose one crossover point, swap the segments after it |
| Uniform Crossover（均匀交叉） | 均匀交叉 | Each gene position is randomly chosen from either parent |
| Mutation（变异） | 变异 | Randomly flipping or perturbing genes with low probability (0.01 or 0.001) |
| Elitism（精英保留） | 精英保留 | Very fit individuals pass directly to the next generation without modification |
| NEAT（神经进化增强拓扑） | 神经进化增强拓扑 | A GA that evolves **both** the topology AND weights of neural networks |
| Node Gene（节点基因） | 节点基因 | Encodes a node: sensor, output, or hidden type |
| Connection Gene（连接基因） | 连接基因 | Encodes a connection: in-node, out-node, weight, enabled/disabled, innovation number |
| Innovation Number（创新编号） | 创新编号 | A globally unique ID assigned to each new structural mutation; enables alignment during crossover |
| Speciation（物种形成） | 物种形成 | Grouping similar individuals into species to protect structural innovations from premature elimination |
| Adjusted Fitness（调整适应度） | 调整适应度 | Individual fitness divided by species size — prevents large species from dominating |
| Disjoint Genes（不相交基因） | 不相交基因 | Genes present in one parent but not the other, falling **within** the other parent's innovation number range |
| Excess Genes（超出基因） | 超出基因 | Genes present in one parent but not the other, falling **beyond** the other parent's maximum innovation number |
| Ablation Study（消融实验） | 消融实验 | Removing one component at a time to verify its contribution to performance |

---

## 🧠 费曼草稿（Feynman Draft）— 用大白话讲清楚

### Part 1: Genetic Algorithms — Like Breeding Racing Turtles

Imagine you are breeding 100 turtles to race. Each turtle has different "genes" — leg length, shell weight, muscle mass — all assigned randomly at birth. You let them race, measure their speed (this is the **fitness function**), keep the fastest 20 (this is **selection**), let those 20 breed by mixing their genes (this is **crossover**), and occasionally a baby turtle has a random gene flip — maybe extra-strong muscles (this is **mutation**, with a low probability like 0.01). Repeat for many generations, and your turtles get faster and faster.

That is a Genetic Algorithm in a nutshell.

```
The complete GA pipeline:

Initialize random population of N individuals
    ↓
Evaluate each individual using Fitness Function
    ↓
Select the fittest individuals
    ↓
Crossover: mix genes of selected parents → offspring
    ↓
Mutation: randomly perturb some genes (low rate)
    ↓
New generation replaces old → go back to Evaluate
    ↓
(After many generations) → best solution found
```

**Key aspects from the lecture (memorize this list):**

1. **Initialization** — random gene values for all N individuals
2. **Fitness/Evaluation** — problem-specific scoring
3. **Selection** — fittest survive
4. **Crossover/Reproduction** — mix genes of parents
5. **Mutation** — random perturbation for diversity

### Part 2: Chromosomes, Genes, and Phenotypes

An "individual" is a chromosome (a string of genes). What the genes *code for* is the **phenotype** — this is problem-specific:

```
Individual A1:  [0, 0, 0, 0, 0, 0]  ← each slot is a Gene
Individual A2:  [1, 1, 1, 1, 1, 1]  ← the entire string is a Chromosome
Individual A3:  [1, 0, 1, 0, 1, 1]
Individual A4:  [1, 1, 0, 1, 1, 0]
      ↑ All individuals together = Population
```

The gene values are **randomly assigned** at initialization. What they represent depends on the problem:
- **Regression** → genes = feature weights
- **Classification** → genes = feature selection (0/1)
- **Gaming/Control** → genes = neural network weights and connections (this is what NEAT does!)
- **Scheduling** → genes = task assignments
- **Portfolio optimization** → genes = asset allocations

### Part 3: Fitness Functions — The Heart of GA

The fitness function is **the most important design decision** in any GA application. It evaluates "how close to ideal" each individual is.

Examples from the lecture:
- **Regression problem** → fitness = negative squared error (lower error = higher fitness)
- **Classification problem** → fitness = accuracy or F1 score
- **Gaming/Control** → fitness = survival time, score, distance traveled

The fittest individuals are selected for the next generation. This is natural selection in action.

### Part 4: Crossover — Two Methods

**Single-point Crossover:**

```
Parent 1:  [A A A A | B B B B]
Parent 2:  [C C C C | D D D D]
                     ↑ crossover point (randomly chosen)
Child 1:   [A A A A | D D D D]  ← left from P1, right from P2
Child 2:   [C C C C | B B B B]  ← left from P2, right from P1
```

**Uniform Crossover:**

```
Parent 1:  [0 0 0 0 0 0 0 0 0 0]
Parent 2:  [1 1 1 1 1 1 1 1 1 1]
Mask:      [P1 P2 P1 P1 P2 P2 P1 P2 P1 P2]  ← random for each position
Child:     [0  1  0  0  1  1  0  1  0  1 ]
```

**Important details from the lecture:**
- **Elitism**: The very fittest individuals pass through directly to the next generation WITHOUT crossover or mutation. This ensures the best solution so far is never lost.
- **Not all individuals undergo crossover** — some are just copied (with possible mutation).

### Part 5: Mutation

Mutation randomly flips or perturbs genes. The rate is **low** — typically 0.01 (1%) or 0.001 (0.1%).

Why low? Too much mutation = random search (no learning from good solutions). Too little = premature convergence (stuck in local optima). Mutation maintains **diversity** in the population.

Both crossover and mutation are called **genetic operators**.

### Part 6: GA Applications

From the lecture slides, GA is good for:
- **Configuration and scheduling** (factory floor, airline crew)
- **Financial portfolio optimization** (asset allocation)
- **Vehicle routing** (delivery logistics)
- **Protein folding** (biological structure prediction)
- **Game AI** (evolving player strategies)

> **Why GA works for these?** Because the search spaces are **vast** and exhaustive search is impractical. GA encodes domain knowledge through the fitness function and explores efficiently through crossover and mutation.

### Part 7: NEAT — Evolving Neural Networks

Now the main event. Ordinary GA optimizes a string of numbers. **NEAT's radical idea: treat the entire neural network — its structure AND weights — as the "individual" to be evolved.**

Imagine a competition for architects. Each contestant starts with the **simplest possible blueprint** (just inputs wired directly to outputs, no hidden rooms). Then:

1. **Evaluate** each design's performance
2. **Select** the best designs
3. **Crossover** good designs together
4. **Mutate** — but here mutation is special!

#### NEAT Genome Encoding

Each NEAT individual's genotype has two types of genes:

**Node Genes:** Each node has a type — Sensor (input), Output, or Hidden

**Connection Genes:** Each connection has five attributes:

| Attribute | Description |
|---|---|
| In-Node | Source node ID |
| Out-Node | Destination node ID |
| Weight | Connection weight (real number) |
| Enabled/Disabled | Whether this connection is active |
| Innovation Number | Globally unique ID for this structural mutation |

Example genome:

```
Node Genes: [Node1(Sensor), Node2(Sensor), Node3(Sensor), Node4(Output), Node5(Hidden)]

Connection Genes:
| In | Out | Weight | Enabled | Innovation# |
|----|-----|--------|---------|-------------|
| 1  | 4   | 0.7    | YES     | 1           |
| 2  | 4   | -0.5   | NO      | 2           |
| 3  | 4   | 0.5    | YES     | 3           |
| 2  | 5   | 0.2    | YES     | 4           |
| 5  | 4   | 0.4    | YES     | 5           |
| 1  | 5   | 0.6    | YES     | 6           |
```

**NEAT starts minimal:** All inputs connected directly to the output, **no hidden nodes**, random weights. Complexity grows only as needed.

### Part 8: Structural Mutations in NEAT

#### Mutation 1 — Add Connection

```
Before mutation:              After mutation:
    4 (Output)                  4 (Output)
   / \                         / | \
  /   \                       /  |  \
 1    2    3                 1   2    3
(In) (In) (In)                  ↑
                          New connection 3→4
                          with random weight
                          and next Innovation Number
```

- Creates a connection between two previously unconnected nodes
- Receives the **next available Innovation Number** and a **random weight**
- **Can loop back** (recurrent connection) → gives the network **memory**! This is critical for tasks where the network needs to remember past inputs (like the double pole balancing task without velocity inputs)

#### Mutation 2 — Add Node

```
Before: Node1 ---(weight 0.7)--→ Node4

After:  Node1 ---(weight 1.0)--→ Node5 ---(weight 0.7)--→ Node4
                                  ↑ NEW node!

The original connection 1→4 is DISABLED.
New connection 1→5: weight = 1.0
New connection 5→4: weight = old weight (0.7)
```

> 💡 **Critical design insight**: The connection INTO the new node has weight **1.0**, and the connection FROM the new node has the **old connection's weight**. This means: 1.0 × 0.7 = 0.7, which equals the old connection's output. So the network **behaves identically before and after the mutation**! This preserves pre-mutation performance and lets the new structure be optimized gradually.

### Part 9: Crossover in NEAT — Innovation Numbers Are the Key

In ordinary GA, crossover is simple (just swap segments). But NEAT networks have **different topologies** — how do you align them? Answer: use **Innovation Numbers** as a global timeline of structural mutations.

```
Parent 1 (fitter):   [1→4, 2→4, 3→4, 2→5, 5→4]
                       Inn#1 Inn#2 Inn#3 Inn#4 Inn#5

Parent 2 (less fit):  [1→4, 2→4, 3→4, 1→5, 5→4, 3→5]
                       Inn#1 Inn#2 Inn#3 Inn#8 Inn#9 Inn#10
```

**Alignment rules:**

| Gene Type | Definition | Inherited From |
|---|---|---|
| **Matching genes** | Same Innovation# in both parents | Randomly chosen from either parent (or from fitter parent) |
| **Disjoint genes** | Present in one parent, within the other's range | Inherited from the **fitter** parent |
| **Excess genes** | Present in one parent, beyond the other's max | Inherited from the **fitter** parent |

**If both parents have equal fitness:** disjoint and excess genes are inherited **randomly** from either parent.

**Disabled genes:** If a gene is disabled in either parent, it has a **small chance of being re-enabled** in the offspring.

**Concrete example of disjoint vs excess:**

```
Parent 1 innovation numbers: [1, 2, 3, 4, 5]
Parent 2 innovation numbers: [1, 2, 3, 8, 9, 10]

Matching:  Inn#1, Inn#2, Inn#3 (both have them)
Disjoint:  Inn#4, Inn#5 (P1 only, within P2's range 1-10)
           Inn#8, Inn#9 (P2 only, within P1's range 1-5... wait, 8 > 5)
           Actually: Inn#4, Inn#5 from P1 are disjoint (within range 1-10)
                     Inn#8, Inn#9 from P2 are disjoint (within range 1-5? No, 8 > 5)

Correction — the boundary is the OTHER parent's max innovation number:
- P1's max = 5, P2's max = 10
- In P2: genes with Inn# > 5 (i.e., 8, 9, 10) are EXCESS
- In P2: genes with Inn# ≤ 5 that P1 doesn't have = DISJOINT (none here)
- In P1: genes with Inn# > 10 = EXCESS (none here)
- In P1: genes with Inn# ≤ 10 that P2 doesn't have = DISJOINT (Inn#4, Inn#5)
```

### Part 10: Speciation — Protecting Innovation

This is NEAT's most clever design.

**The problem:** A new structural mutation (e.g., a new hidden node) performs **poorly at first** because its weights haven't been optimized yet. If it competes directly against well-tuned older networks, it will be eliminated immediately. But maybe it just needs a few more generations to become superior!

**The solution:** Group similar individuals into **species** and make them compete **within their species**, not against the whole population.

#### Distance Formula

$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$

| Symbol | Meaning |
|---|---|
| $E$ | Number of **Excess** genes |
| $D$ | Number of **Disjoint** genes |
| $N$ | Number of genes in the **larger** genome |
| $\overline{W}$ | Average **weight difference** of matching genes |
| $c_1, c_2, c_3$ | Configurable importance coefficients |
| $\delta_t$ | Species distance threshold |

- If $\delta < \delta_t$ → **same species**
- If $\delta \geq \delta_t$ → **different species**

#### Adjusted Fitness (Fitness Sharing)

$$f'_i = \frac{f_i}{|S|}$$

Where $|S|$ is the number of individuals in species $S$.

**Concrete numerical example:**

> Species A has 5 individuals with raw fitness: 10, 8, 6, 12, 9
> Adjusted fitness: 2.0, 1.6, 1.2, 2.4, 1.8
> Sum of adjusted fitness for Species A = **9.0**
>
> Species B has 2 individuals with raw fitness: 10, 8
> Adjusted fitness: 5.0, 4.0
> Sum of adjusted fitness for Species B = **9.0**
>
> Breeding quota: Species A gets 50%, Species B gets 50%.
> Without adjustment, Species A (total raw = 45) would massively dominate Species B (total raw = 18).

**Species quota** is proportional to the sum of adjusted fitness. This:
- Prevents large species from monopolizing reproduction slots
- Gives small species (which may contain novel innovations) time to improve

### Part 11: Evaluation Task — Double Pole Balancing

The NEAT paper's benchmark task:

```
        θ₁    θ₂       ← two poles of DIFFERENT lengths
         |   |
    ┌────┤   ├────┐
    │  ──┼───┼──  │    ← cart
    └────────────────┘
    ←────────────────→
          limited track
```

- A cart on a limited track must balance two poles simultaneously
- Poles have **different lengths** (harder than single pole)
- **Fitness = number of time steps survived** without poles falling or cart leaving track
- **Harder version**: remove angular velocity inputs → the network must develop **recurrent connections** (memory) to infer velocity from position changes over time

**NEAT Pipeline for this task:**

```
1. Initialize population of simple networks
   (inputs: cart position, pole angles → output: force direction)
   No hidden nodes initially!
        ↓
2. Each network controls the cart in simulation
        ↓
3. Measure fitness (survival time steps)
        ↓
4. Selection (using species-adjusted fitness)
        ↓
5. Crossover (align by innovation numbers)
        ↓
6. Mutation (add nodes, add connections, perturb weights)
   Recurrent connections may appear → enables memory!
        ↓
7. Speciate the new generation
        ↓
8. Repeat → networks gradually become more complex
        ↓
9. Eventually: a network that balances both poles!
```

### Part 12: Ablation Study — Every Component Matters

The NEAT authors systematically removed components to prove each one contributes:

| Ablation Condition | Result |
|---|---|
| Fixed fully-connected network (no topology evolution) | **Worse** — slower or fails |
| Larger-than-minimal starting network | **Worse** — slower convergence |
| No speciation | **Worse** — innovations eliminated prematurely |
| No crossover (mutation only) | **Worse** — slower learning |

**Conclusion:** All four NEAT innovations — minimal initialization, structural mutation, historical markings (innovation numbers), and speciation — are **essential**. Remove any one and performance degrades.

### Part 13: NEAT Applications

From the lecture:
- **Game play**: Flappy Bird, Pac-Man, Monopoly
- **Robot control**: pole balancing, locomotion
- **Explainability**: NEAT produces **small, interpretable** networks (unlike deep learning's massive models)

⚠️ **Common Misconception**: Many students think NEAT starts with a complex network with hidden layers. **Wrong!** NEAT begins with the **simplest possible structure** — all inputs directly connected to outputs, zero hidden nodes. Complexity is added incrementally through mutation, only when the fitness pressure demands it. This is NEAT's core philosophy: **complexify incrementally**.

⚠️ **Common Misconception #2**: Students confuse NEAT's mutation with standard GA mutation. In standard GA, mutation just flips a gene value. In NEAT, there are **structural mutations** (add node, add connection) that change the network's topology, plus **weight mutations** that perturb existing weights. Both types coexist.

💡 **Core Intuition**: NEAT = evolution applied to neural networks. Start simple, grow complex only when needed, use innovation numbers to enable crossover between different topologies, and use speciation to protect newborn innovations.

---

## 📐 正式定义（Formal Definition）

**Genetic Algorithm (GA):** A class of metaheuristic optimization algorithms inspired by Darwin's theory of natural selection. A population of N candidate solutions (individuals), each encoded as a chromosome of genes, evolves over generations. In each generation: (1) a fitness function evaluates each individual, (2) the fittest are selected, (3) selected parents undergo crossover to produce offspring, (4) offspring undergo mutation with low probability, and (5) the new generation replaces the old. The process repeats until convergence or a stopping criterion is met.

**NEAT (NeuroEvolution of Augmenting Topologies):** A genetic algorithm proposed by Stanley & Miikkulainen (2002) that evolves both the **topology** (structure) and **weights** of neural networks. Four key innovations:

1. **Minimal initialization** — start with the simplest possible network (all inputs directly connected to outputs, no hidden nodes)
2. **Structural mutation** — add nodes and connections incrementally, growing complexity as needed
3. **Historical markings (Innovation Numbers)** — assign a globally unique ID to each structural mutation, enabling meaningful crossover between different topologies by aligning genes
4. **Speciation** — group similar topologies into species using a distance metric; fitness sharing within species protects new structural innovations from premature elimination

---

## 🔄 机制与推导（How It Works）

### GA Core Algorithm (Pseudocode)

```
GENETIC_ALGORITHM(N, fitness_fn, max_generations):
    population = initialize_random(N)

    for gen = 1 to max_generations:
        scores = [fitness_fn(ind) for ind in population]

        // Selection
        parents = select_fittest(population, scores)

        // Elitism: copy top-k directly
        next_gen = top_k(population, scores)

        // Crossover
        while |next_gen| < N:
            p1, p2 = random_pair(parents)
            if random() < crossover_rate:
                child = crossover(p1, p2)
            else:
                child = copy(p1)

            // Mutation
            if random() < mutation_rate:  // typically 0.01 or 0.001
                mutate(child)

            next_gen.add(child)

        population = next_gen

    return best(population)
```

### NEAT Genome Encoding — Detailed

**Node Genes Table:**

| Node ID | Type |
|---|---|
| 1 | Sensor (Input) |
| 2 | Sensor (Input) |
| 3 | Sensor (Input) |
| 4 | Output |
| 5 | Hidden |

**Connection Genes Table:**

| In | Out | Weight | Enabled | Innovation# |
|----|-----|--------|---------|-------------|
| 1  | 4   | 0.7    | YES     | 1           |
| 2  | 4   | -0.5   | NO      | 2           |
| 3  | 4   | 0.5    | YES     | 3           |
| 2  | 5   | 0.2    | YES     | 4           |
| 5  | 4   | 0.4    | YES     | 5           |
| 1  | 5   | 0.6    | YES     | 6           |

### NEAT Crossover Algorithm

```
NEAT_CROSSOVER(parent1, parent2):
    // Assume parent1 is fitter (or equal)
    child_genes = []

    for each innovation_number in union(p1.genes, p2.genes):
        if innovation_number in BOTH parents:
            // Matching gene → randomly pick from either parent
            child_genes.add(random_choice(p1.gene, p2.gene))
            // If disabled in either parent, small chance (e.g. 25%) to re-enable
        else if innovation_number only in fitter parent:
            // Disjoint or Excess → inherit from fitter parent
            child_genes.add(fitter_parent.gene)
        else:
            // Only in less fit parent → skip (unless equal fitness → random)
            if equal_fitness:
                child_genes.add(gene) with 50% probability

    return child_genes
```

### Speciation Distance Calculation

$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$

**Worked example:**

Genome A: Innovation#s = {1, 2, 3, 4, 5}, weights for matching = {0.5, -0.3, 0.8, -, -}
Genome B: Innovation#s = {1, 2, 3, 6, 7, 8}, weights for matching = {0.7, -0.1, 0.9, -, -, -}

- Matching genes: Inn# 1, 2, 3
- Weight differences: |0.5-0.7|=0.2, |-0.3-(-0.1)|=0.2, |0.8-0.9|=0.1
- $\overline{W}$ = (0.2 + 0.2 + 0.1) / 3 = 0.167
- Disjoint: Inn# 4, 5 (in A, within B's range 1-8) and Inn# 6, 7 (in B, within A's range 1-5... actually 6,7 > 5, so these are excess)
- Corrected: D = 2 (Inn# 4, 5 from A), E = 3 (Inn# 6, 7, 8 from B)
- N = max(5, 6) = 6

With $c_1 = 1.0, c_2 = 1.0, c_3 = 0.4$:

$$\delta = \frac{1.0 \times 3}{6} + \frac{1.0 \times 2}{6} + 0.4 \times 0.167 = 0.5 + 0.333 + 0.067 = 0.9$$

If $\delta_t = 1.0$, then $\delta = 0.9 < 1.0$ → **same species**.

### Adjusted Fitness Formula

$$f'_i = \frac{f_i}{|S|}$$

**Species quota allocation:**

$$\text{quota}(S) = \frac{\sum_{i \in S} f'_i}{\sum_{\text{all species } S'} \sum_{j \in S'} f'_j} \times N$$

---

## ⚖️ 权衡分析（Trade-offs & Comparisons）

### GA vs. Traditional Search Methods

| Dimension | GA | Traditional (BFS/DFS/Gradient) |
|---|---|---|
| Search space | Suited for **vast, complex** spaces | Suited for structured, smaller spaces |
| Prior knowledge | Needs a well-designed fitness function | Needs known search direction or differentiable objective |
| Optimality guarantee | No guarantee of global optimum, but usually good | BFS/DFS can guarantee; gradient may find local optima |
| Parallelism | Naturally parallel (independent evaluation) | Usually sequential |
| Gradient requirement | **None** — works on non-differentiable problems | Gradient descent requires differentiable loss |
| Applications | Scheduling, routing, game AI, protein folding | Supervised learning, pathfinding, constraint satisfaction |

### NEAT vs. Traditional Neural Network Training (Backpropagation)

| Dimension | NEAT | Backpropagation |
|---|---|---|
| What it optimizes | Structure **AND** weights | **Only** weights (fixed architecture) |
| Starting state | Minimal network, grows incrementally | Pre-defined architecture (must be designed by human) |
| Gradient requirement | Not needed | Requires differentiable loss function |
| Typical use case | RL, control, game AI | Supervised learning with labeled data |
| Network size produced | **Small and interpretable** | Usually large (hundreds of layers) |
| Training speed | Slower (many generations needed) | Faster (gradient is efficient) |
| Architecture search | Built-in (via structural mutation) | Must use separate NAS methods |

### NEAT's Four Innovations — What Each Solves

| Innovation | Problem It Solves | What Happens Without It (Ablation) |
|---|---|---|
| Minimal initialization | Avoids searching unnecessarily large structure space | Search is inefficient, convergence is slow |
| Structural mutation | Allows complexity to grow on-demand | Can only optimize fixed structure |
| Innovation Numbers | Enables meaningful crossover between different topologies | Crossover destroys good structures (misalignment) |
| Speciation | Protects new structures from premature elimination | New innovations die before their weights can be optimized |

### When to Use GA vs. When Not To

| Use GA When | Don't Use GA When |
|---|---|
| Search space is vast and unstructured | Problem has smooth, differentiable objective |
| No gradient information available | Labeled data available for supervised learning |
| Multiple conflicting objectives | Real-time training speed required |
| Need to explore diverse solution space | Solution space is small enough for exhaustive search |
| Problem is combinatorial (scheduling, routing) | Standard optimization works well |

---

## 🏗️ 设计题答题框架

> **This is the most exam-critical section.** The professor has asked "design a fitness function" in every recent exam.

### Framework: WHAT → WHY → HOW → TRADE-OFF → EXAMPLE

**1. WHAT (Define):**
"NEAT is a neuroevolution method that evolves both the topology and weights of neural networks using a genetic algorithm."

**2. WHY (Justify choosing NEAT):**
"NEAT is suitable for this problem because: [choose applicable reasons]
- No differentiable loss function exists (e.g., survival time, game score)
- The optimal network structure is unknown
- The task is a reinforcement learning / control problem
- We want small, interpretable networks
- The search space is too large for manual architecture design"

**3. HOW (Specific design — the part that earns marks):**

- **Inputs:** Define what sensor data the network receives
- **Outputs:** Define what actions the network produces
- **Fitness function:** **THIS IS THE KEY** — define exactly how each individual is scored
- **Population size:** Typically 150-300
- **Mutation rates:** Add node ~0.03, add connection ~0.05, weight mutation ~0.8
- **Speciation parameters:** $c_1, c_2, c_3, \delta_t$

**4. TRADE-OFF:**
- Pros: No gradient needed, evolves minimal networks, finds creative solutions, good for RL
- Cons: Computationally expensive, many hyperparameters, not suitable for large-scale supervised learning

**5. EXAMPLE:**
- Game AI (Flappy Bird, Pac-Man, Monopoly)
- Robot control (pole balancing, locomotion)
- Configuration optimization

### Fitness Function Design Template (EXAM CRITICAL)

When designing a fitness function, follow this structure:

```
Fitness = w₁ × (primary_objective) + w₂ × (secondary_objective) - w₃ × (penalty)

Where:
- primary_objective: The main goal (e.g., distance traveled, time survived)
- secondary_objective: Secondary desirable properties (e.g., efficiency, smoothness)
- penalty: Things to avoid (e.g., collisions, instability)
- w₁, w₂, w₃: Weights balancing the objectives
```

**Fitness should be HIGHEST when all differences from the target are LOW.**

---

## 📝 历年真题 & 标准答案

### S1 2025 Actual Q6 (3 marks): BigDog Fitness Function

**Question:** Design a fitness function for a BigDog walking robot trained using a Genetic Algorithm.

**Full-marks answer:**

> The fitness function should evaluate how well a candidate solution (a set of leg control parameters or a neural network controller) enables BigDog to walk correctly. The fitness function considers multiple components measured across a simulation:
>
> **Fitness = - w₁ |target_speed - actual_speed| - w₂ |target_direction - actual_direction| - w₃ |target_height - actual_height| - w₄ (pitch_deviation + yaw_deviation + roll_deviation)**
>
> Where:
> - **|target_speed - actual_speed|**: Penalizes deviation from desired walking speed
> - **|target_direction - actual_direction|**: Penalizes deviation from desired heading
> - **|target_height - actual_height|**: Penalizes the body being too high or too low (should maintain stable torso height)
> - **pitch/yaw/roll deviations**: Penalizes the body tilting or rotating away from the upright orientation — these must stay within bounds
>
> **Highest fitness** is achieved when ALL differences are simultaneously low across the entire simulation. The fitness is evaluated over many time steps to ensure consistent walking, not just a single snapshot.
>
> Additional components could include:
> - Energy efficiency (lower force usage preferred)
> - Smoothness of gait transitions
> - Penalty for foot slippage

**Key exam tip:** The professor wants you to list **specific measurable quantities** with clear reasoning for each. Generic answers like "fitness = how well it walks" score 0-1 marks. You need concrete variables.

### S1 2024 Final Q6: NEAT for Mobile Robot

**Question (a):** Describe an application of NEAT for a mobile robot.

**Answer:**

> NEAT can be applied to evolve a neural network controller for **autonomous obstacle avoidance** in a mobile robot. The robot has sensors (e.g., LIDAR, ultrasonic, infrared) that measure distances to nearby objects. These sensor readings form the **inputs** to the neural network. The **outputs** are motor control signals (e.g., left wheel speed, right wheel speed).
>
> NEAT evolves a population of neural networks. Each network is evaluated by running the robot in a simulation environment. The **fitness function** measures how far the robot travels without hitting obstacles, or how efficiently it reaches a target position. Over many generations, NEAT selects high-performing networks, crosses over their genomes using innovation numbers, and applies structural mutations (adding nodes and connections). The result is a small, evolved neural network that controls the robot effectively — and because NEAT starts minimal, the final network is often **interpretable** and **efficient**.

**Question (b):** What is a time-consuming aspect of training or tuning NEAT?

**Answer:**

> **Designing and tuning the fitness function** is the most time-consuming aspect. The fitness function is the sole guide for evolution, and a poorly designed one can lead to degenerate behaviors. For example, if the fitness function only rewards distance traveled, the robot might learn to spin in circles (maximizing wheel rotations without actual forward progress). Iteratively adjusting the fitness function, running simulation experiments, and verifying that evolved behaviors match real-world requirements demands significant **domain knowledge**, **experimentation time**, and **debugging effort**.
>
> Additional time-consuming aspects include: tuning speciation parameters ($c_1, c_2, c_3, \delta_t$), choosing appropriate mutation rates, and running enough generations for convergence (each generation requires evaluating every individual in simulation).

### S1 2025/2026 Sample Q4 (2m): Robot Soccer

**Question:** Design a strategy for a robot soccer team with an overhead camera and no inter-robot communication.

**Answer:** (See H_multiagent chapter for full answer — this is a cross-topic question.)

> Any of the following strategies work because the **overhead camera gives all robots the same shared information**:
>
> 1. **Collective behaviours (passing)**: Evaluate passing points based on interception prediction; each robot independently calculates the best passing option using the shared overhead view.
> 2. **Positioning strategies (formations)**: Assign formation positions (e.g., 2-1-2) based on ball location; each robot moves to its assigned position using the shared view.
> 3. **Role-based strategies**: Dynamically assign roles (attacker, defender, goalkeeper) based on the current game state; since all robots see the same overhead view, they can independently compute the same role assignments without communication.
>
> All three work because the overhead camera provides a **shared global percept** — no communication is needed if every robot can see the same game state.

### Lecture Quiz Questions

**Q1.** What is the main purpose of mutation in a GA?
- **B. Introduce new variations into the population** ✅
- (Not "preserve best" = elitism, not "select fittest" = selection)

**Q2.** What is the advantage of adding a recurrent connection in NEAT?
- **B. It allows the network to remember past information** ✅
- (Critical for double pole balancing without velocity inputs)

**Q3.** What is the purpose of speciation in NEAT?
- **B. To protect new structures from being eliminated too early** ✅

---

## 🌐 英语表达要点（English Expression Tips）

### Describing GA

```
- "Genetic Algorithms search for solutions by simulating the process of natural selection."
- "Each individual in the population represents a candidate solution encoded as a chromosome."
- "The fitness function evaluates how close each individual is to the ideal solution."
- "Crossover combines genetic material from two parents to create offspring."
- "Mutation introduces random variations to maintain diversity in the population."
- "Elitism ensures the best solutions are preserved across generations."
- "GA is particularly effective for vast search spaces where exhaustive search is impractical."
```

### Describing NEAT

```
- "NEAT evolves both the topology and weights of neural networks simultaneously."
- "Starting from minimal structures, NEAT incrementally adds complexity through structural mutations."
- "Innovation numbers serve as historical markers that enable meaningful crossover between networks with different topologies."
- "Speciation protects structural innovations by grouping similar individuals and allowing them to compete only within their group."
- "Adjusted fitness prevents large species from dominating the population by dividing each individual's fitness by the species size."
- "NEAT produces small, interpretable networks — unlike deep learning, which produces large black-box models."
```

### Describing Fitness Function Design

```
- "The fitness function should reward [desired behavior] and penalize [undesired behavior]."
- "Fitness is highest when all deviations from the target are simultaneously low."
- "The fitness is evaluated over many time steps to ensure consistent performance."
- "A well-designed fitness function balances multiple competing objectives using weighted terms."
```

### 易混淆词汇

| Often Confused | Distinction |
|---|---|
| **Genotype vs Phenotype** | Genotype = the internal encoding (gene sequence); Phenotype = the expressed result (actual network structure) |
| **Disjoint vs Excess** | Disjoint = non-matching genes WITHIN the other parent's range; Excess = non-matching genes BEYOND the other parent's range |
| **Crossover vs Mutation** | Crossover = recombine two parents' genes; Mutation = randomly alter a single individual's genes |
| **Fitness vs Adjusted Fitness** | Fitness = raw score; Adjusted = fitness / species size (prevents large-species dominance) |
| **Structural vs Weight Mutation** | Structural = change topology (add node/connection); Weight = perturb existing weights only |
| **Innovation Number vs Node ID** | Innovation# = unique ID for a connection gene (structural mutation); Node ID = unique ID for a node |
| **Recurrent vs Feedforward connection** | Recurrent = loops back (output → earlier node), enables memory; Feedforward = only goes forward |
| **GA vs NEAT** | GA = general optimization on any chromosome; NEAT = GA specifically designed to evolve neural network topology + weights |

---

## 🧪 Practice Questions

### Multiple Choice

**Q1.** In NEAT, when a new node is added by mutation, what is the weight of the connection going INTO the new node?

A. 0
B. Random
C. **1.0** ✅
D. Same as the original connection

> Explanation: The connection into the new node has weight 1.0; the connection from the new node keeps the original weight. This preserves the network's pre-mutation behavior: 1.0 × original_weight = original_weight.

---

**Q2.** Which of the following is NOT a key innovation of NEAT?

A. Starting from minimal structures
B. Using innovation numbers for crossover
C. **Using backpropagation for weight training** ✅
D. Speciation to protect new structures

> Explanation: NEAT does NOT use backpropagation. Weights are evolved through crossover and weight mutation, not gradient descent.

---

**Q3.** In NEAT's speciation formula $\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$, what does $\overline{W}$ represent?

A. Total weight of all connections
B. **Average weight difference of matching genes** ✅
C. Maximum weight in the network
D. Number of weight mutations

---

**Q4.** Why does NEAT use adjusted fitness (dividing by species size)?

A. To make computation faster
B. To increase mutation rate in large species
C. **To prevent large species from dominating and give small species a fair chance** ✅
D. To reduce the number of species

---

**Q5.** In a standard GA, what is the typical mutation rate?

A. 50% (0.5)
B. 10% (0.1)
C. **1% or 0.1% (0.01 or 0.001)** ✅
D. 0% (no mutation needed)

> Explanation: Mutation rate is kept LOW to avoid turning GA into random search. It provides diversity while preserving good solutions through crossover.

---

### Short Answer

**Q6.** Explain the difference between Disjoint genes and Excess genes in NEAT crossover. (4 marks)

> When aligning two parent genomes by innovation number during crossover:
>
> - **Disjoint genes** are genes that exist in one parent but not the other, and they fall **within the range** of the other parent's innovation numbers. For example, if Parent 1 has innovation numbers {1,2,3,5} and Parent 2 has {1,2,4,6}, then gene 3 and 5 in Parent 1 and gene 4 in Parent 2 are disjoint genes (since they are all within the other parent's range).
>
> - **Excess genes** are genes that exist in one parent but not the other, and they fall **beyond the range** of the other parent's maximum innovation number. In the above example, gene 6 in Parent 2 is an excess gene (since 6 > max of Parent 1 which is 5).
>
> Both disjoint and excess genes are inherited from the **fitter parent**. If parents have equal fitness, they are inherited randomly. Both contribute to the speciation distance formula, but with potentially different coefficients ($c_1$ for excess, $c_2$ for disjoint).

---

**Q7.** Describe the complete pipeline of NEAT applied to the double pole balancing problem. (6 marks)

> 1. **Initialize** a population of simple neural networks with no hidden nodes. Inputs: cart position, pole angles (and possibly velocities). Output: force direction on the cart.
>
> 2. **Evaluate** each network by running it in the pole balancing simulation. The network reads sensor inputs and outputs a force. Fitness = number of time steps the cart survives while keeping both poles balanced and staying on the track.
>
> 3. **Speciate** the population using the distance formula $\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$. Calculate adjusted fitness = individual fitness / species size.
>
> 4. **Select** high-fitness networks using species-adjusted fitness. Assign breeding quotas proportional to each species' total adjusted fitness.
>
> 5. **Crossover** selected parents by aligning their genomes using innovation numbers. Matching genes inherited randomly; disjoint and excess genes from the fitter parent.
>
> 6. **Mutate** offspring: structural mutations (add node with weight 1.0 incoming, add connection with random weight and next innovation number) and weight mutations. In the harder version (no velocity inputs), recurrent connections may evolve to give the network memory.
>
> 7. **Repeat** for many generations until a network successfully balances both poles indefinitely.

---

**Q8.** What is an ablation study? Describe the ablation experiments performed on NEAT. (5 marks)

> An ablation study evaluates the contribution of individual components by **removing them one at a time** and measuring the performance change.
>
> Stanley & Miikkulainen performed four ablation experiments on NEAT:
>
> 1. **Fixed fully-connected network** (no topology evolution) — performance was worse or failed entirely
> 2. **Starting from a larger-than-minimal network** — convergence was slower
> 3. **Disabling speciation** — new structural innovations were eliminated before their weights could be optimized; performance degraded
> 4. **Disabling crossover** (mutation only) — learning was slower
>
> All ablated versions performed worse than full NEAT. This demonstrates that each innovation — minimal starting topology, structural mutation, speciation, and crossover with innovation numbers — contributes meaningfully and is not redundant.

---

**Q9 (Design Question).** You want to use NEAT to evolve a controller for a drone that must fly through a series of hoops. Design the system. (6 marks)

> **Inputs (sensors):**
> - Distance and angle to the next hoop (2 values)
> - Current velocity (x, y, z components = 3 values)
> - Current orientation (pitch, roll = 2 values)
> - Distance to ground (1 value)
>
> **Outputs (actions):**
> - Thrust magnitude
> - Roll adjustment
> - Pitch adjustment
>
> **Fitness function:**
>
> Fitness = w₁ × (number of hoops passed) + w₂ × (1 / total_time) - w₃ × |deviation_from_center_of_hoop| - w₄ × (number_of_crashes)
>
> Highest fitness when: many hoops passed quickly, through the center, without crashing.
>
> **NEAT configuration:**
> - Population: 200 individuals
> - Start minimal: 8 inputs directly connected to 3 outputs, no hidden nodes
> - Structural mutation rates: add node ~0.03, add connection ~0.05
> - Weight mutation rate: ~0.8 (with 10% chance of random new weight vs. perturbation)
> - Speciation: $c_1 = 1.0, c_2 = 1.0, c_3 = 0.4, \delta_t = 3.0$
>
> **Why NEAT over backpropagation?** The fitness function (hoops passed, crash avoidance) is not differentiable. There's no labeled dataset. This is a reinforcement learning scenario where NEAT's gradient-free optimization is ideal.

---

## ✅ 自测检查清单

- [ ] Can I define GA in one English sentence?
- [ ] Can I define NEAT in one English sentence?
- [ ] Can I list the 5 steps of the GA pipeline? (Init → Fitness → Select → Crossover → Mutate)
- [ ] Can I explain both types of crossover (single-point and uniform)?
- [ ] Can I explain elitism and why it matters?
- [ ] Can I draw NEAT's two structural mutations (Add Node, Add Connection)?
- [ ] Can I explain why Add Node uses weight 1.0 for the incoming connection?
- [ ] Can I explain what Innovation Numbers are and why they're needed for crossover?
- [ ] Can I distinguish Disjoint from Excess genes with an example?
- [ ] Can I write the speciation distance formula and explain every symbol?
- [ ] Can I explain Adjusted Fitness and calculate it with numbers?
- [ ] Can I explain why speciation protects innovation?
- [ ] Can I describe the double pole balancing task and NEAT's pipeline for it?
- [ ] Can I describe all four ablation experiments and their results?
- [ ] Can I design a fitness function for a new problem (BigDog, mobile robot, drone)?
- [ ] Can I list at least 4 GA application domains?
- [ ] Can I explain when to use NEAT vs. backpropagation?

---

## 📚 Key References

- Stanley, K. O. & Miikkulainen, R. (2002). *Evolving neural networks through augmenting topologies.* Evolutionary Computation 10(2).
- Raibert, M. et al. (2008). *BigDog, the rough-terrain quadruped robot.* IFAC Proceedings.

---

*Based on COMPSCI 713 Week 6 Lecture 11 (24 slides) — Instructor: Xinyu Zhang, adapted from Prof. Jim Warren.*
