# Embodied AI, Multi-Agent Systems & Collective Behaviour

## 🎯 Exam Importance

🟠 **高频** | Week 6 Lecture 12 (33 slides) | Covers embodied robots, layered control, flocking, teamwork, robot soccer

> **Exam track record:**
> - S1 2025/2026 Sample Q4 (2m): Robot soccer with overhead camera, no communication — name a coordination strategy
> - S1 2025 Actual Q6 (3m): Design fitness function for BigDog walking robot (cross-topic with NEAT)
> - S1 2024 Final Q6: NEAT for mobile robot — related to embodied AI concepts
>
> The professor tests: (1) specific robot knowledge (Polly, Allen, BigDog), (2) flocking rules, (3) robot soccer strategies, and (4) fitness function design for embodied agents.

---

## 📖 Core Concepts

| English Term | 中文 | One-line Definition |
|---|---|---|
| Embodied AI（具身智能） | 具身人工智能 | AI systems with a physical body that react to sensors in real time |
| Situated Reasoning（情境推理） | 情境推理 | Reasoning that exploits the specific environment rather than solving the general case |
| Layered Control（分层控制） | 分层控制 | Architecture where multiple behavior layers run in parallel; their outputs are combined |
| Subsumption Architecture（包容式架构） | 包容式架构 | Brooks' architecture where higher layers can override (subsume) lower ones |
| Simplifying Assumptions（简化假设） | 简化假设 | Exploiting environmental constraints to avoid solving the hardest possible problem |
| Ground-Plane Constraint（地平面约束） | 地平面约束 | Objects on a flat floor appear higher in the image when farther away — depth from a single camera |
| Joint Persistent Goal / JPG（联合持续目标） | 联合持续目标 | A shared goal that team members keep pursuing until Achieved, Unachievable, or Irrelevant |
| STEAM (Shell for TEAMwork) | 团队协作框架 | Tambe's framework for multi-agent teamwork based on JPGs and communication commitments |
| Flocking / Boids（群集行为） | 群集行为 | Emergent collective motion from simple local rules (Reynolds, 1987) |
| Emergence（涌现） | 涌现 | Complex global patterns arising from simple local interactions with no central controller |
| Agent-Based Modelling（基于智能体的建模） | 基于智能体建模 | Simulating systems where global behavior emerges from individual agents following local rules |
| Dynamic Balancing（动态平衡） | 动态平衡 | Continuous real-time control to keep a robot upright while moving |
| Recurrent Connection（循环连接） | 循环连接 | A connection that feeds output back as input, enabling memory of past states |
| Collective Behaviours（集体行为） | 集体行为 | Coordinated team plays (e.g., passing strategies) |
| Positioning Strategies（位置策略） | 位置策略 | Formation-based coverage of the playing field |
| Role-Based Strategies（角色分配） | 角色分配 | Dynamic assignment of roles (attacker, defender, goalie) based on game state |

---

## 🧠 Feynman Draft — Part 1: Embodied AI

### What is Embodied AI?

Imagine you are trying to catch a ball. You don't sit down with a physics textbook, compute the parabolic trajectory, and plan your arm movements. You just *react* — your eyes track the ball, your body adjusts, and your hand reaches out. You use shortcuts: "the ball is getting bigger, so it's coming closer."

That is the core idea of **Embodied AI**: intelligence is not just abstract reasoning inside a computer. It is about **acting robustly in the physical world** — having a body with sensors and actuators, dealing with real-time constraints, and exploiting **environmental shortcuts** instead of solving the hardest general problem.

> Brooks (1990), in his famous paper "Elephants Don't Play Chess," argued: intelligence does NOT start with chess and theorem provers. Evolution spent **billions of years** on simple life forms (bacteria, cockroaches, rats) before complex intelligence appeared. Human-level intelligence has only existed for ~1 million years. So AI should study **simple intelligent behavior** first: locomotion, obstacle avoidance, social coordination.
>
> The broader message: **build upward from situated competence**, not downward from elite symbolic performance.

Three key principles of Embodied AI from the lectures:
1. **Situated reasoning** — exploit the specific environment, don't solve the general case
2. **Layered control** — multiple simple behaviors running in parallel, combined into complex behavior
3. **Environment-specific shortcuts** — use the physical world's structure to simplify computation

### Polly — The First Visually Navigated Robot at Animal Speed (Horswill, 1993)

Polly was a landmark robot: the first to navigate using vision at roughly **animal speed (~1 m/s)**, back in 1993. It served as a tour guide on MIT AI Lab's 7th floor.

**The core design principle:** "Don't solve the hardest possible vision problem if the environment gives you shortcuts."

#### Polly's Three Simplifying Assumptions

| Assumption | How It Works | What It Avoids |
|---|---|---|
| **Uncluttered office environment** | Corridors with uniform, un-patterned carpet | No need for general object recognition |
| **Carpet = safe, pattern = obstacle** | If the camera sees texture/patterns on the ground, it's an obstacle. Smooth carpet = navigable space | No need for 3D object detection |
| **Ground-plane constraint** | Objects rest on the flat floor, so things appearing **higher in the image** are **farther away** | No need for stereo cameras or depth sensors — depth from a single 2D camera! |
| **Corridor geometry** | Narrow corridors constrain where landmarks can appear, reducing the visual search space | No need for full 360-degree scene analysis |

**Visual system details:**
- Captured **64 x 48 pixel images** every **66 ms** (about 15 fps) — extremely low resolution, but cheap to compute
- Produced **Boolean precepts**: `open-left?`, `blocked?`, `wall-ahead?`, `vanishing-point`, etc.
- Used height-in-image as a proxy for depth (ground-plane constraint)

