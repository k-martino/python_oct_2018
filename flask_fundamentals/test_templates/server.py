from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play", defaults={"boxes": 3, "color": "skyblue"})
@app.route("/play/<int:boxes>", defaults={"color": "skyblue"})
@app.route("/play/<int:boxes>/<color>")
def play(boxes, color):
    return render_template("index.html", boxes=boxes, color=color)


if __name__ == "__main__":
    app.run(debug=True)
