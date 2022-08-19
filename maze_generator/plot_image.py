import numpy as np
from PIL import Image, ImageColor


def plot_image(
    maze_array, path_color=(255, 255, 255), wall_color=(0, 0, 0), solution=None
):
    """
    Plot an image based on a maze array.
    """

    img_array = np.zeros((maze_array.shape[0], maze_array.shape[1], 3), dtype=np.uint8)
    for i in range(maze_array.shape[0]):
        for j in range(maze_array.shape[1]):
            if maze_array[i, j] == 0.5:
                img_array[i, j] = path_color
            elif maze_array[i, j] == 0:
                img_array[i, j] = wall_color

    if solution:
        for i in solution:
            img_array[i[0], i[1]] = (255, 0, 0)

    img = Image.fromarray(img_array, "RGB")
    img.save("static/maze.png")