**Navigation system:**
- **Frame library**: Stored records of how landmarks looked from different directions and distances
- **Rotational odometry**: Tracked how much Polly had turned left and right (rough estimate)
- **District recognition**: Identified which corridor/area it was in to recover localization
  - Example: "I'm going east and see a left turn ahead → I must be in the southern corridor"
- Visitors requested a tour by **waving a foot** (camera looked at foot level)

> Navigation was **appearance-based and pragmatic** — no full symbolic world model, no complex SLAM algorithm. Just pattern matching against stored views plus environmental shortcuts.

### Allen — Layered Control (Brooks, 1986)

Allen was Brooks' robot that demonstrated the **layered control architecture** using sonar sensors. This is one of the most important concepts in this chapter.

#### The Three Layers

| Layer | Name | Behavior | Description |
|---|---|---|---|
| **Level 0** | **Avoid** | Obstacle avoidance | Generates a **repulsive force** away from nearby obstacles. Force is scaled with inverse-square distance (1/d²). The closer the obstacle, the stronger the avoidance force. |
| **Level 1** | **Wander** | Random exploration | Picks a **random direction** and follows it for approximately **10 seconds**, then picks a new random direction. |
| **Level 2** | **Explore** | Directed movement | Steers toward **wide-open space** detected by sonar. Heads where there is room to move. |

#### How the layers combine

```
┌─────────────────────────────────────────┐
│ Level 2: EXPLORE                        │
│   → force toward open space             │
├─────────────────────────────────────────┤
│ Level 1: WANDER                         │
│   → force in random direction (~10s)    │
├─────────────────────────────────────────┤
│ Level 0: AVOID                          │
│   → repulsive force from obstacles (1/d²)│
└─────────────────────────────────────────┘
         ↓  All forces COMBINED  ↓
        [Final heading & speed]
```

**Critical points:**
- All three levels run **simultaneously** (not sequentially!)
- Their forces are **summed/combined** to produce the final direction
- There is **no master plan**, no rich knowledge base, no symbolic reasoning
- Result: robust wandering behavior with very simple programming
- The robot appears "intelligent" even though each layer is trivially simple — this is a form of **emergence**

### Other Brooks Robots

**Squirt** (smallest robot):
- One cubic inch — tiny!
- Sought dark places and sat still in corners
- Upper behavior: after a loud noise, stay still, then move toward the noise source
- Lower behavior kicks in: hides again, but now closer to "where the action is"
- Demonstrates: simple behaviors layered together produce seemingly purposeful behavior

**Herbert**:
- Had a robotic arm
- Programmed to **steal empty soda cans** from people's desks
- No complex planning — just sensor-driven can detection and grasping

**Genghis**:
- **Six-legged** walking robot
- Legs were NOT explicitly coordinated — each leg had its own simple controller
- **Loose leg coordination**: legs operated semi-independently, yet the robot scrambled around effectively
- Also followed infrared sources
- Demonstrates: coordination can emerge from independent simple controllers

### BigDog — Rough-Terrain Quadruped (Boston Dynamics, 2008)

BigDog is one of the most famous legged robots, designed to traverse **rough terrain** that wheeled robots cannot handle.

#### Physical Specifications

| Attribute | Value |
|---|---|
| Mass | ~**109 kg** |
| Engine | Two-stroke water-cooled internal combustion |
| Power transmission | Engine → hydraulic pump → high-pressure oil → servo valves → hydraulic cylinders |
| Leg actuators | Hydraulic cylinders at each joint |
| Sensors | Joint position sensors, force sensors, inertial sensors (body angle & acceleration) |
| Computer | Onboard, running two-level control system |

#### Two-Level Control Architecture

```
HIGH-LEVEL CONTROLLER
├── Regulates body speed (match target speed)
├── Controls attitude: pitch, yaw, roll (keep body stable)
├── Selects gait: crawl / walk / trot
│   - Trot for speed on flat ground
│   - Crawl for steep or slippery surfaces
└── Adapts to terrain (adjusts torso pitch for climbing/descending)

LOW-LEVEL CONTROLLER
├── Manages individual joint positions
├── Controls joint forces
└── Directs ground reaction forces toward hip
```

#### Gaits

| Gait | When Used |
|---|---|
| **Crawl** | Steep, slippery, or unstable ground (most stable, slowest) |
| **Walk** | Moderate terrain |
| **Trot** | Flat ground, need for speed (least stable, fastest) |

**Dynamic balancing**: BigDog must continuously adjust its legs in real time to stay upright — this is directly analogous to the **double pole balancing** task in NEAT. Learning-based algorithms (like those evolved by NEAT) can be trained for this kind of control.

**Fate of BigDog**: The prototype was **extremely loud** (the two-stroke engine), so the military lost interest. However, the technology remains promising for:
- Search-and-rescue operations
- Hazardous-site inspection
- Mine clearing

### Mars Rovers — Autonomous Control Under Extreme Constraints

Mars rovers represent embodied AI under the **harshest constraints** — they must operate autonomously because of **communication delay** (signals take minutes to travel between Mars and Earth).

#### Sensing and Navigation

| Sensor | Purpose |
|---|---|
| **Stereo cameras** | Build terrain maps, estimate depth |
| **Wheel odometers** | Estimate distance traveled (unreliable on sand — wheels slip) |
| **Inertial sensors** | Estimate pitch and roll of the rover body |
| **Sun position + time** | Estimate heading direction |

The rover can:
- **Plan a path** through rocky terrain
- **Adapt dynamically** to unexpected obstacles
- **Respect human-labeled no-go areas** (dangerous zones marked by mission control)

