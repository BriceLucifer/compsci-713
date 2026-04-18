# Decision Trees & Ensemble Methods (Week 4 Lecture 2)

## 🎯 Exam Importance
🔴 **必考** | Sample Test Q5, **3 marks = 15% of total**

Random Forest feature bagging is **directly tested** in Q5. Entropy, Information Gain, and the Bagging vs Boosting distinction are foundational concepts that appear across multiple question types. You must be able to calculate entropy, explain why feature bagging decorrelates trees, and trace through an AdaBoost round with numbers.

---

## 📖 Core Concepts

| English Term | 中文 | One-line Definition |
|---|---|---|
| Decision Tree（决策树） | 决策树 | A tree-structured classifier: internal nodes test features, branches represent values, leaves assign class labels |
| CART（分类回归树） | 分类回归树 | Classification And Regression Trees — always performs **binary** splits, uses Gini impurity |
| Entropy $H(X)$（熵） | 熵 | $H(X) = -\sum p(x) \log_2 p(x)$ — measures impurity/uncertainty in a distribution |
| Conditional Entropy $H(Y\|X)$（条件熵） | 条件熵 | $H(Y\|X) = \sum P(X=x)\,H(Y\|X=x)$ — remaining uncertainty about $Y$ after knowing $X$ |
| Information Gain（信息增益） | 信息增益 | $IG(Y\|X) = H(Y) - H(Y\|X)$ — how much knowing $X$ reduces uncertainty about $Y$ |
| Gini Impurity（基尼不纯度） | 基尼不纯度 | $\text{Gini}(t) = 1 - \sum p_i^2$ — alternative splitting criterion used in CART |
| Pruning（剪枝） | 剪枝 | Removing subtrees/leaf nodes to reduce overfitting |
| Ensemble Method（集成方法） | 集成学习 | Combining multiple weak learners into one strong learner |
| Bagging（自助聚合） | 袋装法 / 自助聚合 | Bootstrap Aggregating — train models independently on bootstrap samples, aggregate by vote/average |
| Bootstrap Sample（自助样本） | 自助样本 | A sample of size $n$ drawn **with replacement** from a dataset of size $n$ |
| Random Forest（随机森林） | 随机森林 | Bagging + feature bagging: at each split, only $\sqrt{p}$ random features are considered |
| Feature Bagging（特征袋装） | 特征袋装 | Randomly selecting a subset of features at each split to decorrelate trees |
| Boosting（提升法） | 提升法 | Sequential training where each new model focuses on errors of previous ones |
| AdaBoost（自适应提升） | 自适应提升 | Adaptive Boosting — re-weights misclassified samples each round, combines weighted weak learners |
| Gradient Boosting（梯度提升） | 梯度提升 | Each new tree fits the residual errors (negative gradients) of the current ensemble |
| XGBoost（极端梯度提升） | 极端梯度提升 | Optimised gradient boosting with regularisation in the objective |
| Weak Learner（弱学习器） | 弱学习器 | A classifier only slightly better than random chance (e.g., a decision stump) |
| Decision Stump（决策桩） | 决策桩 | A decision tree with exactly one split (depth 1) |
| Bias（偏差） | 偏差 | Systematic error from a model too simple to capture the true relationship |
| Variance（方差） | 方差 | Sensitivity to training data — how much the model changes with different samples |

---

## 🧠 Feynman Draft — Learning From Scratch

### The 20 Questions Game

Imagine you are playing the game "20 Questions（20个问题游戏）." Someone thinks of an animal, and you ask yes/no questions to narrow down the answer: "Is it bigger than a cat?" → "Does it live in water?" → "Does it have stripes?" Each question splits the remaining possibilities into two groups, and after enough questions you arrive at the answer.

That is exactly how a **decision tree** works. Each internal node asks a question about one feature (e.g., "Is income > $50K?"). Each branch is the answer (yes/no). Each leaf is the final prediction (e.g., "will repay loan" or "will default").

### What Makes a Good Question?

Not all questions are equally useful. Asking "Is it alive?" when you already know it is an animal is worthless — it does not split anything. The best question is one that reduces your **uncertainty** the most.

**Entropy** measures this uncertainty. Think of it as "how surprised are you, on average, by the outcome?"

- **Fair coin flip**: You have no idea what is coming — maximum surprise. $H = 1$ bit.
- **Biased coin (90% heads)**: You mostly expect heads — less surprise. $H \approx 0.47$ bits.
- **Certain outcome (100% heads)**: No surprise at all. $H = 0$ bits.

