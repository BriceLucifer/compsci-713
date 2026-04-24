# Decision Trees & Ensemble Methods

*COMPSCI 713 -- Lecture 8 (W4L2) | Instructor: Xinyu Zhang*

---

## Exam Priority

**MUST-KNOW** | Appeared in **4/4 available tests** | Typically **2--5 marks per test**

Decision trees and ensemble methods are the single most consistently examined topic in this course. Feature bagging has appeared in every sample and real test. The "greedy" nature of CART appeared in the 2025 real test with a very specific marking rubric. If you study only one topic from this chapter, study feature bagging. If you study two, add CART greedy.

**Exam question inventory:**

| Test | Question | Topic | Marks |
|---|---|---|---|
| 2025 Sample | Q5 | Feature bagging (how + why) | 3 |
| 2025 Real | Q4 | CART greedy | 2 |
| 2025 Real | Q5 | Fuzzy logic (cross-ref, not this chapter) | 3 |
| 2026 Sample | Q5 | Feature bagging (how + why) | 3 |

*(Lec 8 -- W4L2)*

---

## Part 1: What IS a Decision Tree?

### The umbrella analogy

Imagine it is morning and you are deciding whether to bring an umbrella. You might think:

1. "Is it cloudy?" -- If no, leave the umbrella at home.
2. If yes: "Did the weather app say rain?" -- If yes, bring the umbrella.
3. If no: "Is it winter?" -- If yes, bring it just in case. If no, skip it.

You just built a decision tree in your head. It is a chain of yes/no questions, where each answer narrows down what you should do, and at the end you reach a final decision.

A **decision tree（决策树）** is exactly this: a tree-shaped structure of questions about your data, where you start at the top (the root) and follow branches based on the answers until you reach a leaf that gives you a prediction.

### The anatomy of a tree

Every decision tree has three types of nodes:

- **Root node（根节点）**: The very first question. This is the most powerful question -- the one that separates your data the best. Every data point enters here.
- **Internal nodes / Decision nodes（决策节点）**: Follow-up questions. Each one tests a single feature against a threshold (for numbers) or checks a category (for categorical data).
- **Leaf nodes（叶节点）**: The endpoints. No more questions. This is where the tree makes its prediction.

### The fruit example from lectures

The lecture slides show a beautiful example of classifying fruits by their measurements. Let me walk you through it step by step.

*(Lec 8, slides 3--5)*

```
              [width > 6.5cm?]              <-- Root Node
               /            \
             Yes              No
             /                  \
    [height > 9.5cm?]      [height > 6.0cm?]    <-- Internal Nodes
       /       \               /       \
     Yes       No           Yes        No
      |         |             |          |
   Lemon     Orange        Lemon     Orange      <-- Leaf Nodes
```

Suppose a new fruit arrives. It has width = 5.8cm and height = 4.2cm.

1. Start at the root: "Is width > 6.5cm?" -- 5.8 is NOT > 6.5, so go RIGHT.
2. Arrive at: "Is height > 6.0cm?" -- 4.2 is NOT > 6.0, so go RIGHT.
3. Arrive at the leaf: **Orange**.

That is the whole prediction process. You just follow the branches.

The key insight from the lecture slides is that each split carves up the feature space into rectangular regions. The scatter plot on slide 5 shows this visually: the tree's splits correspond to horizontal and vertical lines cutting up the width-height plane.

### Classification vs Regression

*(Lec 8, slide 7)*

There are two flavours of decision tree:

| Type | Output | What goes in the leaf |
|---|---|---|
| **Classification tree** | Discrete class label | The **most common class** among training examples that reach this leaf |
| **Regression tree** | Continuous number | The **mean target value** among training examples that reach this leaf |

In this course, we focus on classification.

### Trees can express ANY Boolean function

*(Lec 8, slide 8)*

This is a fact worth knowing for the exam: for discrete inputs and discrete outputs, decision trees can represent **any** function of the input attributes. The proof is simple -- each row of a truth table maps to one root-to-leaf path. For example, XOR can be represented as a tree even though it is not linearly separable.

For continuous inputs, decision trees can approximate any function arbitrarily closely (though the tree might be absurdly large and overfit terribly).

### Trees can be converted to IF-THEN rules

*(Lec 8, slide 9)*

Every path from root to leaf is equivalent to an IF-THEN rule. For the fruit tree above:

- **Rule 1**: IF width > 6.5 AND height > 9.5 THEN Lemon
- **Rule 2**: IF width > 6.5 AND height <= 9.5 THEN Orange
- **Rule 3**: IF width <= 6.5 AND height > 6.0 THEN Lemon
- **Rule 4**: IF width <= 6.5 AND height <= 6.0 THEN Orange

This connects decision trees to rule-based expert systems (like MYCIN from Lecture 7). The difference is that here, the rules are *learned from data* rather than hand-crafted by experts.

---

## Part 2: How Do We BUILD a Decision Tree? The CART Algorithm

### The fundamental problem

*(Lec 8, slide 12)*

Here is the challenge: you have a dataset with many features, and you need to figure out which feature to split on first, then which feature to split on next, and so on. How do you find the *best* tree?

The bad news: **finding the optimal (smallest/simplest) decision tree is NP-complete** (Hyafil & Rivest, 1976). This means there is no known efficient algorithm that guarantees the best tree. With even a moderate number of features, trying all possible trees would take longer than the age of the universe.

The good news: we can use a **greedy heuristic（贪心启发式）** that works remarkably well in practice.

### The CART algorithm, step by step

**CART** stands for **C**lassification **A**nd **R**egression **T**rees. It was introduced by Leo Breiman and colleagues in 1984. Here is how it works:

*(Lec 8, slides 27--29)*

```
CART Algorithm:
1. Pick an attribute to split at the current node
     -> For EVERY feature, and for EVERY possible split point:
        calculate the impurity reduction
     -> Pick the ONE split that gives the BIGGEST impurity reduction
2. Split the data into child groups based on the chosen split
3. For each child group:
     -> If no examples remain: return the majority class of the parent
     -> If all examples belong to the same class: return that class (pure leaf)
     -> Otherwise: RECURSE -- go back to Step 1 for this child
```

CART always builds **binary trees** -- each split produces exactly two children (left and right). This is different from ID3 which can produce multi-way splits.