#### Space Travel Constraints

| Constraint | Why It Matters |
|---|---|
| **Radiation** | Electronics must survive cosmic radiation — limits chip choice |
| **Extreme temperature** | Mars surface: -125C to 20C — hardware must be robust |
| **Power** | Solar panels; dust accumulation can end the mission |
| **Speed** | Rovers move VERY slowly — tipping over would be catastrophic (no mechanic on Mars) |
| **Communication delay** | Minutes per signal round-trip — rover must be autonomous between commands |

**Ingenuity Helicopter**: Originally planned for just **5 flights** as a technology demonstration. Actually completed **72 flights** before its mission ended. A remarkable example of conservative engineering yielding far beyond expectations.

> Mars rovers repeat the same theme as all embodied AI: **physical body + clever approximations under constraints**. Just like Polly used a 64x48 camera with ground-plane constraint, rovers use conservative movement with autonomous path planning.

⚠️ **Common Misconception**: Students think embodied AI requires sophisticated reasoning (complex world models, deep learning). Actually, the key insight is that **environment-specific shortcuts** can replace complex computation. Polly navigated effectively with a 64x48 pixel camera because it exploited the ground-plane constraint and carpet detection. Allen behaved "intelligently" with just three simple behavior layers and no master plan.

💡 **Core Intuition (Part 1)**: Embodied AI succeeds by **exploiting environmental structure** rather than solving the general problem. Intelligence is about acting robustly in the world, not just reasoning abstractly.

---

## 🧠 Feynman Draft — Part 2: AI Teams & Swarms

### From Single Robots to Teams

Once individual robots can navigate and act, the next question is: **can they work together?** This section covers three approaches: joint reasoning (STEAM), emergent behavior (flocking), and structured coordination (robot soccer).

### Joint Reasoning — Tambe (1997) and STEAM

Tambe studied how to plan with a **physically distributed team** of agents. The motivating domain: a squadron of **attack helicopters** on a military mission.

**The problem with brittle plans:**

Imagine a team plan: "Scout flies ahead → reports all-clear → rest of team advances." What if the scout is **destroyed**? The other helicopters wait forever for the all-clear signal. The mission fails.

You might add a patch: "If scout doesn't report in 5 minutes, assume it's destroyed." But what if the scout is just delayed by bad weather? Adding one ad hoc rule may fix one failure, but **other failures remain hidden**, and the patches proliferate until the system is unmaintainable.

**STEAM (Shell for TEAMwork) — the principled solution:**

STEAM introduced the concept of a **Joint Persistent Goal (JPG)**:

- All team members **pursue the goal** until one of three things happens:
  - **A (Achieved)** — the goal is accomplished
  - **U (Unachievable)** — the goal becomes impossible
  - **I (Irrelevant)** — the goal no longer matters

- **The key rule**: If any one agent **privately concludes** A, U, or I, it does NOT simply act on that conclusion alone. Instead, it **must inform the entire team** so they can form a **new mutual belief**.

- STEAM is fundamentally a commitment to **communicate**, not just to act.

**Concrete example:**

> A helicopter team is attacking an enemy base. One helicopter detects a **surface-to-air missile battery** — the mission is now **Unachievable** (too dangerous). The correct behavior under STEAM:
>
> - The helicopter concludes U (Unachievable)
> - It does NOT simply fly home alone (that would leave teammates in danger)
> - It **informs the team**: "Mission is unachievable — SAM battery detected"
> - The team forms a new mutual belief and either retreats together or adjusts the plan

Without STEAM's communication commitment, one agent flying home while others continue = catastrophic coordination failure.

### "Elephants Don't Play Chess" — Brooks (1990)

This is one of the most famous papers in AI, and the professor has directly referenced it in lectures.

**Brooks' argument:**
- Traditional AI focused on **high-level reasoning**: chess, theorem proving, expert systems
- But intelligence didn't start there in evolution
- Evolution spent **billions of years** on simple organisms (bacteria, insects, fish)
- The **Cambrian Explosion** (~500 million years ago) produced larger animals
- **Human-level intelligence** is only ~1 million years old
- Therefore: AI should study **simple intelligent behavior** first — cockroaches navigating, ants coordinating, rats exploring
- **Build upward from situated competence**, not downward from elite symbolic performance

This philosophy directly inspired the layered control architecture (Allen), the Brooks robots (Squirt, Herbert, Genghis), and the idea that complex behavior can emerge from simple local rules (flocking).

### Flocking — Reynolds' Three Rules (1987)

How do thousands of starlings create mesmerizing murmuration patterns with **no central controller**? Craig Reynolds proposed that the answer is just **three simple local rules**:

| Rule | Name | Description |
|---|---|---|
| **R1** | **Collision Avoidance** (Separation) | Do NOT come within a **minimum distance** of nearby flockmates. If too close, steer away. |
| **R2** | **Flock Centering** (Cohesion) | Stay close to the group — steer toward the **average position** of nearby flockmates. Don't drift away. |
| **R3** | **Velocity Matching** (Alignment) | Align your **speed and direction** with nearby agents. Match their heading. |

**Key insight**: Each agent only follows these three rules based on **local information** (what it can see nearby). There is no central controller, no master plan, no global communication. Yet the result is **realistic flocking behavior** — a stunning example of **emergence**.

This is a form of **agent-based modelling**: global behavior emerges from local interactions. The same principle appears in:
- Epidemiology (disease spread from local contact)
- Economics (market patterns from individual trades)
- Social networks (opinion cascades from local influence)

### "Boids" Simulator (Reynolds' Implementation)

