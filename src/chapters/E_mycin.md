# MYCIN, Expert Systems & Forward/Backward Chaining

## Exam Priority

**Medium frequency** | Appeared directly in 1/4 past tests (2025 Sample Q6, backward chaining, 3 marks) | Forward/backward chaining is a fundamental reasoning concept that underpins many AI systems | Typically worth 3 marks

---

## Let's Start From Scratch

### What Is an Expert System?

Before machine learning existed, people still wanted computers to make smart decisions. The idea was simple: find a human expert (say, a doctor who has diagnosed thousands of infections), sit down with them, extract every rule they use, and code those rules into a program.

That program is an **expert system**. It does not learn from data. It reasons from rules that a human gave it.

MYCIN was one of the first and most famous. Built at Stanford in the 1970s by Ted Shortliffe, it diagnosed bacterial blood infections. And here is the remarkable thing: in blind tests, MYCIN's diagnoses were as good as or better than many human physicians. But it was never deployed clinically — partly because doctors did not trust a machine, and partly because of legal liability issues. Still, the ideas it introduced shaped AI for decades.

### The Four Components You Must Know

Think of MYCIN as a detective agency with four departments:

| Component | What It Does | The Detective Analogy |
|---|---|---|
| **Knowledge Base** | ~200 IF-THEN rules with confidence factors | The case-law handbook — "if fingerprints match AND window is broken, suspect burglary (confidence 0.8)" |
| **Inference Engine** | Takes facts and rules, chains them together to reach conclusions | The detective doing the actual reasoning — connecting clues to suspects |
| **Explanation System** | Answers WHY and HOW queries | The detective explaining their reasoning to the jury |
| **User Interface** | Asks the doctor questions, presents conclusions | The detective interviewing witnesses |

