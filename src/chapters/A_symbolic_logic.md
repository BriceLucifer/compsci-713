# Symbolic Logic -- Propositional & First-Order Logic

## 🎯 Exam Importance

🔴 **GUARANTEED TO APPEAR** | Every single test paper has a logic question as Q1

| Test Paper | Question | Marks | Sub-topics |
|-----------|----------|-------|------------|
| S1 2025 Sample Test | Q1 (3 marks / 15 total = 20%) | 1(a) Modus Tollens + De Morgan's on $(I \wedge F) \rightarrow E$; 1(b) FOL translation $\neg\forall x\, \text{Fly}(x)$ + example |
| S1 2025 Actual Test | Q1 (2 marks / 15 total = 13%) | 1(a) Modus Tollens + De Morgan's on $(P \vee Q) \rightarrow R$; 1(b) FOL Modus Tollens with $\forall x(\text{Cheat}(x) \rightarrow \text{Disqualified}(x))$ |
| S1 2026 Sample Test | Q1 (5 marks / 20 total = 25%) | 1(a) Same $(I \wedge F) \rightarrow E$ but **requires full truth table** (3 marks); 1(b) Same FOL $\neg\forall x\, \text{Fly}(x)$ |

**Key observation:** The question has been worth 2--5 marks across papers, and the 2026 sample *tripled* the propositional logic marks by requiring a full truth table. Prepare for both approaches (algebraic deduction AND truth table verification).

---

## 📖 Core Concepts (Quick Reference Table)

| English Term | 中文 | One-line Definition |
|-------------|------|-------------------|
| Propositional Logic（命题逻辑） | 命题逻辑 | Deals with statements that are TRUE or FALSE, combined with logical connectives |
| First-Order Logic / FOL（一阶逻辑） | 一阶逻辑 | Extends propositional logic with variables, quantifiers ($\forall$, $\exists$), predicates, and functions |
| Atomic Proposition（原子命题） | 原子命题 | A basic statement with binary value: true or false (e.g., "It is raining") |
| Connective（逻辑联结词） | 联结词 | Operators: $\neg$ (NOT), $\wedge$ (AND), $\vee$ (OR), $\rightarrow$ (IMPLIES), $\leftrightarrow$ (IFF) |
| Interpretation（解释/赋值） | 解释 | A function $\pi$ that assigns true/false to every atomic proposition |
| Tautology（重言式） | 重言式 | A formula that is true under every possible interpretation |
| Logical Implication（逻辑蕴含） | 逻辑蕴含 | $A \Rightarrow B$: for every interpretation where A is true, B must also be true |
| Logical Equivalence（逻辑等值） | 逻辑等值 | $A \Leftrightarrow B$: A and B have the same truth value under every interpretation |
| Modus Ponens（肯定前件） | 肯定前件 | From $P$ and $P \rightarrow Q$, conclude $Q$ |
| Modus Tollens（否定后件） | 否定后件 | From $P \rightarrow Q$ and $\neg Q$, conclude $\neg P$ |
| Syllogism（三段论） | 三段论 | From $(A \rightarrow B)$ and $(B \rightarrow C)$, conclude $(A \rightarrow C)$ |
| Material Implication（实质蕴含） | 实质蕴含 | $A \rightarrow B$ is false ONLY when A is true and B is false |
| Vacuous Truth（空真） | 空真 | When the premise is false, implication is always true |
| De Morgan's Laws（德摩根定律） | 德摩根律 | $\neg(A \wedge B) \equiv \neg A \vee \neg B$ and $\neg(A \vee B) \equiv \neg A \wedge \neg B$ |
| Universal Quantifier（全称量词） | 全称量词 | $\forall x$: "for all x in the domain" |
| Existential Quantifier（存在量词） | 存在量词 | $\exists x$: "there exists at least one x" |
| Bound Variable（约束变量） | 约束变量 | A variable within the scope of a quantifier ($\forall x$ or $\exists x$) |
| Free Variable（自由变量） | 自由变量 | A variable NOT within any quantifier's scope |
| Sentence（语句） | 语句 | A formula with NO free variables |
| Signature（签名） | 签名 | The vocabulary of a FOL language: its relation and function symbols |
| Domain（论域） | 论域 | The set of objects that variables range over in a FOL interpretation |

---

## 🧠 Feynman Draft -- Learning From Scratch

### Part 1: Propositional Logic

Imagine you are a security guard at a building entrance. Your job manual has simple rules written as "if... then..." statements. Each fact is either TRUE or FALSE -- no grey areas, no "maybe." Your entire job is to follow the rules and figure out what must be true.

For example, your manual says:

> "If the person has a valid ID **and** their fingerprint matches, then grant entry."

In symbols: $(I \wedge F) \rightarrow E$

Now, suppose today the person was **denied entry** ($\neg E$). What can you figure out?

Think of it this way: the rule promises that having both ID and fingerprint match **guarantees** entry. The person was NOT granted entry. So the guarantee must not have kicked in -- meaning they did NOT have both. Either no valid ID, or no fingerprint match, or both were missing.

This reasoning is called **Modus Tollens（否定后件）**: if the consequence didn't happen, the premise couldn't have been fully satisfied.

$$P \rightarrow Q, \quad \neg Q \quad \Longrightarrow \quad \neg P$$

