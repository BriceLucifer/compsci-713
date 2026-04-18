# Knowledge Representation — Foundations (W3L1)

## 🎯 考试重要度

🟡 **中频** | Week 3 Lecture 1 入门内容 | 样本测试中未直接出现，但为后续 MYCIN（W4L1）、KG Embeddings（Q3）的理论基础

> **Why study this?** MYCIN builds on Expert System concepts. KG Embeddings (Sample Test Q3) build on Knowledge Graph concepts. Comparison questions (Expert Systems vs Ontologies vs KG) are a very natural exam question type for this material. Understanding the DIKW pyramid helps frame all AI knowledge tasks.

---

## 📖 核心概念（Core Concepts）

| English Term | 中文 | One-line Definition |
|---|---|---|
| Knowledge Representation (KR)（知识表示） | 知识表示 | The study of how to store, organize, and reason over structured knowledge in AI systems |
| DIKW Pyramid（DIKW金字塔） | DIKW金字塔 | A hierarchy: raw Data → contextualized Information → actionable Knowledge → judgmental Wisdom |
| Expert System（专家系统） | 专家系统 | AI system that encodes human expert knowledge as IF-THEN production rules and uses an inference engine to reason |
| Production Rule（产生式规则） | 产生式规则 | An IF-THEN rule encoding expert knowledge: IF [condition] THEN [conclusion/action] |
| Knowledge Base (KB)（知识库） | 知识库 | The component of an expert system that stores all domain rules and facts |
| Inference Engine（推理引擎） | 推理引擎 | The component that applies rules to known facts to derive new conclusions |
| Ontology（本体论） | 本体论 | A formal, explicit specification of concepts, relationships, and constraints in a domain |
| OWL (Web Ontology Language)（网络本体语言） | 网络本体语言 | A W3C standard for defining ontologies with logical reasoning capabilities on the Semantic Web |
| RDF (Resource Description Framework)（资源描述框架） | 资源描述框架 | A W3C standard for representing facts as (Subject, Predicate, Object) triples |
| Knowledge Graph (KG)（知识图谱） | 知识图谱 | A large-scale graph storing real-world entities and their relationships as RDF triples |
| Triple（三元组） | 三元组 | The atomic unit of a KG: (Subject, Predicate, Object) — e.g., (Einstein, bornIn, Germany) |
| RAG (Retrieval-Augmented Generation)（检索增强生成） | 检索增强生成 | A technique that combines LLMs with external knowledge retrieval to produce factually grounded responses |
| Hallucination（幻觉） | 幻觉 | When an LLM generates plausible-sounding but factually incorrect information |

---

## 🧠 费曼草稿（Feynman Draft）

### The Library Analogy

Imagine you are building a library for a robot. The robot needs to answer questions about the world, but it cannot just read raw books — it needs the knowledge organized in a way that supports *reasoning*, not just storage. This is exactly the problem of **Knowledge Representation**: how do you structure knowledge so that a machine can not only store it, but also think with it?

### The DIKW Pyramid — From Noise to Wisdom

Think of it like processing raw ingredients into a meal:

```
          Wisdom         ← "Should I invest in this stock?" (judgment + context)
         /      \
      Knowledge          ← "When prices drop after earnings, they usually recover" (patterns)
       /      \
   Information           ← "Stock price dropped 5% after earnings report" (contextualized)
    /      \
  Data                   ← "42.37, 44.50, 39.81, ..." (raw numbers, no context)
```

- **Data（数据）**: Raw symbols with no meaning. The number `39.81` by itself tells you nothing.
- **Information（信息）**: Data + context. "The stock price of ACME Corp was $39.81 on March 1st."
- **Knowledge（知识）**: Information + patterns. "ACME's stock tends to drop 3-7% after quarterly earnings reports, then recover within 2 weeks."
- **Wisdom（智慧）**: Knowledge + judgment. "Despite the drop, I should hold because the pattern shows recovery, and this quarter's fundamentals are strong."

**Toy example with numbers:**

| Level | Example |
|---|---|
| Data | `37.2, 101, 30` |
| Information | "Patient has temperature 37.2C, heart rate 101 bpm, age 30" |
| Knowledge | "Heart rate > 100 in an adult may indicate tachycardia" |
| Wisdom | "Given the patient's age and no fever, order an ECG before prescribing medication" |