There is also a **Working Memory** (the facts known about the current patient — like the detective's notepad for *this specific case*) and a **Rule-Acquisition System** (for adding new rules — like updating the handbook with new case law).

The critical insight: the Knowledge Base and the Inference Engine are **separate**. The rules are data, not code. This means you can swap out the medical rules for, say, geology rules, and the same inference engine works. This led to **E-MYCIN** (Empty MYCIN) — the first expert system shell. More on that later.

---

## Production Rules & Confidence Factors

### The Rule Format

Every rule in MYCIN looks like this:

```
IF   condition_1 AND condition_2 AND condition_3
THEN conclusion  (CF = confidence factor)
```

Here is a real MYCIN rule:

```
IF   stain       = gram-negative
AND  morphology  = rod
AND  aerobicity  = anaerobic
THEN identity    = Bacteroides  (CF = 0.6)
```

Translation: "If the bacteria stains gram-negative, is rod-shaped, and cannot survive in oxygen, then it is probably Bacteroides, and I am 60% confident in this rule."

### What Is a Confidence Factor?

A CF is a number between -1 and 1. It is NOT a probability — this is a common exam mistake. It represents the degree of belief:

- CF = 1.0 means "I am completely certain this is true"
- CF = 0.0 means "I have no opinion"
- CF = -1.0 means "I am completely certain this is false"

In practice, most CFs are between 0 and 1 for positive evidence.

### The Two CF Formulas You Must Know

**Formula 1 — Combining premise with rule:**

\\[
\text{CF}(\text{conclusion}) = \text{CF}(\text{premise}) \times \text{CF}(\text{rule})
\\]

This makes intuitive sense: if you are not very sure about your evidence, AND the rule itself is not very strong, then you should be even less sure about the conclusion.

**Formula 2 — CF of a conjunctive premise (AND):**

\\[
\text{CF}(A \land B \land C) = \min\bigl(\text{CF}(A),\; \text{CF}(B),\; \text{CF}(C)\bigr)
\\]

This also makes intuitive sense: a chain is only as strong as its weakest link. If you are very sure about two conditions but uncertain about the third, your overall premise confidence is limited by that weakest condition.

### Worked Example — Follow This Carefully

Let's say we have these facts about a patient's blood sample:

```
CF(stain = gram-negative)  = 0.8   (lab is pretty sure)
CF(morphology = rod)       = 0.9   (lab is quite sure)
CF(aerobicity = anaerobic) = 0.7   (lab is somewhat sure)
```

And the rule says: IF all three THEN Bacteroides (CF = 0.6)

**Step 1: Compute the premise CF using min():**

```
CF(premise) = min(0.8, 0.9, 0.7) = 0.7
```

The weakest link is 0.7 (the anaerobic observation), so the premise confidence is 0.7.

**Step 2: Multiply by the rule CF:**

```
CF(conclusion) = CF(premise) × CF(rule) = 0.7 × 0.6 = 0.42
```

The system is only 42% confident that this is Bacteroides. Why so low? Because the weakest evidence (0.7) AND the rule itself (only 0.6 confidence) both drag it down.

### Another Worked Example — Stronger Evidence

Same rule, but better lab results:

```
CF(stain = gram-negative)  = 1.0   (absolutely certain)
CF(morphology = rod)       = 1.0   (absolutely certain)
CF(aerobicity = anaerobic) = 1.0   (absolutely certain)
```

```
CF(premise) = min(1.0, 1.0, 1.0) = 1.0
CF(conclusion) = 1.0 × 0.6 = 0.6
```

Even with perfect evidence, you can never get above 0.6 because the rule itself only has CF = 0.6. The rule encodes the fact that even when all three conditions are met, there is still a 40% chance it is not Bacteroides.

> **Common Misconception:** Students sometimes multiply all the CFs together: 0.8 × 0.9 × 0.7 × 0.6. This is WRONG. You use **min()** for the AND conditions, then multiply by the rule CF. Do not confuse these two operations.

---

## Forward vs Backward Chaining — The Core of This Chapter

This is the topic that actually gets tested. Let me teach it to you properly.

### The Setup

Imagine you have a set of rules and a set of known facts. The question is: **in what direction do you reason?**

There are exactly two directions, and they are opposites.

### Forward Chaining (Data-Driven)

**The metaphor:** You are a detective who arrives at a crime scene. You walk around, collect every clue you can find, then go back to the station and flip through your rulebook to see what conclusions you can draw.

**The logic:** You start with what you KNOW and push forward to what you can CONCLUDE.

**The formal basis:** Modus Ponens — if \\(P\\) is true and \\(P \to Q\\), then \\(Q\\) is true.

**The condition type:** A is **sufficient** for B. Meaning: if A is true, that is enough to conclude B.

**The connection to MYCIN:** Forward chaining relates to **HOW queries** — "How did you conclude X?" The system traces forward from facts to conclusion.

Let me walk through an example:

```
Rules:
  R1: IF runny_nose AND rash THEN measles
  R2: IF runny_nose THEN common_cold
  R3: IF runny_nose AND history_of_allergies THEN allergies

Known facts: {runny_nose, rash}

Forward chaining process:
  Step 1: Look at facts: runny_nose, rash
  Step 2: Check R1: runny_nose (YES) AND rash (YES) → fire! Conclude: measles
  Step 3: Check R2: runny_nose (YES) → fire! Conclude: common_cold
  Step 4: Check R3: runny_nose (YES) AND history_of_allergies (NO) → cannot fire
  
  Result: {measles, common_cold} are derived
```

Notice: forward chaining fires EVERY rule whose conditions are met. It might derive things you did not ask about. It is exhaustive but can be inefficient.

### Backward Chaining (Goal-Driven)

**The metaphor:** Your boss calls and says "Was this a burglary?" Now you have a specific **goal** to investigate. You look up your rulebook: "To confirm burglary, I need evidence of forced entry AND missing valuables." So you go to the crime scene specifically looking for those two things. If you find one but not the other, you ask the homeowner.

**The logic:** You start with what you WANT TO PROVE and work backward to find the evidence you NEED.

**The condition type:** B is **necessary** for proving A — but NOT necessarily the ONLY way to prove A.

**The connection to MYCIN:** Backward chaining relates to **WHY queries** — "Why are you asking me about rash?" Because the system is trying to prove/disprove measles, and rash is needed for that.

**MYCIN uses backward chaining as its primary reasoning strategy.** It starts with hypotheses about possible infections and works backward to find the evidence.

Let me walk through the same example, but backward:

```
Rules:
  R1: IF runny_nose AND rash THEN measles
  R2: IF runny_nose THEN common_cold
  R3: IF runny_nose AND history_of_allergies THEN allergies

Known facts: {runny_nose}

Backward chaining — Goal: "Does the patient have common cold?"
  Step 1: Goal = common_cold
  Step 2: Which rule concludes common_cold? R2.
  Step 3: R2 needs: runny_nose. Does patient have it? YES.
  Step 4: Rule fires → common_cold is SUPPORTED.

Backward chaining — Goal: "Does the patient have measles?"
  Step 1: Goal = measles
  Step 2: Which rule concludes measles? R1.
  Step 3: R1 needs: runny_nose AND rash.
  Step 4: runny_nose? YES. rash? UNKNOWN.
  Step 5: System asks the doctor: "Does the patient have a rash?"
  Step 6: If YES → measles is SUPPORTED. If NO → measles is NOT SUPPORTED.

Backward chaining — Goal: "Does the patient have allergies?"
  Step 1: Goal = allergies
  Step 2: Which rule concludes allergies? R3.
  Step 3: R3 needs: runny_nose AND history_of_allergies.
  Step 4: runny_nose? YES. history_of_allergies? UNKNOWN.
  Step 5: System asks: "Does the patient have a history of allergies?"
```

See how backward chaining is focused? It only asks about what it needs. It does not wander around collecting random facts.

### The Comparison Table

| Aspect | Forward Chaining | Backward Chaining |
|---|---|---|
| Starting point | Known facts | Hypothesis / goal |
| Direction | Facts → Conclusions | Goal → What evidence do I need? |
| Logic basis | Modus Ponens | Goal reduction |
| Condition type | A is SUFFICIENT for B | A is NECESSARY for B (but not unique) |
| MYCIN query type | HOW ("How did you conclude X?") | WHY ("Why are you asking about X?") |
| When to use | Lots of data, want to explore all conclusions | Specific hypothesis to test |
| Efficiency | May derive irrelevant conclusions | Focused — only explores what is needed |
| Analogy | Collect all clues, then deduce | Boss asks a question, go find specific proof |

### The Critical Nuance — Backward Chaining Does NOT Prove Uniqueness

This is the single most important subtlety, and it costs marks if you miss it.

When backward chaining finds that "runny nose supports common cold," that does NOT mean runny nose can ONLY be caused by a common cold. The same runny nose also supports allergies and measles. Backward chaining finds **possible** support for a hypothesis. It does not prove the hypothesis is the only explanation.

In formal terms:

```
IF A THEN B
```

- **Forward reading:** A is SUFFICIENT for B (if A is true, B follows)
- **Backward reading:** we need A to prove B, but A being true does not mean B is the ONLY thing A can prove

---

## WHY vs HOW Queries — A Clean Summary

This comes up in exams either as a direct question or as part of a backward/forward chaining answer.

| Query | Chaining Direction | What It Does | Example |
|---|---|---|---|
| **WHY** | Backward | Explains why the system is asking a particular question | Doctor: "Why are you asking about rash?" System: "Because I am testing the hypothesis of measles, which requires runny nose AND rash." |
| **HOW** | Forward-like | Explains how the system reached a particular conclusion | Doctor: "How did you conclude Bacteroides?" System: "Because stain=gram-negative AND morphology=rod AND aerobicity=anaerobic, which triggers Rule 27." |

Think of it this way:
- **WHY** looks UP the chain (toward the goal): "I'm asking because I need this to test THAT hypothesis"
- **HOW** looks DOWN the chain (toward the facts): "I concluded this because THOSE facts triggered THAT rule"

---

## E-MYCIN — The First Expert System Shell

Here is one of the most important ideas in AI engineering history.

After MYCIN was built, the researchers realized something: the inference engine, the explanation system, and the user interface had NOTHING to do with medicine. They were completely general. The only medical-specific part was the knowledge base (the 200 rules about bacteria).

So they stripped out the medical knowledge and got **E-MYCIN** (Empty MYCIN) — a general-purpose shell:

```
MYCIN    = E-MYCIN + Medical Knowledge Base
PUFF     = E-MYCIN + Pulmonary Disease Knowledge Base
HEADMED  = E-MYCIN + Headache Diagnosis Knowledge Base
New System = E-MYCIN + Your Domain Knowledge Base
```

This was revolutionary because it separated **knowledge** from **reasoning**. You did not need to write a new AI program for every domain — you just plugged in different rules.

### The Knowledge Acquisition Bottleneck

Expert systems had a fatal weakness that eventually led to the "AI winter" of the late 1980s:

1. **Hard to extract knowledge.** Try getting a doctor to articulate EVERY rule they use. Most expertise is intuitive and implicit — experts often cannot explain why they make a decision.
2. **Hard to maintain.** Medical knowledge changes constantly. 200 rules become 2000 rules. Debugging rule interactions becomes a nightmare.
3. **Brittle.** If a situation falls outside the rules, the system has no way to reason about it. Unlike a human, it cannot improvise.
4. **No learning.** MYCIN could not learn from its mistakes or from new cases. Every improvement required a human to manually add or modify rules.

This is why machine learning eventually replaced expert systems for most tasks. But the ideas — separating knowledge from reasoning, explaining decisions, handling uncertainty — remain deeply influential.

---

## Past Paper: 2025 Sample Q6 (3 marks) — Complete Walkthrough

**Question:** Describe backward chaining reasoning for a patient with runny nose.

**Given concepts:** runny nose, history of allergies, rash, common cold, allergies, measles.

Let me show you exactly how to answer this for full marks.

### What the Examiner Wants

Three things, worth 1 mark each:

1. You correctly start from a **goal/hypothesis** (not from facts)
2. You show **backward reasoning** — tracing from goal to required evidence
3. You show that the system **asks for missing information**

### Model Answer

Backward chaining is a goal-driven reasoning strategy. The system starts with a hypothesis and works backward through rules to determine what evidence is needed.

**Instance 1 — Goal: common cold**

The system hypothesizes "common cold." It looks up the relevant rule: IF runny_nose THEN common_cold. It checks: does the patient have a runny nose? Yes. Therefore, the hypothesis "common cold" is supported.

**Instance 2 — Goal: measles**

The system hypothesizes "measles." The relevant rule: IF runny_nose AND distinctive_rash THEN measles. The patient has a runny nose (confirmed), but the system does not know about a rash. It asks the physician: "Does the patient have a distinctive rash?" — this is a WHY query situation.

**Instance 3 — Goal: allergies**

The system hypothesizes "allergies." The relevant rule: IF runny_nose AND history_of_allergies THEN allergies. Runny nose is confirmed, but history of allergies is unknown. The system asks: "Does the patient have a history of allergies?"

**Important:** Backward chaining does NOT prove that any single diagnosis is correct. It identifies possible support. Multiple hypotheses can be simultaneously supported by the same evidence (runny nose supports all three).

### Mark Allocation

| What to Include | Marks |
|---|---|
| Start from a goal/hypothesis, not from facts | 1 |
| Show backward reasoning (goal → what evidence do I need?) | 1 |
| Show the system asking for missing information when evidence is unknown | 1 |

---

## Practice Problems

### Problem 1 — Forward Chaining Step by Step

Given these rules and facts, show forward chaining:

```
Rules:
  R1: IF fever AND cough THEN flu
  R2: IF flu AND age > 65 THEN hospitalize
  R3: IF cough AND sore_throat THEN cold
  R4: IF fever AND rash THEN measles

Known facts: {fever, cough, age > 65}
```

**Solution:**

```
Step 1: Check all rules against known facts
  R1: fever (YES) AND cough (YES) → FIRE → add "flu" to facts
  R2: flu (not yet known) — skip for now
  R3: cough (YES) AND sore_throat (NO) — cannot fire
  R4: fever (YES) AND rash (NO) — cannot fire

Step 2: Facts updated: {fever, cough, age > 65, flu}
  Re-check rules:
  R2: flu (YES) AND age > 65 (YES) → FIRE → add "hospitalize"
  (R1 already fired, R3 and R4 still cannot fire)

Step 3: Facts updated: {fever, cough, age > 65, flu, hospitalize}
  No new rules can fire → STOP.

Final conclusions: flu, hospitalize
```

### Problem 2 — Backward Chaining Step by Step

Using the same rules, show backward chaining with goal = "hospitalize":

```
Goal: hospitalize
  Which rule concludes "hospitalize"? R2.
  R2 needs: flu AND age > 65
  
  Sub-goal 1: age > 65
    Is this a known fact? YES. ✓
  
  Sub-goal 2: flu
    Is this a known fact? NO.
    Which rule concludes "flu"? R1.
    R1 needs: fever AND cough.
    
    Sub-sub-goal 2a: fever — known? YES. ✓
    Sub-sub-goal 2b: cough — known? YES. ✓
    
    R1 fires → flu is derived. ✓
  
  R2 fires → hospitalize is SUPPORTED. ✓
```

Notice how backward chaining only explored R1 and R2 — it never even looked at R3 or R4. It was laser-focused on proving "hospitalize."

### Problem 3 — WHY or HOW?

For each scenario, identify whether it is a WHY query or a HOW query:

**(a)** The system has just concluded "flu." The doctor asks: "How did you determine the patient has flu?"

**Answer:** HOW query. The system traces forward from facts: "Because the patient has fever AND cough, which triggers Rule R1."

**(b)** The system asks the doctor: "Does the patient have a rash?" The doctor responds: "Why are you asking about rash?"

**Answer:** WHY query. The system traces backward toward the goal: "Because I am testing the hypothesis of measles, which requires fever AND rash."

**(c)** The system presents a final diagnosis. The doctor asks: "How did you reach the diagnosis of Bacteroides?"

**Answer:** HOW query. Forward-like trace from evidence to conclusion.

**(d)** The system asks: "Is the organism aerobic or anaerobic?" The doctor asks: "Why do you need to know this?"

**Answer:** WHY query. The system is pursuing a backward chain toward a hypothesis about organism identity.

### Problem 4 — Compute CF for a Chain of Rules

```
Rule 1: IF A AND B THEN C  (CF = 0.8)
Rule 2: IF C AND D THEN E  (CF = 0.7)

Given:
  CF(A) = 0.9
  CF(B) = 0.6
  CF(D) = 0.85
```

**Solution:**

```
Step 1: Compute CF(C)
  CF(premise of Rule 1) = min(CF(A), CF(B)) = min(0.9, 0.6) = 0.6
  CF(C) = CF(premise) × CF(Rule 1) = 0.6 × 0.8 = 0.48

Step 2: Compute CF(E)
  CF(premise of Rule 2) = min(CF(C), CF(D)) = min(0.48, 0.85) = 0.48
  CF(E) = CF(premise) × CF(Rule 2) = 0.48 × 0.7 = 0.336
```

So the final confidence in E is only 0.336. Notice how uncertainty compounds through a chain of rules — each step multiplies by a number less than 1, so confidence drops rapidly. This is one reason why expert systems with long reasoning chains tend to have very low confidence in their final conclusions.

### Problem 5 — Design Your Own Backward Chaining Scenario

Suppose you have these rules for a car diagnostic system:

```
R1: IF engine_won't_start AND battery_dead THEN replace_battery
R2: IF engine_won't_start AND fuel_empty THEN refuel
R3: IF engine_won't_start AND starter_clicks THEN bad_starter_motor
R4: IF battery_dead AND lights_dim THEN replace_battery
```

Known facts: {engine_won't_start, lights_dim}

**Task:** Show backward chaining for the goal "replace_battery."

**Solution:**

```
Goal: replace_battery
  Which rules conclude replace_battery? R1 and R4.

  Try R1: needs engine_won't_start AND battery_dead
    engine_won't_start? YES. ✓
    battery_dead? UNKNOWN.
    
    Sub-goal: battery_dead
    No rule directly concludes battery_dead from known facts alone.
    But wait — can we infer it?
    
    Actually, R4 concludes replace_battery too. Let's try R4:
    R4 needs battery_dead AND lights_dim.
    lights_dim? YES. ✓
    battery_dead? Still UNKNOWN.
    
    System asks mechanic: "Is the battery dead?"
    If YES → R1 fires (and R4 also fires) → replace_battery is SUPPORTED.
```

---

## Common Mistakes — Do Not Lose Easy Marks

1. **Confusing the direction of chaining.** Forward: facts → conclusions. Backward: goal → find evidence. If you write "backward chaining starts from facts," you will lose marks immediately.

2. **Saying MYCIN uses forward chaining.** MYCIN's primary reasoning strategy is **backward chaining**. The HOW explanation traces forward, but the core reasoning is backward.

3. **Claiming backward chaining proves uniqueness.** Backward chaining shows that evidence *supports* a hypothesis. It does NOT prove the hypothesis is the *only* explanation.

4. **Using multiplication instead of min() for AND.** CF of a conjunctive premise uses **min()**, not multiplication. Multiplication is for combining premise CF with rule CF. These are two different formulas — do not mix them up.

5. **Mixing up WHY and HOW.** WHY = backward (why are you asking me this?). HOW = forward-like (how did you reach that conclusion?). Think: WHY looks up toward the goal, HOW looks down toward the facts.

6. **Saying CF is a probability.** CFs are NOT probabilities. They range from -1 to 1 and represent degrees of belief, not statistical likelihood.

7. **Forgetting E-MYCIN.** If asked about MYCIN's significance, the separation of knowledge from reasoning (leading to E-MYCIN as a reusable shell) is a key point worth mentioning.

---

## English Expression Guide

### Describing Backward Chaining (Exam Sentences)

- "Backward chaining begins with a hypothesis and attempts to find evidence that supports it."
- "The system works backward from a goal, identifying what conditions must hold for the goal to be true."
- "When the system lacks information needed to evaluate a rule, it queries the user."
- "Backward chaining does not prove that a hypothesis is uniquely correct; it identifies possible support."

### Describing Forward Chaining (Exam Sentences)

- "Forward chaining starts from known facts and applies rules to derive new conclusions."
- "Given a set of observations, the system fires all applicable rules to produce inferences."
- "Forward chaining is data-driven: it derives everything that can be concluded from the available evidence."

### Describing MYCIN's Architecture (Exam Sentences)

- "MYCIN separates domain knowledge from the inference mechanism, storing rules in a knowledge base and reasoning over them with a general-purpose engine."
- "The key innovation of MYCIN is that the same inference engine can be reused with different knowledge bases, leading to the concept of an expert system shell (E-MYCIN)."

### Vocabulary Pitfalls

| Correct Term | Common Mistake | Why It Is Wrong |
|---|---|---|
| knowledge base | database | Too generic; a knowledge base has rules, not just data |
| production rule | if-then statement | Too informal for an exam |
| inference engine | reasoning program | Too vague |
| certainty factor (CF) | probability | CF is not a probability — different mathematical framework |
| backward chaining | reverse reasoning | Non-standard term |
| expert system shell | template | A shell is a specific concept with inference + explanation capabilities |

---

## Self-Check Checklist

- [ ] Can you explain in one sentence what MYCIN does and why it was historically important?
- [ ] Can you list the four (or five) main components of MYCIN's architecture?
- [ ] Can you calculate CF(conclusion) given premise CFs and a rule CF?
- [ ] Do you know the difference between min() (for AND premises) and multiplication (for premise × rule)?
- [ ] Can you explain forward vs backward chaining without looking at notes?
- [ ] Can you walk through the 2025 Sample Q6 backward chaining example from memory?
- [ ] Can you explain what WHY and HOW queries do and which direction each uses?
- [ ] Can you explain what E-MYCIN is and why it was a breakthrough?
- [ ] Do you understand why backward chaining does NOT prove uniqueness?
- [ ] Can you compute CF through a multi-step chain of rules?
