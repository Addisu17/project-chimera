class JudgeAgent:
    def __init__(self, name="Judge"):
        self.name = name

    def review_task(self, task_result):
        """
        Decide if a task meets compliance and safety requirements
        """
        print(f"{self.name} reviewing task result...")
        # Placeholder logic: approve everything for now
        return {"approved": True, "notes": "All good"}