Reynolds built a simulator called **Boids** (bird-droids) to demonstrate his rules:

- Just the three rules produce striking, realistic flock-like behavior
- Different parameter settings produce visibly different patterns
- A clean demonstration that **emergence** is real and powerful

**Hermellin & Michel (2017) implementation details:**
- **5 parameters**: field of view, minimum separation distance, cohesion threshold, maximum speed, maximum rotation
- **3 agent attributes**: heading, speed, nearest-neighbor list
- Small implementation choices (e.g., how neighbors are detected, how forces are weighted) can **dramatically change** the emergent behavior

### Robot Soccer — Multi-Agent Coordination in Practice

Robot soccer is the ultimate testbed for embodied multi-agent AI because it combines **everything**:
- Perception (where is the ball? where are teammates? where are opponents?)
- Locomotion (walking/rolling to the right position)
- Communication (sharing information with teammates)
- Coordination (who does what?)
- Strategy (attacking, defending, passing)

#### Coordination Depends on League Rules

Different robot soccer leagues have different constraints:

| Rule Variation | Impact on Strategy |
|---|---|
| **Shared data over WiFi?** | If yes, robots can share their observations → easier coordination |
| **Overhead camera?** | If yes, all robots see the same global view → no need for individual perception |
| **Direct signaling?** | If only body signals, communication bandwidth is very limited |
| **Walking platforms?** | Unstable bipeds have narrow field of view → each robot may only maintain a rough **probabilistic model** of the game state |

#### Three Levels of Strategy (EXAM CRITICAL)

| Strategy Type | Description | Example |
|---|---|---|
| **Collective Behaviours** | Coordinated team plays requiring real-time collaboration | **Passing strategy**: evaluate candidate passing points by **interception prediction** (will an opponent intercept?), score each point by position and tactical value |
| **Positioning Strategies** | Formation-based coverage of the field | Choose formations (e.g., **2-1-2**) that balance attacking and defensive opportunities. Players move to assigned positions based on ball location |
| **Role-Based Strategies** | Dynamic assignment of roles based on current game situation | Assign roles — **goalkeeper, attacker, defender** — dynamically. More attackers when ball is near opponent's goal; more defenders when under pressure |

**Important point:** Position-based and role-based strategies work best when teammates **perceive the situation in a sufficiently similar way**. If every robot has a different understanding of the game state, they'll choose conflicting roles.

⚠️ **Common Misconception**: Students think multi-agent = each agent acts independently. The key challenge is **coordination** — agents must share information and align their actions. Writing "they work together" = **0 marks**. You must name specific strategy types (collective behaviours, positioning, role-based) and explain the mechanism.

⚠️ **Common Misconception #2**: Students confuse centralized and decentralized control. An overhead camera system is **centralized** (one global view). Reynolds' flocking is **decentralized** (each agent only sees local neighbors). Both can produce coordinated behavior, but through fundamentally different mechanisms.

💡 **Core Intuition (Part 2)**: Complex collective behavior can emerge from simple local rules (flocking), and effective teamwork requires **commitment to communication and shared goals** (STEAM), not just individual competence.

---

## 📐 Formal Definitions

**Embodied AI:** AI systems that possess a physical body with sensors and actuators, operating in the real world under real-time constraints. Design emphasizes situated reasoning — exploiting environmental structure rather than solving the general problem.

**Layered Control (Brooks, 1986):** A control architecture where multiple behavior layers (e.g., avoid, wander, explore) run **concurrently** and their outputs are **combined** (typically summed as force vectors). Each layer is simple; complex behavior emerges from their interaction. This is distinct from hierarchical control, where a top-level controller issues commands to lower levels.

**Reynolds' Flocking Rules (1987):** Three local rules — **R1: Collision avoidance** (separation), **R2: Flock centering** (cohesion), and **R3: Velocity matching** (alignment) — that produce emergent flocking behavior without central control. This is a canonical example of agent-based modelling.

**STEAM / Joint Persistent Goal (Tambe, 1997):** A teamwork framework where agents commit to a shared goal and maintain it until it is **Achieved (A)**, **Unachievable (U)**, or **Irrelevant (I)**. The critical feature: agents are committed to **communicating** status changes to the entire team, ensuring mutual belief, not just individual action.

**Emergence:** Complex global patterns or behaviors arising from simple local interactions without central coordination. Examples: flocking from Reynolds' three rules, ant colony optimization, traffic jams from individual driver behavior.

---

## 🔄 How It Works — Detailed Mechanisms

### Allen's Layered Control Architecture

```
SENSORS (Sonar array)
         ↓
┌─────────────────────────────────────────┐
│ Level 2: EXPLORE                        │
│   → Compute force toward open space     │
│   → f_explore = direction_of_max_range  │
├─────────────────────────────────────────┤
│ Level 1: WANDER                         │
│   → Pick random direction every ~10s    │
│   → f_wander = random_heading           │
├─────────────────────────────────────────┤
│ Level 0: AVOID                          │
│   → For each obstacle: repel ∝ 1/d²    │
│   → f_avoid = Σ (1/d²) × away_vector   │
└─────────────────────────────────────────┘
         ↓
FINAL DIRECTION = f_avoid + f_wander + f_explore
         ↓
MOTOR COMMANDS (speed, steering)
```

**All layers run simultaneously**. The avoid layer has the strongest effect when obstacles are close (because 1/d² grows rapidly). When no obstacles are near, wander and explore dominate. This creates robust, adaptive behavior with zero explicit planning.

### Polly's Navigation Pipeline

