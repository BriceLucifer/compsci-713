# Knowledge Representation Methods (W3L1)

## 🎯 考试重要度

🟡 **中频** | Week 3 Lecture 1 (44 slides) | 为后续 KG Embeddings (Sample Test Q3)、MYCIN (W4L1) 的理论基础

> **Why study this?** This lecture defines ALL five KR methods tested in this course: Symbolic Logic, Semantic Networks, Frames, Rule-Based Systems, and Knowledge Graphs. Comparison questions across these methods are a natural exam question type. Understanding each method's strengths and weaknesses is essential for design-type questions. The exercises from this lecture test inference reasoning -- a skill required across Q1 (logic), Q3 (KG embeddings), and Q5 (MYCIN).

---

## 📖 核心概念（Core Concepts）

| English Term | 中文 | One-line Definition |
|---|---|---|
| Knowledge Representation (KR)（知识表示） | 知识表示 | Methods used in AI to **store**, **retrieve**, and **handle** knowledge to enable intelligent reasoning |
| Structured Knowledge（结构化知识） | 结构化知识 | Knowledge organized in a predefined format (databases, tables, ontologies, KGs) |
| Unstructured Knowledge（非结构化知识） | 非结构化知识 | Knowledge without predefined structure (raw text, images, videos, free-form documents) |
| Semantic Network（语义网络） | 语义网络 | Graph-based KR where nodes = concepts and edges = relationships (IS-A, HAS-PROPERTY) |
| Frame（框架） | 框架 | Slot-filler structure grouping related information about an entity (concept/attribute/value) |
| Rule-Based System (RBS)（基于规则的系统） | 基于规则系统 | KR using IF-THEN rules that trigger actions/conclusions when conditions are met |
| Knowledge Graph (KG)（知识图谱） | 知识图谱 | Graph-based representation connecting entities (nodes) with relationships (edges) + properties |
| RDF Triple（RDF三元组） | RDF三元组 | Atomic fact unit: (Subject, Predicate, Object) -- e.g., (Einstein, bornIn, Germany) |
| Transitive Inference（传递推理） | 传递推理 | If A→B and B→C, then A→C; key reasoning pattern in Semantic Networks and KGs |
| Property Inheritance（属性继承） | 属性继承 | Child concepts inherit properties from parent concepts (e.g., Dog inherits warm-blooded from Mammal) |
| Procedural Attachment（过程附件） | 过程附件 | Frame slots that trigger actions when accessed (e.g., hotel check-in slot sends confirmation email) |

---

## 🧠 费曼草稿（Feynman Draft）

### The Filing Cabinet Analogy

Imagine you just got hired to organize ALL the knowledge in a hospital -- every disease, every symptom, every treatment, every patient record. You need the knowledge organized so that a robot doctor can not only *look things up* but also *reason* about new patients it has never seen before. The question is: what filing system do you use?

It turns out there is **no single best system**. Different filing systems are good at different things. This lecture covers five of them.

### System 1: Symbolic Logic -- The Mathematician's Notebook

You write everything as precise mathematical statements:
- "For all x, if x has flu, then x has a fever": $\forall x\ (\text{Flu}(x) \rightarrow \text{HasSymptom}(x, \text{Fever}))$
- "If a patient has fever AND cough, then likely diagnosis is flu": $\forall x\ (\text{HasSymptom}(x, \text{Fever}) \wedge \text{HasSymptom}(x, \text{Cough}) \rightarrow \text{LikelyDiagnosis}(x, \text{Flu}))$

Strengths: absolutely precise, supports formal proof. Weakness: extremely rigid -- try expressing "70% chance of flu" in pure logic!

### System 2: Semantic Networks -- The Mind Map

Think of a giant mind map on a whiteboard. Each sticky note is a concept (Cat, Mammal, Animal, Fur), and you draw labeled arrows between them:

```
Cat ──is-a──► Mammal ──is-a──► Animal
Cat ──has──► Fur
Mammal ──has-property──► Warm-blooded
```

Now here's the magic: because Cat **is-a** Mammal, and Mammal **has-property** Warm-blooded, the system can *infer* that Cat is Warm-blooded -- even though you never wrote that explicitly. This is called **transitive inheritance**.

**Toy example:** Given these three facts:
1. "Dog is-a Mammal"
2. "Mammal is-a Animal"
3. "Mammal has-property Warm-blooded"

The system infers: "Dog is-a Animal" (transitive IS-A) and "Dog has-property Warm-blooded" (property inheritance).

### System 3: Frames -- The Object-Oriented Database

Imagine describing a car using a form you fill out:

| Frame: Car | Slot (Attribute) | Filler (Value) |
|---|---|---|
| Car | Brand | Tesla |
| | Colour | Red |
| | Engine | Electric |
| | Owner | Alice |

Each frame is like an **object in programming** -- it has attributes (slots) and values (fillers). Frames can do four clever things:

1. **Default values**: If you create a new "Dog" frame and don't specify legs, it defaults to 4 (inherited from "Mammal" frame)
2. **Inheritance**: A "Dog" frame inherits "Has Hair = True" from the "Mammal" frame
3. **Slot constraints**: A "Student" frame requires Age > 5
4. **Procedural attachment**: Accessing the "Check-in Time" slot of a "Hotel Reservation" frame automatically triggers sending a confirmation email

### System 4: Rule-Based Systems -- The Decision Flowchart

You encode every decision as an IF-THEN rule:

```
R1: IF Fever AND Cough                    THEN Possible Diagnosis = Flu
R2: IF Fever AND Joint Pain AND Travel     THEN Possible Diagnosis = Dengue Fever
R3: IF Cough AND Difficulty Breathing      THEN Possible Diagnosis = Pneumonia
```

Patient comes in with Fever + Cough + Joint Pain + Recent Travel? R1 fires (Flu) and R2 fires (Dengue Fever). The system considers both.

This is the simplest form -- it's **transparent** (you can trace exactly which rules fired) but **brittle** (you need a rule for every possible situation, and they don't generalize).

### System 5: Knowledge Graphs -- The Fact Encyclopedia

You store millions of specific facts as triples:

```
(Albert Einstein, Born In, Germany)
(Albert Einstein, Discovered, Theory of Relativity)
(Theory of Relativity, Related To, Physics)
```

The power is in **graph traversal for inference**: if you ask "Did Einstein contribute to Physics?", the system walks the graph: Einstein → Discovered → Theory of Relativity → Related To → Physics. Yes!

---

⚠️ **Common Misconception**: Students often think these five methods are "versions" of the same thing (1.0, 2.0, etc.). They are NOT. They are **five different paradigms** -- each stores knowledge in a fundamentally different way and supports different kinds of reasoning. The slide explicitly states: "They are different KR paradigms, not different types of Knowledge Graphs."

⚠️ **Common Misconception**: Semantic Networks and Knowledge Graphs look similar (both are graphs), but they differ in **standardization** and **scale**. Semantic Networks have no unified standard and are typically small/domain-specific (1960s--1980s research). Knowledge Graphs use standardized RDF triples and are designed for web-scale (billions of facts, 2000s--present).

💡 **Core Intuition**: KR is about choosing which "filing system" to organize knowledge -- as logic, mind maps, forms, rules, or fact graphs -- so machines can reason, not just store.

---

## 📐 正式定义（Formal Definition）

### What is Knowledge Representation?

**Definition (from slides):** Knowledge Representation (KR) refers to the methods used in AI to **store**, **retrieve**, and **handle** knowledge to enable intelligent reasoning.

**Why do we need KR?**
- Bridges raw data and intelligent decision-making
- Allows AI to reason logically and infer new facts
- Enables knowledge-driven applications (expert systems, search engines, autonomous robots, chatbots)

### Five Key Requirements of KR

| Requirement | Description | Example (from slides) |
|---|---|---|
| **Expressiveness**（表达力） | Can represent **complex and abstract** knowledge | A self-driving car must represent traffic rules, pedestrian movement, road conditions |
| **Computational Efficiency**（计算效率） | Can **process information quickly** | AI fraud detection must analyze thousands of transactions per second |
| **Scalability**（可扩展性） | Can **handle large and growing** knowledge bases | Google's Knowledge Graph contains **billions** of facts and relationships |
| **Interpretability**（可解释性） | Humans can **understand** how AI makes decisions | AI medical diagnosis must provide **clear reasoning** for treatment recommendations |
| **Modifiability**（可修改性） | Can **update itself** with new knowledge | AI chatbots must constantly **learn** from new conversations |

**Case Study from slides: Self-Driving Car**
- **Expressiveness** → represents road conditions, traffic signals, vehicle movement
- **Computational Efficiency** → processes sensor data in real-time for immediate decisions
- **Scalability** → expands knowledge of new routes and driving patterns
- **Interpretability** → AI must explain why it brakes or changes lanes
- **Modifiability** → updates driving models based on new road conditions

### Structured vs Unstructured Knowledge

| Feature | Structured Knowledge | Unstructured Knowledge |
|---|---|---|
| **Format** | Organized in tables, graphs, or schemas | Free-form (text, images, videos) |
| **Storage** | Databases, ontologies, knowledge graphs | Documents, multimedia files |
| **Processing** | Fast and efficient queries | Requires NLP, deep learning |
| **Interpretability** | High -- easy to understand | Low -- requires advanced AI |
| **Flexibility** | Rigid -- schema-dependent | Flexible -- can capture complex knowledge |

**Examples of Structured:** Relational databases (SQL), Knowledge Graphs (Google KG), Ontologies (medical taxonomy)

**Examples of Unstructured:** News articles, research papers, videos, images, audio recordings, conversations, emails

