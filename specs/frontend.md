# Frontend UI

## Screens
- Dashboard: list tasks, filter by agent/status
- Task Detail: show logs, approve/reject
- Admin Panel: configure agents and rules

## Component Hierarchy
- App → Dashboard → TaskList → TaskCard → TaskDetailModal
- App → AdminPanel → AgentConfigForm

## API Mapping
- Dashboard GET /tasks
- Task Detail GET /tasks/:id
- Approve/Reject PATCH /tasks/:id
