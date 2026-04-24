# Knowledge Representation Methods（知识表示方法）

## 🎯 Exam Importance

🟠 **HIGH FREQUENCY** | Background knowledge for Knowledge Graphs and Expert Systems questions

Knowledge Representation (KR) is the foundation that underpins KG questions, MYCIN/expert system questions, and semantic reasoning questions.
Understanding KR methods is essential for answering the 🔴 must-know KG/TransE questions confidently.

*(Lec 5 — W3L1)*

---

## 📖 Core Concepts

| Term | Definition |
|---|---|
| **Knowledge Representation（知识表示）** | Methods to store, retrieve, and handle knowledge so machines can reason intelligently. |
| **Semantic Network（语义网络）** | A graph where nodes are concepts and edges are relationships (is-a, has-property). |
| **Frame（框架）** | A structured slot-filler data structure for representing stereotyped knowledge, similar to OOP classes. |
| **Rule-Based System（基于规则的系统）** | A system that uses IF-THEN rules to make decisions or draw conclusions. |
| **Knowledge Graph（知识图谱）** | A large-scale graph storing real-world facts as RDF triples: (Subject, Predicate, Object). |
| **Ontology（本体）** | A formal specification of concepts, relationships, and constraints within a domain. |
| **Property Inheritance（属性继承）** | The ability to pass attributes from a parent concept to child concepts through a hierarchy. |
| **Forward Chaining（前向链接）** | Reasoning from data toward conclusions — start with known facts, fire matching rules. |
| **Backward Chaining（后向链接）** | Reasoning from a goal backward to find supporting evidence. |

---

## 🧠 Feynman Draft — Part 1: What Is Knowledge Representation?

### The AI doctor problem

Imagine you are building an AI doctor. This system needs to know things like:

- Flu causes fever.
- Aspirin treats headaches.
- Pneumonia is serious and requires antibiotics.
- A patient with fever AND cough AND fatigue might have flu.

Now here is the real question: **how do you STORE all of this knowledge so that the AI can actually USE it?**

You could dump everything into a big text file. But then how does the AI search through it? How does it connect "flu causes fever" with "this patient has a fever" to conclude "this patient might have flu"? A text dump is not enough. You need **structure**.

Knowledge Representation is the study of how to organize, store, and retrieve knowledge in a form that a computer can reason with. Think of it as choosing the right **filing system** for your AI's brain.

A bad filing system means your AI cannot find the right fact at the right time. A good filing system means your AI can not only look up facts but also **infer new ones** — connect the dots between things it already knows.

### The five requirements — what makes a KR system "good"?

Not all filing systems are equal. From the lectures *(Lec 5)*, a good KR system must satisfy **five requirements**. Let us walk through each one using a self-driving car as our running example.

**Requirement 1: Expressiveness（表达力）**

Your KR system must be able to represent the knowledge you actually need. For a self-driving car, you need to represent traffic rules, road layouts, pedestrian behavior, weather conditions, speed limits, and more. If your KR system can only handle simple yes/no facts, it is not expressive enough.

Think of it this way: a language with only 50 words cannot describe a novel. Your KR system needs enough "vocabulary" to capture complex real-world knowledge.

**Requirement 2: Computational Efficiency（计算效率）**

It is not enough to store knowledge — you need to *retrieve and reason with it quickly*. A self-driving car making a lane-change decision has milliseconds, not minutes. If looking up "is it safe to turn left?" requires scanning every fact in the system, you are in trouble.

Analogy: imagine a librarian who can find any book in 2 seconds versus one who takes 20 minutes. Both have the same books, but only one is useful in a time-critical situation.

**Requirement 3: Scalability（可扩展性）**

Your system must handle growing amounts of knowledge without breaking. A self-driving car that works perfectly in one city must be able to learn the roads of a second city, a third city, and so on. If adding more knowledge makes the whole system grind to a halt, it does not scale.

Analogy: a warehouse that can add more shelves when more stock arrives, versus a closet that is already full.

**Requirement 4: Interpretability（可解释性）**

Humans need to understand what the system knows and why it made a decision. If your self-driving car refuses to turn left, you need to be able to inspect its knowledge and see: "Ah, it knows there is a no-left-turn sign at this intersection." Black-box knowledge that nobody can read or debug is dangerous.

Analogy: a transparent filing cabinet versus a locked safe where nobody has the key.

**Requirement 5: Modifiability（可修改性）**

Knowledge changes. Speed limits get updated. New road construction happens. Your KR system must make it easy to add, remove, or change knowledge without rewriting everything from scratch.

Analogy: a loose-leaf binder where you can swap pages, versus a stone tablet where every change requires a chisel.

