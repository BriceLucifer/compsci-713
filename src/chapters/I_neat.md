# NEAT — NeuroEvolution of Augmenting Topologies（神经进化增强拓扑）

## 🎯 考试重要度

🟠 高频 | Week 6 Lecture 11 专题 | 属于 Soft Computing 大类，与 GA 强关联

> 本章涵盖 **Genetic Algorithm（遗传算法）** 基础 + **NEAT** 算法细节。考试可能出简答题或设计题。

---

## 📖 核心概念速查（Core Concepts）

| English Term | 中文 | 一句话定义 |
|---|---|---|
| Genetic Algorithm (GA) | 遗传算法 | 模仿达尔文进化论的搜索优化算法 |
| Population | 种群 | 一组候选解（个体）的集合 |
| Chromosome | 染色体 | 一个个体的完整编码（一串基因） |
| Gene | 基因 | 染色体中的最小编码单元 |
| Fitness Function | 适应度函数 | 评估一个个体有多"好"的函数 |
| Selection | 选择 | 挑出表现好的个体进入下一代 |
| Crossover | 交叉 | 两个父代混合基因生成子代 |
| Mutation | 变异 | 随机改变基因，引入新变化 |
| Elitism | 精英保留 | 最优秀的个体直接进入下一代，不被修改 |
| NEAT | 神经进化增强拓扑 | 用遗传算法**进化**出神经网络的结构和权重 |
| Innovation Number | 创新编号 | NEAT 中每个新结构变异的唯一 ID，用于对齐交叉 |
| Speciation | 物种形成 | 把相似个体分组，保护新结构不被过早淘汰 |
| Ablation Study | 消融实验 | 去掉某个组件，看性能变化，验证该组件的贡献 |

---

## 🧠 费曼草稿（Feynman Draft）— 用大白话讲清楚

### Part 1: 遗传算法 GA — 像养乌龟一样优化

想象你在养一群乌龟赛跑🐢。

**第一代：** 你随机养了 100 只乌龟（Population / 种群），每只乌龟的"基因"不同——有的腿长、有的壳轻、有的肌肉多。

**评估：** 让它们比赛跑步。跑得快的乌龟得高分（Fitness / 适应度）。

**选择：** 你挑出跑得最快的 20 只（Selection / 选择）。

**交叉：** 让这 20 只乌龟两两"配对"，后代继承父母双方的基因。比如一个孩子继承了妈妈的长腿和爸爸的轻壳（Crossover / 交叉）。

**变异：** 偶尔随机改变某个后代的某个基因，比如突然长出更强的肌肉（Mutation / 变异）。概率很低，一般 0.01 ~ 0.001。

**重复：** 用这些后代组成第二代，继续比赛、选择、交叉、变异……

**结果：** 经过很多代以后，你的乌龟会越来越快！🏃

```
整个 GA 流程：

初始化随机种群
    ↓
评估每个个体的 Fitness
    ↓
选择（Selection）高 fitness 个体
    ↓
交叉（Crossover）生成子代
    ↓
变异（Mutation）引入随机性
    ↓
形成新一代 → 回到评估步骤
    ↓
（循环很多代后）得到最优解
```

### Part 2: 染色体、基因到底长啥样？

一个"个体"就是一条染色体（Chromosome），由一串基因（Gene）组成：

```
个体 A1:  [0, 0, 0, 0, 0, 0]  ← 每个格子是一个 Gene
个体 A2:  [1, 1, 1, 1, 1, 1]  ← 整条叫 Chromosome
个体 A3:  [1, 0, 1, 0, 1, 1]
个体 A4:  [1, 1, 0, 1, 1, 0]
      ↑ 所有个体合在一起叫 Population（种群）
```

基因编码什么，取决于问题：
- **回归问题** → 基因可以是特征权重
- **分类问题** → 基因可以表示某些行为的有/无（0/1）
- **游戏/控制** → 基因编码神经网络的连接和权重（这就是 NEAT 的做法！）

### Part 3: 交叉的两种方式

**单点交叉（Single-point Crossover）：**

