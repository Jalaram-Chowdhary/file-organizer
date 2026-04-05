import random
class FileOrganizerEnv:
    def __init__(self):
        self.file_types = {
            "pdf": "Documents",
            "txt": "Documents",
            "mp3": "Music",
            "jpg": "Images",
            "png": "Images"
        }
        self.reset()
    def reset(self, task="easy"):
        if task == "easy":
            self.files = ["resume.pdf", "song.mp3", "photo.jpg"]
        elif task == "medium":
            self.files = ["resume.pdf", "song.mp3", "photo.jpg", "notes.txt", "image.png"]
        else:
            self.files = [
                "resume_final.pdf", "song1.mp3", "pic1.jpg",
                "notes.txt", "image.png", "track.mp3",
                "doc.pdf", "photo2.jpg"
            ]
        self.file_locations = {file: "Unsorted" for file in self.files}
        return self.state()
    def state(self):
        return self.file_locations
    def step(self, action):
        file, folder = action
        self.file_locations[file] = folder
        ext = file.split(".")[-1]
        correct_folder = self.file_types.get(ext, "Others")
        if folder == correct_folder:
            reward = 1
        else:
            reward = -1
        done = all(
            self.file_locations[f] == self.file_types.get(f.split(".")[-1], "Others")
            for f in self.files
        )
        if done:
            reward += 5
        return self.state(), reward, done
if __name__ == "__main__":
    env = FileOrganizerEnv()
    state = env.reset("easy")
    print("Initial State:", state)
    actions = [
        ("resume.pdf", "Documents"),
        ("song.mp3", "Music"),
        ("photo.jpg", "Images")
    ]
    for action in actions:
        state, reward, done = env.step(action)
        print(state, reward)
    print("Done:", done)