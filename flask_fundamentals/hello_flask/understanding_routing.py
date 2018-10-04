from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def say(name):
    if name == "john":
        return "Hi " + name.title() + "!"
    return "Hi " + name.title()


@app.route('/repeat/<num>/<string>')
def repeat(num, string):
    return string * int(num)

if __name__ == "__main__":
    # If __name__ is "__main__" we know we are running this file directly and
    # not importing it from a different module
    app.run(debug=True)  # Run the app in debug mode.