### Symbolic Logic in KR

**Definition:** Represents knowledge using **formal symbols** and **logical expressions**. Used for reasoning, inference, and formal verification.

Two types used in KR:
- **Propositional Logic (PL)** -- simple true/false statements
- **First-Order Logic (FOL)** -- allows relationships between entities with quantifiers

**FOL Rules Example (Medical Diagnosis):**
- $\forall x\ (\text{Flu}(x) \rightarrow \text{HasSymptom}(x, \text{Fever}))$ -- "If a patient has the flu, they will have a fever"
- $\forall x\ (\text{HasSymptom}(x, \text{Fever}) \wedge \text{HasSymptom}(x, \text{Cough}) \rightarrow \text{LikelyDiagnosis}(x, \text{Flu}))$ -- AI can infer from known symptoms to diagnose patients

### Semantic Networks -- Formal Structure

A **graph-based** KR where:
- **Nodes (Entities/Concepts):** represent objects, ideas, or concepts (e.g., "Cat", "Mammal", "Animal")
- **Edges (Relationships/Connections):** define how entities are related (e.g., "is-a", "has-part", "related-to")

**Two key inference mechanisms:**

1. **Hierarchical Reasoning (IS-A Inference):** Given "Cat → is-a → Mammal" and "Mammal → is-a → Animal", AI infers "Cat is an Animal" via transitive inheritance

2. **Property Inheritance:** Given "Mammal → has-property → Warm-blooded" and "Dog → is-a → Mammal", AI infers "Dog is warm-blooded" (inherits properties from parent)

**Strengths of Semantic Networks:**
1. **Natural Representation** -- mimics human thought; relationships are intuitive and visually clear
2. **Supports Logical Inference** -- AI can deduce new facts through IS-A and HAS-PROPERTY relationships
3. **Efficient Knowledge Retrieval** -- graph structures allow fast lookups using connected nodes

**Weaknesses of Semantic Networks:**
1. **Can Become Too Complex** -- large networks with millions of nodes can be hard to manage
2. **No Standardized Representation** -- different AI models use different graph structures; integration is difficult
3. **Poor Handling of Uncertainty** -- assumes relationships are deterministic (e.g., "Birds can fly" -- but what about penguins?)

### Frames -- Formal Structure

A **frame** is a structured representation that groups related information about an entity into a **slot-filler** structure.

- A **frame** = concept/object
- A **slot** = attribute/property
- A **filler** = value for that slot

**Frame-Based Reasoning (four mechanisms):**

1. **Default Values:** If a slot is empty, AI uses default knowledge. Example: Frame **Dog**, Slot **Has legs** → Default value = 4. AI infers a newly introduced dog has 4 legs unless specified otherwise.

2. **Inheritance (Frame Hierarchies):** Frames inherit attributes from higher-level frames (similar to OOP). Example: Frame **Mammal** → Has Hair = True; Frame **Dog** (inherits from Mammal) → Has Hair = True.

3. **Slot Constraints & Conditions:** Some slots have restrictions on valid values. Example: Frame **Student**, Slot **Age** → Constraint: Must be > 5 years old.

4. **Procedural Attachment:** Some slots trigger actions when accessed. Example: Frame **Hotel Reservation**, Slot **Check-in Time** → Action: Send confirmation email.

**Strengths of Frames:**
1. **Structured & Organized** -- groups related knowledge into slot-filler structures for efficient retrieval
2. **Inheritance and Default Reasoning** -- infers missing values using defaults and hierarchical inheritance
3. **Procedural Knowledge** -- slots can trigger actions (procedural attachments)
4. **Easy to Update & Modify** -- slots and fillers can be modified dynamically

