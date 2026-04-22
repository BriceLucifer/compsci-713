# Knowledge Graphs for AI -- Construction, Inference & TransE (W3L2)

## 🎯 考试重要度

🟠 **高频** | Week 3 Lecture 2 (56 slides) | Sample Test Q3 (2 marks) 直接考查 KG Embeddings 计算

> **Exam alert:** Q3 asks you to explain Knowledge Graph Embeddings and give a common KG inference task. You **must** know the TransE formula and be able to compute L1 distances by hand. Every past test asks about entity/relation embeddings in KG completion. Every test asks about TransE (h+r≈t) and its scoring function. Link prediction example: (Einstein, bornIn, ?) → Germany.

---

## 📖 核心概念（Core Concepts）

| English Term | 中文 | One-line Definition |
|---|---|---|
| Knowledge Graph (KG)（知识图谱） | 知识图谱 | A directed graph where nodes are entities and labeled edges are relations, storing facts as triples $(h, r, t)$ |
| Semantic Network（语义网络） | 语义网络 | Early graph-based KR using nodes and links; KGs are the modern, standardized, large-scale evolution |
| Expert System（专家系统） | 专家系统 | AI system using KB (facts & rules) + inference engine + user interface for domain-specific decision-making |
| Ontology（本体论） | 本体论 | Formal representation defining **concepts, relationships, constraints, and inference rules** in a domain |
| RDF (Resource Description Framework)（资源描述框架） | 资源描述框架 | W3C standard for representing facts as (Subject, Predicate, Object) triples -- flexible, scalable, machine-readable |
| OWL (Web Ontology Language)（网络本体语言） | 网络本体语言 | Extends RDF with **logical reasoning** and **ontology-based classification** -- defines concepts, hierarchies, constraints |
| SPARQL | SPARQL | Query language for RDF triple stores (like SQL for relational databases) |
| Entity Extraction / NER（实体抽取） | 实体抽取 | NLP task identifying real-world entities (people, places, concepts) from unstructured text |
| Relation Extraction（关系抽取） | 关系抽取 | NLP task identifying semantic relationships between extracted entities |
| Knowledge Integration（知识融合） | 知识融合 | Merging entities from different sources that refer to the same real-world object (entity resolution) |
| Property Graph（属性图） | 属性图 | Graph model where nodes and edges carry key-value attributes (Neo4j model) |
| Triple Store / RDF Store（三元组存储） | 三元组存储 | Database storing knowledge as (S, P, O) triples, queried via SPARQL |
| TransE | TransE | KG embedding model: for a true triple $(h, r, t)$, the relation $r$ acts as a translation so $\mathbf{h} + \mathbf{r} \approx \mathbf{t}$ |
| Negative Sampling（负采样） | 负采样 | Creating false triples by corrupting head or tail of a known true triple, used for contrastive training |
| Link Prediction（链接预测） | 链接预测 | Predicting the missing entity in an incomplete triple: $(h, r, ?)$ or $(?, r, t)$ |
| Knowledge Graph Embeddings (KGE)（知识图谱嵌入） | 知识图谱嵌入 | Representing entities and relations as dense vectors in continuous space for inference |
| RAG (Retrieval-Augmented Generation)（检索增强生成） | 检索增强生成 | Architecture that retrieves external knowledge at inference time to ground LLM responses in facts |
| BM25 | BM25 | Sparse (keyword-based) retrieval scoring function used in traditional information retrieval |
| DPR (Dense Passage Retrieval)（稠密段落检索） | 稠密段落检索 | Neural retrieval model encoding queries and passages as dense vectors for semantic similarity search |
| FAISS | FAISS | Facebook AI Similarity Search -- library for efficient approximate nearest neighbor search over dense vectors |

---

## 🧠 费曼草稿（Feynman Draft）

### Part 1: From Semantic Networks to Knowledge Graphs

Imagine you drew a concept map on a napkin -- "Einstein discovered Relativity", "Relativity is related to Physics". That napkin is essentially a **Semantic Network**: a small, informal web of concepts and relationships. Now imagine Google took that idea and built it with billions of facts, standardized formats (RDF triples), and web-scale infrastructure. That is a **Knowledge Graph**.

| Aspect | Semantic Networks | Knowledge Graphs |
|---|---|---|
| Origin | Early AI research (1960s--1980s) | Modern large-scale data systems (2000s) |
| Nature | Conceptual KR model | Industrial-scale knowledge management |
| Representation | Graph (nodes and edges) | Triple-based: (Subject, Predicate, Object) |
| Standardization | No unified standard | Based on standards: **RDF** and **OWL** |
| Scale | Typically small and domain-specific | Designed for **web-scale** knowledge bases |
| Applications | Early AI reasoning, concept representation | Search engines, recommendation systems, AI applications |

**Key insight from slides:** "Knowledge graphs can be viewed as a modern, large-scale implementation and extension of the original semantic network concept."

**Example showing the difference:**
- Semantic Network: Einstein --discovered--> Theory of Relativity; Theory of Relativity --related to--> Physics
- Knowledge Graph: (Albert Einstein, discovered, Theory of Relativity); (Theory of Relativity, relatedTo, Physics) -- standardized triple format

### Part 2: Expert Systems -- The Rule-Following Doctor

Imagine a very obedient robot doctor. Before seeing any patient, human experts sat down and wrote every diagnosis rule on index cards:

```
IF patient has fever AND bacterial infection
THEN recommend antibiotic treatment
```

The robot has three parts:
1. **Knowledge Base** -- the box of index cards (rules + facts)
2. **Inference Engine** -- the process of matching current symptoms to rules and firing them
3. **User Interface** -- how the doctor talks to patients

**MYCIN (1970s)** was a real expert system for diagnosing bacterial infections. It outperformed some human doctors! But it could only handle what its rules covered -- it could not learn, adapt, or handle situations no one had written rules for.

### Part 3: Ontologies -- The Grammar Book for Knowledge

Think of an ontology as a **grammar book** for knowledge. It does not tell you what specific facts are true -- it tells you what *kinds* of facts are **allowed**.

A medical ontology might say:
- "Disease" is a class. "Medicine" is a class.
- A Medicine **treats** a Disease (this kind of relationship is valid).
- A treatment must be associated with **at least one** disease (constraint).

Now compare:
- **Ontology** says: "Medicine treats Disease" (what *kinds* of statements are valid -- schema + rules)
- **Knowledge Graph** says: "(Aspirin, treats, Headache)" (what *specific* facts are true -- data)

An ontology is like the grammar book; a KG is like the encyclopedia written following that grammar.

