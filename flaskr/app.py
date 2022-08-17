from flask import Flask, render_template, request

from maze_generator.create_maze import create_maze

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        height = int(request.form['height'])
        width = int(request.form['width'])
        create_maze(height, width)
        return render_template('index.html', maze_img_path="static/hello.png")

    return render_template("index.html")