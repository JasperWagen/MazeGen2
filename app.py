from flask import Flask, render_template, request
from maze_generator.create_maze import create_maze

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        height = int(request.form["height"])
        width = int(request.form["width"])
        path_color = request.form["path_color"]
        wall_color = request.form["wall_color"]
        create_maze(height, width, path_color, wall_color)

        return render_template(
            "index.html",
            maze_img_path="static/hello.png",
            height=height,
            width=width,
            path_color=path_color,
            wall_color=wall_color,
        )

    height, width = 100, 100
    path_color, wall_color = "#00CDCC",  "#232222"
    create_maze(height, width, path_color, wall_color)
    return render_template(
        "index.html", maze_img_path="static/hello.png", height=height, width=width, path_color=path_color, wall_color=wall_color
    )