**But wait -- what does "not both" mean precisely?**

$\neg(I \wedge F)$ means "it's not the case that BOTH are true." By **De Morgan's Law**, this equals $\neg I \vee \neg F$ -- "at least one of them is false."

This is exactly how every exam question on this topic works. Every. Single. One.

### Part 2: The Implication Trap

Here is the single most confusing thing in propositional logic, and the lecture opens with it:

> "If it rains today, I will bring an umbrella." ($P \rightarrow Q$)
>
> You see the person carrying an umbrella ($Q$ is true). Can you conclude it is raining ($P$)?

**NO!** $Q \rightarrow P$ is NOT the same as $P \rightarrow Q$. The person might just like carrying umbrellas. This mistake is called **Affirming the Consequent（肯定后件谬误）** -- the lecture slide 4-5 opens with exactly this example.

Here is the full truth table for implication:

| $P$ | $Q$ | $P \rightarrow Q$ |
|-----|-----|------------------|
| T | T | **T** |
| T | F | **F** $\leftarrow$ the ONLY row where it's false |
| F | T | **T** $\leftarrow$ vacuous truth |
| F | F | **T** $\leftarrow$ vacuous truth |

The key insight: **$P \rightarrow Q$ is false ONLY when P is true and Q is false.**

Why is $\text{false} \rightarrow \text{anything}$ true? Think of it as a promise: "If it rains, I'll bring an umbrella." If it doesn't rain, I haven't broken my promise regardless of whether I carry an umbrella. The promise is only broken when rain happens and no umbrella appears.

> ⚠️ **Common Misconception**: Students think $P \rightarrow Q$ means "P causes Q" or "P and Q are related." It does NOT. Material implication is purely about truth values. "If pigs fly, then I am the Queen of England" is technically TRUE because the premise is false. This is called **vacuous truth（空真）**.

### Part 3: First-Order Logic

Propositional logic treats facts as indivisible boxes -- "it is raining" is one atomic unit. But what if you need to say something about *many* things at once?

Imagine you are a biologist studying birds. You want to express: "Not all birds in this region can fly." In propositional logic, you would need a separate proposition for each bird -- $\text{Fly}(\text{robin})$, $\text{Fly}(\text{kiwi})$, $\text{Fly}(\text{penguin})$, etc. If you have 1000 birds, you need 1000 propositions. This is the **verbosity problem（冗余问题）**.

First-order logic fixes this by introducing:
- **Objects**: things in your world (birds, people, squares in Wumpus World)
- **Predicates** (relations): properties of objects ($\text{Fly}(x)$, $\text{Pit}(x,y)$)
- **Functions**: mappings from objects to objects ($\text{left}(x,y)$, $\text{fatherOf}(x)$)
- **Quantifiers**: $\forall$ ("for all") and $\exists$ ("there exists")

So "Not all birds can fly" becomes simply: $\neg \forall x\, \text{Fly}(x)$

Which is equivalent to: $\exists x\, \neg\text{Fly}(x)$ -- "there exists a bird that cannot fly."

> ⚠️ **Common Misconception**: Students write $\forall x\, \neg\text{Fly}(x)$ for "not all birds fly." This is WRONG -- it means "NO bird can fly" (way too strong). The negation must go OUTSIDE the quantifier: $\neg\forall x\, \text{Fly}(x)$.

> ⚠️ **Common Misconception**: With $\forall$, use $\rightarrow$ (implication) not $\wedge$. "Every student cheats" is $\forall x (\text{Student}(x) \rightarrow \text{Cheat}(x))$, NOT $\forall x (\text{Student}(x) \wedge \text{Cheat}(x))$. The latter says "everything is both a student AND a cheater" -- it claims your dog is a cheating student!

> 💡 **Core Intuition**: Propositional logic is about combining true/false statements with connectives; FOL adds the power to talk about "all" and "some" objects in a domain using quantifiers and predicates.

---

## 📐 Formal Definitions

### Propositional Logic -- Complete Syntax and Semantics

**Syntax (from lecture slide 15):**

- **Atomic propositions** (atoms): $\text{Atom} = \{X_1, \ldots, X_k\}$, each with domain $\{\text{true}, \text{false}\}$ (or $\{0, 1\}$).
- **Compound propositions** are built using connectives:
  $\neg A$, $(A \vee B)$, $(A \wedge B)$, $(A \rightarrow B)$, $(A \leftarrow B)$, $(A \leftrightarrow B)$

**Semantics:**

An **interpretation** $\pi : \text{Atom} \rightarrow \{\text{true}, \text{false}\}$ assigns truth values to all atoms. The truth value of any compound proposition is determined by the following table:

### Master Truth Table (MEMORIZE THIS)

| $A$ | $B$ | $\neg A$ | $A \wedge B$ | $A \vee B$ | $A \rightarrow B$ | $A \leftarrow B$ | $A \leftrightarrow B$ |
|-----|-----|---------|-------------|-----------|------------------|------------------|---------------------|
| T | T | F | T | T | **T** | T | T |
| T | F | F | F | T | **F** | T | F |
| F | T | T | F | T | **T** | F | F |
| F | F | T | F | F | **T** | T | T |

Key observations:
- $A \rightarrow B$ is false ONLY in row 2 (A true, B false)
- $A \leftrightarrow B$ is true when A and B have the SAME value
- $A \leftarrow B$ is the "reverse implication" ($B \rightarrow A$)