| Requirement | What It Means | Self-Driving Car Example |
|---|---|---|
| **Expressiveness** | Can represent complex, varied knowledge | Must handle rules, maps, weather, behavior |
| **Computational Efficiency** | Fast retrieval and reasoning | Lane-change decisions in milliseconds |
| **Scalability** | Handles growing knowledge | Works in one city, then ten, then a hundred |
| **Interpretability** | Humans can inspect and understand | Engineers can debug why it stopped |
| **Modifiability** | Easy to update | New speed limit? Change one entry, not the whole system |

💡 **Core Intuition:** KR is about choosing the right container for knowledge — different containers suit different tasks, but all must be expressive, fast, scalable, readable, and updatable.

---

## 🧠 Feynman Draft — Part 2: Symbolic Logic in KR

Before we get to the fancy graph-based methods, let us start with the oldest approach: using **formal logic** to represent knowledge.

The idea is straightforward. You take natural language facts and translate them into precise logical statements. Remember propositional logic and first-order logic from the Symbolic Logic chapter? Here is where they become practical.

### Example: encoding medical knowledge in FOL

Natural language: "Every patient with flu has a fever."

First-Order Logic:

\\[ \forall x \; (\text{Flu}(x) \rightarrow \text{HasSymptom}(x, \text{Fever})) \\]

Natural language: "Aspirin treats headaches."

FOL:

\\[ \text{Treats}(\text{Aspirin}, \text{Headache}) \\]

Natural language: "If a patient has fever and cough, they might have flu."

FOL:

\\[ \forall x \; (\text{HasSymptom}(x, \text{Fever}) \land \text{HasSymptom}(x, \text{Cough}) \rightarrow \text{PossibleDiagnosis}(x, \text{Flu})) \\]

Once you have these logical statements, you can use **formal inference rules** (modus ponens, resolution, etc.) to derive new conclusions automatically. Given the fact \\(\text{Flu}(\text{Alice})\\), the system can infer \\(\text{HasSymptom}(\text{Alice}, \text{Fever})\\) purely through logical deduction.

### Strengths of symbolic logic for KR

- **Precision**: no ambiguity — every statement has an exact meaning
- **Formal inference**: can automatically prove new facts from existing ones
- **Well-studied**: centuries of mathematical theory behind it

### Weaknesses of symbolic logic for KR

- **Brittle**: real-world knowledge is messy and full of exceptions ("birds fly... except penguins, ostriches, injured birds...")
- **Cannot represent uncertainty**: logic deals in true/false, but medicine often deals in "probably" and "unlikely"
- **Hard to scale**: writing every piece of knowledge as a logical formula is tedious and error-prone

⚠️ **Common Misconception:** Students sometimes think symbolic logic is outdated and irrelevant. In fact, it is the theoretical backbone of rule-based systems, ontologies, and even parts of modern knowledge graph reasoning. The exam may ask you to write FOL expressions for KR — be ready.

---

## 🧠 Feynman Draft — Part 3: Semantic Networks

### Facts as a map

Picture a city map. Cities are dots, roads are lines connecting them, and each road has a label ("highway", "side street", "one-way").

A **Semantic Network** works exactly the same way:
- **Nodes** = concepts (Dog, Animal, Fur, Bark)
- **Edges** = labeled relationships between concepts

Here is a simple semantic network for animals:

```
              Animal
                ^
                | is-a
                |
             Mammal ----has-property----> Warm-blooded
                ^
                | is-a
                |
               Cat ----has-property----> Fur
                |
                +------has-property----> Whiskers
```

And here is one for a different domain — geography:

```
   Europe
     ^
     | locatedIn
     |
   Germany ----capitalIs----> Berlin
     ^
     | bornIn
     |
  Einstein ----is-a----> Physicist
```

### The magic trick: property inheritance

This is the most important concept in semantic networks, and it comes up on exams repeatedly.

Look at this hierarchy:

```
           Animal ----has-property----> Needs-Food
              ^
              | is-a
              |
           Mammal ----has-property----> Warm-blooded
              ^                         Has-Hair
              | is-a
              |
             Cat ----has-property----> Purrs
```

Now, nobody explicitly told the system that "Cat is warm-blooded" or "Cat needs food." But the system can **infer** these facts by following the is-a chain upward:

1. Cat **is-a** Mammal
2. Mammal **has-property** Warm-blooded
3. Therefore: Cat **has-property** Warm-blooded (inherited!)

This continues further:

4. Mammal **is-a** Animal
5. Animal **has-property** Needs-Food
6. Therefore: Cat **has-property** Needs-Food (inherited through two levels!)

This is **property inheritance** — child nodes automatically receive the properties of all their ancestors in the is-a hierarchy. It is powerful because you do not need to repeat common facts for every single concept.

