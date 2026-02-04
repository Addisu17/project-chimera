# Project Chimera

**Project Chimera** is a simple multi-agent system demonstrating task planning, execution, and evaluation. The project uses three types of agents:

- **PlannerAgent**: Creates tasks based on a given request.
- **WorkerAgent**: Executes tasks assigned by the planner.
- **JudgeAgent**: Evaluates the results of completed tasks.

---

## Folder Structure

project-chimera/
├── agents/
│ ├── planner/
│ │ └── planner_agent.py
│ ├── worker/
│ │ └── worker_agent.py
│ └── judge/
│ └── judge_agent.py
├── main.py
├── README.md
├── pyproject.toml
├── Dockerfile
├── Makefile
└── .meta.md


---

## How to Run

1. Make sure you are in the project root directory.
2. Run the main program using Python:

```bash
python main.py
