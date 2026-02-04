# agents/judge/judge_agent.py

class JudgeAgent:
    def __init__(self, name="Judge"):
        self.name = name

    def evaluate(self, task_result):
        """
        Evaluates the result of a worker's task.
        Returns a simple pass/fail evaluation.
        """
        # For now, we can just mark everything as 'approved'
        evaluation = {
            "task_status": task_result.get("status", "unknown"),
            "approved": True,
            "notes": f"Task reviewed by {self.name}"
        }
        print(f"{self.name} evaluating task: {task_result['output']}")
        return evaluation