```
Camera (64×48, every 66ms)
         ↓
Image Processing
├── Carpet detection (smooth = navigable, pattern = obstacle)
├── Ground-plane constraint (higher in image = farther away)
└── Boolean precepts: open-left?, blocked?, wall-ahead?, vanishing-point
         ↓
Frame Matching
├── Compare current view against stored landmark frames
├── Match by appearance (not by 3D model)
└── Rotational odometry (how far have I turned?)
         ↓
District Recognition
├── Combine direction + landmark observations
├── "Going east + left turn ahead → southern corridor"
└── Recover localization when lost
         ↓
Action Selection
└── Navigate toward destination / give tour
```

### BigDog's Control Flow

```
MISSION COMMAND: "Walk forward at 1.5 m/s"
         ↓
HIGH-LEVEL CONTROLLER
├── Compare target_speed (1.5) with actual_speed → adjust leg timing
├── Compare target_attitude (level) with actual pitch/yaw/roll → adjust torso
├── Select gait based on terrain:
│   - Flat → trot (fastest)
│   - Steep → crawl (most stable)
│   - Moderate → walk
└── Adjust torso pitch for uphill/downhill
         ↓
LOW-LEVEL CONTROLLER (per leg)
├── Compute desired joint positions for current gait phase
├── Servo control: move joints to desired positions
├── Force control: manage ground reaction forces
└── Direct forces toward hip joint (stability)
         ↓
HYDRAULIC ACTUATORS → Physical leg movement
```

### Flocking (Boids) Algorithm — Step by Step

```
FOR EACH AGENT AT EACH TIME STEP:

1. PERCEIVE: Find all flockmates within field of view

2. R1 — COLLISION AVOIDANCE (Separation):
   For each flockmate within minimum_separation_distance:
       Compute repulsive vector AWAY from that flockmate
   f_separation = sum of repulsive vectors

3. R2 — FLOCK CENTERING (Cohesion):
   Compute center_of_mass of visible flockmates
   f_cohesion = vector TOWARD center_of_mass

4. R3 — VELOCITY MATCHING (Alignment):
   Compute average_heading of visible flockmates
   f_alignment = vector TOWARD average_heading

5. COMBINE:
   f_total = w₁ × f_separation + w₂ × f_cohesion + w₃ × f_alignment

6. UPDATE:
   heading += clamp(f_total.angle, max_rotation)
   speed = clamp(f_total.magnitude, max_speed)
   position += speed × heading_direction
```

**Hermellin & Michel's 5 parameters:**
1. Field of view (how far and wide each agent can see)
2. Minimum separation distance (R1 trigger radius)
3. Cohesion threshold (R2 trigger radius)
4. Maximum speed
5. Maximum rotation per time step

**3 agent attributes:** heading, speed, nearest-neighbor list

### STEAM Decision Flow

```
TEAM FORMATION:
    All agents agree on Joint Persistent Goal (JPG)
         ↓
EXECUTION PHASE:
    Each agent pursues the JPG independently
         ↓
STATUS MONITORING:
    Each agent continuously evaluates:
    ├── A: Is the goal ACHIEVED?
    ├── U: Is the goal UNACHIEVABLE?
    └── I: Is the goal IRRELEVANT?
         ↓
IF AGENT PRIVATELY CONCLUDES A/U/I:
    1. Agent exits the JPG
    2. Agent MUST communicate its conclusion to ALL teammates
       (This is NOT optional — it's a commitment)
    3. Wait for team to acknowledge
         ↓
TEAM RESPONSE:
    Team forms NEW MUTUAL BELIEF
    ├── If A: Mission complete → celebrate/debrief
    ├── If U: Abort mission → retreat or replan
    └── If I: Goal no longer matters → redirect to new JPG
```

---

## ⚖️ Trade-offs & Comparisons

### Embodied AI Design Approaches

| Approach | Advantage | Disadvantage | Example |
|---|---|---|---|
| **Simplifying assumptions** | Cheap, fast, works in known environment | Breaks in new environments | Polly (carpet = safe) |
| **Rich world model** (classical AI) | General, transferable across environments | Expensive computation, may be too slow for real-time | Traditional SLAM |
| **Layered control** (Brooks) | Robust, simple per-layer, no master plan needed | Hard to debug emergent behavior, hard to add strategic reasoning | Allen |
| **Full sensor suite** | More accurate perception | Heavy, power-hungry, expensive | Mars rover (stereo cameras, inertial, odometry) |
| **Learning-based control** | Adapts to unexpected situations | Needs lots of training data/simulation, black-box behavior | BigDog + NEAT-style controller |

### Wheels vs Legs

| Dimension | Wheels | Legs (BigDog) |
|---|---|---|
| Terrain capability | Flat/paved surfaces only | **Rough terrain**, stairs, rubble, slopes |
| Mechanical complexity | Simple mechanism | Complex joints, hydraulics, dynamic balancing |
| Energy efficiency | High | Lower (hydraulic systems waste energy) |
| Speed on flat ground | Fast | Slower |
| Versatility | Limited to smooth surfaces | Can go almost anywhere |
| Applications | Warehouses, roads, factories | Search-and-rescue, military, hazardous sites |

### Coordination Strategies Comparison

| Strategy | When to Use | Strength | Limitation |
|---|---|---|---|
| **Joint Persistent Goal (STEAM)** | High-stakes missions requiring reliable teamwork | Principled handling of failures and plan changes | Communication overhead; requires reliable comms |
| **Flocking (local rules)** | Large swarms, no central control needed | Scales to thousands of agents; no single point of failure | No strategic goals — only emergent motion patterns |
| **Collective behaviours** | Complex coordinated plays (passing) | Highly effective teamwork | Computationally expensive in real-time |
| **Positioning strategies** | Predictable field coverage | Simple to implement, reliable | Static — doesn't adapt well to opponent strategy |
| **Role-based strategies** | Flexible, situational adaptation | Dynamic, responsive to game state | Requires shared perception to avoid role conflicts |

