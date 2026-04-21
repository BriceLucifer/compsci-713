# Embodied AI, Multi-Agent Systems & Collective Behaviour

## 🎯 Exam Importance
🟠 **高频** | Week 6 Lecture 12 | Covers embodied robots, layered control, flocking, teamwork, robot soccer

> This chapter covers two major themes: (1) **Embodied AI** — robots with physical bodies that must act in the real world, and (2) **AI Teams & Swarms** — multi-agent coordination from flocking to robot soccer.

---

## 📖 Core Concepts

| English Term | 中文 | One-line Definition |
|---|---|---|
| Embodied AI（具身智能） | 具身人工智能 | AI systems that control a physical body and react to sensors in real time |
| Situated Reasoning（情境推理） | 情境推理 | Reasoning that exploits the specific environment rather than solving the general case |
| Layered Control（分层控制） | 分层控制 | Architecture where multiple behavior layers run in parallel, combined to produce action |
| Subsumption Architecture（包含体系结构） | 包容式架构 | Brooks' architecture where higher layers can override lower ones |
| Simplifying Assumptions（简化假设） | 简化假设 | Exploiting environmental constraints to avoid solving the hardest possible problem |
| Joint Persistent Goal / JPG（联合持续目标） | 联合持续目标 | A shared goal that team members keep pursuing until it is Achieved, Unachievable, or Irrelevant |
| STEAM（Shell for TEAMwork） | 团队协作框架 | Tambe's framework for multi-agent teamwork based on JPGs and communication commitments |
| Flocking / Boids（群集行为） | 群集行为 | Emergent collective motion from simple local rules (Reynolds, 1987) |
| Emergence（涌现） | 涌现 | Complex global patterns arising from simple local interactions |
| Agent-Based Modelling（基于智能体的建模） | 基于智能体建模 | Simulating systems where global behavior emerges from individual agents following local rules |
| Dynamic Balancing（动态平衡） | 动态平衡 | Continuous real-time control to keep a robot upright while moving |
| Recurrent Connection（循环连接） | 循环连接 | A connection that feeds output back as input, enabling memory of past states |

---

## 🧠 Feynman Draft — Part 1: Embodied AI

### What is Embodied AI?

Imagine you're trying to catch a ball. You don't sit down with a physics textbook, calculate trajectories, and plan arm movements — you just *react*. Your body, your eyes, and your muscles work together in real time, using shortcuts like "the ball is getting bigger, so it's coming closer."

That's the core idea of **Embodied AI**: intelligence isn't just about abstract reasoning in a computer. It's about **acting robustly in the physical world** — having a body, sensors, and actuators, and dealing with real-time constraints.

> Brooks (1990), in his famous paper "Elephants Don't Play Chess," argued that intelligence doesn't start with chess and theorem provers. Evolution spent a **billion years** on simple life forms before complex animals appeared. Human-level intelligence has only been around for ~1 million years. So general AI should also study **simple intelligent behavior**: cockroaches, rats, locomotion, and social coordination.

The broader message: **build upward from situated competence**, not downward from elite symbolic performance.

### Polly — A Vision-Based Robot (Horswill, 1993)

Polly was the first visually navigated robot to move at roughly **animal speed (~1 m/s)** back in 1993. It gave tours of MIT AI Lab's 7th floor.

**Key design principle: Don't solve the hardest possible vision problem if the environment lets you solve an easier one.**

Polly exploited **simplifying assumptions** about its environment:
- **Uncluttered office** with corridors and uniform un-patterned carpet
- **Carpet/object detection**: if it's not carpet (has patterns), it's probably an obstacle
- **Ground-plane constraint**: objects rest on the flat floor, so things appearing higher in the image are farther away — no need for real depth sensing!
- **Corridor geometry**: narrow corridors constrain where landmarks can appear, reducing search space

**Visual system:**
- Captured **64 x 48 images** every **66 ms** — extremely low resolution, but cheap to compute
- Produced Boolean precepts: `open-left?`, `blocked?`, `wall-ahead?`, `vanishing-point`, etc.
- Used height in image as proxy for depth (ground-plane constraint)

