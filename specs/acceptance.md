# Acceptance Criteria (Gherkin)

## Task Creation
Given a new task payload
When POST /tasks
Then task is created with status "pending"

## Agent Execution
Given a pending task
When worker executes
Then AgentLogs updated with action details

## Judge Review
Given a completed task
When judge reviews
Then approval or rejection recorded