### Centralized vs Decentralized Control

| Dimension | Centralized | Decentralized |
|---|---|---|
| Decision making | One controller for all agents | Each agent decides locally |
| Communication | All info flows to/from center | Only local information exchange |
| Robustness | **Single point of failure** | No single point of failure |
| Scalability | Limited (bottleneck at center) | Scales to thousands (flocking, ant colonies) |
| Strategic capability | Can implement complex strategy | Limited to emergent behaviors |
| Example | Overhead camera + central computer | Boids, ant colonies, swarm robots |

---

## 🏗️ Design Question Answer Framework

> If the exam asks: "Design a [multi-agent system / robot controller / fitness function] for [scenario]"

### WHAT → WHY → HOW → TRADE-OFF → EXAMPLE

**1. WHAT (Define the approach):**
"I would design a [layered control / flocking-based / role-based / STEAM-based] system where each agent [description of individual behavior]."

**2. WHY (Justify the choice):**
"This approach is suitable because [no central control available / environment is structured / real-time response required / simple agents can produce complex behavior through emergence / reliable communication exists for JPG]."

**3. HOW (Specific design — this is where the marks are):**
- **Agent sensors:** What each agent can perceive (camera, sonar, shared overhead view, WiFi data)
- **Local rules / behaviors:** What rules each agent follows (avoid obstacles, move toward ball, maintain formation)
- **Communication:** How agents share information (WiFi, overhead camera, body signals, or none)
- **Coordination mechanism:** JPG (STEAM) / flocking rules / role assignment / formation-based

**4. TRADE-OFF:**
- Centralized vs decentralized (overhead camera vs individual perception)
- Communication cost vs coordination quality
- Simplicity of individual agents vs sophistication of team behavior
- Robustness (what happens when one agent fails?)

**5. EXAMPLE:**
- Robot soccer: overhead camera + role-based + collective passing
- Search-and-rescue swarm: decentralized flocking + obstacle avoidance
- Military operation: STEAM with JPGs for reliable team commitment
- Mars exploration: conservative autonomy + human-in-the-loop

### Fitness Function Design for Embodied Agents (Cross-topic with NEAT)

When asked to design a fitness function for a robot using GA/NEAT:

```
Fitness = w₁ × (primary_goal_metric)
        + w₂ × (secondary_goal_metric)
        - w₃ × (penalty_for_bad_behavior)
        - w₄ × (penalty_for_instability)

Evaluated over MANY time steps of simulation.
Highest fitness when all deviations from targets are LOW.
```

---

## 📝 Exam-Relevant Questions & Model Answers

### EXAM QUESTION — S1 2025/2026 Sample Q4 (2 marks)

**Question:** In robot soccer with an overhead camera and no inter-robot communication, describe a coordination strategy the robots could use.

**Full-marks answer:**

> **Any ONE of the following** (all valid because the overhead camera gives every robot the **same shared global view**):
>
> **Option A — Collective behaviours (passing):** Each robot independently evaluates candidate passing points based on **interception prediction** — computing whether an opponent could intercept the ball en route. Since all robots see the same overhead view, they can independently arrive at the same conclusion about optimal passes without direct communication.
>
> **Option B — Positioning strategies (formations):** Robots adopt a formation (e.g., 2-1-2) and each robot independently calculates which formation position it should occupy based on ball location and teammate positions — all visible from the overhead camera. No communication needed because every robot computes the same optimal positioning.
>
> **Option C — Role-based strategies (dynamic role assignment):** Each robot dynamically assigns itself a role (goalkeeper, attacker, defender) based on the current game state. Since all robots observe the same overhead view, they can independently compute the same role assignments using shared heuristics (e.g., "closest robot to own goal = goalkeeper").
>
> **Why these all work without communication:** The overhead camera provides a **shared global percept** — every robot sees the same game state simultaneously. This eliminates the need for explicit communication because each robot can independently compute the same strategy.

### EXAM QUESTION — S1 2025 Actual Q6 (3 marks)

**Question:** Design a fitness function for training a BigDog walking robot using a Genetic Algorithm.

**Full-marks answer:**

> The fitness function evaluates how well a candidate controller (evolved by GA) makes BigDog walk. It measures multiple components across the entire simulation:
>
> $$\text{Fitness} = -w_1 |v_{target} - v_{actual}| - w_2 |\theta_{target} - \theta_{actual}| - w_3 |h_{target} - h_{actual}| - w_4 (\Delta\text{pitch} + \Delta\text{yaw} + \Delta\text{roll})$$
>
> **Components:**
>
> 1. **Speed matching**: $|v_{target} - v_{actual}|$ — penalize deviation from desired walking speed
> 2. **Direction matching**: $|\theta_{target} - \theta_{actual}|$ — penalize deviation from desired heading direction
> 3. **Height maintenance**: $|h_{target} - h_{actual}|$ — penalize the body being too high or too low (should maintain stable torso height)
> 4. **Attitude stability**: $\Delta\text{pitch} + \Delta\text{yaw} + \Delta\text{roll}$ — penalize body tilting or rotating away from upright orientation; all three angles must stay within acceptable bounds
>
> **Fitness is highest when ALL differences are simultaneously LOW** across the entire simulation duration. The function is evaluated over many time steps to ensure **consistent** walking performance, not just a single good moment.
>
> Optional additional terms: energy efficiency (prefer lower force usage), gait smoothness, penalty for falling.