**Information Gain** tells you how much a particular question reduces entropy. You always pick the question with the highest Information Gain — the one that tells you the most.

### Toy Entropy Calculation

Suppose you have 10 emails: 6 spam, 4 not-spam.

$$H(Y) = -\frac{6}{10}\log_2\frac{6}{10} - \frac{4}{10}\log_2\frac{4}{10}$$
$$= -0.6 \times (-0.737) - 0.4 \times (-1.322)$$
$$= 0.442 + 0.529 = 0.971 \text{ bits}$$

Now you split on the feature "contains FREE":
- "FREE" group: 5 emails (5 spam, 0 not-spam) → $H = 0$ (pure!)
- "no FREE" group: 5 emails (1 spam, 4 not-spam) → $H = -\frac{1}{5}\log_2\frac{1}{5} - \frac{4}{5}\log_2\frac{4}{5} = 0.722$ bits

Conditional entropy after split:

$$H(Y|X) = \frac{5}{10} \times 0 + \frac{5}{10} \times 0.722 = 0.361 \text{ bits}$$

Information Gain: $IG = 0.971 - 0.361 = 0.610$ bits. This is a great split!

### From One Tree to a Forest — Wisdom of Crowds

A single decision tree is like asking one person for their opinion. That person might be knowledgeable but also biased — they might latch onto irrelevant quirks of their own experience. This is **overfitting**: the tree memorises the training data (high variance).

Now imagine asking 2,048 different people, each of whom:
1. Studied a slightly different version of the material (different **bootstrap samples** of data)
2. Focused on different aspects (different **random subsets of features**)

Then you take a majority vote. Individual errors cancel out. This is **Random Forest（随机森林）** — the "wisdom of crowds" for machine learning.

### Bagging vs Boosting — Two Strategies for Teamwork

![Bagging vs Boosting — parallel vs sequential flow](./figures/07_bagging_boosting.png)

**Bagging（袋装法）** = "parallel teamwork." Everyone works independently on their own slightly different version of the problem. Then you average. Good when each individual is smart but unreliable (high variance).

**Boosting（提升法）** = "sequential coaching." The first person tries, the second person specifically studies the first person's mistakes, the third person studies mistakes that remain, and so on. Good when each individual is weak/simple (high bias).

⚠️ **Common Misconception**: Many students confuse **feature bagging** with **data bagging (bootstrapping)**. They are two separate things that happen together in Random Forest:
- **Data bagging** = each tree trains on a different bootstrap sample of the data (sample with replacement)
- **Feature bagging** = at each split, each tree only considers $\sqrt{p}$ randomly chosen features

Both are needed. Data bagging alone is just "Bagging." Adding feature bagging on top makes it "Random Forest."

💡 **Core Intuition**: Many diverse, slightly-wrong trees vote together to produce one highly accurate prediction — strength through diversity.

---

## 📐 Formal Definitions

### Entropy（熵）

![Entropy curve + Information Gain worked example](./figures/06_entropy_infogain.png)

Entropy measures the average uncertainty (impurity) in a probability distribution:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)$$

Key properties:
- $H(X) \geq 0$ always
- $H(X) = 0$ iff one outcome has probability 1 (complete certainty)
- For binary classification: $H_{\max} = 1$ bit (when $p = 0.5$)
- More classes → higher potential entropy: $H_{\max} = \log_2 k$ for $k$ classes

**Canonical examples:**
- Fair coin: $H = -0.5\log_2(0.5) - 0.5\log_2(0.5) = 0.5 + 0.5 = 1$ bit
- Biased coin ($p=0.9$): $H = -0.9\log_2(0.9) - 0.1\log_2(0.1) = 0.137 + 0.332 = 0.469$ bits

### Conditional Entropy（条件熵）

The remaining uncertainty about $Y$ after observing $X$:

$$H(Y | X) = \sum_{x \in \mathcal{X}} P(X = x)\, H(Y | X = x)$$

Expanded form:

$$H(Y | X) = -\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log_2 p(y | x)$$

This is a **weighted average** of the entropy in each subset created by splitting on $X$.

### Information Gain（信息增益）

$$IG(Y | X) = H(Y) - H(Y | X)$$

- If $X$ tells us nothing about $Y$: $IG = 0$
- If $X$ perfectly determines $Y$: $IG = H(Y)$ (all uncertainty removed)
- Always non-negative: $IG \geq 0$ (knowing something never increases uncertainty)