Each level adds *meaning* on top of the previous one. AI systems operate at different levels — a database stores data; a knowledge graph stores knowledge; an expert system tries to reach wisdom.

### Three Ways to Organize Knowledge

Now, back to our robot library. There are three fundamentally different shelving systems:

**System 1 — Expert Systems (The Rulebook):** You interview a human expert and write down every decision they make as an IF-THEN rule. "IF patient has fever AND cough, THEN diagnose as possible flu." The robot reads through its rulebook, checks which rules match the current situation, and fires them. This is explicit, transparent, and auditable — but you need a rule for *every* situation, and that doesn't scale.

**System 2 — Ontologies (The Classification Manual):** Instead of writing specific rules, you define the *types* of things that exist and how they can relate. "Medicine is a class. Disease is a class. A Medicine *treats* a Disease." This is a schema — it doesn't say *which* medicine treats *which* disease, but it defines what *kinds* of statements are valid. Think of it as a grammar book: it tells you what sentences are legal, not what to say.

**System 3 — Knowledge Graphs (The Fact Encyclopedia):** You store millions of specific facts as triples: (Aspirin, treats, Headache), (Einstein, bornIn, Germany), (Python, isA, ProgrammingLanguage). The robot can traverse this web of facts to answer questions. Need to know if Newton influenced Einstein? Follow the chain: Newton → discovered → GravityLaw → influenced → Relativity ← developed ← Einstein. Yes!

And then there's the modern twist:

**RAG — The Librarian + the Storyteller:** An LLM (like GPT) is a great storyteller but sometimes makes things up. RAG adds a librarian step: before answering, the LLM first searches its knowledge base (KG, documents, etc.) for relevant facts, then incorporates those facts into its answer. The storyteller now has a fact-checker.

---

⚠️ **Common Misconception**: Students often think Expert Systems, Ontologies, and Knowledge Graphs are three levels of the same thing (like versions 1.0, 2.0, 3.0). They are **not**. They are three *different approaches* to the same problem — each with distinct strengths. In practice, a real AI system often combines all three: an ontology defines the schema, a KG stores the facts, and an expert system layer applies rules for decision-making.

💡 **Core Intuition**: KR is about choosing *how* to structure knowledge — as rules (expert systems), schemas (ontologies), or fact graphs (KGs) — so that machines can reason, not just store.

---

## 📐 正式定义（Formal Definition）

### What is Knowledge Representation?

Knowledge Representation (KR) is the field of AI concerned with:
1. **Storing** knowledge in a machine-processable format
2. **Organizing** knowledge into structured, retrievable forms
3. **Reasoning** over knowledge to derive new conclusions

A KR system must satisfy five requirements:

| Requirement | Description | Example |
|---|---|---|
| **Expressiveness**（表达力） | Can represent complex and abstract knowledge | Self-driving car understanding traffic rules |
| **Computational Efficiency**（计算效率） | Can process information quickly | Fraud detection analyzing 1000s of transactions/sec |
| **Scalability**（可扩展性） | Can handle large and growing knowledge bases | Google KG with billions of facts |
| **Interpretability**（可解释性） | Humans can understand the AI's reasoning | Medical AI showing why it recommended a drug |
| **Modifiability**（可修改性） | Can be updated with new knowledge | Chatbot learning from new conversations |

### DIKW Pyramid — Formal Definitions

| Level | Definition | In AI Terms |
|---|---|---|
| **Data** | Raw, unprocessed symbols or observations | Sensor readings, log entries, pixel values |
| **Information** | Data placed in context with meaning assigned | Labeled data, structured records |
| **Knowledge** | Information synthesized into patterns and relationships | Rules, ontologies, knowledge graphs |
| **Wisdom** | Knowledge applied with judgment to make decisions | Expert systems with confidence factors, decision support |

### Expert System — Three Components

An Expert System consists of three components working together:

```
             ┌─────────────────────┐
             │    User Interface   │  ← Doctor inputs patient symptoms
             └─────────┬───────────┘
                       │
             ┌─────────▼───────────┐
             │   Inference Engine  │  ← Applies rules to facts
             │  (Forward/Backward  │     to derive conclusions
             │    Chaining)        │
             └─────────┬───────────┘
                       │
             ┌─────────▼───────────┐
             │   Knowledge Base    │  ← IF fever AND cough
             │   (Production Rules │     THEN possible_flu
             │    + Facts)         │
             └─────────────────────┘
```

**Production Rule format:**

```
IF <condition_1> AND <condition_2> AND ... AND <condition_n>
THEN <conclusion> [WITH confidence_factor]
```

**Example (MYCIN-style):**
```
Rule 001:
  IF   the infection type is primary bacteremia
  AND  the suspected portal of entry is the GI tract
  AND  the site of the culture is blood
  THEN there is suggestive evidence (0.7) that the organism is Bacteroides
```

### Ontology — Five Components

| Component | Role | Example |
|---|---|---|
| **Concepts (Classes)** | Categories of entities | `Disease`, `Medicine`, `Symptom` |
| **Instances (Individuals)** | Specific members of a class | `Flu`, `Aspirin`, `Fever` |
| **Relationships (Properties)** | How entities connect | `Medicine treats Disease` |
| **Constraints (Axioms)** | Logical restrictions | "Only Medicine can treat Disease" |
| **Inference Mechanisms** | Rules for deriving new facts | If `Aspirin is-a Painkiller` and `Painkillers treat Headache`, then `Aspirin treats Headache` |

**OWL Example:**
```xml
<owl:Class rdf:ID="Scientist">
  <rdfs:subClassOf rdf:resource="#Person"/>
</owl:Class>
<owl:ObjectProperty rdf:ID="worksIn">
  <rdfs:domain rdf:resource="#Scientist"/>
  <rdfs:range rdf:resource="#ResearchLab"/>
</owl:ObjectProperty>
```

This ontology says: A `Scientist` is a subclass of `Person`, and a `Scientist` `worksIn` a `ResearchLab`.

### Knowledge Graph — Formal Structure

A Knowledge Graph is defined as a tuple $G = (E, R, T)$ where:
- $E$ = set of entities (nodes)
- $R$ = set of relation types (edge labels)
- $T \subseteq E \times R \times E$ = set of triples (edges/facts)

Each triple follows RDF format: **(Subject, Predicate, Object)**

```
(Albert_Einstein, bornIn, Germany)
(Albert_Einstein, discovered, Theory_of_Relativity)
(Theory_of_Relativity, field, Physics)
```

### RAG — Formal Pipeline

$$\text{Response} = \text{LLM}\big(\text{Query} \oplus \text{Retrieve}(Q, \text{KnowledgeBase})\big)$$

Where $\oplus$ denotes concatenation of the query with retrieved context, and $\text{Retrieve}(Q, KB)$ selects the top-$k$ most relevant documents/facts from the knowledge base.

---

## 🔄 机制与推导（How It Works）

### Step-by-Step: How an Expert System Reasons

Consider a simple medical expert system with these rules:

```
R1: IF fever AND cough           THEN possible_flu
R2: IF fever AND rash            THEN possible_measles
R3: IF possible_flu AND age > 65 THEN recommend_antiviral
R4: IF possible_measles          THEN recommend_isolation
```

**Scenario**: Patient has fever, cough, and age = 70.

**Forward Chaining（前向链接）** — data-driven, start from facts:
1. Known facts: {fever, cough, age=70}
2. Check R1: fever ✅ AND cough ✅ → fire → add `possible_flu`
3. Check R2: fever ✅ AND rash ❌ → skip
4. Check R3: possible_flu ✅ AND age>65 ✅ → fire → add `recommend_antiviral`
5. Check R4: possible_measles ❌ → skip
6. **Result**: recommend_antiviral

**Backward Chaining（后向链接）** — goal-driven, start from hypothesis:
1. Goal: Should we `recommend_antiviral`?
2. R3 can conclude this → need: `possible_flu` AND `age > 65`
3. Is `age > 65`? Yes (70). ✅
4. Is `possible_flu` known? No → subgoal: prove `possible_flu`
5. R1 can conclude this → need: `fever` AND `cough`
6. Both present. ✅ → `possible_flu` proven → `recommend_antiviral` proven

### Step-by-Step: How Ontologies Enable Inference

