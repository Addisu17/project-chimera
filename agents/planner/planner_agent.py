class PlannerAgent:
    def __init__(self, name="Planner"):
        self.name = name

    def create_task(self, description):
        """
        Generates a task for Workers based on functional spec
        """
        task = {
            "description": description,
            "priority": "normal",
            "requires_judge": False
        }
        return task

    def dispatch_task(self, worker, task):
        """
        Send task to a worker agent
        """
        return worker.execute_task(task)