### Complete Logical Equivalence Laws (from lecture slide 22)

**These are your tools for algebraic manipulation. The exam requires you to cite which law you use.**

| Law Name | Equivalence |
|----------|------------|
| **Double Negation** | $\neg\neg A \Leftrightarrow A$ |
| **Commutative** | $(A \wedge B) \Leftrightarrow (B \wedge A)$; $(A \vee B) \Leftrightarrow (B \vee A)$ |
| **Associative** | $(A \wedge (B \wedge C)) \Leftrightarrow ((A \wedge B) \wedge C)$; same for $\vee$ |
| **Distributive** | $(A \wedge (B \vee C)) \Leftrightarrow ((A \wedge B) \vee (A \wedge C))$; $(A \vee (B \wedge C)) \Leftrightarrow ((A \vee B) \wedge (A \vee C))$ |
| **Idempotent** | $(A \wedge A) \Leftrightarrow A$; $(A \vee A) \Leftrightarrow A$ |
| **De Morgan's** | $\neg(A \wedge B) \Leftrightarrow (\neg A \vee \neg B)$; $\neg(A \vee B) \Leftrightarrow (\neg A \wedge \neg B)$ |
| **Implication** | $(A \rightarrow B) \Leftrightarrow (\neg A \vee B)$; $(A \rightarrow B) \Leftrightarrow (\neg A \wedge \neg B) \vee B$ ... simplified: $\neg A \vee B$ |
| **Contrapositive** | $(A \rightarrow B) \Leftrightarrow (\neg B \rightarrow \neg A)$ |
| **Contradiction** | $(A \vee (B \wedge \neg B)) \Leftrightarrow A$ |
| **Absorption** | $A \Leftrightarrow (A \wedge (A \vee B))$; $A \Leftrightarrow (A \vee (A \wedge B))$ |
| **Equivalence** | $(A \leftrightarrow B) \Leftrightarrow ((A \rightarrow B) \wedge (B \rightarrow A))$; $(A \leftrightarrow B) \Leftrightarrow ((A \wedge B) \vee (\neg A \wedge \neg B))$ |

### Logical Implication vs. Material Implication

This distinction is subtle and important (lecture slide 21):

- **Material implication** ($A \rightarrow B$): a connective inside a formula. It has a truth value.
- **Logical implication** ($A \Rightarrow B$): a meta-statement about formulas. It means: for EVERY interpretation $\pi$, if $\pi(A) = \text{true}$ then $\pi(B) = \text{true}$.

**Verification methods:**
1. Truth table: check that every row where A is true also has B true
2. Equivalent test: $A \Rightarrow B$ if and only if $A \rightarrow B$ is a tautology

### Key Inference Rules (from lecture slide 21)

$$\text{Modus Ponens: } ((A \rightarrow B) \wedge A) \Rightarrow B$$

$$\text{Modus Tollens: } ((A \rightarrow B) \wedge \neg B) \Rightarrow \neg A$$

$$\text{Syllogism: } ((A \rightarrow B) \wedge (B \rightarrow C)) \Rightarrow (A \rightarrow C)$$

### First-Order Logic -- Complete Syntax and Semantics

**Three building blocks** (lecture slide 25):
1. **Objects**: people, houses, numbers, grid squares, ...
2. **Relations (Predicates)**: properties or relationships -- unary ($\text{Red}(x)$), binary ($\text{Adjacent}(x,y)$), n-ary
3. **Functions**: mappings that produce objects -- $\text{fatherOf}(x)$, $\text{left}(x,y)$

**Signature** (lecture slide 29): the vocabulary $S = \{R_1, \ldots, R_k, f_1, \ldots, f_\ell\}$ -- the set of relation and function symbols.

**Terms** (lecture slide 29):
- Every variable is a term: $x, y, z$
- Every constant is a term: $1, 2, \text{Alice}$ (a constant is a 0-ary function)
- If $f$ is a function of arity $r$ and $t_0, \ldots, t_{r-1}$ are terms, then $f(t_0, \ldots, t_{r-1})$ is a term
- A **ground term** has no variables (all constants/applied functions on constants)

**Formulas** (lecture slide 30):
- **Atomic**: $t_0 = t_1$ (equality) or $R(t_0, \ldots, t_{n-1})$ (predicate applied to terms)
- **Compound**: built from atomic formulas using $\neg, \wedge, \vee, \rightarrow, \leftrightarrow$ and quantifiers $\forall x, \exists x$

**Free vs. Bound Variables** (lecture slide 32):
- A variable $x$ is **bound** if it appears within $\forall x : \varphi$ or $\exists x : \varphi$
- A variable $x$ is **free** if it is not within any quantifier's scope
- A **sentence** is a formula with NO free variables

**Satisfaction Relation** (lecture slide 33): $I \vDash \varphi$ means interpretation $I$ satisfies formula $\varphi$:
- $I \vDash \forall x : \varphi$ iff for ALL $a \in D$, $I[x/a] \vDash \varphi$
- $I \vDash \exists x : \varphi$ iff there is SOME $a \in D$ such that $I[x/a] \vDash \varphi$

### Quantifier Negation Laws (De Morgan's for Quantifiers)