**Decision tree splitting rule**: At each node, choose the feature $X^*$ that maximises $IG(Y | X^*)$.

### Gini Impurity（基尼不纯度）— Used in CART

$$\text{Gini}(t) = 1 - \sum_{i=1}^{k} p_i^2$$

Where $p_i$ is the proportion of class $i$ at node $t$.

**Interpretation**: Probability that two randomly drawn samples from the node belong to different classes.

**Weighted Gini after a binary split:**

$$\text{Gini}_{\text{split}}(D, A) = \frac{n_1}{n}\,\text{Gini}(D_1) + \frac{n_2}{n}\,\text{Gini}(D_2)$$

**Gini Reduction** = $\text{Gini}(\text{parent}) - \text{Gini}_{\text{split}}$

CART chooses the split that **maximises Gini Reduction**.

**Comparison**: Entropy and Gini give very similar splits in practice. Gini is slightly faster to compute (no logarithm). ID3/C4.5 use entropy; CART uses Gini.

### AdaBoost Algorithm（自适应提升算法）

**Initialise:** $w_i = \frac{1}{N}$ for all $N$ training samples.

**For each round $t = 1, 2, \ldots, T$:**

1. **Train** weak learner $h_t$ using sample weights $\{w_i\}$
2. **Compute weighted error:**
   $$\varepsilon_t = \frac{\sum_{i=1}^{N} w_i \cdot \mathbb{1}[h_t(x_i) \neq y_i]}{\sum_{i=1}^{N} w_i}$$
3. **Compute classifier weight:**
   $$\alpha_t = \frac{1}{2} \ln\left(\frac{1 - \varepsilon_t}{\varepsilon_t}\right)$$
4. **Update sample weights:**
   $$w_i \leftarrow w_i \cdot \exp\left(2\alpha_t \cdot \mathbb{1}[h_t(x_i) \neq y_i]\right)$$
   (Misclassified samples get heavier; correctly classified stay the same or get lighter)

**Final prediction:**
$$H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t\, h_t(x)\right)$$

### Gradient Boosting / XGBoost Objective

Each new tree $f_t$ fits the **residual errors** (pseudo-residuals = negative gradients of the loss):

$$\hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + f_t(x_i)$$

**Objective function (with regularisation):**

$$\mathcal{L} = \sum_{i=1}^{N} \ell(y_i, \hat{y}_i) + \sum_{t=1}^{T} \Omega(f_t)$$

Where $\Omega(f_t) = \gamma T_{\text{leaves}} + \frac{1}{2}\lambda \|w\|^2$ penalises tree complexity.

**Key difference from AdaBoost**: AdaBoost adds one weak rule (typically a stump) per round; Gradient Boosting adds one full tree per round that fits the gradient of the loss function.

---

## 🔄 How It Works — Step by Step

### 1. Building a Decision Tree

**Algorithm (greedy, top-down):**

```
function BuildTree(data D, features F):
    if all samples in D have the same label:
        return LeafNode(that label)
    if F is empty or stopping criterion met:
        return LeafNode(majority label in D)
    
    best_feature = argmax_{X in F} IG(Y | X)
    node = InternalNode(best_feature)
    
    for each value v of best_feature:
        D_v = subset of D where best_feature = v
        node.addChild(v, BuildTree(D_v, F \ {best_feature}))
    
    return node
```

**Important**: This is a **greedy** algorithm. It picks the locally best split at each step. It does NOT guarantee the globally optimal tree — the problem of finding the optimal tree is NP-hard.

### 2. Entropy Calculation — Worked Example

**Lecture example: Coin flip entropy**

Fair coin ($p = 0.5$):
$$H = -0.5 \log_2(0.5) - 0.5 \log_2(0.5) = -0.5 \times (-1) - 0.5 \times (-1) = 0.5 + 0.5 = 1 \text{ bit}$$

Biased coin ($p = 0.9$):
$$H = -0.9 \log_2(0.9) - 0.1 \log_2(0.1)$$
$$= -0.9 \times (-0.152) - 0.1 \times (-3.322)$$
$$= 0.137 + 0.332 = 0.469 \text{ bits}$$

Notice: the more "certain" the outcome, the lower the entropy. A fair coin (maximum uncertainty) has maximum entropy of 1 bit.

### 3. Information Gain — Worked Example