**Weaknesses of Frames:**
1. **Rigid Structure & Limited Flexibility** -- struggle with ambiguous or novel cases (e.g., a "Vehicle" frame might not account for futuristic self-driving cars)
2. **Poor Handling of Uncertainty** -- assume knowledge is complete; difficult to reason with probabilities
3. **Hard to Scale for Large Knowledge Bases** -- grow complex as entities and slots increase
4. **Limited Logical Reasoning** -- do not perform deep logical deductions (can store "All birds can fly" but don't automatically reason exceptions like penguins)

### Rule-Based Systems -- Formal Structure

A Rule-Based System (RBS) represents knowledge as a set of **IF-THEN** rules that trigger actions when conditions are met.

**Structure:** IF (Condition) → THEN (Action/Conclusion). AI checks facts and applies the appropriate rule.

**Strengths:**
1. **Transparent and Explainable** -- every decision is based on clear, human-readable IF-THEN rules
2. **Easy to Implement for Well-Defined Problems** -- works effectively in structured domains with known rules
3. **Works Without Large Training Data** -- does not require massive datasets (unlike ML)

**Weaknesses:**
1. **Hard to Scale with Complex Knowledge** -- managing thousands of IF-THEN rules becomes difficult
2. **Poor Adaptability to New Situations** -- cannot generalize beyond predefined rules
3. **Requires Expert Knowledge to Define Rules** -- rules must be handcrafted by domain experts

### Knowledge Graphs -- Formal Structure

A KG is a **graph-based** representation that connects **entities** (nodes) with **relationships** (edges) and **properties**.

**Components:**
- **Nodes** = Entities/Subjects (people, places, objects)
- **Edges** = Relationships/Predicates
- **Properties** = Attributes of entities or relations

**RDF Triple format:** (Subject, Predicate, Object) = (Head, Relation, Tail)

**Four types of KG inference (from slides):**
1. **Transitive Inference**: $(A \rightarrow B, B \rightarrow C) \Rightarrow (A \rightarrow C)$. Example: "Einstein discovered Theory of Relativity" + "Theory of Relativity is part of Physics" ⇒ "Einstein contributed to Physics"
2. **Relationship Expansion**: Identify hidden connections. Example: if two lectures are taught by the same professor, infer a collaboration link
3. **Entity Disambiguation**: Distinguish entities with similar names. Example: "Apple (Company)" vs. "Apple (Fruit)"
4. **Question Answering**: Retrieve structured answers. Example: "Who invented the telephone?" → Alexander Graham Bell (from graph relations)

**Strengths of Knowledge Graphs:**
1. **Highly Structured & Interpretable** -- provides clearly defined relationships between entities
2. **Enables Inference & Knowledge Discovery** -- infer missing knowledge based on known relationships
3. **Scalable for Large-Scale KR** -- works well with millions of facts and relationships
4. **Supports Multi-Domain Knowledge Integration** -- combine medical, scientific, business knowledge into one system

**Weaknesses of Knowledge Graphs:**
1. **Incomplete Knowledge & Data Sparsity** -- if information is missing, AI cannot infer accurate answers
2. **High Maintenance & Complexity** -- requires constant updates to add new entities and relationships

---

## 🔄 机制与推导（How It Works）

### How Semantic Network Inference Works -- Step by Step

```
Given knowledge:
  Cat ──is-a──► Mammal ──is-a──► Animal
  Mammal ──has-property──► Warm-blooded
  Cat ──has──► Fur

Step 1: Query "Is Cat an Animal?"
  Traverse: Cat → is-a → Mammal → is-a → Animal
  Answer: YES (transitive IS-A inference)

Step 2: Query "Is Cat warm-blooded?"
  Cat → is-a → Mammal → has-property → Warm-blooded
  Answer: YES (property inheritance)

Step 3: Query "Does Dog have Fur?"
  Dog → is-a → Mammal (known)
  Mammal ──has──► ? (no "has Fur" on Mammal)
  Answer: CANNOT INFER (Fur is a property of Cat specifically, 
          not inherited through Mammal)
```

### How Frame Reasoning Works -- Step by Step

**Scenario (Exercise 3 from slides):** An AI healthcare assistant uses Frames.

Patient **Alice** reports: **fever** and **headache**.

| Frame: Patient | Slot | Filler |
|---|---|---|
| Alice | Age | 25 |
| | Symptoms | Fever, Headache |
| | Family History | None |
| | Recent Travel | Tropical regions (2 weeks ago) |
| | Vaccination History | No recent travel vaccines |

| Frame: Malaria | Slot | Filler |
|---|---|---|
| Malaria | Common Symptoms | Fever, Headache, Chills |
| | Transmission Risk | High in tropical regions |
| | Prevention | Vaccination |

**Reasoning process:**
1. **Slot matching**: Alice's symptoms (Fever, Headache) match Malaria's Common Symptoms (Fever, Headache, Chills) -- 2 out of 3 match
2. **Cross-frame inference**: Alice's Recent Travel = "Tropical regions" matches Malaria's Transmission Risk = "High in tropical regions"
3. **Default/constraint check**: Alice has no travel vaccines (Vaccination History slot) and Malaria's Prevention = Vaccination → increased susceptibility
4. **Conclusion**: Malaria flagged as potential diagnosis

### How Rule-Based Systems Work -- Step by Step

**Scenario (Exercise 4 from slides):** Fire detection system.

| Rule ID | IF Condition | THEN Conclusion |
|---|---|---|
| R1 | Temperature > 60C AND Smoke Detected | Trigger Fire Alarm |
| R2 | Temperature > 80C | Trigger Emergency Evacuation |
| R3 | Carbon Monoxide > Safe Limit | Alert Building Manager |
| R4 | Sprinklers Activated AND Smoke Detected | Confirm Fire |

**Current sensor readings:** Temperature = 85C, Smoke = YES, Carbon Monoxide = Safe, Sprinklers = NO

**Forward chaining:**
1. Check R1: Temperature (85) > 60C ✅ AND Smoke Detected ✅ → **Fire Alarm triggered**
2. Check R2: Temperature (85) > 80C ✅ → **Emergency Evacuation triggered**
3. Check R3: Carbon Monoxide = Safe ❌ → R3 does NOT fire
4. Check R4: Sprinklers = NO ❌ → R4 does NOT fire

**Final actions:** Trigger Fire Alarm (R1) + Trigger Emergency Evacuation (R2)

### How Knowledge Graph Inference Works -- Step by Step

**Scenario (Exercise 5 from slides):** Historical figures KG.

| Entity (Node) | Relation (Edge) | Entity (Node) |
|---|---|---|
| Isaac Newton | Discovered | Law of Gravity |
| Law of Gravity | Related To | Physics |
| Albert Einstein | Contributed To | Physics |
| Albert Einstein | Developed | Theory of Relativity |
| Theory of Relativity | Related To | Gravity |
| Theory of Relativity | Influenced By | Law of Gravity |

**Query:** "Did Isaac Newton's discoveries influence Albert Einstein?"

**Graph traversal:**
```
Newton ──Discovered──► Law of Gravity
                            │
                      Influenced ▼
                  Theory of Relativity ◄──Developed── Einstein
```

Path: Newton → Discovered → Law of Gravity → Influenced → Theory of Relativity ← Developed ← Einstein

**Answer:** YES -- Newton's Law of Gravity influenced Einstein's Theory of Relativity. The graph does not connect them *directly*, but AI can infer the relationship by traversing the graph.

---

## ⚖️ 权衡分析（Trade-offs & Comparisons）

### Complete KR Methods Comparison Table

| Feature | Symbolic Logic | Semantic Networks | Frames | Rule-Based Systems | Knowledge Graphs |
|---|---|---|---|---|---|
| **Core idea** | Formal logical expressions (PL, FOL) | Nodes = concepts, edges = relationships | Slot-filler structures (object-like) | IF-THEN rules for decisions | Entity-relation-entity triples |
| **Representation** | Mathematical formulas | Graph (nodes + edges) | Structured records (slots + fillers) | Production rules | RDF triples (S, P, O) |
| **Reasoning** | Formal proof / inference rules | Transitive IS-A, property inheritance | Default values, inheritance, constraints | Forward/backward chaining | Graph traversal, SPARQL, embeddings |
| **Expressiveness** | Very high (FOL is very expressive) | Moderate (limited to graph relations) | Moderate (limited to predefined slots) | Low-moderate (specific rules only) | High (flexible triple format) |
| **Scalability** | Poor (inference is expensive) | Poor (no standard, hard to integrate) | Poor (complex with many entities) | Poor (rule explosion at scale) | Excellent (web-scale, billions of triples) |
| **Interpretability** | High (formal, auditable) | High (visual, intuitive) | High (structured, readable) | High (every rule is traceable) | Moderate (triples readable but paths long) |
| **Uncertainty** | No (inherently crisp) | No (deterministic) | No (assumes completeness) | Limited (MYCIN adds confidence factors) | KG embeddings handle soft reasoning |
| **Standardization** | Standard (FOL is universal) | No unified standard | No unified standard | Domain-specific | Standards-based (RDF, OWL) |
| **Era** | 1950s--present | 1960s--1980s | 1970s--1980s | 1970s--1980s | 2000s--present |
| **Example** | Prolog, theorem provers | Early AI research models | Object-oriented KBs | MYCIN, R1/XCON | Google KG, Wikidata |

### Differences Between KR Methods (from slides)

| Method | Core Idea | Example |
|---|---|---|
| **Semantic Networks** | Knowledge as **connected concepts** | Bird → is-a → Animal |
| **Frames** | Knowledge as **objects with attributes** | Frame: Bird; wings=2; can_fly=yes |
| **Knowledge Graphs** | Knowledge as **entities and relations in triples** | (Bird, is_a, Animal) |

**Key distinction (from slides):**
- Semantic Network: Early graph-based KR using nodes and links. No unified standard. Small/domain-specific.
- Knowledge Graph: A large-scale, **standardized** graph using **RDF triples**. Designed for web-scale.
- KGs can be viewed as a **modern, large-scale implementation and extension** of the original Semantic Network concept.

### When to Choose Which?

| Scenario | Best Method | Rationale |
|---|---|---|
| Need precise mathematical proof | **Symbolic Logic** | Formal inference, verification |
| Small domain, visual concept relationships | **Semantic Networks** | Intuitive, supports IS-A inheritance |
| Describing entities with structured attributes | **Frames** | Slot-filler structure, default values |
| Well-defined decision process, explainable | **Rule-Based System** | Transparent IF-THEN rules, no training data |
| Web-scale fact retrieval, millions of entities | **Knowledge Graph** | Scalable, standardized (RDF), supports embeddings |
| Combining multiple approaches | **Hybrid** | Real systems often combine ontology (schema) + KG (facts) + rules (decisions) |

### KR Landscape (from slides)

```
                Knowledge Representation
                         │
          ┌──────────────┼──────────────┐
     Logic-based     Graph-based    Structured/Rule-based
          │           │       │           │          │
    Symbolic     Semantic   Knowledge   Frames   Rule-based
     Logic      Networks    Graphs               Systems
```

**Key takeaway from slides:** "There is **no single best KR method**. Different methods have different strengths in representation, inference, scalability, and interpretability. In practice, AI systems may combine multiple KR methods to solve real-world problems."

---

## 🏗️ 设计题答题框架

**Prompt type:** "Compare different KR methods and explain which you would choose for [scenario]. Justify your choice."

### WHAT
Identify which KR methods are relevant:
- "For this scenario, I would compare **Semantic Networks**, **Frames**, **Rule-Based Systems**, and **Knowledge Graphs** as candidate approaches..."
- "The primary representation would be a **Knowledge Graph** with an **ontology** providing the schema..."

### WHY
Justify based on the 5 KR requirements:
- **Expressiveness**: "A KG can represent diverse entity types and relationship types via flexible triples"
- **Computational Efficiency**: "Rule-based systems offer fast decision-making via direct rule matching"
- **Scalability**: "KGs scale to billions of triples; frames and rule-based systems do not"
- **Interpretability**: "Rule-based systems are the most transparent -- every conclusion traces to a human-readable rule"
- **Modifiability**: "KGs can be updated by adding new triples without restructuring the entire system"

### HOW
Describe the architecture:
1. Choose the primary KR method and explain its structure
2. Show how knowledge is stored (e.g., as triples, as frames, as rules)
3. Explain how inference works (e.g., graph traversal, property inheritance, forward chaining)

### TRADE-OFF
Discuss what you sacrifice:
- "Semantic Networks are intuitive but lack standardization and cannot handle uncertainty"
- "Rule-Based Systems are transparent but brittle and hard to scale beyond ~10K rules"
- "Frames are structured but rigid and cannot reason with probabilities"
- "KGs are scalable but may be incomplete and require maintenance"

### EXAMPLE
Walk through a concrete scenario:
- "A medical AI receives symptom data. Using a KG: (Patient, hasSymptom, Fever), (Patient, hasSymptom, Cough). Graph traversal finds: (Flu, hasSymptom, Fever), (Flu, hasSymptom, Cough). Match! Suggest Flu as possible diagnosis."

---

## 📝 历年真题 + 课堂练习（Exercises 1--5 from Slides）

### Exercise 1 -- Structured vs Unstructured Knowledge

> **Question:** Which of the following is an example of **structured** knowledge?
> 
> A) A collection of handwritten medical prescriptions.
> B) A database storing customer purchase histories.
> C) A video recording of a classroom lecture.
> D) A set of research papers in PDF format.

