from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "Shhhhhhhh"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def submit():
    return render_template("result.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])

@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We have redirected the user to /.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
