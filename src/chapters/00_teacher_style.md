# 命题风格分析 — Teacher Style Analysis

> **Instructor:** Xinyu Zhang | **Course:** COMPSCI 713 AI Fundamentals | **S1 2026**
> 基于全部可用考试卷分析（S1 2025 Sample, S1 2025 Actual, S1 2026 Sample, S1 2024 Final）

---

## 👤 教师信息

- **Instructor**: Xinyu Zhang (School of Computer Science, University of Auckland)
- **Course**: COMPSCI 713: AI Fundamentals, S1 2026
- **Website**: zhangxinyu-xyz.github.io
- **另一位出题者**: Thomas (负责 Part 2 — 深度学习/RL/LLM 相关，与 Xinyu 的 Part 1 分开考)

---

## 🎯 出题风格总结

### 1. 偏好应用场景题（Application-Based Scenarios）

Xinyu 的题目**几乎从不直接问定义**。每道题都嵌入在一个具体场景中：

| 场景类型 | 出现频率 | 具体例子 |
|---------|---------|---------|
| 安全/门禁系统 | 3 次 | Secure facility (I∧F→E), smart office alarm (P∨Q→R) |
| 智能家居 | 2 次 | Smart home heating (LNN HeatingOn) |
| 自动驾驶 | 1 次 | Autonomous vehicle collision alert (LNN bounds) |
| 医疗诊断 | 1 次 | Runny nose backward chaining |
| 体育/健身 | 1 次 | Hammer thrower (fuzzy logic) |
| 机器人 | 2 次 | Robot soccer, BigDog walking |
| 金融/商业 | 1 次 | Stock prediction (random forest) |

**应对策略**：不要死记硬背定义，要练习在新场景中**应用**概念。

### 2. 偏好"为什么"而非"是什么"

典型问法：
- "Why is feature bagging considered a good idea?" (不是 "What is feature bagging?")
- "What exactly is meant by saying CART is 'greedy'?" (不是 "Define CART")
- "Why is using bounds beneficial in safety-critical applications?" (不是 "What are bounds?")

**应对策略**：准备好每个概念的**原因**和**动机**，不仅仅是定义。

### 3. 重视对比分析（Contrast & Compare）

高频出题模式：
- Boolean logic vs LNN soft logic（每卷 Q2）
- Traditional logic vs Fuzzy logic（2025 Actual Q5）
- Vagueness vs Uncertainty（2026 Sample Q6）
- Decision tree vs Decision forest（2024 Final）
- Forward chaining vs Backward chaining（隐含在 MYCIN 题中）

**应对策略**：准备好两栏对比表格，考试时直接画表回答。

### 4. 计算题轻量但必须准确

- LNN: 0.9 × 0.4 = 0.36 这种简单乘法
- Entropy/Gini: 不会给太复杂的数据，但公式必须正确
- TransE: 概念性理解 h+r≈t 即可，不需要实际向量计算

**应对策略**：把公式写在 cheatsheet 上，考试时代入数字即可。

### 5. 评分标准：Quality over Quantity

考试说明明确写道：
> "We privilege quality over quantity, i.e., you do not need to write very long answers. Be concise and clear."

| 答题长度建议 | 分值 | 建议写法 |
|-----------|------|---------|
| 1 mark | 1-2 句话 | 一个关键点，直接命中 |
| 2 marks | 3-4 句话或一个小段落 | 两个关键点 + 简短解释 |
| 3 marks | 一个段落或结构化回答 | 三个关键点 + 各自解释 |
| 4-5 marks | 结构化回答 + 例子/表格 | 多个关键点 + 具体例子 + 对比 |

### 6. 常用句式模式

Xinyu 的题目经常使用以下句式：

- **"Use propositional logic to deduce what must be true about X and Y."** → 用 Modus Tollens + De Morgan's
- **"What does this rule represent in natural language, and how is it different from..."** → 翻译 + 对比
- **"Explain how the LNN would likely compute..."** → 写出计算步骤
- **"Contrast how the above rule might work using traditional logic as compared to..."** → 画对比表
- **"For each of the following situations, state whether it is mainly..."** → 分类 + 简短理由
- **"Describe one strategy or collective behaviour..."** → 从课堂内容中选一个，解释清楚
- **"Name the elements that should be part of the fitness function..."** → 列出 3-5 个关键要素