**Navigation:**
- Stored a library of **frames** (records) describing how landmarks looked from different directions/distances
- Used rough **rotational odometry** (tracking how much it had turned left and right)
- Recognized **districts** to recover localization (e.g., "going east and see a left turn ahead → must be in the southern corridor")
- Visitors requested a tour by **waving a foot** (camera looked at foot level)

> Navigation was **appearance-based and pragmatic**, not a full symbolic world model.

### Allen — Layered Control (Brooks, 1986)

Allen demonstrated Brooks' idea of a **layered control system** using sonar sensors:

| Layer | Behavior | Description |
|---|---|---|
| **Level 0 — Avoid** | Obstacle avoidance | Veer away from nearby obstacles; stopping force scaled with inverse-square distance |
| **Level 1 — Wander** | Random exploration | Choose a random direction and follow it for ~10 seconds |
| **Level 2 — Explore** | Directed movement | Head toward wide-open space |

- All three levels run **in parallel** and their forces are **combined** to choose a direction
- Result: robust wandering with **no master plan, no rich knowledge**, and very simple programming

### Other Brooks Robots

- **Squirt**: 1 cubic inch robot; sought dark places and sat still in corners. Upper behavior: stay still after a loud noise, then move toward it. Lower behavior kicks in → hides, but now closer to "where the action is"
- **Herbert**: had an arm, programmed to steal empty soda cans
- **Genghis**: six-legged robot with **loose control** — legs were not explicitly coordinated, yet it scrambled around and followed infrared sources

### BigDog — Rough-Terrain Quadruped (Boston Dynamics, 2008)

BigDog was a famous quadruped robot designed to move over **rough terrain** using **legs** rather than wheels.

**Physical specs:**
- Mass: ~**109 kg**
- Two-stroke water-cooled internal combustion engine → hydraulic pump
- High-pressure oil drove servo valves and hydraulic cylinders for leg actuators
- Sensors: joint position, force, inertial sensors (body angle & acceleration)
- Onboard computer ran a **two-level control system**

**Control architecture:**
- **Low-level**: manages position and forces of individual joints
- **High-level**: coordinates legs to regulate body speed, attitude (pitch, yaw, roll), and altitude

**Gaits:** Could switch among **crawl**, **walk**, and **trot**
- Trot for speed; crawl for steep or slippery ground
- Controller adjusts torso pitch for climbing/descending

**Dynamic balancing** — learning-based algorithms can be trained to control legs (relates to NEAT solving the two-pole balancing task!)

**Fate:** Prototype was **very loud** (military lost interest). Still promising for **search-and-rescue**, **hazardous-site inspection**, and **mine clearing**.

### Robots on Mars

Mars rovers need autonomous control because of **communication delay** (signals take minutes to reach Earth).

- **Stereo cameras** build terrain maps
- **Wheel odometers** estimate motion (unreliable on sand due to slipping)
- **Inertial sensors** estimate pitch and roll
- **Heading** estimated from sun position and time
- Rover can **plan a path**, adapt dynamically, and respect human-labeled no-go areas

**Space travel constraints:**
- Hardware must survive radiation and extreme temperatures
- Power is precious (dust on solar panels can end the mission)
- Rovers move **very slowly** — tipping over would be disastrous
- **Ingenuity** helicopter: planned for 5 flights, completed **72**

> Mars rovers repeat the same theme: **embodiment plus clever approximations under harsh constraints**.

⚠️ **Common Misconception**: Students think embodied AI requires sophisticated reasoning. Actually, the key insight is that **environment-specific shortcuts** can replace complex computation. Polly's 64x48 pixel camera worked because it exploited the ground-plane constraint!

💡 **Core Intuition (Part 1)**: Embodied AI succeeds by exploiting environmental structure rather than solving the general problem — intelligence is about acting robustly in the world, not just reasoning abstractly.

---

## 🧠 Feynman Draft — Part 2: AI Teams & Swarms

### From Single Robots to Teams

Once individual robots can navigate and act, the next question is: can they work **together**?

### Joint Reasoning — Tambe (1997) & STEAM

Tambe studied how to do "classic AI planning" with a physically distributed team of agents. Motivating domain: a squadron of **attack helicopters**.

**Problem with brittle team plans:** If a scout is destroyed and everyone else waits forever for the all-clear, the mission fails. Adding one extra rule may patch one failure, but ad hoc patches proliferate and other failures remain hidden.