**Five components of an Ontology:**
1. **Concepts (Classes)** -- categories: Disease, Medicine, Symptom
2. **Instances (Individuals)** -- specific members: Flu, Aspirin, Fever
3. **Relationships (Properties)** -- connections: Medicine "treats" Disease
4. **Constraints & Rules** -- restrictions: "A treatment must be associated with at least one disease"
5. **Inference Mechanisms** -- derive new facts: If Aspirin is-a Pain Reliever, and Pain Relievers treat Headache, then Aspirin can treat Headache

### Part 4: RDF and OWL -- The Technical Standards

**RDF (Resource Description Framework)** is a W3C standard for representing facts as triples:

```
(Subject, Predicate, Object)  =  (Head, Relation, Tail)  =  (h, r, t)

Examples:
<Einstein> <born_in> <Germany>
<Einstein> <discovered> <Theory of Relativity>
<Theory of Relativity> <related_to> <Physics>
```

RDF is **flexible** (any fact can be a triple), **scalable** (designed for the web), and **machine-readable**.

**OWL (Web Ontology Language)** extends RDF by adding **logical reasoning**:

```xml
<owl:Class rdf:ID="Scientist">
  <rdfs:subClassOf rdf:resource="#Person"/>
</owl:Class>
```

This says "Scientist is a subclass of Person." Now if we know "Einstein is-a Scientist", OWL can automatically **infer** "Einstein is-a Person."

**Key difference:**
- **RDF** = facts (the basic triple-based data model for representing knowledge)
- **OWL** = logic + ontology (extends RDF with richer ontology constructs and logical reasoning)

### Part 5: Building a Knowledge Graph

How do you fill a KG with facts? Four steps:

```
Step 1: Entity Extraction (NER)
  "Albert Einstein was born in Germany" → {Albert Einstein, Germany}

Step 2: Relation Extraction
  → (Albert Einstein, born_in, Germany)

Step 3: Knowledge Integration (Entity Resolution)
  "Albert Einstein" (source A) = "A. Einstein" (source B) → merge

Step 4: Storage & Query
  Store in graph database (Neo4j, RDF Store, Dgraph)
  Query using SPARQL or Cypher
```

**Data sources** for KG construction:
1. **Structured** (databases, existing KBs) -- already organized, e.g., DBpedia, Wikidata
2. **Unstructured** (text, webpages) -- use NLP (NER + RE) to extract knowledge
3. **Semi-Structured** (JSON, XML, APIs) -- requires transformation, e.g., Wikipedia infoboxes

**SPARQL query example (from slides):**
```sparql
SELECT ?birthplace WHERE {
  <http://dbpedia.org/resource/Albert_Einstein>
  <http://dbpedia.org/ontology/birthPlace> ?birthplace.
}
```

### Part 6: Three Families of KG Inference

**1. Rule-Based (Symbolic Inference):**
Apply explicit logical rules:
```
IF (A, part_of, B) AND (B, part_of, C) THEN (A, part_of, C)

Facts: (Auckland, part_of, New Zealand), (New Zealand, part_of, Oceania)
Infer: (Auckland, part_of, Oceania) ✅
```
Often implemented using OWL, SPARQL, and FOL.

**2. Graph-Based (Path-Based Inference):**
Traverse graph structure using graph query languages (SPARQL, Cypher) and graph algorithms (PageRank, Shortest Path):
```
Query: "Was Einstein indirectly mentored by Curie?"
Shortest path in Neo4j → Curie ──mentored──► X ──mentored──► Einstein
Answer: Yes, through intermediate node X
```

**3. Embedding-Based (KGE -- this is where TransE lives):**
Represent entities and relations as **dense vectors** in continuous space. Predict missing facts via vector arithmetic. This is the approach tested in exams.

### Part 7: TransE -- The Key Idea

Think of it like giving directions on a map. If "Paris" is at position (0.5, 0.2, 0.7) and the direction "located_in" is the movement (0.3, 0.2, 0.3), then after following that direction you should arrive at "France":

$$\mathbf{h} + \mathbf{r} = (0.5 + 0.3,\ 0.2 + 0.2,\ 0.7 + 0.3) = (0.8,\ 0.4,\ 1.0)$$

Now compare this predicted destination to all candidate entities:

| Candidate | Embedding | L1 Distance from (0.8, 0.4, 1.0) |
|---|---|---|
| **France** | (0.8, 0.4, 1.0) | $|0.8-0.8| + |0.4-0.4| + |1.0-1.0| = \mathbf{0.0}$ |
| Europe | (0.9, 0.3, 1.2) | $0.1 + 0.1 + 0.2 = \mathbf{0.4}$ |
| Germany | (1.2, 0.6, 1.5) | $0.4 + 0.2 + 0.5 = \mathbf{1.1}$ |

**France wins with distance 0.0.** The model correctly predicts (Paris, located_in, **France**).

The beauty: you never told the model any rules. It *learned* that "located_in" means "move by (0.3, 0.2, 0.3)" just from seeing thousands of (city, located_in, country) examples.

### Part 8: RAG -- The Librarian + The Storyteller

An LLM (like GPT) is a great storyteller but sometimes makes things up (**hallucination**). RAG adds a librarian step:

```
User asks: "Who won the Turing Award in 2023?"

WITHOUT RAG (hallucination risk):
  LLM: "The Turing Award is given annually for contributions to 
        computer science, but I am unsure who won in 2023."

WITH RAG:
  Step 1: RETRIEVE from knowledge base
    → "In 2023, the Turing Award was awarded to Geoffrey Hinton 
       for his contributions to deep learning"
  Step 2: AUGMENT -- feed retrieved context to LLM
  Step 3: GENERATE grounded answer
    → "The 2023 Turing Award was awarded to Geoffrey Hinton 
       for his contributions to deep learning."
```

**Why RAG over fine-tuning?** RAG updates knowledge by updating the **retrieval index** (cheap), not by retraining the model (expensive). The LLM's weights are **never modified**.

**RAG Pipeline (from slides):**
1. **User Query** -- "Who won the Turing Award in 2023?"
2. **Knowledge Retrieval** -- search structured (DBs, KGs) and unstructured (documents) sources using BM25 (sparse) or DPR/FAISS (dense)
3. **Contextual Integration** -- retrieved documents passed to LLM as additional context
4. **Response Generation & Re-Ranking** -- LLM generates factually grounded answer; some models apply re-ranking

**Mathematical representation:** $\text{Generated Response} = \text{LLM}(\text{Query} + \text{Retrieved Knowledge})$

---

⚠️ **Common Misconception**: Students often think TransE *proves* a fact is true. It does NOT. TransE gives a *score* (distance). A low score means the triple is *likely* true based on learned patterns. It is probabilistic, not logical.

⚠️ **Common Misconception**: RAG does **not** retrain or fine-tune the LLM. It only provides additional context at inference time. The LLM parameters remain **frozen**.

⚠️ **Common Misconception**: Students confuse Ontology and Knowledge Graph. An ontology defines what is *valid* (schema + rules); a KG stores what is *true* (specific facts). AI systems integrate: **Ontology (rules/schema) → Knowledge Graph (facts)**.