### A concrete toy example

Suppose we have these explicit facts in our semantic network:

- Dog **is-a** Mammal
- Mammal **is-a** Animal
- Animal **has-property** Breathes
- Mammal **has-property** Has-Hair
- Dog **has-property** Can-Bark

Question: Does Dog breathe?

Reasoning chain:
1. Dog is-a Mammal (direct edge)
2. Mammal is-a Animal (direct edge)
3. Animal has-property Breathes (direct edge)
4. By inheritance: Dog has-property Breathes ✓

The system never needed to be told "Dog breathes" explicitly. It figured it out.

### Strengths of semantic networks

- **Intuitive**: mirrors how humans organize categories mentally
- **Supports inference**: property inheritance lets you derive new knowledge
- **Visual**: easy to draw and understand (great for exam diagrams)
- **Efficient retrieval**: just follow edges from a node to find related concepts

### Weaknesses of semantic networks

- **No standardization**: there is no universal rule about what edge labels to use. One person writes "is-a", another writes "type-of", another writes "subclass-of" — they all mean the same thing but the system does not know that.
- **Cannot handle uncertainty**: every edge is either there or not. You cannot say "Dog *probably* has-property Friendly."
- **Scales poorly**: as the network grows to thousands of nodes, it becomes tangled and hard to maintain.
- **Exception handling is awkward**: penguins are birds but cannot fly. The is-a hierarchy says Bird has-property Can-Fly, so Penguin inherits Can-Fly, which is wrong. You need special "exception" mechanisms that make the network messy.

---

## 🧠 Feynman Draft — Part 4: Frames

### Knowledge as forms to fill in

Now imagine you are checking into a hotel. They hand you a registration form:

| Slot | Filler |
|---|---|
| Name | _______ |
| Check-in date | _______ |
| Room type | Standard (default) |
| Breakfast included | Yes (default) |

A **Frame** is exactly this — a structured template with **slots** (attributes) and **fillers** (values). Some slots have **default values** that apply unless you override them.

### Frame example: the animal kingdom

```
Frame: Animal
  Slot: breathes       Filler: True
  Slot: needs-food     Filler: True

Frame: Mammal (inherits from Animal)
  Slot: has-hair       Filler: True
  Slot: warm-blooded   Filler: True

Frame: Dog (inherits from Mammal)
  Slot: can-bark       Filler: True
  Slot: legs           Filler: 4

Frame: Bird (inherits from Animal)
  Slot: can-fly        Filler: True (default)
  Slot: has-wings      Filler: True
  Slot: legs           Filler: 2

Frame: Penguin (inherits from Bird)
  Slot: can-fly        Filler: False    ← overrides the default!
  Slot: habitat        Filler: Antarctic
```

Notice how Penguin inherits everything from Bird (has-wings = True, legs = 2) but **overrides** the can-fly slot. This is exactly how **class inheritance with method overriding** works in OOP.

### Frames vs OOP — the connection

This is worth knowing because the exam might ask you to explain frames using a programming analogy.

| Concept | Frame Terminology | OOP Terminology |
|---|---|---|
| Template | Frame | Class |
| Attribute | Slot | Field / Property |
| Value | Filler | Value |
| Hierarchy | is-a link | extends / inherits |
| Default value | Default filler | Default field value |
| Override | Override slot | Override method/field |

This is not a coincidence. OOP was partly inspired by frame-based AI research from the 1970s (Marvin Minsky).

### A concrete data example

```
Frame: Car
  Slot: brand         Filler: _______
  Slot: color         Filler: _______
  Slot: engine        Filler: Gasoline (default)
  Slot: wheels        Filler: 4
  Slot: owner         Filler: _______

Instance: my-car (instance of Car)
  Slot: brand         Filler: Tesla
  Slot: color         Filler: Red
  Slot: engine        Filler: Electric  ← overrides default
  Slot: owner         Filler: Alice
  (wheels = 4, inherited from Car)
```

### Strengths of frames

- **Organized and structured**: every concept has a clear template
- **Supports defaults**: common properties do not need to be repeated
- **Inheritance with overrides**: handles exceptions cleanly (unlike semantic networks)
- **Familiar to programmers**: works like OOP classes

### Weaknesses of frames

- **Rigid schema**: every concept must fit into a predefined template
- **Hard to scale**: thousands of frames with complex inheritance become difficult to manage
- **Not great for relational knowledge**: frames describe individual concepts well, but relationships between concepts are secondary

---

## 🧠 Feynman Draft — Part 5: Rule-Based Systems

### Knowledge as recipes

Think of a cookbook. Each recipe says: "IF you have these ingredients AND you do these steps, THEN you get this dish."