```
Ontology defines:
  - Scientist subClassOf Person
  - Person has property "name" (string)
  - Scientist has property "researchField" (string)
  
Instances:
  - Einstein : Scientist
  - Einstein.researchField = "Physics"
  
Inference (automatic via OWL reasoner):
  - Einstein : Person  (because Scientist subClassOf Person)
  - Einstein has "name" property  (inherited from Person)
```

The ontology acts as a **schema with reasoning power** — unlike a plain database schema, an OWL ontology can automatically derive new class memberships and property assignments.

### Step-by-Step: How a Knowledge Graph Answers Questions

**Query: "What did Einstein discover that is related to Physics?"**

KG triples:
```
(Einstein, discovered, Theory_of_Relativity)
(Einstein, discovered, Photoelectric_Effect)
(Theory_of_Relativity, field, Physics)
(Photoelectric_Effect, field, Physics)
(Einstein, bornIn, Germany)
```

**Graph traversal:**
```
Einstein ──discovered──► Theory_of_Relativity ──field──► Physics ✅
Einstein ──discovered──► Photoelectric_Effect ──field──► Physics ✅
Einstein ──bornIn──► Germany  (not relevant — no path to Physics)
```

**Answer**: Theory of Relativity, Photoelectric Effect

### Step-by-Step: How RAG Works

```
Step 1: User asks "What are the side effects of Metformin?"

Step 2: RETRIEVE — Search the knowledge base
         ├── Sparse retrieval (BM25): keyword match "Metformin" + "side effects"
         └── Dense retrieval (DPR/FAISS): semantic similarity search
         → Retrieved: "Metformin common side effects include nausea,
            diarrhea, and vitamin B12 deficiency."

Step 3: AUGMENT — Prepend retrieved context to the LLM prompt
         Prompt = "[Context: Metformin common side effects include nausea,
                   diarrhea, and vitamin B12 deficiency.]
                   Question: What are the side effects of Metformin?"

Step 4: GENERATE — LLM produces a grounded answer
         "Metformin's common side effects include nausea, diarrhea,
          and potential vitamin B12 deficiency with long-term use."
```

The key insight: the LLM's weights are **not modified**. RAG only provides additional context at inference time.

---

## ⚖️ 权衡分析（Trade-offs & Comparisons）

### Expert Systems vs Ontologies vs Knowledge Graphs

| Feature | Expert Systems | Ontologies | Knowledge Graphs |
|---|---|---|---|
| **Core idea** | IF-THEN rules encoding expert decisions | Formal schema defining valid concepts & relations | Graph of entity-relation-entity fact triples |
| **What it stores** | Rules + working facts | Class hierarchies + constraints + inference rules | Millions/billions of specific facts |
| **Reasoning style** | Rule firing (forward/backward chaining) | Classification + subsumption + constraint checking | Graph traversal + SPARQL queries + embeddings |
| **Expressiveness** | Domain-specific, explicit | Highly expressive (OWL supports FOL fragments) | Flexible (any fact can be a triple) |
| **Scalability** | Poor (rule explosion at ~10K rules) | Moderate (reasoning is NP-hard in expressive OWL) | Excellent (designed for web-scale, billions of triples) |
| **Interpretability** | High (every rule is human-readable) | High (formal, auditable) | Moderate (triples readable, but graph paths can be long) |
| **Maintainability** | Hard (manual rule crafting by experts) | Moderate (schema changes propagate) | Semi-automated (NLP extraction pipelines) |
| **Handles uncertainty** | Limited (MYCIN uses confidence factors) | No (inherently crisp logic) | KG embeddings can handle soft/probabilistic reasoning |
| **Example system** | MYCIN, R1/XCON | Gene Ontology, SNOMED CT | Google KG, Wikidata, DBpedia |
| **Era** | 1970s--1980s | 1990s--2000s | 2000s--present |

### When to Choose Which?

| Scenario | Best Approach | Rationale |
|---|---|---|
| Medical diagnosis with well-defined protocols | **Expert System** | Rules are explicit, auditable, no training data needed |
| Defining a shared vocabulary for a research field | **Ontology** | Need formal class hierarchies and constraints |
| Web-scale fact retrieval ("Who directed Inception?") | **Knowledge Graph** | Need to store and query billions of entity-relation facts |
| Combining structured knowledge with natural language AI | **RAG + KG** | LLM generates fluent text; KG grounds it in verified facts |
| Domain where knowledge changes rapidly | **KG + RAG** | KG can be updated without retraining; RAG retrieves latest |