💡 **Core Intuition**: TransE treats relations as translations in vector space -- add the relation vector to the head, and you should land near the tail.

---

## 📐 正式定义（Formal Definition）

### Semantic Networks vs Knowledge Graphs (Formal Comparison)

| Aspect | Semantic Networks | Knowledge Graphs |
|---|---|---|
| **Origin** | Early AI research (1960s--1980s) | Modern large-scale data systems (2000s) |
| **Nature** | Conceptual knowledge representation model | Industrial-scale knowledge management system |
| **Representation** | Graph structure (nodes and edges) | Triple-based: (Subject, Predicate, Object) |
| **Standardization** | No unified standard | Based on standards such as **RDF** and **OWL** |
| **Scale** | Typically small and domain-specific | Designed for web-scale knowledge bases |
| **Applications** | Early AI reasoning, concept representation | Search engines, recommendation systems, AI applications |

### Expert System -- Three Components

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
              │   Knowledge Base    │  ← IF fever AND bacterial infection
              │   (Rules + Facts)   │     THEN recommend antibiotic
              └─────────────────────┘
```

**MYCIN example (from slides):** AI for medical diagnosis (1970s). "IF patient has fever AND bacterial infection, THEN recommend an antibiotic treatment." MYCIN outperformed some doctors in diagnosing bacterial infections.

### Ontology -- Five Components

| Component | Role | Example |
|---|---|---|
| **1. Concepts (Classes)** | Categories of entities | Disease, Medicine, Treatment, Patient |
| **2. Instances (Individuals)** | Specific data points (members of classes) | Flu, COVID-19, Aspirin, John Doe |
| **3. Relationships (Properties)** | How entities/instances connect | Medicine "treats" Disease; Aspirin "treats" Headache |
| **4. Constraints & Rules** | Logical restrictions on relationships | "A treatment must be associated with at least one disease" |
| **5. Inference Mechanisms** | Derive new facts from ontology structure | If Aspirin is-a Pain Reliever AND Pain Relievers treat Headache → Aspirin treats Headache |

**Ontology vs Knowledge Graph (from slides):**
- **KG**: (subject, predicate, object) -- only represents **facts**; no clear statement on what is valid
  - Example: (Aspirin, treats, Headache); (Flu, hasSymptom, Fever)
- **Ontology**: concepts, relations, **rules** -- defines that **only** Medicine can treat Disease
  - Example: Medicine "treats" Disease (schema-level constraint)
- AI systems integrate: **Ontology (rules/schema) → Knowledge Graph (facts)**

### Knowledge Graph -- Formal Structure

A Knowledge Graph is a tuple $\mathcal{G} = (E, R, T)$ where:
- $E$ = set of entities (nodes)
- $R$ = set of relation types (edge labels)
- $T \subseteq E \times R \times E$ = set of triples (directed, labeled edges representing facts)

### RDF and OWL

**RDF** represents knowledge using triples:
- $(S, P, O) = (\text{Subject, Predicate, Object}) = (h, r, t)$
- Flexible, scalable, machine-readable

**OWL** extends RDF:
- Allows **logical reasoning** and **ontology-based classification**
- Defines **concepts**, **relationships**, and **hierarchy constraints**
- Example: OWL defines "Scientist" as subclass of "Person" → Einstein is-a Scientist → infer Einstein is-a Person

### KG Inference Tasks (from slides)

| Task | Goal | Example | Use Cases |
|---|---|---|---|
| **KG Completion** | Predict missing links | (Paris, located_in, ?) → France | AI assistants, Medical AI |
| **Relation Prediction** | Predict relation type | (Einstein, ?, Physics) → "studied" | Semantic search, Fraud detection |
| **Fact Verification** | Validate facts | (Moon, made_of, Cheese) → FALSE | Fake news detection, DB cleaning |
| **Fact Generation** | Create new facts | (Drug X, treats, ?) → Disease Y | Biomedical AI, Scientific discovery |
| **KG Reasoning** | Infer new knowledge | (Paris, in, France) + (France, in, EU) → (Paris, in, EU) | Legal AI, Scientific research |
| **KG Alignment** | Merge multiple KGs | "Barack Obama" ≈ "B. Obama" | Enterprise AI, Multilingual AI |

### TransE Scoring Function

For a triple $(h, r, t)$, the energy (score) function is:

$$f(h, r, t) = \|\mathbf{h} + \mathbf{r} - \mathbf{t}\|_{p}$$

where $p = 1$ for L1 norm (Manhattan distance) or $p = 2$ for L2 norm (Euclidean distance).

- **Low** $f(h,r,t)$ → triple is likely **true**
- **High** $f(h,r,t)$ → triple is likely **false**

**L1 norm (Manhattan distance):**
$$\|\mathbf{h} + \mathbf{r} - \mathbf{t}\|_1 = \sum_{i=1}^{d} |h_i + r_i - t_i|$$

**L2 norm (Euclidean distance):**
$$\|\mathbf{h} + \mathbf{r} - \mathbf{t}\|_2 = \sqrt{\sum_{i=1}^{d} (h_i + r_i - t_i)^2}$$

### Margin-Based Ranking Loss

$$\mathcal{L} = \sum_{(h,r,t) \in S}\ \sum_{(h',r,t') \in S'} \max\!\Big(0,\ \gamma + f(h,r,t) - f(h',r,t')\Big)$$

where:
- $S$ = set of **correct** triples (positive examples)
- $S'$ = set of **corrupted** triples (negative examples)
- $\gamma > 0$ = margin hyperparameter (separation gap between positive and negative scores)
- Goal: push $f(\text{positive})$ **down** and $f(\text{negative})$ **up**, with at least $\gamma$ gap

### Negative Sampling (Corruption)

Given a true triple $(h, r, t)$, generate negatives by:
- **Corrupt head**: replace $h$ with random $h' \in E$, yielding $(h', r, t)$
- **Corrupt tail**: replace $t$ with random $t' \in E$, yielding $(h, r, t')$

Constraint: the corrupted triple must **not** exist in $T$ (otherwise it is a valid fact, not a true negative).

---

## 🔄 机制与推导（How It Works）

### KG Construction Pipeline -- Step by Step

```
Raw Text / Structured Data / Semi-Structured Data
        ↓
[Step 1] Entity Extraction (NER)
        "Albert Einstein was born in Germany and developed
         the Theory of Relativity"
        → {Albert Einstein, Germany, Theory of Relativity}
        ↓
[Step 2] Relation Extraction
        → (Albert Einstein, born_in, Germany)
        → (Albert Einstein, discovered, Theory of Relativity)
        ↓
[Step 3] Knowledge Integration (Entity Resolution)
        "Albert Einstein" (Wikipedia) = "A. Einstein" (paper) → merge
        ↓
