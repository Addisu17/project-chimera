# Agent Rules Blueprint

## General Principles
- Planner cannot execute tasks.
- Worker cannot modify logs.
- Judge cannot create tasks.
- Escalate to human if task remains pending >24h.

## Forbidden Actions
- No agent may access sensitive user info.
- No agent may bypass task approval.

## Ambiguity Handling
- Any unclear instruction → log and escalate.
