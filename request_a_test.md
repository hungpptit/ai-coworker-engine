# Edtronaut AI Engineer Intern Take-Home Assignment 2.0

[cite_start]This file documents the official requirements, background context, and evaluation metrics extracted directly from Edtronaut's assignment brief and invitation email[cite: 1, 113].

---

## 📅 Timeline & Submission Details
* [cite_start]**Position:** AI Engineer Intern [cite: 2]
* [cite_start]**Time Expectation:** ~3 Days [cite: 4]
* **Deadline:** Before Monday, June 8, 2026
* [cite_start]**Submission Format:** PDF Report / Slide Deck (max 10-15 slides) + GitHub Repository Link [cite: 7, 12]
* [cite_start]**Submission Channels:** Sent to `hr@edtronaut.ai` and CC to `tram@edtronaut.ai` 

---

## 🚀 The Mission: Building the "AI Co-Worker" Engine
[cite_start]Edtronaut operates an AI-powered Job Simulation Platform designed to mirror real-world job tasks[cite: 40, 41]. [cite_start]While the current platform successfully provides rubric-based scoring and narrative feedback on student submissions [cite: 47][cite_start], the next strategic step is to enable learners to actively collaborate with **AI Co-workers and Stakeholders (NPCs)** inside the simulation[cite: 48, 49].

### The Challenge
[cite_start]Design and prototype the AI core engine behind these workplace virtual colleagues[cite: 50, 51]. [cite_start]The goal is to move beyond generic Q&A chatbots and create agents that operate with distinct **personalities, dynamic memories, hidden business constraints, and specific corporate goals**[cite: 52].

---

## 🏢 Target Simulation Context: Gucci Global Group (HRM Talent & OD)
[cite_start]To ground the technical implementation, candidates are instructed to model the engine using the **HRM Talent & Leadership Development track for Gucci Global Group**[cite: 55, 56]. 

### Case Background
[cite_start]The user joins Group HR as the Global Organization Development (OD) Director[cite: 120]. [cite_start]Nine iconic luxury brands operate with high autonomy[cite: 121]. [cite_start]The core mandate is to architect a group-wide leadership system that increases inter-brand mobility and identifies talent, but **strictly supports (does not impose on) individual brand DNA**[cite: 121, 123].

### The 3 Core AI Co-Workers in the Context:
1. [cite_start]**Gucci Group CEO:** Holds deep insights regarding group mission and culture; defends Group DNA and guides the user through autonomy vs. corporate group alignment tradeoffs[cite: 125, 143, 144].
2. [cite_start]**Gucci Group CHRO:** Focuses on talent development and boosting inter-brand mobility without suffocating brand autonomy[cite: 126, 127, 129, 130]. [cite_start]Anchors conversations around the group competency framework: *Vision, Entrepreneurship, Passion, and Trust*[cite: 131].
3. [cite_start]**Employer Branding & Regional Communications Manager:** Provides regional field insights, current operational status, and cultural challenges when rolling out the new process across branches[cite: 132, 166].

[cite_start]*(Note: Per the assignment guidelines, candidates are allowed to focus technical prototyping on **1 out of the 3 available NPCs** due to the time constraint [cite: 95]).*

---

## 📝 Required Deliverables (The 4-Part Framework)

### Part 1: Persona & Interaction Design (The Logic)
* [cite_start]**Persona Definition:** Outline system prompts and profiles for the chosen NPC, detailing hidden constraints (e.g., personality limits)[cite: 77].
* [cite_start]**Dialogue Flow:** Script examples illustrating a "Good" vs. a "Bad" interaction between the user and the NPC[cite: 79].
* [cite_start]**State Management:** Map out how the character remembers previous turns and adjusts behavior over time (e.g., how annoying the NPC in Turn 1 alters their attitude in Turn 5)[cite: 80, 81].

### Part 2: System Architecture (The Engine)
* [cite_start]**High-Level Diagram:** A visual mapping showing how the Front-End interface communicates with the Orchestration Layer and Foundation LLMs[cite: 84, 85].
* [cite_start]**Tool Use:** Implement mechanisms enabling NPCs to access mock external software applications (e.g., looking up simulation JIRA tickets or calculating KPIs)[cite: 69, 86, 87].
* [cite_start]**Latency vs. Quality:** Propose actionable mitigation strategies to maintain fast chat response times while utilizing deep retrieval pipelines (RAG)[cite: 88].

### Part 3: The "Director" Layer – Supervisor Agent (Orchestration)
* [cite_start]Propose an invisible background Supervisor Agent that monitors conversational health[cite: 91].
* [cite_start]**Scenario Handling:** If the learner becomes stuck, confused, or enters a circular conversational loop, outline how the system detects this semantic stagnation and dynamically forces the NPC to offer a subtle, in-character progress hint[cite: 92, 93].

### Part 4: Prototype & Implementation Strategy
* [cite_start]Select a production-ready tech stack (e.g., FastAPI, LangChain, LangGraph, AutoGen, Vector Databases) and justify the technical trade-offs[cite: 5, 6, 97].
* [cite_start]Provide a clean, runnable Python script or pseudo-class framework (`NPCAgent`) that processes user input messages, maintains historical session states, and handles active safety/guardrail checks[cite: 98].

---

## 📊 Core Evaluation Metrics
[cite_start]Submissions are evaluated on systemic thinking, clarity, and architectural feasibility over syntactically flawless execution[cite: 74, 100]:
1. [cite_start]**Role-Playing Fidelity:** Do the characters demonstrate consistent business functions and genuine corporate friction, or do they sound like a generic out-of-the-box LLM? [cite: 102]
2. [cite_start]**Architecture Soundness:** Is the technical infrastructure modular, modern, and easily replicable across different simulation tracks? [cite: 83, 103]
3. [cite_start]**Problem Solving & Guardrails:** Does the architecture successfully anticipate edge cases, such as unrelated conversational topics or direct malicious prompt injection (jailbreaking)? [cite: 103, 104]