$$\neg \forall x\, \varphi(x) \equiv \exists x\, \neg\varphi(x)$$
$$\neg \exists x\, \varphi(x) \equiv \forall x\, \neg\varphi(x)$$

Additional FOL equivalences (lecture slide 34):
$$\neg\neg\exists x : \varphi(x) \equiv \forall x : \neg\varphi(x) \quad [\text{Double negation + quantifier swap}]$$
$$\exists x : (\varphi_1(x) \vee \varphi_2(x)) \equiv (\exists x : \varphi_1(x)) \vee (\exists x : \varphi_2(x))$$
$$\forall x : (\varphi_1(x) \wedge \varphi_2(x)) \equiv (\forall x : \varphi_1(x)) \wedge (\forall x : \varphi_2(x))$$
$$\neg\forall x : (\varphi_1(x) \rightarrow \varphi_2(x)) \equiv \exists x : (\varphi_1(x) \wedge \neg\varphi_2(x))$$

---

## 🔄 Mechanisms & Derivations -- The Exam Algorithms

### Algorithm 1: Modus Tollens with De Morgan's (The Core Exam Pattern)

This is the algorithm you will execute in 100% of logic exam questions. Master it completely.

**Input:** A rule $P \rightarrow Q$ and an observation $\neg Q$

**Steps:**
1. **Identify the structure**: What is $P$? What is $Q$? (P is often compound, e.g., $I \wedge F$ or $P \vee Q$)
2. **Apply Modus Tollens**: From $P \rightarrow Q$ and $\neg Q$, conclude $\neg P$
3. **Simplify $\neg P$** using De Morgan's Law:
   - If $P = (A \wedge B)$: $\neg(A \wedge B) = \neg A \vee \neg B$ ("at least one is false")
   - If $P = (A \vee B)$: $\neg(A \vee B) = \neg A \wedge \neg B$ ("BOTH are false")
4. **State the conclusion in natural language**

### Algorithm 2: Truth Table Verification (Required in S1 2026 Sample)

The 2026 sample test explicitly asks "Show your steps (Truth Table) clearly" for 3 marks. Here is the exact procedure:

**Step 1:** Write the truth table for $X \rightarrow E$ where $X = I \wedge F$ (1 mark):

| $X$ ($I \wedge F$) | $E$ | $X \rightarrow E$ |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | **0** $\leftarrow$ violates the rule |
| 1 | 1 | 1 |

**Step 2:** Since $\neg E$ (E = 0) and $X \rightarrow E$ must be true, look at rows where E = 0. Only row 1 satisfies both conditions. Therefore $X = I \wedge F = 0$ (1 mark).

**Step 3:** Write the truth table for $I \wedge F$ to determine what $I \wedge F = 0$ means (1 mark):

| $I$ | $F$ | $I \wedge F$ |
|---|---|---|
| 0 | 0 | 0 ✓ |
| 0 | 1 | 0 ✓ |
| 1 | 0 | 0 ✓ |
| 1 | 1 | 1 ✗ |

**Conclusion:** At least one of I, F must be 0. The person either didn't have valid ID, or fingerprint didn't match (or both).

### Algorithm 3: FOL Translation

**Input:** An English sentence

**Steps:**
1. **Identify the domain**: What set of objects are we talking about?
2. **Define predicates**: What properties/relations are relevant?
3. **Identify the quantifier**: "all"/"every" $\rightarrow$ $\forall$; "some"/"exists"/"not all" $\rightarrow$ involves $\exists$
4. **Construct the formula**:
   - "Every X that has property A also has property B" $\rightarrow$ $\forall x\, (A(x) \rightarrow B(x))$
   - "Not all X have property A" $\rightarrow$ $\neg\forall x\, A(x)$ or equivalently $\exists x\, \neg A(x)$
   - "Some X has property A" $\rightarrow$ $\exists x\, A(x)$
5. **Verify**: Read the formula back in English to check

### Algorithm 4: FOL Modus Tollens (S1 2025 Actual Test Pattern)

**Input:** A universal rule $\forall x\, (P(x) \rightarrow Q(x))$ and a fact $\neg Q(a)$ for a specific object $a$

**Steps:**
1. **Universal Instantiation**: From $\forall x\, (P(x) \rightarrow Q(x))$, substitute $x = a$:
   $P(a) \rightarrow Q(a)$
2. **Apply Modus Tollens**: From $P(a) \rightarrow Q(a)$ and $\neg Q(a)$, conclude $\neg P(a)$
3. **State conclusion**: Object $a$ does not have property P

---

## ⚖️ Trade-offs & Comparisons

### Propositional Logic vs First-Order Logic

| Aspect | Propositional Logic | First-Order Logic |
|--------|-------------------|------------------|
| **Building blocks** | Atomic propositions (P, Q, R) | Objects, predicates, functions, quantifiers |
| **Expressiveness** | LOW -- can't say "for all" or "there exists" | HIGH -- quantifiers over objects |
| **Decidability** | Always decidable (finite truth table) | Semi-decidable (may not terminate) |
| **Verbosity** | HIGH for real-world domains (need one prop per fact) | LOW -- one formula can express rules about all objects |
| **Use in AI** | Simple rule engines, circuit design, Wumpus World basics | Knowledge bases, expert systems, theorem proving |
| **Example** | $(I \wedge F) \rightarrow E$ | $\forall x\, (\text{Student}(x) \rightarrow \text{HasExam}(x))$ |