<details>
<summary>Click to reveal answer</summary>

**Answer: B** -- A database storing customer purchase histories.

**Reasoning:** Structured knowledge is organized in a **predefined format** like databases, tables, or knowledge graphs. A database has rows, columns, and a schema -- this is structured. Handwritten prescriptions (A), video recordings (C), and PDF research papers (D) are all **unstructured** because they do not follow a predefined machine-readable format.

</details>

---

### Exercise 2 -- Semantic Network Inference

> **Question:** Which of the following **best demonstrates inference** in a Semantic Network?
> 
> A) A chatbot randomly generating responses.
> B) AI deducing that "whales are mammals" based on an "is-a" relationship.
> C) A search engine ranking web pages based on popularity.
> D) A neural network recognizing images of cats.

<details>
<summary>Click to reveal answer</summary>

**Answer: B** -- AI deducing that "whales are mammals" based on an "is-a" relationship.

**Detailed reasoning:**
- **A incorrect:** A chatbot that **randomly generates responses** is not performing logical inference. In a Semantic Network, **inference relies on relationships between concepts**.
- **B correct:** Semantic Networks allow AI to infer properties and relationships based on hierarchical connections (e.g., IS-A and HAS-PROPERTY). Deducing that whales are mammals via an IS-A relationship is exactly this kind of inference.
- **C incorrect:** Search engines (like Google) rank web pages based on **user behavior** (e.g., clicks, backlinks, and SEO techniques), not by **inference** from a structured knowledge representation.
- **D incorrect:** Neural networks process **unstructured data** (images, text, speech) through pattern recognition but do not inherently **infer new relationships** based on **existing symbolic knowledge**.

