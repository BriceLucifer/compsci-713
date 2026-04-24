# Symbolic Logic — Your Complete Exam Survival Guide

## Exam Importance

**MUST-KNOW** | Appeared in **4/4 past tests (100%)** | Worth 2--5 marks each time

Let's be blunt: this topic appears on every single test. Not "most tests." Every. Single. One. The teacher loves it because it tests whether you can actually *reason*, not just memorise. If you walk into the exam without being able to do Modus Tollens in your sleep, you are giving away free marks.

This chapter will teach you everything from scratch, walk you through every past paper question step by step, and give you enough practice that logic questions become automatic.

---

## Part 1 — What Is Logic, Really? (Building Intuition)

Imagine you are a security guard. Your boss gave you a rulebook:

> "If the visitor has a valid ID **and** their fingerprint matches, let them in."

One day, someone walks up. You deny them entry. Your boss calls and asks: "So what went wrong?"

You answer: "Well, either they didn't have a valid ID, or their fingerprint didn't match. Maybe both."

Congratulations — you just did **propositional logic**. You took a rule, observed that the *outcome didn't happen*, and worked backward to figure out what must have been wrong with the *inputs*.

That is literally what every Question 1a on this exam asks you to do. Every time. Let's make sure you can do it perfectly.

### The Five Connectives — Your Toolkit

Before we do anything fancy, you need to know the five logical connectives like you know your own name:

| Symbol | Name | Plain English | Example |
|--------|------|---------------|---------|
| ¬ | NOT | "it is not the case that..." | ¬P = "P is false" |
| ∧ | AND | "both ... and ..." | P ∧ Q = "P is true and Q is true" |
| ∨ | OR | "at least one of ..." | P ∨ Q = "P is true, or Q is true, or both" |
| → | IMPLIES | "if ... then ..." | P → Q = "if P then Q" |
| ↔ | IFF | "if and only if" | P ↔ Q = "P and Q are both true, or both false" |

**Stop and think**: the OR in logic is *inclusive* — "P or Q" means "at least one of them," not "exactly one." If both are true, P ∨ Q is still true. This is different from how we use "or" in everyday English ("Would you like tea or coffee?" usually means pick one). In logic, the answer "both" is fine.

---

## Part 2 — The Truth Table for Implication (The Thing That Confuses Everyone)

Here is the truth table you absolutely must memorise:

| P | Q | P → Q |
|---|---|-------|
| T | T | **T** |
| T | F | **F** |
| F | T | **T** |
| F | F | **T** |

The second row is the easy one: if P is true and Q is false, the implication is broken. Makes sense — "if it rains, the ground gets wet" is clearly false when it rains and the ground is dry.

But those last two rows trip up almost everyone. **Why is P → Q true when P is false?**

This is called **vacuous truth**, and let me give you three different ways to understand it, because this concept is worth getting right:

### Analogy 1 — The Unkept Promise

Your friend says: "If it snows in Auckland tomorrow, I will buy you a Ferrari."

It does not snow. Did your friend break their promise? No. They never had to do anything. The promise was never activated. In logic, we say the implication holds *vacuously* — it is true by default because the condition was never met.

### Analogy 2 — The Unbreakable Contract

Think of P → Q as a contract. The contract says: "Whenever P happens, Q must follow." The only way to *break* the contract is for P to happen and Q to NOT follow. If P never happens, the contract was never violated. An unviolated contract is a valid contract.

### Analogy 3 — The Quality Control Inspector

An inspector checks products with the rule: "If a product is labelled Premium, it must weigh over 500g." She picks up a product labelled Standard (P is false). Does she need to weigh it? No. The rule does not apply. The rule is not violated. It holds.

**The bottom line**: P → Q is false in exactly ONE case — when P is true and Q is false. In ALL other cases, it is true. Burn this into your brain.

> **Common Misconception**: Students often write "undefined" or "cannot determine" for the F→T and F→F rows. This will lose you marks. The answer is T in both cases. Always.