Dataset: 14 samples for "Play Tennis?" — 9 Yes, 5 No.

$$H(Y) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14} = 0.940 \text{ bits}$$

Split on feature "Outlook" with values {Sunny, Overcast, Rain}:

| Outlook | Yes | No | Total | $H$ |
|---|---|---|---|---|
| Sunny | 2 | 3 | 5 | $-\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5} = 0.971$ |
| Overcast | 4 | 0 | 4 | $0$ (pure) |
| Rain | 3 | 2 | 5 | $-\frac{3}{5}\log_2\frac{3}{5} - \frac{2}{5}\log_2\frac{2}{5} = 0.971$ |

$$H(Y|\text{Outlook}) = \frac{5}{14}(0.971) + \frac{4}{14}(0) + \frac{5}{14}(0.971) = 0.694 \text{ bits}$$

$$IG(Y|\text{Outlook}) = 0.940 - 0.694 = 0.246 \text{ bits}$$

Compare with other features. If "Outlook" gives the highest $IG$, it becomes the root split.

### 4. AdaBoost — 3-Round Worked Example (from Lecture)

**Setup**: 10 samples, equal initial weights $w_i = 0.1$.

**Round 1:**
- Train stump $h_1$ → misclassifies 3 samples
- $\varepsilon_1 = 3 \times 0.1 = 0.3$
- $\alpha_1 = \frac{1}{2}\ln\frac{1 - 0.3}{0.3} = \frac{1}{2}\ln\frac{0.7}{0.3} = \frac{1}{2}\ln(2.333) = \frac{1}{2}(0.847) = 0.424$
- Update: misclassified samples get weight multiplied by $e^{2 \times 0.424} = e^{0.847} \approx 2.333$
- New weights: 7 correct samples keep $w = 0.1$; 3 misclassified get $w = 0.1 \times 2.333 = 0.233$
- (After normalisation, misclassified samples now dominate)

**Round 2:**
- Train stump $h_2$ (focuses more on previously misclassified samples)
- $\varepsilon_2 = 0.21$
- $\alpha_2 = \frac{1}{2}\ln\frac{0.79}{0.21} = \frac{1}{2}\ln(3.762) = \frac{1}{2}(1.326) = 0.653$
- Higher $\alpha$ → this learner is more confident and gets more vote weight

**Round 3:**
- $\varepsilon_3 = 0.14$
- $\alpha_3 = \frac{1}{2}\ln\frac{0.86}{0.14} = \frac{1}{2}\ln(6.143) = \frac{1}{2}(1.815) = 0.916$
- Even higher $\alpha$ → even more confident

**Final classifier:**
$$H(x) = \text{sign}(0.424 \cdot h_1(x) + 0.653 \cdot h_2(x) + 0.916 \cdot h_3(x))$$

**Pattern to notice:** As rounds progress, $\varepsilon_t$ decreases (learners get better at the remaining hard cases) and $\alpha_t$ increases (better learners get more vote weight).

### 5. Random Forest Construction

```
function RandomForest(data D, num_trees M, num_features_per_split k):
    forest = []
    for i = 1 to M:
        D_i = BootstrapSample(D)          // sample n points WITH replacement
        T_i = BuildTree(D_i, k)            // at each split, randomly pick k features
        forest.append(T_i)
    return forest

function Predict(forest, x):
    votes = [T_i.predict(x) for T_i in forest]
    return MajorityVote(votes)             // classification
    // or return Average(votes)            // regression
```

**Typical hyperparameters (from lecture):**
- Number of trees: 2,048 (or similar large number)
- Features per split: $k = \sqrt{p}$ where $p$ = total features
  - Example: 225 features → $\sqrt{225} = 15$ features considered at each split

---

## ⚖️ Trade-offs & Comparisons

### Single Tree vs Random Forest vs Gradient Boosting

| Aspect | Single Decision Tree | Random Forest | AdaBoost / XGBoost |
|---|---|---|---|
| **Training** | Greedy, very fast | Parallel (embarrassingly so) | Sequential (cannot parallelise rounds) |
| **Variance** | High (overfits easily) | **Low** (averaging decorrelates) | Low |
| **Bias** | Low (can fit complex boundaries) | Low (same as base tree) | **Very low** (iteratively corrects errors) |
| **Interpretability** | **High** (can visualise) | Low (thousands of trees) | Low |
| **Sensitivity to noise** | High | Moderate (robust via averaging) | **High** (boosting amplifies noisy samples) |
| **Risk of overfitting** | High | Low | Moderate (can overfit with too many rounds) |
| **Typical use** | Simple, explainable models | General-purpose, robust | Kaggle competitions, max accuracy |