### Q1: Explain Brooks' layered control architecture with an example. (4 marks)

> Brooks' layered control architecture (1986), demonstrated by the robot **Allen**, organizes behavior into multiple **concurrent layers**:
>
> - **Level 0 — Avoid**: The lowest layer reacts to nearby obstacles using sonar, generating a **repulsive force** inversely proportional to distance squared (1/d²). Closer obstacles produce stronger avoidance.
> - **Level 1 — Wander**: Chooses a **random direction** and follows it for about 10 seconds, then picks a new random direction.
> - **Level 2 — Explore**: Steers toward **wide-open space** detected by sonar, heading where there is the most room.
>
> All layers run **simultaneously** and their forces are **combined** (summed) to determine the robot's actual direction and speed. The result is robust wandering behavior with **no master plan** and no rich world knowledge. Higher layers add competence, but the robot still functions even if they fail — Level 0 alone prevents crashes.
>
> This demonstrates that apparently intelligent behavior can emerge from the **combination of simple concurrent behaviors**, without any complex reasoning or planning.

### Q2: What are Reynolds' three flocking rules? What concept do they demonstrate? (3 marks)

> Reynolds (1987) proposed three **local rules** for simulating flocking, where each agent only reacts to nearby neighbors:
>
> 1. **R1 — Collision Avoidance (Separation)**: Don't come within a minimum distance of nearby flockmates. If too close, steer away.
> 2. **R2 — Flock Centering (Cohesion)**: Stay close to the group by steering toward the average position of nearby flockmates.
> 3. **R3 — Velocity Matching (Alignment)**: Align speed and direction with nearby agents, matching their heading.
>
> These three rules demonstrate **emergence** — complex, realistic flocking patterns arise from **simple local interactions** without any central controller. No agent knows the overall flock shape; each just follows three rules based on what it can locally see. This is a canonical example of **agent-based modelling** where global behavior emerges from local rules.

### Q3: Explain the Joint Persistent Goal (JPG) in STEAM. Why is communication essential? (3 marks)

> A **Joint Persistent Goal (JPG)** is a shared goal that all team members commit to pursuing. Members continue working on the JPG unless they determine it is **Achieved (A)**, **Unachievable (U)**, or **Irrelevant (I)**.
>
> Communication is essential because when one agent **privately concludes** A, U, or I, it must **inform the entire team** so they can form a **new mutual belief**. Without this commitment to communicate, one agent might abandon the mission while others wait indefinitely — exactly the "brittle plan" problem that STEAM was designed to solve.
>
> **Example**: If a scout helicopter detects a surface-to-air missile battery (making the mission **Unachievable**), it must tell teammates rather than simply flying home alone. Otherwise, the remaining helicopters continue into danger waiting for an all-clear that will never come.

### Q4: How did Polly use simplifying assumptions to navigate? (3 marks)

> Polly (Horswill, 1993) exploited its **structured indoor environment** to avoid solving the hardest possible vision problem:
>
> 1. **Carpet detection**: The office had uniform, un-patterned carpet. Anything with visual texture/patterns was treated as an obstacle — no general object recognition needed.
> 2. **Ground-plane constraint**: Objects on the flat floor appear **higher in the image when farther away**. This provided depth estimation from a single 2D camera, eliminating the need for stereo cameras or LIDAR.
> 3. **Corridor geometry**: Narrow corridors constrained where landmarks could appear, reducing the visual search space dramatically.
>
> These simplifying assumptions allowed Polly to navigate at animal speed (~1 m/s) with just a **64x48 pixel camera at 15 fps** — far below what general-purpose computer vision would require. The design principle: "Don't solve the hardest possible vision problem if the environment gives you shortcuts."

### Q5: In robot soccer, describe three coordination strategies. (3 marks)

> 1. **Collective behaviours**: Coordinated team plays such as **passing strategies**. Candidate passing points are evaluated based on **interception prediction** (can an opponent reach the ball first?) and scored by tactical value (how close to goal, how open is the receiver).
>
> 2. **Positioning strategies**: Choosing **formations** (e.g., 2-1-2) that provide balanced coverage for both attacking and defensive opportunities. Players move to assigned positions based on ball location.
>
> 3. **Role-based strategies**: **Dynamically assigning roles** (goalkeeper, attacker, defender) based on the current game situation — more attackers when the ball is near the opponent's goal, more defenders when under pressure.
>
> Position- and role-based methods work best when teammates **perceive the situation in a sufficiently similar way** — otherwise they may choose conflicting roles.

### Q6: What was Brooks' argument in "Elephants Don't Play Chess"? (2 marks)

> Brooks (1990) argued that traditional AI focused too much on **high-level reasoning** (chess, theorem proving, expert systems), but real intelligence should be understood **bottom-up**. Evolution spent **billions of years** on simple organisms (bacteria, insects, simple animals) before complex intelligence emerged. Human-level intelligence is only about 1 million years old.
>
> Therefore, AI research should start by studying **simple intelligent behaviors** — locomotion, obstacle avoidance, social coordination in insects and animals — and **build upward from situated competence** rather than downward from elite symbolic performance.

### Q7: Compare BigDog's control architecture with Allen's layered control. (4 marks)