### ID3 vs C4.5 vs CART -- the three classic algorithms

*(Lec 8, slide 28)*

Before diving into stopping criteria, it is worth knowing the three classic decision tree algorithms and how they differ:

| Aspect | **ID3** (Quinlan, 1986) | **C4.5** (Quinlan, successor) | **CART** (Breiman, 1984) |
|---|---|---|---|
| Tree type | **Multiway** (one branch per feature value) | Multiway | **Binary** only (always 2 children) |
| Feature types | Categorical only | Categorical + **continuous** (via discretization) | Both categorical + continuous |
| Split criterion | Information Gain | **Gain Ratio** (corrects IG bias toward many-valued features) | **Gini Impurity** (or MSE for regression) |
| Task | Classification only | Classification only | Classification **AND** regression |
| Post-processing | None | Converts tree to **if-then rules** | Supports **pruning** |
| Strategy | Greedy | Greedy | Greedy, no look-ahead |

**For this course**: CART is the focus. But know that ID3 is the historical starting point, C4.5 improved it by handling continuous features and using gain ratio, and CART is the most general (handles regression too, always binary splits).

### Stopping and pruning

*(Lec 8, slides 29)*

The recursion stops according to a **stopping criterion（停止准则）**, such as:
- All examples in the node belong to the same class (pure node)
- A minimum number of examples per leaf is reached
- Maximum tree depth is reached

After building the full tree, we may apply **pruning（剪枝）**: evaluating the effect of removing each leaf node using validation/test data. If deleting a subtree does not hurt (or even improves) performance on held-out data, we keep the simpler version. Pruning yields a simpler tree that is less likely to overfit.

The trade-off is clear: a fully grown tree has low bias but high variance (overfits). Pruning increases bias slightly but reduces variance significantly, usually improving generalization.

---

## Part 3: Why CART Is "Greedy" -- THE Exam Question

> **EXAM ALERT**: This was Question 4 on the 2025 Real Test (2 marks). The marking rubric was very specific about what earns full marks. Read this section carefully.

### What "greedy" means

*(2025 Real Test Q4, marking rubric)*

Let me give you the clearest analogy I can.

Imagine you are driving through an unfamiliar city without GPS. At every intersection, you pick the road that *looks like* it heads most directly toward your destination. You never consider that a small detour now might save you 20 minutes later. You just pick the best-looking option *right now*.

That is exactly what CART does:

1. At the current node, it looks at **ALL possible features** and **ALL possible split points** for each feature.
2. It evaluates how much each possible split would reduce impurity.
3. It picks the split that gives the **maximum impurity reduction RIGHT NOW**.
4. **It does NOT look ahead** to check whether a different split now might lead to better splits in the future.
5. Then it recurses on each child.

### Why "no look-ahead" matters for your exam mark

Here is the marking rubric note from the 2025 Real Test, **word for word**:

> *"Answers that mentioned maximizing impurity reduction but did not mention the lack of looking ahead did not receive full marks. Generally, these responses received 1 mark out of 2, with 1/2 point variance depending on exactly what else was said."*

This means:
- Saying "CART picks the best split at each node" = **1 mark** (incomplete)
- Saying "CART picks the best split at each node **without any look-ahead**" = **2 marks** (full)

The two key phrases the examiner wants are:
1. Evaluates all possible splits and picks the one that maximally reduces impurity
2. **Without any look-ahead** / no effort to craft an optimal tree overall

### Why would a greedy approach fail?

Consider a dataset where:
- Splitting on Feature A at the root gives a small impurity reduction (say 0.05)
- Splitting on Feature B at the root gives a larger impurity reduction (say 0.15)

CART picks Feature B. But what if splitting on Feature A first would have set up the children so that the *next* splits produce almost pure leaves? The overall tree using Feature A first might be smaller and more accurate, but CART never discovers this because **it does not look ahead**.

This is why greedy algorithms do not guarantee the globally optimal tree.

### The full-marks model answer

**Q: "What exactly is meant by saying CART is 'greedy'?" [2 marks]**

> At each node of the decision tree, starting from the root, the algorithm assesses the potential impurity reduction for splitting the training data on each available feature (and for every possible split point for numeric features). The best-performing split is selected **without any look-ahead**. That is the greedy part -- there is no effort to craft an optimal tree overall, just a locally optimal decision regarding the current split. The algorithm is then recursively invoked on each resulting sub-tree.

*(Source: 2025 Real Test official answer, page 4)*

---

## Part 4: Why Not Just Use Accuracy? Entropy and Information Gain

### The accuracy problem

*(Lec 8, slide 13)*

You might think: "Just pick the split that gives the best accuracy." But accuracy can be **misleading**. Here is the exact example from the lectures:

```
Before split:        After split:
    1: 100               Left:         Right:
    0:  49               1: 50         1: 50
                         0:  0         0: 49
```

Before the split, accuracy = 100/149 = 67.1%.
After the split:
- Left child: accuracy = 50/50 = 100%
- Right child: accuracy = 50/99 = 50.5%
- Weighted accuracy = (50/149)(100%) + (99/149)(50.5%) = 67.1%

The accuracy **did not change at all**! Zero accuracy gain. But this split is actually *very useful* -- it created a completely pure left child with 50 class-1 examples and zero class-0 examples. That is progress, but accuracy does not see it.

So we need a better measure of "how good is this split?" We need a measure of **impurity（不纯度）** -- how mixed the classes are in a group.

### Entropy: measuring surprise

*(Lec 8, slides 15--18)*

**Entropy（熵）** comes from information theory. Think of it as measuring how "surprised" you would be by a random draw from a group.

- If a bag contains 100 red balls and 0 blue balls, you already know the next draw will be red. Zero surprise. **Entropy = 0**.
- If a bag is 50 red and 50 blue, every draw is maximally surprising. **Entropy = 1 bit** (for two classes).
- If a bag is 90 red and 10 blue, you are usually not surprised (it is probably red), but occasionally you are. **Entropy is between 0 and 1** -- specifically about 0.47 bits.

The formula:

\\[
H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)
\\]

Key properties:
- \\( H(X) \geq 0 \\) always
- \\( H(X) = 0 \\) when one class has probability 1 (pure node -- we are certain)
- \\( H(X) \\) is maximized when all classes are equally likely (maximum uncertainty)
- For a binary variable, maximum entropy is 1 bit (at p = 0.5)

