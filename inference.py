from grader import FileOrganizerGrader
def run_inference():
    grader = FileOrganizerGrader()
    tasks = ["easy", "medium", "hard"]
    results = {}
    print("Running Inference...\n")
    for task in tasks:
        score = grader.evaluate(task)
        results[task] = score
        print(f"Task: {task} | Score: {score}")
    print("\nFinal Results:")
    for task, score in results.items():
        print(f"{task}: {score}")
    return results
if __name__ == "__main__":
    run_inference()