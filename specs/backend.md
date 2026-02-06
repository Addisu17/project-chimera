# Backend & Agent Orchestration

## API Endpoints
- POST /tasks → create task
  - Input: {description: str, assigned_agent: str}
  - Output: {task_id: int, status: str}

- GET /tasks/:id → get task details
  - Output: {task_id, description, status, logs[]}

## Agent Workflow
1. Planner reads tasks → assigns worker.
2. Worker executes → updates logs.
3. Judge reviews → flags errors.
4. Human in the loop handles escalations.

## JSON I/O Contracts
All requests/responses are JSON, strictly validated.