### Worked example: computing entropy by hand

**Dataset: 10 animals -- 7 cats, 3 dogs.**

\\[
H = -\left(\frac{7}{10} \log_2 \frac{7}{10} + \frac{3}{10} \log_2 \frac{3}{10}\right)
\\]

Let me compute each term:
- \\( \frac{7}{10} = 0.7 \\), and \\( \log_2 0.7 = \frac{\ln 0.7}{\ln 2} \approx \frac{-0.357}{0.693} \approx -0.515 \\)
- So the first term: \\( -0.7 \times (-0.515) = 0.360 \\)
- \\( \frac{3}{10} = 0.3 \\), and \\( \log_2 0.3 \approx \frac{-1.204}{0.693} \approx -1.737 \\)
- So the second term: \\( -0.3 \times (-1.737) = 0.521 \\)

\\[
H = 0.360 + 0.521 = 0.881 \text{ bits}
\\]

This is fairly high entropy (close to the maximum of 1 bit for binary), which makes sense: the split is 70/30, which is not that far from 50/50.

### Conditional Entropy: what if we already know something?

*(Lec 8, slides 20--23)*

Before we get to information gain, we need **Conditional Entropy（条件熵）** -- the entropy of Y *given that we know X*.

Think of it this way: if I tell you whether it is raining, how much uncertainty remains about whether it is cloudy? That "remaining uncertainty" is the conditional entropy.

**Specific conditional entropy** (for one particular value of X):

\\[
H(Y | X = x) = -\sum_{y} p(y|x) \log_2 p(y|x)
\\]

This is just the entropy formula, but using the conditional probabilities \\( p(y|x) \\) instead of \\( p(y) \\).

**Expected conditional entropy** (averaged over all values of X):

\\[
H(Y | X) = \sum_{x} p(x) \cdot H(Y | X = x)
\\]

This is a weighted average of the specific conditional entropies, weighted by how likely each value of X is.

#### Worked example: Raining / Cloudy

*(Lec 8, slides 21--22)*

Suppose we have a dataset relating "Raining" (X) to "Cloudy" (Y):

| | Raining (X=1) | Not Raining (X=0) |
|---|---|---|
| Probability | 1/4 | 3/4 |
| P(Cloudy=yes \| X) | 24/25 | ... |
| P(Cloudy=no \| X) | 1/25 | ... |

**Step 1**: Specific conditional entropy when raining:

\\[
H(Y | \text{raining}) = -\left(\frac{24}{25} \log_2 \frac{24}{25} + \frac{1}{25} \log_2 \frac{1}{25}\right) \approx 0.24 \text{ bits}
\\]

This is very low -- if it is raining, we are almost certain it is cloudy. Not much surprise.

**Step 2**: Compute \\( H(Y | \text{not raining}) \\) similarly (this will be higher, since without rain the cloudiness is less predictable).

**Step 3**: Expected conditional entropy:

\\[
H(Y | X) = \frac{1}{4} \times H(Y|\text{raining}) + \frac{3}{4} \times H(Y|\text{not raining}) \approx 0.75 \text{ bits}
\\]

#### Key properties of conditional entropy

- **Non-negative**: \\( H(Y|X) \geq 0 \\) always.
- **Chain rule**: \\( H(X, Y) = H(X) + H(Y|X) \\).
- **Independence**: If X and Y are independent, knowing X tells us nothing, so \\( H(Y|X) = H(Y) \\).
- **Perfect knowledge**: If X completely determines Y, then \\( H(Y|X) = 0 \\) -- no remaining uncertainty.
- **Self-conditioning**: \\( H(Y|Y) = 0 \\) -- if you already know Y, there is zero surprise left.

> **💡 Core Intuition**: Conditional entropy measures how much uncertainty about Y *remains* after we learn X. The lower it is, the more informative X is about Y.

---

### Information Gain: how much does a split help?

*(Lec 8, slides 24--26)*

**Information Gain（信息增益）** measures how much entropy *decreases* after a split. It is defined as:

\\[
\text{IG}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)
\\]

In words: Information Gain = (entropy before split) - (weighted average of entropy in children).

We pick the feature with the **highest information gain**.

### Worked example: computing information gain

Continuing the cats/dogs example. Suppose we split on "Has whiskers?":

- **Yes group**: 7 cats, 1 dog (8 total) -- \\( H_{\text{yes}} = -(7/8 \log_2 7/8 + 1/8 \log_2 1/8) \approx 0.544 \\)
- **No group**: 0 cats, 2 dogs (2 total) -- \\( H_{\text{no}} = 0 \\) (pure!)

\\[
\text{IG} = 0.881 - \left(\frac{8}{10} \times 0.544 + \frac{2}{10} \times 0\right) = 0.881 - 0.435 = 0.446 \text{ bits}
\\]

This is a decent information gain. The split reduced uncertainty by about half.

### The lecture's key example: why IG beats accuracy

*(Lec 8, slide 25)*

Going back to the earlier example (100 class-1, 49 class-0):

- Root entropy: \\( H(Y) = -(49/149) \log_2(49/149) - (100/149) \log_2(100/149) \approx 0.91 \\)
- Left child (50 class-1, 0 class-0): \\( H(Y|\text{left}) = 0 \\)
- Right child (50 class-1, 49 class-0): \\( H(Y|\text{right}) \approx 1.0 \\)

\\[
\text{IG} \approx 0.91 - \left(\frac{1}{3} \times 0 + \frac{2}{3} \times 1.0\right) = 0.91 - 0.67 = 0.24 > 0
\\]

Information gain is **positive** even though accuracy gain was zero! This is why we use entropy-based measures instead of accuracy.

### Information Gain as Mutual Information

*(Lec 8, slides 24--25)*

There is a deeper way to think about information gain: **IG measures the mutual information between the feature X and the target Y**.

\\[
\text{IG}(Y | X) = H(Y) - H(Y | X)
\\]

Using the Raining/Cloudy example from above:

\\[
\text{IG}(Y | X) = H(Y) - H(Y | X) \approx 1.0 - 0.75 = 0.25 \text{ bits}
\\]

