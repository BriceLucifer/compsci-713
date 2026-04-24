# Knowledge Graphs & TransE -- Your Complete Guide

## Exam Importance

**MUST-KNOW** | Appeared in **every single past test (100%)** | Worth 2 marks each time

This topic shows up as Question 3 in every paper we have seen. The wording is nearly identical each time. If you nail this chapter, you are banking 2 marks with near certainty.

*(Lec 5 -- W3L1, Lec 6 -- W3L2)*

---

## Part 1: What is a Knowledge Graph? (Building from zero)

### The problem we are trying to solve

Think about everything Google knows. It knows that Albert Einstein was born in Germany, that Germany is in Europe, that Einstein won the Nobel Prize in Physics, and that the Nobel Prize is a scientific award. But here is the thing -- all of that information is scattered across billions of web pages, written in messy human language.

How do you get a machine to *understand* those relationships, not just store the text?

You need structure. You need a way to say: "Einstein" is connected to "Germany" by the relationship "bornIn." Not as a sentence. As a *fact* with a precise format.

### The triple: the atom of a Knowledge Graph

A Knowledge Graph stores facts as **triples**. Every triple has exactly three parts:

```
(Head Entity,  Relation,  Tail Entity)
(Subject,      Predicate, Object)
(h,            r,         t)
```

These three notations all mean the same thing. The exam uses (h, r, t) most often.

Here are some example triples:

```
(Einstein,       bornIn,       Germany)
(Einstein,       wonPrize,     NobelPhysics)
(Germany,        locatedIn,    Europe)
(NobelPhysics,   is-a,         ScientificAward)
(Einstein,       is-a,         Physicist)
(Curie,          is-a,         Physicist)
```

### How triples form a graph

Each entity becomes a **node** (a dot). Each relation becomes a **directed edge** (an arrow). When you connect all the triples, you get a graph -- a web of interconnected facts.

```
                   ┌─────────┐
          bornIn   │ Germany │  locatedIn    ┌────────┐
    ┌─────────────>│         │──────────────>│ Europe │
    │              └─────────┘              └────────┘
    │
┌───┴─────┐  wonPrize   ┌──────────────┐  is-a   ┌──────────────────┐
│ Einstein │────────────>│ NobelPhysics │────────>│ ScientificAward  │
└───┬─────┘              └──────────────┘         └──────────────────┘
    │
    │  is-a    ┌───────────┐
    └─────────>│ Physicist │
               └─────┬─────┘
                      │ is-a
               ┌──────┘
               │
           ┌───┴──┐
           │ Curie │
           └───────┘
```

That is a Knowledge Graph. It is that simple.

### Real-world Knowledge Graphs

| Knowledge Graph | What it does | Scale |
|---|---|---|
| **Google Knowledge Graph** | Powers the info boxes you see in Google Search | Billions of facts |
| **Wikidata** | Structured data behind Wikipedia | 100M+ items |
| **DBpedia** | Extracts structured data from Wikipedia infoboxes | Millions of triples |
| **IBM Watson** | Used KGs to win Jeopardy! | Domain-specific |

*(Lec 6, slides 22-24)*

### Let us build a mini KG from scratch

Suppose you read this paragraph:

> "Marie Curie was born in Poland in 1867. She discovered radium and polonium. She was awarded the Nobel Prize in Physics in 1903 along with Pierre Curie."

Step 1 -- Identify entities: Marie Curie, Poland, Radium, Polonium, Nobel Prize in Physics, Pierre Curie

Step 2 -- Identify relationships and form triples:

```
(Marie Curie,   bornIn,      Poland)
(Marie Curie,   discovered,  Radium)
(Marie Curie,   discovered,  Polonium)
(Marie Curie,   wonPrize,    Nobel Prize in Physics)
(Pierre Curie,  wonPrize,    Nobel Prize in Physics)
```

That is the KG construction process. In practice, AI uses **Named Entity Recognition (NER)** to find entities and **Relation Extraction (RE)** to find relationships. *(Lec 6, slides 30-34)*

### The standard format: RDF and OWL

Knowledge Graphs typically use **RDF (Resource Description Framework)** as their standard format. RDF represents every fact as a triple: (Subject, Predicate, Object) — which maps directly to our (h, r, t) notation. This makes KGs flexible, scalable, and machine-readable. *(Lec 6, slide 24)*

But RDF only stores **facts**. It cannot reason about them. That is where **OWL (Web Ontology Language)** comes in.

**OWL** extends RDF with **logical reasoning and ontology-based classification**. It lets you define hierarchy constraints and inference rules on top of raw facts.

| | RDF | OWL |
|---|---|---|
| **What it stores** | Facts (triples) | Logic + Ontology (extends RDF with richer reasoning) |
| **Reasoning** | None — just retrieval | Can infer new facts from rules |
| **Example** | (Einstein, is-a, Scientist) | Defines "Scientist" as subclass of "Person" → Einstein is-a Scientist → He is-a Person |