</details>

---

### Exercise 3 -- Frame-Based Reasoning (Healthcare)

> **Scenario:** An AI-powered healthcare assistant uses **Frames** to manage patient medical records and suggest possible diagnoses.
> 
> Patient Alice reports: **fever** and **headache**.
>
> | Frame: Patient | Slot | Filler |
> |---|---|---|
> | Alice | Age | 25 |
> | | Symptoms | Fever, Headache |
> | | Family History | None |
> | | Recent Travel | Tropical regions (2 weeks ago) |
> | | Vaccination History | No recent travel vaccines |
>
> | Frame: Malaria | Slot | Filler |
> |---|---|---|
> | Malaria | Common Symptoms | Fever, Headache, Chills |
> | | Transmission Risk | High in tropical regions |
> | | Prevention | Vaccination |
>
> **Question:** What is the most likely reason the AI flags **Malaria** as a potential diagnosis?
> 
> A) Alice has a family history of malaria.
> B) Malaria is common in all patients with pain in the lungs.
> C) Malaria is common in Age from 20 to 30.
> D) Alice recently traveled to a high-risk area and shows matching symptoms.

<details>
<summary>Click to reveal answer</summary>

**Answer: D** -- Alice recently traveled to a high-risk area and shows matching symptoms.

**Reasoning:** Alice has **two key symptoms matching Malaria** (fever & headache); she traveled to a **malaria-prone region** two weeks ago (within incubation period); she has **not received a malaria vaccine**, increasing susceptibility. The frame system matches slots across the Patient frame and the Malaria frame to identify the overlap.