### Bagging vs Boosting

| Feature | Bagging | Boosting |
|---|---|---|
| **Training order** | Independent / parallel | Sequential |
| **Sample weighting** | Equal (uniform bootstrap) | Adaptive (misclassified samples upweighted) |
| **Primary effect** | **Reduces variance** | **Reduces bias** |
| **Base learner** | Full decision tree | Usually weak learner (stump) |
| **Combination rule** | Majority vote / average | Weighted vote ($\alpha_t$) |
| **Example algorithms** | Random Forest | AdaBoost, GBM, XGBoost |
| **Risk** | Cannot fix inherent bias of base learner | Can overfit to noise if too many rounds |

### Entropy vs Gini Impurity

| Property | Entropy ($H$) | Gini Impurity |
|---|---|---|
| **Formula** | $-\sum p_i \log_2 p_i$ | $1 - \sum p_i^2$ |
| **Range (binary)** | $[0, 1]$ | $[0, 0.5]$ |
| **Maximum** | At $p = 0.5$ (= 1 bit) | At $p = 0.5$ (= 0.5) |
| **Computation** | Requires logarithm | Only multiplication |
| **Used by** | ID3, C4.5 | CART |
| **In practice** | Very similar splits | Very similar splits |

### The Key Takeaway (exam-critical)

| Strategy | What it does | What it reduces |
|---|---|---|
| **Bagging** | Averages many independent models → stabilises predictions | **Variance** |
| **Boosting** | Sequentially corrects errors → improves accuracy | **Bias** |

---

## 🏗️ Design Question Framework

### If asked: "Explain how Random Forest works and why feature bagging helps."

**WHAT**: "Random Forest is an ensemble method that combines Bagging with Feature Bagging. It creates many decision trees, each trained on a different bootstrap sample of the data. At each split within each tree, only a random subset of $\sqrt{p}$ features is considered."

**WHY**: "A single decision tree is prone to overfitting (high variance). By training many trees on different data subsets and averaging their predictions, we reduce variance. Feature bagging further decorrelates the trees — without it, every tree would select the same dominant feature at the root, making all trees nearly identical and defeating the purpose of ensemble averaging."

**HOW**: "1) Sample $n$ points with replacement from the training data to create a bootstrap sample. 2) Build a decision tree on this sample, but at each node only evaluate $\sqrt{p}$ randomly chosen features and pick the best among those. 3) Repeat for $M$ trees (e.g., 2,048). 4) For a new input, collect predictions from all trees and take the majority vote."

**TRADE-OFF**: "Each individual tree in a Random Forest is slightly less accurate than a single optimised tree (because it does not see all features at every split). However, the diversity gained makes the ensemble as a whole far more accurate and robust. The trade-off is interpretability — a single tree can be visualised and understood, but a forest of 2,048 trees cannot."

**EXAMPLE**: "With 225 features, each tree considers $\sqrt{225} = 15$ features at each split. This ensures that even if one feature is very strong, most trees will not have it available at the root — producing diverse trees."

### If asked: "Compare Bagging and Boosting."

1. **Define both** with one sentence each
2. **State the key difference**: parallel vs sequential, variance reduction vs bias reduction
3. **Give a concrete algorithm** for each: Random Forest (bagging) and AdaBoost (boosting)
4. **Discuss when to use which**: bagging when individual models overfit; boosting when individual models underfit
5. **Mention the risk**: boosting can overfit to noise if run for too many rounds

### If asked: "Compute Information Gain for a given split."

1. **Compute $H(Y)$** for the parent node
2. **Compute $H(Y|X=v)$** for each child node
3. **Compute $H(Y|X)$** as the weighted average
4. **Compute $IG = H(Y) - H(Y|X)$**
5. **Interpret**: "This split reduces uncertainty by ... bits, which is [good/poor]"

---

## 📝 Exam Practice

### Practice Problem 1: Entropy Calculation (2 marks)

**Q**: A dataset has 100 samples: 70 positive, 30 negative. Calculate the entropy $H(Y)$.

<details>
<summary>Click to reveal answer</summary>

