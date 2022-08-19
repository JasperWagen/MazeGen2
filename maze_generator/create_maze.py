import sys
from random import choice

import numpy as np
from PIL import ImageColor

from maze_generator.directions import Directions
from maze_generator.plot_image import plot_image
from maze_generator.solve_maze import solve_maze

sys.setrecursionlimit(8000)


def create_maze(height, width, path_color, wall_color, with_solution=False):
    """
    Create a maze with the given height and width using the recursive backtracker algorithm.
    """

    maze_array = _create_maze_array(height, width)

    rgb_path_color = ImageColor.getcolor(path_color, "RGB")
    rgb_wall_color = ImageColor.getcolor(wall_color, "RGB")

    if with_solution:
        solution = solve_maze(maze_array)
        plot_image(maze_array, rgb_path_color, rgb_wall_color, solution)
    else:
        plot_image(maze_array, rgb_path_color, rgb_wall_color)


def _create_maze_array(height, width):
    maze_array = _create_maze_grid(height, width)

    start_options = [y for y in range(maze_array.shape[0]) if y % 2 == 0][1:-1]
    start = choice(start_options)

    maze_array[start, 1] = 0.5
    maze_array = _generate(start, 2, maze_array)

    maze_array = _set_exit(maze_array)

    return maze_array


def _set_exit(maze_array):
    exit_options = []
    for i, v in enumerate(maze_array[1:-1, -3], 1):
        if v == 0.5:
            exit_options.append(i)

    exit_choice = choice(exit_options)
    maze_array[exit_choice, -2] = 0.5

    return maze_array


def _create_maze_grid(height, width):
    """
    Create an empty maze grid with the given width and height.
    """

    if height % 2 == 0:
        height += 1
    if width % 2 == 0:
        width += 1

    maze_array = np.ones((height, width), dtype=float)

    for i in range(height):
        if i % 2 == 1:
            maze_array[i, 0:width] = 0
    for j in range(width):
        if j % 2 == 1:
            maze_array[0:height, j] = 0

    (
        maze_array[0:height, 0],
        maze_array[0:height, width - 1],
        maze_array[0, 0:width],
        maze_array[height - 1, 0:width],
    ) = (0.5, 0.5, 0.5, 0.5)

    return maze_array


def _generate(current_y, current_x, maze_array):
    """
    Generates the next step in the maze
    """

    maze_array[current_y, current_x] = 0.5

    while True:
        available_directions = _get_available_directions(
            current_y, current_x, maze_array
        )

        if len(available_directions) == 0:
            break

        move = choice(available_directions)

        maze_array[current_y + move.value[0], current_x + move.value[1]] = 0.5

        _generate(
            current_y + move.value[0] * 2, current_x + move.value[1] * 2, maze_array
        )

    return maze_array


def _get_available_directions(current_y, current_x, maze_array):
    """
    Get the available directions from the current position.
    """

    available_directions = [
        d
        for d in Directions
        if maze_array[current_y + d.value[0] * 2, current_x + d.value[1] * 2] == 1
    ]

    return available_directions


if __name__ == "__main__":
    maze_array = create_maze(7, 7, "#000", "#fff", with_solution=True)