**STEAM (Shell for TEAMwork)** solution — **Joint Persistent Goal (JPG)**:
- Team members keep pursuing a goal unless they learn it is **Achieved (A)**, **Unachievable (U)**, or **Irrelevant (I)**
- If one agent privately concludes A/U/I, it exits the JPG BUT replaces it with a commitment to have **new mutual belief** for the team
- STEAM is fundamentally a commitment to **communicate**, not just to act

> **Example:** If a team member detects a surface-to-air missile battery and the mission becomes **unachievable**, it should NOT simply fly home without explanation. It must inform the team.

### Brooks' "Elephants Don't Play Chess" (1990)

- Intelligence doesn't start with chess — evolution spent most of Earth's history on simple life forms
- The Cambrian Explosion (~500M years ago) produced larger animals; human intelligence is only ~1M years old
- So AI should study **simple intelligent behavior**: cockroaches, rats, locomotion, social coordination
- **Build upward from situated competence**, not downward from elite symbolic performance

### Flocking — Reynolds' Three Rules (1987)

How do thousands of starlings create mesmerizing murmuration patterns with no central controller? Reynolds proposed **three simple rules**:

| Rule | Name | Description |
|---|---|---|
| **R1** | Collision Avoidance（避免碰撞） | Do not come within a minimum distance of nearby flockmates |
| **R2** | Flock Centering（群聚） | Stay close to flockmates rather than drifting away from the group |
| **R3** | Velocity Matching（速度匹配） | Align your motion with nearby agents (velocity = speed + direction) |

This is a form of **agent-based modelling**: **global behavior emerges from local interactions**. Similar ideas appear in epidemiology and social-network dynamics.

### "Boids" (Bird-Droids) Simulator

- Reynolds' rules generate striking flock-like behavior in simulation
- A clean demonstration of **emergence**: realistic patterns from simple local rules
- Helps attribute different visible behaviors to different rules

**Hermellin and Michel's (2017) implementation:**
- **5 parameters**: field of view, minimum separation distance, cohesion threshold, maximum speed, maximum rotation
- **3 agent attributes**: heading, speed, nearest-neighbor list
- Small implementation choices can **dramatically change** the emergent flocking behavior

### Robot Soccer — Multi-Agent Coordination in Practice

Robot soccer is a natural testbed for embodied multi-agent AI. It combines:
- Perception, locomotion, communication, coordination, and strategy

**Coordination depends on league rules:**
- Can players access a **shared data model** over WiFi?
- Is there an **overhead camera view**?
- Can robots signal each other directly, or only use body signals?
- Walking platforms are unstable → narrow field of view → each robot may only maintain a rough **probabilistic model** of the game state

**Three levels of strategy:**

| Strategy Type | Description | Example |
|---|---|---|
| **Collective Behaviours（集体行为）** | Coordinated team plays | Passing strategy: evaluate passing points by interception prediction, score by position and tactical value |
| **Positioning Strategies（位置策略）** | Formation-based coverage | Choose formations that create both attacking and defensive opportunities (e.g., 2-1-2) |
| **Role-Based Strategies（角色分配）** | Dynamic role assignment | Assign roles (goalie, attacker, defender) based on the current game situation |

- Position- and role-based methods work best when **teammates perceive the situation in a sufficiently similar way**

⚠️ **Common Misconception**: Students think multi-agent = each agent acts independently. The key challenge is **coordination** — agents must share information and align their actions. Writing "they work together" = 0 marks. Name specific strategy types!

💡 **Core Intuition (Part 2)**: Complex collective behavior can emerge from simple local rules (flocking), and effective teamwork requires commitment to communication and shared goals, not just individual competence.

---

## 📐 Formal Definitions

**Embodied AI:** AI systems that possess a physical body with sensors and actuators, operating in the real world under real-time constraints. Design emphasizes situated reasoning — exploiting environmental structure rather than solving the general problem.

**Layered Control (Brooks, 1986):** A control architecture where multiple behavior layers (e.g., avoid, wander, explore) run concurrently and their outputs are combined. Each layer is simple; complex behavior emerges from their interaction.

**Reynolds' Flocking Rules (1987):** Three local rules — collision avoidance (R1), flock centering (R2), and velocity matching (R3) — that produce emergent flocking behavior without central control.

