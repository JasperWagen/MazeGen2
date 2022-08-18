from maze_generator.directions import Directions

def solve_maze(maze_array):
    """
    Solves the maze using depth first search.
    """

    finish = [(i, maze_array.shape[1]-1) for i, v in enumerate(maze_array[1:-1, -2], 1) if v == 0.5]
    print(finish)
    start = [(i, 1) for i, v in enumerate(maze_array[1:-1, 1], 1) if v == 0.5]
    path = start
    visited = set(path + finish)
    node = path[0]

    path = dfs(visited, path, maze_array, node)
    path.append(finish[0])
    return path

def dfs(visited, path, maze_array, node):
    while True:
        available_directions = [d.value for d in Directions if _node_not_visited(node, visited, d, maze_array)]
        if len(available_directions) == 0:
            path.pop()
            break

        node = (node[0] + available_directions[0][0], node[1] + available_directions[0][1])
        path.append(node)
        visited.add(node)
        # print(f"{node=}\n{visited=}\n{available_directions=}, {available_directions[0]=} \n\n")
        return dfs(visited, path, maze_array, node)
    return path

def _node_not_visited(node, visited, d, maze_array):
    node_y = node[0] + d.value[0]
    node_x = node[1] + d.value[1]
    if maze_array[node_y, node_x] == 0.5:
        if (node_y, node_x) not in visited:
            return True
    return False