[Step 4] Store in Graph Database & Query
        ├── Neo4j (Property Graph, Cypher queries)
        ├── RDF Store (Triple Store, SPARQL queries)
        └── Dgraph (Distributed, GraphQL+)
```

### Graph Database Comparison

| Database | Model | Query Language | Best For |
|---|---|---|---|
| **Neo4j** | Property Graph (nodes/edges have key-value attributes) | Cypher | Social networks, fraud detection, path queries |
| **RDF Store** (e.g., Virtuoso, Blazegraph) | Triple Store (Subject, Predicate, Object) | SPARQL | Open KGs (DBpedia, Wikidata), semantic web |
| **Dgraph** | Distributed Graph | GraphQL+ | Large-scale, real-time AI applications |

**Key distinction:** Property graphs allow key-value attributes on both nodes and edges. RDF triples are purely (S, P, O) -- to attach metadata you need reification.

### Three Types of KG Inference -- Detailed

#### 1. Rule-Based Inference（基于规则的推理）

Apply explicit logical rules (IF-THEN, OWL reasoning, SPARQL, FOL):

```
Rule: IF (X, part_of, Y) AND (Y, part_of, Z) THEN (X, part_of, Z)

Facts: (Auckland, part_of, New Zealand), (New Zealand, part_of, Oceania)
Infer: (Auckland, part_of, Oceania) ✅
```

Strengths: deterministic, interpretable, guaranteed sound.
Weakness: requires manually written rules; cannot handle missing data.

#### 2. Graph-Based Inference（基于路径的推理）

Traverse graph paths using SPARQL, Cypher, graph algorithms (PageRank, Shortest Path):

```
Query: "Did Newton influence Einstein?"
Path found: Newton →[discovered]→ Law of Gravity →[influenced]→ 
            Theory of Relativity ←[developed]← Einstein
