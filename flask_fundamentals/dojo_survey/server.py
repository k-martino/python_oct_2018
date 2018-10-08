from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "Shhhhhhhh"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def submit():
    print(request.form)
    print('Name', request.form['name'])
    print('Dojo Location', request.form['location'])
    print('Favorite Language', request.form['language'])
    print('Comment', request.form['comment'])
    return render_template("result.html", )


if __name__ == "__main__":
    app.run(debug=True)
