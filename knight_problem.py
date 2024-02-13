import queue
from graphviz import Digraph

def valid_moves(x, y, board_size):
    # Generates all valid knight moves from a given position on the chessboard.
    moves = []
    for dx, dy in [(-2, 1), (-2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2), (2, 1), (2, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < board_size and 0 <= new_y < board_size:
            moves.append((new_x, new_y))
    return moves

def bfs(source, target, board_size):
    # Performs BFS to find all minimum-length sequences of knight moves.
    visited = set()
    parent = {}  # Track parent nodes for path reconstruction
    q = queue.Queue()
    q.put(source)
    visited.add(source)

    while not q.empty():
        curr_x, curr_y = q.get()
        for new_x, new_y in valid_moves(curr_x, curr_y, board_size):
            if (new_x, new_y) not in visited:
                q.put((new_x, new_y))
                parent[(new_x, new_y)] = (curr_x, curr_y)
                visited.add((new_x, new_y))

                if new_x == target[0] and new_y == target[1]:
                    return parent

def reconstruct_paths(parent, source, target):
    # Reconstructs all minimum-length paths from the parent dictionary.
    paths = []
    while target != source:
        paths.append(target)
        target = parent[target]
    paths.append(source)
    paths.reverse()  # Order paths from source to target
    return paths

def draw_graph(parent, source, target):
    # Creates a Graphviz visualization of the "all shortest path" graph.
    dot = Digraph("knight_paths")
    for child, parent_node in parent.items():
        child_str = f"{child[0]},{child[1]}"
        parent_str = f"{parent_node[0]},{parent_node[1]}"
        dot.node(child_str)
        dot.node(parent_str)
        dot.edge(parent_str, child_str)

    # Highlight source and target nodes
    dot.node(f"{source[0]},{source[1]}", style="filled", fillcolor="green")
    dot.node(f"{target[0]},{target[1]}", style="filled", fillcolor="red")

    return dot

if __name__ == "__main__":
    board_size = 8  # Example chessboard size
    source = (1, 6)  # Replace with actual source cell
    target = (2, 1)  # Replace with actual target cell
    # source = tuple([int(x) for x in input("Define the starting position (x, y): ").split(',')])
    # target = tuple([int(x) for x in input("Define the target position (x, y): ").split(',')])

    parent = bfs(source, target, board_size)

    if parent is None:
        print("No paths found from source to target.")
    else:
        paths = reconstruct_paths(parent, source, target)
        print("Minimum-length paths:")
        for path in paths:
            print(" -> ".join([f'{x},{y}' for x, y in paths]))

        dot = draw_graph(parent, source, target)
        dot.format = 'png'
        dot.render("knight_paths", view=False)  # Replace with preferred method
        dot.format = 'pdf'
        dot.render("knight_paths", view=False)  # Replace with preferred method
