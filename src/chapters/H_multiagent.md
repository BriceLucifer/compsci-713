# Embodied AI and AI Teams (Lecture 12 / W6L1)

## Exam Priority

**HIGH FREQUENCY** | Appeared 3/4 past tests | 2 marks each time (robot soccer Q4) | One of the easiest 2 marks on the exam.

This lecture covers two big themes: **Embodied AI** (robots that act in the physical world) and **AI Teams** (multiple agents coordinating). The exam question always targets robot soccer, but understanding the full lecture gives you the conceptual foundation to answer confidently and handle any variation the examiner might throw in.

---

# Part 1: Embodied AI

## What Is Embodied AI?

Imagine you have built the world's best chess engine. It can beat any human. Now ask it to walk across a room, pick up a coffee cup, and bring it to you. It cannot do any of that. It has no body, no sensors, no motors. It lives entirely in an abstract world of board positions.

**Embodied AI** is the opposite: systems that control a physical body and must react to sensor data in real time. A robot that navigates a corridor, a quadruped that balances on rough terrain, a rover that drives across Mars -- these are embodied AI.

Why does having a body change everything? Three reasons:

| Factor | Abstract AI (e.g., chess) | Embodied AI (e.g., robot) |
|---|---|---|
| **Environment** | Perfect information, discrete states | Noisy sensors, continuous world |
| **Time** | Take as long as you need to think | Must react in milliseconds |
| **Failure mode** | Wrong move costs a piece | Wrong move crashes into a wall |

The main thread of this lecture is a philosophical one: **intelligence is often about acting robustly in the world, not about abstract reasoning.** A cockroach navigating a kitchen floor is solving a harder real-time control problem than most theorem provers ever face. This idea comes from Rodney Brooks, and it underpins the entire lecture.

### Three Key Ideas from Embodied AI

1. **Situated reasoning** -- the robot reasons about its specific situation, not abstract possibilities. "Is there an obstacle 30cm ahead?" beats "What is the optimal path through all possible obstacle configurations?"

2. **Layered control** -- instead of one monolithic planner, stack simple behavior layers that run in parallel. Each layer is dumb on its own; together they produce competent behavior.

3. **Environment-specific shortcuts** -- if you know the environment, exploit it. Do not solve the general case when a special case is easier.

These three ideas recur through every robot example in the lecture.

---

## Brooks' Philosophy: "Elephants Don't Play Chess" (1990)

Before we look at specific robots, understand the philosophical position that motivated all of them.

In 1990, Rodney Brooks published a provocative paper arguing that mainstream AI had it backwards. The AI community was building chess players, theorem provers, and expert systems -- the "elite" intellectual tasks. Brooks said: look at evolution.

- Evolution spent **billions of years** producing organisms that could move, sense obstacles, find food, and survive in dynamic environments.
- Only in the last tiny sliver of evolutionary time did abstract reasoning appear.
- Yet AI researchers started with abstract reasoning and assumed locomotion and perception would be "easy add-ons."

Brooks' argument: **build upward from situated competence, not downward from elite symbolic performance.** Study how a cockroach navigates before you study how a professor reasons. The cockroach problem is arguably harder -- it requires real-time sensor processing, robust motor control, and instant adaptation to a changing world.

This is not just philosophy. It directly influenced how every robot in this lecture was designed: simple behaviors, layered control, environment-specific tricks, no grand unified planner.

> **Exam angle**: If you are asked "Why did Brooks argue that AI should study cockroaches before chess?" the answer is: evolution spent billions of years on basic sensorimotor intelligence and only moments on abstract reasoning, so robust physical behavior is the harder and more fundamental problem. AI should build upward from simple situated competence.

---

## Allen (Brooks, 1986) -- The Layered Control Demo

Allen was a small mobile robot built to demonstrate **layered control architecture** (also called subsumption architecture). This is one of the most important concepts in embodied AI.

### How Layered Control Works

Instead of one brain that plans everything, Allen had three behavior layers running simultaneously:

```
┌─────────────────────────────────────────────┐
│  Level 2: EXPLORE                           │
│  "Head toward the most wide-open space"     │
├─────────────────────────────────────────────┤
│  Level 1: WANDER                            │
│  "Pick a random direction, follow it ~10s"  │
├─────────────────────────────────────────────┤
│  Level 0: AVOID                             │
│  "Veer away from obstacles"                 │
│  Force inversely proportional to distance   │
└─────────────────────────────────────────────┘
```

