# main.py

from agents.planner.planner_agent import PlannerAgent
from agents.worker.worker_agent import WorkerAgent
from agents.judge.judge_agent import JudgeAgent

def main():
    # Initialize agents
    planner = PlannerAgent()
    worker = WorkerAgent()
    judge = JudgeAgent()

    # Step 1: Planner creates a plan
    request = "Build a small project plan"
    tasks = [planner.create_task(request)]  # wrap in a list for iteration
    print(f"Planner generated tasks: {tasks}")

    # Step 2: Worker executes each task
    results = []
    for task in tasks:
        result = worker.execute_task(task)
        print(f"Worker executed task: {result}")
        results.append(result)

    # Step 3: Judge evaluates the results
    evaluations = []
    for result in results:
        eval_result = judge.evaluate(result)
        print(f"Judge evaluation: {eval_result}")
        evaluations.append(eval_result)

if __name__ == "__main__":
    main()