### Modus Ponens vs Modus Tollens vs Converse Error

| | Modus Ponens | Modus Tollens | Converse Error (INVALID!) |
|---|---|---|---|
| **Given** | $P \rightarrow Q$ and $P$ | $P \rightarrow Q$ and $\neg Q$ | $P \rightarrow Q$ and $Q$ |
| **Conclude** | $Q$ ✅ | $\neg P$ ✅ | $P$ ❌ WRONG |
| **Direction** | Forward reasoning | Backward reasoning | Fallacy |
| **Example** | Rain $\rightarrow$ Wet. Rain. $\therefore$ Wet. | Rain $\rightarrow$ Wet. Not wet. $\therefore$ Not rain. | Rain $\rightarrow$ Wet. Wet. $\therefore$ Rain?? (sprinkler!) |
| **Exam status** | Not directly tested | Tested EVERY exam | Tested as motivation (lecture slide 4-5) |

### De Morgan's: $\wedge$ vs $\vee$ Negation

| Original | Negated | Result | Intuition |
|----------|---------|--------|-----------|
| $A \wedge B$ (both true) | $\neg(A \wedge B)$ | $\neg A \vee \neg B$ (at least one false) | Breaking an AND gives OR |
| $A \vee B$ (at least one true) | $\neg(A \vee B)$ | $\neg A \wedge \neg B$ (both false) | Breaking an OR gives AND |

> **Memory trick**: negation "flips" the connective ($\wedge \leftrightarrow \vee$) and negates each operand.

### $\forall$ with $\rightarrow$ vs $\exists$ with $\wedge$ (Critical FOL Pattern)

| Statement | Correct FOL | Common WRONG Version | Why wrong |
|-----------|------------|---------------------|-----------|
| "Every student is enrolled" | $\forall x\, (\text{Student}(x) \rightarrow \text{Enrolled}(x))$ | $\forall x\, (\text{Student}(x) \wedge \text{Enrolled}(x))$ | Claims everything in domain is both a student AND enrolled |
| "Some student is happy" | $\exists x\, (\text{Student}(x) \wedge \text{Happy}(x))$ | $\exists x\, (\text{Student}(x) \rightarrow \text{Happy}(x))$ | Vacuously true for any non-student object |

> **Rule of thumb**: $\forall$ pairs with $\rightarrow$; $\exists$ pairs with $\wedge$.

---

## 🏗️ Design Question Framework

If asked to model a scenario using symbolic logic:

**WHAT**: Define the propositions/predicates and their English meanings
- List each atomic proposition or predicate with a clear one-line definition
- Specify the domain for FOL

**WHY**: Why use formal logic here?
- Precise and unambiguous (unlike natural language)
- Machine-verifiable (automated reasoning)
- Supports inference: derive new facts from existing rules

**HOW**: Write the rules as logical formulas
- Express each rule using connectives and quantifiers
- Show at least one inference step (Modus Ponens or Modus Tollens)

**TRADE-OFF**: Discuss limitations
- Propositional logic: verbose, can't express "for all"
- FOL: more expressive but semi-decidable
- Both: can't handle uncertainty (need fuzzy logic / LNN for soft values)

**EXAMPLE**: Demonstrate with a concrete instance
- Show a specific inference with your rules

---

## 📝 Exam Questions -- Complete Collection with Model Answers

### ===== EXAM Q1: S1 2025 Sample Test Q1(a) -- 1 mark =====

**Question:** In a secure facility, $(I \wedge F) \rightarrow E$. The person was not granted entry ($\neg E$). Deduce what must be true about I and F.

**Model Answer:**

> Given: $(I \wedge F) \rightarrow E$ and $\neg E$.
>
> By Modus Tollens: $\neg E \Rightarrow \neg(I \wedge F)$.
>
> By De Morgan's Law: $\neg(I \wedge F) \equiv \neg I \vee \neg F$.
>
> **Conclusion:** The person either did not have a valid ID ($\neg I$) or the fingerprint did not match ($\neg F$), or both.

**Marking note:** 1 mark for correct application of Modus Tollens + De Morgan's + stating conclusion.

---

### ===== EXAM Q2: S1 2025 Sample Test Q1(b)(i) -- 1 mark =====

**Question:** A biologist claims "Not all birds in this region can fly." Domain: all birds in the region. $\text{Fly}(x)$ = bird x can fly. Write in FOL.

**Model Answer:**

> $$\neg \forall x\, \text{Fly}(x)$$
>
> Equivalently: $\exists x\, \neg\text{Fly}(x)$

**Marking note:** Either form accepted for full mark.

---

### ===== EXAM Q3: S1 2025 Sample Test Q1(b)(ii) -- 1 mark =====

**Question:** Provide a realistic example (one sentence) that would make the statement true.

**Model Answer:**

> "There is a penguin in this region, and penguins cannot fly."

**Marking note:** Any concrete example naming a flightless bird (penguin, kiwi, ostrich, emu) is acceptable.

---

### ===== EXAM Q4: S1 2025 Actual Test Q1(a) -- 1 mark =====

**Question:** In a smart office, $(P \vee Q) \rightarrow R$. The alarm did not sound ($\neg R$). Deduce what must be true about P and Q.

