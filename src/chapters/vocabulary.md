# Technical Vocabulary Quick Reference（专业词汇速查）

> Organised by module. Each entry: English term → 中文 → spelling/usage notes.

---

## Module A — Symbolic Logic

| Term | 中文 | Watch Out |
|------|------|-----------|
| Propositional Logic | 命题逻辑 | NOT "proportional" |
| First-Order Logic (FOL) | 一阶逻辑 | Also: predicate logic |
| Connective | 逻辑联结词 | ∧ AND, ∨ OR, → implies, ¬ NOT |
| Modus Ponens | 肯定前件 | P, P→Q ⊢ Q |
| Modus Tollens | 否定后件 | ¬Q, P→Q ⊢ ¬P |
| Resolution | 归结 | NOT "revolution" |
| CNF (Conjunctive Normal Form) | 合取范式 | AND of ORs |
| Quantifier | 量词 | ∀ universal, ∃ existential |
| Vacuous truth | 空真 | P→Q is TRUE when P is FALSE |
| Predicate | 谓词 | Function returning T/F: Fly(x) |
| Inference | 推理 | NOT "reference" |

## Module B — LNN

| Term | 中文 | Watch Out |
|------|------|-----------|
| Logic Neural Network (LNN) | 逻辑神经网络 | "Logic Neural" not "Logical Neural" |
| T-norm | 三角范数 | Generalises AND to [0,1] |
| Łukasiewicz | 卢卡西维茨 | Hard to spell; max(0, a+b-1) |
| Differentiable | 可微的 | Enables gradient-based learning |
| Truth bounds | 真值上下界 | [L, U] interval |
| Conjunction / Disjunction | 合取 / 析取 | AND / OR |
| Bidirectional inference | 双向推理 | Upward + downward pass |

## Module C — Knowledge Representation

| Term | 中文 | Watch Out |
|------|------|-----------|
| Expert System | 专家系统 | Rule-based, mimics human experts |
| Knowledge Base | 知识库 | NOT just "database" |
| Inference Engine | 推理引擎 | Applies rules to derive conclusions |
| Ontology | 本体论 | Formal concepts + relationships |
| OWL | 网络本体语言 | Web Ontology Language |
| RDF | 资源描述框架 | (subject, predicate, object) triples |
| Knowledge Graph | 知识图谱 | Entity-relation-entity graph |
| RAG | 检索增强生成 | Retrieval-Augmented Generation |

## Module D — Knowledge Graphs

| Term | 中文 | Watch Out |
|------|------|-----------|
| Entity/Relation Embedding | 实体/关系嵌入 | Dense, learned vectors |
| TransE | TransE模型 | h + r ≈ t |
| Link Prediction | 链接预测 | (h, r, ?) or (?, r, t) |
| Negative Sampling | 负采样 | Corrupt h or t for training |
| L1 norm / Manhattan distance | L1范数 | Σ\|x_i - y_i\| |

## Module E — MYCIN

| Term | 中文 | Watch Out |
|------|------|-----------|
| Backward Chaining | 反向链接 | Goal-driven |
| Forward Chaining | 正向链接 | Data-driven |
| Confidence Factor (CF) | 确信因子 | Range [-1, +1]; NOT a probability |
| Production Rule | 产生式规则 | IF-THEN format |
| E-MYCIN | 基本MYCIN | Domain-independent shell |
| Knowledge Acquisition Bottleneck | 知识获取瓶颈 | Hard to extract expert knowledge |

## Module F — Decision Trees & Ensembles

| Term | 中文 | Watch Out |
|------|------|-----------|
| Decision Tree | 决策树 | NOT "decision three" |
| Entropy | 熵 | H(X) = -Σ p(x) log₂ p(x) |
| Information Gain | 信息增益 | IG = H(Y) - H(Y\|X) |
| Gini Index | 基尼指数 | 1 - Σ p²(i) |
| Bagging | 袋装法 | Bootstrap Aggregating — parallel |
| Boosting | 提升法 | Sequential error correction |
| Random Forest | 随机森林 | Bagging + feature bagging |
| AdaBoost | 自适应提升 | Adaptive Boosting |
| XGBoost | 极端梯度提升 | eXtreme Gradient Boosting |
| Weak Learner | 弱学习器 | Slightly better than random |
| Decision Stump | 决策桩 | One-split tree |
| Bootstrap | 自助采样 | Sample WITH replacement |

## Module G — Soft Computing

| Term | 中文 | Watch Out |
|------|------|-----------|
| Vagueness | 模糊性 | Blurry boundaries → fuzzy logic |
| Uncertainty | 不确定性 | Unknown state → Bayesian |
| Fuzzy Logic | 模糊逻辑 | Degrees of truth [0, 1] |
| Membership Function | 隶属函数 | μ_A(x) — NOT a probability |
| Bayesian Reasoning | 贝叶斯推理 | P(H\|e) via Bayes' theorem |
| Prior / Posterior | 先验 / 后验 | Before / after seeing evidence |
| Likelihood | 似然 | P(evidence \| hypothesis) |
| Naive Bayes | 朴素贝叶斯 | Assumes feature independence |

---

## Top Confused Pairs（最易混淆）

| Pair | Key Difference |
|------|---------------|
| **vagueness** vs **uncertainty** | Blurry concept vs unknown fact |
| **bagging** vs **boosting** | Parallel/variance vs sequential/bias |
| **forward** vs **backward chaining** | Data-driven vs goal-driven |
| **inference** vs **reference** | Reasoning vs citing |
| **parameter** vs **hyperparameter** | Learned vs manually set |
| **embedding** vs **encoding** | Dense learned vs any representation |
| **ontology** vs **knowledge graph** | Schema/vocabulary vs data instances |
| **entropy** vs **information gain** | Impurity measure vs impurity reduction |
| **precision** vs **accuracy** | TP/(TP+FP) vs correct/total |