**STEAM / Joint Persistent Goal (Tambe, 1997):** A teamwork framework where agents commit to a shared goal and maintain it until it is Achieved, Unachievable, or Irrelevant. Agents are committed to communicating status changes, not just acting.

---

## 🔄 How It Works

### Allen's Layered Control Architecture

```
┌─────────────────────────────────────────┐
│ Level 2: EXPLORE                        │
│   → head toward open space              │
├─────────────────────────────────────────┤
│ Level 1: WANDER                         │
│   → pick random direction, follow ~10s  │
├─────────────────────────────────────────┤
│ Level 0: AVOID                          │
│   → repel from obstacles (1/d² force)   │
└─────────────────────────────────────────┘
         ↓  All forces COMBINED  ↓
        [Final heading & speed]
```

- All layers run **simultaneously**
- Forces from all levels are **summed** to produce the final direction
- No master plan needed — robust behavior emerges

### Polly's Navigation Pipeline

```
Camera (64×48, 66ms) → Boolean Precepts → Frame Matching → Action
                         ↑                      ↑
              Ground-plane          Landmark library
              constraint            (stored views)
                         ↓
              District recognition → Localization recovery
```

### BigDog's Two-Level Control

```
High-Level Controller
├── Body speed regulation
├── Attitude control (pitch, yaw, roll)
├── Gait selection (crawl / walk / trot)
└── Terrain adaptation

Low-Level Controller
├── Individual joint position control
├── Joint force control
└── Ground reaction forces → directed toward hip
```

### Flocking (Boids) Algorithm

```
For each agent at each time step:
    1. Find nearby flockmates (within field of view)
    2. R1 — Collision avoidance:
       If any flockmate too close → rotate away
    3. R2 — Flock centering:
       If flockmates at medium distance → adjust heading
       toward mean heading of visible neighbors
    4. R3 — Velocity matching:
       Align speed and direction with nearby agents
    5. Apply combined forces → update heading and speed
```

### STEAM Decision Flow

```
Team has Joint Persistent Goal (JPG)
    ↓
Each agent pursues JPG
    ↓
Agent privately concludes one of:
├── A (Achieved)   → exit JPG, inform team
├── U (Unachievable) → exit JPG, inform team
└── I (Irrelevant)   → exit JPG, inform team
    ↓
Team forms new mutual belief
    ↓
New JPG or mission ends
```

---

## ⚖️ Trade-offs & Comparisons

### Embodied AI Design Approaches

| Approach | Advantage | Disadvantage |
|---|---|---|
| **Simplifying assumptions** (Polly) | Cheap, fast, works in known environment | Breaks in new environments |
| **Rich world model** (classical AI) | General, transferable | Expensive computation, may be too slow for real-time |
| **Layered control** (Allen/Brooks) | Robust, simple per-layer, no master plan | Hard to debug emergent behavior |
| **Full sensor suite** (Mars rover) | More accurate perception | Heavy, power-hungry, expensive |

### Wheels vs Legs

| | Wheels | Legs (BigDog) |
|---|---|---|
| Terrain | Flat/paved surfaces | **Rough terrain**, stairs, rubble |
| Complexity | Simple mechanism | Complex joints, dynamic balancing |
| Energy efficiency | High | Lower (hydraulic systems) |
| Speed | Fast on flat ground | Slower but more versatile |
| Applications | Warehouses, roads | Search-and-rescue, military |

### Coordination Strategies Comparison

| Strategy | When to Use | Limitation |
|---|---|---|
| **Joint Persistent Goal (STEAM)** | High-stakes missions requiring reliable teamwork | Communication overhead |
| **Flocking (local rules)** | Large swarms, no central control needed | No strategic goals, only emergent patterns |
| **Collective behaviours** | Complex coordinated plays (passing) | Computationally expensive in real-time |
| **Positioning** | Simple, predictable coverage | Static, doesn't adapt to opponent |
| **Role-based** | Flexible, situational adaptation | Requires shared perception to avoid role conflicts |

### Centralized vs Decentralized Control

| | Centralized | Decentralized |
|---|---|---|
| Decision making | One controller for all | Each agent decides locally |
| Communication | All info flows to/from center | Only local info exchange |
| Robustness | Single point of failure | No single point of failure |
| Scalability | Limited | Scales to thousands (flocking) |
| Example | Overhead camera + central computer | Boids, ant colonies |