Answer: Yes — Newton's work indirectly influenced Einstein.
```

Strengths: uses graph structure directly; no training needed.
Weakness: only finds what is reachable; cannot generalize beyond existing edges.

#### 3. Embedding-Based Inference（基于嵌入的推理）

Represent entities and relations as dense vectors; predict missing facts via vector arithmetic.

**Why use embeddings?**
- Captures **hidden patterns**: generalizes beyond explicit triples
- **Scalable & efficient**: works well for large-scale KGs (Wikidata, Freebase)
- Enables **deep learning integration**: works with LLMs and generative AI

**This is where TransE operates.** See the complete treatment below.

### TransE Training -- Complete Process

**Step 1: Initialize embeddings**

Assign each entity $e \in E$ a random $d$-dimensional vector $\mathbf{e} \in \mathbb{R}^d$.
Assign each relation $r \in R$ a random $d$-dimensional vector $\mathbf{r} \in \mathbb{R}^d$.
(Optional) Normalize all entity vectors to unit length: $\|\mathbf{e}\| = 1$.

**Step 2: Sample a mini-batch of true triples**

From the training set $T$, sample positive triples, e.g.:
- (Paris, located_in, France)
- (Berlin, located_in, Germany)
- (France, part_of, Europe)

**Step 3: Generate negative triples (corruption)**

For each positive triple $(h, r, t)$, create a negative by randomly replacing head or tail:
- (Paris, located_in, France) → corrupt tail → (Paris, located_in, **Germany**) [negative]
- (Berlin, located_in, Germany) → corrupt head → (**Tokyo**, located_in, Germany) [negative]

**Step 4: Compute scores**

For positive triple: $f^+ = \|\mathbf{h} + \mathbf{r} - \mathbf{t}\|$
For negative triple: $f^- = \|\mathbf{h'} + \mathbf{r} - \mathbf{t}\|$ (or $\|\mathbf{h} + \mathbf{r} - \mathbf{t'}\|$)

We want $f^+$ to be **small** and $f^-$ to be **large**.

**Step 5: Compute margin loss and update**

$$\text{loss} = \max(0,\ \gamma + f^+ - f^-)$$

If $f^- - f^+ > \gamma$, the loss is zero (good separation).
Otherwise, adjust embeddings via gradient descent to push $f^+$ down and $f^-$ up.

**Step 6: (Optional) Normalize entity embeddings**

Re-normalize entity vectors after each gradient step to prevent embedding magnitudes from exploding.

**Step 7: Repeat** until convergence.

### TransE Inference -- Worked Example (Lecture Slides 45--46)

> **This exact computation style appears in Sample Test Q3. Practice until automatic.**

**Setup:**

Known facts:
- (Paris, located_in, France)
- (France, part_of, Europe)

Pre-trained embeddings ($d = 3$):

| Entity | Embedding Vector |
|---|---|
| Paris | $(0.5, 0.2, 0.7)$ |
| France | $(0.8, 0.4, 1.0)$ |
| Europe | $(0.9, 0.3, 1.2)$ |
| Germany | $(1.2, 0.6, 1.5)$ |

| Relation | Embedding Vector |
|---|---|
| located_in | $(0.3, 0.2, 0.3)$ |

**Query:** (Paris, located_in, ?) -- Which entity is Paris located in?

**Step 1:** Compute $\mathbf{h} + \mathbf{r}$:

$$\mathbf{h} + \mathbf{r} = (0.5, 0.2, 0.7) + (0.3, 0.2, 0.3) = (0.8, 0.4, 1.0)$$

**Step 2:** Compute L1 distance to each candidate entity:

$$d(\text{France}) = |0.8 - 0.8| + |0.4 - 0.4| + |1.0 - 1.0| = 0 + 0 + 0 = \mathbf{0.0}$$

$$d(\text{Europe}) = |0.8 - 0.9| + |0.4 - 0.3| + |1.0 - 1.2| = 0.1 + 0.1 + 0.2 = \mathbf{0.4}$$

$$d(\text{Germany}) = |0.8 - 1.2| + |0.4 - 0.6| + |1.0 - 1.5| = 0.4 + 0.2 + 0.5 = \mathbf{1.1}$$

**Step 3:** Rank by distance (ascending):

| Rank | Entity | L1 Distance |
|---|---|---|
| 1 | **France** | **0.0** |
| 2 | Europe | 0.4 |
| 3 | Germany | 1.1 |

**Answer: France** (smallest L1 distance = 0.0). The model predicts (Paris, located_in, **France**).

### Ontology Inference -- Worked Example (Exercise 2 from slides)

**Scenario:** A company ontology for employees, projects, and roles.

**Ontology structure:**
- **Classes:** Employee (Alice, Bob, Charlie), Project (Project X, Project Y), Role (Manager, Developer)
- **Relationships:** Employee "works on" Project; Employee "has role" Role; Role "is responsible for" Project
- **Instances:**
  - Alice → has role → Manager; Bob → has role → Developer; Charlie → has role → Developer
  - Manager → is responsible for → Project X; Developer → is responsible for → Project Y
  - Alice → works on → Project X; Bob → works on → Project Y; Charlie → works on → Project X
- **Constraints:**
  1. Each Project has at least one Employee working on it
  2. Each Role is responsible for at least one Project
  3. If an Employee has a Role and that Role is responsible for a Project, then the Employee can be inferred to be working on that Project
  4. An employee works on exactly one Project

**Question:** Which of the following inferences is logically valid?
- A) Alice can be inferred to be working on Project Y
- B) Charlie can be inferred to be responsible for Project X
- C) Bob can be inferred to be working on Project Y because his Role (Developer) is responsible for that Project
- D) Alice and Bob must switch projects

**Answer: C**

**Reasoning:**
- **A incorrect:** No relationship between Alice and Project Y in the ontology
- **B incorrect:** Charlie is a Developer, but Project X is the responsibility of a **Manager**. The ontology states that **Roles** (not individuals) are responsible. Charlie has the role Developer, and Project Y is the responsibility of the Developer role. But this does NOT automatically mean Charlie is responsible for Project X.
- **C correct:** Bob is a Developer. The ontology states Developer is responsible for Project Y. Constraint 3 says: if Employee has Role AND Role is responsible for Project → Employee works on that Project. Therefore Bob works on Project Y. ✅
- **D incorrect:** No rule states a Manager must be assigned to all projects

**Important note from slides:** In ontology reasoning: (1) Explicit facts take priority, (2) Inferences cannot contradict or replace given facts.

### RDF + OWL Inference -- Worked Example (Exercise 3 from slides)

**Scenario:** A university KG stored using RDF triples and OWL reasoning rules.

**RDF triples:**
```
<Prof_John> <teaches> <AI_Course>
<AI_Course> <belongs_to> <CS_Department>
<CS_Department> <part_of> <Engineering_Faculty>
<Prof_John> <works_in> <CS_Department>
```

**OWL ontology rules:**
1. All courses belong to exactly one department
2. If a professor teaches a course, they are part of that course's department
3. All departments are part of a faculty
4. If a professor works in a department, they are a member of that faculty

**Question:** Which faculty does Prof. John belong to?

**Answer: B -- Prof. John belongs to the Engineering Faculty based on OWL reasoning rules.**

**Step-by-step reasoning:**
1. RDF: Prof. John teaches AI_Course → AI_Course belongs_to CS_Department → Prof. John is in CS_Department (OWL Rule 2)
2. RDF: Prof. John works_in CS_Department (also given directly)
3. OWL Rule 4: Professor works in department → also faculty member; CS_Department is part_of Engineering_Faculty (OWL Rule 3)
4. **Conclusion:** Prof. John is a faculty member of the **Engineering Faculty**

---

## TransE Limitations & Extensions

### Why TransE Struggles

TransE's core equation $\mathbf{h} + \mathbf{r} = \mathbf{t}$ means that for a given relation $r$ and tail $t$, there is exactly **one** ideal head vector: $\mathbf{h} = \mathbf{t} - \mathbf{r}$.

This causes problems with **1-to-N, N-to-1, and N-to-N relations**:

**Example (N-to-1):** (Paris, located_in, France), (Lyon, located_in, France), (Marseille, located_in, France).

TransE requires: $\mathbf{Paris} + \mathbf{r} \approx \mathbf{France}$, $\mathbf{Lyon} + \mathbf{r} \approx \mathbf{France}$, $\mathbf{Marseille} + \mathbf{r} \approx \mathbf{France}$.

This forces $\mathbf{Paris} \approx \mathbf{Lyon} \approx \mathbf{Marseille}$ -- all three cities **collapse to the same point**, losing their distinct identities!

### Extensions Beyond TransE (from slides)

**TransH** -- deals with many-to-one issue:
- Each relation $r$ has a **normal vector** $\mathbf{w}_r$ defining a hyperplane
- Project entities onto the hyperplane: $\mathbf{h}_\perp = \mathbf{h} - \mathbf{w}_r^\top \mathbf{h} \cdot \mathbf{w}_r$
- Score: $f(h,r,t) = \|\mathbf{h}_\perp + \mathbf{r} - \mathbf{t}_\perp\|$
- Different $h$ can get the same $h_\perp$, allowing distinct entities to have different projected representations
- Example: "Paris located_in France" and "Louvre located_in France" are **projected onto different planes**, preventing entity overlap

**TransR** -- projects into relation-specific space:
- Each relation $r$ has a projection matrix $\mathbf{M}_r \in \mathbb{R}^{k \times d}$
- Project entities: $\mathbf{h}_r = \mathbf{M}_r \mathbf{h}$, $\mathbf{t}_r = \mathbf{M}_r \mathbf{t}$
- Score: $f(h,r,t) = \|\mathbf{h}_r + \mathbf{r} - \mathbf{t}_r\|$
- More expressive but requires more parameters

| Aspect | TransE | TransH | TransR |
|---|---|---|---|
| **Relation modeling** | Single translation vector | Translation on hyperplane | Translation in relation-specific space |
| **Parameters per relation** | $d$ (one vector) | $2d$ (vector + normal) | $d + k \times d$ (vector + matrix) |
| **1-to-1 relations** | Excellent | Excellent | Excellent |
| **N-to-1 / 1-to-N** | Poor (entity collapse) | Good (different projections) | Good (relation-specific projections) |
| **N-to-N relations** | Poor | Moderate | Good |
| **Training speed** | Fast (fewest parameters) | Moderate | Slow (matrix per relation) |

---

## ⚖️ 权衡分析（Trade-offs & Comparisons）

### KG Inference Methods Compared

| Feature | Rule-Based | Path-Based | Embedding-Based (TransE etc.) |
|---|---|---|---|
| **Approach** | Apply logical rules (IF-THEN, OWL, SPARQL) | Traverse graph paths | Vector arithmetic |
| **Can predict missing facts?** | No -- only derives from existing facts | No -- only follows existing edges | **Yes** -- core strength |
| **Interpretability** | High (readable rules) | Medium (explainable paths) | Low (opaque vectors) |
| **Scalability** | Poor (rule explosion) | Medium (path search is expensive) | Good (matrix operations, GPU-friendly) |
| **Requires training?** | No | No | Yes (learn embeddings) |
| **Handles noise?** | Poorly (brittle) | Poorly | Well (statistical patterns) |

### Expert Systems vs Ontologies vs Knowledge Graphs

| Feature | Expert Systems | Ontologies | Knowledge Graphs |
|---|---|---|---|
| **Core idea** | IF-THEN rules encoding expert decisions | Formal schema defining valid concepts & relations | Graph of entity-relation-entity fact triples |
| **What it stores** | Rules + working facts | Class hierarchies + constraints + inference rules | Millions/billions of specific facts |
| **Reasoning style** | Rule firing (forward/backward chaining) | OWL reasoners: classification, subsumption, constraint checking | Graph traversal + SPARQL + embeddings |
| **Expressiveness** | Domain-specific, explicit | Highly expressive (OWL supports FOL fragments) | Flexible (any fact can be a triple) |
| **Scalability** | Poor (rule explosion at ~10K rules) | Moderate (reasoning is NP-hard in expressive OWL) | Excellent (web-scale, billions of triples) |
| **Handles uncertainty** | Limited (MYCIN uses confidence factors) | No (inherently crisp logic) | KG embeddings handle soft/probabilistic reasoning |
| **Example system** | MYCIN, R1/XCON | Gene Ontology, SNOMED CT | Google KG, Wikidata, DBpedia |

### RAG vs Fine-Tuning vs Vanilla LLM

| Aspect | Vanilla LLM | Fine-Tuned LLM | RAG |
|---|---|---|---|
| **Knowledge source** | Training data only | Training + fine-tuning data | Training data + retrieved documents at inference |
| **Up-to-date knowledge?** | No (static cutoff) | Partially | **Yes** (real-time retrieval) |
| **Hallucination risk** | High | Medium | **Low** (grounded in retrieved facts) |
| **Cost to update knowledge** | Full retraining ($$$) | Fine-tuning ($$) | Update retrieval index ($) |
| **Latency** | Low | Low | Higher (retrieval step added) |
| **Explainability** | Low (black box) | Low | Higher (can cite sources) |

### Evolution of KR in AI (from slides)

```
Expert Systems (1970s--1980s)
  ↓ Early symbolic AI, rule-based knowledge bases
  ↓ Example: MYCIN for medical diagnosis
  
