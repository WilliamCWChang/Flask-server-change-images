from flask import Flask, render_template, url_for, send_file
import os
import random
import math
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template("summer.html", user_image='static/0.jpg')


@app.route('/get_image')
def get_image():
    filename = get_random_image()
    return render_template("summer.html", user_image=filename)


def get_random_image():
    image_list = []
    for file in os.listdir("./static"):
        if file.endswith((".jpg", ".png")):
            image_list.append(os.path.join("/static", file))

    image_index = math.floor(len(image_list) * random.random())

    return image_list[image_index]


if __name__ == "__main__":
    Bootstrap(app)
    app.run(host='0.0.0.0', port=80)
    # print(PEOPLE_FOLDER)