A **Rule-Based System** stores all of its knowledge as IF-THEN rules:

```
Rule 1: IF patient has fever AND patient has cough
        THEN suspect flu

Rule 2: IF suspect flu AND no complications
        THEN prescribe rest and fluids

Rule 3: IF patient has fever AND patient has rash AND patient is child
        THEN suspect measles

Rule 4: IF suspect measles
        THEN recommend isolation AND contact health authority
```

Given a set of **known facts** about a patient, the system checks which rules' IF-conditions are satisfied, fires those rules, and produces conclusions. Those conclusions may trigger further rules, creating a **chain of reasoning**.

### Forward chaining vs backward chaining

There are two ways to run a rule-based system. This is an important distinction for the exam.

**Forward Chaining（前向链接）: data drives conclusions**

You start with what you know (the facts) and keep firing rules until no more rules apply.

```
Known facts: {fever, cough}

Step 1: Rule 1 matches (fever AND cough) → add "suspect flu"
Step 2: Rule 2 matches (suspect flu AND no complications [assumed]) → add "prescribe rest"
Step 3: No more rules match → STOP

Final conclusions: {fever, cough, suspect flu, prescribe rest}
```

Forward chaining is **data-driven**: you start with evidence and see where it leads.

**Backward Chaining（后向链接）: goals drive evidence search**

You start with a goal (something you want to prove) and work backward to find supporting evidence.

```
Goal: Does the patient have measles?

Step 1: Rule 3 says measles requires {fever, rash, is-child}
Step 2: Check: does the patient have fever? → YES (known fact)
Step 3: Check: does the patient have rash? → YES (known fact)
Step 4: Check: is the patient a child? → YES (known fact)
Step 5: All conditions met → CONCLUDE measles
```

Backward chaining is **goal-driven**: you start with a hypothesis and see if the evidence supports it.

| Aspect | Forward Chaining | Backward Chaining |
|---|---|---|
| Direction | Data → Conclusions | Goal → Evidence |
| Starting point | Known facts | A question or hypothesis |
| Strategy | Fire all matching rules | Find rules that conclude the goal |
| Analogy | Detective collecting clues | Lawyer building a case for a verdict |
| Use case | Monitoring systems, alerts | Diagnostic systems, Q&A |

### Connection to expert systems

Rule-based systems are the foundation of **Expert Systems** like MYCIN (which diagnoses bacterial infections). MYCIN uses backward chaining with **certainty factors** to handle uncertainty — something basic rule-based systems cannot do. This is covered in detail in the [Expert Systems chapter](./E_mycin.md).

### Strengths of rule-based systems

- **Transparent**: you can trace exactly which rules fired and why — full explainability
- **Easy for domain experts**: a doctor can write "IF fever AND cough THEN flu" without knowing programming
- **Modular**: each rule is independent, so you can add or remove rules without breaking others (in theory)

### Weaknesses of rule-based systems

- **Does not scale well**: hundreds of interacting rules become very hard to manage and debug
- **Brittle**: if the real world does not match the rules exactly, the system fails. What if the patient has "mild fever"? The rule says "fever", not "mild fever."
- **Cannot learn from data**: rules must be hand-written by human experts
- **Rule conflicts**: what if Rule 5 says "prescribe drug A" and Rule 6 says "prescribe drug B"? You need a conflict resolution strategy.

---

## 🧠 Feynman Draft — Part 6: Knowledge Graphs

### Semantic Networks that graduated and got a job at Google

A Knowledge Graph is essentially a Semantic Network that has been **standardized and scaled up massively**. The key innovation is using a fixed format for every fact: the **RDF triple**.

Every piece of knowledge in a KG is stored as:

```
(Subject, Predicate, Object)
```

Examples:

```
(Einstein,   bornIn,      Germany)
(Einstein,   is-a,        Physicist)
(Germany,    locatedIn,   Europe)
(Einstein,   wonAward,    NobelPrize)
(NobelPrize, awardedIn,   1921)
```

That is it. Every fact in the entire knowledge graph — whether it is about physics, geography, history, or medicine — uses this same three-part structure. This standardization is what makes KGs interoperable and scalable to billions of facts.

### Real-world knowledge graphs

- **Google Knowledge Graph**: powers those info boxes when you search for a person or place
- **Wikidata**: open-source KG with over 100 million items
- **DBpedia**: structured data extracted from Wikipedia

### Semantic Network vs Knowledge Graph

Students often confuse these. Here is the key distinction:

| Aspect | Semantic Network | Knowledge Graph |
|---|---|---|
| **Scale** | Small to medium (dozens to hundreds of nodes) | Massive (millions to billions of triples) |
| **Standardization** | No universal format for edges | Standardized: RDF / OWL standards |
| **Inference** | Graph traversal only | Embeddings (TransE, etc.) + traversal |
| **Uncertainty** | Not supported | Partially supported (confidence scores) |
| **Querying** | Ad hoc traversal | SPARQL query language |
| **Use case** | Academic examples, small expert systems | Google Search, Watson, Wikidata |
| **Era** | 1960s–1980s AI research | 2010s–present industry applications |
| **Exam Tip** | Know the structure (nodes + labeled edges) | Know the triple format (h, r, t) and TransE |

The detailed coverage of KG embeddings (TransE, TransR) and link prediction is in the [Knowledge Graphs chapter](./D_knowledge_graphs.md).

---

## 🧠 Feynman Draft — Part 7: Ontologies

### The rule book for your knowledge graph

Imagine you run a hospital database. You have a knowledge graph full of facts:

```
(Aspirin, treats, Headache)
(Penicillin, treats, Infection)
(Dr. Smith, treats, Headache)    ← WAIT. This is wrong!
```

"Dr. Smith treats Headache" uses the same "treats" relationship, but Dr. Smith is a person, not a medicine. The knowledge graph does not know this is invalid because it has no rules about what **types** of things can be connected by "treats."

This is where **Ontologies** come in.

An ontology is a formal description of:
1. **Concepts** (classes): Medicine, Disease, Doctor, Patient
2. **Relationships**: treats, diagnoses, prescribes
3. **Constraints** (rules about what is valid):
   - ONLY things of type "Medicine" can "treat" things of type "Disease"
   - ONLY things of type "Doctor" can "diagnose" things of type "Disease"
   - A "Patient" cannot "prescribe" a "Medicine"

With an ontology in place, the system would **reject** the triple (Dr. Smith, treats, Headache) because Dr. Smith is a Doctor, not a Medicine, and the ontology says only Medicines can treat Diseases.

### Knowledge Graph + Ontology = powerful reasoning

Think of it this way:

| Component | Role | Analogy |
|---|---|---|
| **Knowledge Graph** | Stores facts | The actual data in a spreadsheet |
| **Ontology** | Defines rules and schema | The column headers and validation rules |
| **Together** | Facts + rules = reasoning | A well-designed database with constraints |

The ontology tells you **what kinds of knowledge are valid**. The knowledge graph stores **specific instances of that knowledge**. Together, they enable powerful reasoning:

- **Consistency checking**: "Is this new fact valid according to the ontology?"
- **Classification**: "What type of entity is X, given its properties?"
- **Inference**: "If X is a type of Medicine and treats Disease Y, what else can we infer?"

### Ontology vs Knowledge Graph — the exam distinction

| Aspect | Knowledge Graph | Ontology |
|---|---|---|
| **Contains** | Specific facts about the world | Rules about what facts are valid |
| **Example** | (Aspirin, treats, Headache) | "Only Medicines can treat Diseases" |
| **Analogy** | Data rows in a database | Schema + constraints of the database |
| **Purpose** | Store and retrieve facts | Define structure and validate facts |
| **Language** | RDF triples | OWL (Web Ontology Language) |

⚠️ **Common Misconception:** Students often treat "ontology" and "knowledge graph" as synonyms. They are not. A KG stores facts; an ontology defines the rules and structure those facts must follow. An ontology without a KG is an empty schema. A KG without an ontology is an unvalidated pile of triples.

---

## 🧠 Feynman Draft — Part 8: Structured vs Unstructured Knowledge

### Not all knowledge comes in neat boxes

So far, every KR method we have discussed produces **structured knowledge** — organized, machine-readable, directly queryable. But most of the world's knowledge is **unstructured**.

| Aspect | Structured Knowledge | Unstructured Knowledge |
|---|---|---|
| **Format** | Tables, graphs, triples, frames | Free text, images, audio, video |
| **Examples** | KGs, databases, ontologies, rule bases | Wikipedia articles, medical textbooks, X-rays |
| **Machine readability** | High — directly queryable | Low — requires NLP, CV, or speech processing |
| **Expressiveness** | Limited to the schema | Unlimited — natural language can express anything |
| **Reasoning** | Direct logical inference | Must extract structure first, then reason |
| **Volume** | Small fraction of world knowledge | Vast majority of world knowledge |

The key insight: **most of the world's knowledge is unstructured**, but AI reasoning systems need structured knowledge. This is why fields like NLP (extracting facts from text) and Computer Vision (extracting facts from images) are so important — they convert unstructured knowledge into structured form.

### Example: building a medical KG from text

