from maze_generator.directions import Directions


def solve_maze(maze_array):
    """
    Solves the maze using depth first search.
    """

    finish = [
        (i, maze_array.shape[1] - 2)
        for i, v in enumerate(maze_array[1:-1, -2], 1)
        if v == 0.5
    ]
    start = [(i, 1) for i, v in enumerate(maze_array[1:-1, 1], 1) if v == 0.5]

    path = start
    visited = set(path)

    path = _dfs(visited, path, maze_array, finish[0])
    path.append(finish[0])

    return path


def _dfs(visited, path, maze_array, finish):
    while True:
        node = path[-1]
        if node == finish:
            return path

        available_directions = [
            d.value
            for d in Directions
            if _node_not_visited(node, visited, d, maze_array)
        ]

        if len(available_directions) == 0:
            path.pop()
            continue

        next_node = (
            node[0] + available_directions[0][0],
            node[1] + available_directions[0][1],
        )
        path.append(next_node)
        visited.add(next_node)


def _node_not_visited(node, visited, d, maze_array):
    node_y = node[0] + d.value[0]
    node_x = node[1] + d.value[1]
    if maze_array[node_y, node_x] == 0.5:
        if (node_y, node_x) not in visited:
            return True
    return False