```
Parent 1:  [A A A A | B B B B]
Parent 2:  [C C C C | D D D D]
                     ↑ 交叉点
Child 1:   [A A A A | D D D D]  ← 左边来自 Parent1，右边来自 Parent2
Child 2:   [C C C C | B B B B]
```

**均匀交叉（Uniform Crossover）：**

```
Parent 1:  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1]
Parent 2:  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
Child:     [1 0 0 0 1 1 0 1 0 1 0 0 1 1 1 0 1]  ← 每个位置随机选一个父代
```

> **精英保留（Elitism）：** 少数最优秀的个体直接"免试"进入下一代，不需要交叉变异。保证最优解不会丢失。

### Part 4: NEAT — 用 GA 来"养"出一个神经网络！

现在到了重头戏。普通 GA 是优化一串数字，NEAT 的想法是：**把神经网络本身当作"个体"来进化！**

想象你是一个建筑师比赛的评委。一开始，每个参赛者只有最简单的设计图（几个输入直接连到输出，没有隐藏层）。然后：

1. **评估**每个设计的性能
2. **选择**好的设计
3. **交叉**好设计的特征
4. **变异**——但这里的变异很特别！

#### NEAT 的两种结构变异（Structural Mutation）

**变异 1 — 添加连接（Add Connection）：**

```
变异前：                   变异后：
    4(输出)                  4(输出)
   / \                     / | \
  /   \                   /  |  \
 1    2    3             1   2    3
(输入)(输入)(输入)           ↑
                          新增连接 3→4
```

- 两个之前没连接的节点之间加一条新边
- 这条新连接获得一个**创新编号（Innovation Number）**和一个**随机权重**
- 甚至可以"回连"（recurrent connection），让网络能记住之前的信息！

**变异 2 — 添加节点（Add Node）：**

```
变异前：1 ---(权重0.7)--→ 4

变异后：1 ---(权重1.0)--→ 5 ---(权重0.7)--→ 4
                         ↑ 新节点！

原来的连接 1→4 被禁用（Disabled）
新连接 1→5 的权重 = 1.0（保证初始行为不变）
新连接 5→4 的权重 = 原来的 0.7
```

> 💡 关键设计：进入新节点的权重设为 1，出去的权重保持原值。这样添加节点后，网络的初始表现**和变异前一样**，不会突然变差！

### Part 5: NEAT 的交叉——创新编号的妙用

普通 GA 交叉很简单，但 NEAT 的网络结构不同怎么办？答案是用**创新编号（Innovation Number）**来对齐！

```
Parent 1 (更强):  [1→4, 2→4, 3→4, 2→5, 5→4]
                   Inn#1 Inn#2 Inn#3 Inn#4 Inn#5

Parent 2 (较弱):  [1→4, 2→4, 3→4, 1→5, 5→4, 3→5]
                   Inn#1 Inn#2 Inn#3 Inn#8 Inn#9 Inn#10
```

**规则：**
- **匹配基因**（两个 parent 都有的 Innovation Number）→ 随机选一个 parent 的
- **Disjoint 基因**（在中间不匹配的）→ 来自**更强的** parent
- **Excess 基因**（在末尾多出来的）→ 来自**更强的** parent
- 如果两个 parent 一样强 → 随机选
- 被禁用的基因有小概率被重新启用

### Part 6: 物种形成（Speciation）— 保护创新

这是 NEAT 最聪明的设计之一！

**问题：** 一个新结构刚出现时，权重还没优化好，表现可能很差。如果和已经优化好的老结构直接竞争，新结构会被立刻淘汰。但也许这个新结构只需要再优化几代就能超越老结构！

**解决方案：** 把相似的个体分成不同的"物种"，让新结构只和同类竞争。

**距离公式（判断两个个体是否属于同一物种）：**

$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$

| 符号 | 含义 |
|---|---|
| $E$ | Excess 基因数量（末尾多出来的） |
| $D$ | Disjoint 基因数量（中间不匹配的） |
| $N$ | 较大基因组的基因总数 |
| $\overline{W}$ | 匹配基因的平均权重差异 |
| $c_1, c_2, c_3$ | 可调参数 |