$$H(Y) = -\frac{70}{100}\log_2\frac{70}{100} - \frac{30}{100}\log_2\frac{30}{100}$$
$$= -0.7 \log_2(0.7) - 0.3 \log_2(0.3)$$
$$= -0.7 \times (-0.515) - 0.3 \times (-1.737)$$
$$= 0.360 + 0.521 = 0.881 \text{ bits}$$

This is less than 1 bit (maximum for binary), reflecting the imbalance toward positive class.

</details>

### Practice Problem 2: Information Gain (3 marks)

**Q**: Given 8 samples for "Buy Computer?" — 5 Yes, 3 No. Splitting on "Student?" gives:
- Student=Yes: 4 samples (3 Yes, 1 No)
- Student=No: 4 samples (2 Yes, 2 No)

Calculate the Information Gain of splitting on "Student?"

<details>
<summary>Click to reveal answer</summary>

**Step 1**: Parent entropy:
$$H(Y) = -\frac{5}{8}\log_2\frac{5}{8} - \frac{3}{8}\log_2\frac{3}{8} = -0.625(-0.678) - 0.375(-1.415) = 0.424 + 0.530 = 0.954 \text{ bits}$$

**Step 2**: Child entropies:
$$H(Y|\text{Student}=\text{Yes}) = -\frac{3}{4}\log_2\frac{3}{4} - \frac{1}{4}\log_2\frac{1}{4} = 0.311 + 0.500 = 0.811 \text{ bits}$$
$$H(Y|\text{Student}=\text{No}) = -\frac{2}{4}\log_2\frac{2}{4} - \frac{2}{4}\log_2\frac{2}{4} = 0.5 + 0.5 = 1.0 \text{ bit}$$

**Step 3**: Conditional entropy:
$$H(Y|\text{Student}) = \frac{4}{8}(0.811) + \frac{4}{8}(1.0) = 0.406 + 0.500 = 0.906 \text{ bits}$$

**Step 4**: Information Gain:
$$IG = 0.954 - 0.906 = 0.048 \text{ bits}$$

This is a very small gain — "Student?" is a weak splitting feature here.

</details>

### Practice Problem 3: Feature Bagging in Random Forest (Q5-style, 3 marks)

**Q**: A Random Forest is built on a dataset with 225 features.

(a) [2 marks] Describe how feature bagging works in Random Forest.

(b) [1 mark] Explain why feature bagging is beneficial.

<details>
<summary>Click to reveal answer</summary>

**(a)** Feature bagging means that at each split in each tree, instead of evaluating all 225 features, only a random subset of features is considered. Typically, $\sqrt{p} = \sqrt{225} = 15$ features are sampled (with replacement) for each split. A large number of trees (e.g., 2,048) are constructed, each using different random feature subsets at every node. The final prediction is made by majority vote across all trees.

**(b)** Feature bagging is beneficial because it **decorrelates the trees** in the ensemble. Without feature bagging, if one feature is much stronger than the others, every tree would select it at the root node, making all trees highly similar. Averaging correlated predictions provides little variance reduction. By forcing each tree to consider different features, the trees become structurally diverse, and their averaged prediction is much more robust and accurate.

</details>

### Practice Problem 4: AdaBoost Weight Calculation (2 marks)

**Q**: In round 1 of AdaBoost with 10 equally-weighted samples, the weak learner misclassifies 3 samples. Calculate $\alpha_1$ and describe what happens to the misclassified samples' weights.

<details>
<summary>Click to reveal answer</summary>

Weighted error: $\varepsilon_1 = 3 \times 0.1 = 0.3$

Classifier weight:
$$\alpha_1 = \frac{1}{2}\ln\frac{1 - 0.3}{0.3} = \frac{1}{2}\ln(2.333) = \frac{1}{2}(0.847) = 0.424$$

Weight update for misclassified samples:
$$w_i^{\text{new}} = 0.1 \times e^{2 \times 0.424} = 0.1 \times e^{0.847} = 0.1 \times 2.333 = 0.233$$

The 3 misclassified samples now have weight 0.233 each (vs 0.1 for correct ones). After normalisation, the next weak learner will "pay more attention" to these harder samples.

</details>

### Practice Problem 5: Bagging vs Boosting Conceptual (2 marks)

**Q**: Explain the key difference between Bagging and Boosting in terms of what type of error each method primarily reduces.

<details>
<summary>Click to reveal answer</summary>

**Bagging** (e.g., Random Forest) primarily reduces **variance**. It trains multiple models independently on bootstrap samples and averages their predictions. Averaging independent (or decorrelated) estimates reduces the fluctuations caused by different training sets.

