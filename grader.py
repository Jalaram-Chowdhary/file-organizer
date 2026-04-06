from env import FileOrganizerEnv
class FileOrganizerGrader:
    def __init__(self):
        self.env = FileOrganizerEnv()
    def evaluate(self, task="easy"):
        state = self.env.reset(task)
        for file in state:
            ext = file.split(".")[-1]
            if ext in ["pdf", "txt"]:
                action = (file, "Documents")
            elif ext in ["mp3"]:
                action = (file, "Music")
            elif ext in ["jpg", "png"]:
                action = (file, "Images")
            else:
                action = (file, "Others")
            state, reward, done = self.env.step(action)
        correct = 0
        total = len(state)
        for file, folder in state.items():
            ext = file.split(".")[-1]
            if ext in ["pdf", "txt"] and folder == "Documents":
                correct += 1
            elif ext in ["mp3"] and folder == "Music":
                correct += 1
            elif ext in ["jpg", "png"] and folder == "Images":
                correct += 1
        score = correct / total
        return round(score, 2)
if __name__ == "__main__":
    grader = FileOrganizerGrader()
    print("Easy Score:", grader.evaluate("easy"))
    print("Medium Score:", grader.evaluate("medium"))
    print("Hard Score:", grader.evaluate("hard"))