Ontologies (1990s--2000s)
  ↓ Formal representation of domain knowledge
  ↓ Defines concepts, relationships, constraints
  ↓ Enables logical reasoning and classification
  
Knowledge Graphs (2000s--present)
  ↓ Large-scale graph-based representation
  ↓ Built using RDF/OWL
  ↓ Supports reasoning, inference, retrieval
  
RAG (2020s--present)
  ↓ Combines KG retrieval with LLMs
  ↓ Reduces hallucination, improves accuracy
```

---

## 🏗️ 设计题答题框架

### Prompt: "Design a knowledge-based system that uses KG embeddings to recommend research papers."

**WHAT:** "I would design a system that constructs a Knowledge Graph of papers, authors, topics, and citations, then uses TransE-family embeddings for link prediction to discover relevant but undiscovered connections, with a RAG pipeline to generate natural-language explanations."

**WHY:** "A KG captures structured relationships (author-wrote-paper, paper-cites-paper, paper-covers-topic) that collaborative filtering alone misses. Embeddings enable prediction of missing links (e.g., papers a researcher *should* read but hasn't cited)."

**HOW:**
1. **KG Construction**: Extract entities (papers, authors, topics) from metadata + NLP on abstracts. Relations: wrote, cites, covers_topic, affiliated_with.
2. **Storage**: Use Neo4j for rich property attributes (publication year, citation count on edges).
3. **Embedding Training**: Train TransR (not TransE -- because "covers_topic" is N-to-N: many papers cover the same topic). Optimize margin-based ranking loss.
4. **Inference**: For researcher $R$, compute $\mathbf{R} + \mathbf{should\_read}$ and rank all papers by L1 distance. Top-k = recommendations.
5. **RAG layer**: User asks "Why is this paper relevant?" → retrieve related KG triples → LLM generates natural-language explanation grounded in facts.

**TRADE-OFF:**
- TransE is simpler and faster but would collapse papers covering the same topic → choose TransR for expressiveness at the cost of more parameters.
- Neo4j offers rich property storage but single-machine limits → if scale demands, migrate to Dgraph.
- RAG adds latency but eliminates "black box" recommendations.

**EXAMPLE:** "Researcher studies 'attention mechanisms'. KG link prediction finds (Researcher, should_read, 'FlashAttention paper') with low distance score. RAG retrieves: (FlashAttention, improves, Transformer efficiency), (Researcher, studies, Attention) → LLM explains: 'This paper is relevant because it improves the efficiency of the attention mechanisms you study.'"

---

## 📝 历年真题 + 练习题

### Sample Test Q3 (2 marks) -- Original

> **Explain Knowledge Graph Embeddings and give a common KG inference task.**

**Model answer (2-mark level):**

Knowledge Graph Embeddings represent entities and relations as dense vectors in a continuous space. Models like TransE learn these vectors such that for a true triple $(h, r, t)$, the relationship $\mathbf{h} + \mathbf{r} \approx \mathbf{t}$ holds. This enables the system to predict missing facts via vector arithmetic rather than explicit graph traversal.

A common inference task is **Link Prediction**: given an incomplete triple $(h, r, ?)$, compute $\mathbf{h} + \mathbf{r}$ and find the entity $t^*$ whose embedding is nearest (by L1 or L2 distance). For example, (Einstein, born_in, ?) → compute $\mathbf{h} + \mathbf{r}$ → nearest entity = Germany.

---

### Exercise 1 -- Expert Systems: Fraud Detection (from W3L2 slides)

> **Scenario:** A bank uses an Expert System for fraud detection with these IF-THEN rules:
>
> | Rule ID | IF Condition | THEN Conclusion |
> |---|---|---|
> | R1 | Transaction amount > $10,000 AND foreign country AND no travel history | Flag as Potential Fraud |
> | R2 | Multiple transactions occur within 5 min in different locations | Flag as High-Risk Fraud |
> | R3 | User confirms transaction via 2FA | Approve Transaction |
> | R4 | Transaction is flagged as fraud (R1 or R2) AND user does NOT confirm via 2FA | Temporarily Block Card |
> | R5 | User has history of similar transactions in same location | Approve Transaction |
>
> **Case Study:** A user attempts a **$12,500** transaction in **Japan** at 3 PM.
> - The user has **no** travel history to Japan
> - Five minutes earlier, a $100 transaction occurred in **New York, USA**
> - The user does **NOT** confirm via 2FA
> - The user has no prior transactions in Japan
>
> **Question:** How should the Expert System respond?
>
> A) Approve the transaction because the user has made similar purchases before.
> B) Temporarily block the user's card due to suspicious activity.
> C) Approve the transaction because it happened at a normal time.
> D) Flag the transaction but allow it since the amount is not too high.

<details>
<summary>Click to reveal answer</summary>

**Answer: B** -- Temporarily block the user's card due to suspicious activity.

**Reasoning:**
1. **R1 matches:** $12,500 > $10,000 ✅, foreign country (Japan) ✅, no travel history ✅ → **Flag as Potential Fraud**
2. **R2 matches:** Two transactions (Japan & USA) within 5 minutes in different locations ✅ → **Flag as High-Risk Fraud**
3. User does NOT confirm via 2FA → **R4 condition met** (flagged by R1 or R2 AND no 2FA) → **Temporarily Block Card**

**Final AI Decision:** Temporarily Block Card & Notify User of Suspicious Activity.

</details>

---

### Exercise 2 -- Ontology Reasoning (Employee/Project)

> See the detailed Exercise 2 worked example in the "How It Works" section above.

---

### Exercise 3 -- RDF + OWL Inference (Prof. John)

> See the detailed Exercise 3 worked example in the "How It Works" section above.

---

### Exercise 4 -- Extracting Triples from Text (Marie Curie)

> **Scenario:** An AI system uses NER and RE to construct a Knowledge Graph from unstructured text.
>
> **Text:** "Marie Curie, a physicist and chemist, was born in Poland in 1867. She discovered radium and polonium, and was awarded the Nobel Prize in Physics in 1903 along with Pierre Curie. Later, in 1911, she won another Nobel Prize, this time in Chemistry."
>
> **Question:** What triples can you extract for the Knowledge Graph (as many as you can)?

<details>
<summary>Click to reveal answer</summary>

**Example triples (partial list from slides):**
- (Marie Curie, born_in, Poland)
- (Marie Curie, discovered, Radium)
- (Marie Curie, discovered, Polonium)
- (Marie Curie, profession, Physicist)
- (Marie Curie, profession, Chemist)
- (Pierre Curie, co_winner, Nobel Prize in Physics)
- (Marie Curie, awarded, Nobel Prize in Physics)
- (Marie Curie, awarded, Nobel Prize in Chemistry)
- (Nobel Prize in Physics, year, 1903)
- (Nobel Prize in Chemistry, year, 1911)
- (Marie Curie, born_year, 1867)
- (Marie Curie, co_winner_with, Pierre Curie)

**Key skills tested:** Entity extraction (identifying people, places, awards, elements) and relation extraction (identifying relationships between extracted entities). The more triples you extract, the richer the KG.

</details>

---

### Exercise 5 -- TransE Computation (from W3L2 slides, same as Sample Test style)

> **Scenario:** TransE is trained on facts: (Paris, located_in, France), (France, part_of, Europe), (Berlin, located_in, Germany), (Germany, part_of, Europe).
>
> **Learned embeddings:**
> - Paris → $(0.5, 0.2, 0.7)$, France → $(0.8, 0.4, 1.0)$, Europe → $(0.9, 0.3, 1.2)$, Germany → $(1.2, 0.6, 1.5)$
> - located_in → $(0.3, 0.2, 0.3)$
>
> **Query:** (Paris, located_in, ?) -- which entity is the most likely prediction using **L1 distance**?

<details>
<summary>Click to reveal solution</summary>

**Step 1:** Compute $\mathbf{h} + \mathbf{r}$:

$$\mathbf{Paris} + \mathbf{located\_in} = (0.5 + 0.3,\ 0.2 + 0.2,\ 0.7 + 0.3) = (0.8,\ 0.4,\ 1.0)$$

**Step 2:** Compute L1 distances:

- **France** $(0.8, 0.4, 1.0)$: $|0.8-0.8| + |0.4-0.4| + |1.0-1.0| = \mathbf{0.0}$
- Europe $(0.9, 0.3, 1.2)$: $|0.8-0.9| + |0.4-0.3| + |1.0-1.2| = 0.1 + 0.1 + 0.2 = \mathbf{0.4}$
- Germany $(1.2, 0.6, 1.5)$: $|0.8-1.2| + |0.4-0.6| + |1.0-1.5| = 0.4 + 0.2 + 0.5 = \mathbf{1.1}$

**Step 3:** Rank:

| Rank | Entity | L1 Distance |
|---|---|---|
| 1 | **France** | **0.0** |
| 2 | Europe | 0.4 |
| 3 | Germany | 1.1 |

**Answer: France** (L1 distance = 0.0). Since France has the smallest L1 distance, it is the most likely prediction.

</details>

---

### Practice Problem -- TransE Computation ($d = 4$)

> **Entity embeddings:**
> - Tokyo → $(0.1, 0.5, 0.3, 0.8)$
> - Japan → $(0.4, 0.7, 0.6, 1.1)$
> - China → $(0.6, 0.9, 0.5, 1.3)$
> - Seoul → $(0.2, 0.4, 0.4, 0.9)$
> - South Korea → $(0.5, 0.6, 0.7, 1.2)$
>
> **Relation embedding:**
> - capital_of → $(0.3, 0.2, 0.3, 0.3)$
>
> **Query: (Tokyo, capital_of, ?)**

<details>
<summary>Click to reveal solution</summary>

**Step 1:** Compute $\mathbf{h} + \mathbf{r}$:

$$\mathbf{Tokyo} + \mathbf{capital\_of} = (0.1 + 0.3,\ 0.5 + 0.2,\ 0.3 + 0.3,\ 0.8 + 0.3) = (0.4,\ 0.7,\ 0.6,\ 1.1)$$

**Step 2:** Compute L1 distances:

- **Japan** $(0.4, 0.7, 0.6, 1.1)$: $|0.4-0.4| + |0.7-0.7| + |0.6-0.6| + |1.1-1.1| = \mathbf{0.0}$
- China $(0.6, 0.9, 0.5, 1.3)$: $0.2 + 0.2 + 0.1 + 0.2 = \mathbf{0.7}$
- Seoul $(0.2, 0.4, 0.4, 0.9)$: $0.2 + 0.3 + 0.2 + 0.2 = \mathbf{0.9}$
- South Korea $(0.5, 0.6, 0.7, 1.2)$: $0.1 + 0.1 + 0.1 + 0.1 = \mathbf{0.4}$

**Step 3:** Rank:

| Rank | Entity | L1 Distance |
|---|---|---|
| 1 | **Japan** | **0.0** |
| 2 | South Korea | 0.4 |
| 3 | China | 0.7 |
| 4 | Seoul | 0.9 |

**Answer: Japan** (L1 distance = 0.0)

</details>

---

### Practice Problem -- Negative Sampling

> **Given the true triple (Berlin, located_in, Germany), generate two negative triples by corruption.**

<details>
<summary>Click to reveal solution</summary>

**Corrupt head:** Replace Berlin with a random entity:
- $(\textbf{Tokyo}, \text{located\_in}, \text{Germany})$ -- false, Tokyo is not in Germany

**Corrupt tail:** Replace Germany with a random entity:
- $(\text{Berlin}, \text{located\_in}, \textbf{Japan})$ -- false, Berlin is not in Japan

Important: verify that the corrupted triple does not accidentally appear in the known fact set $T$. If (Tokyo, located_in, Germany) happened to be a true fact, you would need to pick a different corruption.

</details>

---

### Practice Problem -- Conceptual (Short Answer)

> **Why does TransE fail for N-to-1 relations? Give a specific example.**

<details>
<summary>Click to reveal solution</summary>

TransE requires $\mathbf{h} + \mathbf{r} \approx \mathbf{t}$ for every true triple. For an N-to-1 relation like "located_in" where multiple heads map to the same tail:

- (Paris, located_in, France): $\mathbf{Paris} + \mathbf{r} \approx \mathbf{France}$
- (Lyon, located_in, France): $\mathbf{Lyon} + \mathbf{r} \approx \mathbf{France}$
- (Marseille, located_in, France): $\mathbf{Marseille} + \mathbf{r} \approx \mathbf{France}$

Since $\mathbf{r}$ is the same vector for all three, we get $\mathbf{Paris} \approx \mathbf{Lyon} \approx \mathbf{Marseille}$. The model **collapses distinct entities into the same point**, losing their individual identities.

**TransH solves this** by projecting entities onto a relation-specific hyperplane, allowing different entities to occupy different projected positions even for the same relation.

</details>

---

## 🌐 英语表达要点（English Expression）

### Defining KG Embeddings (exam sentence starters)

```
"Knowledge Graph Embeddings map entities and relations to continuous 
 vector representations, enabling algebraic operations for inference 
 over incomplete knowledge graphs."