**Boosting** (e.g., AdaBoost, XGBoost) primarily reduces **bias**. It trains models sequentially, with each new model focusing on the errors of the previous ensemble. This iterative error correction allows the ensemble to learn complex patterns that a single weak learner would miss.

**Summary**: Bagging stabilises (reduces variance); Boosting sharpens (reduces bias).

</details>

---

## 🌐 English Expression Tips

### Describing Decision Trees

```
"A decision tree is a hierarchical model where each internal node tests
 a feature, each branch represents a feature value, and each leaf node
 assigns a class label."

"At each node, the algorithm greedily selects the feature that maximises
 information gain, defined as IG(Y|X) = H(Y) - H(Y|X)."

"CART performs binary splits and uses Gini impurity: Gini(t) = 1 - Σ pᵢ²."
```

### Describing Entropy and Information Gain

```
"Entropy measures the average uncertainty in a distribution. High entropy
 means high impurity; low entropy means the distribution is concentrated."

"Information gain quantifies how much a given feature reduces our
 uncertainty about the target variable."

"The feature with the highest information gain is chosen as the splitting
 criterion at each node."
```

### Describing Feature Bagging

```
"For each tree in the forest, at each split point, a random subset of
 features — typically of size √p — is sampled, and only these features
 are evaluated as potential splits."

"Feature bagging reduces the correlation between trees, which is essential
 because averaging highly correlated predictions provides little benefit."
```

### Comparing Bagging and Boosting

```
"Bagging trains classifiers independently on bootstrap samples and
 aggregates their predictions by majority vote, primarily reducing variance."

"Boosting trains classifiers sequentially, with each new learner assigning
 higher weight to previously misclassified examples, primarily reducing bias."

"The fundamental distinction is: bagging operates in parallel and targets
 variance, while boosting operates sequentially and targets bias."
```

### Describing AdaBoost

```
"AdaBoost maintains a weight distribution over training samples. In each
 round, it trains a weak learner, computes the weighted classification
 error, and assigns a coefficient α proportional to the learner's accuracy."

"Misclassified samples receive increased weight, causing subsequent learners
 to focus more heavily on these difficult examples."

"The final prediction is a weighted majority vote: H(x) = sign(Σ αₜ hₜ(x))."
```

### Common Errors to Avoid

- ❌ "Bagging reduces bias" → ✅ "Bagging reduces **variance**"
- ❌ "Boosting reduces variance" → ✅ "Boosting reduces **bias**"
- ❌ "Feature bagging means training on different data" → ✅ "Feature bagging means considering different **features** at each split; data sampling (bootstrapping) is separate"
- ❌ "Random Forest = Bagging" → ✅ "Random Forest = Bagging + Feature Bagging"
- ❌ "Information Gain can be negative" → ✅ "Information Gain is always $\geq 0$"
- ❌ "Gradient Boosting uses decision stumps" → ✅ "AdaBoost typically uses stumps; Gradient Boosting uses full trees that fit residuals"

---

## ✅ Self-Test Checklist

- [ ] Can you define entropy, conditional entropy, and information gain with formulas?
- [ ] Can you compute $H(Y)$ for a binary distribution by hand?
- [ ] Can you compute $IG$ for a given feature split?
- [ ] Can you explain the greedy tree-building algorithm?
- [ ] Do you know why a single decision tree overfits (high variance, greedy, not globally optimal)?
- [ ] Can you explain the 3 steps of Bagging: bootstrap → train → aggregate?
- [ ] Do you know Random Forest = Bagging + Feature Bagging?
- [ ] Can you explain **why** feature bagging decorrelates trees (and why that matters)?
- [ ] Given 225 features, do you know $\sqrt{225} = 15$ features per split?
- [ ] Do you know: Bagging reduces **variance**, Boosting reduces **bias**?
- [ ] Can you trace through one round of AdaBoost: compute $\varepsilon_t$, $\alpha_t$, and weight update?
- [ ] Do you know the difference between AdaBoost (adds stumps) and Gradient Boosting (fits residuals with trees)?
- [ ] Can you write the AdaBoost final classifier: $H(x) = \text{sign}(\sum \alpha_t h_t(x))$?
- [ ] Can you draw a decision tree diagram with internal nodes, branches, and leaves?
- [ ] Can you explain Gini impurity and how it differs from entropy?