- A is incorrect: Family History = None
- B is incorrect: Alice has no lung pain symptoms
- C is incorrect: There is no age-based rule in the Malaria frame

</details>

---

### Exercise 4 -- Rule-Based System (Fire Detection)

> **Scenario:** Rule-Based AI system for **fire detection** in a smart building.
>
> | Rule ID | IF Condition | THEN Conclusion |
> |---|---|---|
> | R1 | Temperature > 60C **AND** Smoke Detected | Trigger Fire Alarm |
> | R2 | Temperature > 80C | Trigger Emergency Evacuation |
> | R3 | Carbon Monoxide > Safe Limit | Alert Building Manager |
> | R4 | Sprinklers Activated **AND** Smoke Detected | Confirm Fire |
>
> **Current Sensor Readings:** Temperature = 85C, Smoke Detected = YES, Carbon Monoxide = Safe, Sprinklers Activated = NO
>
> **Question:** What actions will the AI take?
> 
> A) Trigger Fire Alarm and Emergency Evacuation.
> B) Only Alert the Building Manager.
> C) Only Trigger the Fire Alarm.
> D) Confirm Active Fire and Trigger Evacuation.

<details>
<summary>Click to reveal answer</summary>

**Answer: A** -- Trigger Fire Alarm and Emergency Evacuation.

**Reasoning (forward chaining):**
1. **R1** fires: Temperature (85) > 60C ✅ AND Smoke Detected ✅ → **Fire Alarm** triggered
2. **R2** fires: Temperature (85) > 80C ✅ → **Emergency Evacuation** triggered
3. **R3** does NOT fire: Carbon Monoxide is at safe level ❌
4. **R4** does NOT fire: Sprinklers are NOT activated ❌ (so AI cannot confirm active fire)

**Final AI Actions:** Trigger Fire Alarm (R1) + Trigger Emergency Evacuation (R2)

**Why not D?** R4 requires Sprinklers Activated = YES, but sprinklers are NOT activated, so fire cannot be confirmed.

</details>

---

### Exercise 5 -- Knowledge Graph Inference (Historical Figures)

> **Scenario:** An AI system uses a Knowledge Graph for historical figures and scientific discoveries.
>
> | Entity (Node) | Relation (Edge) | Entity (Node) |
> |---|---|---|
> | Isaac Newton | Discovered | Law of Gravity |
> | Law of Gravity | Related To | Physics |
> | Albert Einstein | Contributed To | Physics |
> | Albert Einstein | Developed | Theory of Relativity |
> | Theory of Relativity | Related To | Gravity |
> | Theory of Relativity | Influenced By | Law of Gravity |
>
> **Question:** Did Isaac Newton's discoveries influence Albert Einstein?
> 
> A) No, no direct link between Newton and Einstein.
> B) Yes, Einstein contributed to Physics, and Physics includes Gravity.
> C) Yes, Newton discovered Law of Gravity, and Theory of Relativity was influenced by it.
> D) No, Einstein worked on different theories.

<details>
<summary>Click to reveal answer</summary>

**Answer: C** -- Yes, because Newton discovered the Law of Gravity, and the Theory of Relativity was influenced by it.

**Reasoning (graph traversal):**
The graph does NOT directly connect Newton to Einstein, but AI can infer by **traversing** the graph:
1. Newton → Discovered → Law of Gravity
2. Law of Gravity → Influenced → Theory of Relativity
3. Einstein → Developed → Theory of Relativity

Therefore, Newton's discovery (Law of Gravity) influenced Einstein's work (Theory of Relativity).

**Why not A?** While there is no *direct* edge between Newton and Einstein, KG inference works precisely by finding *indirect* paths through graph traversal.