**Level 0 -- Avoid**: The most basic layer. Uses distance sensors. If something is close, generate a repulsive force away from it. The closer the obstacle, the stronger the force. This runs constantly and never turns off.

**Level 1 -- Wander**: Periodically picks a random heading and follows it for about 10 seconds. This gives the robot forward motion instead of just sitting in place.

**Level 2 -- Explore**: Looks at sensor data to find the direction with the most open space and steers toward it. This gives the robot purposeful movement instead of random wandering.

### The Key Insight: Layer Combination

The forces from all three layers **combine**. If Level 2 says "go left toward open space" but Level 0 says "there is a wall on the left, veer right," the net force steers the robot into a safe compromise direction. No layer has absolute control. The result is robust wandering with obstacle avoidance and a tendency to explore -- with **no master plan, no map, no explicit goal.**

This is a toy example, but the principle is profound: you can get competent-looking behavior from layers of simple rules without any high-level planning.

> **Common Misconception**: Students sometimes think layered control means the layers take turns. They do NOT take turns. All layers run simultaneously and their outputs combine. Higher layers can suppress or modify lower layers, but the lower layers are always active as a safety net.

---

## Polly (1993, MIT AI Lab) -- Simplifying Assumptions

Polly was the first robot to navigate visually at animal-like speed (approximately 1 meter per second). It gave tours of the MIT AI Lab to visitors. This robot is a perfect example of Brooks' principle: **do not solve the hardest possible problem if the environment lets you solve an easier one.**

### The Design Principle

General-purpose computer vision -- recognizing arbitrary objects in arbitrary scenes -- was (and still is) extremely hard. Polly's designers asked: what if we do NOT need general-purpose vision? What if we design for THIS specific environment?

The MIT AI Lab had:
- Uncluttered corridors
- Uniform carpet on the floor
- Predictable corridor geometry
- Standard office layout

Polly exploited every one of these properties.

### Computational Shortcuts

**Carpet/Object Detection**: Instead of recognizing objects, Polly detected carpet. If a pixel region does NOT look like carpet, it is probably an obstacle. This is enormously simpler than "what is this object?"

**Ground-Plane Constraint**: Objects higher in the camera image are further away. This is a geometric fact about a forward-facing camera at a fixed height. Polly used this instead of computing depth from stereo vision or rangefinders.

**Corridor Geometry**: Corridors constrain where things can be. Walls are on the sides, the path is ahead, landmarks are at intersections. This drastically reduces the search space for navigation.

### Visual System Specs

- Resolution: 64 x 48 pixels (tiny by any standard)
- Frame rate: one frame every 66 milliseconds (~15 fps)
- Output: Boolean percepts -- simple yes/no answers:
  - `open-left?` -- is the left side clear?
  - `blocked?` -- is there an obstacle ahead?
  - `person-ahead?` -- is there a person in front?
  - And several others

These Boolean percepts fed directly into behavior layers (just like Allen). No complex reasoning, no object recognition, no path planning. Just: is it clear? Is something there? Act accordingly.

### Navigation

Polly stored a library of **landmark frames** -- snapshots of what key locations looked like. It used **rotational odometry** (measuring how much it had turned) and **district recognition** (matching current view to stored landmarks) to know roughly where it was.

Visitors requested tours by **waving a foot** in front of the camera (which was at floor level). Polly would detect the motion and begin its tour route.

### Why Polly Matters for the Exam

Polly demonstrates the key design principle of embodied AI: **exploit environmental constraints to simplify the problem.** If you get a question about Polly or about embodied AI design principles, this is the core idea. Do not solve general vision. Solve corridor vision.

---

## Other Brooks Robots (Brief)

The lecture mentions several other robots from Brooks' lab. You probably will not be asked about these specifically, but they reinforce the layered-control theme:

- **Squirt** -- a tiny robot that sought dark places. Layered behavior: hide in darkness, listen for noise, move toward noise source, then hide again in the nearest dark spot. Simple rules, surprisingly "intelligent" behavior.

- **Herbert** -- a robot arm on a mobile base that roamed the lab and stole empty soda cans. It found cans, picked them up, and collected them. All through layered behaviors, no explicit planning.