Think of it this way: RDF is a filing cabinet full of fact cards. OWL is the filing cabinet **plus** a smart librarian who can draw conclusions from those cards.

*(Lec 6, slides 24-25)*

### Exercise 3: RDF & OWL Inference (slides 26-27) — Worked Example

This is a great example of how OWL rules let you chain reasoning across a KG.

**Setup — A University Knowledge Graph:**

```
(Prof_John,       teaches,      AI_Course)
(AI_Course,       belongs_to,   CS_Department)
(CS_Department,   part_of,      Engineering_Faculty)
(Prof_John,       works_in,     CS_Department)
```

**OWL Rules defined on this KG:**
1. Courses belong to exactly one department
2. If a professor teaches a course → they are part of that course's department
3. Departments are part of a faculty
4. If a professor is in a department → they are a faculty member of that department's faculty

**Question:** Which faculty does Prof. John belong to?

**Answer: Engineering Faculty.** Here is the reasoning chain:

```
Prof_John teaches AI_Course
  → AI_Course belongs_to CS_Department
    → Prof_John is part of CS_Department  (Rule 2)
      → CS_Department part_of Engineering_Faculty  (Rule 3)
        → Prof_John is a faculty member of Engineering_Faculty  (Rule 4)
```

Notice how none of the original triples directly say "Prof_John is in Engineering_Faculty." OWL *inferred* it by chaining rules. This is the power of adding logic on top of raw facts.

### Graph Databases (slide 28)

Once you have a KG, you need somewhere to store and query it. Three major graph database technologies:

| Database | Model | Best For |
|---|---|---|
| **Neo4j** | Property Graph Model | Social networks, fraud detection |
| **RDF Store** | RDF triples | Semantic Web, Wikidata, Google Knowledge Graph |
| **Dgraph** | Distributed graph | Real-time, AI-driven KGs at scale |

*(Lec 6, slide 28)*

### How KGs are constructed (slides 30-32)

We touched on this briefly with the Marie Curie example above. Here is the formal pipeline:

| Step | What Happens | Technique |
|---|---|---|
| **1. Entity Extraction** | Identify entities from raw text | Named Entity Recognition (NER) |
| **2. Relation Extraction** | Identify relationships between entities | Relation Extraction (RE) models |
| **3. Knowledge Integration** | Merge duplicate entities ("Albert Einstein" = "A. Einstein") | Entity resolution / deduplication |
| **4. Storage & Query** | Store triples and enable queries | Neo4j, RDF Stores, SPARQL queries |

The key challenge is step 3 — the same entity can appear under many different names in different sources, and the system needs to recognize they are the same thing.

*(Lec 6, slides 30-32)*

---

## Part 2: The Problem -- Knowledge Graphs Are Incomplete

Here is the uncomfortable truth: **no Knowledge Graph contains every true fact**.

Google's Knowledge Graph has billions of facts, but it is still missing many connections that are actually true. This is not a minor issue -- research estimates that even the largest KGs are significantly incomplete.

### A concrete example

Your KG knows these facts:
```
(Einstein,  bornIn,    Germany)
(Einstein,  is-a,      Physicist)
(Curie,     is-a,      Physicist)
```

But it is *missing* this fact:
```
(Curie,     bornIn,    Poland)       <-- TRUE, but not in the KG!
```

Can the computer *guess* this missing fact? Can it figure out that Curie was probably born in *some country*, and work out which one?

This is the **Knowledge Graph Completion** problem. And it is one of the most important tasks in KG research.

### KG Inference tasks (the exam asks about these)

There are several types of inference tasks. The exam consistently asks you to "introduce a common Knowledge Graph Inference task." Here are the main ones:

| Task | Query Format | What you are predicting | Example |
|---|---|---|---|
| **KG Completion (Link prediction)** | (h, r, ?) or (?, r, t) | The missing entity | (Paris, located_in, ?) → France |
| **Relation Prediction** | (h, ?, t) | The missing relation type | (Einstein, ?, Physics) → "studied" |
| **Fact Verification** | (h, r, t) True/False? | Whether a triple is true | (Moon, madeOf, Cheese) → False |
| **Fact Generation** | Synthesize new triples | Create entirely new facts | (Drug X, treats, ?) → Disease Y |
| **KG Reasoning** | Chain existing facts | Infer new knowledge via logic | (Paris, in France) + (France, in EU) → (Paris, in EU) |
| **KG Alignment** | Match across KGs | Merge entities from multiple KGs | (Barack Obama, ≈, B. Obama) |

*(Lec 6, slide 36)*

**For the exam, link prediction is the safest example to give.** Every model answer we have seen uses it.

---

## Part 3: Why Vectors? The Idea Behind Embeddings