Two boundary cases are worth memorizing:

- **If X is completely uninformative** (independent of Y): \\( H(Y|X) = H(Y) \\), so \\( \text{IG} = 0 \\). The feature tells us nothing -- no point splitting on it.
- **If X is completely informative** (perfectly determines Y): \\( H(Y|X) = 0 \\), so \\( \text{IG} = H(Y) \\). The feature tells us everything -- maximum possible gain.

These boundary cases give you a quick sanity check on any IG calculation: the value must lie between 0 and \\( H(Y) \\).

### Gini Impurity: a simpler alternative

*(Lec 8, slides 30--32)*

**Gini Impurity（基尼不纯度）** is another way to measure impurity. It is simpler to compute (no logarithms):

\\[
\text{Gini}(S) = 1 - \sum_{i=1}^{C} p_i^2
\\]

For our 7 cats / 3 dogs example:

\\[
\text{Gini} = 1 - (0.7^2 + 0.3^2) = 1 - (0.49 + 0.09) = 1 - 0.58 = 0.42
\\]

Gini reaches 0 for pure nodes and 0.5 for a perfectly balanced binary split (its maximum).

**For the exam**: Know both formulas. Be able to compute both by hand. The examiner has not explicitly asked for Gini calculations in past tests, but the concepts appear in lecture slides 30--32 and could appear.

### The Gini split formula

When evaluating a split on attribute A that produces subsets \\( D_1 \\) and \\( D_2 \\):

\\[
\text{Gini}_{\text{split}}(D, A) = \frac{n_1}{n} \text{Gini}(D_1) + \frac{n_2}{n} \text{Gini}(D_2)
\\]

Pick the split that **minimizes** the weighted Gini after splitting (equivalently, maximizes the Gini reduction \\( \Delta\text{Gini} \\)).

### Worked example: Gini for the 100/49 split

*(Lec 8, slides 30--31)*

Let us revisit the same example we used for information gain (100 class-1, 49 class-0), but now compute Gini.

**Step 1**: Gini of the root (before splitting):

\\[
\text{Gini}(\text{root}) = 1 - \left(\frac{100}{149}\right)^2 - \left(\frac{49}{149}\right)^2 = 1 - 0.4505 - 0.1081 \approx 0.4414
\\]

**Step 2**: Gini of the left child ({50 class-1, 0 class-0}):

\\[
\text{Gini}(\text{left}) = 1 - 1^2 - 0^2 = 0
\\]

Pure node -- Gini is 0, as expected.

**Step 3**: Gini of the right child ({50 class-1, 49 class-0}):

\\[
\text{Gini}(\text{right}) = 1 - \left(\frac{50}{99}\right)^2 - \left(\frac{49}{99}\right)^2 \approx 1 - 0.2551 - 0.2450 \approx 0.4999
\\]

Almost 0.5 -- this is a nearly 50/50 split, maximum impurity.

**Step 4**: Weighted Gini after splitting:

\\[
\text{Gini}_{\text{split}} = \frac{50}{149} \times 0 + \frac{99}{149} \times 0.4999 \approx 0 + 0.3322 = 0.3322
\\]

**Step 5**: Gini reduction:

\\[
\Delta\text{Gini} = 0.4414 - 0.3322 = 0.1092 > 0 \quad \text{(good split!)}
\\]

The split reduces Gini impurity by 0.1092. Just like information gain, Gini correctly identifies this as a useful split -- even though accuracy gain was zero.

### Entropy vs Gini: which to use?

*(Lec 8, slide 32)*

| Aspect | Entropy (Information Gain) | Gini Impurity |
|---|---|---|
| Formula | \\( -\sum p_i \log_2 p_i \\) | \\( 1 - \sum p_i^2 \\) |
| Computation speed | Slower (requires logarithm) | **Faster** (no logarithm) |
| Range (binary) | [0, 1] bits | [0, 0.5] |
| Imbalanced classes | May behave **slightly better** | Good but less sensitive |
| Default in sklearn | No | **Yes** (CART uses Gini) |
| Resulting trees | In practice, **very similar** | In practice, **very similar** |

The bottom line: for most practical purposes they produce nearly identical trees. If you are doing a hand calculation in an exam, Gini is easier since you avoid log computations. Scikit-learn's `DecisionTreeClassifier` uses Gini by default.

---

## Part 5: Ensemble Methods -- Many Weak Trees Beat One Strong Tree

### Why a single tree is not enough

*(Lec 8, slides 33--37)*

A single decision tree has three fundamental problems:

1. **Exponentially less data at lower levels**: Each split divides the data. By the time you reach the bottom of the tree, each leaf may contain only a handful of examples. Decisions at deep nodes are based on very little evidence.
2. **Overfitting**: Very large trees memorize the training data, including noise. They perform well on training data but poorly on unseen data.
3. **Greedy construction**: As we just learned, CART does not find the globally optimal tree -- the greedy heuristic may miss better solutions.

Additionally, trees have **high variance**: small changes in the training data can produce a completely different tree. The tree is *unstable*.

The insight behind ensemble methods is simple: **many weak learners combined can outperform a single strong learner**.

### Bias and Variance -- a quick detour

*(Lec 8, slide 37)*

Before understanding ensembles, you need to understand the bias-variance tradeoff:

- **Bias（偏差）**: How far off the model's *average* prediction is from the true value. High bias = the model is too simple (underfitting).
- **Variance（方差）**: How much the model's predictions *change* when trained on different datasets. High variance = the model is too sensitive to the training data (overfitting).