1. **Unstructured**: "Aspirin is commonly used to treat headaches and reduce inflammation."
2. **NLP extraction**: identifies entities (Aspirin, headaches, inflammation) and relationships (treats, reduces)
3. **Structured triples**: (Aspirin, treats, Headache), (Aspirin, reduces, Inflammation)

This pipeline — from unstructured text to structured KG — is an active research area and a common exam topic when discussing KG construction.

---

## 📐 Formal Definitions

### Semantic Network

A directed labeled graph \\( G = (V, E) \\) where:
- \\( V \\) = set of concept nodes
- \\( E \subseteq V \times L \times V \\) = set of labeled directed edges
- \\( L \\) = set of relationship labels (e.g., is-a, has-property)

### Frame

A structured record \\( F = \\{(s_1, v_1), (s_2, v_2), \ldots, (s_n, v_n)\\} \\) where:
- \\( s_i \\) = slot name (attribute)
- \\( v_i \\) = filler value (which may be a default)
- Frames can inherit slots from parent frames via an **is-a** link.

### Knowledge Graph Triple

An RDF triple \\( (h, r, t) \\) where:
- \\( h \\) = head entity (subject)
- \\( r \\) = relation (predicate)
- \\( t \\) = tail entity (object)

### Ontology (formal)

An ontology \\( O = (C, R, A) \\) where:
- \\( C \\) = set of classes (concepts)
- \\( R \\) = set of relations between classes
- \\( A \\) = set of axioms (constraints and rules governing valid relationships)

---

## ⚖️ Trade-offs & Comparisons

### Master Comparison Table: All KR Methods

| Method | Representation | Expressiveness | Scalability | Interpretability | Uncertainty | Best For |
|---|---|---|---|---|---|---|
| **Symbolic Logic** | FOL formulas | High | Low | High | None | Precise, small domains |
| **Semantic Network** | Labeled graph | Medium | Low-Medium | High | None | Taxonomies, hierarchies |
| **Frame** | Slot-filler records | Medium | Medium | High | None | Stereotyped concepts |
| **Rule-Based** | IF-THEN rules | Medium | Low | Very High | None (basic) | Expert systems, diagnosis |
| **Knowledge Graph** | RDF triples | Medium-High | Very High | Medium | Partial | Large-scale fact storage |
| **Ontology** | Classes + axioms | High | Medium | Medium | None | Schema definition, validation |

### When to Use Which Method

| Scenario | Best Method | Why |
|---|---|---|
| Medical diagnosis system | Rule-Based + Ontology | Clear rules, need explainability |
| Web-scale fact search (Google) | Knowledge Graph | Billions of facts, needs scale |
| Animal taxonomy for a textbook | Semantic Network | Simple hierarchy, visual |
| Hotel booking system | Frames | Structured records with defaults |
| Legal reasoning | Symbolic Logic | Precise, formal, no ambiguity |
| Product recommendation | Knowledge Graph | Connects users, products, attributes at scale |

---

## 🏗️ Design Question Answer Framework

> "Compare two KR methods and discuss when each is appropriate."

**WHAT:** Define both methods clearly (1-2 sentences each). State the representation format.

**WHY:** Explain why multiple KR methods exist — different knowledge types need different containers. No single method satisfies all five requirements perfectly.

**HOW:** Describe how each method stores and retrieves knowledge (graph traversal, slot lookup, rule firing, SPARQL query).

**TRADE-OFF:** Use a comparison table covering expressiveness, scalability, interpretability, and uncertainty handling.

**EXAMPLE:** Give a concrete scenario for each.
- Symbolic Logic: encoding traffic laws for autonomous vehicles
- Semantic Network: representing an animal taxonomy
- Frame: representing a hotel booking system
- Rule-Based: medical diagnosis (MYCIN)
- Knowledge Graph: Google's search knowledge panel
- Ontology: defining valid relationships in a medical database

---

## 📝 Past Paper Connections

KR methods are rarely asked as standalone questions, but they appear as **background knowledge** in:

1. **KG questions** — "What is a Knowledge Graph?" requires understanding that it evolved from Semantic Networks *(see [Knowledge Graphs chapter](./D_knowledge_graphs.md))*
2. **Expert System questions** — "Explain how MYCIN works" requires understanding Rule-Based Systems and forward/backward chaining *(see [Expert Systems chapter](./E_mycin.md))*
3. **Comparison questions** — "Compare Semantic Networks and Knowledge Graphs" *(Lec 5)*
4. **Ontology questions** — "What is the role of an ontology in a knowledge-based system?"

---

## 🌐 English Expression Tips

### Describing KR methods