"TransE models each relation as a translation vector in embedding space, 
 such that for a valid triple (h, r, t), the equation h + r ≈ t holds."
```

### Explaining Link Prediction

```
"To predict the missing tail in (h, r, ?), we compute h + r and rank 
 all candidate entities by their L1 or L2 distance to this predicted 
 point. The entity with the smallest distance is the predicted answer."
```

### Explaining Ontologies vs KGs

```
"An ontology provides the formal schema — defining what types of entities
 exist and how they may relate — while a knowledge graph stores the 
 specific factual instances conforming to that schema."

"The fundamental difference is that an ontology defines what is *valid*,
 while a KG stores what is *true*."
```

### Describing Expert Systems

```
"An Expert System consists of three components: a Knowledge Base storing
 domain rules and facts, an Inference Engine that applies rules to derive
 conclusions, and a User Interface for input/output."
```

### Describing RAG

```
"Retrieval-Augmented Generation addresses LLM hallucination by retrieving 
 relevant knowledge from external sources at inference time and injecting 
 it into the prompt as context, without modifying the model's parameters."

"The key advantage of RAG over fine-tuning is that the knowledge base
 can be updated independently of the model, enabling real-time access
 to the latest information at minimal cost."
```

### Comparing Models

```
"While TransE is computationally efficient and works well for 1-to-1 
 relations, it struggles with N-to-N mappings because multiple entities 
 sharing the same relation and target collapse to identical embeddings."