**Why not B?** Although technically true, this reasoning path is weaker -- the question asks about *influence*, and the direct influence path is through Law of Gravity → Theory of Relativity, not through the generic "Physics" node.

</details>

---

## 🌐 英语表达要点（English Expression）

### Defining KR Methods

```
"Knowledge Representation refers to the methods used in AI to store,
 retrieve, and handle knowledge to enable intelligent reasoning."

"A Semantic Network is a graph-based KR method where nodes represent
 concepts and edges represent relationships such as IS-A and HAS-PROPERTY."

"A Frame is a structured representation that groups related information
 about an entity into a slot-filler structure, enabling inheritance
 and default reasoning."

"A Rule-Based System encodes domain knowledge as a set of IF-THEN
 production rules, providing transparent and explainable decision-making."

"A Knowledge Graph is a graph-based representation that connects
 entities (nodes) with relationships (edges), storing facts as
 RDF triples in the form (Subject, Predicate, Object)."
```

### Comparing Methods

```
"While Semantic Networks represent knowledge as interconnected concept
 nodes, Knowledge Graphs use standardized RDF triples and are designed
 for web-scale applications with billions of facts."

"Unlike Rule-Based Systems, which require manually crafted IF-THEN rules,
 Knowledge Graphs can be populated semi-automatically using NLP techniques
 such as Named Entity Recognition and Relation Extraction."

"Frames organize knowledge similarly to objects in programming, with
 slots (attributes) and fillers (values), whereas Semantic Networks
 focus on the relationships between concepts rather than their attributes."

"The fundamental trade-off between Rule-Based Systems and Knowledge Graphs
 is interpretability versus scalability: rules are transparent but brittle
 at scale, while KGs scale to billions of facts but paths can be opaque."
```

### Discussing Requirements

```
"A good KR system must balance five requirements: expressiveness,
 computational efficiency, scalability, interpretability, and modifiability."

"The choice of KR method depends on the application's priorities --
 for example, medical diagnosis systems prioritize interpretability,
 while web search engines prioritize scalability."
```

### 易错词汇

| Confused Pair | Distinction |
|---|---|
| **Semantic Network** vs **Knowledge Graph** | Semantic Network: early, no standard, small-scale. KG: modern, standardized (RDF), web-scale |
| **Frame** vs **Object (OOP)** | Frames are KR structures for AI reasoning with inheritance and defaults; OOP objects are programming constructs |
| **Slot** vs **Property** vs **Attribute** | In frames: slot = attribute = property. In KGs: property = attribute of an entity or relation |
| **Structured** vs **Unstructured** | Structured = predefined schema (databases, KGs). Unstructured = no schema (text, images) |
| **Inference** vs **Retrieval** | Inference = derive NEW knowledge from existing facts. Retrieval = find existing stored facts |
| **Forward chaining** vs **Backward chaining** | Forward = data → conclusion (what can I infer?). Backward = goal → evidence (is this true?) |

---

## ✅ 自测检查清单

- [ ] Can I define Knowledge Representation and its purpose in one sentence?
- [ ] Can I list and explain the 5 key requirements of KR (Expressiveness, Computational Efficiency, Scalability, Interpretability, Modifiability)?
- [ ] Can I explain the difference between Structured and Unstructured Knowledge with examples?
- [ ] Can I describe how Symbolic Logic (PL + FOL) is used in KR?
- [ ] Can I draw a Semantic Network and explain IS-A inference and property inheritance?
- [ ] Can I name 3 strengths and 3 weaknesses of Semantic Networks?
- [ ] Can I describe a Frame with its slots and fillers, and explain the 4 reasoning mechanisms (defaults, inheritance, constraints, procedural attachment)?
- [ ] Can I name 4 strengths and 4 weaknesses of Frames?
- [ ] Can I write an IF-THEN rule and trace forward chaining through a set of rules?
- [ ] Can I name 3 strengths and 3 weaknesses of Rule-Based Systems?
- [ ] Can I explain Knowledge Graph structure (nodes, edges, properties) and write RDF triples?
- [ ] Can I name the 4 types of KG inference (transitive, relationship expansion, entity disambiguation, QA)?
- [ ] Can I name 4 strengths and 2 weaknesses of Knowledge Graphs?
- [ ] Can I compare all five KR methods in a table (core idea, representation, reasoning, strengths, weaknesses)?
- [ ] Can I explain the KR Landscape diagram showing logic-based, graph-based, and structured/rule-based categories?
- [ ] Can I solve all 5 exercises from the lecture slides?

---

> **Cross-references:**
> - For Symbolic Logic in depth, see [Propositional Logic & FOL chapter](./A_symbolic_logic.md)
> - For Knowledge Graphs, TransE, and RAG in depth, see [KG for AI chapter](./D_knowledge_graphs.md)
> - For Expert Systems and MYCIN, see [MYCIN chapter](./E_mycin.md)