- **Genghis** -- a six-legged walking robot. Each leg had its own loose control loop. The legs were not tightly synchronized by a central controller -- instead, each leg followed simple rules, and coordinated walking emerged from the interaction. Genghis also followed infrared sources (warm bodies). This is a beautiful example of layered control applied to locomotion.

---

## BigDog (Boston Dynamics, DARPA)

BigDog is a quadruped robot designed for rough terrain, funded by DARPA for military applications. It is a much more complex system than Allen or Polly, but the same principles of layered control appear.

### Physical System

```
Two-stroke engine
      ↓
Hydraulic pump
      ↓
Servo valves (one per joint)
      ↓
Leg actuators (move the legs)
```

### Sensor Suite

| Sensor | What It Measures |
|---|---|
| Joint position sensors | Angle of each leg joint |
| Joint force sensors | Load on each joint |
| IMU (Inertial Measurement Unit) | Body angle and acceleration |

### Two-Level Control

**Low-level control**: Individual joint controllers. Each joint has a feedback loop: read the current position and force, compute the correction, send the command. This runs at high frequency (hundreds of Hz).

**High-level control**: Manages speed, body attitude (lean angle), and altitude (body height). Selects gaits based on terrain.

### Gaits

BigDog could switch between multiple gaits depending on terrain and speed:

- **Crawl** -- slow, always at least three legs on the ground. Most stable.
- **Walk** -- moderate speed, alternating legs.
- **Trot** -- fastest, diagonal legs move together. Least stable but most efficient.

The gait-switching logic is a higher-level controller that observes terrain conditions and selects the appropriate gait. This is layered control again: low-level joint control runs continuously, high-level gait selection runs on top of it.

### Dynamic Balancing

BigDog's most impressive feature was dynamic balancing -- maintaining stability on uneven terrain, recovering from shoves, walking on ice. This is the same class of control problem as **NEAT's cart-pole balancing task** that you studied in the evolutionary computation chapter: keep an unstable system upright by reading sensor data and making rapid corrections.

> **Exam connection**: If asked "How does BigDog's control relate to NEAT's pole-balancing?" the answer is: both are dynamic balancing problems where an unstable system must be kept upright through continuous sensor-feedback control. BigDog's IMU measures body angle just as the cart-pole task measures pole angle. The control challenge is fundamentally the same.

### Fate of BigDog

BigDog was **too loud** for military use (the two-stroke engine made it conspicuous). The project was not adopted by the military, but the technology has applications in search-and-rescue, hazardous site inspection, and mine clearing -- situations where noise does not matter but terrain capability does.

---

## Mars Rovers

The Mars rovers are embodied AI operating in the most extreme environment possible: another planet, with a communication delay of 4 to 24 minutes each way. This delay means the rover must have significant **autonomy** -- it cannot be teleoperated in real time.

### Sensor Suite

| Sensor | Purpose | Challenge |
|---|---|---|
| Stereo cameras | Build terrain map | Limited resolution, dust on lenses |
| Wheel odometers | Measure distance traveled | **Unreliable on sand** (wheels slip) |
| Inertial sensors | Measure pitch and roll | Drift over time |
| Sun position sensor | Determine heading | Only works during day |

### Engineering Conservatism

Mars rover design is extremely conservative. The rover must survive:
- Radiation (no atmosphere to shield it)
- Extreme temperature swings (-120C to +20C)
- Limited power (solar panels, later nuclear)
- No repair possible

This conservatism means the rovers use older, radiation-hardened processors and simple algorithms. They are not running state-of-the-art deep learning -- they are running carefully tested classical algorithms.

### Ingenuity Helicopter

The Ingenuity helicopter, which rode to Mars on the Perseverance rover, was planned for **5 flights** as a technology demonstration. It completed **72 flights** before its mission ended. This is a remarkable example of conservative engineering that exceeded all expectations.

---

# Part 2: AI Teams and Swarms

Now we shift from individual robots to groups of agents working together. The central question: **how do you get coordinated group behavior?**

---

## Social Animals and Collective Intelligence

The lecture opens this section with an observation about bees. Individual bees are not smart. They have tiny brains. But a bee colony shows rich, organized behavior: building complex hives, efficiently foraging over large areas, communicating food locations through dance, thermoregulating the hive.

The intelligence is in the **collective**, not the individual. This is the biological inspiration for multi-agent AI: can we build systems where the group is smarter than any individual member?

---

