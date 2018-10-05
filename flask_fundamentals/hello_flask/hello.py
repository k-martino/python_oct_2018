from flask import Flask, render_template

app = Flask(__name__)
# Global variable __name__ tells Flask whether or not we are running the file
# directly, or importing it as a module.


@app.route("/")
def hello_world():
    return render_template(
        "index.html", first_name="Kristen", last_name="Martino", list=[1, 3, 5]
    )


if __name__ == "__main__":
    # If __name__ is "__main__" we know we are running this file directly and
    # not importing it from a different module
    app.run(debug=True)
