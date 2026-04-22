# 考点频率分布 — Topic Frequency Heat Map

> 基于全部可用考试卷的统计分析（S1 2025 Sample, S1 2025 Actual, S1 2026 Sample, S1 2024 Final）

---

## 📊 考点频率总览

| 知识模块 | 出现次数 | 总分占比 | 优先级 | 考查形式 |
|---------|---------|--------|--------|---------|
| **Symbolic Logic** (PL + FOL + Modus Tollens) | 4/4 卷 | 13-25% | 🔴 必考 | 推理推导 + FOL 翻译 |
| **Logic Neural Networks** (Soft Logic + Truth Bounds) | 3/3 mid-tests | 13-20% | 🔴 必考 | 计算 + 概念对比 |
| **Knowledge Graphs** (TransE + Embeddings + Inference) | 3/3 mid-tests | 10-13% | 🔴 必考 | 概念解释 + 公式 |
| **Decision Trees & Ensembles** (CART + RF + Bagging) | 3/4 卷 | 10-20% | 🔴 必考 | 概念理解 + 应用 |
| **Soft Computing** (Fuzzy Logic + Vagueness vs Uncertainty) | 3/4 卷 | 15-20% | 🔴 必考 | 对比分析 + 场景分类 |
| **NEAT & Genetic Algorithms** | 2/4 卷 | 13-20% | 🟠 高频 | 适应度函数设计 |
| **Embodied AI & Robot Soccer** | 2/3 mid-tests | 10-13% | 🟠 高频 | 策略描述 |
| **MYCIN / Expert Systems** (Backward Chaining) | 1/3 mid-tests | 13-20% | 🟠 高频 | 推理过程描述 |
| **Naïve Bayes** | 1/4 卷 (final) | ~10% | 🟡 中频 | 假设解释 |
| **Knowledge Representation** (Frames, Semantic Nets, RBS) | 0 (直接考题) | — | 🟢 低频 | 间接考查 |

---

## 🎯 按考题编号统计（Mid-term Test 模式）

每份试卷固定 6 道简答题，主题分布如下：

| 题号 | S1 2025 Sample (15m) | S1 2025 Actual (15m) | S1 2026 Sample (20m) |
|-----|---------------------|---------------------|---------------------|
| Q1 | Symbolic Logic (3m) | Symbolic Logic (2m) | Symbolic Logic (5m) |
| Q2 | LNN (2m) | LNN (3m) | LNN (4m) |
| Q3 | Knowledge Graphs (2m) | Knowledge Graphs (2m) | Knowledge Graphs (2m) |
| Q4 | Robot Soccer (2m) | Decision Trees (2m) | Robot Soccer (2m) |
| Q5 | Random Forest (3m) | Fuzzy Logic (3m) | Random Forest (3m) |
| Q6 | MYCIN/Backward Chaining (3m) | GA/Fitness Function (3m) | Vagueness vs Uncertainty (4m) |

### 规律总结：
- **Q1 永远是 Symbolic Logic**（分值从 2→5 递增！）
- **Q2 永远是 LNN**（分值从 2→4 递增！）
- **Q3 永远是 Knowledge Graphs / TransE**
- **Q4-Q6 在以下主题中轮换**：Decision Trees/RF、Soft Computing/Fuzzy、NEAT/GA、Robot Soccer、MYCIN

---

## 📈 分值趋势分析

```
2025 Sample (15m):  Logic(3) + LNN(2) + KG(2) + Robot(2) + RF(3) + MYCIN(3)
2025 Actual (15m):  Logic(2) + LNN(3) + KG(2) + DT(2) + Fuzzy(3) + GA(3)
2026 Sample (20m):  Logic(5) + LNN(4) + KG(2) + Robot(2) + RF(3) + V/U(4)
```

**关键发现**：
1. 2026 总分从 15→20，额外的 5 分主要加在了 Logic (+2) 和 LNN (+2) 上
2. Symbolic Logic 要求从"代数推导"升级为"完整真值表"
3. Vagueness vs Uncertainty 是新增的高分考点（4分）