## Joint Reasoning -- Tambe (1997)

Before we get to the elegant solutions, let's look at a failed approach to understand why it fails.

Tambe (1997) studied **classical AI planning with distributed agents** -- specifically, a team of attack helicopters on a military mission. Each helicopter had a role (scout, attacker, reserve), and the team followed a detailed plan.

### The Problem: Brittle Team Plans

What happens when the scout helicopter is destroyed? In the original system, the other helicopters **wait forever** for the scout's report. The plan said "wait for scout data," so they wait. Nobody adapts. The mission fails.

The obvious fix: add a rule "if scout is destroyed, skip to phase 2." But then what if the attacker is destroyed? Add another rule. What if communication is jammed? Another rule. What if two things go wrong simultaneously? More rules.

This is called **ad hoc patching** -- adding special-case handlers for every possible failure. The patches proliferate, the system becomes complex and fragile, and you can never cover every case.

> **Core problem**: the agents were committed to a PLAN, not to a GOAL. When the plan broke, they had no way to reason about what to do next.

---

## STEAM: Shell for TEAMwork

STEAM is the solution to the brittle team plan problem. It was a framework developed to make multi-agent teamwork robust.

### The Core Idea: Joint Persistent Goal (JPG)

Instead of committing to a specific plan, the team commits to a **Joint Persistent Goal**. The team keeps pursuing the goal unless one of three conditions is met:

| Condition | Meaning | Example |
|---|---|---|
| **Achieved** | The goal has been accomplished | "We destroyed the target" |
| **Unachievable** | The goal is now impossible | "The target was already evacuated" |
| **Irrelevant** | The goal no longer matters | "The war ended, mission cancelled" |

These three conditions (A, U, I) are the only reasons to stop pursuing a goal.

### The Communication Rule

Here is the crucial part, and this is what makes STEAM different from ad hoc patching:

**If one agent concludes that the goal is Achieved, Unachievable, or Irrelevant, it must COMMUNICATE this to the team before exiting.**

The agent does NOT just fly home. It tells its teammates WHY it is stopping.

### A Concrete Example

A team of helicopters is on a strike mission. One helicopter discovers a surface-to-air missile battery, making the mission unachievable (they would be shot down).

**Without STEAM**: The discovering helicopter turns around and flies home. The other helicopters continue the mission and get shot down. Disaster.

**With STEAM**: The discovering helicopter broadcasts "Mission unachievable -- SAM battery detected at coordinates X." All team members receive this, independently verify that the goal is now unachievable, and abort together.

The key insight: **STEAM is a commitment to COMMUNICATE, not just a commitment to act.** The contract between teammates is: if you learn something that changes the goal status, you MUST share it.

> **Exam answer**: If asked "What is a JPG in STEAM?" -- A Joint Persistent Goal is a shared commitment by a team to pursue a goal until it is achieved, becomes unachievable, or becomes irrelevant. If any agent determines one of these conditions holds, it must communicate this to the team before withdrawing.

---

## Flocking and Boids

Now we go from deliberate planning (STEAM) to emergent behavior (flocking). This is a fundamentally different approach to multi-agent coordination.

### The Phenomenon

Watch a murmuration of starlings -- thousands of birds swooping, turning, and flowing as a single mass. There is no leader. No bird is "in charge." Yet the group moves with stunning coordination.

How?

### Reynolds' Three Rules (1987)

Craig Reynolds showed that you can reproduce realistic flocking with just **three simple rules** applied to each individual agent (which he called "boids" -- bird-droids):

**Rule 1 -- Collision Avoidance (Separation)**
> Do not come too close to your neighbors.
Each boid steers away from any neighbor that is within a minimum separation distance.

**Rule 2 -- Flock Centering (Cohesion)**
> Stay close to the group.
Each boid steers toward the average position of its neighbors.

**Rule 3 -- Velocity Matching (Alignment)**
> Match speed and direction with your neighbors.
Each boid adjusts its velocity to match the average velocity of nearby boids.

That is it. Three rules. No leader, no global plan, no communication beyond observing your neighbors.

### Why This Matters: Emergence

The stunning thing about boids is that complex, coordinated, beautiful group behavior **emerges** from simple local rules. No individual boid knows about the flock as a whole. Each boid only looks at its nearest neighbors. Yet the global pattern -- the swooping murmuration -- appears as if by magic.

