TITLE: Smart File Organizer

About:
This is a simple AI environment where an agent organizes files into correct folders like Documents, Music, and Images.

Goal:
The agent must place each file into the correct folder based on its type.
Example:
- pdf -> Documents
- mp3 -> Music
- jpg/png -> Images

How it works?
>State : Shows where each file is currently stored.
>Actions : Move a file to a folder
           (file_name, folder_name)
>Reward :
 - +1 -> correct move
 - -1 ->wrong move
 - +5 -> all files correct

Task:
- Easy -> 3 files
- Medium -> 5 files
- Hard -> 8 files

Score:
Score=correct files / total files
Range:0.0 to 1.0

How to Run?
Run this command : python inference.py

Files are :
- env.py -> environment
- grader.py -> scoring
- inference.py ->  runs everything
- openenv.yaml -> config
- Dockerfile ->container setup
