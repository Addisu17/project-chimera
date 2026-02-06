# Database & Data Management

## DB Choice
PostgreSQL for structured project data, Redis for caching high-velocity metadata.

## Schemas
- Users(user_id, name, role)
- Tasks(task_id, description, status, assigned_agent)
- AgentLogs(log_id, agent_type, action, timestamp)

## Relationships
- 1:N: User → Tasks
- 1:N: Task → AgentLogs

## Data Flow
1. Task created via frontend → stored in Tasks table.
2. Agent reads task → logs in AgentLogs.
3. Redis caches high-frequency metrics.