---

## 🔄 题目进化趋势（2025 → 2026）

| 变化维度 | 2025 | 2026 预测 |
|---------|------|----------|
| 总分 | 15 marks | 20 marks |
| Logic 分值 | 2-3 marks | 5 marks（要求真值表）|
| LNN 分值 | 2-3 marks | 4 marks（更深入）|
| 新增考点 | — | Vagueness vs Uncertainty (4m) |
| 难度 | 中等 | 稍有提升（需要更完整的推导过程）|
| 时间压力 | 55min/15m ≈ 3.7min/mark | 55min/20m = 2.75min/mark |

**关键发现**：2026 时间更紧了！每分只有 2.75 分钟，比 2025 的 3.7 分钟少了约 25%。必须更加简洁高效。

---

## ⚠️ 常见陷阱与扣分点

| 陷阱 | 说明 | 正确做法 |
|-----|------|---------|
| 混淆 ¬(A∧B) 和 ¬(A∨B) | De Morgan's 展开方向不同 | ¬(A∧B)=¬A∨¬B, ¬(A∨B)=¬A∧¬B |
| 混淆 vagueness 和 uncertainty | "high risk" 是 vagueness，"is there a burglary?" 是 uncertainty | 问"概念本身有没有模糊边界" |
| 忘记说 CART 是 "no look-ahead" | 只说 "maximizes impurity reduction" 只能拿一半分 | 必须强调 greedy = no look-ahead |
| LNN 中混淆 Product-Sum 和 min/max | 考题用 Product-Sum AND (A×B)，fuzzy 用 min | 看题目指定的是哪种运算 |
| Feature bagging 只说 "random features" | 需要说明目的是 decorrelate trees | 解释为什么：防止 dominant feature 总是做 root |
| Backward chaining 不说 "start from goal" | 关键是从假设出发 | 明确说 "start with hypothesis, find support" |
| TransE 忘记说 "smaller score = more likely" | 这是 distance-based score | f(h,r,t) = \|\|h+r-t\|\|, 越小越好 |

---

## 📝 高分答题策略

### 1. 结构化回答
对于 2-3 分的题，使用：
```
[1句总结] + [关键点1 + 解释] + [关键点2 + 解释]
```

### 2. 对比题用表格
```
| Aspect | Method A | Method B |
|--------|---------|---------|
| ...    | ...     | ...     |
```

### 3. 计算题写出每一步
```
Given: Cold = 0.9, AtHome = 0.4
AND (Product-Sum) = 0.9 × 0.4 = 0.36
If threshold α = 0.5, then 0.36 < 0.5 → heating NOT activated
```

### 4. 推理题用链式推导
```
Given: ¬E
Rule: (I ∧ F) → E
By Modus Tollens: ¬E → ¬(I ∧ F)
By De Morgan's: ¬(I ∧ F) = ¬I ∨ ¬F
∴ Either ¬I or ¬F (or both)
```

### 5. 时间管理（2026 格式，20 marks / 55 min）

| 题号 | 预期分值 | 建议时间 | 策略 |
|-----|---------|---------|------|
| Q1 (Logic) | 5m | 12 min | 先写代数推导，再补真值表 |
| Q2 (LNN) | 4m | 10 min | 先翻译，再计算，最后对比 |
| Q3 (KG) | 2m | 5 min | TransE 公式 + 一个例子 |
| Q4 (轮换) | 2m | 5 min | 从课堂内容选一个策略展开 |
| Q5 (轮换) | 3m | 8 min | 结构化回答，每个分点一段 |
| Q6 (轮换) | 4m | 10 min | 每个子题 2-3 句，确保覆盖评分点 |
| 检查 | — | 5 min | 检查计算和 De Morgan's 方向 |