### How They Work Together in Practice

```
                    ┌──────────────┐
                    │   Ontology   │  ← Defines the schema
                    │  (OWL/RDF)   │     "Medicine treats Disease"
                    └──────┬───────┘
                           │ governs
                    ┌──────▼───────┐
                    │  Knowledge   │  ← Stores the facts
                    │    Graph     │     "(Aspirin, treats, Headache)"
                    └──────┬───────┘
                           │ feeds into
              ┌────────────▼────────────┐
              │      Expert System      │  ← Applies decision rules
              │   IF symptoms match     │     "IF headache THEN suggest Aspirin"
              │   THEN recommend drug   │
              └────────────┬────────────┘
                           │ enhanced by
                    ┌──────▼───────┐
                    │     RAG      │  ← Retrieves context for LLM
                    │  LLM + KG   │     "Aspirin: take 500mg, avoid if..."
                    └──────────────┘
```

### RAG vs Traditional LLM vs Fine-Tuning

| Aspect | Traditional LLM | Fine-Tuned LLM | RAG |
|---|---|---|---|
| Knowledge source | Training data (frozen) | Training + fine-tuning data | External KB (live) |
| Up-to-date info | No (cutoff date) | Partially (if fine-tuned recently) | Yes (retrieves in real-time) |
| Hallucination risk | High | Medium | Low (grounded in retrieved facts) |
| Cost to update | Retrain ($$$) | Fine-tune ($$) | Update KB ($) |
| Domain adaptation | General | Specialized | Flexible |
| Interpretability | Low (black box) | Low | Higher (can cite sources) |

---

## 🏗️ 设计题答题框架

**Prompt type: "Design a knowledge-based system for [domain]. Explain the KR approach you would use and justify your choices."**

### WHAT
Define the KR components you would use. Be specific:
- "I would use a **Knowledge Graph** to store domain facts as RDF triples..."
- "An **ontology** (OWL) would define the valid entity types and relationship constraints..."
- "An **expert system** layer would encode domain-specific decision rules as production rules..."
- "**RAG** would connect the KG to an LLM for natural-language query answering..."

### WHY
Justify each choice based on system requirements:
- "A KG is chosen because the domain has **millions of entity-relationship facts** that need to be queried flexibly."
- "An ontology ensures **data integrity** — only valid relationships are stored."
- "Production rules provide **explainable decisions** required in regulated domains (healthcare, finance)."
- "RAG is needed because end-users expect **natural language answers**, and pure KG queries (SPARQL) are not user-friendly."

### HOW
Describe the architecture and data flow:
1. Define the ontology (classes, properties, constraints)
2. Populate the KG from structured + unstructured sources (NER + relation extraction)
3. Implement the inference engine (forward chaining over rules; OWL reasoner for ontology)
4. Add RAG layer: retriever indexes KG facts; LLM generates user-facing answers

### TRADE-OFF
Discuss limitations and mitigations:
- "Expert systems are interpretable but **brittle** — mitigated by combining with KG for broader coverage."
- "KGs may be **incomplete** — mitigated by KG embedding models (TransE) for link prediction."
- "RAG reduces hallucination but **adds latency** — mitigated by caching frequent queries."
- "Ontology reasoning can be **computationally expensive** in expressive OWL profiles — mitigated by using OWL Lite or pre-computing inferences."

### EXAMPLE
Provide a concrete walk-through:
- "A patient presents with fever and cough. The expert system checks its rules: R1 matches (fever AND cough → possible flu). The KG is queried for treatments: (Flu, treatedBy, Oseltamivir). The ontology confirms Oseltamivir is-a Antiviral and Antiviral treats ViralInfection. RAG generates: 'Based on symptoms, possible flu is suggested. Oseltamivir (Tamiflu) is recommended per current guidelines.'"

---

## 📝 Exam Practice

### Practice Question 1 (6 marks)

**Explain the DIKW pyramid with an example. For each level, describe how an AI system might process data at that level.**

