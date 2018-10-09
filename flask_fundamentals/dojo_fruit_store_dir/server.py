from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    session = {
        'a':
        int(request.form['apple']),
        'r':
        int(request.form['raspberry']),
        'b':
        int(request.form['blackberry']),
        's':
        int(request.form['strawberry']),
        'total':
        (int(request.form['apple']) + int(request.form['raspberry']) + int(
            request.form['blackberry']) + int(request.form['strawberry'])),
        'first_name':
        request.form['first_name'],
        'last_name':
        request.form['last_name'],
        'timestamp':
        datetime.date.today(),
        'student_id':
        request.form['student_id']
    }
    return render_template("checkout.html", session=session)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)