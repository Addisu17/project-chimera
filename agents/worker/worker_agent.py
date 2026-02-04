class WorkerAgent:
    def __init__(self, name="Worker"):
        self.name = name

    def execute_task(self, task):
        """
        Simulate task execution; real implementation will call APIs via MCP
        """
        print(f"{self.name} executing task: {task['description']}")
        result = {"status": "done", "output": f"Result for {task['description']}"}
        return result