Think of a target/dartboard analogy (from the lecture's target diagram):

| | **Low Variance** | **High Variance** |
|---|---|---|
| **Low Bias** | Shots clustered tightly around the bullseye -- **ideal** | Shots centered on bullseye but spread widely -- e.g., **unpruned decision trees** |
| **High Bias** | Shots clustered tightly but away from center -- consistent but wrong, **underfitting** (e.g., linear model for complex data) | Shots scattered everywhere away from center -- **worst case** |

An unpruned decision tree typically has **low bias but high variance**: it can fit the training data very well, but small changes in the data produce wildly different trees.

The key takeaway for ensembles:
- **Bagging reduces VARIANCE** (takes the spread-out shots and averages them toward the center)
- **Boosting reduces BIAS** (shifts the cluster toward the bullseye)

This is exactly what ensembles fix.

### Bagging: reducing variance by averaging

*(Lec 8, slides 38--39)*

**Bagging** stands for **B**ootstrap **Agg**regat**ing**. The idea:

1. From your dataset of \\( n \\) examples, create \\( m \\) new datasets by sampling \\( n \\) examples **with replacement** (bootstrap sampling). Some examples appear multiple times; others do not appear at all. On average, each bootstrap sample contains approximately **63.2%** of the unique original examples (the rest are duplicates). The probability of a specific example *not* being picked in \\( n \\) draws is \\( (1 - 1/n)^n \approx 1/e \approx 0.368 \\), so the chance it *is* picked at least once is \\( \approx 63.2\% \\).
2. Train one decision tree on each bootstrap sample.
3. Aggregate predictions: **majority vote** for classification, **average** for regression.

```
Original Data D = [A, B, C, D, E]

Bootstrap sample 1: [A, A, C, D, E]  -->  Tree 1
Bootstrap sample 2: [B, C, C, D, B]  -->  Tree 2
Bootstrap sample 3: [A, B, D, D, E]  -->  Tree 3

New example x arrives:
  Tree 1 says: "Cat"
  Tree 2 says: "Dog"
  Tree 3 says: "Cat"
  
  Majority vote: "Cat" (2 out of 3)
```

Bagging reduces variance because averaging many independent estimates is more stable than relying on a single estimate. But there is a catch...

### The correlation problem

*(Lec 8, slide 40)*

Even with bagging, if one feature is very strong (e.g., "does the email contain the word 'viagra'?" for spam detection), that feature will dominate the root of **every** tree. All your trees will look nearly identical despite the different bootstrap samples.

Asking 2,048 copies of the same person for directions gives you the same answer 2,048 times. That is useless as an ensemble.

The trees are **highly correlated（高度相关的）**, so averaging them does not help much.

### Random Forest and Feature Bagging -- THE Most-Tested Topic

*(Lec 8, slide 40)*

A **Random Forest（随机森林）** = bagged decision trees + **feature bagging（特征袋装）**.

The problem with plain bagging alone is that the trees are still highly correlated: the same dominant features always get selected at the root, so you end up with many near-identical trees. Feature bagging solves this by decorrelating the trees.

**Feature bagging** means: at each split, each tree only considers a **random subset** of the available features.

Here is how it works, step by step:

1. Create many bootstrap samples of the data (just like bagging).
2. For each tree, at each node, **randomly select a subset of features**.
   - Typical subset size: \\( \sqrt{n} \\) where \\( n \\) is the total number of features.
   - Example: 225 features \\( \to \sqrt{225} = 15 \\) features per split.
   - The features are selected as a **random sample, with replacement**, of size much smaller than the total.
3. From this subset, pick the best split using information gain or Gini.
4. Build many trees (e.g., 2,048) and aggregate by majority vote.

### WHY feature bagging works -- the key insight

Without feature bagging, the same dominant feature gets selected as the root of most trees. All trees become nearly identical. Identical trees are useless as an ensemble.

Feature bagging **forces diversity**: each tree sees different features, so different trees make different splits, even at the root. This makes the trees **less correlated** with each other. When you average the predictions of many uncorrelated trees, the errors cancel out much more effectively than if the trees were correlated.

Think of it this way: if you want diverse perspectives on a problem, you should not give every advisor the same information. Give each one a different subset of facts, and their conclusions will complement each other.

### Feature bagging vs Data bagging -- do NOT confuse these

| | Feature bagging | Data bagging (Bootstrap) |
|---|---|---|
| What is sampled? | **Features** (columns) | **Data points** (rows) |
| Purpose | Decorrelate trees | Create diverse training sets |
| Subset size | \\( \sqrt{n} \\) features | \\( n \\) data points (with replacement) |
| Which is more important for Random Forest? | **This one** -- it is the key innovation | Necessary but not sufficient |

> **Common Misconception**: Students often confuse feature bagging with data bagging. The exam specifically asks about **feature** bagging. When the question says "how does the bagging algorithm select features," it is asking about the column-level random selection, not the row-level bootstrap sampling. Make sure your answer talks about features, not data points.

---

## Part 6: Bagging vs Boosting

*(Lec 8, slides 36, 43--60)*

### The big picture

| Aspect | Bagging | Boosting |
|---|---|---|
| Training order | **Parallel** -- trees are independent | **Sequential** -- each tree depends on previous ones |
| Data sampling | Bootstrap samples (with replacement) | Reweighting: misclassified examples get higher weight |
| What it reduces | **Variance** (overfitting) | **Bias** (underfitting) |
| Overfitting risk | Low | Can overfit if too many rounds |
| Example algorithms | Random Forest | AdaBoost, Gradient Boosting, XGBoost |
| Key idea | Average many diverse models | Each new model fixes the previous one's mistakes |

```
Bagging:                             Boosting:
Data --+---> Tree 1 ---+             Data ---> Model 1
       +---> Tree 2 ---+                        | errors
       +---> Tree 3 ---+--> Vote                v
       +---> Tree N ---+             Reweighted Data ---> Model 2
                                                 | errors
  (parallel, independent)                       v
                                     Reweighted Data ---> Model 3
                                                 |
                                       (sequential, dependent)
                                                 v
                                     Weighted Combination
```

### AdaBoost in brief

*(Lec 8, slides 48--55)*

AdaBoost (Adaptive Boosting) builds a sequence of **weak learners（弱学习器）** -- typically decision stumps (trees with a single split). The key steps:

1. Initialize all training examples with equal weight \\( w_i = 1/N \\).
2. Train a weak classifier \\( h_t \\) on the weighted data.
3. Compute weighted error: \\( \varepsilon_t = \sum w_i \mathbb{1}\{h_t(x^{(i)}) \neq t^{(i)}\} / \sum w_i \\)
4. Compute classifier coefficient: \\( \alpha_t = \frac{1}{2} \log \frac{1 - \varepsilon_t}{\varepsilon_t} \\)
   - Better classifiers (lower error) get higher \\( \alpha \\).
5. Update weights: increase weights on misclassified examples.
6. Final prediction: \\( H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t h_t(x)\right) \\)