如果 $\delta < \delta_t$（阈值），两个个体属于同一物种。

**适应度共享（Fitness Sharing）：**

$$\text{adjusted fitness} = \frac{\text{individual fitness}}{\text{species size}}$$

> 举例：Species A 有 5 个个体，原始 fitness 分别是 10, 8, 6, 12, 9。调整后变成 2, 1.6, 1.2, 2.4, 1.8。
>
> Species B 有 2 个个体，fitness 是 10, 8。调整后变成 5, 4。
>
> Species A 总调整 fitness = 9，Species B 总调整 fitness = 9。繁殖配额 1:1。

这样大物种不会垄断资源，小物种（可能包含创新结构）也有机会存活！

### Part 7: 一个完整例子——双杆平衡（Double Pole Balancing）

NEAT 论文中用了一个经典任务来测试：

```
        θ₁    θ₂       ← 两根不同长度的杆子
         |   |
    ┌────┤   ├────┐
    │  ──┼───┼──  │    ← 小车
    └────────────┘
    ←————————————→
        轨道
```

- 小车在有限轨道上移动
- 需要同时平衡两根长度不同的杆子
- **Fitness = 小车存活的时间步数**
- 更难的版本：不给角速度和小车速度作为输入 → 网络需要**自己学会记忆**（用 recurrent connection）

**NEAT 的 Pipeline：**

```
初始化简单神经网络种群（输入直连输出）
    ↓
每个网络控制小车（输出力的方向）
    ↓
运行模拟，测量 fitness（存活时间）
    ↓
选择高 fitness 的网络
    ↓
交叉 + 变异（添加节点/连接）
    ↓
形成新一代（网络逐渐变复杂）
    ↓
重复很多代
    ↓
进化出能平衡杆子的网络！
```

⚠️ **Common Misconception / 常见误解：**

> 很多同学以为 NEAT 一开始就有复杂的隐藏层。**错！** NEAT 从最简单的结构开始（输入直连输出，没有隐藏节点），复杂度通过变异**逐渐增长**。这是 NEAT 的核心设计哲学——**从简单开始，按需增长复杂度（complexify incrementally）**。

### Part 8: 消融实验（Ablation Study）

NEAT 的作者做了消融实验来证明每个组件都有用：

| 消融条件 | 结果 |
|---|---|
| 使用固定的全连接网络（不进化结构） | 更慢 / 失败 |
| 从较大网络开始（而不是最简结构） | 更慢 |
| 去掉物种形成（Speciation） | 更慢 / 失败 |
| 去掉交叉（只用变异） | 更慢 |

**结论：** NEAT 的四个创新——最小化起始、结构变异、历史标记（Innovation Number）、物种形成——**缺一不可**。

💡 **Core Intuition / 核心直觉：**

> NEAT = 用进化的方式，从最简单的网络开始，同时优化网络的**结构**和**权重**，通过物种形成保护创新结构。

---

## 📐 正式定义（Formal Definition）

**Genetic Algorithm（遗传算法）：** A class of optimization algorithms inspired by Darwin's theory of evolution. A population of candidate solutions evolves over generations through selection, crossover, and mutation, guided by a fitness function.

**NEAT（NeuroEvolution of Augmenting Topologies）：** A genetic algorithm that evolves both the topology (structure) and weights of neural networks. Key innovations:

1. **Minimal initialization** — start with simplest possible network (inputs directly connected to outputs)
2. **Structural mutation** — add nodes and connections incrementally
3. **Historical markings** — innovation numbers enable meaningful crossover between different topologies
4. **Speciation** — protect new structural innovations from premature elimination

---

## 🔄 机制与推导（How It Works）

### GA 核心流程

```
Step 1: Initialize   → 随机生成 N 个个体
Step 2: Evaluate      → 用 fitness function 评估每个个体
Step 3: Select        → 选出高 fitness 的个体
Step 4: Crossover     → 选出的个体交叉生成子代
Step 5: Mutate        → 以小概率变异子代的基因
Step 6: Replace       → 新一代替换旧一代
Step 7: Repeat        → 回到 Step 2，直到收敛
```

### NEAT Genome 编码

