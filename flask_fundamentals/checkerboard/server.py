from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={"x": 8, "y": 8})
@app.route('/<int:x>/<int:y>')
def checkerboard(x, y):
   return render_template("index.html", x=x, y=y)



if __name__ == "__main__":
    app.run(debug=True)