---

## ⏰ 建议复习时间分配（基于频率和分值）

| 模块 | 建议时间占比 | 理由 |
|-----|-----------|------|
| Symbolic Logic | 20% | 每卷必考，分值最高（最多 5m），需要熟练掌握真值表 + Modus Tollens |
| LNN | 15% | 每卷必考，分值递增，计算和概念并重 |
| Soft Computing (Fuzzy + Bayes + V/U) | 15% | 高频，vagueness vs uncertainty 新增为高分考点 |
| Decision Trees & Ensembles | 15% | 高频，重点理解"为什么" (greedy, feature bagging) |
| Knowledge Graphs & TransE | 10% | 每卷必考但分值稳定在 2m，概念性强 |
| NEAT & GA | 10% | 高频，重点是 fitness function 设计 |
| Embodied AI & Robot Soccer | 10% | 中频，概念性强，答题灵活 |
| MYCIN & Expert Systems | 5% | 低频但重要概念（backward chaining） |

---

## 🧩 考点共现分析

以下概念经常在同一道题或同一考卷中一起出现：

| 概念组合 | 出现模式 | 意义 |
|---------|---------|------|
| Modus Tollens + De Morgan's | 每道 Q1 | 先否定后件，再展开否定前件 |
| LNN + Soft Logic AND | 每道 Q2 | LNN 的核心计算依赖 Product-Sum AND |
| LNN Bounds + Safety-Critical | 2025 Actual | bounds 在自动驾驶中的应用 |
| TransE + Link Prediction | 每道 Q3 | h+r≈t 用于预测缺失链接 |
| Fuzzy vs Traditional Logic | 2025 Actual | 同一规则在两种体系下的对比 |
| GA + Embodied AI | 2025 Actual | 用 GA 训练 BigDog 机器人控制器 |
| Vagueness vs Uncertainty | 2026 Sample | 四个场景分类 |
| Bagging + Feature Bagging | 每道 RF 题 | 两者缺一不可 |

---

## 🎯 Cheatsheet 优先级排序

根据出题频率和分值，你的双面 A4 手写笔记应该包含以下内容（按重要性排序）：

### 必须写（占据 60% 空间）
1. Modus Tollens 公式 + De Morgan's Laws + 两种 premise 结构的展开方式
2. 完整的 implication 真值表 (4 行)
3. LNN Soft Logic (Product-Sum): AND = A×B, OR = A+B-AB, NOT = 1-A
4. LNN Truth Bounds 分类规则 (L≥α → TRUE, U≤α → FALSE, etc.)
5. OR bounds: L=max(L₁,L₂), U=max(U₁,U₂)
6. TransE: h+r≈t, f(h,r,t) = ||h+r-t||
7. Entropy: H(X) = -Σp(x)log₂p(x), IG = H(Y) - H(Y|X)
8. Gini: G(D) = 1 - Σpᵢ²
9. Fuzzy: AND=min, OR=max, NOT=1-μ
10. Vagueness vs Uncertainty 判断流程图

### 建议写（占据 30% 空间）
11. Bayes' Theorem: P(H|e) = P(e|H)P(H)/P(e)
12. Naïve Bayes: P(C|x) ∝ P(C)ΠP(xᵢ|C)
13. CART = greedy (no look-ahead)
14. RF = Bagging + Feature Bagging (√features)
15. CF(conclusion) = CF(premise) × CF(rule)
16. Forward vs Backward Chaining 对比
17. NEAT: speciation distance δ = c₁E/N + c₂D/N + c₃W̄
18. Flocking 3 rules: separation, cohesion, alignment

### 如果有空间（占据 10%）
19. FOL 量词否定: ¬∀x P(x) ≡ ∃x ¬P(x)
20. STEAM: Joint Persistent Goal (A/U/I)
21. Ontology vs KG 区别
22. RDF triple 格式