This is **agent-based modeling**: define simple rules for individuals, simulate their interactions, and observe what global behavior emerges. It is the opposite of top-down design.

### Implementation Details

The boids simulation uses:

**5 Parameters:**

| Parameter | What It Controls |
|---|---|
| Field of view | How far each boid can see |
| Minimum separation | How close is "too close" (Rule 1) |
| Cohesion threshold | How far is "too far from the group" (Rule 2) |
| Maximum speed | Upper bound on boid velocity |
| Maximum rotation | How fast a boid can turn |

**3 Agent Attributes:**
- Heading (current direction)
- Speed (current velocity magnitude)
- Nearest-neighbor list (which boids are visible)

Each time step, every boid:
1. Looks at its neighbors
2. Computes forces from all three rules
3. Combines the forces into a new heading and speed
4. Moves

This is computationally cheap and scales well because each boid only needs to check its local neighborhood, not the entire flock.

> **Exam answer**: If asked "State Reynolds' three rules for flocking and what emergent behavior they produce" -- (1) Collision avoidance: steer away from neighbors that are too close. (2) Flock centering: steer toward the average position of neighbors. (3) Velocity matching: align speed and direction with neighbors. Together, these local rules produce realistic flocking behavior -- coherent group movement, smooth turns, and splitting/merging around obstacles -- without any central controller or global plan.

---

## Robot Soccer (THE Exam Question)

This is the section that directly answers the recurring exam question. Read it until you can write the answer in your sleep.

### Why Robot Soccer?

Robot soccer is the natural testbed for embodied multi-agent AI because it combines almost every challenge in one scenario:

- **Perception**: Where is the ball? Where are teammates and opponents?
- **Locomotion**: Move to the right position quickly
- **Real-time decision-making**: The game does not pause
- **Coordination**: Work with teammates toward a shared goal
- **Strategy**: Adapt to the opponent's behavior
- **Adversarial environment**: The other team is actively working against you

### Coordination Depends on the Rules

Different robot soccer leagues have different rules about perception and communication, and the available strategies depend heavily on these rules:

| Rule Variant | Effect on Strategy |
|---|---|
| Shared overhead camera | All robots know everything -- enables implicit coordination |
| WiFi data sharing allowed | Robots can exchange plans explicitly |
| Local cameras only | Each robot sees only its own view -- limited coordination |
| Body signals only (no radio) | Coordination through gestures/movements |

**The exam question always specifies**: overhead camera (shared perception), no communication signals allowed. This combination is what makes implicit coordination possible.

### Perception Can Be Very Limited