---

## 🏗️ Design Question Answer Framework

> If the exam asks: "Design a multi-agent system for [scenario]"

### WHAT → WHY → HOW → TRADE-OFF → EXAMPLE

**1. WHAT (Define the approach):**
"I would design a multi-agent system using [layered control / flocking rules / role-based strategies], where each agent [description of individual behavior]."

**2. WHY (Justify the choice):**
"This approach is suitable because [no central control needed / environment is structured / real-time response required / simple agents can produce complex behavior through emergence]."

**3. HOW (Specific design):**
- **Agent sensors:** What each agent can perceive
- **Local rules:** What rules each agent follows
- **Communication:** How agents share information (if at all)
- **Coordination mechanism:** JPG / flocking / role assignment

**4. TRADE-OFF:**
- Centralized vs decentralized
- Communication cost vs coordination quality
- Simplicity of individual agents vs sophistication of team behavior

**5. EXAMPLE:**
- Robot soccer: overhead camera + role-based + collective passing
- Search-and-rescue: decentralized flocking + obstacle avoidance
- Mars exploration: conservative autonomy + human-in-the-loop

---

## 📝 Exam-Relevant Questions & Answers

### Q1: Explain Brooks' layered control architecture with an example. (4 marks)

> Brooks' layered control architecture (1986), demonstrated by the robot Allen, organizes behavior into multiple **concurrent layers**:
>
> - **Level 0 — Avoid**: The lowest layer reacts to nearby obstacles, generating a repulsive force inversely proportional to distance (1/d²).
> - **Level 1 — Wander**: Chooses a random direction and follows it for about 10 seconds.
> - **Level 2 — Explore**: Steers toward wide-open space.
>
> All layers run **simultaneously** and their forces are **combined** to determine the robot's actual direction. The result is robust wandering behavior with no master plan or rich world knowledge. Higher layers add competence but the robot still functions if they fail.

### Q2: What are Reynolds' three flocking rules? What concept do they demonstrate? (3 marks)

> Reynolds (1987) proposed three local rules for simulating flocking:
> 1. **Collision avoidance (R1)**: Don't come within a minimum distance of nearby flockmates.
> 2. **Flock centering (R2)**: Stay close to the group rather than drifting away.
> 3. **Velocity matching (R3)**: Align speed and direction with nearby agents.
>
> These demonstrate **emergence** — complex, realistic flocking patterns arise from simple local interactions without any central controller. This is a form of **agent-based modelling** where global behavior emerges from local rules.

### Q3: Explain the concept of a Joint Persistent Goal (JPG) in STEAM. Why is communication essential? (3 marks)

> A JPG is a **shared goal** that all team members commit to pursuing. Members continue working on the JPG unless they determine it is **Achieved (A)**, **Unachievable (U)**, or **Irrelevant (I)**.
>
> Communication is essential because when one agent privately concludes A/U/I, it must **inform the entire team** so they can form a **new mutual belief**. Without this commitment to communicate, one agent might abandon the mission while others wait indefinitely.
>
> Example: If a helicopter detects a surface-to-air missile battery (making the mission unachievable), it must tell teammates rather than simply flying home alone.

### Q4: How did Polly use simplifying assumptions to navigate? (3 marks)

> Polly (1993) exploited its **structured indoor environment** to avoid solving the hardest possible vision problem:
> 1. **Carpet detection**: Non-carpet surfaces (with patterns) were treated as obstacles — no object recognition needed.
> 2. **Ground-plane constraint**: Objects on the flat floor appear higher in the image when farther away, providing depth information from a single camera.
> 3. **Corridor geometry**: Narrow corridors constrained where landmarks could appear, reducing the visual search space.
>
> This design principle — exploiting environmental structure — allowed Polly to work with just a 64×48 pixel camera at 15 fps, far below what general-purpose vision would require.

### Q5: In robot soccer, describe three coordination strategies. (3 marks)

