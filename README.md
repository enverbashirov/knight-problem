# Author: Enver Bashirov

## Problem Definition: Knight Problem

Part 1: This project provides a Python script and a Dockerfile to find the minimum-length sequences of moves for a knight to travel from one cell to another on an empty chessboard. It also generates a Graphviz visualization of the "all shortest path" graph.

### Features:

- Efficient BFS algorithm to find all minimum-length paths.
- Clear output displaying all possible solution paths.
- Graphviz visualization for better understanding of the solution space.
- Dockerfile for easy deployment and execution.

### Installation:

**1. Python Script:**

- Make sure you have Python 3.11 or later installed.
- Clone this repository or download the files.
- Install required libraries:

```bash
pip install -r requirements.txt
```

- Edit `knight_problem.py` to replace `source` and `target` with your desired starting and ending cell positions (format: `<x>,<y>`).
- Run the script:

```bash
python knight_problem.py
```

**2. Docker:**

- Make sure you have Docker installed and running.
- Build the Docker image:

```bash
docker build -t docker_knight_problem .
```

- Run the container:

```bash
docker run docker_knight_problem source=<x>,<y> target=<x>,<y>
```

- Replace `<x>,<y>` with your desired source and target positions.

**Example:**

```bash
python knight_problem.py
# Output:
Minimum-length paths:
(0,0) -> (1,2) -> (2,4) -> (3,6) -> (7,7)
(0,0) -> (2,1) -> (4,2) -> (6,3) -> (7,7)
# ... (other paths)

docker run knight_path_solver source=0,0 target=7,7
# Output:
(0,0) -> (1,2) -> (2,4) -> (3,6) -> (7,7)
# ... (other paths in a Docker container)
```