<details>
<summary>Click to reveal answer framework</summary>

**Definition (2 marks):**
The DIKW pyramid represents four levels of abstraction in processing information:
- **Data**: Raw, unprocessed symbols (e.g., sensor readings: 38.5, 120, 95)
- **Information**: Contextualized data (e.g., "Patient temperature is 38.5C, heart rate 120 bpm, blood oxygen 95%")
- **Knowledge**: Patterns derived from information (e.g., "Temperature > 38C with elevated heart rate suggests infection")
- **Wisdom**: Judgment applied to knowledge (e.g., "Start antibiotics now because the patient is immunocompromised and delay increases risk")

**AI system mapping (4 marks):**
- Data level: Sensors, logs, databases store raw observations
- Information level: ETL pipelines, data preprocessing, feature engineering add context
- Knowledge level: Knowledge graphs, ontologies, and trained models encode patterns
- Wisdom level: Expert systems with confidence reasoning, decision support systems apply judgment

**Common mistakes to avoid:**
- Do not confuse Information and Knowledge — Information is contextualized data; Knowledge is generalized patterns
- Do not forget to give concrete examples at each level
</details>

### Practice Question 2 (8 marks)

**Compare Expert Systems, Ontologies, and Knowledge Graphs as knowledge representation methods. For each, describe (a) how knowledge is represented, (b) how reasoning is performed, (c) one strength and one weakness, and (d) a real-world example.**

<details>
<summary>Click to reveal answer framework</summary>

| Aspect | Expert System | Ontology | Knowledge Graph |
|---|---|---|---|
| **(a) Representation** | IF-THEN production rules in a knowledge base | Formal class hierarchies with relationships and constraints (OWL/RDF) | Entity-relation-entity triples in RDF format |
| **(b) Reasoning** | Forward chaining (data-driven) and backward chaining (goal-driven) over rules | OWL reasoners perform subsumption, classification, constraint validation | Graph traversal (SPARQL/Cypher), path-based inference, KG embeddings |
| **(c) Strength** | Transparent and explainable — every conclusion traces to human-readable rules | Formal schema ensures data integrity; supports automatic classification via OWL reasoners | Scales to billions of facts; flexible triple format can represent any domain |
| **(c) Weakness** | Does not scale — rule maintenance becomes intractable beyond ~10K rules | Reasoning complexity can be NP-hard in expressive OWL profiles | May be incomplete — missing triples require KG completion techniques |
| **(d) Example** | MYCIN (bacterial infection diagnosis, 1970s) | SNOMED CT (standardized medical terminology ontology) | Google Knowledge Graph (web-scale entity-relation search) |

**Scoring rubric (estimated):**
- Representation (2 pts): Clear description of each method's format
- Reasoning (2 pts): Correct reasoning mechanisms for each
- Strength/Weakness (2 pts): One valid strength and weakness per method
- Examples (2 pts): Appropriate real-world examples

**Common mistakes to avoid:**
- Do not say KGs "replaced" Expert Systems — they solve different problems
- Do not confuse Ontology (schema) with Knowledge Graph (facts)
- Do not forget to mention reasoning mechanism (not just storage)
</details>

### Practice Question 3 (5 marks)

**What is RAG (Retrieval-Augmented Generation)? Explain why it was developed and describe its pipeline with an example.**

<details>
<summary>Click to reveal answer framework</summary>

**Why RAG was developed (2 marks):**
LLMs suffer from three key limitations:
1. **Hallucination** — generate plausible but factually incorrect information
2. **Knowledge cutoff** — cannot access information after their training date
3. **No source verification** — cannot cite where their answers come from

RAG addresses all three by retrieving verified external knowledge before generating a response.

**RAG Pipeline (2 marks):**
1. **Query**: User asks a question (e.g., "Who won the 2024 Nobel Prize in Physics?")
2. **Retrieve**: System searches external knowledge base (KG, document store) using sparse (BM25) or dense (DPR) retrieval. Returns top-k relevant passages.
3. **Augment**: Retrieved passages are prepended to the LLM prompt as context.
4. **Generate**: LLM produces a response grounded in the retrieved facts.