每个 NEAT 个体的"基因组"包含两类基因：

| 类型 | 内容 |
|---|---|
| **Node Genes（节点基因）** | 节点 ID、类型（Sensor / Output / Hidden） |
| **Connection Genes（连接基因）** | In-Node、Out-Node、Weight、Enabled/Disabled、Innovation Number |

示例：

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

### Speciation Distance Formula

$$\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$$

- $\delta < \delta_t$ → same species
- $\delta \geq \delta_t$ → different species

### Adjusted Fitness

$$f'_i = \frac{f_i}{|S|}$$

Where $|S|$ is the number of individuals in species $S$. This prevents large species from dominating.

---

## ⚖️ 权衡分析（Trade-offs & Comparisons）

### GA vs. 传统搜索

| 维度 | GA（遗传算法） | 传统搜索（BFS/DFS/Gradient） |
|---|---|---|
| 搜索空间 | 适合**巨大、复杂**的空间 | 适合结构化、较小的空间 |
| 先验知识 | 需要设计 fitness function | 需要知道搜索方向 |
| 最优性 | 不保证全局最优，但通常很好 | BFS/DFS 可保证，梯度下降可能局部最优 |
| 并行性 | 天然可并行（种群独立评估） | 通常串行 |

### NEAT vs. 传统神经网络训练

| 维度 | NEAT | Backpropagation |
|---|---|---|
| 优化内容 | 结构 **+** 权重 | 仅权重 |
| 起始状态 | 最简网络，逐渐增长 | 预定义结构 |
| 梯度需求 | 不需要梯度 | 需要可微分的 loss |
| 适用场景 | 强化学习、控制、游戏 | 有标签的监督学习 |
| 生成网络大小 | 小而精（可解释） | 通常较大 |
| 训练速度 | 较慢（需要很多代） | 较快（梯度高效） |

### NEAT 四大创新的作用

| 创新 | 解决的问题 | 如果去掉会怎样 |
|---|---|---|
| 最小化起始 | 避免搜索过大的结构空间 | 搜索效率低，收敛慢 |
| 结构变异 | 让网络复杂度按需增长 | 只能优化固定结构 |
| Innovation Number | 不同拓扑也能有意义地交叉 | 交叉会破坏好的结构 |
| Speciation | 保护新结构不被过早淘汰 | 创新结构来不及优化就被淘汰 |

---

## 🏗️ 设计题答题框架

> 如果考试出："Design a system using NEAT to solve [某问题]"

### WHAT → WHY → HOW → TRADE-OFF → EXAMPLE

**1. WHAT（定义）：**
"NEAT is a neuroevolution method that evolves both the structure and weights of neural networks using a genetic algorithm."

**2. WHY（为什么选 NEAT）：**
"NEAT is suitable for this problem because [不需要梯度 / 搜索空间大 / 需要同时优化结构 / 强化学习场景]."

**3. HOW（具体设计）：**
- **Genome encoding:** Define what the inputs/outputs are
- **Fitness function:** How to evaluate each network
- **Population size:** Typically 150-300
- **Mutation rates:** Add node ~0.03, add connection ~0.05, weight mutation ~0.8
- **Speciation parameters:** $c_1, c_2, c_3, \delta_t$

**4. TRADE-OFF（权衡）：**
- Pros: Doesn't require gradient, evolves minimal networks, finds creative solutions
- Cons: Computationally expensive, many hyperparameters, not suitable for large-scale supervised learning

**5. EXAMPLE（举例）：**
- Game AI (Flappy Bird, Pac-Man)
- Robot control (pole balancing)
- Configuration optimization

---

## 📝 历年真题 & 可能考法

### 来自 Lecture Quiz 的题目

**Q1.** What is the main purpose of **mutation** in a Genetic Algorithm?
- A. Preserve the best individuals
- B. **Introduce new variations into the population** ✅
- C. Select the fittest individuals

**Q2.** What is the advantage of adding a **recurrent connection** in NEAT?
- A. It reduces the number of nodes
- B. **It allows the network to remember past information** ✅
- C. It speeds up crossover

