# Project Chimera – Functional Specification

## 1. Overview

This document defines the **functional behavior** of Project Chimera agents and subsystems.  
It translates constitutional principles (_meta.md) into actionable specifications.

- Defines user stories and use cases
- Assigns responsibilities to Planners, Workers, and Judges
- Establishes economic and HITL flows

---

## 2. User Stories

### 2.1 Social Media Trend Detection
**As a** Planner agent,  
**I want** to detect emerging social media trends across multiple platforms,  
**So that** Workers can generate relevant content in a timely manner.

### 2.2 Autonomous Content Generation
**As a** Worker agent,  
**I want** to generate social media content aligned with trending topics,  
**So that** posts maximize engagement while obeying brand safety rules.

### 2.3 HITL Verification
**As a** Judge agent,  
**I want** to approve or reject content flagged as sensitive,  
**So that** all published content aligns with ethical and regulatory standards.

### 2.4 Economic Management
**As a** CFO Judge,  
**I want** to approve cost-incurring actions,  
**So that** agents operate within defined budget constraints.

---

## 3. Agent Responsibilities

| Agent Type | Responsibilities |
|------------|-----------------|
| Planner    | Trend detection, task orchestration, workflow planning |
| Worker     | Stateless execution, content generation, API interactions via MCP |
| Judge      | Safety, quality, and budget enforcement, irreversible action approval |
| CFO Judge  | Financial validation and audit |

---

## 4. Interaction Patterns

### 4.1 Planner → Worker
- Planner dispatches task with structured prompt
- Worker executes task using MCP resources
- Worker returns results to Planner

### 4.2 Worker → Judge
- If task is high-risk or flagged by Planner, Worker submits to Judge
- Judge validates compliance with `_meta.md` rules
- Judge approves/rejects or escalates to human

### 4.3 Planner → Judge
- Planner may request Judge validation for sensitive trends or ambiguous content
- Judge ensures adherence to budget, safety, and governance

---

## 5. Constraints & Rules

- Workers may never bypass Judges
- All budget-sensitive actions require CFO Judge approval
- Agents must log all actions for traceability
- Ambiguous tasks default to human escalation
- API calls only via MCP layer

---

## 6. Traceability

Each functional requirement **must** reference `_meta.md` section:

- Trend detection → `_meta.md §3.2 FastRender Swarm Pattern`
- HITL → `_meta.md §4 Human-in-the-Loop Doctrine`
- Budget control → `_meta.md §5 Economic Agency Constraints`

---

## 7. Non-Functional Requirements

- System must be horizontally scalable
- Logging and audit must be persistent and tamper-proof
- Response latency < 1s for internal agent communication
- All AI-generated content must be deterministic given same input and spec