**Example (1 mark):**
Without RAG: LLM says "I'm not sure who won the 2024 Nobel Prize in Physics."
With RAG: Retriever finds "The 2024 Nobel Prize in Physics was awarded to John Hopfield and Geoffrey Hinton for foundational discoveries in machine learning." LLM generates an accurate, sourced response.

**Key point**: RAG does **not** retrain or fine-tune the LLM. It only provides external context at inference time. The model weights remain unchanged.
</details>

---

## 🌐 英语表达要点（English Expression）

### Defining KR Concepts

```
"Knowledge Representation refers to the methods used in AI to store,
 organize, and reason over structured knowledge, enabling machines
 to make intelligent decisions."

"The DIKW pyramid describes a hierarchy where raw data is progressively
 refined into information, knowledge, and ultimately wisdom."

"An Expert System encodes domain expert knowledge as a set of IF-THEN
 production rules and uses an inference engine to derive conclusions
 from known facts."
```

### Comparing Approaches

```
"While Expert Systems encode knowledge as explicit IF-THEN rules,
 Knowledge Graphs represent knowledge as entity-relation-entity triples,
 offering greater scalability at the cost of less structured reasoning."

"Unlike a Knowledge Graph, which stores specific factual instances,
 an ontology provides the formal schema — defining what types of
 entities exist and how they may relate."

"The fundamental difference between an ontology and a knowledge graph
 is that an ontology defines what is *valid*, while a KG stores
 what is *true*."
```

### Explaining RAG

```
"RAG addresses the hallucination problem in LLMs by dynamically
 retrieving verified knowledge from external sources before generation,
 ensuring factual grounding without modifying the model's weights."

"The key advantage of RAG over fine-tuning is that the knowledge base
 can be updated independently of the model, enabling real-time access
 to the latest information."
```

### Commonly Confused Terms

| Confused Pair | Distinction |
|---|---|
| **Ontology** vs **Knowledge Graph** | Ontology = schema (what *types* of facts are valid); KG = data (what *specific* facts are true) |
| **Knowledge Base** vs **Knowledge Graph** | KB is a general term (can include rules); KG specifically means graph-structured triples |
| **Forward Chaining** vs **Backward Chaining** | Forward = data → conclusion (what can I infer?); Backward = goal → evidence (is this true?) |
| **RAG** vs **Fine-tuning** | RAG = add context at inference, no weight change; Fine-tuning = modify model weights on new data |
| **Data** vs **Information** | Data = raw symbols; Information = data + context/meaning |
| **Knowledge** vs **Wisdom** | Knowledge = patterns/rules; Wisdom = judgment about when/how to apply knowledge |

---

## ✅ 自测检查清单

- [ ] Can I define Knowledge Representation and explain its purpose in one sentence in English?
- [ ] Can I draw the DIKW pyramid and give an example at each level?
- [ ] Can I name the 5 requirements of a KR system (Expressiveness, Efficiency, Scalability, Interpretability, Modifiability)?
- [ ] Can I draw the 3-component architecture of an Expert System (KB + Inference Engine + User Interface)?
- [ ] Can I write an IF-THEN production rule and explain how it fires?
- [ ] Can I explain the difference between forward chaining and backward chaining?
- [ ] Can I list the 5 components of an Ontology (Concepts, Instances, Relationships, Constraints, Inference)?
- [ ] Can I explain the difference between an Ontology and a Knowledge Graph?
- [ ] Can I write an RDF triple and explain the (Subject, Predicate, Object) format?
- [ ] Can I explain the RAG pipeline (Query → Retrieve → Augment → Generate) and why it reduces hallucination?
- [ ] Can I compare Expert Systems, Ontologies, and KGs in a table (representation, reasoning, strengths, weaknesses)?
- [ ] Do I know which KR method is best suited for which scenario?

---

> **Cross-references:**
> - For deeper coverage of Expert Systems and MYCIN, see [Expert Systems chapter](./E_expert_systems.md)
> - For deeper coverage of Knowledge Graphs, Ontologies, KG Embeddings, and RAG, see [Knowledge Graphs chapter](./F_knowledge_graphs.md)
> - For the broader KR methods landscape (Semantic Networks, Frames, Rule-Based Systems), see [KR Methods chapter](./F_kr_methods.md)