Where: P = door is open, Q = motion sensor triggered, R = alarm sounds.

**Model Answer:**

> Given: $(P \vee Q) \rightarrow R$ and $\neg R$.
>
> By Modus Tollens: $\neg R \Rightarrow \neg(P \vee Q)$.
>
> By De Morgan's Law: $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$.
>
> **Conclusion:** The door was NOT open AND the motion sensor was NOT triggered. (Both must be false.)

**Critical difference from the sample test:** Here the premise uses $\vee$ (OR), so De Morgan's produces $\wedge$ (AND). The conclusion is STRONGER: BOTH P and Q must be false (not just "at least one").

| Premise Connective | After De Morgan's | Conclusion Strength |
|---|---|---|
| $A \wedge B$ (AND) | $\neg A \vee \neg B$ | At least one is false |
| $A \vee B$ (OR) | $\neg A \wedge \neg B$ | BOTH are false |

---

### ===== EXAM Q5: S1 2025 Actual Test Q1(b) -- 1 mark =====

**Question:** $\forall x\, (\text{Cheat}(x) \rightarrow \text{Disqualified}(x))$. Alice is not disqualified. Did Alice cheat?

**Model Answer:**

> From the universal rule: $\forall x\, (\text{Cheat}(x) \rightarrow \text{Disqualified}(x))$
>
> Instantiate for Alice: $\text{Cheat}(\text{Alice}) \rightarrow \text{Disqualified}(\text{Alice})$
>
> Given: $\neg\text{Disqualified}(\text{Alice})$
>
> By Modus Tollens: $\neg\text{Disqualified}(\text{Alice}) \Rightarrow \neg\text{Cheat}(\text{Alice})$
>
> **Conclusion:** Alice did not cheat.

**Key steps for marks:** (1) Universal instantiation, (2) Modus Tollens, (3) Conclusion in English.

---

### ===== EXAM Q6: S1 2026 Sample Test Q1(a) -- 3 marks =====

**Question:** SAME scenario as 2025 sample $(I \wedge F) \rightarrow E$, $\neg E$, but now **explicitly requires truth table** for 3 marks.

**Model Answer:**

> **Step 1 (1 mark):** Let $X = I \wedge F$. Truth table for $X \rightarrow E$:
>
> | $X$ ($I \wedge F$) | $E$ | $X \rightarrow E$ |
> |---|---|---|
> | 0 | 0 | 1 |
> | 0 | 1 | 1 |
> | 1 | 0 | 0 |
> | 1 | 1 | 1 |
>
> **Step 2 (1 mark):** Since $E = 0$ and $X \rightarrow E$ is true (given the rule holds), the only valid row is row 1 where $X = 0$. Therefore $I \wedge F = 0$.
>
> Truth table for $I \wedge F$:
>
> | $I$ | $F$ | $I \wedge F$ |
> |---|---|---|
> | 0 | 0 | 0 ✓ |
> | 0 | 1 | 0 ✓ |
> | 1 | 0 | 0 ✓ |
> | 1 | 1 | 1 ✗ |
>
> **Step 3 (1 mark):** Since $I \wedge F = 0$, at least one of $I$ or $F$ must be 0.
>
> **Conclusion:** The person either did not have a valid ID or the fingerprint did not match (or both).

---

### ===== EXAM Q7: S1 2026 Sample Test Q1(b) -- 2 marks =====

Identical to S1 2025 Sample Q1(b). Same answers apply:
- (i) $\neg\forall x\, \text{Fly}(x)$ [1 mark]
- (ii) "There is a penguin in this region, and penguins cannot fly." [1 mark]

---

### ===== LECTURE MOTIVATION QUESTION (potential exam question) =====

**Question (slide 4-5):** "If it rains, I bring an umbrella" ($P \rightarrow Q$). You see the person with an umbrella ($Q$). Can you conclude it is raining ($P$)?

**Answer:** No. $Q \rightarrow P$ (converse) is NOT logically equivalent to $P \rightarrow Q$. Seeing $Q$ true does not let us conclude $P$. This is the fallacy of **Affirming the Consequent**.

To conclude $P$, you would need $Q \rightarrow P$ (the converse) as a separate rule, or equivalently $P \leftrightarrow Q$ (biconditional).

---

## 🔬 Additional Practice Problems (Exam-Style)

### Practice 1: Combined Modus Tollens with Additional Information

**Given:** $(P \wedge A) \rightarrow C$; $\neg C$; $A$ is true.

**Question:** What can you conclude about P?

<details>
<summary>Click to see answer</summary>

Step 1: By Modus Tollens: $\neg C$ and $(P \wedge A) \rightarrow C$ gives $\neg(P \wedge A)$.