---

## Part 3 — Modus Ponens vs Modus Tollens (Forward vs Backward Reasoning)

These are the two most important inference rules. Let's understand them deeply.

### Modus Ponens — "The Forward Rule"

```
Given:  P → Q      (the rule)
Given:  P           (the premise is true)
─────────────────
Conclude: Q         (so the conclusion must be true)
```

This is intuitive. "If it rains, the ground gets wet. It rained. Therefore the ground is wet." Nobody struggles with this.

### Modus Tollens — "The Backward Rule" (THIS IS THE EXAM FAVOURITE)

```
Given:  P → Q      (the rule)
Given:  ¬Q          (the conclusion is FALSE)
─────────────────
Conclude: ¬P        (so the premise must have been FALSE)
```

Think about why this works. Look at the truth table again:

| P | Q | P → Q |
|---|---|-------|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

We are told P → Q is true (it is a given rule). We are told Q is false (¬Q). Look at the rows where Q is false — that is rows 2 and 4. In row 2, P → Q is **false**, but we were told the rule is true, so row 2 is impossible. That leaves only row 4, where P is false. Therefore ¬P.

That is the proof. That is why Modus Tollens works. The exam will never ask you to prove it, but understanding *why* it works means you will never forget *how* to use it.

### When to use which?

| You have... | You use... | You get... |
|---|---|---|
| P → Q and P | Modus Ponens | Q |
| P → Q and ¬Q | **Modus Tollens** | **¬P** |

On this exam, the teacher always gives you a rule and a **negated** conclusion. That means Modus Tollens. Every time. In 4 out of 4 papers.

### Two Dangerous Fallacies (Things That LOOK Like Valid Reasoning But Are NOT)

| Fallacy | Pattern | Why It Is Wrong |
|---------|---------|-----------------|
| **Affirming the consequent** | P → Q, Q, therefore P | Other things could cause Q! |
| **Denying the antecedent** | P → Q, ¬P, therefore ¬Q | Q might be true for other reasons! |

Example of affirming the consequent: "If it rains, the ground is wet. The ground IS wet. Therefore it rained." WRONG — the sprinkler could be on.

Example of denying the antecedent: "If it rains, the ground is wet. It did NOT rain. Therefore the ground is NOT wet." WRONG — again, sprinkler.

If you catch yourself doing either of these on the exam, stop immediately. They are traps.

---

## Part 4 — De Morgan's Laws (The AND/OR Flip)

When you apply Modus Tollens and the antecedent is a compound expression (like P ∧ Q or P ∨ Q), you need De Morgan's Laws to simplify ¬(P ∧ Q) or ¬(P ∨ Q).

Here they are:

```
¬(A ∧ B)  =  ¬A ∨ ¬B       "not both" = "at least one is missing"
¬(A ∨ B)  =  ¬A ∧ ¬B       "neither"  = "both are absent"
```

### Memory Trick: "The NOT goes in, the connector FLIPS"

When you push the negation inside the parentheses:
- ∧ becomes ∨
- ∨ becomes ∧

Think of it like a see-saw. NOT pushes down, and the connector flips to the other side.

### Another Memory Trick: English Translation

- ¬(A ∧ B): "It's NOT the case that BOTH are true" = "At least one is false" = ¬A ∨ ¬B
- ¬(A ∨ B): "It's NOT the case that EITHER is true" = "NEITHER is true" = ¬A ∧ ¬B

Say it in English first, and the formula writes itself.

### The Critical Pattern on Exams

Here is what happens on every test, combined:

```
Step 1: You have a rule like (X ∧ Y) → Z  or  (X ∨ Y) → Z
Step 2: You are told ¬Z
Step 3: Modus Tollens gives you ¬(X ∧ Y)  or  ¬(X ∨ Y)
Step 4: De Morgan's simplifies:
        ¬(X ∧ Y) = ¬X ∨ ¬Y    (at least one failed)
        ¬(X ∨ Y) = ¬X ∧ ¬Y    (BOTH failed)
Step 5: State the conclusion in English
```