Before we get to TransE, we need to understand *why* we turn everything into vectors.

### The limitation of symbols

In the raw KG, "Einstein" is just a symbol -- a string of characters. "Curie" is another symbol. The computer has no idea that these two symbols are *similar* (both are physicists, both won Nobel Prizes). To the computer, "Einstein" is as different from "Curie" as it is from "Banana."

### The embedding idea

What if we turned each entity into a **list of numbers** -- a vector?

```
Einstein = [0.8, 0.3, 0.9, 0.1]
Curie    = [0.7, 0.4, 0.8, 0.2]
Banana   = [0.1, 0.9, 0.1, 0.8]
```

Now the computer can *measure* similarity. Einstein and Curie have similar numbers -- they are close together in this number space. Banana is far away. The computer has learned something about meaning, just from the numbers.

This is what **Knowledge Graph Embeddings (KGE)** do. They map every entity and every relation into a dense vector in continuous space. And once everything is a vector, you can do *math* on it -- compute distances, predict missing links, reason about relationships.

**Formal definition:** Knowledge Graph Embeddings represent entities and relations as dense vectors in a continuous vector space. These embeddings allow models to predict missing links, validate facts, and reason over structured knowledge. *(Lec 6, slide 38)*

> That definition in bold is essentially the 1-mark answer for the first half of the exam question. Memorize it.

---

## Part 4: TransE -- The Key Model (tested EVERY exam)

### The core idea in one sentence

For a valid triple (h, r, t), the equation **h + r should approximately equal t**.

That is it. That is the entire idea of TransE. Everything else is details.

### The map analogy

Imagine you are standing in a city. Each entity is a location on a map. Each relation is a set of *walking directions*.

- You are standing at "Einstein" (a point on the map)
- Someone gives you directions called "bornIn" (walk 3 blocks east, 1 block south)
- If you follow those directions, you should arrive at "Germany"

If the directions are correct, you end up exactly at Germany. If you end up somewhere else, the directions were wrong -- the triple is probably false.

**TransE works exactly like this, but with vectors instead of map coordinates.**

$$
\mathbf{h} + \mathbf{r} \approx \mathbf{t}
$$

*(Lec 6, slide 41)*

### Concrete numerical example -- work through this with pen and paper

Let us use 2D vectors to keep things simple.

**Setup -- the learned embeddings:**
```
Einstein = [1, 2]
bornIn   = [3, -1]
Germany  = [4, 1]
France   = [5, 3]
Poland   = [6, 3.1]
Curie    = [3, 4]
```

**Test 1: Is (Einstein, bornIn, Germany) true?**
```
h + r = [1, 2] + [3, -1] = [4, 1]
t     = [4, 1]

Distance = ||[4,1] - [4,1]|| = 0

Score = 0  -->  PERFECT MATCH. This triple is very likely true.
```

**Test 2: Is (Einstein, bornIn, France) true?**
```
h + r = [1, 2] + [3, -1] = [4, 1]
t     = [5, 3]

Distance (L2) = sqrt((4-5)^2 + (1-3)^2) = sqrt(1 + 4) = sqrt(5) = 2.24

Score = 2.24  -->  HIGH score. This triple is probably false.
```

**Test 3: Predict (Curie, bornIn, ?)**
```
h + r = [3, 4] + [3, -1] = [6, 3]

Which entity is closest to [6, 3]?
  Poland  = [6, 3.1]  -->  distance = sqrt(0 + 0.01) = 0.1   CLOSEST!
  Germany = [4, 1]    -->  distance = sqrt(4 + 4) = 2.83
  France  = [5, 3]    -->  distance = sqrt(1 + 0) = 1.0

Answer: Poland!  Curie was born in Poland. Correct!
```

See how the model predicted the right answer without anyone telling it? It learned the pattern from existing triples.

### The scoring function

The **scoring function** measures how far off h + r is from t:

$$
f(h, r, t) = \| \mathbf{h} + \mathbf{r} - \mathbf{t} \|_{L_1 / L_2}
$$

- \\( L_1 \\) norm (Manhattan distance): \\( \sum_{i=1}^{d} |h_i + r_i - t_i| \\)
- \\( L_2 \\) norm (Euclidean distance): \\( \sqrt{\sum_{i=1}^{d} (h_i + r_i - t_i)^2} \\)

**The critical rule you must not get backwards:**
- **Smaller score = more likely the triple is true** (h + r is close to t)
- **Larger score = less likely the triple is true** (h + r is far from t)

Think of the score as an *error measurement*. Less error = better fit.

*(Lec 6, slide 42)*

> **Common Misconception:** Many students write that a *higher* TransE score means the triple is more likely true. This is BACKWARDS. The score is a distance. Smaller distance = closer match = more plausible triple. This mistake alone can cost you a mark. Do not make it.