> 1. **Collective behaviours**: Coordinated plays such as passing strategies, where candidate passing points are evaluated based on interception prediction and scored by position and tactical value.
> 2. **Positioning strategies**: Choosing formations (e.g., 2-1-2) that provide balanced coverage for both attacking and defensive opportunities.
> 3. **Role-based strategies**: Dynamically assigning roles (goalkeeper, attacker, defender) based on the current game situation — more attackers when the ball is near the opponent's goal.
>
> Position- and role-based methods work best when teammates **perceive the situation similarly**.

### Q6: What was Brooks' argument in "Elephants Don't Play Chess"? (2 marks)

> Brooks argued that traditional AI focused too much on high-level reasoning (chess, theorem proving), but intelligence should be understood **bottom-up**. Evolution spent billions of years on simple organisms before complex intelligence emerged. Therefore, AI research should study simple behaviors like locomotion, obstacle avoidance, and social coordination, building upward from **situated competence** rather than downward from symbolic performance.

---

## 🌐 English Expression Tips

### Describing Embodied AI
```
- "Embodied AI refers to systems that control a physical body and must react to sensor input in real time."
- "The design principle is to exploit environmental constraints rather than solving the hardest possible problem."
- "Polly demonstrated that simplifying assumptions about the environment enable effective navigation with minimal computation."
- "Layered control allows robust behavior to emerge from the combination of simple, concurrent behavior layers."
```

### Describing Teamwork and Coordination
```
- "A Joint Persistent Goal commits team members to both pursuing the goal and communicating changes in its status."
- "Flocking demonstrates emergence — complex global patterns arising from simple local interactions."
- "Reynolds' three rules — collision avoidance, flock centering, and velocity matching — produce realistic flocking without central control."
- "In robot soccer, coordination strategies include collective behaviours, positioning, and role-based assignment."
```

### Key Vocabulary to Get Right

| Often Confused | Distinction |
|---|---|
| Embodied vs Situated | Embodied = has a body; Situated = reasons in context of specific environment |
| Emergence vs Design | Emergence = patterns arise unplanned from local rules; Design = patterns are explicitly programmed |
| Layered vs Hierarchical | Layered (Brooks) = all layers run simultaneously and combine; Hierarchical = top-down command |
| Centralized vs Decentralized | Centralized = one controller; Decentralized = each agent decides locally |
| Flocking vs Swarming | Flocking = coordinated movement; Swarming = broader term for collective behavior |

---

## ✅ Self-Test Checklist

- [ ] Can I explain what Embodied AI means and why it matters?
- [ ] Can I describe Polly's three simplifying assumptions?
- [ ] Can I draw Allen's three-layer control architecture?
- [ ] Can I describe BigDog's two-level control system?
- [ ] Can I state Reynolds' three flocking rules and explain emergence?
- [ ] Can I explain STEAM and the Joint Persistent Goal concept?
- [ ] Can I explain why communication is essential in JPG?
- [ ] Can I name and describe three robot soccer coordination strategies?
- [ ] Can I explain Brooks' "Elephants Don't Play Chess" argument?
- [ ] Can I compare centralized vs decentralized multi-agent control?
- [ ] Can I explain the ground-plane constraint used by Polly?

---

## 📚 Key References

- Horswill, I. (1993). *Polly: A vision-based artificial agent*. Proc. AAAI-93.
- Brooks, R. (1986). *A robust layered control system for a mobile robot*. IEEE J. Robotics and Automation.
- Brooks, R. (1990). *Elephants don't play chess*. Robotics and Autonomous Systems 6.
- Raibert, M. et al. (2008). *BigDog, the rough-terrain quadruped robot*. IFAC Proceedings.
- Bajracharya, M. et al. (2008). *Autonomy for Mars rovers: Past, present, and future*. Computers 41(12).
- Reynolds, C. W. (1987). *Flocks, herds and schools: A distributed behavioral model*. Proc. SIGGRAPH.
- Tambe, M. (1997). *Agent architectures for flexible, practical teamwork*. Proc. AAAI 97.
- Hermellin, E. & Michel, F. (2017). *Complex flocking dynamics without global stimulus*. Proc. ECAL 2017.
- Antonioni, E. et al. (2021). *Game strategies for physical robot soccer players: A survey*. IEEE Trans. Games.

---

*Based on COMPSCI 713 Week 6 Lecture 12 (Instructor: Xinyu Zhang, adapted from Prof. Jim Warren).*