A **weak learner（弱学习器）** is a classifier that performs just slightly better than random chance. The most common weak learner is a **decision stump（决策桩）**: a tree with only ONE split and two leaves. It is the simplest possible tree.

#### Worked example from lectures (slides 50--54)

The lecture walks through 3 rounds of AdaBoost:

**Round 1**:
- Train stump \\( h_1 \\) on equally weighted data.
- Weighted error: \\( \varepsilon_1 = 0.30 \\)
- Classifier weight: \\( \alpha_1 = \frac{1}{2} \log \frac{1 - 0.30}{0.30} = \frac{1}{2} \log \frac{0.70}{0.30} \approx 0.42 \\)
- Update weights: increase weight on examples \\( h_1 \\) got wrong.

**Round 2**:
- Train stump \\( h_2 \\) on the reweighted data (harder examples now matter more).
- Weighted error: \\( \varepsilon_2 = 0.21 \\) (lower, because the model is adapting)
- Classifier weight: \\( \alpha_2 = \frac{1}{2} \log \frac{0.79}{0.21} \approx 0.65 \\)
- Update weights again.

**Round 3**:
- Weighted error: \\( \varepsilon_3 = 0.14 \\)
- Classifier weight: \\( \alpha_3 = \frac{1}{2} \log \frac{0.86}{0.14} \approx 0.92 \\)

**Final ensemble**:

\\[
H(x) = \text{sign}(0.42 \cdot h_1(x) + 0.65 \cdot h_2(x) + 0.92 \cdot h_3(x))
\\]

Notice the pattern: **more accurate classifiers (lower error) get HIGHER weights** in the final combination. The third stump, with only 14% error, gets weight 0.92 -- more than double the first stump's weight. This makes intuitive sense: we should trust better classifiers more.

### Gradient Boosting in brief

*(Lec 8, slides 56--59)*

Gradient Boosting is like AdaBoost, but instead of reweighting examples, each new tree is trained to predict the **residual errors (gradients of the loss function)** of the current ensemble.

Key differences from AdaBoost:

| Aspect | AdaBoost | Gradient Boosting |
|---|---|---|
| Base learner | Decision **stumps** (one split) | Full decision **trees** (multiple splits) |
| How it adapts | Reweights misclassified examples | Fits **residuals** (gradient of loss) |
| What is added each round | One rule at a time | One tree at a time |
| Regularization | Implicit (through \\( \alpha \\) weighting) | **Explicit** regularization term |

Gradient Boosting optimizes an objective function that includes both a loss term and a regularization term for model complexity:

\\[
\text{obj}(\theta) = \sum_{i=1}^{N} \ell(y_i, \hat{y}_i) + \sum_{t=1}^{T} \omega(f_t)
\\]

The regularization term \\( \omega(f_t) \\) penalizes complex trees (e.g., too many leaves or too large leaf weights), helping prevent overfitting.

**XGBoost** (eXtreme Gradient Boosting) is the most popular implementation. It includes additional optimizations like second-order gradient approximation, column subsampling, and efficient handling of sparse data.

### The ensemble evolution, summarized

*(Lec 8, slide 60)*

| Level | Method | What it does |
|---|---|---|
| 1 | Decision tree | One tree |
| 2 | Decision forest (bagging) | Many trees, aggregate results |
| 3 | Random forest (feature bagging) | Many trees with random feature subsets -- trees are less correlated |
| 4 | AdaBoost | Sequentially reweight errors |
| 5 | Gradient boosting / XGBoost | Sequentially fit residuals |

---

## Part 7: Every Past Paper Question -- Walked Through

### 2025 Real Test Q4 [2 marks]: CART Greedy

**Question**: "What exactly is meant by saying CART is 'greedy'?"

**Full-marks answer** (from official marking rubric):

> At each node of the decision tree, starting from the root, the algorithm assesses the potential impurity reduction for splitting the training data on each available feature (and for every possible split point for numeric features). The best-performing split is selected **without any look-ahead**. That is the greedy part -- there is no effort to craft an optimal tree overall, just a locally optimal decision regarding the current split. The algorithm is then recursively invoked on each resulting sub-tree.

**Mark allocation**:
- 1 mark: Evaluates all splits and picks the best (maximum impurity reduction)
- 1 mark: **Without look-ahead** / no global optimization

**What loses marks**: Saying "CART maximizes impurity reduction" without mentioning "no look-ahead" earns only **1 out of 2**.

---

### 2025 Sample Q5 [3 marks]: Feature Bagging

**Question**: You are trying to predict the 1-month change in value for a stock based on a set of 225 different features. You are going to use a random forest with feature bagging.

**(a) Describe how the bagging algorithm selects features for any given tree [2 marks]**

**Full-marks answer** (from official marking rubric):

> A random subset of the features would be sampled for any given tree in the random forest. Square-root of the total features was given as an example sample size, so sampling 15 features (\\( \sqrt{225} \\)) per tree would be a great choice; but anything substantially less than 225 could be OK. Typically, a large number of trees are produced (e.g. 2,048), so we need to sample with replacement. So, features would be selected as a random sample, with replacement, of size much less than 225.

**Mark allocation**:
- 1 mark: Random subset mechanism (randomly select features, not all features)
- 1 mark: \\( \sqrt{n} \\) sizing or concrete example (e.g., \\( \sqrt{225} = 15 \\))

**(b) Why is feature bagging considered a good idea? [1 mark]**

**Full-marks answer**:

> Feature bagging is a solution to trees being highly correlated, for instance due to a single strong feature being selected as the root of most trees (even on random subsets of the data). Feature bagging is considered to be a good idea because it makes the trees in the forest **less correlated** and more able to complement one another as an ensemble.

**Mark allocation**:
- 1 mark: Explains decorrelation / complementarity

---

### 2026 Sample Q5 [3 marks]: Feature Bagging (identical question)

This is the exact same question as 2025 Sample Q5, with identical mark allocation and model answers. The fact that they repeated it verbatim tells you this is a near-certain exam question.

---

### 2025 Real Q5 [3 marks]: Fuzzy Logic vs Traditional Logic

This question is about decision rules for athlete selection (STRONG AND HEAVY for hammer throwing) and compares classical Boolean logic with Fuzzy Logic. Although it involves rule-based *decisions*, the core content is covered in the **Soft Computing chapter**, not here. See the cross-reference in that chapter for the full model answer.