**Q3.** What is the purpose of **speciation** in NEAT?
- A. To increase mutation rate
- B. **To protect new structures from being eliminated too early** ✅
- C. To reduce population size

### 可能的考试简答题

1. **"Explain the role of Innovation Numbers in NEAT crossover."**
   → Innovation Numbers uniquely identify structural mutations. They allow NEAT to align genes from two parents with different topologies during crossover, distinguishing matching, disjoint, and excess genes.

2. **"Why does NEAT start from minimal structures?"**
   → Starting from minimal structures means NEAT searches through a smaller space initially. Complexity is added only when needed, avoiding the "bloat" problem of unnecessarily complex networks.

3. **"How does speciation protect innovation in NEAT?"**
   → New structures may initially perform poorly because their weights haven't been optimized. Speciation groups similar individuals into species and makes them compete within their group, giving new topologies time to improve before competing with established structures.

---

## 🌐 英语表达要点（English Expression Tips）

### 描述 GA 的常用句式

```
- "Genetic Algorithms search for solutions by simulating the process of natural selection."
- "Each individual in the population represents a candidate solution encoded as a chromosome."
- "The fitness function evaluates how well each individual solves the problem."
- "Crossover combines genetic material from two parents to create offspring."
- "Mutation introduces random variations to maintain diversity in the population."
```

### 描述 NEAT 的常用句式

```
- "NEAT evolves both the topology and weights of neural networks."
- "Starting from minimal structures, NEAT incrementally adds complexity through structural mutations."
- "Innovation numbers serve as historical markers that enable meaningful crossover between different network topologies."
- "Speciation protects structural innovations by grouping similar individuals and allowing them to compete within their group."
- "Adjusted fitness prevents large species from dominating the population."
```

### 易混淆词汇

| 容易搞混的 | 区别 |
|---|---|
| Genotype vs Phenotype | Genotype = 编码（基因序列），Phenotype = 表现型（实际的网络结构） |
| Disjoint vs Excess | Disjoint = 中间不匹配的基因，Excess = 末尾多出来的基因 |
| Crossover vs Mutation | Crossover = 父代基因重组，Mutation = 随机改变 |
| Fitness vs Adjusted Fitness | Fitness = 原始评分，Adjusted = 除以物种大小后的评分 |
| Structural vs Weight Mutation | Structural = 改变拓扑（加节点/边），Weight = 只改权重 |

---

## ✅ 自测检查清单

- [ ] 能用英文一句话定义 GA 和 NEAT？
- [ ] 能画出 GA 的完整流程图？
- [ ] 能解释 NEAT 的两种结构变异（Add Node / Add Connection）？
- [ ] 能解释 Innovation Number 在交叉中的作用？
- [ ] 能写出 Speciation 的距离公式并解释每个符号？
- [ ] 能解释 Adjusted Fitness 的计算方法和目的？
- [ ] 能说出 NEAT 从最简结构开始的原因？
- [ ] 能列举 NEAT 的应用场景？
- [ ] 能解释消融实验的四个条件及结果？

---

## 🎯 GA 应用领域（GA Applications）

- **Configuration and scheduling**（配置与调度优化）
- **Financial portfolio optimization**（金融投资组合优化）
- **Vehicle routing**（车辆路径规划）
- **Protein folding**（蛋白质折叠）
- **Game AI**（游戏 AI，如 Flappy Bird、Pac-Man、Monopoly）

> GA 特别适合**搜索空间巨大**、传统搜索（BFS/DFS）不可行的问题。它能 work 的原因是：通过 fitness function 和 crossover/mutation 的设计，把领域知识嵌入了搜索过程中。

---

## 🧪 课后练习题（Practice Questions）

### 选择题

**Q1.** In NEAT, when a new node is added by mutation, what is the weight of the connection going INTO the new node?

A. 0  
B. Random  
C. **1.0** ✅  
D. Same as the original connection  

> 解析：进入新节点的权重设为 1.0，离开新节点的权重保持原连接的权重值。这样可以保证添加节点后网络的初始行为不变。

---

**Q2.** Which of the following is NOT a key innovation of NEAT?