Notice the crucial difference in Step 4:
- If the original used AND: the conclusion uses OR ("at least one failed")
- If the original used OR: the conclusion uses AND ("both failed")

Students under time pressure frequently forget the flip and lose marks. Do not be that student.

---

## Part 5 — Every Past Paper Question, Solved Step by Step

Let's walk through every single logic question that has appeared on past tests. I will explain each step as if you have never seen the problem before.

### Past Paper 1: 2026 Sample Test, Q1a (3 marks)

**The question:**

> In a secure facility, a person is granted entry only if they provide both a valid ID and a fingerprint match.
> 
> I: The person has a valid ID
> F: The fingerprint matches
> E: The person is granted entry
> 
> Rule: (I ∧ F) → E
> Observation: The person was not granted entry (¬E).
> 
> Use propositional logic to deduce what must be true about I and F. Show your steps (Truth Table) clearly. **[3 marks]**

**Let's solve this together, step by step.**

This is worth 3 marks — the most this question type has ever been worth. The model answer shows us exactly what the teacher wants: a truth table approach.

**Step 1 — Apply Modus Tollens (1 mark)**

We have:
- Rule: (I ∧ F) → E
- Observation: ¬E

Let X = (I ∧ F). Then our rule is X → E, and we know ¬E.

By Modus Tollens: ¬E implies ¬X, which means ¬(I ∧ F).

Here is the key insight for the 3-mark version: the teacher wants you to show *why* via a truth table. Let me show you the truth table of X → E:

| X (= I ∧ F) | E | X → E |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | **0** |
| 1 | 1 | 1 |

We are told X → E is true (it is our rule) and E = 0 (our observation). Look at the rows where E = 0: that is rows 1 and 3. Row 3 has X → E = 0, which contradicts our rule being true. So only row 1 is possible, where X = 0. Therefore I ∧ F = 0.

**Step 2 — Show the truth table of I ∧ F to determine what I and F can be (1 mark)**

Now we know I ∧ F = 0. What does that tell us about I and F individually?

| I | F | I ∧ F |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Since I ∧ F must be 0, any of the first three rows is possible. The only row eliminated is (I=1, F=1). So: at least one of I or F must be 0.

This is exactly De Morgan's Law: ¬(I ∧ F) = ¬I ∨ ¬F.

**Step 3 — State the conclusion in English (1 mark)**

"The person either did not have a valid ID (¬I), or the fingerprint did not match (¬F), or both."

**Full model answer to write on the exam (3-mark version):**