---

## Part 8: Practice Problems with Solutions

### Problem 1: CART Greedy (2 marks)

**Q: What makes CART greedy? Write a 2-mark answer.**

**Model answer**: CART is greedy because at each node it evaluates all possible splits across all available features and selects the one that maximally reduces impurity (e.g., maximizes information gain or minimizes Gini impurity). Critically, this selection is made **without any look-ahead** -- CART does not consider whether a different split at the current node might lead to a better overall tree. It only optimizes the current split locally.

---

### Problem 2: Feature count (1 mark)

**Q: Given 400 features, how many would you select per tree in a random forest? Why?**

**Model answer**: You would select approximately \\( \sqrt{400} = 20 \\) features per tree. This is the standard guideline for classification tasks. The goal is to use substantially fewer features than the total so that trees are forced to use different features, reducing correlation between trees in the ensemble.

---

### Problem 3: Why Random Forest beats a single tree even with a perfect feature (2 marks)

**Q: A dataset has one feature that perfectly predicts the outcome. Why might a Random Forest STILL be better than a single tree?**

**Model answer**: Even with a perfect feature, a single tree would overfit to the training data: any noise in other features could lead to unnecessary splits that do not generalize. A random forest is more robust because: (1) not every tree will see the perfect feature (due to feature bagging), forcing other trees to find alternative patterns that may generalize better to unseen data; and (2) the bootstrapping introduces diversity in the training data, so the ensemble is less sensitive to any particular set of training examples. If the perfect feature truly is perfect, the forest will still get every prediction right (since the trees that *do* see it will dominate the vote), but with added robustness against noise and overfitting.

---

### Problem 4: Compute entropy (1 mark)

**Q: Compute the entropy for a dataset with 60% class A, 40% class B.**

**Solution**:

\\[
H = -(0.6 \log_2 0.6 + 0.4 \log_2 0.4)
\\]

- \\( \log_2 0.6 \approx -0.737 \\), so \\( -0.6 \times (-0.737) = 0.442 \\)
- \\( \log_2 0.4 \approx -1.322 \\), so \\( -0.4 \times (-1.322) = 0.529 \\)

\\[
H = 0.442 + 0.529 = 0.971 \text{ bits}
\\]

This is close to the maximum of 1 bit, which makes sense because 60/40 is close to 50/50.

---

### Problem 5: Compute information gain (2 marks)

**Q: A dataset has 20 examples: 12 positive, 8 negative. A split produces Left (8 positive, 2 negative) and Right (4 positive, 6 negative). Compute the information gain.**

**Solution**:

Step 1: Parent entropy.

\\[
H_{\text{parent}} = -(12/20 \log_2 12/20 + 8/20 \log_2 8/20) = -(0.6 \log_2 0.6 + 0.4 \log_2 0.4) \approx 0.971
\\]

Step 2: Left child entropy (8 pos, 2 neg = 10 total).

\\[
H_{\text{left}} = -(0.8 \log_2 0.8 + 0.2 \log_2 0.2) \approx -(0.8 \times (-0.322) + 0.2 \times (-2.322)) \approx 0.258 + 0.464 = 0.722
\\]

Step 3: Right child entropy (4 pos, 6 neg = 10 total).

\\[
H_{\text{right}} = -(0.4 \log_2 0.4 + 0.6 \log_2 0.6) \approx 0.971
\\]

Step 4: Information gain.

\\[
\text{IG} = 0.971 - \left(\frac{10}{20} \times 0.722 + \frac{10}{20} \times 0.971\right) = 0.971 - (0.361 + 0.486) = 0.971 - 0.847 = 0.124 \text{ bits}
\\]

The split provides a modest information gain of 0.124 bits.

---

### Problem 6: Bagging vs Boosting (2 marks)

**Q: Explain the difference between bagging and boosting in 3 sentences.**

**Model answer**: Bagging trains multiple models independently on different bootstrap samples of the training data and aggregates their predictions by majority vote, which reduces **variance** (overfitting). Boosting trains models sequentially, where each new model focuses on the examples that previous models got wrong by increasing their weights, which reduces **bias** (underfitting). In short, bagging stabilizes an unstable model by averaging, while boosting iteratively corrects an underpowered model by targeting its weaknesses.

---

### Problem 7: Why greedy can fail (2 marks)

**Q: Why might a greedy approach fail to find the optimal tree? Give a specific example.**

**Model answer**: A greedy approach makes locally optimal decisions without considering the global picture. For example, suppose classifying fruits requires checking colour first and then shape, but checking shape first followed by colour produces a slightly less impure first split but leads to perfectly pure leaves in the second split. CART would choose the colour split first (better immediate impurity reduction) and might end up with a deeper, less efficient tree. Because CART never looks ahead, it cannot discover that the globally better strategy is to accept a slightly worse first split in exchange for a much better overall tree.

---

## Part 9: How to Write the Perfect Exam Answer

### For CART Greedy (2 marks)

**Template**:

> "CART uses a greedy heuristic. At each node, it evaluates all possible splits on all available features and selects the split that maximally reduces impurity. **Critically, this is done without any look-ahead** -- there is no effort to optimize the tree globally, only to make the best local decision at the current node. The algorithm then recurses on each child."

**Checklist before submitting**:
- [ ] Did I say "evaluates all possible splits"? (1st mark)
- [ ] Did I say "without look-ahead" or "no global optimization"? (2nd mark -- **this is the one students miss**)

### For Feature Bagging (2+1 marks)

**Template for part (a) -- how [2 marks]**:

> "For each tree in the random forest, a random subset of features is selected. The typical subset size is \\( \sqrt{n} \\) where \\( n \\) is the total number of features -- for example, with 225 features, each tree considers approximately \\( \sqrt{225} = 15 \\) features. Features are selected as a random sample, with replacement, of size much smaller than the total. A large number of trees are produced (e.g., 2,048) and their predictions are aggregated."

**Checklist**:
- [ ] Did I mention random subset? (1st mark)
- [ ] Did I give the \\( \sqrt{n} \\) rule or a concrete number? (2nd mark)

**Template for part (b) -- why [1 mark]**:

> "Without feature bagging, the same dominant feature would be selected as the root of most trees, making them highly correlated. Correlated trees provide little benefit when aggregated. Feature bagging forces diversity: each tree sees different features, making trees less correlated and better able to complement each other as an ensemble."

**Checklist**:
- [ ] Did I explain the correlation problem? (the mark)

---

## Formal Definitions Reference

### Decision Tree

A decision tree is a function \\( f: \mathcal{X} \to \mathcal{Y} \\) represented as a directed acyclic tree where each internal node tests a feature \\( x_j \\) against a threshold, each branch corresponds to an outcome, and each leaf assigns a prediction \\( y \in \mathcal{Y} \\).

### Entropy

\\[
H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)
\\]

### Conditional Entropy

\\[
H(Y|X) = \sum_{x} p(x) \cdot H(Y|X=x) = -\sum_{x} p(x) \sum_{y} p(y|x) \log_2 p(y|x)
\\]

### Information Gain

\\[
\text{IG}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)
\\]

### Gini Impurity

\\[
\text{Gini}(S) = 1 - \sum_{i=1}^{C} p_i^2
\\]

### Gini Split

\\[
\text{Gini}_{\text{split}}(D, A) = \frac{n_1}{n} \text{Gini}(D_1) + \frac{n_2}{n} \text{Gini}(D_2)
\\]

### AdaBoost Final Classifier

\\[
H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t h_t(x)\right), \quad \alpha_t = \frac{1}{2} \log \frac{1-\varepsilon_t}{\varepsilon_t}
\\]

---

## English Expression Guide

### Useful phrases for decision tree questions

**Explaining CART:**
- "CART uses a greedy heuristic that selects the locally optimal split at each node."
- "The algorithm makes no attempt to look ahead or optimize the tree globally."
- "At each step, the split that maximally reduces impurity is chosen."

**Explaining feature bagging:**
- "A random subset of features is considered at each split point."
- "This decorrelates the individual trees, enabling the ensemble to benefit from diversity."
- "Without feature bagging, trees would be highly correlated due to the dominance of strong features."

**Explaining entropy / information gain:**
- "Entropy quantifies the uncertainty in the class distribution."
- "Information gain measures the reduction in entropy achieved by a particular split."
- "The split that yields the highest information gain is selected."

**Explaining bagging vs boosting:**
- "Bagging trains models independently and reduces variance by averaging."
- "Boosting trains models sequentially, each focusing on the errors of its predecessors, and reduces bias."

### Easily confused terms

| Confused pair | How to distinguish |
|---|---|
| Feature bagging vs Data bagging | Feature bagging samples **features** (columns); data bagging samples **data points** (rows). Both happen in Random Forest. |
| Entropy vs Gini | Both measure impurity. Entropy uses \\( -p \log p \\); Gini uses \\( 1 - \sum p^2 \\). Nearly identical results in practice. |
| Bagging vs Boosting | Bagging = parallel, reduces variance. Boosting = sequential, reduces bias. |
| Pruning vs Early stopping | Pruning removes branches after building. Early stopping limits depth during building. |
| Parameter vs Hyperparameter | A tree's splits are learned (parameters). Tree depth, minimum leaf size are set by you (hyperparameters). |

---

## Common Mistakes -- Avoid These

1. **Incomplete greedy answer**: Saying "CART maximizes impurity reduction" without mentioning "no look-ahead" costs you marks. The 2025 Real Test marking rubric *explicitly* says this earns only 1/2 marks. Always include "without look-ahead."

2. **Confusing feature bagging with data bagging**: When the exam asks "how does the bagging algorithm select *features*," talk about random subsets of *columns*, not bootstrap samples of *rows*. Three out of four past tests asked specifically about features.

3. **Saying Random Forest trains on "different data"**: That describes bagging (row-level). The exam question about feature bagging is specifically about the column-level random selection.

4. **Forgetting the \\( \sqrt{n} \\) rule**: The marking rubric awards a mark for giving a concrete subset size. Always mention \\( \sqrt{n} \\) and ideally give a numeric example (225 features --> 15 per tree).

5. **Not explaining WHY feature bagging helps**: The 1-mark "why" question requires you to explain the **decorrelation** mechanism. Just saying "it adds randomness" is too vague. Say "it prevents a dominant feature from appearing at the root of every tree, thereby decorrelating the trees."

6. **Mixing up bias and variance reduction**: Bagging reduces **variance**. Boosting reduces **bias**. Do not swap these.

7. **Forgetting that decision trees can express any Boolean function**: Each row of a truth table maps to a root-to-leaf path. This is a quick fact worth remembering.

---

## Self-Check Checklist

Before the exam, make sure you can do ALL of the following:

- [ ] Explain CART's greedy nature in one sentence, including "no look-ahead"
- [ ] Compute entropy by hand for a 2-class dataset (e.g., 70/30 split)
- [ ] Compute information gain for a simple split
- [ ] Compute Gini impurity by hand
- [ ] Explain the difference between feature bagging and data bagging
- [ ] Give the \\( \sqrt{n} \\) rule with a concrete numeric example (e.g., 225 -> 15)
- [ ] Explain **WHY** feature bagging helps (decorrelation of trees)
- [ ] Draw a simple decision tree diagram with root, internal, and leaf nodes
- [ ] Convert a tree path into an IF-THEN rule
- [ ] Explain the difference between bagging and boosting (parallel vs sequential, variance vs bias)
- [ ] Describe how AdaBoost works at a high level (reweight misclassified examples)
- [ ] Explain why accuracy is a bad split criterion (the 100/49 example from lectures)
- [ ] State that finding the optimal tree is NP-complete (Hyafil & Rivest 1976)
- [ ] Compute conditional entropy and use it to derive information gain
- [ ] Know the differences between ID3, C4.5, and CART
- [ ] Compute Gini impurity and Gini split reduction for a worked example
- [ ] Explain the 63.2% bootstrap fact (why each sample has ~63.2% unique examples)
- [ ] Walk through one round of AdaBoost: compute error, alpha, weight update
- [ ] Explain how Gradient Boosting differs from AdaBoost (residuals vs reweighting)
- [ ] Draw the bias-variance target diagram and label each quadrant
- [ ] Know which question type appears most often: feature bagging (4/4 tests)