A. Starting from minimal structures  
B. Using innovation numbers for crossover  
C. **Using backpropagation for weight training** ✅  
D. Speciation to protect new structures  

> 解析：NEAT 不使用反向传播。它通过遗传算法的 crossover 和 mutation 来优化权重。

---

**Q3.** In NEAT's speciation formula $\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$, what does $\overline{W}$ represent?

A. Total weight of all connections  
B. **Average weight difference of matching genes** ✅  
C. Maximum weight in the network  
D. Number of weight mutations  

> 解析：$\overline{W}$ 是两个个体中匹配基因（共有的 Innovation Number）的**平均权重差异**。

---

**Q4.** Why does NEAT use adjusted fitness (dividing by species size)?

A. To make computation faster  
B. To increase mutation rate in large species  
C. **To prevent large species from dominating and give small species a fair chance** ✅  
D. To reduce the number of species  

> 解析：如果不调整，大物种因为个体多，总 fitness 高，会占据更多繁殖名额。调整后每个个体的 fitness 被物种大小稀释，保证小物种也能分到足够的繁殖配额。

---

### 简答题

**Q5.** Explain the difference between Disjoint genes and Excess genes in NEAT crossover. (4 marks)

**参考答案：**

> When aligning two parent genomes by innovation number during crossover:
>
> - **Disjoint genes** are genes that exist in one parent but not the other, and they fall **within the range** of the other parent's innovation numbers. For example, if Parent 1 has innovation numbers [1,2,3,5] and Parent 2 has [1,2,4,6], then gene 3 in Parent 1 and gene 4 in Parent 2 are disjoint genes.
>
> - **Excess genes** are genes that exist in one parent but not the other, and they fall **beyond the range** of the other parent's innovation numbers. In the example above, gene 5 in Parent 1 and gene 6 in Parent 2 are excess genes.
>
> Both disjoint and excess genes are inherited from the **fitter parent**. If parents have equal fitness, they are inherited randomly.

---

**Q6.** Describe the complete pipeline of NEAT applied to the double pole balancing problem. (6 marks)

**参考答案：**

> 1. **Initialize** a population of simple neural networks (inputs directly connected to outputs, no hidden nodes). Inputs: cart position, pole angles. Output: force direction.
>
> 2. **Evaluate** each network by running it in the simulation. The network controls the cart by outputting a force. Fitness = number of time steps survived while keeping both poles balanced and the cart on the track.
>
> 3. **Select** high-fitness networks using species-adjusted fitness scores.
>
> 4. **Crossover** selected parents by aligning their genomes using innovation numbers. Matching genes are inherited randomly; disjoint and excess genes come from the fitter parent.
>
> 5. **Mutate** offspring: structural mutations (add node, add connection) and weight mutations. Recurrent connections may be added to allow the network to detect changes over time (important for the harder version without velocity inputs).
>
> 6. **Speciate** the new generation using the distance formula $\delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \overline{W}$. Assign breeding quotas proportional to each species' adjusted fitness sum.
>
> 7. **Repeat** for many generations until a network successfully balances both poles.

---

**Q7.** What is an ablation study? Describe the ablation experiments performed on NEAT and their findings. (5 marks)

**参考答案：**

> An ablation study is a method of evaluating the contribution of individual components by **removing them one at a time** and comparing performance to the full system.
>
> Stanley & Miikkulainen performed four ablation experiments on NEAT:
>
> 1. **Fixed fully-connected network** (no topology evolution) — slower or failed to learn
> 2. **Starting with a larger-than-minimal network** — slower convergence
> 3. **Disabling speciation** — new innovations eliminated too early, slower or failed
> 4. **Disabling crossover** (mutation only) — slower learning
>
> All ablated versions performed worse than full NEAT, demonstrating that each innovation (minimal starting topology, structural mutation, speciation, and crossover with innovation numbers) contributes meaningfully to NEAT's performance.

---

*本章基于 COMPSCI 713 Week 6 Lecture 11 (Instructor: Xinyu Zhang, adapted from Prof. Jim Warren) 整理。参考文献：Stanley & Miikkulainen (2002) "Evolving neural networks through augmenting topologies."*