In leagues with local cameras only, perception is severely constrained:
- Narrow field of view (like looking through a toilet paper tube)
- Unstable camera platforms (the robot is moving, so the image shakes)
- Self-occlusion (the robot's own body blocks part of the view)

This is why the overhead camera variant is so interesting: it removes the perception problem entirely and lets you focus on the coordination problem.

---

## The Exam Question: Setup and Deep Understanding

### The Exact Scenario (paraphrased from 3/4 tests)

> A robot soccer league where all robots can access an **overhead camera view** of the field. They know the positions of all teammates, all opponents, and the ball. However, they **cannot send signals** to teammates. Describe one strategy or collective behaviour that can be effective under these conditions.

### Why Coordination Works Without Communication

This is the conceptual core. Think about a basketball team where all five players can see the entire court. Nobody needs to shout "I am open!" if everyone can SEE who is open. Each player independently reads the situation and acts.

The logic:

```
SAME INPUT (all robots see the same overhead view)
     ↓
SAME ALGORITHM (all robots run the same strategy code)
     ↓
SAME CONCLUSIONS (all robots agree on what to do)
     ↓
COORDINATED ACTION (no communication needed)
```

This is **implicit coordination**: coordination that emerges from shared perception and shared reasoning, without any explicit message exchange.

**Why it works formally**: If every robot has function f(state) that maps the game state to an action, and every robot observes the same state, then every robot computes the same action assignment. The passer knows where to pass because the receiver knows where to run -- both computed the answer from the same data.

The lecture slide makes this point explicitly: **"Position- and role-based methods work best when teammates perceive the situation in a sufficiently similar way."** The overhead camera guarantees identical perception. That is the enabler.

---

## Three Strategies (Any ONE Scores Full Marks)

### Strategy 1: Collective Passing Behaviour

**How it works:**

1. Every robot sees the full field via the overhead camera.
2. Each robot independently identifies **candidate passing points** -- locations where a pass could be received.
3. For each candidate point, the robot evaluates:
   - Distance to nearest teammate (can someone get there?)
   - **Interception risk** (are opponents positioned to steal the pass?)
   - Goal proximity (does this pass advance toward scoring?)
   - Angle quality (is there a clear passing lane?)
4. Each passing point gets a **value score** combining these factors.
5. The robot with the ball selects the highest-value point and passes there.
6. The intended receiver -- who computed the SAME scores from the SAME data -- knows this is the best point and moves to receive.

**Why no communication is needed**: Both passer and receiver ran the same evaluation on the same input. They independently arrived at the same "best passing point."

**Mini-example:**

```
Field snapshot:
  Robot A (has ball) ---- center field
  Robot B (teammate) ---- left wing, open
  Robot C (teammate) ---- right wing, blocked by Opponent X

Both A and B independently compute:
  Pass to right wing: HIGH interception risk (Opponent X)
  Pass to left wing:  LOW interception risk, good goal angle
  → Best pass: left wing

Robot A passes left. Robot B runs to receive. No message needed.
```

### Strategy 2: Positioning / Formation Strategy

**How it works:**

1. Each robot independently assesses the game state:
   - Are we attacking or defending?
   - Where is the ball relative to our goal?
   - Where are teammates and opponents clustered?
2. Based on this assessment, each robot computes the optimal **formation**:
   - Ball near opponent's goal → attacking formation (3 forwards, 1 defender)
   - Ball near our goal → defensive formation (1 forward, 3 defenders)
3. Each robot picks the formation slot closest to its current position (minimizing wasted movement).
4. As the game state changes, formations update dynamically.

**Why no communication is needed**: Formation choice is a deterministic function of game state. Same input, same output. Every robot converges on the same formation.

### Strategy 3: Role-Based Strategy

**How it works:**

1. Each robot independently assigns roles based on positions:
   - **Goalkeeper**: robot closest to own goal
   - **Attacker**: robot closest to the ball
   - **Support**: remaining robots take midfield positions
2. Roles reassign dynamically as positions change.

**Why no communication is needed**: "Closest to the ball" and "closest to own goal" are objective facts visible to everyone. Every robot computes the same role assignments.

```
Current positions:
  Robot 1: near own goal    → GOALKEEPER
  Robot 2: near ball        → ATTACKER
  Robot 3: midfield         → MIDFIELDER
  Robot 4: near opponent goal → FORWARD SUPPORT

All four robots compute these same assignments independently.
```

### Summary Table

| Strategy | Core Mechanism | Why It Works Without Communication |
|---|---|---|
| Collective passing | Evaluate passing points by value score | All robots compute same scores from same camera data |
| Formation positioning | Choose formation based on game state | Same state → same formation for all robots |
| Role assignment | Assign roles by relative positions | Positional facts are objective and shared |

---

## Model Exam Answers (Each Scores 2/2)

The exam gives 2 marks. You need to describe ONE strategy clearly. Here are three standalone answers. Memorize your favorite.

### Model Answer A (Passing)

> One effective collective behaviour is a **passing strategy**. Each robot uses the overhead camera to identify candidate passing points on the field. For each candidate, the robot evaluates interception risk, distance to teammates, and goal proximity. Because all robots compute these same evaluations from the same shared view, the passer and receiver independently agree on the best passing point -- enabling coordinated passing without explicit communication.

### Model Answer B (Formation)

> An effective strategy is **formation-based positioning**. Each robot independently assesses the game situation (ball position, teammate and opponent locations) and computes an optimal team formation -- shifting to attack when the ball is near the opponent's goal, or defense when it is near their own. Since all robots see the same overhead view and apply the same logic, they converge on the same formation positions without needing to communicate.

### Model Answer C (Roles)

> A useful collective behaviour is **implicit role assignment**. Each robot independently assigns roles based on the shared overhead view -- the robot closest to the ball becomes the attacker, the one nearest the home goal becomes goalkeeper, and others take support positions. Because role assignment is based on objective positional data visible to all robots, each robot arrives at the same allocation independently.

---

# Deeper Understanding: Questions a Tutor Would Ask

## "What if robots had different camera views?"

If each robot only saw its local surroundings (no overhead camera):

- **Implicit coordination breaks down** -- different inputs mean different conclusions
- Robots would need **explicit communication** to share observations
- Strategies would shift to local behaviors: "follow the ball," "patrol a zone"
- This is the difference between **centralized perception** (shared camera) and **decentralized perception** (local sensors)

## "What if robots COULD communicate?"

Communication enables additional strategies:
- **Explicit play-calling**: "I will pass to position X at time T"
- **Negotiation**: robots bid for roles and resolve conflicts
- **Information sharing**: detailed observations about opponent behavior
- **Sequential planning**: multi-step coordinated plays

Communication adds flexibility but also complexity (message delays, bandwidth limits, message conflicts). Implicit coordination is simpler and more robust when shared perception is available.

## "How does this connect to STEAM?"

STEAM and robot soccer represent two different approaches to multi-agent coordination:

| Aspect | STEAM | Robot Soccer (implicit) |
|---|---|---|
| Coordination type | Explicit (communicate goals) | Implicit (shared perception) |
| Communication | Required -- must announce goal status | Forbidden in the exam scenario |
| Plan robustness | Robust through JPG commitment | Robust through shared computation |
| Failure handling | Communicate A/U/I conditions | Re-compute from current state |

## "How does this connect to boids?"

Both boids and robot soccer produce coordinated group behavior, but through different mechanisms:

- **Boids**: each agent follows local rules with no global information. Coordination is emergent.
- **Robot soccer (overhead camera)**: each agent has global information and computes the globally optimal action. Coordination is computed.
- **Boids**: no agent knows about the flock as a whole. **Robot soccer**: every agent knows the full game state.

---

# Practice Problems

## Problem 1 (2 marks)
**What is layered control? Use Allen's robot as an example.**

*Think before reading the answer framework.*

> **Answer framework**: Layered control is an architecture where multiple behavior layers run simultaneously and combine their outputs. Allen had three layers: Level 0 (Avoid) generated repulsive forces from obstacles, Level 1 (Wander) picked random directions, Level 2 (Explore) steered toward open space. All layers ran in parallel and their forces combined, producing competent navigation without any explicit planning.

---

## Problem 2 (1 mark)
**What design principle did Polly demonstrate for embodied AI?**

> **Answer framework**: Polly demonstrated that you should exploit environmental constraints to simplify perception. Rather than solving general computer vision, Polly used the specific properties of its environment (uniform carpet, corridor geometry, predictable layout) to reduce vision to simple Boolean percepts like "is there carpet?" and "is the left side open?"

---

## Problem 3 (3 marks)
**State Reynolds' three rules for flocking. What emergent behavior do they produce?**

> **Answer framework**: (1) Collision avoidance (separation) -- steer away from neighbors that are too close. (2) Flock centering (cohesion) -- steer toward the average position of nearby neighbors. (3) Velocity matching (alignment) -- adjust speed and direction to match nearby neighbors. These three local rules, applied by each individual boid with no central controller, produce realistic flocking behavior: coherent group movement, smooth coordinated turns, and natural splitting and merging around obstacles. This is an example of emergence -- complex global behavior arising from simple local interactions.

---

## Problem 4 (2 marks)
**What is a Joint Persistent Goal in STEAM? Why must agents communicate when exiting a JPG?**

> **Answer framework**: A JPG is a shared team commitment to pursue a goal until it is achieved, becomes unachievable, or becomes irrelevant. Agents must communicate when they determine one of these conditions holds because otherwise teammates will continue pursuing the goal under false assumptions. For example, if one agent discovers the goal is unachievable but does not inform the team, other agents may waste resources or put themselves in danger continuing a futile mission.

---

## Problem 5 (2 marks -- THE exam question, 3 valid answers)
**In robot soccer with overhead camera but no communication, describe one effective strategy.**

> **Answer option A**: Collective passing -- each robot evaluates candidate passing points using interception risk and goal proximity. Since all robots compute the same evaluations from the same camera data, passer and receiver independently agree on the best passing point.
>
> **Answer option B**: Formation positioning -- each robot computes an optimal formation (attack or defense) based on ball position and player locations. Same game state and same algorithm produces the same formation for all robots.
>
> **Answer option C**: Role assignment -- each robot assigns roles (attacker, goalkeeper, support) based on relative positions. Since "closest to ball" is an objective fact visible to all robots, everyone computes the same assignments.

---

## Problem 6 (2 marks)
**Why did Brooks argue that AI should study cockroaches before chess?**

> **Answer framework**: Brooks argued that evolution spent billions of years developing organisms with basic sensorimotor intelligence -- locomotion, obstacle avoidance, foraging -- before abstract reasoning appeared in the last evolutionary instant. This suggests that robust physical behavior in a dynamic environment is the harder and more fundamental problem. AI should build upward from simple situated competence rather than starting with elite symbolic tasks like chess and theorem proving, which represent a tiny fraction of what intelligence actually involves.

---

## Problem 7 (1 mark)
**How does BigDog's control system relate to NEAT's pole-balancing task?**

> **Answer framework**: Both are dynamic balancing problems. BigDog must keep an unstable quadruped body upright on rough terrain by reading IMU sensor data and adjusting joint actuators in real time, just as the pole-balancing task requires reading the pole's angle and adjusting the cart's position to prevent the pole from falling. The fundamental control challenge -- stabilize an inherently unstable system through continuous sensor-feedback correction -- is the same.

---

# Key Vocabulary

| Term | Definition |
|---|---|
| Embodied AI | AI that controls a physical body, sensing and acting in the real world |
| Layered Control (Subsumption) | Architecture where multiple behavior layers run simultaneously and combine outputs; lower layers handle basic survival, higher layers add goals |
| Situated Reasoning | Reasoning about the agent's specific current situation rather than abstract possibilities |
| Simplifying Assumptions | Exploiting known properties of the environment to reduce computational complexity (Polly's principle) |
| Joint Persistent Goal (JPG) | A shared team commitment to pursue a goal until it is achieved, unachievable, or irrelevant |
| STEAM | Shell for TEAMwork -- framework enforcing JPGs and mandatory communication on goal-status changes |
| Boids | Reynolds' simulated bird-droids that demonstrate emergent flocking from three local rules |
| Emergence | Complex global behavior arising from simple local interactions with no central controller |
| Agent-Based Modeling | Defining simple rules for individuals and observing what group behavior emerges |
| Implicit Coordination | Coordination achieved through shared perception and shared reasoning, without explicit communication |
| Explicit Coordination | Coordination through direct communication between agents |
| Centralized Perception | All agents share the same global view (e.g., overhead camera) |
| Decentralized Perception | Each agent has only a local view from its own sensors |

---

# Common Mistakes on This Topic

1. **Describing a strategy that requires communication** -- the exam question explicitly says robots CANNOT send signals. Do not describe radio-based or message-passing strategies.

2. **Forgetting to explain WHY the strategy works without communication** -- always connect back to the shared overhead camera. The marker wants to see that you understand implicit coordination, not just the strategy name.

3. **Being too vague** -- do not just say "robots work together." Describe the specific mechanism (passing point evaluation, formation computation, or role assignment).

4. **Confusing "no communication" with "no coordination"** -- the whole point is that coordination IS possible without communication, given shared perception.

5. **Saying boids have a leader** -- there is no leader in flocking. The behavior is entirely emergent from local rules.

6. **Saying Allen's layers take turns** -- all layers run simultaneously and their outputs combine. This is not sequential processing.

7. **Forgetting STEAM's communication requirement** -- the whole point of STEAM is that agents MUST communicate when exiting a JPG. An agent that just leaves without telling the team defeats the purpose.

8. **Over-writing for 2 marks** -- the robot soccer question is 2 marks. Write 3-5 clear sentences, not an essay. State the strategy, explain the mechanism, connect to shared perception. Done.

---

# Self-Check Checklist

- [ ] Can you name the three layers of Allen's control architecture and what each does?
- [ ] Can you state Polly's key design principle in one sentence?
- [ ] Can you explain Brooks' "Elephants Don't Play Chess" argument?
- [ ] Can you state Reynolds' three flocking rules from memory?
- [ ] Can you define emergence and give boids as an example?
- [ ] Can you explain what a JPG is and why STEAM requires communication?
- [ ] Can you describe at least 2 robot soccer strategies from memory?
- [ ] Can you write a complete 2-mark robot soccer answer in under 2 minutes?
- [ ] Can you explain what would change if robots had local-only perception?
- [ ] Can you connect BigDog's balancing to NEAT's pole-balancing task?
- [ ] Can you explain the difference between implicit and explicit coordination?