- "Knowledge Representation refers to the methods used to store, retrieve, and handle knowledge for intelligent reasoning."
- "A Semantic Network represents knowledge as a graph, where nodes correspond to concepts and edges represent relationships."
- "Frames are structured representations that use slot-filler pairs, similar to classes in object-oriented programming."
- "An ontology defines the types of entities, their relationships, and the constraints governing those relationships."

### Comparing methods

- "While Semantic Networks represent knowledge graphically, Frames use a more structured, template-based approach."
- "The fundamental difference between a Semantic Network and a Knowledge Graph lies in scale and standardization."
- "Rule-Based Systems excel in domains with well-defined logic, whereas Knowledge Graphs are better suited for large-scale fact storage."
- "Unlike a Knowledge Graph, which stores specific facts, an ontology defines the rules and constraints that those facts must follow."

### Explaining forward and backward chaining

- "Forward chaining is a data-driven approach: it starts with known facts and applies rules to derive new conclusions."
- "Backward chaining is goal-driven: it starts with a hypothesis and works backward to find supporting evidence."
- "The choice between forward and backward chaining depends on whether the task is exploratory (forward) or diagnostic (backward)."

### Commonly confused terms

| Confused Pair | Distinction |
|---|---|
| Semantic Network vs Knowledge Graph | KG = standardized (RDF triples) + large scale; SN = informal graph, small scale |
| Frame vs Ontology | Frame = data structure for one concept; Ontology = formal schema for an entire domain |
| Rule vs Implication | Rule = IF-THEN in a system; Implication = logical connective (→) in propositional logic |
| Knowledge Graph vs Ontology | KG = stores facts (data); Ontology = defines rules/schema (structure) |
| Forward vs Backward Chaining | Forward = data → conclusions; Backward = goal → evidence |

---

## 📝 Practice Problems

### Problem 1: Choosing the right KR method

**Question:** Which KR method would be best for a medical diagnosis system that needs to explain its reasoning to doctors? Justify your choice with reference to the five KR requirements. (5 marks)

**Answer Framework:**

The best choice is a **Rule-Based System**, potentially combined with an **Ontology**.

- **Expressiveness**: IF-THEN rules can capture diagnostic logic ("IF fever AND cough AND duration > 7 days THEN suspect pneumonia"). An ontology ensures only valid medical relationships are used.
- **Interpretability**: This is the critical requirement. Doctors need to understand WHY the system made a diagnosis. Rule-based systems provide full transparency — you can trace exactly which rules fired. This is far superior to a black-box approach.
- **Modifiability**: Medical knowledge updates frequently (new diseases, new treatments). Rules can be added or modified individually without rewriting the entire system.
- **Computational Efficiency**: For a clinical setting, rule-based systems are fast enough — diagnosis does not require processing billions of facts.
- **Scalability**: This is the weakness. As the number of rules grows, the system becomes harder to manage. For a specialized domain (e.g., bacterial infections only, like MYCIN), this is acceptable.

**Why not other methods?**
- KG: great for storing medical facts but does not provide transparent reasoning chains
- Semantic Network: too informal for medical precision
- Pure symbolic logic: too rigid and hard for doctors to read/write

---

### Problem 2: Drawing a semantic network

**Question:** Draw a semantic network for the following facts: Dogs are mammals. Mammals are animals. Dogs have fur. Dogs can bark. Animals need food. What can you infer about dogs through property inheritance? (4 marks)

**Answer:**

```
         Animal ----has-property----> Needs-Food
            ^
            | is-a
            |
         Mammal
            ^
            | is-a
            |
           Dog ----has-property----> Fur
            |
            +------has-property----> Can-Bark
```

**Inferences through property inheritance:**
1. Dog **is-a** Mammal **is-a** Animal → Dog is an Animal (transitive is-a)
2. Animal **has-property** Needs-Food → Dog inherits Needs-Food

So without being told directly, the system can infer: **Dog needs food**.

---

### Problem 3: Knowledge Graph vs Ontology

**Question:** What is the difference between a Knowledge Graph and an Ontology? Give an example of each and explain how they work together. (4 marks)

**Answer Framework:**

A **Knowledge Graph** stores specific facts about the world as RDF triples:
- (Aspirin, treats, Headache)
- (Penicillin, treats, Infection)

An **Ontology** defines the rules and constraints governing what kinds of facts are valid:
- "Only entities of type Medicine can have a 'treats' relationship with entities of type Disease"
- "Medicine is a subclass of Substance"

**How they work together:**
- The ontology defines the **schema**: what types of entities exist and what relationships are allowed
- The KG stores the **data**: specific instances following that schema
- When a new triple is added, the ontology can **validate** it: (Dr. Smith, treats, Headache) would be rejected because Dr. Smith is a Doctor, not a Medicine