> Given: (I ∧ F) → E and ¬E.
> 
> The truth table for X → E (where X = I ∧ F):
> 
> | X (I ∧ F) | E | X → E |
> |---|---|---|
> | 0 | 0 | 1 |
> | 0 | 1 | 1 |
> | 1 | 0 | 0 |
> | 1 | 1 | 1 |
> 
> Since E = 0 and X → E must be true, X = I ∧ F must be 0.
> 
> The truth table for I ∧ F:
> 
> | I | F | I ∧ F |
> |---|---|---|
> | 0 | 0 | 0 |
> | 0 | 1 | 0 |
> | 1 | 0 | 0 |
> | 1 | 1 | 1 |
> 
> Since I ∧ F = 0, we have ¬I ∨ ¬F (by De Morgan's Law).
> 
> **Conclusion**: The person either did not have a valid ID or the fingerprint did not match (or both).

---

### Past Paper 2: 2025 Sample Test, Q1a (1 mark)

**The question:** Exact same scenario as above — (I ∧ F) → E, given ¬E — but only **1 mark**.

**Here is the trick most students miss**: when the question is worth only 1 mark, you do NOT need to draw truth tables. The teacher just wants to see that you know Modus Tollens and De Morgan's. Quick and clean.

**Full model answer to write on the exam (1-mark version):**

> Given (I ∧ F) → E and ¬E, apply Modus Tollens: ¬E → ¬(I ∧ F).
> By De Morgan's Law: ¬(I ∧ F) = ¬I ∨ ¬F.
> Conclusion: The person either did not have a valid ID or the fingerprint did not match (or both).

That is it. Three lines. One mark. Done.

**Lesson**: always calibrate your answer length to the mark value. More on this in the "How to Write the Perfect Answer" section below.

---

### Past Paper 3: 2025 Real Test, Q1a (1 mark)

**The question:**

> In a smart office, the alarm system is governed by the following rule:
> "If the door is open or the motion sensor is triggered, then the alarm will sound."
> 
> P: The door is open
> Q: The motion sensor is triggered
> R: The alarm sounds
> 
> Rule: (P ∨ Q) → R
> Observation: The alarm did not sound (¬R).
> 
> Use propositional logic to deduce what must be true about P and Q. **[1 mark]**

**Let's solve this together.**

This looks almost identical to the previous problems, but there is one crucial difference: the antecedent uses **OR (∨)** instead of **AND (∧)**. This changes the De Morgan's result!

**Step 1 — Modus Tollens:**

We have (P ∨ Q) → R and ¬R.
By Modus Tollens: ¬R implies ¬(P ∨ Q).

**Step 2 — De Morgan's Law:**

¬(P ∨ Q) = ¬P **∧** ¬Q

Notice the flip! The OR became AND. This means BOTH must be false, not just one.

**Step 3 — Conclusion in English:**

"The door was NOT open AND the motion sensor was NOT triggered."

**Full model answer:**

> Given (P ∨ Q) → R and ¬R, apply Modus Tollens: ¬(P ∨ Q).
> By De Morgan's Law: ¬(P ∨ Q) = ¬P ∧ ¬Q.
> Therefore, the door was not open and the motion sensor was not triggered.

**Key difference from the previous questions**: When you negate an OR, you get AND. The conclusion here is stronger — we know for certain that BOTH P and Q are false. Compare this to the AND version, where we only know at least one is false.

Let's make sure you really feel this difference:

| Original connective | After Modus Tollens | After De Morgan's | Meaning |
|---|---|---|---|
| (A **∧** B) → C, ¬C | ¬(A ∧ B) | ¬A **∨** ¬B | At least one is false |
| (A **∨** B) → C, ¬C | ¬(A ∨ B) | ¬A **∧** ¬B | Both are false |

This table is gold for the exam. The teacher has tested both variants. Know them both.

---

### Past Paper 4: FOL — "Not all birds can fly" (appeared in 2026 Sample Q1b AND 2025 Sample Q1b)

**The question (from both papers):**

> A biologist claims: "Not all birds in this region can fly."
> Let the domain be all birds in this region, and Fly(x) means bird x can fly.
> 
> (i) Write this claim in formal first-order logic. **[1 mark]**
> (ii) Provide a realistic example (in one sentence) that would make the statement true. **[1 mark]**

**Let's think through this carefully.**

"Not all birds can fly." What does this actually mean?

It does NOT mean "no birds can fly." It means "there is at least one bird that cannot fly." Most birds might still fly just fine — we only need one counterexample.

In FOL, "all birds can fly" would be: ∀x Fly(x)
(Since the domain is already "all birds in this region," we do not need a Bird(x) predicate.)

"NOT all birds can fly" is the negation: **¬∀x Fly(x)**

And by the quantifier negation rule: ¬∀x Fly(x) ≡ ∃x ¬Fly(x)

This reads: "There exists a bird x such that x cannot fly."

**Model answer for part (i):**

> ¬∀x Fly(x)

That is it. One formula, one mark. You could also write ∃x ¬Fly(x) — both are correct.

**Model answer for part (ii):**

> "There is a penguin in this region, and penguins cannot fly."

**The trap to avoid**: Do NOT write ∀x ¬Fly(x). That means "ALL birds cannot fly" — which is much stronger than what the biologist claimed. This is the single most common mistake on this question. Let me explain why in detail.

---

### Past Paper 5: FOL — Universal Instantiation + Modus Tollens (2025 Real Test Q1b, 1 mark)

**The question:**

> At a university, the disciplinary policy states:
> "Every student who cheats in the exam will be disqualified from the course."
> 
> Cheat(x): student x cheats
> Disqualified(x): student x is disqualified
> 
> Rule: ∀x (Cheat(x) → Disqualified(x))
> Observation: Student Alice is not disqualified.
> 
> Based on the rule and the observed fact, use first-order logic to determine whether Alice cheated. **[1 mark]**

**Let's solve this step by step.**

This problem combines two techniques: Universal Instantiation and Modus Tollens. Let's take it one step at a time.

**Step 1 — Universal Instantiation:**

The rule says ∀x (Cheat(x) → Disqualified(x)). This means the rule applies to *every* x. In particular, it applies to Alice. So we can substitute x = Alice:

Cheat(Alice) → Disqualified(Alice)

We have just gone from "for all x" to one specific person. This step is called **universal instantiation**.

**Step 2 — Modus Tollens:**

Now we have a simple propositional setup:
- Rule: Cheat(Alice) → Disqualified(Alice)
- Fact: ¬Disqualified(Alice)

By Modus Tollens: ¬Cheat(Alice)

**Step 3 — Conclusion:**

Alice did not cheat.

**Full model answer:**

> From ∀x (Cheat(x) → Disqualified(x)), instantiate for Alice:
> Cheat(Alice) → Disqualified(Alice).
> Given ¬Disqualified(Alice), apply Modus Tollens:
> ¬Cheat(Alice).
> Conclusion: Alice did not cheat.

Notice the flow: Universal Rule → Instantiate for specific individual → Modus Tollens → Conclusion. This is a template. If the teacher gives you a ∀x rule and a negated fact about a specific person, this is always the approach.

---

## Part 6 — The Tricky Parts That Trip Students Up

### Trap 1: ¬∀x P(x) vs ∀x ¬P(x)

This is the most common FOL mistake. Let me kill it with concrete examples.

**¬∀x P(x)** means "Not all x satisfy P." In other words, there is at least one x that does NOT satisfy P. But many x might still satisfy P.

**∀x ¬P(x)** means "No x satisfies P." Every single x fails to satisfy P.

Example with students and passing:
- ¬∀x Passed(x) = "Not all students passed" = "At least one student failed" (but most might have passed)
- ∀x ¬Passed(x) = "No student passed" = "Every single student failed"

These are wildly different statements. If you write ∀x ¬Passed(x) when you mean ¬∀x Passed(x), you are saying something much too strong.

**The correct equivalence is**: ¬∀x P(x) ≡ **∃x** ¬P(x) — "not all" = "there exists one that doesn't."

### Trap 2: Forgetting the English Conclusion

Look at the model answers from the marking rubrics. Every single one ends with a sentence in English. "The person either did not have a valid ID or the fingerprint did not match." "Alice did not cheat." "The door was not open and the motion sensor was not triggered."

The marks often say things like "1 mark for the natural language conclusion." If you stop at the symbolic derivation, you are literally leaving a mark on the table. Always finish with a plain English sentence.

### Trap 3: Not Adjusting for Mark Value

The same question — (I ∧ F) → E with ¬E — appeared as both a 3-mark and a 1-mark question across different papers. The 3-mark version wants truth tables. The 1-mark version wants a concise three-line derivation. Writing truth tables for a 1-mark question wastes time. Writing three lines for a 3-mark question loses marks.

---

## Part 7 — First-Order Logic: The Complete Guide

### The Three Ingredients of FOL

Propositional logic can only talk about specific facts: "It is raining." "The alarm is on."

First-Order Logic (FOL) adds the ability to talk about *categories*:

1. **Variables**: x, y — placeholders for objects in some domain
2. **Predicates**: Bird(x), Fly(x), Cheat(x) — properties that objects can have
3. **Quantifiers**: 
   - ∀x ("for all x") — every object in the domain satisfies this
   - ∃x ("there exists an x") — at least one object in the domain satisfies this

### The Quantifier Negation Rules

These are essential and come up constantly:

```
¬∀x P(x)  ≡  ∃x ¬P(x)      "not all do" = "some don't"
¬∃x P(x)  ≡  ∀x ¬P(x)      "none do"    = "all don't"
```

Think of these as De Morgan's Laws for quantifiers. The negation goes inside, and ∀ flips to ∃ (and vice versa). Same pattern as AND flipping to OR.

### Common FOL Translation Patterns

Here are the patterns the teacher is most likely to test, based on past papers:

| English | FOL |
|---------|-----|
| "All birds can fly" | ∀x (Bird(x) → Fly(x)) |
| "Not all birds can fly" | ¬∀x Fly(x) or ∃x ¬Fly(x) |
| "No bird can fly" | ∀x ¬Fly(x) or ¬∃x Fly(x) |
| "Some birds can fly" | ∃x (Bird(x) ∧ Fly(x)) |
| "Every student who cheats is disqualified" | ∀x (Cheat(x) → Disqualified(x)) |
| "There is a student who cheats but is not disqualified" | ∃x (Cheat(x) ∧ ¬Disqualified(x)) |

**Important subtlety**: Notice that "all X that are Y are Z" uses →, while "some X are Y and Z" uses ∧. This is a common source of errors:

- ∀x (Bird(x) **→** Fly(x)) — CORRECT for "all birds fly"
- ∀x (Bird(x) **∧** Fly(x)) — WRONG! This says "everything is a bird and can fly" (chairs, rocks, everything)

With ∀, use →. With ∃, use ∧. This is a reliable rule of thumb.

### Universal Instantiation

If you know a statement holds for ALL x, it holds for any specific individual:

```
∀x P(x)
──────────────── Universal Instantiation (x = c)
P(c)
```

This is what lets you go from "every cheater gets disqualified" to "if Alice cheats, Alice gets disqualified."

---

## Part 8 — How to Write the Perfect Answer

Based on the actual marking rubrics from all four papers, here is exactly what to write for each mark value.

### For a 1-mark propositional logic question:

Write exactly this pattern (3 lines, ~30 seconds):

> Given [rule] and [observation], apply Modus Tollens: ¬[consequent] → ¬[antecedent].
> By De Morgan's Law: ¬[antecedent] = [simplified form].
> Conclusion: [English sentence].

Example:
> Given (P ∨ Q) → R and ¬R, apply Modus Tollens: ¬(P ∨ Q).
> By De Morgan's: ¬(P ∨ Q) = ¬P ∧ ¬Q.
> Conclusion: The door was not open and the motion sensor was not triggered.

### For a 3-mark propositional logic question:

Write this pattern (~2 minutes):

> 1. State the rule and observation.
> 2. Show the truth table for X → E (the implication).
> 3. Explain: since E = 0 and the rule is true, X must be 0.
> 4. Show the truth table for the antecedent (e.g., I ∧ F).
> 5. Identify which rows have the antecedent = 0.
> 6. State De Morgan's Law.
> 7. Write the English conclusion.

### For a 1-mark FOL translation:

Just write the formula. One line.

> ¬∀x Fly(x)

### For a 1-mark FOL reasoning question:

Write the instantiation, Modus Tollens, and conclusion (4 lines):

> From ∀x (Cheat(x) → Disqualified(x)), instantiate for Alice:
> Cheat(Alice) → Disqualified(Alice).
> Given ¬Disqualified(Alice), by Modus Tollens: ¬Cheat(Alice).
> Conclusion: Alice did not cheat.

### For a 2-mark FOL question (translation + example):

> (i) ¬∀x Fly(x)
> (ii) "There is a penguin in this region, and penguins cannot fly."

---

## Part 9 — Practice Problems with Full Solutions

Here are practice problems covering every angle the teacher might test. Try each one BEFORE reading the solution. Seriously — cover the solution and work it out on paper first.

### Practice 1: Modus Tollens with AND antecedent

> A hospital has the following rule: "If the patient has both a fever (F) and a cough (C), then the patient is isolated (I)."
> Rule: (F ∧ C) → I
> Observation: Patient Bob is not isolated (¬I).
> What can you deduce about F and C?

**Solution:**

> By Modus Tollens: ¬I → ¬(F ∧ C).
> By De Morgan's: ¬(F ∧ C) = ¬F ∨ ¬C.
> Conclusion: Patient Bob either does not have a fever, or does not have a cough (or both).

### Practice 2: Modus Tollens with OR antecedent

> A fire alarm system works as follows: "If smoke is detected (S) or heat exceeds the threshold (H), the alarm activates (A)."
> Rule: (S ∨ H) → A
> Observation: The alarm did not activate (¬A).
> What can you deduce?

**Solution:**

> By Modus Tollens: ¬A → ¬(S ∨ H).
> By De Morgan's: ¬(S ∨ H) = ¬S ∧ ¬H.
> Conclusion: Smoke was NOT detected AND heat did NOT exceed the threshold. Both conditions were absent.

Note how the OR in the original gives a stronger conclusion (AND) compared to Practice 1 where AND in the original gave a weaker conclusion (OR).

### Practice 3: FOL translation — "Not all X are Y"

> Translate into FOL: "Not every employee in the company speaks English."
> Let the domain be all employees in the company. Let Speaks(x) mean "x speaks English."

**Solution:**

> ¬∀x Speaks(x)
>
> Equivalently: ∃x ¬Speaks(x) — "There exists an employee who does not speak English."
>
> Example: "Maria is an employee who only speaks Spanish."

### Practice 4: FOL translation — "Every X that is Y is also Z"

> Translate into FOL: "Every student who submits late receives a penalty."
> Domain: all students. Late(x): x submits late. Penalty(x): x receives a penalty.

**Solution:**

> ∀x (Late(x) → Penalty(x))

Not ∀x (Late(x) ∧ Penalty(x)) — that would mean every student in the domain submits late AND receives a penalty, which is not what the English says.

### Practice 5: Universal Instantiation + Modus Tollens

> Rule: "Every car that exceeds the speed limit will receive a fine."
> ∀x (Speeding(x) → Fined(x))
> Observation: Car #42 did not receive a fine (¬Fined(Car42)).
> Did Car #42 exceed the speed limit?

**Solution:**

> By universal instantiation with x = Car42:
> Speeding(Car42) → Fined(Car42).
> Given ¬Fined(Car42), by Modus Tollens:
> ¬Speeding(Car42).
> Conclusion: Car #42 did not exceed the speed limit.

### Practice 6: Truth Table Construction (for 3-mark questions)

> Rule: (A ∨ B) → C
> Observation: ¬C
> Show, using truth tables, what must be true about A and B.

**Solution:**

Let X = (A ∨ B). Truth table for X → C:

| X (A ∨ B) | C | X → C |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Since C = 0 and X → C is true (our rule), only row 1 is valid. So X = A ∨ B = 0.

Truth table for A ∨ B:

| A | B | A ∨ B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

A ∨ B = 0 only in row 1. So A = 0 and B = 0.

This is De Morgan's: ¬(A ∨ B) = ¬A ∧ ¬B.

Conclusion: Both A and B are false.

### Practice 7: Mixed — FOL negation chain

> Rule: ∀x (Registered(x) → CanVote(x))
> Translate the negation of the rule into FOL. What does it mean?

**Solution:**

> ¬∀x (Registered(x) → CanVote(x))
> ≡ ∃x ¬(Registered(x) → CanVote(x))

Now, recall that P → Q ≡ ¬P ∨ Q. So ¬(P → Q) ≡ ¬(¬P ∨ Q) ≡ P ∧ ¬Q.

> ≡ ∃x (Registered(x) ∧ ¬CanVote(x))

Meaning: "There exists a registered person who cannot vote." The rule has a loophole.

---

## Part 10 — Quick Reference Card

Keep this in your head (or on your double-sided handwritten note sheet):

```
MODUS PONENS:    P → Q,  P       ⟹  Q
MODUS TOLLENS:   P → Q,  ¬Q      ⟹  ¬P        ← ALWAYS tested

DE MORGAN 1:     ¬(A ∧ B)  =  ¬A ∨ ¬B          ← negate AND, get OR
DE MORGAN 2:     ¬(A ∨ B)  =  ¬A ∧ ¬B          ← negate OR, get AND

QUANTIFIER NEGATION:
  ¬∀x P(x)  ≡  ∃x ¬P(x)     "not all" = "some don't"
  ¬∃x P(x)  ≡  ∀x ¬P(x)     "none"    = "all don't"

UNIVERSAL INSTANTIATION:
  ∀x P(x)  ⟹  P(c)           for any specific c

IMPLICATION EQUIVALENCE:
  P → Q  ≡  ¬P ∨ Q

COMMON FALLACIES (INVALID — never use these):
  P → Q,  Q   ⟹  P     ← WRONG (affirming the consequent)
  P → Q,  ¬P  ⟹  ¬Q    ← WRONG (denying the antecedent)
```

---

## Part 11 — English Expression Guide

### Phrases for Modus Tollens derivations

- "We are given the rule (P ∧ Q) → R and observe ¬R."
- "By Modus Tollens, since the consequent R is false, the antecedent (P ∧ Q) must also be false."
- "Applying De Morgan's Law, ¬(P ∧ Q) is equivalent to ¬P ∨ ¬Q."
- "We conclude that at least one of P or Q is false (or both)."

### Phrases for FOL questions

- "Let the domain be the set of all [people / birds / students]."
- "Define the predicate P(x) to mean 'x has property P.'"
- "By universal instantiation with x = Alice, the rule becomes..."
- "There exists an x such that x is a [bird] and x cannot [fly]."

### Words to avoid

| Do not write | Write instead |
|---|---|
| "A implies B, so B implies A" | "A implies B does not tell us anything about the converse" |
| "disprove" (when meaning ¬Q) | "Q is false" or "the negation of Q holds" |
| "cannot determine" (for F→T in truth table) | The value is T (true, by vacuous truth) |

---

## Self-Check Checklist

Before you walk into the exam, make sure you can answer YES to every single one:

- [ ] Can I write truth tables for ∧, ∨, →, and ↔ from memory?
- [ ] Can I explain why P → Q is true when P is false (vacuous truth)?
- [ ] Can I apply Modus Tollens on (A ∧ B) → C with ¬C, and get ¬A ∨ ¬B?
- [ ] Can I apply Modus Tollens on (A ∨ B) → C with ¬C, and get ¬A ∧ ¬B?
- [ ] Do I know the difference between the two De Morgan's results above?
- [ ] Can I translate "not all X satisfy P" into FOL (¬∀x P(x) ≡ ∃x ¬P(x))?
- [ ] Can I do Universal Instantiation then Modus Tollens for a named individual?
- [ ] Do I always finish with a natural language conclusion?
- [ ] Do I know to write truth tables for 3-mark questions but not for 1-mark questions?
- [ ] Can I spot and reject affirming the consequent and denying the antecedent?
- [ ] Do I know that ¬∀x P(x) is NOT the same as ∀x ¬P(x)?