### How TransE trains (the learning process)

The training process in detail *(Lec 6, slides 42-44)*:

1. **Initialize** all entity and relation vectors with random embeddings
2. **Compute scores** for positive (correct) triples using the scoring function:
   - \\( f(h, r, t) = \| \mathbf{h} + \mathbf{r} - \mathbf{t} \| \\) using L1 or L2 norm
3. **Generate negative (corrupted) triples** by randomly replacing the head or tail with a random entity:
   - Correct triple: (Paris, located_in, France)
   - Corrupted triple: (Paris, located_in, **Banana**) — replace tail
   - Or: (**Moon**, located_in, France) — replace head
4. **Compute scores** for the corrupted triples
5. **Optimize** with gradient descent: push correct triple scores **down**, push corrupted triple scores **up**
6. **Optionally normalize** embedding vectors after each update step
7. **Repeat** until convergence

**The two norms in detail:**

- **L1 Norm (Manhattan distance):** \\( \sum_{i=1}^{d} |h_i + r_i - t_i| \\) — sum of absolute differences
- **L2 Norm (Euclidean distance):** \\( \sqrt{\sum_{i=1}^{d} (h_i + r_i - t_i)^2} \\) — straight-line distance

The formal loss function is the **margin-based ranking loss**:

$$
\mathcal{L} = \sum_{(h,r,t) \in S} \sum_{(h',r,t') \in S'} \max(0, \; \gamma + f(h,r,t) - f(h',r,t'))
$$

Breaking this down:
- \\( S \\) = set of correct triples
- \\( S' \\) = set of corrupted (negative) triples
- \\( \gamma > 0 \\) = margin hyperparameter (forces a gap between correct and incorrect scores)
- The loss says: "make sure the correct triple's score is at least \\( \gamma \\) lower than the corrupted triple's score"

*(Lec 6, slides 43-44)*

> You do not need to memorize the loss function formula for the exam (it has not been asked). But understanding the training intuition -- minimize score for true triples, maximize for false -- is essential.

### The lecture's own worked example (Exercise 5 from slides)

This is worth working through because the exam could give you a similar calculation.

**Given:** TransE is trained on: (Paris, located_in, France), (France, part_of, Europe), (Berlin, located_in, Germany), (Germany, part_of, Europe)

**Learned embeddings:**
```
Paris      = (0.5, 0.2, 0.7)
France     = (0.8, 0.4, 1.0)
Europe     = (0.9, 0.3, 1.2)
Germany    = (1.2, 0.6, 1.5)
located_in = (0.3, 0.2, 0.3)
```

**Query:** (Paris, located_in, ?) -- which entity?

**Step 1:** Compute h + r
```
Paris + located_in = (0.5+0.3, 0.2+0.2, 0.7+0.3) = (0.8, 0.4, 1.0)
```

**Step 2:** Compute L1 distance to each candidate

Distance to **France (0.8, 0.4, 1.0)**:
```
|0.8-0.8| + |0.4-0.4| + |1.0-1.0| = 0 + 0 + 0 = 0.0
```

Distance to **Europe (0.9, 0.3, 1.2)**:
```
|0.8-0.9| + |0.4-0.3| + |1.0-1.2| = 0.1 + 0.1 + 0.2 = 0.4
```

Distance to **Germany (1.2, 0.6, 1.5)**:
```
|0.8-1.2| + |0.4-0.6| + |1.0-1.5| = 0.4 + 0.2 + 0.5 = 1.1
```

**Answer:** France (distance 0.0) -- the closest entity.

*(Lec 6, slides 45-46)*

### TransE limitations (good to mention for bonus marks)

TransE struggles with certain relation types because it uses a single translation vector per relation:

| Relation type | Example | Why TransE fails |
|---|---|---|
| **1-to-N** | (Einstein, fieldOf, Physics), (Einstein, fieldOf, Math) | Multiple tails for same (h,r) — h + r cannot equal two different t vectors |
| **N-to-1** | (Paris, locatedIn, France), (Lyon, locatedIn, France), (Marseille, locatedIn, France) | All head vectors collapse to the same point |
| **N-to-N** | Symmetric and transitive relations | Combines both problems |

**Concrete collapse example (slide 47):**

Consider these three true triples with the same relation and tail:
```
(Paris,     located_in, France)   →  Paris + located_in = France
(Lyon,      located_in, France)   →  Lyon + located_in = France
(Marseille, located_in, France)   →  Marseille + located_in = France
```

Since all three must satisfy h + r = t with the **same** r and **same** t, TransE forces:
```
Paris + located_in = France
Lyon + located_in = France
Marseille + located_in = France
```
This means Paris = Lyon = Marseille. They all **collapse to the same embedding**, losing all distinctiveness between these three very different cities. That is a serious problem.

*(Lec 6, slide 47)*

### Beyond TransE (slide 48)

Several models address TransE's limitations:

| Model | Key Idea | What It Fixes |
|---|---|---|
| **TransH** | Projects entities onto **relation-specific hyperplanes** before translation | Handles many-to-one relations — different entities can project to different points on the hyperplane |
| **TransR** | Projects entities into **relation-specific spaces** (separate entity and relation dimensions) | Each relation gets its own space, so entities can have different representations for different relations |
| **ComplEx** | Uses **complex-valued embeddings** (real + imaginary parts) | Naturally handles symmetric and antisymmetric relations |

For this exam, you only need to know TransE in detail. But mentioning that TransH/TransR exist and *why* they were invented (to fix TransE's N-to-1 and symmetric relation problems) is a good way to show deeper understanding.

*(Lec 6, slide 48)*

---

## Part 5: Knowledge Representation Context (Lecture 5-6 Background)

The KG topic sits within the broader "Knowledge Representation" module. While the exam tests KG/TransE specifically, understanding the surrounding concepts helps you connect ideas. Here is a quick map:

### Semantic Networks (semantic networks -- early KGs)

A **Semantic Network** is an older, simpler version of a Knowledge Graph. Nodes are concepts, edges are relationships like "is-a" and "has-property."

```
Cat  --is-a-->  Mammal  --is-a-->  Animal
Cat  --has-->   Fur
Mammal --has-property--> Warm-blooded
```

The AI can infer: "Cat is warm-blooded" by traversing the is-a chain to Mammal, which has the property warm-blooded. This is called **property inheritance**.

Key difference from KGs: Semantic networks are small, non-standardized, conceptual. KGs are large-scale, use RDF standards, and store actual facts. *(Lec 6, slide 4)*

### Frames

A **Frame** groups information about an entity into **slot-filler** structures (like an object in programming):

| Frame: Car | Slot | Filler |
|---|---|---|
| | Brand | Tesla |
| | Colour | Red |
| | Engine | Electric |
| | Owner | Alice |

Frames support **default values** (a Dog frame has legs=4 unless stated otherwise) and **inheritance** (a Dog inherits has_hair=True from the Mammal frame). *(Lec 5, slides 19-20)*

### Expert Systems

An Expert System mimics human expert reasoning using three components:

| Component | Role | Analogy |
|---|---|---|
| **Knowledge Base** | Stores domain facts and IF-THEN rules | The textbook |
| **Inference Engine** | Applies rules to derive conclusions | The reasoning brain |
| **User Interface** | Collects input, displays results | The conversation |

Classic example: **MYCIN** (1970s) for diagnosing bacterial infections. *(Lec 6, slide 9)*

### Ontologies

An **Ontology** defines the *schema* -- what types of entities exist, what relationships are allowed, what constraints apply.

| | Ontology | Knowledge Graph |
|---|---|---|
| Stores | Rules, definitions, constraints | Actual facts (triples) |
| Example | "A Person can be bornIn a Country" | "(Einstein, bornIn, Germany)" |
| Analogy | The grammar of a language | Sentences written in that language |
| Standard | OWL (Web Ontology Language) | RDF (Resource Description Framework) |

Key insight: AI systems integrate both -- the ontology provides the rules/schema, the KG provides the facts. *(Lec 6, slides 14-16)*

---

## Part 5B: RAG — Retrieval-Augmented Generation (slides 49-53)

This is where Knowledge Graphs meet modern Large Language Models.

### The problem with LLMs alone

LLMs like GPT are impressive, but they have three critical weaknesses:

1. **Hallucination** — they confidently make up facts that sound plausible but are wrong
2. **No explicit reasoning** — they pattern-match rather than logically chain facts
3. **Memory limitations** — they only know what was in their training data (which has a cutoff date)

### The RAG solution

**RAG (Retrieval-Augmented Generation)** solves this by combining Knowledge Representation (KGs, databases, documents) with LLMs. Instead of asking the LLM to answer from memory, you first *retrieve* relevant information, then feed it to the LLM as context.

Think of it like this: instead of asking someone to answer a question from memory (where they might make things up), you hand them the relevant textbook pages first, then ask them to answer.

### The RAG pipeline

```
User Query
    │
    ▼
┌──────────────────────────┐
│  1. Knowledge Retrieval  │  Search databases, KGs, documents
│     (BM25, DPR, FAISS)   │  using retrieval models
└──────────┬───────────────┘
           │ Retrieved context
           ▼
┌──────────────────────────┐
│  2. Contextual           │  Combine retrieved info
│     Integration          │  with the original query
└──────────┬───────────────┘
           │ Augmented prompt
           ▼
┌──────────────────────────┐
│  3. LLM Response         │  Generate answer grounded
│     Generation           │  in retrieved evidence
│     (with re-ranking)    │
└──────────────────────────┘
```

### Concrete example

**Query:** "Who won the Turing Award in 2023?"

- **Without RAG:** LLM might hallucinate an answer based on training data, which may not include 2023 events
- **With RAG:**
  1. Retrieval system searches a database/KG and finds a document about the 2023 Turing Award
  2. That document is passed to the LLM as context
  3. LLM generates a grounded answer based on the retrieved evidence

### Key retrieval methods mentioned in slides

| Method | What it does |
|---|---|
| **BM25** | Classic keyword-based search (like a smart text search) |
| **DPR (Dense Passage Retrieval)** | Uses embeddings to find semantically relevant passages |
| **FAISS** | Facebook's library for fast similarity search over dense vectors |

*(Lec 6, slides 49-53)*

> **Exam tip:** RAG has not appeared in past KG questions, but it connects KGs to LLMs — a very hot topic. If the exam asks about combining Knowledge Representation with modern AI, RAG is your go-to answer.

---

## Part 6: Every Past Paper Question, Walked Through

### 2026 Sample Test -- Question 3 [2 marks]

> "What is the role of entity and relation embeddings in knowledge graph completion? Introduce a common Knowledge Graph Inference task and provide one example of how such embeddings help in a typical KG task."

**Full model answer (aim for this level of detail):**

Knowledge Graph Embeddings (KGE) represent entities and relations as dense vectors in a continuous vector space. These embeddings allow models to predict missing links, validate facts, and reason over structured knowledge.

A common KG inference task is **link prediction**, where the goal is to predict the missing entity in an incomplete triple such as (h, r, ?) or (?, r, t). For example, given embeddings of entities and relations, a model like TransE might discover that (Einstein, bornIn, ?) -> Germany, even if this triple was not originally present in the KG. It does this by computing h + r and finding the entity whose embedding is nearest to the result.

**Mark allocation:**
- 1 mark: Define KGE as dense vectors in continuous space that allow prediction/reasoning
- 1 mark: Name an inference task (link prediction) + give a concrete example

*(Source: 2026 Sample Test Answers, page 2)*

---

### 2025 Sample Test -- Question 3 [2 marks]

> Identical question to 2026.

**The same answer works.** This question has appeared word-for-word in both sample tests.

*(Source: 2025 Sample Test Answers, page 2)*

---

### 2025 Real Test -- Question 3 [2 marks]

> (a) "Briefly explain how TransE learns representations." [1 mark]
> (b) "What is the basic idea behind TransE's scoring function?" [1 mark]

**Model answer for (a):**

TransE is a translation-based embedding model that represents **entities and relations as vectors in the same space**. It assumes that for a valid triple (h, r, t), the embedding of the tail entity t should be **close to** the embedding of the head entity h plus the relation vector r, i.e., **h + r ≈ t**.

**Model answer for (b):**

TransE defines a distance-based scoring function: **f(h, r, t) = ||h + r - t||** using L1 or L2 norm. The **smaller** the score, the **more likely** the triple is true, because a smaller distance means h + r is closer to t.

**Mark allocation:**
- (a) 1 mark: entities and relations as vectors + h + r ≈ t for valid triples
- (b) 1 mark: correct formula + smaller score = more likely true

*(Source: 2025 Real Test Answers, page 3)*

---

## Part 7: How to Write the Perfect Answer

### The 2-mark version (KGE role + inference task)

This is the most common format. You need two things in your answer:

**Sentence 1-2 (1 mark):** Define what KGE does.
> "Knowledge Graph Embeddings represent entities and relations as dense vectors in a continuous vector space. These embeddings allow models to predict missing links, validate facts, and reason over structured knowledge."

**Sentence 3-4 (1 mark):** Name a task + give an example.
> "A common inference task is link prediction, which predicts the missing entity in an incomplete triple such as (h, r, ?). For example, given learned embeddings, the model can predict (Einstein, bornIn, ?) -> Germany."

Total: 4 sentences. Under 1 minute to write. Full marks.

### The 1-mark version (TransE mechanism only)

When they ask specifically about TransE:
> "TransE represents entities and relations as vectors in the same embedding space. For a valid triple (h, r, t), it enforces h + r ≈ t, meaning the head vector plus the relation vector should approximately equal the tail vector."

2 sentences. 30 seconds. Full mark.

### The 1-mark version (scoring function only)

> "The TransE scoring function is f(h, r, t) = ||h + r - t||, measured using L1 or L2 norm. A smaller score indicates the triple is more likely true."

2 sentences. Full mark.

### What NOT to write

- Do NOT say "higher score = more likely true" (this is backwards)
- Do NOT confuse Knowledge Graphs with Ontologies (KG = facts, Ontology = rules/schema)
- Do NOT write a paragraph when two sentences will do (the exam says "Be concise and clear")
- Do NOT forget the example -- every model answer includes one

---

## Part 8: Practice Problems (with full solutions)

### Problem 1: Basic TransE computation

**Given:** h = [2, 1], r = [1, 3], t = [3, 4]

Compute the TransE score using L1 norm. Is this triple likely true?

<details>
<summary>Solution</summary>

```
h + r = [2+1, 1+3] = [3, 4]
t     = [3, 4]

L1 distance = |3-3| + |4-4| = 0 + 0 = 0

Score = 0 --> This triple is very likely true (perfect match).
```

</details>

---

### Problem 2: Comparing two candidate triples

**Given:** h = [1, 0], r = [2, 1]

Candidate A: t_A = [3, 1]
Candidate B: t_B = [4, 2]

Which candidate is more likely the correct tail entity?

<details>
<summary>Solution</summary>

```
h + r = [1+2, 0+1] = [3, 1]

Distance to t_A = |3-3| + |1-1| = 0      --> Score = 0
Distance to t_B = |3-4| + |1-2| = 1 + 1 = 2  --> Score = 2

Candidate A (score 0) is much more likely. Lower score = more plausible.
```

</details>

---

### Problem 3: Why TransE fails with symmetric relations

**Given:** (Alice, friendOf, Bob) is true. TransE learns h + r = t, so:

Alice + friendOf = Bob

Now, should (Bob, friendOf, Alice) also be true?

<details>
<summary>Solution</summary>

If Alice + friendOf = Bob, then for (Bob, friendOf, Alice) to also hold:
Bob + friendOf = Alice

But this means:
(Alice + friendOf) + friendOf = Alice
Alice + 2*friendOf = Alice
2*friendOf = [0, 0, ...]

This forces the friendOf vector to be the zero vector, which makes it useless for distinguishing any other triples using friendOf. This is why TransE **cannot properly model symmetric relations** -- it would need the relation vector to be zero, which collapses the relation's meaning.

</details>

---

### Problem 4: Write a 2-mark exam answer

**Question:** "What is the role of entity and relation embeddings in knowledge graph completion? Introduce a common KG inference task and provide one example."

<details>
<summary>Model answer</summary>

Knowledge Graph Embeddings represent entities and relations as dense vectors in a continuous vector space. This enables models to predict missing links, validate the plausibility of new facts, and perform reasoning over structured knowledge.

A common inference task is link prediction, where the goal is to predict the missing entity in a triple such as (h, r, ?) or (?, r, t). For example, given learned embeddings, a model like TransE can predict (Einstein, bornIn, ?) -> Germany by computing h + r and finding the nearest entity vector.

</details>

---

### Problem 5: Write a 1-mark exam answer

**Question:** "Briefly explain how TransE learns representations."

<details>
<summary>Model answer</summary>

TransE represents both entities and relations as vectors in the same embedding space. For a valid triple (h, r, t), the model enforces that the head vector plus the relation vector should approximately equal the tail vector, i.e., h + r ≈ t.

</details>

---

### Problem 6: Link prediction with 3D vectors

**Given:**
```
Tokyo      = (0.2, 0.8, 0.5)
capitalOf  = (0.6, -0.3, 0.4)
Japan      = (0.8, 0.5, 0.9)
Korea      = (0.9, 0.6, 1.1)
China      = (0.7, 0.4, 0.8)
```

Predict: (Tokyo, capitalOf, ?) using L1 distance.

<details>
<summary>Solution</summary>

```
h + r = (0.2+0.6, 0.8+(-0.3), 0.5+0.4) = (0.8, 0.5, 0.9)

Distance to Japan (0.8, 0.5, 0.9):
|0.8-0.8| + |0.5-0.5| + |0.9-0.9| = 0.0

Distance to Korea (0.9, 0.6, 1.1):
|0.8-0.9| + |0.5-0.6| + |0.9-1.1| = 0.1 + 0.1 + 0.2 = 0.4

Distance to China (0.7, 0.4, 0.8):
|0.8-0.7| + |0.5-0.4| + |0.9-0.8| = 0.1 + 0.1 + 0.1 = 0.3

Japan has the smallest distance (0.0), so the prediction is Japan.
```

</details>

---

### Problem 7: Why embeddings beat lookup tables

**Question:** Why can't we just use a lookup table (a database) instead of embeddings to complete a KG?

<details>
<summary>Solution</summary>

A lookup table can only retrieve facts that are *explicitly stored*. If (Curie, bornIn, Poland) is not in the table, the table returns nothing.

Embeddings can **generalize to unseen triples**. By learning patterns from existing triples (e.g., the "bornIn" relation tends to map scientists to countries), the model can predict facts it has never seen. The continuous vector space captures semantic similarity -- entities that appear in similar contexts end up with similar vectors, enabling meaningful predictions.

This is the fundamental advantage of embeddings: they go beyond retrieval to **inference**.

</details>

---

## Part 9: English Expression Guide

### Defining Knowledge Graphs

- "A Knowledge Graph stores real-world facts as triples in the form (head, relation, tail)."
- "Each triple represents a factual relationship between two entities."

### Explaining the role of KGE

- "Knowledge Graph Embeddings map discrete entities and relations into a continuous vector space, enabling mathematical operations for reasoning."
- "The primary purpose of KGE is to predict missing links in incomplete Knowledge Graphs."

### Explaining TransE

- "TransE models relations as translation operations in the embedding space."
- "The key idea is that for a valid triple, the head entity plus the relation vector should approximately equal the tail entity."
- "The scoring function measures the distance between h + r and t -- a smaller distance indicates higher plausibility."

### Describing inference tasks

- "Link prediction is the task of predicting the missing entity in an incomplete triple."
- "Given a query such as (Einstein, bornIn, ?), the model computes h + r and finds the entity whose embedding is nearest."

### Words students commonly confuse

| Confused Pair | How to distinguish them |
|---|---|
| "high score = good" vs "low score = good" | In TransE, **lower** score = **better**. The score is a distance. Do NOT say high score means the triple is true. |
| Knowledge Graph vs Ontology | KG stores **facts** as triples. Ontology defines the **schema/rules**. |
| Embedding vs Encoding | Embedding = learned dense vector representation. Encoding = any transformation to a different format. |
| Entity vs Node | Same concept in KG context, but "entity" is the standard KG term. Use "entity" in your answer. |
| Semantic Network vs Knowledge Graph | Semantic networks are early, small-scale, non-standardized. KGs are modern, large-scale, use RDF standards. |

---

## Part 10: Self-Check Checklist

Before the exam, make sure you can do ALL of these:

- [ ] Define a Knowledge Graph and write the triple format (h, r, t) from memory
- [ ] Give at least two real-world KG examples (Google Knowledge Graph, Wikidata)
- [ ] Explain the difference between RDF (facts/triples) and OWL (logic + ontology)
- [ ] Walk through an OWL inference chain (like the Prof_John → Engineering_Faculty example)
- [ ] Name the four KG construction steps: Entity Extraction → Relation Extraction → Knowledge Integration → Storage & Query
- [ ] List at least four KG inference tasks (completion, relation prediction, fact verification, reasoning, alignment)
- [ ] State the TransE principle in one sentence (h + r ≈ t for valid triples)
- [ ] Write the TransE scoring function from memory: f(h,r,t) = ||h + r - t||
- [ ] Correctly state that **smaller** score = **more likely** true (do NOT get this backwards)
- [ ] Explain the difference between L1 (Manhattan) and L2 (Euclidean) norms
- [ ] Describe the margin-based ranking loss intuition (correct triples score lower than corrupted by at least gamma)
- [ ] Walk through a link prediction example with actual numbers (like Problem 6 above)
- [ ] Explain why TransE struggles with N-to-1 relations (entity collapse problem) and symmetric relations
- [ ] Name TransH, TransR, and ComplEx and state what each fixes
- [ ] Explain the difference between a Knowledge Graph and an Ontology in one sentence
- [ ] Explain what RAG is and why it helps LLMs (retrieval grounds the answer, reduces hallucination)
- [ ] Write the 2-mark answer (KGE role + inference task + example) in under 2 minutes
- [ ] Write the 1-mark answer (TransE mechanism) in under 1 minute

---

## Quick Reference Card (for your cheat sheet)

If you are putting this on your handwritten notes page, here is the minimum you need:

```
KG: stores facts as triples (h, r, t)
    Real examples: Google KG, Wikidata, DBpedia
    RDF = facts (triples)    OWL = logic + ontology (extends RDF)

KG Construction: NER → Relation Extraction → Knowledge Integration → Storage

KGE: entities & relations -> dense vectors in continuous space
     Purpose: predict missing links, validate facts, reason

TransE: h + r ≈ t  (for valid triples)
        Scoring: f(h,r,t) = ||h + r - t||  (L1 or L2)
        SMALLER score = MORE LIKELY true
        Training: margin-based ranking loss, minimize for true, maximize for corrupted
        Limitation: N-to-1 collapse (Paris=Lyon=Marseille)
        Fixes: TransH (hyperplanes), TransR (relation spaces), ComplEx (complex vectors)

KG Tasks: Completion, Relation Prediction, Fact Verification,
          Fact Generation, KG Reasoning, KG Alignment

Link prediction: (h, r, ?) -> compute h+r, find nearest entity
Example: (Einstein, bornIn, ?) -> h+r -> nearest = Germany

Ontology = schema/rules     KG = actual facts
RAG = Retrieve docs/KG facts → feed to LLM → grounded answer (no hallucination)
```

That fits in about 10 lines. With those 10 lines on your cheat sheet, you can answer any KG question this exam throws at you.
