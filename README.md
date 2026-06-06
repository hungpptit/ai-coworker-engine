# AI Co-Worker NPC Engine (Edtronaut Technical Assignment)

[cite_start]This repository contains the technical prototype implementation for the **AI Co-Worker Engine**, designed as part of the AI Engineer Intern take-home assignment for Edtronaut[cite: 1, 2, 3]. 

[cite_start]The engine powers dynamic, stateful, and mission-driven Non-Player Characters (NPCs) inside workplace simulation tracks to help learners practice cross-functional collaboration and business problem-solving[cite: 48, 51, 52, 54].

---

## 🎯 Case Context: Gucci Group Global CHRO

[cite_start]This specific implementation pilots the **HRM Talent & Leadership Development simulation for Gucci Global Group**[cite: 53, 56]. [cite_start]It focuses heavily on the **Global CHRO Persona**[cite: 63, 95].

* [cite_start]**The Mission:** The simulation taker acts as the Global OD Director [cite: 120] [cite_start]and must architect a group-wide leadership framework[cite: 123].
* [cite_start]**The Challenge:** The CHRO NPC is programmed to evaluate the user based on boosting inter-brand mobility [cite: 63, 65] [cite_start]while strictly defending individual brand autonomy (preventing forced centralized compliance that dilutes unique brand DNA)[cite: 62, 63, 66].
* [cite_start]**Core Pillars:** All solutions must align with the group competency matrix: *Vision, Entrepreneurship, Passion, and Trust*[cite: 63, 67].

---

## 🛠️ Repository Architecture

[cite_start]The project is structured modularly following enterprise-grade production patterns to ensure scalability across multiple distinct simulation tracks[cite: 58, 83]:

```text
ai-coworker-engine/
├── app/
│   ├── agents/
│   │   ├── chro_agent.py          # Core CHRO NPC Behavior & State Mutation Logic
│   │   └── director_agent.py      # Background Supervisor Layer (Deadlock Detection)
│   ├── prompts/
│   │   └── system_instructions.py # Production-grade System Instruction / Persona Prompt
│   ├── graph.py                   # Simulated Agentic Dialogue Flow Routing
│   └── main.py                    # FastAPI Web Application & Request API Gateway
├── README.md                      # Project Documentation & Execution Guide