**Analogy:** The ontology is like the column headers and validation rules of a spreadsheet. The KG is the actual data in the rows.

---

### Problem 4: Property inheritance with exceptions

**Question:** Consider a semantic network where Bird has-property Can-Fly. Penguin is-a Bird. But penguins cannot fly. How would you handle this using (a) a semantic network and (b) a frame? Which approach handles it better? (4 marks)

**Answer Framework:**

**(a) Semantic Network approach:**

```
   Bird ----has-property----> Can-Fly
     ^
     | is-a
     |
  Penguin ----has-property----> Cannot-Fly   (contradicts inherited Can-Fly!)
```

Problem: the network now has a **contradiction**. Penguin inherits Can-Fly from Bird but also has its own Cannot-Fly. The semantic network has no built-in mechanism to resolve this conflict. You would need an additional rule like "local properties override inherited properties," but this is not part of the standard semantic network formalism.

**(b) Frame approach:**

```
Frame: Bird
  Slot: can-fly     Filler: True (default)
  Slot: has-wings   Filler: True
  Slot: legs        Filler: 2

Frame: Penguin (inherits from Bird)
  Slot: can-fly     Filler: False    ← cleanly overrides the default
  Slot: habitat     Filler: Antarctic
```

The frame approach handles this **much more cleanly**. Default values can be overridden in child frames, just like method overriding in OOP. There is no contradiction — the local value simply takes precedence over the inherited default.

**Conclusion:** Frames handle exceptions better than semantic networks because they have a built-in mechanism for default values with overrides.

---

### Problem 5: Forward vs Backward Chaining

**Question:** Given the following rules and facts, show how forward chaining and backward chaining would each reach a conclusion. (4 marks)

```
Rules:
R1: IF fever AND cough THEN flu
R2: IF flu AND bodyache THEN severe-flu
R3: IF severe-flu THEN hospitalize

Facts: {fever, cough, bodyache}
```

**Forward Chaining (data → conclusions):**

```
Start: {fever, cough, bodyache}
Step 1: R1 matches (fever ∧ cough) → add flu       → {fever, cough, bodyache, flu}
Step 2: R2 matches (flu ∧ bodyache) → add severe-flu → {fever, cough, bodyache, flu, severe-flu}
Step 3: R3 matches (severe-flu) → add hospitalize    → {fever, cough, bodyache, flu, severe-flu, hospitalize}
Step 4: No more rules match → DONE
```

**Backward Chaining (goal → evidence):**

```
Goal: Should we hospitalize?
Step 1: R3 says hospitalize requires severe-flu → Sub-goal: prove severe-flu
Step 2: R2 says severe-flu requires flu AND bodyache → Sub-goals: prove flu, prove bodyache
Step 3: R1 says flu requires fever AND cough → Sub-goals: prove fever, prove cough
Step 4: fever ∈ Facts ✓, cough ∈ Facts ✓ → flu PROVED
Step 5: bodyache ∈ Facts ✓ → severe-flu PROVED
Step 6: → hospitalize PROVED ✓
```

Both approaches reach the same conclusion, but forward chaining explores all derivable facts while backward chaining is more focused — it only checks what is needed for the specific goal.

---

## ✅ Self-Check Checklist

- [ ] Can you name and briefly define all six KR methods (logic, semantic networks, frames, rules, KGs, ontologies)?
- [ ] Can you draw a semantic network with is-a and has-property edges?
- [ ] Can you explain property inheritance with a concrete example?
- [ ] Can you describe a frame with slots, fillers, and default values?
- [ ] Can you list the five requirements for a good KR system?
- [ ] Can you explain forward chaining vs backward chaining with an example?
- [ ] Can you state the key difference between a Knowledge Graph and an Ontology?
- [ ] Can you explain why semantic networks struggle with exceptions (the penguin problem)?
- [ ] Can you explain what structured vs unstructured knowledge means?
- [ ] Can you write all of the above in English under exam conditions?

---

⚠️ **Common Misconception:** Students often think Semantic Networks and Knowledge Graphs are the same thing. They share the graph structure, but KGs use **standardized triple format (RDF)**, operate at **much larger scale**, and support **embedding-based reasoning** (TransE, etc.) — none of which traditional Semantic Networks do.

⚠️ **Common Misconception:** Students often conflate Knowledge Graphs and Ontologies. Remember: a KG stores **facts** (data), while an ontology defines **rules and constraints** (schema). They complement each other but serve different purposes.

💡 **Core Intuition:** Knowledge Representation is the art of choosing the right container for knowledge. Logic gives precision, networks give intuition, frames give structure, rules give transparency, KGs give scale, and ontologies give validation. No single method does everything — real systems combine multiple approaches.
