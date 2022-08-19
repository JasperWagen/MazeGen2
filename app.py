import logging

from flask import Flask, render_template, request

from maze_generator.create_maze import create_maze

app = Flask(__name__)

logger = logging.getLogger("waitress")


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        height = int(request.form["height"])
        width = int(request.form["width"])
        path_color = request.form["path_color"]
        wall_color = request.form["wall_color"]

        try:
            with_solution = request.form["with_solution"] == "on"
        except KeyError:
            with_solution = False

        try:
            logger.info(f"Creating maze with height {height} and width {width}")
            create_maze(height, width, path_color, wall_color, with_solution)
        except Exception as e:
            logger.error(f"An error occurred when creating the maze, error: {e}")
            raise e

        return render_template(
            "index.html",
            maze_img_path="static/maze.png",
            height=height,
            width=width,
            path_color=path_color,
            wall_color=wall_color,
            with_solution=with_solution,
        )

    height, width = 100, 100
    path_color, wall_color = "#00CDCC", "#232222"
    with_solution = False

    create_maze(height, width, path_color, wall_color, with_solution)
    return render_template(
        "index.html",
        maze_img_path="static/maze.png",
        height=height,
        width=width,
        path_color=path_color,
        wall_color=wall_color,
        with_solution=with_solution,
    )
