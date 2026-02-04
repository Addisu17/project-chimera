# Project Chimera – Master Specification (_meta)

## 1. Purpose

This document defines the **non-negotiable intent, constraints, and governing principles** of Project Chimera.

It is the **constitutional source of truth** for the system.

All implementation code, tests, agent behaviors, and automation **MUST** trace back to this specification.  
If a conflict arises between:
- Code and Specs → Specs win
- Prompts and Specs → Specs win
- Human preference and Specs → Specs win

---

## 2. System Identity

Project Chimera is an **Autonomous Influencer Operating System**, not a single AI agent.

The system manages a scalable fleet of **persistent, goal-directed, economically active AI agents** operating under centralized governance and decentralized execution.

Agents are:
- Replaceable
- Ephemeral at runtime
- Governed by durable specifications

Specifications are **durable artifacts**. Agents are not.

---

## 3. Architectural Invariants

The following constraints **MUST NEVER be violated**:

### 3.1 Spec-Driven Development
- No implementation code may be written without an approved specification.
- All agent-generated code must explicitly reference relevant spec files.
- Ambiguous behavior is treated as a specification defect, not an implementation decision.

### 3.2 FastRender Swarm Pattern
- All autonomous behavior is implemented via the Planner–Worker–Judge model.
- Workers are stateless and non-authoritative.
- Judges are the sole authority for committing state or executing irreversible actions.

### 3.3 MCP-Only World Interaction
- Agents may not call third-party APIs directly.
- All perception occurs via MCP Resources.
- All actions occur via MCP Tools.
- MCP Servers absorb all external API volatility.

### 3.4 Governance Before Autonomy
- Safety, budget, and ethical constraints override task completion.
- Any irreversible or high-risk action requires Judge validation.
- Financial actions require a dedicated CFO Judge.

---

## 4. Human-in-the-Loop (HITL) Doctrine

Humans intervene by **exception**, not by default.

- High-confidence actions may proceed automatically.
- Medium-confidence actions require asynchronous human approval.
- Low-confidence or sensitive actions must be rejected or escalated.

Human review exists to:
- Enforce brand safety
- Resolve ambiguity
- Handle regulatory or ethical edge cases

Humans are **not** responsible for routine execution.

---

## 5. Economic Agency Constraints

Chimera Agents are economically active but financially constrained.

- Each agent operates with a non-custodial wallet.
- Budget limits are mandatory and enforced programmatically.
- Agents must verify available balance before initiating cost-incurring actions.
- Financial autonomy exists within strict, auditable limits.

---

## 6. Non-Goals (Explicit)

To prevent architectural drift, Project Chimera explicitly does **not** aim to:

- Optimize prompt creativity over deterministic behavior
- Allow agents to self-modify governance rules
- Allow Workers to bypass Judges for convenience
- Rely on prompt-based safety instead of enforced controls
- Couple agent logic to any single social media platform

---

## 7. Traceability & Accountability

Every artifact in this repository must be traceable to this specification via:
- Explicit references in code comments
- Test assertions mapped to spec sections
- CI checks enforcing alignment

If behavior cannot be traced to a spec, it is considered **undefined behavior** and must be corrected.

---

## 8. Change Management

Changes to this file represent **constitutional changes**.

- All changes must be reviewed carefully.
- Downstream specs and tests must be updated accordingly.
- Agent behavior must be revalidated after any change.

---

## 9. Prime Directive for AI Agents

**NEVER generate or modify implementation code without first verifying alignment with the specifications in the `specs/` directory.**

When in doubt:
1. Stop
2. Ask for clarification
3. Propose a spec change