"TransH addresses this limitation by introducing a relation-specific 
 hyperplane, allowing entities to have distinct projected representations 
 even when they share the same relation."
```

### 易错词汇

| Incorrect / Confused | Correct Usage | Note |
|---|---|---|
| "embedding" vs "encoding" | Embedding = learned vector; Encoding = deterministic transformation | TransE uses **embeddings** (trainable), not encodings |
| "predict" vs "infer" | Predict = estimate unknown; Infer = derive from given info | TransE **predicts** missing links; rule-based systems **infer** |
| "score" direction | Low score = **true** triple in TransE | Counterintuitive -- students often assume high score = true |
| "negative sample" vs "false triple" | Negative sample = artificially corrupted for training | A negative sample might accidentally be true; check against $T$ |
| "ontology" vs "knowledge graph" | Ontology = schema + rules (what is valid); KG = facts (what is true) | They complement each other; AI systems integrate both |
| "retrieval" vs "generation" | Retrieval = find existing info; Generation = create new text | RAG combines **both** -- retrieval feeds into generation |
| "RDF" vs "OWL" | RDF = data model for triples; OWL = extends RDF with logical reasoning | OWL builds ON TOP of RDF, not a replacement |

---

## ✅ 自测检查清单

- [ ] Can I compare Semantic Networks vs Knowledge Graphs in a table (origin, scale, standardization)?
- [ ] Can I draw the 3-component architecture of an Expert System (KB + Inference Engine + UI)?
- [ ] Can I explain the MYCIN example and what an Expert System does?
- [ ] Can I list the 5 components of an Ontology (Concepts, Instances, Relationships, Constraints, Inference)?
- [ ] Can I explain the difference between an Ontology and a Knowledge Graph in one sentence?
- [ ] Can I explain RDF (triples) and how OWL extends it (adds logical reasoning)?
- [ ] Can I solve the Exercise 2 ontology reasoning problem (employee/project)?
- [ ] Can I trace the Exercise 3 RDF+OWL inference (Prof. John → Engineering Faculty)?
- [ ] Can I compare Neo4j vs RDF Store vs Dgraph in a table?
- [ ] Can I explain the 4-step KG construction pipeline (Entity Extraction → Relation Extraction → Knowledge Integration → Storage & Query)?
- [ ] Can I extract triples from a text passage (Exercise 4, Marie Curie)?
- [ ] Can I name and explain the 3 types of KG inference (rule-based, path-based, embedding-based)?
- [ ] Can I list 6 KG inference tasks (completion, relation prediction, fact verification, fact generation, reasoning, alignment)?
- [ ] Can I write the TransE scoring formula $f(h,r,t) = \|\mathbf{h} + \mathbf{r} - \mathbf{t}\|$ from memory?
- [ ] Can I compute $\mathbf{h} + \mathbf{r}$ and L1 distances to predict a missing entity by hand in under 2 minutes?
- [ ] Can I explain negative sampling -- how to corrupt a triple and why we need it?
- [ ] Can I write the margin-based ranking loss and explain what $\gamma$ controls?
- [ ] Can I explain **why** TransE fails for N-to-1 relations with a concrete example?
- [ ] Can I describe how TransH fixes TransE's limitation (hyperplane projection)?
- [ ] Can I compare TransE, TransH, TransR in a table?
- [ ] Can I draw the RAG pipeline (Query → Retrieve → Augment → Generate)?
- [ ] Can I explain the difference between RAG and fine-tuning in one sentence?
- [ ] Can I compare RAG vs Fine-Tuning vs Vanilla LLM in a table?
- [ ] Can I explain why modern AI combines KR (structured knowledge) with LLMs (data-driven models)?
- [ ] Can I solve a TransE computation problem like Sample Test Q3 under exam conditions?

---

> **Cross-references:**
> - For KR fundamentals (Semantic Networks, Frames, Rule-Based Systems), see [KR Methods chapter](./C_kr_methods.md)
> - For Symbolic Logic (PL + FOL), see [Symbolic Logic chapter](./A_symbolic_logic.md)
> - For Expert Systems and MYCIN in depth, see [MYCIN chapter](./E_mycin.md)