> **Allen (Brooks, 1986)** uses a **layered behavior architecture**:
> - Three layers (Avoid, Wander, Explore) run simultaneously
> - Forces from all layers are combined (summed)
> - No explicit hierarchy — emergence from simple parallel behaviors
> - Very simple: no physics model, no terrain adaptation
>
> **BigDog (2008)** uses a **two-level hierarchical controller**:
> - **High-level**: coordinates legs for body speed, attitude (pitch/yaw/roll), and gait selection
> - **Low-level**: manages individual joint positions and forces
> - Explicitly hierarchical — high-level commands flow down to low-level execution
> - Complex: physics-based control, terrain adaptation, gait switching
>
> **Key difference**: Allen demonstrates that intelligent behavior can emerge from **simple parallel layers with no hierarchy**. BigDog demonstrates that **complex physical tasks** (rough-terrain walking) may require **explicit hierarchical control** where a high-level controller coordinates low-level actuators.
>
> Both exploit the embodied AI principle of **situated action in the physical world**, but at very different levels of complexity.

---

## 🌐 English Expression Tips

### Describing Embodied AI

```
- "Embodied AI refers to systems that control a physical body and must react to sensor input in real time."
- "The design principle is to exploit environmental constraints rather than solving the hardest possible problem."
- "Polly demonstrated that simplifying assumptions about the environment enable effective navigation with minimal computation."
- "Layered control allows robust behavior to emerge from the combination of simple, concurrent behavior layers."
- "The ground-plane constraint allows depth estimation from a single 2D camera."
```

### Describing Teamwork and Coordination

```
- "A Joint Persistent Goal commits team members to both pursuing the goal and communicating changes in its status."
- "Flocking demonstrates emergence — complex global patterns arising from simple local interactions."
- "Reynolds' three rules — collision avoidance, flock centering, and velocity matching — produce realistic flocking without central control."
- "In robot soccer, coordination strategies include collective behaviours, positioning strategies, and role-based assignment."
- "Position- and role-based strategies work best when teammates perceive the situation in a sufficiently similar way."
```

### Describing Design Choices

```
- "The rationale for choosing layered control over hierarchical planning is that it provides robustness without requiring a world model."
- "The trade-off between centralized and decentralized control involves reliability versus scalability."
- "This approach scales well because each agent only requires local information."
- "One potential limitation is that emergent behavior is difficult to predict or debug."
```

### Key Vocabulary to Get Right

| Often Confused | Distinction |
|---|---|
| **Embodied vs Situated** | Embodied = has a physical body; Situated = reasons in the context of a specific environment. An AI can be situated without being embodied (e.g., a recommendation system situated in a specific user context). |
| **Emergence vs Design** | Emergence = patterns arise unplanned from local rules; Design = patterns are explicitly programmed. Flocking is emergence; a formation strategy is design. |
| **Layered vs Hierarchical** | Layered (Brooks) = all layers run simultaneously and outputs combine; Hierarchical (BigDog) = top-level commands flow down to lower levels |
| **Centralized vs Decentralized** | Centralized = one controller makes decisions for all (overhead camera); Decentralized = each agent decides independently (flocking) |
| **Flocking vs Swarming** | Flocking = coordinated movement (Reynolds' rules); Swarming = broader term for any collective behavior |
| **Communication vs Coordination** | Communication = exchanging information; Coordination = aligning actions. You can have coordination WITHOUT communication (overhead camera → all see the same thing) |

---

## ✅ Self-Test Checklist

- [ ] Can I explain what Embodied AI means and give three examples (Polly, Allen, BigDog)?
- [ ] Can I state Polly's three simplifying assumptions and explain each one?
- [ ] Can I explain the ground-plane constraint?
- [ ] Can I draw Allen's three-layer control architecture and explain how forces combine?
- [ ] Can I name at least three Brooks robots and describe what each does?
- [ ] Can I describe BigDog's two-level control system and its three gaits?
- [ ] Can I explain why Mars rovers need autonomous control?
- [ ] Can I state Reynolds' three flocking rules by name AND describe each?
- [ ] Can I explain the concept of emergence with a concrete example?
- [ ] Can I explain the Joint Persistent Goal (JPG) and the A/U/I conditions?
- [ ] Can I explain why communication is essential in STEAM?
- [ ] Can I name and describe all three robot soccer coordination strategies?
- [ ] Can I explain why overhead camera eliminates the need for communication?
- [ ] Can I explain Brooks' "Elephants Don't Play Chess" argument?
- [ ] Can I compare centralized vs decentralized multi-agent control?
- [ ] Can I design a fitness function for an embodied agent (BigDog, mobile robot)?
- [ ] Can I state the 5 parameters and 3 agent attributes in Hermellin & Michel's Boids?

---

## 📚 Key References

- Horswill, I. (1993). *Polly: A vision-based artificial agent.* Proc. AAAI-93.
- Brooks, R. (1986). *A robust layered control system for a mobile robot.* IEEE J. Robotics and Automation.
- Brooks, R. (1990). *Elephants don't play chess.* Robotics and Autonomous Systems 6.
- Raibert, M. et al. (2008). *BigDog, the rough-terrain quadruped robot.* IFAC Proceedings.
- Bajracharya, M. et al. (2008). *Autonomy for Mars rovers: Past, present, and future.* Computers 41(12).
- Reynolds, C. W. (1987). *Flocks, herds and schools: A distributed behavioral model.* Proc. SIGGRAPH.
- Tambe, M. (1997). *Agent architectures for flexible, practical teamwork.* Proc. AAAI 97.
- Hermellin, E. & Michel, F. (2017). *Complex flocking dynamics without global stimulus.* Proc. ECAL 2017.
- Antonioni, E. et al. (2021). *Game strategies for physical robot soccer players: A survey.* IEEE Trans. Games.

---

*Based on COMPSCI 713 Week 6 Lecture 12 (33 slides) — Instructor: Xinyu Zhang, adapted from Prof. Jim Warren.*