Step 2: $\neg(P \wedge A) = \neg P \vee \neg A$ (De Morgan's).

Step 3: Since $A$ is TRUE, $\neg A$ is FALSE.

Step 4: Therefore $\neg P \vee \text{FALSE} = \neg P$ must be TRUE.

**Conclusion:** $P$ is false. The student did NOT pass the exam.

</details>

### Practice 2: FOL Translation -- University Scenario

**Translate:** "Every computer science student at Auckland takes at least one math course."

**Domain setup:**
- $\text{CS}(x)$: x is a CS student
- $\text{Math}(y)$: y is a math course
- $\text{Takes}(x, y)$: student x takes course y

<details>
<summary>Click to see answer</summary>

$$\forall x\, [\text{CS}(x) \rightarrow \exists y\, (\text{Math}(y) \wedge \text{Takes}(x, y))]$$

Read back: "For all x, if x is a CS student, then there exists a y such that y is a math course and x takes y."

Note the nested quantifiers: $\forall$ outside, $\exists$ inside. The $\exists y$ is within the scope of $\forall x$.

</details>

### Practice 3: Identify the Fallacy

**Given:** $\forall x\, (\text{Student}(x) \rightarrow \text{Enrolled}(x, \text{Uni}))$. David is enrolled at Uni. Conclusion: David is a student.

<details>
<summary>Click to see answer</summary>

**This is INCORRECT.** This is Affirming the Consequent.

The rule says: Student $\rightarrow$ Enrolled. Being enrolled does not mean being a student. David could be enrolled as staff, auditor, etc.

To conclude David is a student, you would need the converse: $\text{Enrolled}(x, \text{Uni}) \rightarrow \text{Student}(x)$, which is a different (and not given) rule.

</details>

### Practice 4: FOL with Negated Quantifiers

**Translate:** "No robot in the warehouse is idle."

<details>
<summary>Click to see answer</summary>

**Option 1:** $\neg\exists x\, \text{Idle}(x)$ ("there does not exist an idle robot")

**Option 2 (equivalent):** $\forall x\, \neg\text{Idle}(x)$ ("every robot is not idle")

These are equivalent by quantifier negation: $\neg\exists x\, \varphi(x) \equiv \forall x\, \neg\varphi(x)$

</details>

### Practice 5: Truth Table for OR-based Implication

**Given:** $(A \vee B) \rightarrow C$, $\neg C$. Deduce what must be true.

<details>
<summary>Click to see answer</summary>

By Modus Tollens: $\neg(A \vee B)$.

By De Morgan's: $\neg A \wedge \neg B$.

**Both A and B must be false.** (This is the same pattern as the S1 2025 actual test.)

Full truth table verification:

| $A$ | $B$ | $A \vee B$ | $C$ | $(A \vee B) \rightarrow C$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 ✓ |
| 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 ✗ |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 ✗ |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 ✗ |
| 1 | 1 | 1 | 1 | 1 |

With $C = 0$ and rule true: only row 1 works. Both $A = 0$ and $B = 0$.

</details>

---

## 🌍 Wumpus World -- The Lecture's Running Example

The Wumpus World (lecture slides 17-20) is used to illustrate how propositional logic represents knowledge and enables inference. You should understand this example for conceptual questions.

**Setup:** A $4 \times 4$ grid with pits, a Wumpus, and gold. The agent navigates from (1,1).

**Key rules in propositional logic (slide 19):**
- "Square (1,3) has a pit": $P_{1,3}$
- "Square (2,2) has no wumpus": $\neg W_{2,2}$
- "Either (2,2) has a pit or (1,3) has a pit": $P_{2,2} \vee P_{1,3}$
- "Since (2,2) has no stench, (1,2) has no wumpus": $\neg S_{2,2} \rightarrow \neg W_{1,2}$
- "(2,4) is safe iff no pit or wumpus": $OK_{2,4} \leftrightarrow (\neg P_{2,4} \wedge \neg W_{2,4})$

**Inference example (slide 20):**
- $P1 = \neg S_{1,1} \wedge \neg B_{1,1}$ (no stench, no breeze at start)
- From P1, infer $P2 = \neg S_{1,1}$ (no stench at start)
- $P3$: if $(3,1)$ is a pit, at least one of $(2,1)$, $(3,2)$ has a breeze
- $P4$: if none of $(2,1)$, $(3,2)$ has a breeze, then $(3,1)$ is not a pit

This demonstrates how propositional logic enables **forward chaining** (derive new facts from known facts) and **backward chaining** (verify a hypothesis by checking its premises).

**Why propositional logic is weak for Wumpus World (slide 24):**
- "A breeze is sensed iff an adjacent location contains a pit" requires one formula per square:
  - $B_{1,1} \leftrightarrow (P_{1,2} \vee P_{2,1})$
  - $B_{1,2} \leftrightarrow (P_{1,3} \vee P_{2,2} \vee P_{1,1})$
  - ... one for EACH square

In FOL, this becomes ONE formula: $\forall x\, (\text{Breeze}(x) \leftrightarrow \exists y\, (\text{Adjacent}(x,y) \wedge \text{Pit}(y)))$

---

## 🌐 English Expression Tips

### Exam Answer Sentence Templates

**For Modus Tollens questions:**
- "Given the rule [formula] and the observation [negated conclusion], by Modus Tollens we can deduce [negated premise]."
- "Applying De Morgan's Law, $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$, which means at least one of P, Q must be false."
- "Applying De Morgan's Law, $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$, which means both P and Q must be false."

**For FOL translation questions:**
- "Let the domain be [X]. Define predicate [name](x) to mean [meaning]."
- "The statement translates to: [formula]."
- "This is equivalent to [alternative form] by [law name]."

**For FOL reasoning:**
- "From the universal rule $\forall x\, (P(x) \rightarrow Q(x))$, we instantiate for [specific object]: $P(a) \rightarrow Q(a)$."
- "Given $\neg Q(a)$, by Modus Tollens: $\neg P(a)$. Therefore, [conclusion in English]."

### Commonly Confused Terms

| Pair | Clarification |
|------|---------------|
| "implies" ($\rightarrow$) vs "equivalent" ($\leftrightarrow$) | $\rightarrow$ is one-way; $\leftrightarrow$ is two-way. "If P then Q" vs "P if and only if Q" |
| "logically implies" ($\Rightarrow$) vs "material implication" ($\rightarrow$) | $\Rightarrow$ is a meta-statement (always true across all interpretations); $\rightarrow$ is a connective with a truth value |
| $\forall$ vs $\exists$ | "for all" vs "there exists" -- check quantifier scope carefully |
| "necessary" vs "sufficient" | In $P \rightarrow Q$: P is **sufficient** for Q; Q is **necessary** for P |
| "converse" vs "contrapositive" | Converse of $P \rightarrow Q$ is $Q \rightarrow P$ (NOT equivalent); Contrapositive is $\neg Q \rightarrow \neg P$ (equivalent) |
| "bound" vs "free" variable | Bound = within scope of $\forall$ or $\exists$; Free = not bound by any quantifier |
| "formula" vs "sentence" | A sentence has no free variables; a formula may have free variables |

### Commonly Misspelled Words

- ~~proposisional~~ $\rightarrow$ propositional
- ~~modus tolens~~ $\rightarrow$ modus tollens (double-l)
- ~~De Morgans~~ $\rightarrow$ De Morgan's (with apostrophe)
- ~~equivelance~~ $\rightarrow$ equivalence
- ~~tautaology~~ $\rightarrow$ tautology
- ~~existensial~~ $\rightarrow$ existential
- ~~quantifer~~ $\rightarrow$ quantifier

---

## ✅ Self-Test Checklist

### Propositional Logic Fundamentals
- [ ] Can I write the truth table for ALL five connectives ($\neg, \wedge, \vee, \rightarrow, \leftrightarrow$) from memory?
- [ ] Can I explain why $P \rightarrow Q$ is TRUE when $P$ is false (vacuous truth)?
- [ ] Can I convert $P \rightarrow Q$ to $\neg P \vee Q$ and back?
- [ ] Do I know both De Morgan's Laws and can I apply them correctly?
- [ ] Can I distinguish between $\neg(A \wedge B) = \neg A \vee \neg B$ and $\neg(A \vee B) = \neg A \wedge \neg B$?

### Inference Rules
- [ ] Can I identify Modus Tollens in a word problem and apply it step by step?
- [ ] Can I explain why Affirming the Consequent ($P \rightarrow Q$, $Q$ $\therefore$ $P$) is INVALID?
- [ ] Can I state the difference between Modus Ponens and Modus Tollens?
- [ ] Can I perform the full truth-table-based deduction required by the 2026 sample?

### First-Order Logic
- [ ] Can I translate "Not all X have property P" correctly as $\neg\forall x\, P(x)$ (NOT $\forall x\, \neg P(x)$)?
- [ ] Do I know the quantifier negation laws: $\neg\forall x = \exists x\, \neg$ and $\neg\exists x = \forall x\, \neg$?
- [ ] Can I apply Universal Instantiation followed by Modus Tollens (S1 2025 actual test pattern)?
- [ ] Do I know the rule of thumb: $\forall$ pairs with $\rightarrow$, $\exists$ pairs with $\wedge$?
- [ ] Can I distinguish free vs. bound variables and identify whether a formula is a sentence?

### Exam Readiness
- [ ] Can I solve the AND-premise version: $(I \wedge F) \rightarrow E$, $\neg E$ $\therefore$ $\neg I \vee \neg F$?
- [ ] Can I solve the OR-premise version: $(P \vee Q) \rightarrow R$, $\neg R$ $\therefore$ $\neg P \wedge \neg Q$?
- [ ] Can I do both the algebraic AND the truth table method for the same problem?
- [ ] Can I provide a realistic example for $\neg\forall x\, \text{Fly}(x)$ (e.g., penguins, kiwis)?
- [ ] Can I explain why "D is enrolled $\therefore$ D is a student" is a converse error?
- [ ] Have I practiced writing each answer within 3 minutes (time pressure)?

---

## 📋 Quick Reference Card (For Your Handwritten Cheat Sheet)

```
MODUS TOLLENS:  P->Q, ~Q  ==>  ~P

DE MORGAN'S:    ~(A^B) = ~Av~B    (AND becomes OR)
                ~(AvB) = ~A^~B    (OR becomes AND)

IMPLICATION:    P->Q  =  ~PvQ

QUANTIFIERS:    ~forall x P(x)  =  exists x ~P(x)
                ~exists x P(x)  =  forall x ~P(x)

FOL RULE:       forall uses ->    (forall x: P(x) -> Q(x))
                exists uses ^     (exists x: P(x) ^ Q(x))

CONVERSE ERROR: P->Q, Q  =/=>  P    (INVALID!)
CONTRAPOSITIVE: P->Q  =  ~Q->~P     (VALID equivalent)

EXAM PATTERN:
  1. Identify P->Q structure
  2. Apply Modus Tollens: ~Q ==> ~P
  3. Apply De Morgan's to simplify ~P
  4. State conclusion in English
```
